import sys
import os
import re
from datetime import datetime, timedelta

# Pfad zu den Skripten hinzufügen, um Module zu importieren
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '00_SCRIPTS', 'GOOGLE')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '00_SCRIPTS')))

try:
    from google_auth_util import get_service
except ImportError:
    print("FEHLER: Konnte 'google_auth_util' nicht importieren.")
    print("Stelle sicher, dass '00_SCRIPTS/GOOGLE/google_auth_util.py' existiert.")
    sys.exit(1)

KANBAN_FILE = os.path.join(os.path.dirname(__file__), 'KANBAN_BOARD.md')
TASK_LIST_NAME = 'My Tasks'  # Standard Google Tasks Liste

def parse_markdown_tasks():
    """Liest die Markdown-Datei und extrahiert Aufgaben."""
    tasks = []
    if not os.path.exists(KANBAN_FILE):
        print(f"Kanban Board nicht gefunden unter: {KANBAN_FILE}")
        return []

    with open(KANBAN_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_section = None
    for line in lines:
        line = line.strip()
        if line.startswith('## '):
            current_section = line[3:].strip()
        elif line.startswith('- [ ]') or line.startswith('- [x]'):
            is_done = line.startswith('- [x]')
            text = line[5:].strip()
            
            # Deadline extrahieren (due: YYYY-MM-DD)
            due_date = None
            due_match = re.search(r'\(due:\s*(\d{4}-\d{2}-\d{2})\)', text)
            if due_match:
                due_date = due_match.group(1)
                # Entferne das due-Tag aus dem Titel für Google Tasks (optional)
                # text = text.replace(due_match.group(0), '').strip()

            tasks.append({
                'title': text,
                'section': current_section,
                'done': is_done,
                'due': due_date
            })
    return tasks

def get_google_tasks(service):
    """Holt alle Aufgaben von der Standard-Liste."""
    try:
        results = service.tasklists().list().execute()
        items = results.get('items', [])
        
        task_list_id = None
        for tasklist in items:
            if tasklist['title'] == TASK_LIST_NAME:
                task_list_id = tasklist['id']
                break
        
        if not task_list_id:
            # Fallback: Erste Liste nehmen
            if items:
                task_list_id = items[0]['id']
            else:
                return None, []

        all_tasks = []
        page_token = None
        while True:
            results = service.tasks().list(tasklist=task_list_id, showCompleted=True, pageToken=page_token).execute()
            items = results.get('items', [])
            all_tasks.extend(items)
            page_token = results.get('nextPageToken')
            if not page_token:
                break
                
        return task_list_id, all_tasks
    except Exception as e:
        print(f"Fehler beim Abrufen der Google Tasks: {e}")
        return None, []

def sync_tasks():
    print("🔄 Starte Synchronisierung...")
    
    # 1. Lokale Aufgaben lesen
    local_tasks = parse_markdown_tasks()
    
    # 2. Google Service starten
    try:
        service = get_service('tasks', 'v1')
    except Exception as e:
        print(f"❌ Auth-Fehler: {e}")
        return

    # 3. Google Aufgaben holen
    list_id, google_tasks = get_google_tasks(service)
    if not list_id:
        print("❌ Keine Google Task Liste gefunden.")
        return

    google_titles = [t['title'] for t in google_tasks]
    
    # 4. Sync: Lokal -> Google (Nur neue hinzufügen)
    added_count = 0
    for task in local_tasks:
        # Wir syncen nur 'TODO' und 'IN PROGRESS' die noch nicht erledigt sind
        if not task['done'] and task['title'] not in google_titles:
            print(f"➕ Füge hinzu: {task['title']}")
            body = {
                'title': task['title'],
                'notes': f"Status: {task['section']} | Importiert aus Obsidian"
            }
            if task['due']:
                # Google API erwartet RFC 3339 timestamp string
                due_dt = datetime.strptime(task['due'], '%Y-%m-%d')
                body['due'] = due_dt.isoformat() + 'Z'

            try:
                service.tasks().insert(tasklist=list_id, body=body).execute()
                added_count += 1
            except Exception as e:
                print(f"   Fehler beim Hinzufügen: {e}")

    if added_count == 0:
        print("✅ Alle lokalen Aufgaben sind bereits in Google Tasks.")
    else:
        print(f"✅ {added_count} Aufgaben zu Google Tasks hinzugefügt.")

    # 5. Deadlines checken
    print("
⏰ DEADLINE CHECK:")
    today = datetime.now()
    upcoming_found = False
    
    for task in local_tasks:
        if task['due'] and not task['done']:
            due_dt = datetime.strptime(task['due'], '%Y-%m-%d')
            delta = (due_dt - today).days + 1 # +1 weil heute = 0 diff, aber wir wollen "noch X Tage"
            
            if delta < 0:
                print(f"🔴 ÜBERFÄLLIG ({abs(delta)} Tage): {task['title']}")
                upcoming_found = True
            elif delta <= 3:
                print(f"🟠 BALD FÄLLIG (in {delta} Tagen): {task['title']}")
                upcoming_found = True
            elif delta <= 7:
                 print(f"🟡 Diese Woche ({delta} Tage): {task['title']}")
                 upcoming_found = True

    if not upcoming_found:
        print("   Keine dringenden Deadlines in Sicht.")

if __name__ == "__main__":
    sync_tasks()
