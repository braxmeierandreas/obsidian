# 💻 02_CODING - Deine Entwicklungs-Zentrale

Hier entstehen "Haushalts-Held", deine Obsidian-Skripte und Python-Automatisierungen.

## 🛠 Verfügbare Power-Tools
1.  **Codebase Investigator** (`codebase_investigator`): Analysiert bestehende Projekte und Strukturen.
2.  **Exa Code Search** (`get_code_context_exa`): Findet Code-Snippets und Doku (StackOverflow, GitHub).
3.  **File Operations** (`write_file`, `read_file`, `run_shell_command`): Zum Erstellen und Testen von Code.

## ⚡ Trigger & Beispiele

### 1. "Haushalts-Held" (Startup)
**Szenario:** Du willst die Datenbank-Struktur aufsetzen.
> **Befehl:** `gemini "Erstelle ein Python-Skript mit SQLAlchemy für 'Haushalts-Held'. Ich brauche Tabellen für User, Verträge (Strom, Gas, Internet) und Kündigungsfristen. Speichere es als 'models.py' hier im Ordner."`

### 2. Obsidian Automatisierung
**Szenario:** Dein Zotero-Skript macht Probleme oder soll erweitert werden.
> **Befehl:** `gemini "Lies @{../00_SCRIPTS/zotero_to_obsidian.py}. Erweitere das Skript so, dass es automatisch Tags basierend auf dem Publikationsjahr hinzufügt."`

### 3. Debugging & Hilfe
**Szenario:** Du bekommst einen Fehler in Python.
> **Befehl:** `gemini "Ich bekomme einen 'KeyError' in meinem Dashboard-Skript. Hier ist der Code: @{../00_SCRIPTS/routine_dashboard_update.py}. Finde den Fehler und korrigiere ihn."`

---
**Wichtig:** Ich kann Shell-Befehle ausführen! Sag mir einfach: *"Führe das Skript aus und zeig mir den Output."*
