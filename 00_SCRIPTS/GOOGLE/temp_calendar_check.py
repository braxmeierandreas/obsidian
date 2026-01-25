import datetime
from google_auth import get_service

def get_next_week_events():
    try:
        service = get_service('calendar', 'v3')
        # Start: Morgen 00:00 Uhr
        start_date = datetime.datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
        # Ende: Start + 7 Tage
        end_date = start_date + datetime.timedelta(days=7)
        
        print(f"Hole Termine von {start_date} bis {end_date}...")
        
        # Calendars to check
        calendars = {
            'primary': 'Privat',
            'b8c614cae6a22dc62c1e60d444beff5ce38c5c7f9bf2d88168582af9cd386966@group.calendar.google.com': 'Studium/Arbeit'
        }

        all_events = []

        for cal_id, cal_name in calendars.items():
            events_result = service.events().list(
                calendarId=cal_id, 
                timeMin=start_date.isoformat() + 'Z', 
                timeMax=end_date.isoformat() + 'Z', 
                singleEvents=True, 
                orderBy='startTime'
            ).execute()
            
            for e in events_result.get('items', []):
                e['cal_name'] = cal_name
                all_events.append(e)

        # Sort by time
        all_events.sort(key=lambda x: x['start'].get('dateTime', x['start'].get('date')))

        for e in all_events:
            start = e['start'].get('dateTime', e['start'].get('date'))
            end = e['end'].get('dateTime', e['end'].get('date'))
            
            # Formatting
            if 'T' in start:
                start_dt = datetime.datetime.fromisoformat(start.replace('Z', '+00:00'))
                end_dt = datetime.datetime.fromisoformat(end.replace('Z', '+00:00'))
                day_name = start_dt.strftime("%A")
                time_str = f"{start_dt.strftime('%H:%M')} - {end_dt.strftime('%H:%M')}"
            else:
                day_name = datetime.datetime.strptime(start, "%Y-%m-%d").strftime("%A")
                time_str = "Ganztägig"
                
            print(f"[{day_name}] {time_str}: {e['summary']} ({e['cal_name']})")

    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    get_next_week_events()
