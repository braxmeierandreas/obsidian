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
# check_days: None=Daily, [0]=Mon...[6]=Sun, "month"=1st of month
TRACKERS = [
    # MORNING ROUTINE
    {"id": "rise_5am", "name": "WAKE UP 5 AM", "type": "habit", "goal": "Daily", "auto": None, "time": "05:00", "duration": 5, "check_days": None},
    {"id": "make_bed", "name": "MAKE BED", "type": "habit", "goal": "Daily", "auto": None, "time": "05:05", "duration": 2, "check_days": None},
    {"id": "weight_measure", "name": "MEASURE WEIGHT & FAT", "type": "habit", "goal": "Daily", "auto": None, "time": "05:07", "duration": 1, "check_days": None},
    {"id": "temp_measure", "name": "MEASURE TEMPERATURE", "type": "habit", "goal": "Daily", "auto": None, "time": "05:08", "duration": 2, "check_days": None},
    {"id": "dream_journal", "name": "DREAM JOURNAL", "type": "habit", "goal": "Daily", "auto": None, "time": "05:10", "duration": 10, "check_days": None},
    {"id": "electrolytes", "name": "DRINK ELECTROLYTES", "type": "habit", "goal": "Daily", "auto": None, "time": "05:20", "duration": 5, "check_days": None},
    {"id": "vitamins", "name": "TAKE VITAMINS", "type": "habit", "goal": "Daily", "auto": None, "time": "05:25", "duration": 5, "check_days": None},
    {"id": "jogging", "name": "JOGGING", "type": "habit", "goal": "Daily", "auto": None, "time": "05:30", "duration": 45, "check_days": None},
    {"id": "hygiene_m", "name": "MORNING HYGIENE", "type": "habit", "goal": "Daily", "auto": None, "time": "06:15", "duration": 25, "check_days": None},
    {"id": "cold_shower", "name": "COLD SHOWER", "type": "habit", "goal": "Daily", "auto": None, "time": "06:40", "duration": 5, "check_days": None},
    {"id": "cat_feed_am", "name": "CAT FEEDING (AM)", "type": "habit", "goal": "Daily", "auto": None, "time": "06:45", "duration": 5, "check_days": None},
    {"id": "cat_litter", "name": "CAT LITTER", "type": "habit", "goal": "Daily", "auto": None, "time": "06:50", "duration": 5, "check_days": None},
    {"id": "bible", "name": "READ BIBLE", "type": "habit", "goal": "Daily", "auto": None, "time": "07:00", "duration": 15, "check_days": None},
    {"id": "meditate", "name": "MEDITATION", "type": "habit", "goal": "Daily", "auto": None, "time": "07:15", "duration": 15, "check_days": None},
    {"id": "journal_m", "name": "MORNING JOURNAL", "type": "habit", "goal": "Daily", "auto": None, "time": "07:30", "duration": 15, "check_days": None},
    {"id": "planning", "name": "DAILY PLANNING", "type": "habit", "goal": "Daily", "auto": None, "time": "07:45", "duration": 15, "check_days": None},
    {"id": "spanish", "name": "LEARN SPANISH", "type": "habit", "goal": "Daily", "auto": None, "time": "08:00", "duration": 60, "check_days": None},

    # DAY / EVENING
    {"id": "church", "name": "CHURCH SERVICE", "type": "habit", "goal": "Weekly", "auto": None, "time": "10:30", "duration": 60, "check_days": [6]}, # Sunday only
    {"id": "visit_parents", "name": "VISIT PARENTS", "type": "habit", "goal": "Monthly", "auto": None, "time": "10:00", "duration": 240, "check_days": "month"},
    {"id": "monthly_review", "name": "MONTHLY REVIEW & BUDGET", "type": "habit", "goal": "Monthly", "auto": None, "time": "12:00", "duration": 30, "check_days": "month"},
    {"id": "fasting", "name": "FASTING 19-13", "type": "habit", "goal": "Daily", "auto": None, "time": "13:00", "duration": 0, "check_days": None},
    {"id": "grocery", "name": "GROCERY", "type": "habit", "goal": "Daily", "auto": None, "time": "13:00", "duration": 15, "check_days": None},
    {"id": "cooking", "name": "COOKING", "type": "habit", "goal": "Daily", "auto": None, "time": "13:15", "duration": 45, "check_days": None},
    {"id": "laundry", "name": "LAUNDRY & LINENS", "type": "habit", "goal": "Weekly", "auto": None, "time": "14:00", "duration": 60, "check_days": [6]}, # Sunday only
    {"id": "chores", "name": "DAILY CHORES", "type": "habit", "goal": "Daily", "auto": None, "time": "14:00", "duration": 10, "check_days": None},
    {"id": "backup_system", "name": "SYSTEM BACKUP", "type": "habit", "goal": "Weekly", "auto": None, "time": "14:30", "duration": 15, "check_days": [6]}, # Sunday only
    {"id": "call_parents", "name": "CALL PARENTS", "type": "habit", "goal": "Weekly", "auto": None, "time": "15:00", "duration": 30, "check_days": [6]}, # Sunday only
    {"id": "training", "name": "WORKOUT", "type": "habit", "goal": "Daily", "auto": "heart_minutes", "threshold": 40, "time": "17:00", "duration": 45, "check_days": None},
    {"id": "cat_feed_pm", "name": "CAT FEEDING (PM)", "type": "habit", "goal": "Daily", "auto": None, "time": "18:00", "duration": 5, "check_days": None},
    {"id": "dinner", "name": "DINNER", "type": "habit", "goal": "Daily", "auto": None, "time": "18:15", "duration": 30, "check_days": None},
    {"id": "walk", "name": "DAILY WALK", "type": "habit", "goal": "Daily", "auto": None, "time": "18:45", "duration": 60, "check_days": None},
    {"id": "vacuum", "name": "VACUUMING", "type": "habit", "goal": "Daily", "auto": None, "time": "19:45", "duration": 5, "check_days": None},
    {"id": "dishes", "name": "DO DISHES", "type": "habit", "goal": "Daily", "auto": None, "time": "19:50", "duration": 5, "check_days": None},
    {"id": "chores", "name": "DAILY CHORES", "type": "habit", "goal": "Daily", "auto": None, "time": "19:55", "duration": 5, "check_days": None},
    {"id": "reading", "name": "READING", "type": "habit", "goal": "Daily", "auto": None, "time": "20:00", "duration": 60, "check_days": None},
    {"id": "call", "name": "CALL GF", "type": "habit", "goal": "Daily", "auto": None, "time": "21:00", "duration": 15, "check_days": None},
    {"id": "meditate_pm", "name": "MEDITATION (PM)", "type": "habit", "goal": "Daily", "auto": None, "time": "21:15", "duration": 15, "check_days": None},
    {"id": "journal_e", "name": "EVENING JOURNAL", "type": "habit", "goal": "Daily", "auto": None, "time": "21:30", "duration": 15, "check_days": None},
    {"id": "hygiene_e", "name": "EVENING HYGIENE", "type": "habit", "goal": "Daily", "auto": None, "time": "21:45", "duration": 15, "check_days": None},
    {"id": "steps", "name": "10K STEPS", "type": "habit", "goal": "Daily", "auto": "steps", "threshold": 10000, "time": "22:00", "duration": 0, "check_days": None},

    # DETOX / 24H (Sorted at End)
    {"id": "sugar", "name": "NO SUGAR", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H", "duration": 0, "check_days": None},
    {"id": "corn", "name": "NO PORN/MASTURBATION", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H", "duration": 0, "check_days": None},
    {"id": "coffee", "name": "NO COFFEE", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H", "duration": 0, "check_days": None},
    {"id": "weed", "name": "NO WEED", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H", "duration": 0, "check_days": None},
    {"id": "alcohol", "name": "NO ALCOHOL", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H", "duration": 0, "check_days": None},
    {"id": "smoking", "name": "NO SMOKING", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H", "duration": 0, "check_days": None},
    {"id": "games", "name": "NO VIDEO GAMES", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H", "duration": 0, "check_days": None},
    {"id": "tv", "name": "NO TV/SERIES", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H", "duration": 0, "check_days": None},
    {"id": "melatonin", "name": "NO MELATONIN", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H", "duration": 0, "check_days": None},
    {"id": "youtube", "name": "NO YOUTUBE", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H", "duration": 0, "check_days": None},
    {"id": "lies", "name": "NO LIES", "type": "avoid", "goal": "Clean Streak", "auto": None, "time": "24H", "duration": 0, "check_days": None}
]

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"history": {}, "streaks": {}, "best_streaks": {}, "legacy_streaks": {}}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if "best_streaks" not in data: data["best_streaks"] = {}
            if "legacy_streaks" not in data: data["legacy_streaks"] = {}
            return data
    except:
        return {"history": {}, "streaks": {}, "best_streaks": {}, "legacy_streaks": {}}

def save_data(data):
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
        choice = input(f"{prompt} [y/n/l/s]: ").lower().strip()
        if choice in ['y', 'yes', 'j', 'ja', '1']: return True
        if choice in ['n', 'no', 'nein', '0']: return False
        if choice in ['l', 'later', 's', 'skip', 'ny', 'not yet', '']: return None

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

def calculate_streaks(data, best_streaks_data):
    history = data.get("history", {})
    legacy = data.get("legacy_streaks", {})
    current_streaks = {t["id"]: 0 for t in TRACKERS}
    today = datetime.date.today()
    for t in TRACKERS:
        tid = t["id"]
        current = 0
        offset = legacy.get(tid, 0)
        for i in range(365):
            d = today - datetime.timedelta(days=i)
            d_str = d.strftime("%Y-%m-%d")
            if d_str not in history:
                if i == 0: continue
                else: break
            val = history[d_str].get(tid)
            if val is True: current += 1
            elif val is False: break
            else: break 
        final_streak = current + offset
        current_streaks[tid] = final_streak
        if final_streak > best_streaks_data.get(tid, 0): best_streaks_data[tid] = final_streak
    return current_streaks, best_streaks_data

def run_tracker():
    os.system('color')
    try:
        import colorama
        colorama.init()
        CYAN = colorama.Fore.CYAN
        RESET = colorama.Style.RESET_ALL
    except ImportError:
        CYAN = "\033[96m"
        RESET = "\033[0m"

    data = load_data()
    current_hour = datetime.datetime.now().hour
    default_date_str = get_date_str(0)
    if 0 <= current_hour < 4:
        print(f"\n🌙 It is late ({current_hour}:00).")
        if ask_user("Do you want to track for YESTERDAY as default?"):
            default_date_str = get_date_str(1)
    print(f"\n📅 Target Date: {default_date_str}")
    date_input = input("Enter specific date (YYYY-MM-DD), offset (e.g. -1), or Enter to confirm: ").strip()
    target_date_str = default_date_str
    if date_input:
        try:
            if date_input.startswith("-") and date_input[1:].isdigit():
                offset = int(date_input[1:])
                target_date_str = get_date_str(offset)
            else:
                datetime.datetime.strptime(date_input, "%Y-%m-%d")
                target_date_str = date_input
        except ValueError:
            print(f"⚠️ Invalid format. Using default: {target_date_str}")

    print(f"🚀 Tracking for: {target_date_str}")
    print("---------------------------------------")
    auto_data = fetch_google_fit_data(target_date_str)

    # Load existing entries
    day_entry = data["history"].get(target_date_str, {})
    
    target_date_obj = datetime.datetime.strptime(target_date_str, "%Y-%m-%d")
    dow = target_date_obj.weekday()
    dom = target_date_obj.day

    # --- CORRECTION MODE CHECK ---
    correction_mode = False
    if day_entry: # Only ask if there is data to correct
        print("\n📝 Existing data found.")
        if ask_user("Do you want to CORRECT/EDIT existing entries?"):
            correction_mode = True
            print("✏️  CORRECTION MODE ACTIVE. Press Enter to keep current value.")

    print("\n--- 🔨 EXECUTION (l/s = Later/Skip) ---")
    
    sorted_trackers = sorted(TRACKERS, key=lambda x: x["time"])
    changes_made = False

    for t in sorted_trackers:
        # FREQUENCY CHECK
        check_days = t.get("check_days")
        should_ask = True
        if check_days is not None:
            if check_days == "month":
                if dom != 1: should_ask = False
            elif isinstance(check_days, list):
                if dow not in check_days: should_ask = False
        
        # In correction mode, allow editing even if not strictly 'due' today, if data exists
        has_data = day_entry.get(t["id"]) is not None
        if not should_ask and not has_data:
            continue

        existing_val = day_entry.get(t["id"])
        
        if t["auto"] and t["auto"] in auto_data:
            val = auto_data[t["auto"]]
            if val >= t["threshold"]:
                day_entry[t["id"]] = True
                changes_made = True
                print(f"✅ {CYAN}{t['name']}{RESET}: Auto-Completed ({val})")
                continue
        
        # Skip logic: Skip if already done AND NOT in correction mode
        if existing_val is not None and not correction_mode:
            continue

        # Construct Prompt
        status_str = ""
        if existing_val is True: status_str = f" ({colorama.Fore.GREEN}DONE{RESET})"
        elif existing_val is False: status_str = f" ({colorama.Fore.RED}FAILED{RESET})"
        
        action_verb = "execute" if t["type"] == "habit" else "stay CLEAN from"
        q = f"Did you {action_verb}: {CYAN}{t['name']}{RESET}{status_str}?"
        
        success = ask_user(q)
        
        # If user entered a value (True/False/None via 'l'), update.
        # If user just pressed Enter (None) IN CORRECTION MODE, keep existing value!
        if correction_mode:
            if success is not None:
                day_entry[t["id"]] = success
                changes_made = True
            # If success is None (Skip), we do nothing, preserving the existing value.
        else:
            # Normal mode: Update only if valid input
            if success is not None:
                day_entry[t["id"]] = success
                changes_made = True

    data["history"][target_date_str] = day_entry
    curr, best = calculate_streaks(data, data.get("best_streaks", {}))
    data["streaks"] = curr
    data["best_streaks"] = best
    if changes_made or target_date_str not in data["history"]:
        save_data(data)
        generate_dashboard(data)
    else:
        print("\nNo changes made.")

def generate_dashboard(data):
    today = datetime.date.today()
    year = today.year
    month = today.month
    month_name = today.strftime('%B').upper()
    month_folder_name = f"{year}_{month:02d}_{month_name}"
    month_folder_path = os.path.join(CURRENT_DIR, month_folder_name)
    if not os.path.exists(month_folder_path): os.makedirs(month_folder_path)
    monthly_dashboard_path = os.path.join(month_folder_path, f"DASHBOARD_{month_name}_{year}.md")

    def get_day_score(d_str):
        entry = data["history"].get(d_str, {})
        if not entry: return 0
        return sum(1 for t in TRACKERS if entry.get(t["id"]) is True)

    today_str = get_date_str(0)
    yesterday_str = get_date_str(1)
    today_score = get_day_score(today_str)
    yesterday_score = get_day_score(yesterday_str)
    daily_diff = ((today_score - yesterday_score) / len(TRACKERS) * 100) if len(TRACKERS) > 0 else 0
    daily_status = "🚀 IMPROVING" if daily_diff > 0 else "📉 DECLINING" if daily_diff < 0 else "⚖️ STABLE"

    def get_monthly_perf(y, m):
        success = 0
        total = 0
        for d_str, entries in data["history"].items():
            if d_str.startswith(f"{y}-{m:02d}"):
                for t in TRACKERS:
                    if entries.get(t["id"]) is True: success += 1
                    total += 1
        return (success / total * 100) if total > 0 else 0.0

    current_perf = get_monthly_perf(year, month)
    prev_date = today.replace(day=1) - datetime.timedelta(days=1)
    prev_perf = get_monthly_perf(prev_date.year, prev_date.month)
    month_diff = current_perf - prev_perf

    def calculate_end_time(start_str, duration_min):
        if start_str == "24H": return "24H"
        try:
            t = datetime.datetime.strptime(start_str, "%H:%M")
            end = t + datetime.timedelta(minutes=duration_min)
            return end.strftime("%H:%M")
        except: return "?"

    content = f"# 📊 PERFORMANCE DASHBOARD - {month_name} {year}\n\n"
    content += "## 📈 KEY PERFORMANCE INDICATORS\n"
    content += f"- **Monthly Performance:** {current_perf:.1f}% (Month-to-Month: {month_diff:+.1f}%)\n"
    content += f"- **Daily Trend:** {daily_status} ({daily_diff:+.1f}% vs Yesterday)\n"
    content += f"- **Daily Score:** {today_score}/{len([t for t in TRACKERS if t['goal'] == 'Daily'])} Daily Missions completed\n\n"
    
    sorted_trackers = sorted(TRACKERS, key=lambda x: x["time"])

    def build_table(title, filter_func):
        table = f"## {title}\n\n"
        table += "| MISSION | START | END | DUR | STREAK | BEST | STATUS |\n|:---|:---:|:---:|:---:|:---:|:---:|:---:|" + "\n"
        filtered = [t for t in sorted_trackers if filter_func(t)]
        if not filtered: return ""
        for t in filtered:
            streak = data["streaks"].get(t["id"], 0)
            best = data["best_streaks"].get(t["id"], 0)
            status = "💀 FAIL" if streak == 0 else "🔥 ON FIRE" if streak > 7 else "🟢 ACTIVE"
            start = t['time']
            dur = f"{t['duration']}m" if t['duration'] > 0 else "-"
            end = calculate_end_time(start, t['duration']) if t['duration'] > 0 else "-"
            table += f"| **{t['name']}** | {start} | {end} | {dur} | **{streak} Days** | **{best} Days** | {status} |\n"
        return table + "\n"

    content += build_table("🌞 DAILY MISSIONS", lambda t: t['type'] == 'habit' and t['goal'] == 'Daily')
    content += build_table("📅 WEEKLY & FITNESS MISSIONS", lambda t: t['type'] == 'habit' and t['goal'] in ['Weekly', '2x/Week', '3x/Week'])
    content += build_table("🗓️ MONTHLY MISSIONS", lambda t: t['type'] == 'habit' and t['goal'] == 'Monthly')
    content += build_table("🚫 DETOX PROTOCOL", lambda t: t['type'] == 'avoid')
    
    content += f"\n## 📅 CALENDAR: {month_name}\n\n"
    headers = ["DATE"] + [t["name"] for t in sorted_trackers]
    content += "| " + " | ".join(headers) + " |\n"
    content += "| :--- " + "| :---: " * len(sorted_trackers) + "|\n"
    
    num_days = calendar.monthrange(year, month)[1]
    for day in range(1, num_days + 1):
        d_obj = datetime.date(year, month, day)
        d_str = d_obj.strftime("%Y-%m-%d")
        row = f"| **{d_obj.strftime('%d.%m.')}** | "
        if d_str in data["history"]:
            entries = data["history"].get(d_str)
            for t in sorted_trackers:
                val = entries.get(t["id"])
                if val is True: icon = "✅"
                elif val is False: icon = "❌"
                else: icon = "➖"
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