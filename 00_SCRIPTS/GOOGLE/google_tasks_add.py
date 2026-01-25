from google_auth_util import get_service

def add_task(task_title, task_list_title='My Tasks'):
    try:
        service = get_service('tasks', 'v1')

        # Get task lists
        results = service.tasklists().list().execute()
        items = results.get('items', [])
        
        task_list_id = None
        for tasklist in items:
            if tasklist['title'] == task_list_title:
                task_list_id = tasklist['id']
                break

        if not task_list_id:
            print(f"Task list '{task_list_title}' not found. Creating a new one.")
            new_task_list = service.tasklists().insert(body={'title': task_list_title}).execute()
            task_list_id = new_task_list['id']

        task = {
            'title': task_title
        }
        
        result = service.tasks().insert(tasklist=task_list_id, body=task).execute()
        print(f"Task '{task_title}' added to '{task_list_title}'.")
        return result

    except Exception as e:
        print(f"Fehler beim Hinzufügen der Aufgabe: {e}")
        return None

if __name__ == '__main__':
    # Example usage:
    # add_task("Testaufgabe von Gemini")
    # add_task("Wichtige Aufgabe", "Meine Einkaufsliste")
    print("This script is designed to be imported and used by other scripts.")
    print("To add a task, call add_task(task_title, task_list_title).")