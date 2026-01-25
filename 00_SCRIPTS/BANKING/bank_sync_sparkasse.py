import json
import os
import sys
import datetime
from fints.client import FinTS3PinTanClient

# Pfade
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(os.path.dirname(BASE_DIR), "CONFIG", "bank_secrets.json")
OUTPUT_PATH = os.path.join(os.path.dirname(BASE_DIR), "14_TRADING", "02_DATA", "banking_snapshot.json")

def sync_sparkasse():
    if not os.path.exists(CONFIG_PATH):
        print(f"❌ Fehler: {CONFIG_PATH} nicht gefunden.")
        return

    with open(CONFIG_PATH, 'r') as f:
        secrets = json.load(f)['sparkasse']

    if secrets['pin'] == "HIER_PIN_EINTRAGEN":
        print("❌ Bitte trage zuerst deine PIN in 00_SCRIPTS/CONFIG/bank_secrets.json ein!")
        return

    print(f"🔗 Verbinde mit Sparkasse (BLZ {secrets['blz']})...")
    
    client = FinTS3PinTanClient(
        secrets['blz'],
        secrets['username'],
        secrets['pin'],
        secrets['fints_url'],
        product_id='ObsidianBot_V1'
    )

    try:
        with client:
            print("🔗 Dialog aufgebaut, frage Konten ab...")
            accounts = client.get_sepa_accounts()
            if not accounts:
                print("⚠️ Keine SEPA-Konten gefunden.")
                return
            
            acc = accounts[0]
            balance = client.get_balance(acc)
            amount = float(balance.amount)
            
            print(f"✅ Kontostand für {acc.iban} erfolgreich abgerufen: {amount} {balance.currency}")

            # Snapshot aktualisieren
            bank_data = {}
            if os.path.exists(OUTPUT_PATH):
                with open(OUTPUT_PATH, 'r') as f:
                    try:
                        bank_data = json.load(f)
                    except:
                        bank_data = {}
            
            bank_data['sparkasse_balance'] = amount
            bank_data['last_update'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            
            with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
                json.dump(bank_data, f, indent=4)
            
            print("📊 Dashboard-Daten aktualisiert.")

    except Exception as e:
        print(f"❌ Fehler: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    sync_sparkasse()
