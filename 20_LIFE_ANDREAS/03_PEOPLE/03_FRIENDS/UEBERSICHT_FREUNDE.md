[[..\_Übersicht_Personen|← Zurück zur Personen-Übersicht]]

# Übersicht Freunde

---


---

---

## Dynamische Übersicht (DataviewJS)

```dataviewjs
dv.table(["Name", "Geburtstag", "Beziehung mit"],
  dv.pages('"15_Personen/Freunde"')
    .where(p => p.role == "Freund")
    .sort(p => p.file.name, "asc")
    .map(p => [p.file.link, p.birthday, p.relationship_with])
)
```
