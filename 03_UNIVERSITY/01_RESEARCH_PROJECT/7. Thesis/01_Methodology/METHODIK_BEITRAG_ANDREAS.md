# Methodischer Eigenanteil: Technische Koordination und Datenmanagement

## 1. Technische Infrastruktur und Kollaborationsumgebung

Zur Gewährleistung einer reibungslosen Zusammenarbeit innerhalb des Forschungsteams sowie einer effizienten Kommunikation mit externen Partnern wurde eine dedizierte technische Infrastruktur etabliert. 

In der initialen Projektphase erfolgte die Datenhaltung zunächst über Microsoft OneDrive. Aufgrund von Synchronisationsproblemen und zur Optimierung der kollaborativen Zugriffsrechte wurde die gesamte Projektumgebung im weiteren Verlauf auf **Google Drive** migriert. Diese Umstellung ermöglichte eine hochverfügbare, zentrale Ablage für alle Transkripte, Analysedokumente und die Akteursdatenbank. Parallel dazu wurde ein zentraler Google-Mail-Account für die Außenkommunikation eingerichtet, auf den das gesamte Team Zugriff hatte, um eine konsistente Ansprache der Akteure sicherzustellen.

Die Durchführung der qualitativen Interviews erfolgte hybrid: zum einen **vor Ort** in den jeweiligen Einrichtungen der Akteure, zum anderen digital via **Videokonferenz (Zoom)**. Um die Datenverfügbarkeit für die anschließende Transkription unmittelbar sicherzustellen, wurden die digitalen Aufzeichnungen in der Cloud gesichert. Die technischen Einstellungen wurden dabei so konfiguriert, dass eine bestmögliche Audioqualität für die nachfolgende **ASR-Verarbeitung** (Automatic Speech Recognition – automatische Spracherkennung) gewährleistet war. Zur Gewährleistung des Datenschutzes wurde zudem eine strikte "Download-and-Delete"-Policy verfolgt: Die Aufzeichnungen wurden unmittelbar nach dem Interview auf lokale Datenträger migriert und zeitnah aus der Cloud-Umgebung entfernt.

## 2. Akteursrecherche und zweistufiges Sampling-Verfahren

Die Identifikation der **Akteure** erfolgte in einem systematischen, zweistufigen Prozess, der darauf abzielte, eine **maximale Variationsbreite** innerhalb des Samples abzubilden.

*   **Phase 1 (Initial-Sampling):** Zunächst wurde eine Primärliste von ca. 50 relevanten Akteuren im Landkreis Schwarzwald-Baar erstellt.
*   **Phase 2 (Erweiterungs-Sampling):** Aufgrund der Notwendigkeit einer tieferen Feldausschöpfung wurde das Sample in einer zweiten Recherchephase auf **insgesamt über 150 Akteure** erweitert.

Die Akteure wurden dabei in einer **Stratifizierungsmatrix** verortet, um die strukturelle Vielfalt der Versorgungslandschaft abzubilden. Die Operationalisierung der Matrix basierte auf zwei zentralen Dimensionen, die wie folgt definiert wurden:

1.  **Zielgruppenreichweite:** Dieser Aspekt beschreibt die Anzahl der Kinder und Jugendlichen, die durch die Angebote eines Akteurs potenziell erreicht werden.
    *   *Groß:* Erreicht schätzungsweise $\ge$ 50 Kinder und Jugendliche.
    *   *Klein:* Erreicht schätzungsweise < 50 Kinder und Jugendliche.
2.  **Kontakthäufigkeit:** Dieser Aspekt erfasst die Regelmäßigkeit der Interaktion.
    *   *Regelmäßig:* Der Kontakt findet planmäßig und frequentiert statt (z. B. wöchentlich).
    *   *Gelegentlich:* Der Kontakt erfolgt unregelmäßig, saisonal (z. B. Fasnet) oder projektbezogen.

Durch die Kombination dieser Dimensionen ergaben sich vier Quadranten: (1) Große Reichweite/Regelmäßiger Kontakt, (2) Große Reichweite/Gelegentlicher Kontakt, (3) Kleine Reichweite/Regelmäßiger Kontakt und (4) Kleine Reichweite/Gelegentlicher Kontakt. Die vorläufige Zuordnung der Akteure erfolgte zunächst teamintern und wurde zu Beginn jedes Interviews validiert und bei Bedarf angepasst.

Ziel dieses Verfahrens war es, die vier Quadranten für das finale Sample möglichst gleichmäßig zu besetzen. Die systematische Recherche dieser Daten über kommunale Webseiten, Vereinsregister und öffentliche Datenbanken sowie die Validierung der Kontaktdaten sicherte eine optimierte Rücklaufquote. Rückblickend konnte durch dieses Vorgehen eine annähernd gleichmäßige Verteilung über die vier Quadranten der Stratifizierungsmatrix realisiert werden (jeweils ca. [XX] %), womit das Ziel einer maximalen Variationsbreite im Sample erreicht wurde.

## 3. Monitoring und operatives Controlling

Zur Steuerung des Feldzugangs wurde ein dynamisches **Excel-Monitoringsystem** implementiert. Dieses Instrument diente als "Single Source of Truth" für den aktuellen Rekrutierungsstand. Ergänzend zur Akteurssteuerung wurde ein **Gantt-Chart** geführt, um kritische Meilensteine (z. B. Abschluss der Feldphase) kontinuierlich mit dem tatsächlichen Projektfortschritt abzugleichen.

Der Feldzugang wurde prozessual in zwei Wellen gestaltet:
1. **Erste Kontaktwelle (Standardisiert):** Die initial identifizierten 50 Akteure wurden zunächst über ein standardisiertes E-Mail-Anschreiben kontaktiert.
2. **Zweite Kontaktwelle (Personalisiert):** Um die Rücklaufquote bei den Akteuren der Erweiterungsphase zu erhöhen, erfolgte hier die Ansprache bereits im Erstkontakt personalisiert. Hierfür wurden zielgruppenspezifische Kommunikationsvorlagen (z. B. für Schulen, Vereine, Kitas) genutzt, in welche die individuellen Daten eingepflegt wurden.
3. **Telefonisches Nachfassen:** Zur finalen Klärung des Feldzugangs wurde bei strategisch wichtigen Akteuren oder ausbleibender Rückmeldung zusätzlich telefonisch nachgefasst.

Das Monitoring-System visualisierte den Status jedes Akteurs (z. B. *Kontaktiert, Zusage, Absage, Terminiert*) in einem Dashboard. Dies ermöglichte es dem Team, den Feldzugang quantitativ zu überwachen und Redundanzen zu vermeiden. Final resultierte dieser Prozess in einer Rücklaufquote von [XX] %, was einer Anzahl von [XX] Interviews entspricht.

## 4. KI-gestützte Datenaufbereitung und Anonymisierung

Ein Kernaspekt des technischen Workflows war die hocheffiziente Aufbereitung der erhobenen Audiodaten. Die Transkription erfolgte in einem mehrstufigen Prozess:
1.  **Lokale KI-Transkription:** Aus Datenschutzgründen wurden die Audiofiles mit der Software **Vibe** lokal verarbeitet (Modell **`ggml-large-v3-turbo`**).
2.  **Post-Processing & Anonymisierung:** Im Anschluss wurde das Large Language Model **Google Gemini 3.5** eingesetzt, um das Roh-Transkript zu veredeln. Dies umfasste die Zusammenführung von Sprecherrollen, die Glättung des Sprachflusses bei Beibehaltung der inhaltlichen Integrität sowie die **systematische Anonymisierung** der Interviewpartner (z. B. Kodierung als B1).
3. **Qualitätssicherung (Human-in-the-loop):** Um Informationsverluste oder Verzerrungen durch die KI auszuschließen, wurden die geglätteten Transkripte anschließend im Team erneut vollständig gesichtet und mit **der Audioaufnahme** abgeglichen. Unklarheiten wurden manuell validiert.

Dieser hybride Workflow sicherte sowohl eine signifikante Zeitersparnis als auch eine hohe Transkriptionsgüte. Nach Abschluss des Prüfungsverfahrens werden sämtliche Rohdaten gemäß den datenschutzrechtlichen Vorgaben vernichtet; an den Projektpartner werden ausschließlich anonymisierte Ergebnisse übermittelt.