# Anki-Synchronisation für Obsidian

Dieses System ermöglicht es, direkt aus Obsidian heraus Karteikarten zu erstellen und mit Anki zu synchronisieren.

---

## 1. Aufbau der Karteikarten (Die Syntax)

Damit das Skript deine Notizen als Karteikarten erkennt, müssen sie einer einfachen Struktur folgen.

### Ordner-Struktur

- **Hauptordner:** Alle Karteikarten gehören in den Ordner `19_FLASHCARDS`.
- **Themen-Ordner:** Erstelle für jedes Thema (z.B. ein Fach oder ein Buch) einen eigenen Unterordner (z.B. `01_Review_Verfahren`).
- **Datei-Decks:** Jede Markdown-Datei (`.md`) innerhalb eines Themen-Ordners wird zu einem eigenen Unter-Deck in Anki.

**Beispiel:**
Die Datei `19_FLASHCARDS\Biologie\Zellbiologie.md` wird in Anki zum Deck `Biologie::Zellbiologie`.

### Datei-Inhalt

Innerhalb einer Markdown-Datei definierst du die Karten wie folgt:

- **Vorderseite:** Eine Zeile, die mit `##` beginnt (z.B. `## Was ist die Hauptstadt von Deutschland?`).
- **Rückseite:** Alles, was direkt darunter bis zur nächsten Trennlinie (`---`) steht.
- **Trennung:** Einzelne Karten werden durch `---` auf einer eigenen Zeile voneinander getrennt.

**Beispiel (`Zellbiologie.md`):**

```markdown
## Was ist die Funktion der Mitochondrien?
Sie sind die Kraftwerke der Zelle und verantwortlich für die Zellatmung und die Produktion von ATP.

---

## Was ist der Zellkern?
Der Zellkern enthält die genetische Information der Zelle in Form von DNA.
```

---

## 2. Einmalige Einrichtung

Damit die Synchronisation funktioniert, müssen folgende Dinge auf deinem System (PC oder Laptop) eingerichtet sein.

### Schritt 1: Anki & AnkiConnect
1.  Installiere das [Anki-Programm](https://apps.ankiweb.net/) auf deinem Computer.
2.  Öffne Anki.
3.  Gehe zu `Extras` > `Erweiterungen`.
4.  Klicke auf `Erweiterung herunterladen...`.
5.  Gib den folgenden Code ein: **`2055492159`**
6.  Starte Anki neu.

**Wichtig:** Anki muss immer im Hintergrund geöffnet sein, wenn du die Synchronisation startest.

### Schritt 2: Python
Stelle sicher, dass [Python](https://www.python.org/downloads/) auf deinem System installiert ist. Bei der Installation, setze den Haken bei "Add Python to PATH".

### Schritt 3: Python-Bibliothek `requests`
Öffne eine Kommandozeile (CMD oder PowerShell) und führe einmalig diesen Befehl aus:
```
pip install requests
```

---

## 3. Synchronisation durchführen

Wenn die Einrichtung abgeschlossen ist, ist die Synchronisation kinderleicht:

1.  Stelle sicher, dass Anki im Hintergrund läuft.
2.  Navigiere zum Ordner `19_FLASHCARDS`.
3.  Führe die Datei **`SYNC_ANKI.bat`** mit einem Doppelklick aus.

Ein schwarzes Fenster erscheint, zeigt den Fortschritt an und schließt sich nach getaner Arbeit. Deine neuen Karten sind nun in Anki!
