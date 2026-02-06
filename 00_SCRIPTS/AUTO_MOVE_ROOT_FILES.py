import os
import shutil
import datetime

# --- KONFIGURATION ---
SOURCE_DIR = r"C:\Users\braxm\obsidian"
DEST_DIR = r"C:\Users\braxm\obsidian\00_INBOX"

# NUR diese Dateien bleiben im Root. Alles andere fliegt raus!
MINIMAL_WHITELIST = [
    "GEMINI.md",             # Brauche ich fuer die KI-Interaktion
    "CLEAN_UP_VAULT.bat",    # Dein Besen
    ".gitignore",
    ".geminiignore",
    ".obsidian"              # Das ist ein Ordner, wird eh ignoriert, aber sicherheitshalber
]

def move_everything_loose():
    moved_count = 0
    print("--- 🧹 Radikaler Root-Sweeper gestartet ---")
    
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)

    for filename in os.listdir(SOURCE_DIR):
        source_path = os.path.join(SOURCE_DIR, filename)

        # Wir verschieben nur Dateien, keine Ordner
        if os.path.isfile(source_path):
            
            # Check gegen die minimale Whitelist
            if filename in MINIMAL_WHITELIST:
                continue

            # Dotfiles (versteckte Systemdateien) lassen wir meistens in Ruhe
            if filename.startswith("."):
                continue

            try:
                dest_path = os.path.join(DEST_DIR, filename)
                
                # Falls Datei schon da ist (z.B. test.md gibt es schon in Inbox)
                if os.path.exists(dest_path):
                    timestamp = datetime.datetime.now().strftime("%H%M%S")
                    name, ext = os.path.splitext(filename)
                    dest_path = os.path.join(DEST_DIR, f"{name}_{timestamp}{ext}")

                shutil.move(source_path, dest_path)
                print(f"📦 Verschoben: {filename}")
                moved_count += 1
            except Exception as e:
                print(f"❌ Fehler bei {filename}: {e}")

    print(f"--- Fertig! {moved_count} lose Dateien in die Inbox verfrachtet. ---")

if __name__ == "__main__":
    move_everything_loose()
    input("Root ist jetzt sauber. Druecke Enter...")
