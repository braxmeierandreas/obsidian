# Alt-Text & Barrierefreiheit für KI-Analyse

Bilder, Diagramme und Tabellen in PDFs sind für einfache Text-Parser oft "blinde Flecken". Durch das Hinzufügen von **Alt-Texten** (Alternativtexten) machen Sie diese Daten für KI-Systeme (und Screenreader) lesbar. Dies erhöht die Chance, dass Ihre grafisch dargestellten Daten in einer automatischen Analyse berücksichtigt werden.

---

## 🖼 Wo Alt-Texte platziert werden
*   **Word:** Rechtsklick auf Bild > "Alternativtext anzeigen".
*   **PDF:** Nutzung der Tags-Struktur (Barrierefreiheits-Tools in Acrobat).

---

## 🤖 Prompts für "Data-Dense" Alt-Texte

### 1. Diagramm-Interpretation
Verwandeln Sie eine Grafik in reinen Text, den die KI verstehen kann.

**Prompt:**
> "Beschreibe die angehängte Grafik (Diagramm) so präzise, dass jemand die Daten ohne das Bild verstehen kann.
> Struktur:
> 1. Was zeigt das Diagramm (Titel/Achsen)?
> 2. Was sind die genauen Datenpunkte (Max/Min/Trends)?
> 3. Was ist die Kern-Aussage (Insight)?
> Der Text soll als 'Alt-Text' für ein wissenschaftliches Paper dienen."

### 2. Komplexe Modelle beschreiben
Für Flussdiagramme oder Prozessmodelle.

**Prompt:**
> "Erstelle eine textuelle Beschreibung dieses Prozessmodells. Gehe Schritt für Schritt vor: 'Schritt A führt zu Entscheidung B. Wenn Ja, dann C, sonst D'. Verwende eine logische, nummerierte Liste."

---

## 📝 Beispiel für guten Alt-Text

**Schlecht:** "Ein Balkendiagramm über Umsatz."
**Gut:** "Balkendiagramm 'Jahresumsatz 2025 nach Quartal'. Zeigt einen stetigen Anstieg von Q1 (10k€) bis Q4 (50k€). Der stärkste Zuwachs erfolgte zwischen Q3 und Q4 (+40%). Das Diagramm belegt die These der saisonalen Kaufkraft."