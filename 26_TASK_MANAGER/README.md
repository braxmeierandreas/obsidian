# 📋 Personal Task Manager System

Dieses Verzeichnis enthält ein automatisiertes Task-Management-System, das Obsidian (Markdown) mit Google Tasks synchronisiert.

## 🚀 Schnellstart

1.  **Aufgaben verwalten:** Öffne `KANBAN_BOARD.md` und füge Aufgaben hinzu.
2.  **Synchronisieren:** Starte `MANAGE_TASKS.bat`.
    *   Synchronisiert Aufgaben (Obsidian ↔ Google Tasks).
    *   Zeigt überfällige Deadlines an.
    *   Öffnet das Board in Obsidian.

## 📂 Dateien & Struktur

*   **`KANBAN_BOARD.md`**: Deine zentrale Aufgabenliste.
    *   Format: Kanban (ToDo, In Progress, Done).
    *   Unterstützt Deadlines: `(due: YYYY-MM-DD)`.
*   **`MANAGE_TASKS.bat`**: Das Haupt-Tool für den manuellen Aufruf.
*   **`sync_and_manage.py`**: Das "Gehirn" des Systems (Python-Skript).
*   **`README.md`**: Diese Datei.

## 🔄 Synchronisation (Bi-Direktional)

Das System hält deine Aufgaben auf dem PC und dem Handy synchron:

1.  **Obsidian ➡️ Google Tasks:**
    *   Neue Aufgaben unter `## TODO` oder `## IN PROGRESS` werden zu Google Tasks hochgeladen.
    *   Erledigte Aufgaben (`- [x]`) werden in Google Tasks als "erledigt" markiert.

2.  **Google Tasks ➡️ Obsidian:**
    *   Aufgaben, die du unterwegs (z.B. in der Google Tasks App) abhakst, werden beim nächsten Sync in `KANBAN_BOARD.md` automatisch auf erledigt (`- [x]`) gesetzt.

## ⏰ Deadlines

Füge Deadlines im Format `(due: YYYY-MM-DD)` zu deinen Aufgaben hinzu:
*   `- [ ] Businessplan abgeben (due: 2026-02-28)`

Das Skript warnt dich farblich codiert:
*   🔴 **ÜBERFÄLLIG**
*   🟠 **BALD FÄLLIG** (in 3 Tagen)
*   🟡 **DIESE WOCHE** (in 7 Tagen)

## 🤖 Automatisierung

Der Sync ist in deine Morgenroutine integriert!
Wenn du `START_MY_DAY.bat` (im Hauptverzeichnis `00_SCRIPTS`) ausführst, wird der Task-Sync automatisch als **Schritt 4/5** durchgeführt.
