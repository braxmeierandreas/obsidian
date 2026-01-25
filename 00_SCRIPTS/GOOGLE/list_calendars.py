from google_auth import get_service

def list_calendars():
    try:
        service = get_service('calendar', 'v3')
        page_token = None
        while True:
            calendar_list = service.calendarList().list(pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                print(f"Name: {calendar_list_entry['summary']}, ID: {calendar_list_entry['id']}")
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break
    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    list_calendars()
