[[00_Zentrale/_Übersicht_Zentrale.md|Zurück zur Zentrale]]

# Übersicht Schlaf und Traumtagebuch

---


---

## Enthaltene Notizen

- [[_templates/Vorlage_Tagebuch_Eintrag.md | Vorlage für Tageseinträge]]

## Struktur und Nutzung der Tageseinträge

Tageseinträge werden im Format `JJJJ-MM-TT Schlaf- & Traumtagebuch.md` gespeichert und enthalten YAML-Frontmatter für eine bessere Organisation und Abfragbarkeit (z.B. mit Dataview). Sie werden in Jahres- und Monatsordnern organisiert (z.B. `2025/Dezember 2025/2025-12-20 Schlaf- & Traumtagebuch.md`).

### Nutzung der Vorlage

Um die Erstellung von Tageseinträgen zu vereinfachen, können Sie die `Vorlage_Tagebuch_Eintrag.md` im Ordner `_templates` mit dem Obsidian Templates Core Plugin oder dem Periodic Notes Plugin verwenden.

**Einrichtung im Obsidian Templates Plugin:**
1.  Gehen Sie zu "Einstellungen" -> "Core Plugins" -> "Templates".
2.  Stellen Sie den "Template folder location" auf `_templates` ein.
3.  Wenn Sie eine neue Notiz erstellen, können Sie das Template über die Befehlspalette (`Strg/Cmd + P` und "Insert template") auswählen.

**Einrichtung im Periodic Notes Plugin (für Daily Notes):**
1. Gehen Sie zu "Einstellungen" -> "Community Plugins" -> "Periodic Notes".
2. Aktivieren Sie "Daily Notes".
3. Stellen Sie das "Template file" auf `_templates/Vorlage_Tagebuch_Eintrag.md` ein.
4. Stellen Sie das "Date format" auf `YYYY-MM-DD` ein (dies wird intern verwendet, der Dateiname wird dann entsprechend der Vorlage generiert).
5. Stellen Sie den "Folder" für Daily Notes auf den Pfad des Jahresordners ein (z.B. `2025`). Sie müssen die Monatsordner manuell erstellen oder eine Templater-Funktion verwenden, um sie dynamisch zu erstellen.

### Verknüpfungen

*   **Tageseinträge zu Übersicht:** Jeder Tageseintrag verlinkt zurück zu dieser Übersichtsseite.
*   **Monatsübersichten:** In jedem Monatsordner (z.B. `2025/Dezember 2025/`) befindet sich eine Monatsübersicht (`JJJJ-MM Monat Übersicht.md`), die alle Tageseinträge des Monats auflistet.
*   **Jahresübersichten:** Im Jahresordner (z.B. `2025/`) befindet sich eine Jahresübersicht (`JJJJ Jahresübersicht.md`), die alle Monatsübersichten des Jahres verlinkt.

Dies ermöglicht eine einfache Navigation und Analyse der Daten.

## Dynamische Übersichten mit Dataview

Um das volle Potenzial der strukturierten Daten (Frontmatter) zu nutzen, kann das Dataview-Plugin (falls installiert) verwendet werden. Hier sind einige Beispiele:

### Alle Schlaf- & Traumtagebucheinträge

```dataview
TABLE date as "Datum", 
  Schlafdauer_Stunden AS "Dauer (h)",
  Schlafqualitaet_1-10 AS "Qualität (1-10)",
  Ins_Bett_gegangen_um AS "Ins Bett",
  Aufgestanden_um AS "Aufgestanden",
  Gefuehl_beim_Aufwachen AS "Gefühl",
  Unterbrechungen AS "Unterbrechungen",
  file.link as "Eintrag"
FROM #Schlaftagebuch OR #Traumtagebuch
SORT date DESC
```

*Hinweis: Damit diese Abfragen funktionieren, muss das Dataview-Plugin in Obsidian installiert und aktiviert sein.*

