# Karteikarten: Vertiefung Randomisierung & Missing Data

---

## Frage: Was ist der Unterschied zwischen "Generierung" und "Verbergen" der Zuteilungssequenz?

**Antwort:**
*   **Generierung (Generation):** Das *Erstellen* der Zufallsliste (z.B. Computer würfelt eine Liste: A, A, B, A, B).
    *   *Ziel:* Unvorhersehbarkeit.
*   **Verbergen (Concealment):** Das *Geheimhalten* dieser Liste vor den Ärzten/Patienten bis zum Moment des Einschließens.
    *   *Ziel:* Niemand soll die Zuteilung beeinflussen können ("Der nächste ist Gruppe A, da nehme ich lieber den gesünderen Patienten").

---

## Frage: Erklären Sie Blockrandomisierung und wann sie sinnvoll ist.

**Antwort:**
**Prinzip:** Man randomisiert in kleinen Blöcken (z.B. 4er Block: 2x A, 2x B). Sobald 4 Patienten da sind, ist das Verhältnis sicher 2:2.
**Vorteil:** Verhindert bei kleinen Studien oder Zwischenanalysen, dass zufällig viel mehr Patienten in einer Gruppe landen (z.B. AAAA).
**Beispiel:** Bei einer Studie mit nur 20 Patienten sichert dies, dass am Ende 10 in Gruppe A und 10 in Gruppe B sind.

---

## Frage: Erklären Sie Stratifizierte Randomisierung anhand eines Beispiels.

**Antwort:**
**Prinzip:** Man bildet erst Untergruppen (Strata) nach wichtigen Merkmalen und randomisiert dann innerhalb dieser Gruppen separat.
**Beispiel:** Man will sichergehen, dass Alter das Ergebnis nicht verfälscht. Man bildet zwei Töpfe: "Unter 60" und "Über 60". In *beiden* Töpfen wird separat 50:50 randomisiert. So sind am Ende in beiden Therapiegruppen gleich viele Alte und Junge.

---

## Frage: Erklären Sie MCAR (Missing Completely At Random) mit einem Beispiel.

**Antwort:**
Das Fehlen der Daten ist reiner Zufall.
**Beispiel:** Eine Blutprobe fällt im Labor versehentlich runter und geht kaputt. Das hat nichts mit dem Patienten oder seiner Krankheit zu tun.
**Folge:** Kein Bias, nur weniger Daten (weniger Power).

---

## Frage: Erklären Sie MAR (Missing At Random) mit einem Beispiel.

**Antwort:**
Das Fehlen hängt von bekannten Daten ab (die wir gemessen haben), aber nicht vom fehlenden Wert selbst.
**Beispiel:** Wir wissen, dass Männer seltener Fragebögen ausfüllen. Wenn in der Studie Männer fehlen, liegt das am Geschlecht (was wir wissen). Innerhalb der Gruppe der Männer ist das Fehlen aber zufällig.
**Folge:** Kann man statistisch korrigieren, wenn man für das Geschlecht kontrolliert.

---

## Frage: Erklären Sie MNAR (Missing Not At Random) mit einem Beispiel.

**Antwort:**
Das Fehlen hängt direkt mit dem Wert zusammen, der fehlt ("Nicht-ignorable Ausfälle").
**Beispiel:** In einer Studie zu Depression fehlen die Fragebögen der Depressivsten, weil sie antriebslos sind und es nicht schaffen, den Bogen auszufüllen. Uns fehlen also genau die hohen Werte.
**Folge:** Führt zu massivem Bias (Unterschätzung der Depression), schwer zu korrigieren.

---

## Frage: Warum gilt ROBINS-I (für nicht-randomisierte Studien) als besser als die Newcastle-Ottawa Scale (NOS)?

**Antwort:**
*   **NOS (Veraltet):** Basiert auf einem **Punktesystem (Scale)**. Man zählt Punkte ("Stars"), aber das Gewicht der Punkte ist unklar. Es ist oft zu simpel.
*   **ROBINS-I (Modern):** Ist **domänenbasiert** (wie RoB 2). Es bewertet spezifische Probleme (z.B. Confounding) detailliert und zwingt den Reviewer, darüber nachzudenken, *wie* der Bias das Ergebnis beeinflusst (Direction of Bias), statt nur Punkte zu zählen.

---

## Frage: Was ist der "Carry-Over-Effekt" in Cross-Over-Studien?

**Antwort:**
Das Risiko, dass die Wirkung der ersten Behandlung (z.B. Medikament A) noch anhält, während der Patient schon die zweite Behandlung (Medikament B) bekommt. Das verfälscht das Ergebnis von B.

---

## Frage: Was ist eine "Washout-Phase"?

**Antwort:**
Eine behandlungsfreie Pause zwischen den zwei Phasen einer Cross-Over-Studie. Sie dient dazu, Carry-Over-Effekte zu vermeiden, damit das erste Medikament vollständig aus dem Körper ausgeschieden ist, bevor das zweite beginnt.

---

## Frage: Was ist der Intraclass Correlation Coefficient (ICC) bei Cluster-Randomisierten Studien?

**Antwort:**
Ein Maß dafür, wie ähnlich sich die Patienten innerhalb eines Clusters (z.B. einer Arztpraxis oder Schulklasse) sind.
*   Da Patienten im gleichen Cluster oft ähnlich sind (weniger unabhängig), haben Cluster-Studien statistisch weniger Power als normale RCTs.
*   Der ICC wird benötigt, um den "Design Effect" zu berechnen und die Fallzahl entsprechend zu erhöhen.
