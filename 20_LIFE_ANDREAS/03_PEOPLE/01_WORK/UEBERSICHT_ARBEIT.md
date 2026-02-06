[[..\_Übersicht_Personen|← Zurück zur Personen-Übersicht]]

# Übersicht Arbeit

---


---

---

## Dynamische Übersicht (DataviewJS)

```dataviewjs
dv.table(["Name", "Geburtstag", "Beziehung mit"],
  dv.pages('"15_Personen/Arbeit"')
    .where(p => p.role == "Kollege")
    .sort(p => p.file.name, "asc")
    .map(p => [p.file.link, p.birthday, p.relationship_with])
)
```
