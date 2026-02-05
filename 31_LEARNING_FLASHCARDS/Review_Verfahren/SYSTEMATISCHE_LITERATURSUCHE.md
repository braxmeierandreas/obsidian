# Karteikarten: Systematische Literatursuche

---

## Frage: Erklären Sie das Spannungsfeld zwischen Sensitivität (Recall) und Präzision (Precision) in der Suche.

**Antwort:**
Es ist ein Trade-off:
*   **Hohe Sensitivität:** Man findet *alles* Relevante, aber auch sehr viel "Müll" (irrelevante Treffer). Ziel von systematischen Reviews ("Nadel im Heuhaufen finden, indem man den ganzen Heuhaufen kauft").
*   **Hohe Präzision:** Man findet fast nur Relevantes, übersieht aber vielleicht wichtige Studien. Eher für schnelle klinische Antworten ("Quick & Dirty").
*   *Strategie im Review:* Man maximiert die Sensitivität auf Kosten der Präzision.

---

## Frage: Warum nutzen wir kontrolliertes Vokabular (z.B. MeSH) *und* Freitextsuche (Keywords) parallel?

**Antwort:**
Um die Schwächen des jeweils anderen auszugleichen:
*   **Nur MeSH:** Man verpasst brandneue Artikel (noch nicht indexiert) oder Artikel, die schlampig indexiert wurden.
*   **Nur Freitext:** Man verpasst Artikel, die andere Synonyme nutzen (z.B. "Cancer" statt "Tumor" oder "Neoplasm").
*   **Kombination (mit OR):** Maximiert die Sensitivität (Recall).

---

## Frage: Was bedeutet "Explosion" (Exploding) bei der MeSH-Suche?

**Antwort:**
Wenn man einen MeSH-Begriff "explodiert", sucht man nicht nur nach diesem Begriff, sondern automatisch auch nach **allen spezifischeren Unterbegriffen** in der Hierarchie.
*Beispiel:* Suche nach `[Infection]` inkludiert automatisch `[Bacterial Infection]`, `[Viral Infection]`, `[Pneumonia]` etc.
Dies erhöht die Sensitivität massiv.

---

## Frage: Was ist der Unterschied zwischen MEDLINE und PubMed?

**Antwort:**
*   **MEDLINE:** Die eigentliche Datenbank mit qualitätsgeprüften, indexierten (MeSH) Artikeln.
*   **PubMed:** Die Suchmaschine (Benutzeroberfläche). PubMed durchsucht MEDLINE, aber *zusätzlich* auch "Pre-prints", Artikel "ahead of print" und manche Bücher, die noch gar keine MeSH-Terms haben.

---

## Frage: Warum ist die Suche nach "Grauer Literatur" wichtig, um Bias zu vermeiden?

**Antwort:**
Um **Publikationsbias** zu reduzieren.
Kommerzielle Verlage publizieren lieber signifikante, positive Ergebnisse. In grauer Literatur (Dissertationen, Behördenberichte, Konferenzabstracts) finden sich oft Studien mit "negativen" oder "null" Ergebnissen. Wenn man diese ignoriert, überschätzt man den Effekt einer Intervention.
