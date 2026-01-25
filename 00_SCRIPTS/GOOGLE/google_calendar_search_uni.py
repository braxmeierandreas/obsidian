import datetime
from auth_helper import get_service

STUDIUM_CAL_ID = "b8c614cae6a22dc62c1e60d444beff5ce38c5c7f9bf2d88168582af9cd386966@group.calendar.google.com"

def search_studium_events(query=None, months_back=3):
    try:
        service = get_service('calendar', 'v3')
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        past = (datetime.datetime.utcnow() - datetime.timedelta(days=30*months_back)).isoformat() + 'Z'
        
        print(f"Suche im Kalender 'Studium + Arbeit'...")
        
        events_result = service.events().list(
            calendarId=STUDIUM_CAL_ID, 
            timeMin=past, 
            timeMax=now,
            q=query,
            singleEvents=True, 
            orderBy='startTime'
        ).execute()
        
        events = events_result.get('items', [])
        
        if not events:
            print("Keine Einträge gefunden.")
            return
            
        print(f"\nEinträge in 'Studium + Arbeit':")
        for e in events:
            start = e['start'].get('dateTime', e['start'].get('date'))
            print(f"- {start[:10]} {start[11:16]}: {e['summary']}")
            
    except Exception as e:
        print(f"Fehler bei der Suche: {e}")

if __name__ == "__main__":
    search_studium_events()

