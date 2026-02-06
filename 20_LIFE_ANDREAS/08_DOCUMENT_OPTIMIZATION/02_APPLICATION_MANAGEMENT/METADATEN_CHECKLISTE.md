# Metadaten & Dokumenten-Hygiene

Metadaten sind der "digitale Reisepass" eines Dokuments. Falsche oder fehlende Metadaten können dazu führen, dass ein Dokument falsch kategorisiert oder als unprofessionell wahrgenommen wird.

---

## 📋 Checkliste: Vor dem Export

Prüfen Sie diese Felder in Word (`Datei > Informationen > Eigenschaften`) oder im PDF-Editor:

| Feld | Best Practice | Beispiel |
| :--- | :--- | :--- |
| **Titel** | Aussagekräftig, enthält Name & Dokumenttyp. Keine Dateinamen-Syntax (_v2_final). | `Lebenslauf - Max Mustermann - 2026` |
| **Autor** | Ihr voller bürgerlicher Name. | `Max Mustermann` |
| **Betreff** | Kurzfassung des Inhalts (wichtig für die Vorschau in E-Mail-Clients). | `Bewerbung als Senior Developer bei Firma XY` |
| **Stichwörter** | Semikolon-getrennte Liste der Top-Kompetenzen. | `Projektmanagement; Python; C#; Scrum; Teamleitung` |

---

## 🤖 Prompts zur Metadaten-Erstellung

### 1. Titel & Betreff generieren
Lassen Sie die KI den perfekten "Titel-Tag" schreiben.

**Prompt:**
> "Ich sende dieses Dokument als Bewerbung an [Firmenname]. Generiere mir basierend auf dem Inhalt (unten) einen professionellen **Titel** für die PDF-Metadaten und einen prägnanten Satz für das Feld **Betreff**, der meine Eignung sofort unterstreicht."
>
> *[Inhalt des Anschreibens/CV]*

### 2. Zusammenfassung für das Abstract-Feld
Einige Systeme zeigen das Feld "Kommentar" oder "Beschreibung" als Vorschau an.

**Prompt:**
> "Schreibe eine 'Executive Summary' meines Lebenslaufs in maximal 2 Sätzen (unter 200 Zeichen). Fokus auf meine stärksten Alleinstellungsmerkmale. Dies wird in die Datei-Metadaten als Beschreibung eingefügt."

---

## 🛠 Technische Reinigung

*   **Verfasser bereinigen:** Stellen Sie sicher, dass nicht "HP-User", "Admin" oder der Name einer anderen Person (falls Vorlage genutzt) im Autor-Feld steht.
*   **Erstelldatum:** Ein aktuelles Datum signalisiert Frische. Alte Erstellungsdaten (z.B. 2019) können den Eindruck erwecken, der CV sei veraltet.
