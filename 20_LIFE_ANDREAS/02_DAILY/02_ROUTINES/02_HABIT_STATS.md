# 📊 Habit Tracker & Analyse

Überblick über die Routine-Konsistenz basierend auf den täglichen Briefings.

## 📅 Wochen-Rückblick (Letzte 10 Tage)

```dataview
TABLE WITHOUT ID
  link(file.link, dateformat(file.day, "ccc, dd.MM.")) as "Datum",
  choice(length(filter(file.tasks, (t) => contains(t.text, "08:00 Aufstehen") AND t.completed)) > 0, "✅", "❌") as "🌅 8:00",
  choice(length(filter(file.tasks, (t) => contains(t.text, "Spanisch") AND t.completed)) > 0, "✅", "❌") as "🇪🇸 Spanisch",
  choice(length(filter(file.tasks, (t) => contains(t.text, "Sport") AND t.completed)) > 0, "✅", "❌") as "💪 Sport",
  choice(length(filter(file.tasks, (t) => contains(t.text, "Bibel") AND t.completed)) > 0, "✅", "❌") as "🙏 Bibel",
  choice(length(filter(file.tasks, (t) => contains(t.text, "Protein") AND t.completed)) > 0, "✅", "❌") as "🥩 Protein"
FROM "02_JOURNAL/08_BRIEFING"
WHERE file.day >= date(today) - dur(10 days)
SORT file.day DESC
```

## 📈 Konsistenz-Score (Diesen Monat)

```dataviewjs
// Berechnet die Disziplin basierend auf ALLEN Checkboxen in den Briefings diesen Monats
const pages = dv.pages('"02_JOURNAL/08_BRIEFING"').where(p => p.file.day >= dv.date('beginning of month'));
let totalHabits = 0;
let checkedHabits = 0;

for (let page of pages) {
    const tasks = page.file.tasks;
    totalHabits += tasks.length;
    checkedHabits += tasks.where(t => t.completed).length;
}

const percentage = totalHabits > 0 ? Math.round((checkedHabits / totalHabits) * 100) : 0;

dv.paragraph(`### Monatliche Disziplin: **${percentage}%**`);
dv.paragraph(`*${checkedHabits} von ${totalHabits} Habits erledigt.*`);

// Progress Bar Visualisierung
const barLength = 20;
const filledLength = Math.round((barLength * percentage) / 100);
const bar = '█'.repeat(filledLength) + '░'.repeat(barLength - filledLength);
dv.paragraph(`${bar}`);

if (percentage >= 80) dv.paragraph("🔥 **Exzellent! Weiter so!**");
else if (percentage >= 50) dv.paragraph("⚠️ **Guter Weg, aber da geht noch mehr!**");
else dv.paragraph("🛑 **Fokus schärfen! Komm zurück in die Routine.**");
```

## 🔍 Offene Habits (Heute)
*Was steht heute noch an?*

```dataview
TASK
FROM "02_JOURNAL/08_BRIEFING"
WHERE file.day = date(today) AND !completed
```
