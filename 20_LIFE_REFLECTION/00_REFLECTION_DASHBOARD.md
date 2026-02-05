# 🚀 Reflection & Intelligence Center

> "Data beats opinion. Was sagen meine Muster über mich?"

## 📊 Live Status

### ⚠️ Offene Action Items aus Reflexionen
```dataview
TASK
FROM "27_REFLECTION_AND_GROWTH/01_DAILY_LOG"
WHERE !completed
```

### 🔥 Letzte 7 Tage: Trigger Analyse
```dataview
TABLE trigger_type as "Trigger", severity as "Schwere (1-10)", energy_level as "Energie"
FROM "27_REFLECTION_AND_GROWTH/01_DAILY_LOG"
WHERE file.ctime > date(today) - dur(7 days)
SORT file.ctime desc
```

---

## 🛠️ Tools & Protokolle

| Aktion | Link |
| :--- | :--- |
| **Neuer Eintrag** | [[99_TEMPLATES/Reflexions_Template|📝 Erstellen]] |
| **Bias Check** | [[02_TRIGGER_DATABASE/COGNITIVE_BIASES|🧠 Denkfehler Liste]] |
| **Wochen-Review** | [[99_TEMPLATES/Weekly_Growth_Review|📅 Review starten]] |

## 🎓 Lessons Learned (High Impact)
```dataview
LIST
FROM "27_REFLECTION_AND_GROWTH/01_DAILY_LOG"
WHERE severity >= 7
LIMIT 5
```

---
[[GEMINI|🔙 Mainframe]]