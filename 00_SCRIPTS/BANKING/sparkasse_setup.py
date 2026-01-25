import sys
import getpass
from fints.client import FinTS3PinTanClient

def setup():
    print("==========================================")
    print("   🏦 Sparkasse FinTS/HBCI Setup-Assistent")
    print("==========================================\n")

    blz = input("1. Bitte gib deine Sparkassen BLZ ein: ").strip()
    user = input("2. Dein Anmeldename / Legitimations-ID: ").strip()
    pin = getpass.getpass("3. Deine PIN (wird nicht angezeigt): ").strip()

    # Standard-URL Schema für Sparkassen
    # Viele Sparkassen nutzen: https://fints.sparkasse-remscheid.de/fints/FinTS3PinTanHttpGate (Beispiel)
    # Wir versuchen eine gängige Liste oder lassen den User suchen
    
    # Hinweis: In einem produktiven Skript würde man hier eine BLZ-Datenbank abfragen.
    # Für den Start versuchen wir den Standard-Weg:
    print(f"\nVersuche Verbindung zur Sparkasse (BLZ {blz}) aufzubauen...")
    
    # Bekannte Sparkassen-Endpunkte (Beispiele)
    # Wenn deiner nicht dabei ist, kann man ihn oft auf der Website der Sparkasse unter "HBCI" finden.
    url = f"https://fints.sparkasse.de/fints/FinTS3PinTanHttpGate" # Allgemeiner Einstiegspunkt
    
    client = FinTS3PinTanClient(blz, user, pin, url)

    try:
        with client:
            print("✅ Verbindung erfolgreich!")
            accounts = client.get_sepa_accounts()
            print(f"\nGefundene Konten ({len(accounts)}):")
            for i, acc in enumerate(accounts):
                print(f"[{i}] {acc.iban} ({acc.account_number})")
            
            # Speichere Konfiguration lokal (OHNE PIN)
            config = {
                "blz": blz,
                "user": user,
                "url": url,
                "accounts": [{"iban": a.iban, "id": a.account_number} for a in accounts]
            }
            
            # Hier könntest du entscheiden, ob du die PIN (unsicher) oder einen Keyring nutzen willst.
            # Für den Anfang lassen wir es bei der manuellen Eingabe oder einer lokalen config.json.
            
    except Exception as e:
        print(f"\n❌ Fehler beim Login: {e}")
        print("\nHinweis: Prüfe BLZ, Nutzer und ob FinTS bei deiner Sparkasse aktiviert ist.")

if __name__ == "__main__":
    setup()
