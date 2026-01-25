import os
from google_auth_oauthlib.flow import InstalledAppFlow

# Berechtigungen für Gmail, Drive und Docs
SCOPES = [
    'https://mail.google.com/',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/presentations',
    'https://www.googleapis.com/auth/forms.body',
    'https://www.googleapis.com/auth/tasks.readonly',
    'https://www.googleapis.com/auth/fitness.activity.read',
    'https://www.googleapis.com/auth/fitness.body.read',
    'https://www.googleapis.com/auth/fitness.sleep.read',
    'https://www.googleapis.com/auth/fitness.heart_rate.read',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/contacts.readonly',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/cloud-platform'
]

def login():
    # Define path to config directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_DIR = os.path.join(BASE_DIR, 'CONFIG')
    
    # Priorisiere key_neu.json, dann credentials_desktop.json
    key_neu = os.path.join(CONFIG_DIR, 'key_neu.json')
    creds_desktop = os.path.join(CONFIG_DIR, 'credentials_desktop.json')
    
    creds_file = key_neu if os.path.exists(key_neu) else creds_desktop
    
    if not os.path.exists(creds_file):
        print(f"FEHLER: Weder '{key_neu}' noch '{creds_desktop}' gefunden!")
        return

    print(f"Starte Login-Vorgang mit {creds_file}...")
    
    try:
        flow = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
        creds = flow.run_local_server(port=0)

        # Token speichern
        token_path = os.path.join(CONFIG_DIR, 'token.json')
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
        
        print(f"\nERFOLG! Die Datei '{token_path}' wurde erstellt.")
        print("Du bist jetzt dauerhaft eingeloggt.")
    except Exception as e:
        print(f"Fehler beim Login: {e}")

if __name__ == '__main__':
    login()
