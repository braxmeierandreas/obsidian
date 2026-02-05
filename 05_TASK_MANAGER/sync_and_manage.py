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
    print("🔄 Starte Synchronisierung (Bi-Directional)...")
    
    # 1. Lokale Aufgaben lesen (und Zeilen merken für Rewrite)
    if not os.path.exists(KANBAN_FILE):
        print("❌ Kanban Datei nicht gefunden.")
        return

    with open(KANBAN_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

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

    # Mappen für schnelleren Zugriff: Title -> Google Task Object
    google_map = {t['title']: t for t in google_tasks}
    
    updates_to_file = False
    new_lines = lines[:] # Kopie der Zeilen für Modifikationen

    # 4. Sync Logik
    
    # A) Obsidian -> Google (Neue Tasks + Status Update zu Google)
    added_count = 0
    closed_in_google_count = 0

    for task in local_tasks:
        g_task = google_map.get(task['title'])
        
        if not g_task:
            # Task existiert lokal, aber nicht in Google -> Nur hochladen wenn er NICHT erledigt ist
            if not task['done']:
                print(f"➕ Upload zu Google: {task['title']}")
                body = {
                    'title': task['title'],
                    'notes': f"Status: {task['section']} | Importiert aus Obsidian"
                }
                if task['due']:
                    due_dt = datetime.strptime(task['due'], '%Y-%m-%d')
                    body['due'] = due_dt.isoformat() + 'Z'
                
                try:
                    service.tasks().insert(tasklist=list_id, body=body).execute()
                    added_count += 1
                except Exception as e:
                    print(f"   Fehler: {e}")
        
        else:
            # Task existiert in beiden -> Status Check
            # Case 1: Lokal [x], Google Open -> Google schließen
            if task['done'] and g_task['status'] != 'completed':
                print(f"✅ Markiere in Google als erledigt: {task['title']}")
                try:
                    service.tasks().update(tasklist=list_id, task=g_task['id'], body={
                        'id': g_task['id'],
                        'title': g_task['title'],
                        'status': 'completed'
                    }).execute()
                    closed_in_google_count += 1
                except Exception as e:
                    print(f"   Fehler: {e}")

            # Case 2: Lokal [ ], Google Completed -> Lokal schließen
            elif not task['done'] and g_task['status'] == 'completed':
                print(f"📥 Markiere in Obsidian als erledigt: {task['title']}")
                # Datei-Update Logik
                updates_to_file = True
                # Wir müssen die Zeile finden. Wir gehen einfach über alle Zeilen.
                # Achtung: Das ist simpel und könnte bei doppelten Titeln Probleme machen.
                for i, line in enumerate(new_lines):
                    if f"- [ ] {task['title']}" in line:
                        new_lines[i] = line.replace("- [ ]", "- [x]")
                        break

    # B) Datei zurückschreiben, falls Änderungen
    if updates_to_file:
        try:
            with open(KANBAN_FILE, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print("💾 Kanban Board lokal aktualisiert.")
        except Exception as e:
            print(f"❌ Fehler beim Schreiben der Datei: {e}")

    if added_count == 0 and closed_in_google_count == 0 and not updates_to_file:
        print("✨ Alles synchron.")

    # 5. Deadlines checken
    print("\n⏰ DEADLINE CHECK:")
    today = datetime.now()
    upcoming_found = False
    
    # Reload local tasks falls wir die Datei geändert haben
    if updates_to_file:
        local_tasks = parse_markdown_tasks()

    for task in local_tasks:
        if task['due'] and not task['done']:
            due_dt = datetime.strptime(task['due'], '%Y-%m-%d')
            delta = (due_dt - today).days + 1 
            
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