import os
import shutil
import time
import pandas as pd
import json

WATCH_DIR = os.path.expanduser("~/Downloads")
TARGET_DATA = "C:/Users/braxm/Meine Ablage/Obsidian/14_TRADING/02_DATA/banking_snapshot.json"

def process_revolut_csv(file_path):
    print(f"Verarbeite Revolut CSV: {file_path}")
    try:
        df = pd.read_csv(file_path)
        # Revolut CSVs haben meist eine Spalte 'Balance' oder wir berechnen den letzten Stand
        # Wir nehmen den aktuellsten Kontostand
        latest_balance = df['Balance'].iloc[0] # Beispiel
        
        with open(TARGET_DATA, 'r') as f:
            data = json.load(f)
        
        data['revolut_balance'] = float(latest_balance)
        data['last_update'] = time.strftime("%Y-%m-%d %H:%M")
        
        with open(TARGET_DATA, 'w') as f:
            json.dump(data, f, indent=4)
            
        print(f"✅ Revolut Stand aktualisiert: {latest_balance} €")
        os.remove(file_path) # Datei löschen nach Import
    except Exception as e:
        print(f"Fehler beim Import: {e}")

def start_watchdog():
    print(f"Beobachte {WATCH_DIR} nach Revolut CSVs...")
    while True:
        for file in os.listdir(WATCH_DIR):
            if file.startswith("account-statement") and file.endswith(".csv"):
                process_revolut_csv(os.path.join(WATCH_DIR, file))
        time.sleep(10) # Alle 10 Sekunden prüfen

if __name__ == "__main__":
    start_watchdog()
