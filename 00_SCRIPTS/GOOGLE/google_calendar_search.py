import datetime
from auth_helper import get_service

def find_past_events(query, months_back=6):
    try:
        service = get_service('calendar', 'v3')
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        past = (datetime.datetime.utcnow() - datetime.timedelta(days=30*months_back)).isoformat() + 'Z'
        
        print(f"Suche nach '{query}' von {past} bis {now}...")
        
        events_result = service.events().list(
            calendarId='primary', 
            timeMin=past, 
            timeMax=now,
            q=query,
            singleEvents=True, 
            orderBy='startTime'
        ).execute()
        
        events = events_result.get('items', [])
        
        if not events:
            print(f"Keine Einträge für '{query}' gefunden.")
            return
            
        print(f"\nGefundene Einträge für '{query}':")
        for e in events:
            start = e['start'].get('dateTime', e['start'].get('date'))
            print(f"- {start[:10]}: {e['summary']}")
            
    except Exception as e:
        print(f"Fehler bei der Suche: {e}")

if __name__ == "__main__":
    find_past_events("Arbeiten")

