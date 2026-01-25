# Inhalts-Analyse Triggern (BLUF-Prinzip)

KI-Modelle (und Dozenten) haben eine begrenzte Aufmerksamkeitsspanne (Token-Limit). Um sicherzustellen, dass Ihre Kernargumente extrahiert werden, müssen Sie den Text so strukturieren, dass das Wichtigste zuerst kommt.

**BLUF** = **B**ottom **L**ine **U**p **F**ront.

---

## 🏗 Struktur-Strategien für Parser

1.  **Überschriften-Hierarchie:** Nutzen Sie strikt H1 > H2 > H3. Überspringen Sie keine Ebenen. Parser nutzen dies als "Inhaltsverzeichnis".
2.  **Der erste Satz zählt:** Der erste Satz eines Absatzes (Topic Sentence) muss den Inhalt zusammenfassen.
3.  **Signposting:** Nutzen Sie explizite Marker wie "Zusammenfassend lässt sich sagen...", "Der entscheidende Faktor ist...", "Drei Gründe sprechen dafür:".

---

## 🤖 Prompts zur Text-Strukturierung

### 1. Topic Sentences schärfen
Macht Absätze scanbar.

**Prompt:**
> "Überarbeite den folgenden Absatz nach dem 'Topic Sentence'-Prinzip. Der allererste Satz soll die Hauptaussage des gesamten Absatzes glasklar zusammenfassen. Der Rest des Absatzes soll Beweise liefern."
>
> *[Absatz einfügen]*

### 2. Zusammenfassungen generieren (Abstract)
Für den Anfang des Dokuments.

**Prompt:**
> "Erstelle ein akademisches Abstract (max. 250 Wörter) für den folgenden Text. Struktur:
> 1. Problemstellung/Kontext
> 2. Methodik
> 3. Wichtigste Ergebnisse
> 4. Fazit/Implikation
> Verwende eine klare, wissenschaftliche Sprache."

### 3. Argumentations-Check
Prüft, ob die rote Linie erkennbar ist.

**Prompt:**
> "Analysiere den Text und extrahiere die 3 Hauptargumente. Wenn du sie nicht klar finden kannst, sag mir, wo der Text vage bleibt und wie ich die Argumente schärfer formulieren kann."