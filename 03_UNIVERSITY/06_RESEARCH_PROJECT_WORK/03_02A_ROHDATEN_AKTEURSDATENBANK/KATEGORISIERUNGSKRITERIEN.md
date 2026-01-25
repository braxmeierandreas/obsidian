# Kriterien zur Einordnung von Akteuren

Dieses Dokument legt die Kriterien fest, nach denen Akteure aus den `excel1.md` und `excel2.md` Dateien in die vier Kategorien "groß, regelmäßig", "groß, gelegentlich", "klein, regelmäßig" und "klein, gelegentlich" eingeordnet werden sollen.

## 1. Kriterium: Größe des Akteurs ("Groß" / "Klein")

**Definition des Schwellenwerts:**
Ein Akteur wird als **"groß"** eingestuft, wenn die Größe des Vereins (oder der Organisation) **größer als 50** ist.
Ein Akteur wird als **"klein"** eingestuft, wenn die Größe des Vereins (oder der Organisation) **kleiner oder gleich 50** ist.

**Herausforderung bei der Datenextraktion aus den Excel-Dateien:**
Die bereitgestellten Excel-Dateien enthalten keine direkten Angaben zur genauen Größe eines Vereins (z.B. Mitgliederzahlen). Um eine bestmögliche Einordnung nach dem Kriterium "Größe des Vereins" zu ermöglichen, müssen indirekte Indikatoren aus den vorhandenen Daten genutzt werden. Dies ist eine Inferenz und bedarf der Bestätigung durch den Benutzer.

**Vorschläge zur Ableitung der Größe (Inferenz basierend auf verfügbaren Daten):**
Da keine direkten Mitgliederzahlen vorliegen, wird die Größe eines Akteurs anhand einer Kombination folgender indirekter Indikatoren aus den Spalten "Name", "Angebotstyp", "Beschreibung des Angebots/Akteurs" sowie der Existenz von Kontaktdaten (`Homepage`, `Email-Adresse`, `Telefonnummer`) geschätzt:

*   **Indikatoren für "Groß" (> 50 Mitglieder):**
    *   **Umfangreiche Angebote / Infrastruktur:** Akteure, die in der Spalte "Beschreibung des Angebots/Akteurs" mehrere detaillierte Aktivitäten, Kurse, "Jugend-" oder "Kinder-" Gruppen (z.B. "Jugendmannschaften", "Kinderturnen", "Jugendfeuerwehr") oder mehrere Abteilungen auflisten.
    *   **Strukturierte Organisation:** Die Erwähnung von "Kreisverband", "Amt für...", "Stiftung", oder "Klinikum" impliziert eine größere, oft überregionale Struktur.
    *   **Bildungs- und Betreuungseinrichtungen:** "Schulen", "Kindergärten", "Kindertagesstätten", "Jugendhäuser", "Musikschulen" werden aufgrund ihrer institutionellen Natur und des breiten Angebots in der Regel als "groß" eingestuft.
    *   **Professionelle Präsenz:** Das Vorhandensein einer "Homepage", einer spezifischen "Email-Adresse" und "Telefonnummer", oft mit mehreren Ansprechpartnern, deutet auf eine etablierte Organisation hin.
    *   **Regionale Reichweite:** Akteure, deren "Name" oder "Beschreibung" auf eine Tätigkeit in mehreren "Teilorten" oder einer ganzen Region hindeuten (z.B. "Schwarzwald-Baar-Kreis").
    *   **Sportstätten mit breitem Angebot:** "Sportstätten" wie Hallen- & Freibäder, Stadien, größere Sportplätze mit vielfältigen Trainingsmöglichkeiten, die von einem Akteur betrieben werden.

*   **Indikatoren für "Klein" (<= 50 Mitglieder):**
    *   **Begrenzte Angebote / Singularität:** Akteure, die in der "Beschreibung des Angebots/Akteurs" nur eine sehr spezifische oder einzelne Aktivität ohne weitere Untergliederungen oder Jugend-/Kindergruppen nennen.
    *   **Einfache Organisationsform:** Kleine, lokale "e.V."s, deren "Name" oder "Beschreibung" auf einen überschaubaren Wirkungsbereich hindeuten.
    *   **Fehlende detaillierte Präsenz:** Akteure ohne explizite "Homepage" oder mit generischen Kontaktinformationen, die keine große organisatorische Tiefe vermuten lassen.
    *   **Nischen- oder Hobbygruppen:** Akteure, die sehr spezialisierte oder hobbymäßige Aktivitäten beschreiben, die typischerweise von kleineren Gruppen ausgeübt werden (z.B. "Kleingärtner", "Imkerverein" in kleineren Gemeinden, "Pit-Pat-Club").

**Wichtiger Hinweis:** Die Zuweisung "groß" oder "klein" auf dieser Inferenzbasis ist eine Schätzung und kann im Einzelfall ungenau sein. Eine manuelle Überprüfung oder zusätzliche Daten sind zur präzisen Einhaltung des Schwellenwerts von "50" erforderlich.

## 2. Kriterium: Regelmäßigkeit der Aktivität ("Regelmäßig" / "Gelegentlich")

Dieses Kriterium basiert auf dem "Angebotstyp" (aus `excel1.md`) sowie der Art und Bezeichnung des Akteurs, wie sie in der Spalte "Name" und "Beschreibung des Angebots/Akteurs" sowie dem Kontext der `Stadt/Gemeinde` und des `Teilorts` angegeben ist.

*   **Regelmäßig:**
    *   Akteure, die eine etablierte Struktur und fortlaufende Angebote implizieren.
    *   **Basierend auf "Angebotstyp":**
        *   "Sportangebot", "Bildung", "Religion", "BOS" (Behörden und Organisationen mit Sicherheitsaufgaben wie Feuerwehr, DRK, THW), "Betreuung", "Kultur" (wenn es sich um etablierte Vereine/Institutionen handelt), "Prävention", "Soziales", "Natur" (wenn es sich um Naturschutzvereine o.ä. handelt), "Kuration", "Tiere" (wenn es sich um Tierzucht- oder Hundevereine handelt), "Eltern-Kind-Angebote", "Pfadfinder", "Umweltschutz".
    *   **Keywords / Typen in "Name" oder "Beschreibung":** "e.V." (eingetragener Verein), "Verein", "Club", "Jugendarbeit", "Schule", "Kindergarten", "Kindertagesstätte", "Kirche", "Kirchengemeinde", "Pfarrei", "Zentrum", "Amt für...", "Beratungsstelle", "Akademie", "Musikschule", "Bibliothek", "Halle" (wenn als Trägerorganisation genannt), "Stiftung".
    *   Akteure, die durch ihre Natur tägliche, wöchentliche oder monatliche Aktivitäten erwarten lassen.

*   **Gelegentlich:**
    *   Akteure, die primär einmalige, saisonale oder unregelmäßige Veranstaltungen/Projekte organisieren oder nur eine reine Lokation (ohne expliziten Träger) sind.
    *   **Basierend auf "Angebotstyp":** "Fasnet" (da es sich um saisonale Veranstaltungen handelt).
    *   **Keywords / Typen in "Name" oder "Beschreibung":** Explizite Erwähnung von "Projekt" (wenn der Akteur selbst das Projekt und nicht die dahinterstehende regelmäßige Organisation ist), "Sommerlager", "Fest", "Veranstaltung".
    *   Reine Nennung von Orten/Anlagen wie "Sportplatz", "Bolzplatz", "Schwimmbad", "Minigolf", "Skisprungschanze" ohne zugehörige Organisation oder wenn diese Orte als Akteur selbst gelistet sind und keine regelmäßige betreibende Organisation im Namen erkennbar ist. (In `excel1.md` sind diese "Sportstätte" unter "Angebotstyp", was auf *regelmäßige* Verfügbarkeit hindeutet, aber der Akteur selbst könnte "gelegentlich" sein, wenn er nur als Ort dient und nicht selbst betrieben wird von einer Organisation).

## 3. Umgang mit "Irregulären" Einträgen

Es wurde festgestellt, dass insbesondere in der `excel2.md` Datei einige Einträge vom standardmäßigen Markdown-Tabellenformat abweichen. Auch in `excel1.md` können vereinzelt Formatierungsinkonsistenzen auftreten (z.B. Zeilenumbrüche innerhalb von Zellen). Diese Einträge erfordern eine manuelle Interpretation, um relevante Informationen für die Kategorisierung zu extrahieren.
*   **Vorgehen:** Der Inhalt dieser Zeilen muss auf Keywords, Organisationsformen und implizierte Aktivitäten hin analysiert werden, um die oben genannten Kriterien anzuwenden. Auch hier sind eingebettete Kontaktdaten (Telefonnummern, E-Mails, URLs) Indikatoren für eine regelmäßige Existenz. Die zusätzlichen Spalten in `excel1.md` (wie "Angebotstyp", "Beschreibung des Angebots/Akteurs") sind hierbei besonders hilfreich, auch wenn die Formatierung nicht perfekt ist.
