# 2. Umsatz- und Kostenplanung: Was kommt rein, was geht raus?

---

Nachdem du weißt, was der Start kostet, planst du nun die erwarteten Einnahmen und die laufenden Ausgaben im Detail. Hier wird dein Geschäftsmodell in konkrete Zahlen gegossen. Plane für die ersten 3-5 Geschäftsjahre, wobei du das erste Jahr auf Monatsbasis und die Folgejahre auf Jahresbasis planst.

**Tipp:** Erstelle diese Planung in einer Tabellenkalkulation (Excel, Google Sheets). Das macht die Berechnungen und Anpassungen viel einfacher.

---

## Teil A: Die Umsatzplanung (Was kommt rein?)

Die Umsatzplanung ist oft der schwierigste Teil, da sie auf Annahmen über die Zukunft beruht. Sei hier realistisch und konservativ. Es ist besser, positiv überrascht zu werden, als einem unrealistischen Plan hinterherzulaufen.

**Bottom-Up-Planung (am besten für Start-ups):**
Du rechnest nicht vom großen Marktanteil herunter, sondern von der Anzahl der Kunden, die du realistischerweise gewinnen kannst.

**Bausteine deiner Umsatzplanung (Beispiel "Haushalts-Held"):**

1.  **Anzahl der Neukunden pro Monat:**
    - Basiert auf deinen Marketingzielen (Ordner 06).
    - *Annahme Jahr 1: Du startest mit 10 Kunden in Monat 1, 15 in Monat 2, 20 in Monat 3 usw. (Wachstum annehmen!).*
2.  **Kunden-Abwanderung (Churn Rate):**
    - Wie viel Prozent deiner Abo-Kunden kündigen pro Monat/Jahr?
    - *Annahme: 2% Churn pro Monat. Das bedeutet, du verlierst jeden Monat 2% deiner Bestandskunden.*
3.  **Preis pro Produkt/Paket:**
    - Aus deiner Preisstrategie (Ordner 05).
    - *Annahme: 80% der Kunden wählen das Jahresabo (149€), 20% das Monatsabo (14,99€).*

**Beispielrechnung für einen Monat in Excel:**

|                                | Monat 1 | Monat 2 | Monat 3 | ... |
| ------------------------------ | --------: | --------: | --------: | --- |
| **Kundenstamm (Anfang d. Mon.)**| 0         | 10        | 24        | ... |
| **+ Neukunden**                | 10        | 15        | 20        | ... |
| **- Kündigungen (Churn 2%)**   | 0         | 0         | -1        | ... |
| **= Kundenstamm (Ende d. Mon.)**| **10**    | **24**    | **43**    | ... |
|                                |           |           |           |     |
| **Umsatz Jahresabo (80%)**     | 8 * 149€  | 12 * 149€ | 16 * 149€ | ... |
| **Umsatz Monatsabo (20%)**     | 2 * 14,99€| 3 * 14,99€| 4 * 14,99€| ... |
| **+ Umsatz aus Vormonaten (Monatsabos)** | 0€ | 2 * 14,99€ | 5 * 14,99€ | ...|
| **= Gesamtumsatz pro Monat**   | **1.222€**| **1.848€**| **2.533€**| ... |

**Dein Arbeitsbereich (in Excel/Sheets):**
> Erstelle eine Tabelle für die ersten 36 Monate.
> - Zeile für Neukunden (plane das Wachstum realistisch!)
> - Zeile für Kündigungen (Churn)
> - Zeile für den Kundenstamm am Monatsende
> - Zeilen für die Umsätze aus deinen verschiedenen Paketen
> - Zeile für den monatlichen Gesamtumsatz
>
> **WICHTIG:** Dokumentiere deine Annahmen! Warum gehst du von X Neukunden aus? Warum Y% Churn? Das zeigt, dass du dir Gedanken gemacht hast.
>
> ---

## Teil B: Die Kostenplanung (Was geht raus?)

Hier listest du alle Kosten auf, die im laufenden Betrieb anfallen. Man unterscheidet zwischen variablen und fixen Kosten.

### 1. Variable Kosten (wachsen mit dem Umsatz)
*Diese Kosten steigen, je mehr Kunden du hast oder je mehr du verkaufst.*

- **Beispiele für "Haushalts-Held":**
  - **API-Kosten:** Jeder neue Kunde, der Verträge analysieren lässt, verursacht Kosten bei der Gemini-API.
  - **Server-/Cloud-Kosten:** Mehr Kunden bedeuten mehr Daten, mehr Rechenleistung -> höhere Kosten.
  - **Zahlungsgebühren:** z.B. 2,9% + 0,30€ pro Transaktion bei Stripe/PayPal.

**Planung in Excel:**
> *Variable Kosten pro Kunde (z.B. 1,50€) * Anzahl der Kunden = Variable Kosten gesamt pro Monat*

### 2. Fixe Kosten (bleiben (fast) immer gleich)
*Diese Kosten fallen jeden Monat an, egal ob du 0 oder 1.000 Kunden hast.*

- **Personalkosten:**
  - Dein Unternehmerlohn (siehe Kapitalbedarfsplan).
  - Gehälter für zukünftige Mitarbeiter (plane realistisch, wann du jemanden einstellen kannst/musst, z.B. einen Marketing-Mitarbeiter im 2. Jahr).
  - Sozialabgaben (Arbeitgeberanteil).
- **Marketingkosten:**
  - Dein monatliches Budget für Google Ads, Social Media etc. (aus Ordner 06).
- **Raumkosten:**
  - Miete für ein Büro (am Anfang vielleicht noch nicht nötig, Home-Office).
- **Betriebskosten:**
  - Software-Lizenzen (Buchhaltung, CRM, Office...).
  - Internet, Telefon.
  - Geschäftskonto-Gebühren.
- **Beratungskosten:**
  - Laufende Kosten für den Steuerberater.
- **Abschreibungen:**
  - Deine Gründungsinvestitionen (z.B. der Laptop) verlieren über die Zeit an Wert. Dieser Wertverlust wird als "Abschreibung" über mehrere Jahre als fiktive Kosten verbucht. (z.B. Laptop für 1.200€ wird über 3 Jahre abgeschrieben -> 400€ Kosten pro Jahr / 33,33€ pro Monat). Dein Steuerberater hilft dir hier.

**Dein Arbeitsbereich (in der gleichen Excel/Sheets-Tabelle):**
> Lege für jede Kostenart eine eigene Zeile an.
> - Zeilen für die variablen Kosten (verknüpft mit der Kundenzahl).
> - Zeilen für die Personalkosten (denke an zukünftige Mitarbeiter!).
> - Zeilen für Marketing, Miete, Software etc.
> - Zeile für Abschreibungen.
> - Addiere alles zu einer **Gesamtkosten-Zeile pro Monat**.
>
> ---

### Nächster Schritt:
Wenn du die Umsatz- und die Kostenplanung für jeden Monat fertig hast, kannst du den nächsten, entscheidenden Schritt tun: die **Rentabilitätsvorschau**. Du ziehst einfach die Gesamtkosten vom Gesamtumsatz ab und siehst, ob du Gewinn oder Verlust machst. Das machen wir im nächsten Dokument.

---

## Verwandte Notizen

- [[01_Investitions-und_Kapitalbedarfsplan]]
- [[03_Rentabilitaetsvorschau]]
- [[04_Liquiditaetsplanung]]

---

## Zurück zur Übersicht

- [[_Übersicht_07-Finanzplanung|  Übersicht 07-Finanzplanung Uebersicht]]
