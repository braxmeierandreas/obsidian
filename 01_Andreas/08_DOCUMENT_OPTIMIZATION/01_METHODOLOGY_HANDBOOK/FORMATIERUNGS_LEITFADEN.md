# Formatierungs-Leitfaden für Maschinenlesbarkeit

Ein Dokument mag für das menschliche Auge perfekt aussehen, aber für eine Maschine "kaputt" sein. Dieser Leitfaden hilft, technische Barrieren zu entfernen, damit Parser (wie ATS oder KI-Tools) den Text linear und korrekt verarbeiten können.

---

## 🚫 Die Top-Killer für Parser

1.  **Textfelder (Floating Boxes):**
    *   **Problem:** Text in Word-Textfeldern wird oft erst ganz am Ende des Dokuments ausgelesen, wodurch der logische Zusammenhang verloren geht. Ein Parser liest Stream-basiert (von oben links nach unten rechts im Code, nicht visuell).
    *   **Lösung:** Schreiben Sie im Haupttextfluss. Nutzen Sie Spalten-Layouts statt freischwebender Textfelder für mehrspaltiges Design.

2.  **Kreative Schriftarten & Icons:**
    *   **Problem:** Einige Design-Schriftarten kodieren Zeichen nicht standardkonform. Ein visuelles "A" ist im Code vielleicht ein Sonderzeichen. Icons werden oft als "Müll-Zeichen" interpretiert.
    *   **Lösung:** Nutzen Sie Unicode-Standardschriftarten (Arial, Calibri, Roboto, Times New Roman, Helvetica). Nutzen Sie Standard-Bulletpoints statt Bilder.

3.  **Harte Zeilenumbrüche:**
    *   **Problem:** Mitten im Satz `Enter` drücken, damit der Zeilenumbruch optisch "schön aussieht".
    *   **Folge:** Parser lesen dies als Satzende. Der Satz wird zerhackt, der Kontext geht für die KI verloren.
    *   **Lösung:** Nutzen Sie die automatische Silbentrennung und saubere Seitenränder.

---

## 🤖 Prompts zur Text-Reinigung & Prüfung

### 1. OCR-Fehler und Umbrüche bereinigen
Wenn Sie Text aus PDFs kopieren, entstehen oft Fehler.

**Prompt:**
> "Bereinige den folgenden Text von OCR-Fehlern (z.B. falsche harte Zeilenumbrüche mitten im Satz, 'rn' statt 'm', verwechselte Buchstaben). Entferne Trennstriche am Zeilenende. Erhalte den ursprünglichen Wortlaut bei, korrigiere nur Rechtschreibung und Formatierung für optimalen Lesefluss."

### 2. Plain-Text Konvertierung (Der "Röntgenblick")
Um zu prüfen, was die KI "sieht".

**Prompt:**
> "Wandle den folgenden formatierten Text in reines Markdown um. Entferne alle dekorativen Elemente, Tabellen-Layouts und Kopfzeilen. Behalte aber die logische Struktur (Überschriften H1-H3, Listen) bei. Dies dient dazu, zu prüfen, ob die Struktur logisch aufeinander aufbaut."

---

## 🛠 Export-Settings (PDF)
Achten Sie beim Export aus Word/InDesign auf folgende Einstellungen:
*   [x] **Tags für Barrierefreiheit einschließen** (Essenziell für die logische Struktur!)
*   [x] **Lesezeichen erstellen** (Generiert aus Überschriften ein Inhaltsverzeichnis im PDF).
*   [ ] **Text in Pfade umwandeln** (NIEMALS tun! Das macht den Text als Bild flach und unsichtbar für die Suche.)
