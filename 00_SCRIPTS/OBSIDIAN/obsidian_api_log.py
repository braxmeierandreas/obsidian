import requests
import datetime
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = "ae123548a695eed44ccb77ab8eac6e157efd2c847710a94a11b2b887f5b45682"
PORT = "27124" 
BASE_URL = f"https://127.0.0.1:{PORT}"

def log_to_obsidian(text):
    today = datetime.date.today().strftime("%Y-%m-%d")
    file_path = f"02_JOURNAL/08_BRIEFING/BRIEFING_{today}.md"
    url = f"{BASE_URL}/vault/{file_path}"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "text/markdown"}

    try:
        res = requests.get(url, headers=headers, verify=False, timeout=5)
        content = res.text if res.status_code == 200 else f"# Briefing {today}\n\n"
        
        # LOGIK-ERWEITERUNG:
        if text.startswith("h:"): # HABIT
            habit_name = text.replace("h:", "").strip()
            new_entry = f"- [ ] {habit_name}"
        elif text.startswith("w:"): # WEIGHT (für Massephase)
            weight = text.replace("w:", "").strip()
            new_entry = f"weight:: {weight}" # Inline Metadata für Dataview
        else: # NORMALER LOG
            now = datetime.datetime.now().strftime("%H:%M")
            new_entry = f"- [{now}] {text}"

        if not content.endswith("\n"): content += "\n"
        updated_content = content + new_entry + "\n"

        requests.put(url, headers=headers, data=updated_content.encode('utf-8'), verify=False, timeout=5)
        print(f"✅ Notiert für {today}: {new_entry}")

    except Exception as e:
        print(f"❌ Fehler: {e}")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        log_to_obsidian(" ".join(sys.argv[1:]))