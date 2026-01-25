# 3. Rentabilitätsvorschau (Gewinn- und Verlustrechnung)

---

Die Rentabilitätsvorschau (auch Gewinn- und Verlustrechnung, GuV, genannt) ist das Ergebnis deiner Umsatz- und Kostenplanung. Hier zeigt sich, ob dein Unternehmen auf dem Papier profitabel ist und wann du voraussichtlich die Gewinnzone erreichst (den Break-Even-Point).

Diese Vorschau ist eine der wichtigsten Tabellen für dich und für potenzielle Investoren. Sie zeigt die wirtschaftliche Leistungsfähigkeit deiner Idee über die Zeit.

**Basis:** Die Excel/Google Sheets-Tabelle aus dem vorherigen Dokument `02_Umsatz-und_Kostenplanung.md`.

---

## Aufbau der Rentabilitätsvorschau

Du erweiterst deine bestehende Tabelle um die folgenden Berechnungen. Plane wieder das erste Jahr auf Monatsbasis und die Jahre 2 und 3 auf Jahresbasis.

**Vorlage für die Rentabilitätsvorschau (vereinfacht):**

| Position                             | Monat 1   | Monat 2   | ... | **Jahr 1 (Summe)** | **Jahr 2** | **Jahr 3** |
| ------------------------------------ | --------- | --------- | --- | ------------------ | ---------- | ---------- |
| **1. Gesamtumsatz**                  | 1.222 €   | 1.848 €   | ... | **35.000 €**       | 120.000 €  | 298.000 €  |
|                                      |           |           |     |                    |            |            |
| **2. Variable Kosten**               | -20 €     | -48 €     | ... | **-1.500 €**       | -6.000 €   | -15.000 €  |
| **= Deckungsbeitrag 1**              | **1.202 €** | **1.800 €** | ... | **33.500 €**       | 114.000 €  | 283.000 €  |
|                                      |           |           |     |                    |            |            |
| **3. Fixe Kosten**                   |           |           |     |                    |            |            |
| - Personalkosten (Unternehmerlohn etc.) | -3.300 €  | -3.300 €  | ... | **-39.600 €**      | -45.000 €  | -80.000 €  |
| - Marketingkosten                    | -650 €    | -650 €    | ... | **-8.000 €**       | -12.000 €  | -20.000 €  |
| - Betriebskosten (Software, Miete...) | -250 €    | -250 €    | ... | **-3.000 €**       | -4.000 €   | -6.000 €   |
| - Abschreibungen                     | -33 €     | -33 €     | ... | **-400 €**         | -400 €     | -400 €     |
| **= Summe Fixe Kosten**              | **-4.233 €**| **-4.233 €**| ... | **-51.000 €**      | -61.400 €  | -106.400 € |
|                                      |           |           |     |                    |            |            |
| **= Betriebsergebnis (EBIT)**        | **-3.031 €**| **-2.433 €**| ... | **-17.500 €**      | **52.600 €** | **176.600 €**|
|                                      |           |           |     |                    |            |            |
| - Zinsen (für Kredite)               | -150 €    | -150 €    | ... | **-1.800 €**       | -1.500 €   | -1.000 €   |
| **= Ergebnis vor Steuern (EBT)**     | **-3.181 €**| **-2.583 €**| ... | **-19.300 €**      | **51.100 €** | **175.600 €**|
|                                      |           |           |     |                    |            |            |
| - Steuern (z.B. 30% auf Gewinn)      | 0 €       | 0 €       | ... | **0 €**            | -15.330 €  | -52.680 €  |
| **= Jahresüberschuss / Gewinn/Verlust** | **-3.181 €**| **-2.583 €**| ... | **-19.300 €**      | **35.770 €** | **122.920 €**|

---

## Die wichtigsten Kennzahlen und ihre Bedeutung

### Deckungsbeitrag (DB)
- **Formel:** Umsatz - Variable Kosten
- **Was er sagt:** Wie viel Geld von deinem Umsatz übrig bleibt, um deine Fixkosten zu decken.
- **Warum er wichtig ist:** Ein positiver Deckungsbeitrag ist die Grundvoraussetzung, um jemals profitabel zu werden. Jeder einzelne Verkauf muss mehr einbringen, als er direkt kostet.

### Betriebsergebnis (EBIT - Earnings Before Interest and Taxes)
- **Formel:** Deckungsbeitrag - Fixe Kosten
- **Was er sagt:** Ob dein operatives Kerngeschäft profitabel ist, unabhängig von Zinsen und Steuern.
- **Warum er wichtig ist:** Das ist die ehrlichste Kennzahl für den Erfolg deines Geschäftsmodells. Ein positives EBIT zeigt, dass deine Firma im Kern gesund ist.

### Ergebnis vor Steuern (EBT - Earnings Before Taxes)
- **Formel:** EBIT - Zinsen
- **Was er sagt:** Der Gewinn vor Abzug der Steuern.

### Jahresüberschuss (Nettogewinn)
- **Formel:** EBT - Steuern
- **Was er sagt:** Das, was am Ende des Jahres "unter dem Strich" wirklich übrig bleibt. Dieser Betrag kann (nach Rücklagenbildung) an dich ausgeschüttet werden oder im Unternehmen bleiben, um weiter zu wachsen (Thesaurierung).

---

## Der Break-Even-Point: Ab wann verdienst du Geld?

Der Break-Even-Point (BEP) ist der Punkt, an dem deine **Umsätze exakt so hoch sind wie deine Kosten**. Ab diesem Punkt machst du Gewinn. Man kann ihn auf zwei Arten betrachten:

**1. Zeitlicher Break-Even:**
- **Frage:** In welchem Monat übersteigen die Umsätze zum ersten Mal die Kosten?
- **Wo du es findest:** Scrolle in deiner Monatstabelle zu der Zeile "Betriebsergebnis (EBIT)" oder "Jahresüberschuss". Der Monat, in dem diese Zahl zum ersten Mal positiv wird, ist dein Break-Even-Monat.
- **Beispiel:** Wenn das EBIT im Monat 22 zum ersten Mal positiv ist, hast du nach 22 Monaten den Break-Even erreicht.

**2. Mengenmäßiger Break-Even:**
- **Frage:** Wie viele Kunden brauche ich pro Monat, um meine Kosten zu decken?
- **Formel:** Fixkosten / Deckungsbeitrag pro Kunde
- **Beispielrechnung:**
  - Fixkosten pro Monat: 4.233 €
  - Durchschnittlicher Umsatz pro Kunde im Monat: (149€/12) = 12,42 €
  - Variable Kosten pro Kunde im Monat: 1,50 €
  - **Deckungsbeitrag pro Kunde / Monat:** 12,42 € - 1,50 € = 10,92 €
  - **Break-Even (Kunden):** 4.233 € / 10,92 € = **ca. 388 Kunden**
- **Was das bedeutet:** Du musst einen aktiven Kundenstamm von 388 zahlenden Abonnenten haben, um jeden Monat bei Null rauszukommen.

**Dein Arbeitsbereich:**
> **Analyse meiner Rentabilitätsvorschau:**
>
> * **Mein Break-Even-Point wird voraussichtlich erreicht:**
>   * **Zeitlich:** im Monat [z.B. 22]
>   * **Mengenmäßig:** bei ca. [z.B. 388] Kunden.
> * **Entwicklung des Gewinns:**
>   * Im 1. Jahr mache ich einen geplanten Verlust von [z.B. -19.300 €].
>   * Im 2. Jahr erziele ich einen Gewinn von [z.B. 35.770 €].
>   * Im 3. Jahr steigert sich der Gewinn auf [z.B. 122.920 €].
> * **Schlussfolgerung:** Das Geschäftsmodell ist laut Plan ab dem zweiten Jahr profitabel und zeigt eine gesunde Gewinnentwicklung. Der anfängliche Verlust ist durch die Anlaufkosten und Marketing-Investitionen begründet.
>
> ---

Im letzten Schritt der Finanzplanung, der **Liquiditätsplanung**, überprüfen wir, ob du trotz der anfänglichen Verluste immer genug Geld auf dem Konto hast, um deine Rechnungen zu bezahlen.

---

## Verwandte Notizen

- [[01_Investitions-und_Kapitalbedarfsplan]]
- [[02_Umsatz-und_Kostenplanung]]
- [[04_Liquiditaetsplanung]]

---

## Zurück zur Übersicht

- [[_Übersicht_07-Finanzplanung|  Übersicht 07-Finanzplanung Uebersicht]]
