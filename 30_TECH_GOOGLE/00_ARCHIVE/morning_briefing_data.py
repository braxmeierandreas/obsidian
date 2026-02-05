import datetime
import os
from auth_helper import get_service

def get_calendar_events():
    try:
        service = get_service('calendar', 'v3')
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        end_of_day = (datetime.datetime.utcnow().replace(hour=23, minute=59, second=59)).isoformat() + 'Z'
        
        events_result = service.events().list(calendarId='primary', timeMin=now, timeMax=end_of_day,
                                              singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])
        return events
    except Exception as e:
        return f"Fehler Kalender: {e}"

def get_unread_mails():
    try:
        service = get_service('gmail', 'v1')
        today = datetime.date.today().strftime("%Y/%m/%d")
        results = service.users().messages().list(userId='me', q=f'is:unread after:{today}', maxResults=5).execute()
        messages = results.get('messages', [])
        mail_list = []
        for msg in messages:
            m = service.users().messages().get(userId='me', id=msg['id'], format='metadata').execute()
            headers = m['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(Kein Betreff)')
            mail_list.append(subject)
        return mail_list
    except Exception as e:
        return [f"Fehler Mail: {e}"]

def get_tasks():
    try:
        service = get_service('tasks', 'v1')
        tasklists = service.tasklists().list().execute().get('items', [])
        all_tasks = []
        for tl in tasklists:
            tasks = service.tasks().list(tasklist=tl['id'], showCompleted=False).execute().get('items', [])
            if tasks:
                all_tasks.extend([t['title'] for t in tasks])
        return all_tasks[:5] # Top 5 Tasks
    except Exception as e:
        return [f"Fehler Tasks: {e}"]

def get_fit_status():
    try:
        # Wir nutzen die Logik aus update_dashboard, aber geben nur die Kernwerte zurück
        service = get_service('fitness', 'v1')
        now_dt = datetime.datetime.now()
        start_of_month = now_dt.replace(day=1, hour=0, minute=0, second=0)
        
        body = {
            "aggregateBy": [{"dataTypeName": "com.google.step_count.delta"}],
            "bucketByTime": { "durationMillis": 86400000 },
            "startTimeMillis": int(start_of_month.timestamp() * 1000),
            "endTimeMillis": int(now_dt.timestamp() * 1000)
        }
        res = service.users().dataset().aggregate(userId="me", body=body).execute()
        
        total_steps = 0
        today_steps = 0
        for bucket in res.get('bucket', []):
            s = sum(v.get('intVal', 0) for ds in bucket.get('dataset', []) for p in ds.get('point', []) for v in p.get('value', []))
            total_steps += s
            # Letzter Bucket ist meist heute
        
        # Vereinfachte Rückgabe für das Briefing
        avg = total_steps / now_dt.day
        needed = max(0, (now_dt.day * 10000) - (total_steps - today_steps))
        return {"avg": int(avg), "needed_today": int(needed)}
    except:
        return None

def run_briefing():
    print("--- Sammle Daten für dein Morning-Briefing ---")
    
    cal = get_calendar_events()
    mails = get_unread_mails()
    tasks = get_tasks()
    fit = get_fit_status()
    
    print("\n--- DEIN BRIEFING DATEN-DUMP ---")
    print(f"TERMINE: {cal}")
    print(f"MAILS: {mails}")
    print(f"TASKS: {tasks}")
    print(f"FIT: {fit}")
    
    # Der Dump wird von Gemini gelesen und in eine schöne Antwort verwandelt.

if __name__ == "__main__":
    run_briefing()
