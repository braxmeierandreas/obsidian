import datetime
import os
import sys

# Pfad zur Obsidian Inbox (Relativ zum Obsidian Root)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
INBOX_PATH = os.path.join(ROOT_DIR, "01_Andreas", "01_DASHBOARD", "01_INBOX", "INBOX.md")

def capture_note(note_text):
    if not note_text:
        print("Fehler: Kein Text zum Speichern übergeben.")
        return

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Formatierung für Obsidian (z.B. als Liste mit Zeitstempel)
    formatted_note = f"- [{now}] {note_text}\n"

    try:
        # Sicherstellen, dass der Ordner existiert
        os.makedirs(os.path.dirname(INBOX_PATH), exist_ok=True)
        
        # Datei im Append-Modus öffnen
        with open(INBOX_PATH, 'a', encoding='utf-8') as f:
            f.write(formatted_note)
        
        print(f"Erfolg: Notiz wurde in die Inbox gespeichert.")
    except Exception as e:
        print(f"Fehler beim Speichern der Notiz: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Alle Argumente nach dem Skriptnamen als eine Notiz zusammenfassen
        note = " ".join(sys.argv[1:])
        capture_note(note)
    else:
        # Interaktive Abfrage, falls keine Argumente übergeben wurden
        note = input("Was möchtest du in die Inbox schreiben? ")
        capture_note(note)
