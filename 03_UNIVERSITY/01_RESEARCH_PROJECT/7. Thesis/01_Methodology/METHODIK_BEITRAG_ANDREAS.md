# Methodischer Eigenanteil: Technische Koordination und Datenmanagement

## 1. Technische Infrastruktur und Kollaborationsumgebung

Zur Gewährleistung einer reibungslosen Zusammenarbeit innerhalb des Forschungsteams sowie einer effizienten Kommunikation mit externen Partnern wurde eine dedizierte technische Infrastruktur etabliert. 

In der initialen Projektphase erfolgte die Datenhaltung zunächst über Microsoft OneDrive. Aufgrund von Synchronisationsproblemen und zur Optimierung der kollaborativen Zugriffsrechte wurde die gesamte Projektumgebung im weiteren Verlauf auf **Google Drive** migriert. Diese Umstellung ermöglichte eine hochverfügbare, zentrale Ablage für alle Transkripte, Analysedokumente und die Akteursdatenbank. Parallel dazu wurde ein zentraler Google-Mail-Account für die Außenkommunikation eingerichtet, auf den das gesamte Team Zugriff hatte, um eine konsistente Ansprache der Akteure sicherzustellen.

Die Durchführung der qualitativen Interviews erfolgte digital via **Zoom**. Um die Datenverfügbarkeit für die anschließende Transkription unmittelbar sicherzustellen, wurden die Aufzeichnungen in der Cloud gesichert. Die technischen Einstellungen wurden dabei so konfiguriert, dass eine bestmögliche Audioqualität für die nachfolgende ASR-Verarbeitung gewährleistet war. Zur Gewährleistung des Datenschutzes wurde zudem eine strikte "Download-and-Delete"-Policy verfolgt: Die Aufzeichnungen wurden unmittelbar nach dem Interview auf lokale Datenträger migriert und zeitnah aus der Cloud-Umgebung entfernt.

## 2. Akteursrecherche und zweistufiges Sampling-Verfahren

Die Identifikation der Untersuchungseinheiten erfolgte in einem systematischen, zweistufigen Prozess, der darauf abzielte, eine **maximale Variationsbreite** innerhalb des Samples abzubilden.

*   **Phase 1 (Initial-Sampling):** Zunächst wurde eine Primärliste von ca. 50 relevanten Akteuren im Landkreis Schwarzwald-Baar erstellt.
*   **Phase 2 (Erweiterungs-Sampling):** Aufgrund der Notwendigkeit einer tieferen Feldausschöpfung wurde das Sample in einer zweiten Recherchephase auf **insgesamt über 150 Akteure** erweitert.

Die Akteure wurden dabei in einer **Stratifizierungsmatrix** verortet, die auf zwei zentralen Kriterien basierte: **Reichweite** (Groß vs. Klein) und **Angebotsfrequenz** (Regelmäßig vs. Gelegentlich). 
Die Operationalisierung erfolgte dabei anhand pragmatischer Schwellenwerte: Als "groß" wurden Angebote klassifiziert, die regelmäßig $\ge$ 50 Kinder/Jugendliche erreichen; als "regelmäßig" galten wöchentliche Frequenzen im Gegensatz zu saisonalen oder projektbezogenen Formaten. Diese vorläufige Kategorisierung wurde zu Beginn jedes Interviews validiert und bei Bedarf angepasst.

Ziel dieses Verfahrens war es, die vier daraus resultierenden Quadranten für das finale Sample möglichst gleichmäßig zu besetzen, um eine strukturelle Vergleichbarkeit der Daten zu gewährleisten. Meine Aufgabe umfasste die systematische Recherche dieser Daten über kommunale Webseiten, Vereinsregister und öffentliche Datenbanken sowie die Validierung der Kontaktdaten (E-Mail, Telefonnummern, Ansprechpartner), um die Rücklaufquote zu optimieren. Rückblickend konnte durch dieses Vorgehen eine Verteilung von ca. [XX] % großen und [XX] % kleinen Akteuren realisiert werden, womit das Ziel einer breiten Varianz [erreicht/annähernd erreicht] wurde.

## 3. Monitoring und operatives Controlling

Zur Steuerung des Feldzugangs wurde ein dynamisches **Excel-Monitoringsystem** implementiert. Dieses Instrument diente als "Single Source of Truth" für den aktuellen Rekrutierungsstand. 

Der Feldzugang wurde prozessual in mehreren Stufen gestaltet:
1. **Erste Kontaktwelle:** Initial wurden alle identifizierten Akteure über ein standardisiertes E-Mail-Anschreiben kontaktiert.
2. **Zweite Kontaktwelle:** Bei ausbleibender Rückmeldung erfolgte eine zweite, nun personalisierte Ansprache. Hierfür wurden zielgruppenspezifische Kommunikationsvorlagen (z. B. für Schulen, Vereine, Kitas) entwickelt, in welche die individuellen Akteursdaten eingepflegt wurden, um die spezifische Relevanz der Studie für den jeweiligen Kontext hervorzuheben.
3. **Telefonisches Nachfassen:** Zur finalen Klärung des Feldzugangs wurde bei strategisch wichtigen Akteuren zusätzlich telefonisch nachgefasst.

Das Monitoring-System visualisierte den Status jedes Akteurs (z. B. *Kontaktiert, Zusage, Absage, Terminiert*) in einem Dashboard. Dies ermöglichte es dem Team, den Feldzugang quantitativ zu überwachen, Redundanzen bei der Kontaktaufnahme zu vermeiden und die Interviewtermine effizient zu koordinieren. Final resultierte dieser Prozess in einer Rücklaufquote von [XX] %, was einer Anzahl von [XX] durchgeführten Interviews entspricht.

## 4. KI-gestützte Datenaufbereitung und Anonymisierung

Ein Kernaspekt des technischen Workflows war die hocheffiziente Aufbereitung der erhobenen Audiodaten für die qualitative Inhaltsanalyse. 

Die Transkription erfolgte in einem mehrstufigen, technologisch gestützten Prozess:
1.  **Lokale KI-Transkription:** Aus Datenschutzgründen wurden die Audiofiles mit der Software **Vibe** lokal (offline) verarbeitet. Dabei kam das Modell **`ggml-large-v3-turbo`** zum Einsatz, welches eine präzise Erst-Verschriftlichung lieferte.
2.  **Post-Processing & Anonymisierung:** Im Anschluss wurde das Large Language Model **Google Gemini 1.5 Pro** eingesetzt, um das Roh-Transkript zu veredeln. Dies umfasste die Zusammenführung von Sprecherrollen, die Glättung des Sprachflusses bei Beibehaltung der inhaltlichen Integrität sowie die **systematische Anonymisierung** der Interviewpartner (z. B. Kodierung als B1, B2, B3).
3. **Qualitätssicherung (Human-in-the-loop):** Um Informationsverluste oder "Halluzinationen" der KI auszuschließen, wurden die geglätteten Transkripte anschließend erneut vollständig gesichtet und mit dem Audio abgeglichen. Unklarheiten wurden durch mich manuell validiert. Eine abschließende Detailkontrolle erfolgte durch ein weiteres Teammitglied (Sophie Scheffler).

Dieser hybride Workflow aus lokaler KI-Technologie und manueller Revision sicherte sowohl eine signifikante Zeitersparnis als auch eine hohe Transkriptionsgüte. Nach Abschluss des Prüfungsverfahrens werden sämtliche Rohdaten (Audiofiles) und personenbezogene Zuordnungslisten gemäß den datenschutzrechtlichen Vorgaben vernichtet; an den Projektpartner (Gesundheitsamt) werden ausschließlich die anonymisierten Ergebnisse übermittelt.

Da das Forschungsdesign ausschließlich **Experteninterviews** mit erwachsenen Fachkräften vorsah und keine direkten Interaktionen mit vulnerablen Gruppen (Kindern oder Jugendlichen) beinhaltete, war **kein gesonderter Ethikantrag** erforderlich. Die Perspektive auf die Zielgruppe wurde somit indirekt über die professionelle Außensicht der Akteure erhoben. Im Zuge der Datenaufbereitung erfolgte eine **Teilanonymisierung**: Während personenbezogene Daten (Namen der Interviewpartner) konsequent pseudonymisiert wurden, blieben die Bezeichnungen der Institutionen und Vereine erhalten, um die für die Netzwerkanalyse relevanten strukturellen Kontexte nicht zu verlieren.