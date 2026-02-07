# ♟️ Schach

Ein einfaches, aber voll funktionsfähiges Schachspiel in Python.

## 🚀 Starten

Doppelklicke einfach auf die Datei **`START_GAME.bat`**.
Das Skript wird automatisch eine virtuelle Umgebung erstellen, die benötigten Bibliotheken (`pygame`, `python-chess`) installieren und das Spiel starten.

## 🎮 Steuerung

- **Maus:** Klicke auf eine Figur, um sie auszuwählen. Klicke auf ein Zielfeld, um sie zu bewegen.
- **Regeln:** Das Spiel nutzt die offizielle `python-chess` Bibliothek, kennt also alle Regeln (Rochade, En Passant, Remis, Schachmatt).
- **Promotion:** Bauern werden aktuell automatisch zur Dame umgewandelt, um den Spielfluss einfach zu halten.

## 🛠️ Technologie

- **Engine:** `python-chess` (für Logik und Regelüberprüfung)
- **GUI:** `pygame` (für die Darstellung)
- **Assets:** Nutzt Unicode-Schachsymbole und System-Schriftarten (keine externen Bilder nötig).
