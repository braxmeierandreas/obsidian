# ☀️ GOOD MORNING, Andreas!

Willkommen in deinem persönlichen Betriebssystem. Dieses Dokument erklärt dir, wie du deinen Tag startest und deine Automatisierung steuerst.

## 🚀 Der Start-Knopf

Alles beginnt mit einer einzigen Datei in diesem Ordner:

`START_MY_DAY.bat`

**Was passiert bei einem Doppelklick?**
1.  **Daten-Sync:** Deine Fitness-Daten (Schritte) und Finanz-Status werden abgerufen.
2.  **Briefing-Generierung:** Ein personalisiertes Morning Briefing wird erstellt.
    *   Es zieht deine aktuellen Termine aus dem Google Kalender.
    *   Es holt deine tägliche **Habit-Checkliste** (angepasst an deinen echten Rhythmus).
    *   Es liefert dir Wetter, News und einen Bibelvers als geistigen Anker.
3.  **Obsidian Start:** Obsidian öffnet sich automatisch und springt direkt in die neue Briefing-Notiz.

---

## ⚙️ Wie passe ich meine Routine an?

Dein System passt sich dir an, nicht umgekehrt. Hier sind die Stellschrauben:

### 1. Habits & Routine ändern
Wenn du deine Weckzeit, deine Sport-Tage oder deine Rituale ändern willst:
👉 **Gehe zu:** `01_Andreas/02_DAILY/02_ROUTINES`

Dort findest du alles Zentral:
*   `00_ROUTINE_HUB.md`: Dein Cockpit.
*   `01_MASTER_CHECKLISTE.md`: Hier änderst du die Habits.
*   `02_HABIT_STATS.md`: Hier siehst du deine Erfolge.

*Das Skript liest jeden Morgen die Master-Checkliste neu ein.*

### 2. Termine & Tagesplan
Dein Tagesplan basiert auf deinem **Google Kalender**.
*   Trage Termine dort ein, damit sie im Briefing erscheinen.
*   Nutze für detaillierte Planung in Obsidian die Vorlagen:
    *   `02_JOURNAL/03_TEMPLATES/TAGESPLAN_WOCHENTAG.md` (Mo-Fr)
    *   `02_JOURNAL/03_TEMPLATES/TAGESPLAN_WOCHENENDE.md` (Sa/So)

### 3. Dashboard
Dein Fortschritt wird hier visualisiert:
👉 **Datei:** `01_Andreas/01_DASHBOARD/DASHBOARD_ANDREAS_BRAXMEIER_VAULT.md`
👉 **Habit-Tracker:** `01_Andreas/01_DASHBOARD/HABIT_TRACKER.md` (Neu!)

---

## 🛠️ Technische Details (Hintergrund)

Das System läuft auf Python-Skripten im Ordner `00_SCRIPTS`.

*   `routine_daily_briefing.py`: Der "Gehirn"-Teil. Erstellt das Markdown-File für den Tag.
*   `routine_dashboard_update.py`: Der "Daten"-Teil. Aktualisiert Zahlen im Dashboard.
*   `google_*.py`: Diverse Helfer für die Kommunikation mit Google (Kalender, Tasks, Fit).

**Voraussetzung:**
Du musst online sein, damit Kalender, Wetter und News geladen werden können.

---

## 🆘 Erste Hilfe

**Das Fenster schließt sich sofort / Fehler?**
1.  Prüfe deine Internetverbindung.
2.  Öffne eine Konsole (CMD) in diesem Ordner und tippe `START_MY_DAY.bat`, um die Fehlermeldung zu sehen.
3.  Oft liegt es an abgelaufenen Google-Tokens. Falls nötig, sage mir (Gemini) Bescheid, ich helfe beim Login-Refresh.

*Viel Erfolg für deinen Tag!*
