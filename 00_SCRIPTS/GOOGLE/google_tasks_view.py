from google_auth import get_service

def list_tasks():
    try:
        service = get_service('tasks', 'v1')
        
        # Get task lists
        results = service.tasklists().list().execute()
        items = results.get('items', [])

        if not items:
            print('Keine Task-Listen gefunden.')
            return

        print('--- Deine Google Tasks ---')
        for tasklist in items:
            print(f"\nListe: {tasklist['title']}")
            tasks = service.tasks().list(tasklist=tasklist['id']).execute()
            task_items = tasks.get('items', [])
            
            if not task_items:
                print('  (Keine Aufgaben in dieser Liste)')
            else:
                for task in task_items:
                    status = "[x]" if task['status'] == 'completed' else "[ ]"
                    print(f"  {status} {task['title']}")
                    if 'notes' in task:
                        print(f"      Notiz: {task['notes']}")

    except Exception as e:
        print(f"Fehler beim Abrufen der Tasks: {e}")

if __name__ == '__main__':
    list_tasks()

