import json
import os
import getpass

def setup_comdirect():
    print("==========================================")
    print("   🏦 comdirect REST API Setup-Assistent")
    print("==========================================\n")

    print("Hinweis: Du benötigst Client ID und Client Secret aus dem comdirect Developer Portal.")
    client_id = input("1. Client ID: ").strip()
    client_secret = input("2. Client Secret: ").strip()
    zugangsnummer = input("3. Zugangsnummer: ").strip()
    pin = getpass.getpass("4. PIN (wird nicht angezeigt): ").strip()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(os.path.dirname(BASE_DIR), "CONFIG", "bank_secrets.json")

    config = {}
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)

    config['comdirect'] = {
        "client_id": client_id,
        "client_secret": client_secret,
        "zugangsnummer": zugangsnummer,
        "pin": pin
    }

    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)

    print("\n✅ Konfiguration in 00_SCRIPTS/CONFIG/bank_secrets.json gespeichert.")
    print("Du kannst nun 'python 00_SCRIPTS/bank_sync_comdirect.py' ausführen.")

if __name__ == "__main__":
    setup_comdirect()
