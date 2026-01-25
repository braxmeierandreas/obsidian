# Karteikarten: Metaanalysen

---

## Frage 1: Was sind Effektstärken und welche Stärken eignen sich in Metaanalysen?

**Antwort:**
**Effektstärken** sind quantitative Maße, die die Größe eines Effekts oder einer Beziehung zwischen Variablen ausdrücken. Sie machen die Ergebnisse verschiedener Studien vergleichbar und sind der Kern einer Metaanalyse.

**Geeignete Effektstärken in Metaanalysen:**
*   **Für dichotome (binäre) Daten:**
    *   Odds Ratios (OR)
    *   Relative Risiken (RR)
    *   Risiko-Differenzen
*   **Für metrische (kontinuierliche) Daten:**
    *   Cohen’s d (Standardmaß für Mittelwertunterschiede)
    *   Hedges’ g (Variante von Cohen's d, besonders geeignet für kleine Stichproben)
    *   Glass’ delta (Geeignet, wenn die Streuungen in den Gruppen unterschiedlich sind)
*   **(Generell, auch außerhalb von Metaanalysen):** Phi und Cramer‘s V (für den Chi-Quadrat-Test zur Beschreibung der Stärke des Zusammenhangs in Kreuztabellen).

---

## Frage 2: Was unterscheidet Random-Effect-Modell und Fixed-Effect-Modelle in Metaanalysen?

**Antwort:**

**Fixed-Effect-Modell (Modell mit festen Effekten):**
*   **Annahme:** Geht davon aus, dass alle eingeschlossenen Studien denselben "wahren" Behandlungseffekt schätzen.
*   **Variabilität:** Beobachtete Unterschiede zwischen den Studienergebnissen werden ausschließlich auf Zufallsschwankungen (Messfehler oder Stichprobenfehler) zurückgeführt.
*   **Implikation:** Bei unendlich großen Stichproben würden die Unterschiede zwischen den Studien verschwinden.
*   **Voraussetzung:** Selten realistisch, da es gleiche Studienpopulation, Auswahlkriterien und Behandlung in allen Studien voraussetzt.
*   **Gewichtung:** Studien werden invers proportional zu ihrer Varianz gewichtet; größere Studien mit geringerer Varianz erhalten mehr Gewicht.

**Random-Effect-Modell (Modell mit zufälligen Effekten):**
*   **Annahme:** Geht davon aus, dass die wahren Behandlungseffekte zwischen den Studien variieren können (z.B. aufgrund realer Unterschiede in Population, Intervention, Setting oder Studiendesign). Jede Studie hat einen eigenen, aber verwandten wahren Effekt.
*   **Variabilität:** Beobachtete Unterschiede resultieren sowohl aus den realen Unterschieden der Effekte zwischen den Studien (Heterogenität) als auch aus Zufallsschwankungen.
*   **Implikation:** Auch bei unendlich großen Stichproben würden die Effektschätzungen zwischen den Studien variieren.
*   **Ursachen für Heterogenität:** Unterschiede in Studienpopulationen (z.B. Alter), Interventionen (z.B. Dosierung), Nachbeobachtungsdauer oder andere studienbezogene Faktoren.
*   **Gewichtung:** Studien werden invers proportional zur Summe aus ihrer Varianz und dem Heterogenitätsparameter (Tau²) gewichtet. Auch kleinere Studien erhalten ein gewisses Gewicht.

---

## Frage 3: Wie lässt sich ein Forest-Plot lesen?

**Antwort:**
Ein **Forest-Plot** ist eine grafische Darstellung der Ergebnisse einer Metaanalyse.

**Bestandteile und Lesart:**
*   **Einzelne Studien:** Jede horizontale Linie repräsentiert eine einzelne Studie.
    *   **Quadrat:** Zeigt die Punktschätzung des Effekts der jeweiligen Studie. Die Größe des Quadrats ist proportional zur Gewichtung der Studie in der Metaanalyse (größere Studien haben größere Quadrate).
    *   **Horizontale Linie:** Das Konfidenzintervall (z.B. 95%-KI) der Effektschätzung der einzelnen Studie.
*   **Vertikale Linie der "No-Effekt":** Eine vertikale Linie (oft bei 0 für Mittelwertdifferenzen oder bei 1 für Odds Ratios/Relative Risiken), die den Punkt des fehlenden Effekts oder der Gleichheit anzeigt.
    *   Kreuzt das Konfidenzintervall einer Studie diese Linie, ist der Effekt dieser Studie nicht statistisch signifikant.
*   **Gesamteffekt (Summary Effect):** Unten im Plot wird ein rautenförmiges Symbol (oder eine andere Form) dargestellt.
    *   **Mitte der Raute:** Repräsentiert die gepoolte (zusammengefasste) Punktschätzung des Effekts aus allen Studien.
    *   **Breite der Raute:** Zeigt das Konfidenzintervall für den Gesamteffekt an.
    *   Kreuzt auch das Konfidenzintervall der Raute die Linie der "No-Effekt", ist der Gesamteffekt der Metaanalyse nicht statistisch signifikant.
*   **Heterogenitätsmaße:** Oft werden am unteren Rand des Plots auch Angaben zur Heterogenität (z.B. I²-Statistik, Tau²) gemacht.

---

## Frage 4: Wie lässt sich die Heterogenität von Metaanalysen bewerten?

**Antwort:**
**Heterogenität** beschreibt die Variabilität der wahren Effekte zwischen den Studien in einer Metaanalyse. Ihre Bewertung ist entscheidend, um zu beurteilen, ob eine statistische Zusammenfassung der Ergebnisse sinnvoll ist.

**Kennzahlen zur Bewertung der Heterogenität:**
*   **Tau² (Tau-Quadrat):**
    *   Ein **absolutes Maß** der Heterogenität.
    *   Beschreibt die *Streuung der wahren Effekte* zwischen den Studien.
    *   Je größer Tau², desto heterogener sind die Studien. Der Wertebereich ist abhängig von den verwendeten Effektmaßen.
*   **I²-Statistik:**
    *   Ein **relatives Maß** der Heterogenität, das den Prozentsatz der Gesamtvariation angibt, der auf die wahre Heterogenität (und nicht auf Zufall) zurückzuführen ist.
    *   Wertebereich von 0% (keine Heterogenität) bis 100% (sehr hohe Heterogenität).
    *   **Faustregeln für die Interpretation:**
        *   0% bis 40%: Kaum Heterogenität
        *   30% bis 60%: Moderate Heterogenität
        *   50% bis 90%: Deutliche Heterogenität
        *   75% bis 100%: Sehr deutliche Heterogenität (kann die Aussagekraft der Studienergebnisse in Frage stellen).

**Strategien zur Reduzierung/Erklärung von Heterogenität:**
*   **Datenqualität prüfen:** Ausschluss von Studien minderer Qualität oder Durchführung von Sensitivitätsanalysen.
*   **Subgruppenanalysen:** Untersuchung, ob die Heterogenität durch spezifische Studiencharakteristika (z.B. Patientenpopulation, Interventionstyp, Studiendesign) erklärt werden kann.
*   **Metaregression:** Statistische Methode zur Erklärung von Heterogenität durch Kovariaten.
*   **Narrative Ergebnisdarstellung:** Bei sehr hoher und unerklärlicher Heterogenität (>75-90% I²) kann es sinnvoller sein, die Ergebnisse narrativ statt statistisch zusammenzufassen.

---

## Frage 5: Was ist ein Publication Bias (Publikationsverzerrung) und wie lässt er sich erkennen?

**Antwort:**
**Publication Bias (Publikationsverzerrung)** tritt auf, wenn die Wahrscheinlichkeit, dass Studienergebnisse veröffentlicht werden, systematisch von der Art, Richtung oder Signifikanz der Ergebnisse abhängt. Typischerweise werden Studien mit statistisch signifikanten oder "positiven" Ergebnissen eher veröffentlicht als Studien mit nicht-signifikanten oder "negativen" Ergebnissen. Dies führt zu einer verzerrten Darstellung der Evidenz und kann die Ergebnisse von Metaanalysen verfälschen.

**Erkennung von Publication Bias:**
*   **Funnel-Plot:**
    *   Ein **Funnel-Plot** ist eine Streudiagramm, das die Effektstärken der einzelnen Studien (auf der X-Achse) gegen ein Maß für deren Präzision (z.B. den Standardfehler oder die Stichprobengröße, auf der Y-Achse) aufträgt.
    *   Bei Abwesenheit von Publikationsbias sollten die Punkte eine **symmetrische, umgekehrte Trichterform** bilden: Präzisere Studien (große Stichproben) haben engere Konfidenzintervalle und liegen oben dichter beieinander, während weniger präzise Studien (kleinere Stichproben) breitere Intervalle haben und unten weiter streuen.
    *   **Asymmetrie** (z.B. Fehlen von kleinen Studien mit nicht-signifikanten oder negativen Ergebnissen auf einer Seite des Plots) deutet auf Publikationsbias hin.
*   **Statistische Tests:**
    *   **Egger’s Test:** Ein statistischer Test, der die Asymmetrie des Funnel-Plots prüft. Ein signifikanter p-Wert bei diesem Test deutet auf das Vorhandensein von Publikationsbias hin.
    *   **Beggs Test:** Ein weiterer statistischer Test zur Bewertung der Symmetrie von Funnel-Plots.
*   **Trim-and-Fill-Methode:** Eine Methode, um den möglichen Einfluss von Publikationsbias abzuschätzen und ggf. fehlende Studien zu "imputieren", um einen korrigierten Gesamteffekt zu erhalten.

---

## Frage 6: Was lassen sich Anwendung, Stärken und Schwächen von Metaanalysen beschreiben?

**Antwort:**

**Anwendung von Metaanalysen:**
*   Zusammenfassung des gesamten Forschungsstandes zu einer spezifischen wissenschaftlichen Frage.
*   Präzisere Schätzung des wahren Effekts einer Intervention oder eines Zusammenhangs.
*   Identifizierung von Subgruppen, die von einer Intervention besonders profitieren könnten.
*   Erklärung von Inkonsistenzen und Heterogenität zwischen Studienergebnissen.
*   Grundlage für evidenzbasierte Entscheidungen in Klinik, Praxis und Politik sowie für die Entwicklung von Leitlinien.

**Stärken von Metaanalysen:**
*   **Erhöhte statistische Power:** Durch die Kombination von Daten aus mehreren Studien können auch kleine Effekte entdeckt werden, die in Einzelstudien unentdeckt blieben.
*   **Präzisere Effektschätzung:** Der gepoolte Effekt ist oft eine genauere Schätzung des wahren Effekts.
*   **Reduktion von Zufallsfehlern:** Zufällige Fehler in Einzelstudien gleichen sich im Durchschnitt aus.
*   **Identifikation von Heterogenität:** Ermöglicht die systematische Untersuchung, warum Studienergebnisse variieren.
*   **Objektivität und Transparenz:** Ein systematischer Ansatz reduziert die Subjektivität im Vergleich zu narrativen Reviews.
*   **Höchste Evidenzstufe:** Werden in der Hierarchie der Evidenz oft als Studien mit dem höchsten Evidenzgrad angesehen (insbesondere Metaanalysen von RCTs).

**Schwächen von Metaanalysen:**
*   **"Garbage in, garbage out":** Die Qualität der Metaanalyse hängt direkt von der Qualität der eingeschlossenen Primärstudien ab. Schlechte Studien führen zu schlechten Metaanalysen.
*   **Anfälligkeit für Publikationsbias:** Eine Metaanalyse kann zu falschen Schlussfolgerungen führen, wenn relevante Studien (insbesondere solche mit nicht-signifikanten Ergebnissen) nicht veröffentlicht wurden.
*   **"Äpfel und Birnen"-Problem:** Wenn die eingeschlossenen Studien zu heterogen sind (z.B. zu unterschiedliche Populationen, Interventionen, Outcomes), ist eine statistische Zusammenfassung nicht sinnvoll und kann irreführend sein.
*   **Methodischer Aufwand:** Die Durchführung erfordert detaillierte methodologische und statistische Kenntnisse.
*   **Potenzielle Vereinfachung:** Komplexe Sachverhalte können durch eine reine Zahlenzusammenfassung übermäßig vereinfacht werden.

---
