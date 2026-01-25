import datetime
from google_auth import get_service

def get_event_color(calendar_id):
    try:
        service = get_service('calendar', 'v3')
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        
        print(f"Lese letzte Termine aus Kalender '{calendar_id}'...")
        
        events_result = service.events().list(
            calendarId=calendar_id, 
            timeMax=now,
            maxResults=500,
            singleEvents=True, 
            orderBy='startTime'
        ).execute()
        
        events = events_result.get('items', [])
        
        if not events:
            print("Keine vergangenen Termine gefunden.")
            return

        found_work = False
        for event in events:
            summary = event.get('summary', 'Kein Titel')
            if "Arbeit" in summary or "Hiwi" in summary:
                color_id = event.get('colorId', 'Standard (nicht gesetzt)')
                print(f"- {event['start'].get('dateTime')}: {summary} (Farbe/ColorId: {color_id})")
                found_work = True
        
        if not found_work:
            print("Keine 'Arbeit' Termine in den letzten 50 Einträgen gefunden.")
            
    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    CAL_ID = "b8c614cae6a22dc62c1e60d444beff5ce38c5c7f9bf2d88168582af9cd386966@group.calendar.google.com"
    get_event_color(CAL_ID)
