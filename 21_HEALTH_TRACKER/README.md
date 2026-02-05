# 🏋️ FitTrack CLI - Kalorien & Wasser Tracker

Ein leichtgewichtiges Terminal-Tool zur Verfolgung von Ernährung, Körperwerten und Wasseraufnahme, mit automatischer Obsidian-Integration.

## 🚀 Funktionen
- **Kalorien & Makros:** Manuelle Eingabe oder schnelle Presets (Magerquark, Reis, etc.).
- **Wasser-Tracker:** Schnelles Loggen der täglichen Trinkmenge.
- **Körperwerte:** Verfolgung von Gewicht und Körperfettanteil (KFA).
- **Statistiken:** Automatische Berechnung von Grundumsatz (BMR) und Gesamtumsatz (TDEE).
- **Obsidian Dashboard:** Erstellt/Aktualisiert die Datei `TRACKER_STATS.md` mit:
    - Fortschrittsbalken für Kalorien, Protein und Wasser.
    - Automatischer Generierung von Verlaufsdiagrammen (PNG).
    - Historien-Tabelle der letzten 7 Tage.

## 🛠️ Installation
1. Stelle sicher, dass Python installiert ist.
2. Installiere die Abhängigkeiten (im Ordner `26_CALORIE_TRACKER`):
   ```bash
   pip install -r requirements.txt
   ```

## 📋 Benutzung
- **Einfach:** Doppelklick auf die `TRACK_FITNESS.bat` im Hauptverzeichnis.
- **Terminal:** `python tracker.py` im Ordner `26_CALORIE_TRACKER`.

## ⚙️ Konfiguration
Du kannst dein Profil (Alter, Gewicht, Ziele) direkt in der `tracker.py` im `USER_PROFILE` Dictionary anpassen.

## 📁 Struktur
- `tracker.py`: Das Hauptskript.
- `tracker.db`: SQLite Datenbank (deine Daten).
- `progress_chart.png`: Automatisch generiertes Diagramm.
- `requirements.txt`: Benötigte Python-Bibliotheken.
