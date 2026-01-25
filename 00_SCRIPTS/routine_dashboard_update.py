import datetime
import os
import re
import json
import sys

# Ensure local imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from GOOGLE.google_auth import get_service

# Pfade definieren (Relativ zu 00_SCRIPTS)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
DASHBOARD_PATH = os.path.join(ROOT_DIR, "01_Andreas", "01_DASHBOARD", "DASHBOARD_ZENTRALE.md")
FINANCE_PATH = os.path.join(ROOT_DIR, "14_TRADING", "02_DATA", "banking_snapshot.json")
PORTFOLIO_PATH = os.path.join(ROOT_DIR, "14_TRADING", "02_DATA", "portfolio_snapshot.json")

def get_stats():
    # --- Fitness Data ---
    today_data = {
        "steps": 0, "calories": 0, "distance": 0, "heart_minutes": 0, "active_minutes": 0,
        "avg_heart_rate": 0, "body_fat": 0, "oxygen_saturation": 0, "hydration": 0
    }
    total_steps = 0
    avg_current = 0
    remaining_today_avg = 0
    now_dt = datetime.datetime.now()

    try:
        service = get_service('fitness', 'v1')
        start_of_month = now_dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        
        body = {
            "aggregateBy": [
                {"dataTypeName": "com.google.step_count.delta"},
                {"dataTypeName": "com.google.calories.expended"},
                {"dataTypeName": "com.google.heart_minutes"},
                {"dataTypeName": "com.google.active_minutes"},
                {"dataTypeName": "com.google.heart_rate.bpm"},
                {"dataTypeName": "com.google.body.fat.percentage"},
                # {"dataTypeName": "com.google.oxygen_saturation"}, # 403 Forbidden
                # {"dataTypeName": "com.google.hydration"} # 403 Forbidden
            ],
            "bucketByTime": { "durationMillis": 86400000 },
            "startTimeMillis": int(start_of_month.timestamp() * 1000),
            "endTimeMillis": int(now_dt.timestamp() * 1000)
        }
        
        response = service.users().dataset().aggregate(userId="me", body=body).execute()
        
        today_str = now_dt.strftime('%Y-%m-%d')
        
        for bucket in response.get('bucket', []):
            start_ts = int(bucket['startTimeMillis']) / 1000
            date_str = datetime.datetime.fromtimestamp(start_ts).strftime('%Y-%m-%d')
            
            day_steps = 0
            day_calories = 0
            day_heart_pts = 0
            day_active = 0
            day_bpm_sum = 0
            day_bpm_count = 0
            day_body_fat = 0
            day_oxygen = 0
            day_hydration = 0

            for dataset in bucket.get('dataset', []):
                dtype = dataset.get('dataSourceId', '')
                for point in dataset.get('point', []):
                    for value in point.get('value', []):
                        val = value.get('intVal') if value.get('intVal') is not None else value.get('fpVal', 0)
                        
                        if "step_count" in dtype: day_steps += val
                        elif "calories" in dtype: day_calories += val
                        elif "heart_minutes" in dtype: day_heart_pts += val
                        elif "active_minutes" in dtype: day_active += val
                        elif "heart_rate" in dtype: 
                            if val > 0:
                                day_bpm_sum += val
                                day_bpm_count += 1
                        elif "body.fat" in dtype: day_body_fat = val
                        elif "oxygen_saturation" in dtype: day_oxygen = val
                        elif "hydration" in dtype: day_hydration += val

            total_steps += day_steps
            if date_str == today_str:
                avg_hr = day_bpm_sum / day_bpm_count if day_bpm_count > 0 else 0
                today_data.update({
                    "steps": day_steps, 
                    "calories": day_calories, 
                    "heart_minutes": day_heart_pts, 
                    "active_minutes": day_active,
                    "avg_heart_rate": avg_hr,
                    "body_fat": day_body_fat,
                    "oxygen_saturation": day_oxygen,
                    "hydration": day_hydration
                })

        days_passed = now_dt.day
        avg_current = total_steps / days_passed
        remaining_today_avg = max(0, (days_passed * 10000) - (total_steps - today_data["steps"]) - today_data["steps"])
    except Exception as e:
        print(f"⚠️ Warnung: Fitness-Daten konnten nicht geladen werden ({e}). Fahre fort...")

    # --- Finance Data ---
    finance_stats = ""
    try:
        if os.path.exists(FINANCE_PATH):
            with open(FINANCE_PATH, 'r', encoding='utf-8') as f:
                fin_data = json.load(f)
            nw = fin_data['net_worth_history'][-1]['Total_Net_Worth']
            cash = fin_data.get('sparkasse_balance', 0) + fin_data.get('revolut_balance', 0) + fin_data.get('comdirect_balance', 0)
            finance_stats += f"- **Net Worth:** {nw:,.2f} €\n"
            finance_stats += f"- **Liquidität:** {cash:,.2f} €\n"
        
        if os.path.exists(PORTFOLIO_PATH):
            with open(PORTFOLIO_PATH, 'r', encoding='utf-8') as f:
                port = json.load(f)
            res = port['cash']['result']
            finance_stats += f"- **Portfolio:** {'📈' if res >= 0 else '📉'} {port['cash']['invested']+res:,.2f} € ({'+' if res >= 0 else ''}{res:,.2f} €)\n"
    except:
        finance_stats = "- Finanzdaten aktuell nicht verfügbar."

    return {
        "today": today_data,
        "avg_steps": int(avg_current),
        "total_steps": total_steps,
        "remaining_avg": int(remaining_today_avg),
        "finance": finance_stats,
        "last_update": now_dt.strftime('%H:%M Uhr')
    }

def update_dashboard(stats):
    if not os.path.exists(DASHBOARD_PATH): return

    with open(DASHBOARD_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Icons & Formatting
    hr_str = f"{int(stats['today']['avg_heart_rate'])} bpm" if stats['today']['avg_heart_rate'] > 0 else "n/a"
    fat_str = f"{stats['today']['body_fat']:.1f}%" if stats['today']['body_fat'] > 0 else "n/a"
    # oxy_str = f"{stats['today']['oxygen_saturation']:.1f}%" if stats['today']['oxygen_saturation'] > 0 else "n/a"
    # hydro_str = f"{stats['today']['hydration']:.1f} L"

    stats_block = f"""
## 📊 Live-Metriken
**Fitness (Google Fit):**
- **Schritte:** {stats['today']['steps']:,} / 10.000 (Schnitt: {stats['avg_steps']:,})
- **Kcal:** {int(stats['today']['calories']):,} (Ziel: 3.000)
- **Gesundheit:** ❤️ {hr_str}
- **Körper:** {fat_str} Fett (Limit: 20%)

**Finanzen (Banking):**
{stats['finance']}
*Zuletzt aktualisiert: {stats['last_update']}*
"""

    header_pattern = r"## 📊 Live-Metriken.*?(?=\n##|---|$) "
    if re.search(header_pattern, content, re.DOTALL):
        new_content = re.sub(header_pattern, stats_block.strip(), content, flags=re.DOTALL)
    else:
        new_content = content + "\n" + stats_block

    with open(DASHBOARD_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Dashboard erfolgreich aktualisiert!")

if __name__ == "__main__":
    try:
        data = get_stats()
        update_dashboard(data)
    except Exception as e:
        print(f"Fehler: {e}")
