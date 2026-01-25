import datetime
from google_auth import get_service

def delete_events(query, start_date_str, end_date_str):
    try:
        service = get_service('calendar', 'v3')
        
        # Parse dates and make them timezone aware (UTC) for the API
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
        
        time_min = start_date.isoformat() + 'Z'
        time_max = end_date.isoformat() + 'Z'
        
        print(f"Suche nach '{query}' von {start_date_str} bis {end_date_str} im 'primary' Kalender...")
        
        events_result = service.events().list(
            calendarId='primary', 
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

        print(f"{len(events)} Termine gefunden. Lösche...")
        
        count = 0
        for event in events:
            # Sicherheitscheck: Nur löschen, wenn Titel exakt stimmt
            if event['summary'] == query:
                service.events().delete(calendarId='primary', eventId=event['id']).execute()
                print(f"Gelöscht: {event['start'].get('dateTime')} - {event['summary']}")
                count += 1
            else:
                 print(f"Übersprungen (Titel stimmt nicht exakt): {event['start'].get('dateTime')} - {event['summary']}")
        
        print(f"Fertig. {count} Termine gelöscht.")

    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    # Suche vom 21.01.2026 bis 01.02.2026 um alle erstellten Termine zu erwischen
    delete_events("Arbeit", "2026-01-21", "2026-02-01")
