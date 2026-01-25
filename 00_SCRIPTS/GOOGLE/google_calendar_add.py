import datetime
import sys
from google_auth import get_service

def add_calendar_event(summary, start_time_str, duration_minutes=60, description="", calendar_id='primary'):
    """
    summary: Titel des Termins
    start_time_str: "HH:MM" (für heute) oder "YYYY-MM-DD HH:MM"
    calendar_id: ID des Kalenders (default: 'primary')
    """
    try:
        service = get_service('calendar', 'v3')
        
        now = datetime.datetime.now()
        
        # Zeitformat parsen
        if len(start_time_str) == 5: # HH:MM Format
            start_dt = datetime.datetime.strptime(f"{now.strftime('%Y-%m-%d')} {start_time_str}", "%Y-%m-%d %H:%M")
        else: # YYYY-MM-DD HH:MM Format
            start_dt = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
            
        end_dt = start_dt + datetime.timedelta(minutes=int(duration_minutes))
        
        event = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': start_dt.isoformat(),
                'timeZone': 'Europe/Berlin',
            },
            'end': {
                'dateTime': end_dt.isoformat(),
                'timeZone': 'Europe/Berlin',
            },
            'reminders': {
                'useDefault': True,
            },
        }

        event = service.events().insert(calendarId=calendar_id, body=event).execute()
        print(f"Termin erstellt in Kalender '{calendar_id}': {event.get('htmlLink')}")
        return True
    except Exception as e:
        print(f"Fehler beim Erstellen des Termins: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Nutzung: python add_event.py \"Titel\" \"HH:MM\" [Dauer_Minuten] [Beschreibung] [Kalender_ID]")
        print("Beispiel: python add_event.py \"Spaziergang\" \"18:00\" 60 \"Schritte sammeln\"")
    else:
        summary = sys.argv[1]
        start_time = sys.argv[2]
        duration = sys.argv[3] if len(sys.argv) > 3 else 60
        desc = sys.argv[4] if len(sys.argv) > 4 else ""
        cal_id = sys.argv[5] if len(sys.argv) > 5 else 'primary'
        add_calendar_event(summary, start_time, duration, desc, cal_id)
