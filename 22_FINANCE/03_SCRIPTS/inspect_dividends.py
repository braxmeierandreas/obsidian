import requests
import base64
import json

# --- KONFIGURATION ---
API_KEY = "35211271ZsmeVZHQQODoFZSbqBqCRreRDsJsN"
API_SECRET = "aRJqiON-t61xEkN13xWlP5MsqYr02qBpKiUheCWRmFk"
BASE_URL = "https://live.trading212.com/api/v0"

# Auth Header
auth_str = f"{API_KEY}:{API_SECRET}"
encoded_auth = base64.b64encode(auth_str.encode()).decode()
HEADERS = {"Authorization": f"Basic {encoded_auth}"}

try:
    print("Fetching dividend history...")
    # Fetch dividends (default)
    r = requests.get(f"{BASE_URL}/equity/history/dividends", headers=HEADERS)
    r.raise_for_status()
    divs = r.json()

    print(f"Type of response: {type(divs)}")
    if isinstance(divs, dict):
        print(f"Keys: {divs.keys()}")
    else:
        print("It is a list.")


except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"Error Type: {type(e)}")
    print(f"Error: {e}")
