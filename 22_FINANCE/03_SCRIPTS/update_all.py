# -*- coding: utf-8 -*-
import subprocess
import os
import sys

# Pfade
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR) # Gehe eins hoch zu 14_TRADING
FETCH_T212 = os.path.join(SCRIPT_DIR, "fetch_t212_data.py")
ANALYZE_BANK = os.path.join(SCRIPT_DIR, "analyze_banking.py")

def run_update():
    print("🚀 Starte komplettes Finanz-Update (Master Sync)...")
    print("-" * 50)
    
    # 1. Trading 212 & Dividenden
    print("\nStep 1: Trading 212 & Dividenden abrufen...")
    try:
        subprocess.run([sys.executable, FETCH_T212], check=True)
    except Exception as e:
        print(f"❌ Fehler bei Trading 212 Update: {e}")

    # 2. Banking & Master Dashboard
    print("\nStep 2: Bankdaten analysieren & Master Dashboard erstellen...")
    try:
        subprocess.run([sys.executable, ANALYZE_BANK], check=True)
    except Exception as e:
        print(f"❌ Fehler bei Banking Analyse: {e}")

    print("\n" + "-" * 50)
    print("✅ ALLES AKTUALISIERT!")
    print(f"Dashboards bereit in: {BASE_DIR}")

if __name__ == "__main__":
    run_update()
