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
    r = requests.get(f"{BASE_URL}/equity/history/dividends", headers=HEADERS)
    divs = r.json().get("items", [])

    print(f"Found {len(divs)} records.")

    # Search for the entry with amount around 6.35
    for d in divs:
        if 6.30 <= d.get('amount', 0) <= 6.40:
            print("\n--- SUSPICIOUS ENTRY ---")
            print(json.dumps(d, indent=4))
        
        # Also print unique 'type' values if they exist
        # print(f"Type: {d.get('type')}") 

except Exception as e:
    print(f"Error: {e}")
