# Karteikarten: Metaanalysen Grundlagen & Vertiefung

---

## Frage: Erklären Sie das "Äpfel und Birnen"-Problem bei Metaanalysen.

**Antwort:**
Das Problem, wenn man Studien zusammenfasst, die eigentlich zu unterschiedlich sind, um einen gemeinsamen Durchschnitt zu bilden.
**Beispiel:** Eine Studie untersucht *Kinder mit Aspirin*, die andere *Senioren mit Herz-OP*. Ein gemeinsames Ergebnis wäre biologisch sinnlos ("Obstsalat"), auch wenn man es statistisch berechnen kann.

---

## Frage: Erklären Sie den Unterschied zwischen klinischer, methodischer und statistischer Heterogenität.

**Antwort:**
*   **Klinische Heterogenität:** Unterschiede in PICO (z.B. Teilnehmer, Interventionen).
*   **Methodische Heterogenität:** Unterschiede im Studiendesign (z.B. RCT vs. Kohortenstudie, hohes vs. niedriges Bias-Risiko).
*   **Statistische Heterogenität:** Die Variabilität in den Effektschätzungen (Zahlen), die über den Zufall hinausgeht (gemessen mit I²).
*   *Zusammenhang:* Klinische und methodische Vielfalt verursachen statistische Heterogenität.

---

## Frage: Was ist der entscheidende Unterschied zwischen I² und Tau² bei der Heterogenität?

**Antwort:**
*   **I² (Relative Heterogenität):** Gibt an, *welcher Anteil* der Varianz echt ist (0-100%). Es ist unabhängig von der Skala und gut vergleichbar zwischen Metaanalysen. Sagt aber nichts über die *Größe* der Streuung aus.
*   **Tau² (Absolute Heterogenität):** Gibt die *tatsächliche Größe* der Varianz der wahren Effekte an. Es ist abhängig von der Maßeinheit des Outcomes. Wichtig für die Berechnung des Prädiktionsintervalls.

---

## Frage: Was ist eine Sensitivitätsanalyse in der Metaanalyse?

**Antwort:**
Ein "Stresstest" für die Ergebnisse. Man wiederholt die Analyse unter geänderten Bedingungen, um zu sehen, ob das Ergebnis stabil (robust) bleibt.
**Beispiel:** "Bleibt der Effekt der Intervention signifikant, wenn wir die zwei Studien mit schlechter Qualität (High Risk of Bias) rauslassen?"
*   Wenn ja: Ergebnis ist robust.
*   Wenn nein: Ergebnis ist fragil und hängt von schlechten Studien ab.

---

## Frage: Was ist der Unterschied zwischen einem Konfidenzintervall (CI) und einem Prädiktionsintervall (Prediction Interval) in einer Metaanalyse?

**Antwort:**
*   **Konfidenzintervall (Raute):** Sagt uns etwas über den *Durchschnitt*. "Wir sind zu 95% sicher, dass der wahre *mittlere* Effekt aller Studien hier liegt."
*   **Prädiktionsintervall (Linie unter der Raute):** Sagt uns etwas über die *nächste* Studie. "Wir erwarten, dass der Effekt einer *zukünftigen* einzelnen Studie in diesem Bereich liegen wird."
*   *Bedeutung:* Das Prädiktionsintervall ist immer breiter. Es ist für die klinische Praxis oft wichtiger, da Ärzte Patienten (Einzelfälle) behandeln, keine Durchschnitte.

---

## Frage: Erklären Sie das Fixed-Effect-Modell mit einer Analogie.

**Antwort:**
**Annahme:** Es gibt *einen* wahren Wert für alle.
**Analogie:** Wir wollen die Größe des Mondes messen. Wir haben 5 Teleskope. Jedes misst leicht anders (Messfehler/Zufall), aber alle schauen auf *denselben* Mond. Wir berechnen den Durchschnitt, um den Messfehler zu minimieren.
**Konsequenz:** Große Studien (genaue Teleskope) bekommen extrem viel Gewicht. Nur zulässig bei sehr homogenen Studien!

---

## Frage: Erklären Sie das Random-Effect-Modell mit einer Analogie.

**Antwort:**
**Annahme:** Es gibt *viele* wahre Werte, die ähnlich sind (Verteilung).
**Analogie:** Wir wollen die durchschnittliche Größe von Früchten an einem Baum messen. Nicht jeder Apfel ist gleich groß (echte Unterschiede/Heterogenität). Wir messen 5 Äpfel. Jeder Apfel steht für eine Studie. Wir wollen den Durchschnitt *aller* Äpfel schätzen.
**Konsequenz:** Auch kleinere Studien bekommen Gewicht, weil sie einen weiteren "Apfel" (einen anderen Aspekt der Realität) repräsentieren. Standard in der Medizin.

---

## Frage: Wie interpretiere ich den I²-Wert (Heterogenität) in der Praxis?

**Antwort:**
I² gibt an, wie viel % der Streuung "echt" ist und nicht nur Zufall.
*   **0%:** Homogen.
*   **50%:** Moderate Heterogenität. Man sollte prüfen, warum (Subgruppenanalyse?).
*   **90%:** Erhebliche Heterogenität. Man sollte vielleicht gar keine Metaanalyse rechnen, da der gepoolte Wert wenig Aussagekraft hat.

---

## Frage: Was zeigt ein Funnel Plot (Trichter-Diagramm) und wie sieht er bei Publikationsbias aus?

**Antwort:**
Er zeigt den Zusammenhang zwischen Studiengröße (Präzision, y-Achse) und Effektstärke (x-Achse).
*   **Ohne Bias:** Symmetrisches Dreieck. Kleine Studien streuen breit unten, große Studien liegen eng oben.
*   **Mit Publikationsbias:** Asymmetrie ("angebissener Trichter"). Es fehlen meist die kleinen Studien auf der Seite der "schlechten/negativen" Ergebnisse (links oder rechts unten), weil diese nicht publiziert wurden.

---

## Frage: Was ist die "Trim-and-Fill"-Methode?

**Antwort:**
Eine statistische Methode zur Korrektur von **Publikationsbias**. Sie "erfindet" (imputiert) rechnerisch die fehlenden Studien im Funnel Plot, um die Symmetrie wiederherzustellen und berechnet dann den (korrigierten) Gesamteffekt.

---

## Frage: Was ist eine Netzwerk-Metaanalyse (NMA)?

**Antwort:**
Eine Methode, um **mehr als zwei Interventionen** gleichzeitig zu vergleichen (z.B. Medikament A vs. B vs. C), auch wenn manche davon nie direkt in einer Studie miteinander verglichen wurden (indirekte Vergleiche).

---

## Frage: Was ist ein "indirekter Vergleich" in der Netzwerk-Metaanalyse?

**Antwort:**
Das mathematische Schätzen eines Effekts über einen gemeinsamen Komparator.
*Beispiel:* Wir haben keine Studie "A vs. B". Aber wir haben "A vs. Placebo" und "B vs. Placebo". Über die gemeinsame "Brücke" (Placebo) können wir berechnen, wie A im Vergleich zu B wirkt.

---

## Frage: Was ist die "Transitivitäts-Annahme" bei Netzwerk-Metaanalysen?

**Antwort:**
Die Voraussetzung für indirekte Vergleiche. Sie besagt, dass die Studienpopulationen und Methoden in den "A vs. Placebo"-Studien ähnlich genug sind wie in den "B vs. Placebo"-Studien. Wenn A an jungen Sportlern und B an alten Kranken getestet wurde, ist der indirekte Vergleich ungültig (keine Transitivität).