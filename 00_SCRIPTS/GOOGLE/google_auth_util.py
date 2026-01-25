import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Note: SCOPES should ideally be managed centrally or passed as an argument.
# For simplicity, we'll redefine relevant ones here, but in a real app,
# ensure consistency with setup_google_auth.py.
SCOPES = [
    'https://mail.google.com/',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/presentations',
    'https://www.googleapis.com/auth/forms.body',
    'https://www.googleapis.com/auth/tasks', # Changed from tasks.readonly to tasks
    'https://www.googleapis.com/auth/fitness.activity.read',
    'https://www.googleapis.com/auth/fitness.body.read',
    'https://www.googleapis.com/auth/fitness.sleep.read',
    'https://www.googleapis.com/auth/fitness.heart_rate.read',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/contacts.readonly',
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/cloud-platform'
]

def get_service(api_name, api_version, scopes=None):
    """
    Authenticates and returns a Google API service object.
    If no token is found, it will attempt to re-authenticate using the credentials file.
    """
    creds = None
    
    # Define path to config directory
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_DIR = os.path.join(os.path.dirname(BASE_DIR), 'CONFIG')
    token_path = os.path.join(CONFIG_DIR, 'token.json')
    
    # The token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES) # Use SCOPES here
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Fallback to credentials_desktop.json for initial flow if token is missing
            creds_file_name = 'credentials_desktop.json' # Prioritize key_neu.json as in setup_google_auth.py if it exists
            key_neu = os.path.join(CONFIG_DIR, 'key_neu.json')
            if os.path.exists(key_neu):
                creds_file_name = 'key_neu.json'

            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.join(CONFIG_DIR, creds_file_name), SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build(api_name, api_version, credentials=creds)
        return service
    except HttpError as err:
        print(f"An HTTP error occurred: {err}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == '__main__':
    # Example usage (for testing purposes, if run directly)
    # This will trigger the authentication flow if not already authenticated.
    print("This script provides the get_service function for Google API access.")
    print("Attempting to get a Tasks service...")
    tasks_service = get_service('tasks', 'v1', ['https://www.googleapis.com/auth/tasks'])
    if tasks_service:
        print("Successfully obtained Tasks service.")
    else:
        print("Failed to obtain Tasks service.")
