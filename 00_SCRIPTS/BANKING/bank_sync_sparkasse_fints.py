from fints.client import FinTS3PinTanClient
import json
import os

# --- DEINE DATEN (Lokal gespeichert) ---
BLZ = "DEINE_SPARKASSEN_BLZ"
USER = "DEIN_ANMELDENAME"
PIN = "DEINE_PIN"
END_POINT = "https://fints-hamburg.fints.de/fints/FinTS3PinTanHttpGate" # Beispiel Hamburg

def sync_sparkasse():
    client = FinTS3PinTanClient(
        BLZ,
        USER,
        PIN,
        END_POINT
    )

    # Challenge-Response (TAN) wird hier oft benötigt
    with client:
        # Konten abrufen
        accounts = client.get_sepa_accounts()
        for acc in accounts:
            balance = client.get_balance(acc)
            print(f"Konto {acc.iban}: {balance.amount} {balance.currency}")
            
            # Hier speichern wir den Wert in dein banking_snapshot.json
            output_path = "14_TRADING/02_DATA/banking_snapshot.json"
            # (Logik zum Updaten der JSON)

if __name__ == "__main__":
    print("Sparkasse FinTS Abfrage gestartet...")
    # sync_sparkasse() # Erst nach Installation von fints aktivieren
