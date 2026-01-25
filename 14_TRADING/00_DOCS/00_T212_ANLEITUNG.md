# 📘 Trading 212 Skript - Anleitung

Diese Datei erklärt, wie du dein Trading 212 Dashboard in Obsidian aktualisierst.

## 🤖 Die KI-Methode (Gemini CLI)

Wenn du morgens deine Daten aktualisieren willst, schreib mir einfach:
*   **"GO"**
*   "Update alles"

Ich starte dann den kompletten Prozess (Depot, Dividenden, Banken) im Hintergrund.

---

## 🚀 Die schnelle Methode (Windows)

Doppelklick auf: `update_t212.bat` im Ordner `14_TRADING`.
Dies aktualisiert alle Dashboards gleichzeitig.

---

## ⚙️ Technische Details

*   **Skript-Pfad:** `C:\Users\braxm\Obsidian\14_TRADING\fetch_t212_data.py`
*   **Ausgabe-Dateien:**
    1.  `C:\Users\braxm\Obsidian\14_TRADING\T212_Dashboard.md` (Trading Cockpit)
    2.  `C:\Users\braxm\Obsidian\14_TRADING\T212_Dividends.md` (Dividenden-Historie)
*   **API-Keys:** Sind fest im Python-Skript hinterlegt.

> **Hinweis:** Das Skript überschreibt bei jedem Durchlauf beide Dateien. Wenn du historische Stände behalten willst, kopiere den Inhalt vorher oder nutze "Speichern unter" in Obsidian.
