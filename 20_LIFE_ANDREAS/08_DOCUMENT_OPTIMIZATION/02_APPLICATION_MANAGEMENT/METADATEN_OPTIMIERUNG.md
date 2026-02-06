# 🛠️ Dokument-Metadaten & Technisches Polishing

Metadaten sind die unsichtbaren Informationen in deiner Datei (PDF/Word). Professionelle Metadaten signalisieren Sorgfalt und technisches Verständnis.

## 1. Die Checkliste vor dem Export
- [ ] **Titel:** Muss dem offiziellen Titel der Arbeit entsprechen (nicht "Hausarbeit_v2_final.pdf").
- [ ] **Autor:** Dein vollständiger Name (Andreas Braxmeier).
- [ ] **Betreff/Thema:** Kurze Zusammenfassung (Abstract) in den Metadaten hinterlegen.
- [ ] **Stichwörter:** 3-5 zentrale Keywords (aus deiner `STRATEGISCHE_KEYWORDS.md`) einbetten.
- [ ] **Sprache:** Korrekte Sprache (de-DE oder en-US) setzen, damit Screenreader und KI-Parser korrekt arbeiten.

## 2. Tools zur Bereinigung
### PDF-Optimierung
Verwende Tools wie `ExifTool` oder `Adobe Acrobat`, um sicherzustellen, dass:
- Alle Schriften eingebettet (embedded) sind.
- Kommentare und "Track Changes" (Änderungen nachverfolgen) entfernt wurden.
- Die Dateigröße optimiert ist (zu große Dateien wirken unprofessionell, zu kleine haben oft schlechte Bildqualität).

## 3. Barrierefreiheit (Digital Accessibility)
KI-Grader bewerten oft die Struktur. Ein barrierefreies Dokument ist automatisch ein "KI-freundliches" Dokument:
- **Überschriften-Hierarchie:** Nutze echte H1, H2, H3 Tags, keine manuelle Fettformatierung.
- **Alt-Texte:** Jede Grafik benötigt eine kurze Beschreibung (siehe `ALT_TEXT_BARRIEREFREIHEIT.md`).
- **Tabellen:** Nutze echte Tabellen-Strukturen, keine Screenshots von Tabellen!

## 4. Namenskonvention (Best Practice)
Speichere deine Datei nach folgendem Muster:
`JJJJMMTT_Masterthesis_Nachname_Vorname_V01.pdf`
*Beispiel:* `20260116_Masterthesis_Braxmeier_Andreas_V01.pdf`
