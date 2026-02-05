import sys
import os
import datetime
import math

# --- CONFIGURATION ---
LOG_FILE = r"C:\Users\braxm\obsidian\04_GOALS\01_HEALTH\08_HALBMARATHON_2026\RUNNING_LOG.md"
TARGET_PACE_HM = "05:41" # Target for 2:00h
TARGET_DIST_HM = 21.1

# ANSI Colors for "Cool" Output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def parse_time(time_str):
    """Parses mm:ss or mmm:ss into total minutes."""
    try:
        parts = time_str.split(':')
        if len(parts) == 2:
            return float(parts[0]) + float(parts[1])/60
        elif len(parts) == 3: # h:mm:ss
            return float(parts[0])*60 + float(parts[1]) + float(parts[2])/60
        else:
            return float(time_str)
    except:
        return 0.0

def format_pace(minutes_per_km):
    mins = int(minutes_per_km)
    secs = int((minutes_per_km - mins) * 60)
    return f"{mins:02d}:{secs:02d}"

def load_log():
    runs = []
    if not os.path.exists(LOG_FILE):
        return runs
    
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    # Skip header (starts with | Date)
    for line in lines:
        if not line.strip().startswith('|'): continue
        if "Date" in line or ":---" in line: continue
        
        parts = [p.strip() for p in line.split('|')]
        if len(parts) < 8: continue
        
        try:
            runs.append({
                'date': parts[1],
                'dist': float(parts[2]),
                'time': parse_time(parts[3]),
                'pace': parts[4],
                'hr': int(parts[5]) if parts[5].isdigit() else 0,
                'spm': int(parts[6]) if parts[6].isdigit() else 0
            })
        except:
            continue
    return runs

def main():
    # 1. Get Arguments
    if len(sys.argv) < 6:
        print("Error: Not enough arguments.")
        return

    # args: script, dist, time, hr, spm, notes...
    try:
        dist = float(sys.argv[1])
        time_str = sys.argv[2]
        hr = sys.argv[3]
        spm = sys.argv[4]
        notes = " ".join(sys.argv[5:])
    except ValueError:
        print("Error: Invalid arguments. Please ensure distance is a number.")
        return
    
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    # Calculate Pace
    total_mins = parse_time(time_str)
    pace_decimal = total_mins / dist if dist > 0 else 0
    pace_str = format_pace(pace_decimal)
    
    # 2. Append to Log File
    # Using explicit newline character in f-string to avoid syntax errors
    new_line = f"| {today} | {dist} | {time_str} | {pace_str} | {hr} | {spm} | {notes} |\n"
    
    header = "| Date | Dist (km) | Time (min) | Pace (/km) | HR (bpm) | SPM | Note |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
    
    file_exists = os.path.exists(LOG_FILE)
    
    # Create directory if it doesn't exist
    log_dir = os.path.dirname(LOG_FILE)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        if not file_exists:
            f.write("# 🏃‍♂️ Running Log\n\n" + header)
        f.write(new_line)

    # 3. Calculate Stats & Cool Output
    runs = load_log()
    
    total_km = sum(r['dist'] for r in runs)
    this_month = datetime.date.today().strftime("%Y-%m")
    month_km = sum(r['dist'] for r in runs if r['date'].startswith(this_month))
    
    # Streak Calculation
    sorted_dates = sorted(list(set([r['date'] for r in runs])), reverse=True)
    streak = 0
    check_date = datetime.date.today()
    
    # Check if we ran today (we just added it)
    if sorted_dates and sorted_dates[0] == check_date.strftime("%Y-%m-%d"):
        streak = 1
        check_date -= datetime.timedelta(days=1)
        for d in sorted_dates[1:]:
            if d == check_date.strftime("%Y-%m-%d"):
                streak += 1
                check_date -= datetime.timedelta(days=1)
            else:
                break
    
    # Console Output
    print("\n" + "="*50)
    print(f"{Colors.HEADER}🚀 RUN LOGGED SUCCESSFULLY!{Colors.ENDC}")
    print(f"{Colors.BOLD}Run Details:{Colors.ENDC} {dist}km in {time_str} ({pace_str}/km) @ {hr}bpm")
    print("="*50)
    
    print(f"\n{Colors.CYAN}📊 STATS UPDATE:{Colors.ENDC}")
    print(f"  🔥 {Colors.WARNING}Current Streak:{Colors.ENDC} {streak} Days")
    print(f"  🏃 {Colors.GREEN}Total Distance:{Colors.ENDC} {total_km:.2f} km")
    print(f"  📅 {Colors.BLUE}This Month:{Colors.ENDC}     {month_km:.2f} km")
    
    # Fun Progress Bar to Half Marathon Distance (Single Run)
    pct_hm = min(100, (dist / TARGET_DIST_HM) * 100)
    bar_len = 20
    filled = int(bar_len * pct_hm / 100)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"\n🎯 {Colors.HEADER}Half Marathon Readiness (Dist):{Colors.ENDC}")
    print(f"  [{bar}] {dist:.1f}km / 21.1km ({pct_hm:.1f}%)")
    
    # Feedback
    if pace_decimal < 6.0: # Sub 6:00 pace
        print(f"\n⚡ {Colors.WARNING}FAST PACE! You're flying!{Colors.ENDC}")
    elif int(hr) < 135 and dist > 5:
        print(f"\n💚 {Colors.GREEN}Great Zone 2 building! Heart of steel.{Colors.ENDC}")
    
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()