# Methodischer Eigenanteil: Technische Koordination und Datenmanagement

## 1. Technische Infrastruktur und Kollaborationsumgebung

Zur Gewährleistung einer reibungslosen Zusammenarbeit innerhalb des Forschungsteams sowie einer effizienten Kommunikation mit externen Partnern wurde eine dedizierte technische Infrastruktur etabliert. 

In der initialen Projektphase erfolgte die Datenhaltung zunächst über Microsoft OneDrive. Aufgrund von Synchronisationsproblemen und zur Optimierung der kollaborativen Zugriffsrechte wurde die gesamte Projektumgebung im weiteren Verlauf auf **Google Drive** migriert. Diese Umstellung ermöglichte eine hochverfügbare, zentrale Ablage für alle Transkripte, Analysedokumente und die Akteursdatenbank. Parallel dazu wurde ein zentraler Google-Mail-Account für die Außenkommunikation eingerichtet, auf den das gesamte Team Zugriff hatte, um eine konsistente Ansprache der Akteure sicherzustellen.

Die Durchführung der qualitativen Interviews erfolgte digital via **Zoom**. Um die Datenverfügbarkeit für die anschließende Transkription unmittelbar sicherzustellen, wurden die Aufzeichnungen in der Cloud gesichert. Die technischen Einstellungen wurden dabei so konfiguriert, dass eine bestmögliche Audioqualität für die nachfolgende ASR-Verarbeitung gewährleistet war.

## 2. Akteursrecherche und zweistufiges Sampling-Verfahren

Die Identifikation der Untersuchungseinheiten erfolgte in einem systematischen, zweistufigen Prozess, der darauf abzielte, eine **maximale Variationsbreite** innerhalb des Samples abzubilden.

*   **Phase 1 (Initial-Sampling):** Zunächst wurde eine Primärliste von ca. 50 relevanten Akteuren im Landkreis Schwarzwald-Baar erstellt.
*   **Phase 2 (Erweiterungs-Sampling):** Aufgrund der Notwendigkeit einer tieferen Feldausschöpfung wurde das Sample in einer zweiten Recherchephase auf **insgesamt über 150 Akteure** erweitert.

Die Akteure wurden dabei nach zwei zentralen Kriterien stratifiziert: **Reichweite** (Groß vs. Klein) und **Angebotsfrequenz** (Regelmäßig vs. Gelegentlich). Meine Aufgabe umfasste die systematische Recherche dieser Daten über kommunale Webseiten, Vereinsregister und öffentliche Datenbanken sowie die Validierung der Kontaktdaten (E-Mail, Telefonnummern, Ansprechpartner), um die Rücklaufquote zu optimieren.

## 3. Monitoring und operatives Controlling

Zur Steuerung des Feldzugangs wurde ein dynamisches **Excel-Monitoringsystem** implementiert. Dieses Instrument diente als "Single Source of Truth" für den aktuellen Rekrutierungsstand. 

Das System visualisierte den Status jedes Akteurs (z. B. *Kontaktiert, Zusage, Absage, Terminiert*) in einem Dashboard. Dies ermöglichte es dem Team, den Feldzugang quantitativ zu überwachen, Redundanzen bei der Kontaktaufnahme zu vermeiden und die Interviewtermine effizient zu koordinieren.

## 4. KI-gestützte Datenaufbereitung und Anonymisierung

Ein Kernaspekt des technischen Workflows war die hocheffiziente Aufbereitung der erhobenen Audiodaten für die qualitative Inhaltsanalyse. 

Die Transkription erfolgte in einem mehrstufigen, technologisch gestützten Prozess:
1.  **Lokale KI-Transkription:** Aus Datenschutzgründen wurden die Audiofiles mit der Software **Vibe** lokal (offline) verarbeitet. Dabei kam das Modell **`ggml-large-v3-turbo`** zum Einsatz, welches eine präzise Erst-Verschriftlichung lieferte.
2.  **Post-Processing & Anonymisierung:** Im Anschluss wurde eine spezialisierte KI eingesetzt, um das Roh-Transkript zu veredeln. Dies umfasste die Zusammenführung von Sprecherrollen, die Glättung des Sprachflusses bei Beibehaltung der inhaltlichen Integrität sowie die **systematische Anonymisierung** der Interviewpartner (z. B. Kodierung als B1, B2, B3).
3. **Qualitätssicherung:** Unklarheiten im Text wurden in Interaktion mit der KI identifiziert und anschließend durch mich manuell validiert. Eine abschließende Detailkontrolle und inhaltliche Validierung erfolgte durch ein weiteres Teammitglied (Sophie Scheffler).

Dieser hybride Workflow aus lokaler KI-Technologie und manueller Revision sicherte sowohl eine signifikante Zeitersparnis als auch eine hohe Transkriptionsgüte unter Einhaltung datenschutzrechtlicher Anforderungen.

Da das Forschungsdesign ausschließlich **Experteninterviews** mit erwachsenen Fachkräften vorsah und keine direkten Interaktionen mit vulnerablen Gruppen (Kindern oder Jugendlichen) beinhaltete, war **kein gesonderter Ethikantrag** erforderlich. Die Perspektive auf die Zielgruppe wurde somit indirekt über die professionelle Außensicht der Akteure erhoben. Im Zuge der Datenaufbereitung erfolgte eine **Teilanonymisierung**: Während personenbezogene Daten (Namen der Interviewpartner) konsequent pseudonymisiert wurden, blieben die Bezeichnungen der Institutionen und Vereine erhalten, um die für die Netzwerkanalyse relevanten strukturellen Kontexte nicht zu verlieren.