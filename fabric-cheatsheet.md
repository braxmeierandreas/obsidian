# Fabric Cheat Sheet (Andreas' Edition)

Ein Spickzettel für die Nutzung von Daniel Miesslers `fabric` im Kontext von Studium, Obsidian und täglicher Produktivität.

---

## 🚀 Grundlagen & Setup

| Befehl | Beschreibung |
| :--- | :--- |
| `fabric --version` | Zeigt die installierte Version. |
| `fabric --list` | Listet alle verfügbaren Patterns (Skills) auf. |
| `fabric -p <pattern> --help` | Zeigt Hilfe und Details zu einem speziellen Pattern. |
| `fabric --update` | Aktualisiert Fabric und die Patterns (wichtig!). |

---

## 🧠 Second Brain & Obsidian Workflow

Wie du Fabric nutzt, um deine Obsidian-Notizen zu verbessern.

### 1. Chaos strukturieren (Brain Dumps)
Verwandle schnelle, unstrukturierte Notizen in sauberes Markdown.
```powershell
# Liest eine "schmutzige" Notiz und gibt eine saubere Struktur aus
fabric -p clean_up_notes -C "Unbenannt.md"
```

### 2. Zusammenfassungen für das Daily Journal
Erstelle eine kompakte Zusammenfassung eines langen Textes für dein Journal.
```powershell
# Den Inhalt in die Zwischenablage kopieren und dann:
fabric -p summarize
```

### 3. Output direkt als neue Notiz speichern
Der **wichtigste Trick** für Obsidian: Leite den Output direkt in eine Datei um.
```powershell
# Analysiert ein Paper und speichert das Ergebnis direkt in deinem Inbox-Ordner
fabric -p extract_wisdom -C "paper.pdf" > "01_Andreas/00_INBOX/Paper_Analyse.md"
```

---

## 🎓 Studium & Universität (Master HFU)

### 1. Vorlesungen nachbereiten
Nutze `extract_wisdom` statt `summarize`. Es extrahiert Kernaussagen, Zitate und Prinzipien – viel besser für akademisches Arbeiten.
```powershell
fabric -p extract_wisdom -C "Mitschrift_Vorlesung.md"
```

### 2. Lernzettel & Prüfungsfragen erstellen
Lass dir vom KI-Modell Fragen zum Stoff stellen.
```powershell
# Erstellt Quizfragen aus deinen Notizen
fabric -p create_quiz -C "Kapitel_3_Zusammenfassung.md"

# Erstellt Karteikarten (Flashcards)
fabric -p create_flashcards -C "Vokabelliste.md"
```

### 3. Komplexe Konzepte verstehen
Wenn ein akademischer Text zu kompliziert ist:
```powershell
fabric -p explain_like_i_am_5 -C "Komplexer_Absatz.txt"
# Oder etwas seriöser:
fabric -p explain_docs -C "Studienordnung.pdf"
```

---

## 🌐 Web, YouTube & Content

### 1. YouTube Videos analysieren (Game Changer)
Spart extrem viel Zeit bei Tutorials oder Vorlesungsaufzeichnungen.
```powershell
# Extrahiert die "Weisheit" aus einem Video URL
fabric -y "https://www.youtube.com/watch?v=VIDEO_ID" -p extract_wisdom
```

### 2. Artikel & Webseiten
Kopiere den Text eines Artikels und lass ihn analysieren.
```powershell
# Text in Zwischenablage -> Pattern -> Ausgabe
pbpaste | fabric -p summarize_newsletter
# (Hinweis: 'pbpaste' ist Mac/Linux. In PowerShell einfach den Text kopieren und 'fabric -p ...' ausführen, es nimmt oft automatisch die Zwischenablage, oder nutze 'Get-Clipboard | fabric ...')
```
*PowerShell Alternative für Clipboard:*
```powershell
Get-Clipboard | fabric -p extract_wisdom
```

---

## 🛠️ Fortgeschrittene Tipps

### Piping (Verkettung)
Du kannst Befehle verketten. Zum Beispiel erst Text extrahieren, dann zusammenfassen.
```powershell
type "Meeting_Notes.txt" | fabric -p clean_up_notes | fabric -p summarize
```

### Kontext (-C) vs. Input
*   `-C "Datei.md"`: Nutzt den Inhalt einer Datei als Kontext.
*   Ohne `-C`: Wartet auf Input (Tippen oder Paste) oder Piping.

### Nützliche Patterns für Andreas
*   `extract_wisdom`: Der "Goldstandard" für fast alles.
*   `write_essay`: Hilft beim Formulieren von Hausarbeiten.
*   `improve_writing`: Korrekturlesen von E-Mails oder Texten.
*   `create_visualization`: Schlägt vor, wie man Daten visualisieren könnte (gut für Mermaid Charts in Obsidian).
*   `translate`: Für deine Spanisch-Lernziele (z.B. `translate_to_spanish`).

---

## 📝 Beispiel-Workflow für heute
1.  Suche dir ein interessantes YouTube-Video zum Thema "Global Health" (für deine Präsentation).
2.  Führe aus: `fabric -y "URL" -p extract_wisdom > "03_UNIVERSITY/01_RESEARCH_PROJECT/Video_Notizen.md"`
3.  Öffne die Datei in Obsidian und bearbeite sie.