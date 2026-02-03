import json
import os
import datetime
import calendar
import sys
import shutil

# --- IMPORT GOOGLE AUTH ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "00_SCRIPTS"))
sys.path.append(SCRIPTS_DIR)

try:
    from GOOGLE.google_auth import get_service
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False
    print("⚠️ Google Auth Module not found. Running in manual mode.")

# --- CONFIGURATION ---
DATA_FILE = os.path.join(CURRENT_DIR, "habit_data.json")
BACKUP_FILE = os.path.join(CURRENT_DIR, "habit_data.json.bak")
# Root Dashboard for quick access
ROOT_DASHBOARD = os.path.join(CURRENT_DIR, "DASHBOARD_HABITS.md")

# TRACKERS with AUTO-CHECK Rules
TRACKERS = [
    # MORNING ROUTINE (05:00 - 08:00)
    {"id": "rise_5am", "name": "WAKE UP 5 AM", "type": "habit", "goal": "Daily", "auto": None, "time": "05:00"},
    {"id": "make_bed", "name": "MAKE BED", "type": "habit", "goal": "Daily", "auto": None, "time": "05:05"},
    {"id": "electrolytes", "name": "DRINK ELECTROLYTES", "type": "habit", "goal": "Daily", "auto": None, "time": "05:10"},
    {"id": "vitamins", "name": "TAKE VITAMINS", "type": "habit", "goal": "Daily", "auto": None, "time": "05:15"},
    {"id": "cold_shower", "name": "COLD SHOWER", "type": "habit", "goal": "Daily", "auto": None, "time": "05:20"},
    {"id": "beard", "name": "GROOM BEARD", "type": "habit", "goal": "Daily", "auto": None, "time": "05:30"},
    {"id": "bible", "name": "READ BIBLE", "type": "habit", "goal": "Daily", "auto": None, "time": "06:00"},
    {"id": "meditate", "name": "MEDITATION", "type": "habit", "goal": "Daily", "auto": None, "time": "06:15"},
    {"id": "journal", "name": "JOURNALING", "type": "habit", "goal": "Daily", "auto": None, "time": "06:30"},
    {"id": "planning", "name": "DAILY PLANNING", "type": "habit", "goal": "Daily", "auto": None, "time": "06:45"},
    {"id": "dream_journal", "name": "DREAM JOURNAL", "type": "habit", "goal": "Daily", "auto": None, "time": "07:00"},
    {"id": "spanish", "name": "LEARN SPANISH", "type": "habit", "goal": "Daily", "auto": None, "time": "07:30"},

    # DAY / EVENING (12:00 - 22:00)
    {"id": "fasting", "name": "INTERMITTENT FASTING", "type": "habit", "goal": "Daily", "auto": None, "time": "12:00"},
    {"id": "training", "name": "GYM WORKOUT", "type": "habit", "goal": "3x/Week", "auto": "heart_minutes", "threshold": 40, "time": "17:00"},
    {"id": "jogging", "name": "JOGGING", "type": "habit", "goal": "2x/Week", "auto": None, "time": "17:30"},
    {"id": "tea", "name": "DRINK TEA", "type": "habit", "goal": "Daily", "auto": None, "time": "20:00"},
    {"id": "reading", "name": "READING", "type": "habit", "goal": "Daily", "auto": None, "time": "21:00"},
    {"id": "stretching", "name": "STRETCHING", "type": "habit", "goal": "Daily", "auto": None, "time": "21:30"},
    {"id": "steps", "name": "10K STEPS", "type": "habit", "goal": "Daily", "auto": "steps", "threshold": 10000, "time": "22:00"},

    # DETOX / 24H (Sorted at End)
    {"id": "corn", "name": "NO PORN/MASTURBATION", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H"},
    {"id": "coffee", "name": "NO COFFEE", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H"},
    {"id": "weed", "name": "NO WEED", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H"},
    {"id": "games", "name": "NO VIDEO GAMES", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H"},
    {"id": "melatonin", "name": "NO MELATONIN", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H"},
    {"id": "youtube", "name": "NO YOUTUBE", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H"}
]

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"history": {}, "streaks": {}, "best_streaks": {}}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if "best_streaks" not in data: data["best_streaks"] = {}
            return data
    except:
        return {"history": {}, "streaks": {}, "best_streaks": {}}

def save_data(data):
    # Create Backup before saving
    if os.path.exists(DATA_FILE):
        try:
            shutil.copyfile(DATA_FILE, BACKUP_FILE)
        except Exception as e:
            print(f"⚠️ Backup failed: {e}")
            
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_date_str(days_offset=0):
    return (datetime.date.today() - datetime.timedelta(days=days_offset)).strftime("%Y-%m-%d")

def ask_user(prompt):
    while True:
        choice = input(f"{prompt} (y/n): ").lower().strip()
        if choice in ['y', 'yes', 'j', 'ja', '1']: return True
        if choice in ['n', 'no', 'nein', '0']: return False

def fetch_google_fit_data(target_date_str):
    if not GOOGLE_AVAILABLE: return {}
    try:
        service = get_service('fitness', 'v1')
        target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d")
        start_ts = int(target_date.replace(hour=0, minute=0, second=0).timestamp() * 1000)
        end_ts = int(target_date.replace(hour=23, minute=59, second=59).timestamp() * 1000)
        body = {
            "aggregateBy": [
                {"dataTypeName": "com.google.calories.expended"},
                {"dataTypeName": "com.google.heart_minutes"},
                {"dataTypeName": "com.google.step_count.delta"}
            ],
            "bucketByTime": {"durationMillis": 86400000},
            "startTimeMillis": start_ts,
            "endTimeMillis": end_ts
        }
        dataset_res = service.users().dataset().aggregate(userId="me", body=body).execute()
        calories = 0
        heart_minutes = 0
        steps = 0
        for bucket in dataset_res.get('bucket', []):
            for ds in bucket.get('dataset', []):
                dtype = ds.get('dataSourceId', '')
                for p in ds.get('point', []):
                    for v in p.get('value', []):
                        val = v.get('intVal') if v.get('intVal') is not None else v.get('fpVal', 0)
                        if "calories" in dtype: calories += val
                        if "heart_minutes" in dtype: heart_minutes += val
                        if "step_count" in dtype: steps += val
        prev_noon = (target_date - datetime.timedelta(days=1)).replace(hour=12)
        target_noon = target_date.replace(hour=12)
        sleep_res = service.users().sessions().list(userId="me", startTime=prev_noon.isoformat() + "Z", endTime=target_noon.isoformat() + "Z", activityType=[72]).execute()
        sleep_hours = 0.0
        for sess in sleep_res.get('session', []):
            s = int(sess['startTimeMillis'])
            e = int(sess['endTimeMillis'])
            sleep_hours += (e - s) / 1000 / 3600
        return {"calories_burned": calories, "heart_minutes": heart_minutes, "steps": steps, "sleep_hours": sleep_hours}
    except: return {}

def calculate_streaks(history, best_streaks_data):
    current_streaks = {t["id"]: 0 for t in TRACKERS}
    today = datetime.date.today()
    for t in TRACKERS:
        tid = t["id"]
        current = 0
        for i in range(365):
            d = today - datetime.timedelta(days=i)
            d_str = d.strftime("%Y-%m-%d")
            if d_str not in history:
                if i == 0: continue
                else: break
            if history[d_str].get(tid) is True: current += 1
            else: break
        current_streaks[tid] = current
        if current > best_streaks_data.get(tid, 0): best_streaks_data[tid] = current
    return current_streaks, best_streaks_data

def run_tracker():
    data = load_data()
    is_evening = datetime.datetime.now().hour >= 20
    target_date_str = get_date_str(0) if is_evening else get_date_str(1)
    
    print(f"\n⚡ PERFORMANCE CHECK: {target_date_str} ⚡")
    print("---------------------------------------")
    auto_data = fetch_google_fit_data(target_date_str)

    if target_date_str in data["history"]:
        print("✅ Data for this date already exists.")
        if not ask_user("Overwrite?"):
            generate_dashboard(data)
            return

    day_entry = {}
    print("\n--- 🔨 EXECUTION ---")
    
    # Sort trackers by time for the execution flow as well
    sorted_trackers = sorted(TRACKERS, key=lambda x: x["time"])
    
    for t in sorted_trackers:
        success = None
        if t["auto"] and t["auto"] in auto_data:
            val = auto_data[t["auto"]]
            if val >= t["threshold"]: success = True
        if success is None:
            q = f"Did you execute: {t['name']}?" if t["type"] == "habit" else f"Did you stay CLEAN from: {t['name']}?"
            success = ask_user(q)
        day_entry[t["id"]] = success

    data["history"][target_date_str] = day_entry
    curr, best = calculate_streaks(data["history"], data.get("best_streaks", {}))
    data["streaks"] = curr
    data["best_streaks"] = best
    save_data(data)
    generate_dashboard(data)

def generate_dashboard(data):
    today = datetime.date.today()
    year = today.year
    month = today.month
    month_name = today.strftime('%B').upper()
    
    month_folder_name = f"{year}_{month:02d}_{month_name}"
    month_folder_path = os.path.join(CURRENT_DIR, month_folder_name)
    if not os.path.exists(month_folder_path): os.makedirs(month_folder_path)
    monthly_dashboard_path = os.path.join(month_folder_path, f"DASHBOARD_{month_name}_{year}.md")

    # --- PERFORMANCE CALCULATIONS ---
    def get_day_score(d_str):
        entry = data["history"].get(d_str, {})
        if not entry: return 0
        return sum(1 for t in TRACKERS if entry.get(t["id"]) is True)

    today_str = get_date_str(0)
    yesterday_str = get_date_str(1)
    
    today_score = get_day_score(today_str)
    yesterday_score = get_day_score(yesterday_str)
    
    # 1% Better logic: Success rate today vs yesterday
    daily_diff = ((today_score - yesterday_score) / len(TRACKERS) * 100) if len(TRACKERS) > 0 else 0
    daily_status = "🚀 IMPROVING" if daily_diff > 0 else "📉 DECLINING" if daily_diff < 0 else "⚖️ STABLE"

    def get_monthly_perf(y, m):
        success = 0
        total = 0
        for d_str, entries in data["history"].items():
            if d_str.startswith(f"{y}-{m:02d}"):
                for t in TRACKERS:
                    if entries.get(t["id"]): success += 1
                    total += 1
        return (success / total * 100) if total > 0 else 0.0

    current_perf = get_monthly_perf(year, month)
    prev_date = today.replace(day=1) - datetime.timedelta(days=1)
    prev_perf = get_monthly_perf(prev_date.year, prev_date.month)
    month_diff = current_perf - prev_perf

    # --- BUILD CONTENT ---
    content = f"# 📊 PERFORMANCE DASHBOARD - {month_name} {year}\n\n"
    
    # KPI Section
    content += "## 📈 KEY PERFORMANCE INDICATORS\n"
    content += f"- **Monthly Performance:** {current_perf:.1f}% (Month-to-Month: {month_diff:+.1f}%)\n"
    content += f"- **Daily Trend:** {daily_status} ({daily_diff:+.1f}% vs Yesterday)\n"
    content += f"- **Daily Score:** {today_score}/{len(TRACKERS)} Missions completed\n\n"
    
    content += "## 🔥 CURRENT STREAKS\n\n"
    content += "| MISSION | TIME | STREAK | BEST | STATUS |\n|:---|:---:|:---:|:---:|:---:|\n"
    
    # SORT TRACKERS FOR DASHBOARD
    sorted_trackers = sorted(TRACKERS, key=lambda x: x["time"])
    
    for t in sorted_trackers:
        streak = data["streaks"].get(t["id"], 0)
        best = data["best_streaks"].get(t["id"], 0)
        status = "💀 FAIL" if streak == 0 else "🔥 ON FIRE" if streak > 7 else "🟢 ACTIVE"
        content += f"| **{t['name']}** | {t['time']} | **{streak} Days** | **{best} Days** | {status} |\n"
    
    content += f"\n## 📅 CALENDAR: {month_name}\n\n"
    # Use abbreviation or short name for calendar columns to save space? 
    # User wanted longer names, but calendar table might break.
    # Let's use the full name but maybe truncated if needed, or just full name. 
    # For now, full name as requested.
    headers = ["DATE"] + [t["name"] for t in sorted_trackers]
    content += "| " + " | ".join(headers) + " |\n"
    content += "| :--- " + "| :---: " * len(sorted_trackers) + "|\n"
    
    num_days = calendar.monthrange(year, month)[1]
    for day in range(1, num_days + 1):
        d_obj = datetime.date(year, month, day)
        d_str = d_obj.strftime("%Y-%m-%d")
        row = f"| **{d_obj.strftime('%d.%m.')}** | "
        if d_str in data["history"]:
            entries = data["history"][d_str]
            for t in sorted_trackers:
                icon = "✅" if entries.get(t["id"]) is True else "❌"
                row += f"{icon} | "
        elif d_obj > today: row += "➖ | " * len(sorted_trackers)
        else: row += "❌ | " * len(sorted_trackers)
        content += row + "\n"

    for path in [monthly_dashboard_path, ROOT_DASHBOARD]:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print(f"📊 Dashboard updated: {monthly_dashboard_path}")

if __name__ == "__main__":
    run_tracker()
