# Karteikarten: Metaanalyse – Spezifische Tools und Methoden

---

## Frage 1: Welche spezifischen Effektstärken können in Metaanalysen für kontinuierliche und binäre Outcomes verwendet werden und welche Schätzer und Standardfehleranpassungen sind verfügbar?

**Antwort:**
In Metaanalysen, insbesondere mit Software wie IBM SPSS Statistics, werden spezifische Effektstärken je nach Art des Outcomes verwendet:

**Für kontinuierliche Outcomes (z.B. Mittelwertunterschiede):**
*   **Unstandardisierte Mittelwertdifferenz (Unstandardized Mean Difference):** Direkter Unterschied zwischen den Mittelwerten der Gruppen.
*   **Cohen’s d:** Standardisierte Mittelwertdifferenz, nützlich für Studien mit unterschiedlichen Messskalen.
*   **Hedges’ g:** Korrigierte Version von Cohen’s d, die einen Bias bei kleinen Stichprobengrößen berücksichtigt.
*   **Glass’ delta:** Eine weitere standardisierte Mittelwertdifferenz, die die Standardabweichung der Kontrollgruppe verwendet und geeignet ist, wenn die Standardabweichungen zwischen den Gruppen unterschiedlich sind.

**Für binäre Outcomes (z.B. Häufigkeit eines Ereignisses):**
*   **Log Odds Ratio (Log OR):** Der Logarithmus des Odds Ratios, das die Chancen eines Ereignisses in einer Gruppe im Verhältnis zu einer anderen ausdrückt.
*   **Peto’s Log Odds Ratio:** Eine Variante des Log Odds Ratios, besonders nützlich bei seltenen Ereignissen.
*   **Log Risk Ratio (Log RR):** Der Logarithmus des Relativen Risikos.
*   **Risk Difference (Risikodifferenz):** Der absolute Unterschied in der Ereignishäufigkeit zwischen den Gruppen.

**Verfügbare Schätzer für den Gesamteffekt:**
*   Restricted Maximum Likelihood (REML) (oft Standard)
*   Maximum Likelihood (ML)
*   Empirical Bayes
*   Hedges
*   Hunter-Schmidt
*   DerSimonian-Laird
*   Sidik-Jonkman

**Standardfehleranpassungen:**
*   Keine Anpassung
*   Knapp-Hartung-Anpassung
*   Abgeschnittene Knapp-Hartung-Anpassung

---

## Frage 2: Welche Plot-Typen werden in Metaanalysen zur Visualisierung von Ergebnissen und zur Bias-Diagnose verwendet?

**Antwort:**
Zur Visualisierung von Ergebnissen und zur Diagnose potenzieller Biasquellen in Metaanalysen werden verschiedene Plot-Typen eingesetzt:

*   **Forest Plot (Wald-Diagramm):**
    *   **Zweck:** Zeigt die Effektgrößen und Konfidenzintervalle der einzelnen Studien sowie den gepoolten Gesamteffekt. Dient der visuellen Beurteilung von Effekten und Heterogenität.
*   **Funnel Plot (Trichter-Diagramm):**
    *   **Zweck:** Visualisiert die Beziehung zwischen Effektgröße und Präzision der Studien. Dient zur visuellen Erkennung von Publikationsbias (Asymmetrie deutet auf Bias hin).
*   **Cumulative Forest Plot:**
    *   **Zweck:** Zeigt den kumulativen Effekt einer Metaanalyse, wenn Studien nacheinander hinzugefügt werden (z.B. chronologisch). Kann die Stabilität des Gesamteffekts über die Zeit oder mit zunehmender Evidenz veranschaulichen.
*   **Bubble Plot (Blasen-Diagramm):**
    *   **Zweck:** Wird oft in Meta-Regressionen verwendet, um die Effektgröße gegen eine Moderatorvariable aufzutragen, wobei die Größe der Blasen die Präzision der Studie (z.B. inverser Varianz oder Stichprobengröße) darstellt.
*   **Galbraith Plot (auch Radial Plot):**
    *   **Zweck:** Zeigt die Effektgröße gegen den inversen Standardfehler jeder Studie. Studien, die innerhalb von 95%-Konfidenzintervall-Grenzen um den Gesamteffekt liegen, bilden einen "Trichter". Dient der schnellen visuellen Erkennung von Heterogenität und Ausreißern.
*   **L’Abbé Plot:**
    *   **Zweck:** Stellt die Ereignisraten in der Interventionsgruppe gegen die Ereignisraten in der Kontrollgruppe für binäre Outcomes dar. Hilft, die Heterogenität über verschiedene Studien hinweg zu visualisieren und zu sehen, ob eine Intervention in Studien mit hohen Basisrisiken anders wirkt als in Studien mit niedrigen Basisrisiken.

---
