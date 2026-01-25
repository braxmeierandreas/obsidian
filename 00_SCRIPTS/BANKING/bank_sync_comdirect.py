import os
import json
import uuid
import time
import requests
import datetime

# Pfade
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(os.path.dirname(BASE_DIR), "CONFIG", "bank_secrets.json")
OUTPUT_PATH = os.path.join(os.path.dirname(BASE_DIR), "14_TRADING", "02_DATA", "banking_snapshot.json")
TOKEN_CACHE = os.path.join(os.path.dirname(BASE_DIR), "CONFIG", "comdirect_tokens.json")

class ComdirectAPI:
    def __init__(self, client_id, client_secret, zugangsnummer, pin):
        self.client_id = client_id
        self.client_secret = client_secret
        self.zugangsnummer = zugangsnummer
        self.pin = pin
        self.base_url = "https://api.comdirect.de/api"
        self.oauth_url = "https://api.comdirect.de/oauth/token"
        self.session = requests.Session()
        self.access_token = None
        self.refresh_token = None
        self.session_id = str(uuid.uuid4())
        self.request_counter = 0

    def get_headers(self, tan=None):
        self.request_counter += 1
        request_id = str(int(time.time() * 1000))[-9:]
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-http-request-info": json.dumps({
                "clientRequestId": {
                    "sessionId": self.session_id,
                    "requestId": request_id
                }
            })
        }
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        if tan:
            headers["x-once-authentication-code"] = tan
        return headers

    def authenticate(self):
        # 1. Versuche Token zu laden und zu refreshen
        if self.load_tokens():
            print("🔄 Versuche Token-Refresh...")
            data = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token
            }
            response = requests.post(self.oauth_url, data=data)
            if response.status_code == 200:
                print("✅ Token-Refresh erfolgreich! (Keine TAN nötig)")
                self.handle_token_response(response.json())
                return True
            else:
                print(f"⚠️ Refresh fehlgeschlagen ({response.status_code}). Fallback zu Login.")

        # 2. Fallback: Voller Login (Password Flow)
        print("🔐 Führe vollständigen Login durch...")
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "password",
            "username": self.zugangsnummer,
            "password": self.pin
        }
        response = requests.post(self.oauth_url, data=data)
        if response.status_code != 200:
            print(f"❌ OAuth Fehler: {response.status_code} - {response.text}")
            return False
        
        self.handle_token_response(response.json())
        return True

    def handle_token_response(self, token_data):
        self.access_token = token_data['access_token']
        self.refresh_token = token_data['refresh_token']
        self.save_tokens(token_data)

    def load_tokens(self):
        if os.path.exists(TOKEN_CACHE):
            try:
                with open(TOKEN_CACHE, 'r') as f:
                    tokens = json.load(f)
                    self.access_token = tokens.get('access_token')
                    self.refresh_token = tokens.get('refresh_token')
                    return True
            except:
                return False
        return False

    def save_tokens(self, token_data):
        os.makedirs(os.path.dirname(TOKEN_CACHE), exist_ok=True)
        with open(TOKEN_CACHE, 'w') as f:
            json.dump(token_data, f)

    def get_sessions(self):
        url = f"{self.base_url}/session/clients/user/v1/sessions"
        response = self.session.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()
        return None

    def validate_session(self, session_uuid):
        url = f"{self.base_url}/session/clients/user/v1/sessions/{session_uuid}/validate"
        payload = {
            "identifier": session_uuid,
            "sessionTanActive": True,
            "activated2FA": True
        }
        response = self.session.post(url, headers=self.get_headers(), json=payload)
        return response

    def activate_session(self, session_uuid, tan):
        url = f"{self.base_url}/session/clients/user/v1/sessions/{session_uuid}"
        payload = {
            "identifier": session_uuid,
            "sessionTanActive": True,
            "activated2FA": True
        }
        response = self.session.patch(url, headers=self.get_headers(tan=tan), json=payload)
        return response

    def get_balances(self):
        url = f"{self.base_url}/banking/clients/user/v1/accounts/balances"
        response = self.session.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()
        return None

def sync_comdirect():
    if not os.path.exists(CONFIG_PATH):
        print(f"❌ Fehler: {CONFIG_PATH} nicht gefunden.")
        return

    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)
        if 'comdirect' not in config:
            print("❌ comdirect Konfiguration fehlt in bank_secrets.json")
            return
        secrets = config['comdirect']

    if secrets['client_id'] == "HIER_CLIENT_ID_EINTRAGEN":
        print("❌ Bitte trage zuerst deine comdirect API-Daten in 00_SCRIPTS/CONFIG/bank_secrets.json ein!")
        return

    api = ComdirectAPI(
        secrets['client_id'],
        secrets['client_secret'],
        secrets['zugangsnummer'],
        secrets['pin']
    )

    print("🔗 Authentifizierung bei comdirect...")
    if not api.authenticate():
        return

    print("🔍 Suche nach aktiven Sessions...")
    sessions = api.get_sessions()
    if not sessions:
        print("❌ Konnte Sessions nicht abrufen.")
        return

    session_uuid = sessions[0]['identifier']
    
    # Prüfen ob Session bereits aktiv ist
    balances = api.get_balances()
    if balances:
        print("✅ Session ist bereits aktiv.")
    else:
        print("⚠️ Session erfordert Aktivierung (PhotoTAN/App-Bestätigung).")
        val_resp = api.validate_session(session_uuid)
        if val_resp.status_code == 201:
            auth_info = json.loads(val_resp.headers.get('x-once-authentication-info', '{}'))
            challenge_typ = auth_info.get('typ')
            print(f"Challenge-Typ: {challenge_typ}")
            
            if challenge_typ == 'P_TAN':
                print("📸 PhotoTAN/App-Bestätigung erforderlich.")
                challenge_path = os.path.join(BASE_DIR, "comdirect_challenge.png")
                try:
                    import base64
                    with open(challenge_path, "wb") as fh:
                        fh.write(base64.b64decode(auth_info.get('challenge')))
                    print(f"🖼️ Challenge wurde unter {challenge_path} gespeichert.")
                except:
                    print("⚠️ Konnte Challenge-Bild nicht speichern.")

            print("\n👉 Bitte bestätige den Auftrag in deiner PhotoTAN-App.")
            print("⏳ Warte 45 Sekunden auf Bestätigung (oder gib die TAN manuell ein)...")
            
            # Non-blocking input attempt or just sleep
            import select
            import sys
            
            tan = ""
            if sys.platform == "win32":
                import msvcrt
                print("TAN (optional): ", end="", flush=True)
                start_time = time.time()
                while time.time() - start_time < 45:
                    if msvcrt.kbhit():
                        char = msvcrt.getche().decode()
                        if char in ['\r', '\n']:
                            break
                        tan += char
                    time.sleep(0.1)
                print()
            else:
                i, o, e = select.select([sys.stdin], [], [], 15)
                if i:
                    tan = sys.stdin.readline().strip()

            # Aktivierung versuchen
            if tan:
                print(f"🔄 Sende TAN zur Aktivierung...")
                act_resp = api.activate_session(session_uuid, tan)
                if act_resp.status_code == 200:
                    print("✅ Session mit TAN aktiviert!")
                else:
                    print(f"⚠️ TAN-Aktivierung fehlgeschlagen: {act_resp.status_code}")
            else:
                print("ℹ️ Keine TAN eingegeben (Push-Verfahren). Prüfe Status...")

            # Prüfen ob Zugriff jetzt möglich ist
            time.sleep(2) # Kurze Pause zur Sicherheit
            balances = api.get_balances()
            
            if not balances:
                 print("❌ Zugriff auf Kontostände weiterhin verweigert.")
                 # Debug: Check response from a raw call to see why
                 debug_resp = api.session.get(f"{api.base_url}/banking/clients/user/v1/accounts/balances", headers=api.get_headers())
                 print(f"DEBUG: Status {debug_resp.status_code} - {debug_resp.text[:200]}")
                 return

    if balances:
        total_balance = 0
        print("\n📊 comdirect Kontostände:")
        for item in balances.get('values', []):
            acc_type = item.get('account', {}).get('accountType', {}).get('text', 'Unbekannt')
            amount = float(item.get('balance', {}).get('amount', 0))
            currency = item.get('balance', {}).get('unit', 'EUR')
            print(f"- {acc_type}: {amount:.2f} {currency}")
            if currency == 'EUR':
                total_balance += amount

        # Snapshot aktualisieren
        bank_data = {}
        if os.path.exists(OUTPUT_PATH):
            with open(OUTPUT_PATH, 'r') as f:
                try:
                    bank_data = json.load(f)
                except:
                    bank_data = {}
        
        bank_data['comdirect_balance'] = total_balance
        bank_data['last_update'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        
        with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
            json.dump(bank_data, f, indent=4)
        
        print("\n✅ Snapshot aktualisiert.")

if __name__ == "__main__":
    sync_comdirect()
