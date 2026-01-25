import duolingo
import datetime
import os

# --- Deine Daten ---
USERNAME = 'braxmeierandreas'
PASSWORD = '$ftHnxSJ1ZGh0TvBgpgvPWc1Jtwn0q1gaEyRQ' # Dein Duolingo-Passwort
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))
VAULT_PATH = os.path.join(ROOT_DIR, '09_LEARNING_SPANISH', '08_DUOLINGO', 'Duolingo_Stats.md')

def get_duo_data():
    try:
        print(f"Versuche Login für {USERNAME} mit der duolingo-API Bibliothek...")
        lingo = duolingo.Duolingo(USERNAME, PASSWORD)
        
        user_info = lingo.get_user_info()
        streak_info = lingo.get_streak_info()
        
        # Extrahiere benötigte Daten basierend auf der Dokumentation
        streak = streak_info.get('site_streak', 0)
        total_xp = user_info.get('xp', 0) # 'xp' is found under user_info in many examples

        # Some sources indicate 'total_xp' is directly under user_info, others 'xp'
        # Let's try to be robust and check both.
        if 'total_xp' in user_info:
            total_xp = user_info['total_xp']


        # Zeitstempel für das Tracking (1% better every day)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Markdown Content erstellen
        content = f"""---
updated: {now}
type: tracking
---
## 🦉 Duolingo Progress: {USERNAME}
- **Aktueller Streak:** 🔥 {streak} Tage
- **Gesamt-XP:** ⚡ {total_xp}
- **Sprache:** 🇪🇸 Spanisch (Ziel: B1)
- **Status:** 💎 Diamond League

---
*Automatisch generiert für den Haushalts-Held-Service am {now}.*
"""
        
        # In Obsidian Vault schreiben
        with open(VAULT_PATH, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"Erfolg! Deine Stats wurden nach {VAULT_PATH} exportiert.")

    except Exception as e:
        print(f"Fehler beim Abruf: {e}")
        # If the error is related to authentication, suggest checking credentials
        if "login" in str(e).lower() or "authentication" in str(e).lower() or "unauthorized" in str(e).lower():
             print("Möglicherweise sind die Duolingo-Anmeldedaten (Benutzername/Passwort) falsch oder Duolingo hat seine API geändert. Bitte überprüfen Sie Ihr Passwort im Skript.")

if __name__ == "__main__":
    get_duo_data()