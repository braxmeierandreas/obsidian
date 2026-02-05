import os
import datetime
import sys

# Encoding Setup fuer Windows Konsole
sys.stdout.reconfigure(encoding='utf-8')

# --- KONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FILE = os.path.join(BASE_DIR, "TEMPLATES", "Reflexion.md")
LOG_DIR = os.path.join(BASE_DIR, "LOGS")

def ask(question, default=""):
    print(f"\n🔹 {question}")
    answer = input("   > ").strip()
    return answer if answer else default

def create_interactive_entry():
    print("\n" + "="*50)
    print("   🧠 REFLEXION & WACHSTUM - INTERVIEW MODUS")
    print("="*50)
    print("Lass uns den Tag analysieren. Kurz & ehrlich.\n")

    # 1. Daten abfragen
    situation = ask("Was ist passiert? (Objektive Situation)")
    if not situation:
        print("❌ Abbruch: Keine Situation eingegeben.")
        return

    trigger = ask("Was war der Trigger? (Person, Stress, Gedanke?)", default="Unklar")
    reaction = ask("Deine Reaktion? (Gefuehl/Handlung)", default="Unbewusst")
    bias = ask("Welcher Denkfehler? (z.B. Katastrophisieren, Ego)", default="Keiner")
    
    print("\n🔸 Jetzt der wichtige Teil (Lernen):")
    fix = ask("The 1% Fix: Was machst du naechstes Mal anders?", default="Achtsamer sein")
    action = ask("Konkretes Action Item? (Leer lassen fuer keins)", default="")

    # Metadaten (nur Zahlen)
    while True:
        try:
            severity = int(ask("Schweregrad des Fehlers (1-10)?", default="1"))
            break
        except ValueError:
            print("   Bitte eine Zahl eingeben!")

    energy = ask("Dein Energie-Level heute (1-10)?", default="5")

    # 2. Datei vorbereiten
    today = datetime.date.today()
    iso_date = today.strftime("%Y-%m-%d")
    filename = f"{iso_date}_Reflexion.md"
    output_path = os.path.join(LOG_DIR, filename)

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # 3. Template lesen & fuellen
    try:
        with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Ersetzen
        final_content = content.replace("{{date}}", iso_date)
        final_content = final_content.replace("{{situation}}", situation)
        final_content = final_content.replace("{{trigger}}", trigger)
        final_content = final_content.replace("{{reaction}}", reaction)
        final_content = final_content.replace("{{bias}}", bias)
        final_content = final_content.replace("{{fix}}", fix)
        final_content = final_content.replace("{{action}}", action if action else "Nichts definiert")
        final_content = final_content.replace("{{severity}}", str(severity))
        final_content = final_content.replace("{{energy}}", str(energy))

        # Speichern
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_content)
            
        print("\n" + "="*50)
        print(f"✅ Reflexion gespeichert: {filename}")
        print("="*50 + "\n")
        
        # Optional: Datei oeffnen zur Kontrolle
        # os.startfile(output_path) 
        
    except Exception as e:
        print(f"\n❌ FEHLER beim Speichern: {e}")
        input("Enter druecken...")

if __name__ == "__main__":
    create_interactive_entry()