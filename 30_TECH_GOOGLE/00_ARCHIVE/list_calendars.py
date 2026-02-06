from auth_helper import get_service

def list_calendars():
    try:
        service = get_service('calendar', 'v3')
        calendar_list = service.calendarList().list().execute()
        
        print("Verfügbare Kalender:")
        for calendar_list_entry in calendar_list.get('items', []):
            print(f"- Name: {calendar_list_entry['summary']} | ID: {calendar_list_entry['id']}")
            
    except Exception as e:
        print(f"Fehler beim Auflisten der Kalender: {e}")

if __name__ == "__main__":
    list_calendars()
