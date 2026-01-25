# 01 Detaillierte Anforderungen und Meilensteine (DiPA-Spezifikation)

Dieses Dokument definiert die messbaren Anforderungen und Verifikationskriterien für das DiPA-Projekt, basierend auf dem BfArM-Leitfaden (V1.0) und der DAA-Studie (Daum, 2022).

## 1. Wissenschaftliche Anforderungen: Nachweis des pflegerischen Nutzens (PN)

Ein "pflegerischer Nutzen" ist gemäß § 40a Abs. 2 SGB XI nur dann gegeben, wenn messbare Verbesserungen in einem der 8 Bereiche (§ 14 Abs. 2 SGB XI) vorliegen.

### 1.1 Messbare Outcome-Parameter (Beispiele)
| PN-Bereich | Messinstrument (Input) | Erwarteter Output (Messbarer Erfolg) |
| :--- | :--- | :--- |
| **Mobilität** | Barthel-Index (BI) / Timed Up and Go Test | Signifikante Verbesserung (p < 0,05) der Scores nach 3 Monaten. |
| **Kognition** | Mini-Mental-State-Examination (MMSE) | Stabilisierung oder Verlangsamung des Abbaus im Vergleich zur Kontrollgruppe. |
| **Selbstversorgung** | ADL-Skala (Activities of Daily Living) | Erhöhung des Scores um mind. 10% in der Interventionsgruppe. |
| **Häusliche Versorgung** | Burden Scale for Family Caregivers (BSFC) | Reduktion des empfundenen Belastungsscores um mind. 5 Punkte. |

### 1.2 Studiendesign-Anforderungen
- **Typ:** Vergleichende Studie (vorzugsweise RCT).
- **Population:** Repräsentative Stichprobe (N >= 50 pro Gruppe für statistische Power).
- **Dauer:** Mindestbeobachtungszeitraum von 3 Monaten für das Fast-Track-Verfahren.
- **Vergleich:** Interventionsgruppe (DiPA + eUL) vs. Kontrollgruppe (Standard-of-Care).

## 2. Technische & Regulatorische Anforderungen (Verifizierbar)

### 2.1 Interoperabilität & Datenfluss
- **Format:** Export in menschenlesbarem (PDF) und maschinenlesbarem Format (XML/JSON) gemäß § 7 DiPAV.
- **Schnittstellen:** Pflicht zur Unterstützung von Profilen des Interoperabilitätsverzeichnisses (vesta).
- **Authentifizierung:** 2-Faktor-Authentifizierung (2FA) gemäß BSI-Sicherheitsniveau "hoch".

### 2.2 Anforderungen an ergänzende Unterstützungsleistungen (eUL)
Jede eUL muss im Antrag (§ 39a SGB XI) wie folgt strukturiert sein:
- **ID:** Eindeutige Kennung.
- **Inhalt:** Präzise Beschreibung der Tätigkeit (z.B. "Monatliche Anpassung der Sturzsensor-Parameter").
- **Zeitaufwand:** Messbar in Minuten (z.B. "15 Min. pro Monat").
- **Qualifikation:** Anforderung an das Personal (z.B. "Pflegefachkraft mit IT-Zusatzqualifikation").

## 3. Implementierungs-Anforderungen (DAA-Studie-Korrektiv)

Um die Barrieren aus der DAA-Studie (83% fehlende Entlastung) zu adressieren, gelten folgende Projekt-Anforderungen:
- **Partizipations-Check:** Nachweis der Einbeziehung von mind. 5 Pflegekräften in die UI/UX-Gestaltung (Protokollpflicht).
- **Infrastruktur-Audit:** Vor Einsatz der DiPA muss ein WLAN-Signalstärke-Check (mind. -67 dBm in allen Versorgungsräumen) durchgeführt werden.
- **Schulungs-Outcome:** Verifikation der Kompetenz durch einen standardisierten Abschlusstest für Pflegekräfte nach der Einweisung.

## 4. Meilensteinplanung (36 Monate)

| Meilenstein | Erwarteter Output (Deliverable) | Verifikationsmethode |
| :--- | :--- | :--- |
| **M1: Literatur & Design** | Finales Studienprotokoll (SPIRIT-konform) | Review durch wissenschaftliche Leitung |
| **M2: Datenerhebung** | Rohdatensatz von 25 Experteninterviews | Vorliegen der Transkripte (anonymisiert) |
| **M3: Modellentwicklung** | DiPA-Implementierungs-Framework (Draft) | Peer-Review Workshop mit Stakeholdern |
| **M4: Finaler Bericht** | Veröffentlichungsfähiges Manuskript | Einreichungsbestätigung Fachjournal |
