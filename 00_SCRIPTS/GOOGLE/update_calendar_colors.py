import datetime
from google_auth import get_service

def update_event_colors(calendar_id, query, start_date_str, end_date_str, color_id):
    try:
        service = get_service('calendar', 'v3')
        
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
        
        time_min = start_date.isoformat() + 'Z'
        time_max = end_date.isoformat() + 'Z'
        
        print(f"Suche '{query}' in {calendar_id} ({start_date_str} bis {end_date_str})...")
        
        events_result = service.events().list(
            calendarId=calendar_id, 
            timeMin=time_min, 
            timeMax=time_max,
            q=query,
            singleEvents=True, 
            orderBy='startTime'
        ).execute()
        
        events = events_result.get('items', [])
        
        if not events:
            print("Keine passenden Termine gefunden.")
            return

        print(f"{len(events)} Termine gefunden. Aktualisiere auf Farbe {color_id}...")
        
        count = 0
        for event in events:
            if event['summary'] == query:
                # Patch request to update only the colorId
                service.events().patch(
                    calendarId=calendar_id, 
                    eventId=event['id'], 
                    body={'colorId': color_id}
                ).execute()
                print(f"Aktualisiert: {event['start'].get('dateTime')} - {event['summary']}")
                count += 1
            else:
                 print(f"Übersprungen: {event['summary']}")
        
        print(f"Fertig. {count} Termine aktualisiert.")

    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    CAL_ID = "b8c614cae6a22dc62c1e60d444beff5ce38c5c7f9bf2d88168582af9cd386966@group.calendar.google.com"
    # Update Arbeit events to Yellow (Id 5)
    update_event_colors(CAL_ID, "Arbeit", "2026-01-21", "2026-02-01", "5")
