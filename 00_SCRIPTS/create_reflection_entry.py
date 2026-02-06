import os
import datetime
import sys

# --- KONFIGURATION ---
# Wir gehen davon aus, dass dieses Skript in 00_SCRIPTS liegt.
# Root ist also ein Level höher.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)

TEMPLATE_FILE = os.path.join(ROOT_DIR, "27_REFLECTION_AND_GROWTH", "99_TEMPLATES", "Reflexions_Template.md")
OUTPUT_DIR = os.path.join(ROOT_DIR, "27_REFLECTION_AND_GROWTH", "01_DAILY_LOG")

def create_entry():
    # Datum ermitteln
    today = datetime.date.today()
    iso_date = today.strftime("%Y-%m-%d")     # 2026-02-05
    
    # Dateiname definieren
    filename = f"{iso_date}_Reflexion.md"
    output_path = os.path.join(OUTPUT_DIR, filename)

    # Prüfen, ob Ordner existiert
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Ordner erstellt: {OUTPUT_DIR}")

    # Prüfen, ob Datei schon existiert
    if os.path.exists(output_path):
        print(f"✅ Die Datei für heute existiert bereits: {filename}")
        print("🚀 Öffne Datei...")
        os.startfile(output_path)
        return

    # Datei neu erstellen
    try:
        print(f"📝 Lese Template...")
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Platzhalter ersetzen
        # Wir ersetzen {{date}} mit dem ISO-Datum für YAML und Text
        new_content = content.replace("{{date}}", iso_date)
        
        print(f"💾 Speichere neue Reflexion...")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"✅ Erfolgreich erstellt: {filename}")
        print("🚀 Öffne Datei...")
        os.startfile(output_path)
        
    except FileNotFoundError:
        print(f"❌ FEHLER: Template nicht gefunden unter: {TEMPLATE_FILE}")
        input("Drücke Enter zum Beenden...")
    except Exception as e:
        print(f"❌ Ein unerwarteter Fehler ist aufgetreten: {e}")
        input("Drücke Enter zum Beenden...")

if __name__ == "__main__":
    create_entry()
