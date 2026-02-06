[[..\_Übersicht_Personen|← Zurück zur Personen-Übersicht]]

# Übersicht Familie

---


---

---

## Dynamische Übersicht (DataviewJS)

```dataviewjs
dv.table(["Name", "Geburtstag", "Beziehung mit"],
  dv.pages('"15_Personen/Familie"')
    .where(p => p.file.name != "Familienstammbaum" && p.role == "Familienmitglied")
    .sort(p => p.file.name, "asc")
    .map(p => [p.file.link, p.birthday, p.relationship_with])
)
```
