import json
import os
import sys

# --- CONFIGURATION ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(CURRENT_DIR, "habit_data.json")

# Import TRACKERS from the main script to ensure consistency
try:
    from habit_tracker import TRACKERS
except ImportError:
    print("❌ Error: Could not import TRACKERS from habit_tracker.py")
    sys.exit(1)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"history": {}, "streaks": {}, "best_streaks": {}, "legacy_streaks": {}}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if "legacy_streaks" not in data: data["legacy_streaks"] = {}
            return data
    except:
        return {"history": {}, "streaks": {}, "best_streaks": {}, "legacy_streaks": {}}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def run_setup():
    os.system('color')
    CYAN = "\033[96m"
    RESET = "\033[0m"
    GREEN = "\033[92m"

    print("\n🛠️  HABIT STREAK SETUP  🛠️")
    print("----------------------------")
    print("Enter the number of days you have ALREADY completed for each habit.")
    print("Press [ENTER] to skip (leave as is or 0).\n")

    data = load_data()
    legacy = data.get("legacy_streaks", {})

    for t in TRACKERS:
        tid = t["id"]
        name = t["name"]
        current_legacy = legacy.get(tid, 0)
        
        prompt = f"Existing streak for {CYAN}{name}{RESET} [{current_legacy}]: "
        val = input(prompt).strip()
        
        if val:
            try:
                new_val = int(val)
                legacy[tid] = new_val
                print(f"   -> Set to {GREEN}{new_val}{RESET} days.")
            except ValueError:
                print("   -> Invalid number, skipping.")
        # else: keep existing

    data["legacy_streaks"] = legacy
    save_data(data)
    print("\n✅ Setup complete! run RUN_HABITS.bat to see your updated streaks.")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    run_setup()
