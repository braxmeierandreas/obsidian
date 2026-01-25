import datetime
import os
from auth_helper import get_service

# Pfade definieren (Relativ)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
JOURNAL_BASE = os.path.join(ROOT_DIR, "02_JOURNAL", "01_2026")

def get_weekly_fit(service):
    now = datetime.datetime.now()
    start_of_week = now - datetime.timedelta(days=6)
    start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
    
    body = {
        "aggregateBy": [{"dataTypeName": "com.google.step_count.delta", "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps"}],
        "bucketByTime": { "durationMillis": 86400000 },
        "startTimeMillis": int(start_of_week.timestamp() * 1000),
        "endTimeMillis": int(now.timestamp() * 1000)
    }
    
    response = service.users().dataset().aggregate(userId="me", body=body).execute()
    
    fit_report = "### 🏃‍♂️ Fitness (Schritte)\n"
    total_steps = 0
    
    for bucket in response.get('bucket', []):
        start_ts = int(bucket['startTimeMillis']) / 1000
        date_str = datetime.datetime.fromtimestamp(start_ts).strftime('%a, %d.%m.')
        
        steps = 0
        for dataset in bucket.get('dataset', []):
            for point in dataset.get('point', []):
                for value in point.get('value', []):
                    steps += value.get('intVal', 0)
        
        status = "✅" if steps >= 10000 else "⚠️"
        fit_report += f"- **{date_str}**: {steps:,} Schritte {status}\n"
        total_steps += steps
    
    avg = total_steps / 7
    fit_report += f"\n**Wochen-Gesamt:** {total_steps:,} Schritte\n"
    fit_report += f"**Wochen-Schnitt:** {int(avg):,} Schritte/Tag\n"
    return fit_report

def get_weekly_tasks(service):
    now = datetime.datetime.now()
    start_of_week = now - datetime.timedelta(days=7)
    # Format: 2026-01-11T00:00:00Z
    rfc_start = start_of_week.isoformat() + "Z"
    
    task_report = "### ✅ Erledigte Aufgaben (Woche)\n"
    found_any = False
    
    tasklists = service.tasklists().list().execute().get('items', [])
    for tl in tasklists:
        tasks = service.tasks().list(tasklist=tl['id'], showCompleted=True, completedMin=rfc_start).execute().get('items', [])
        completed_this_week = [t for t in tasks if t.get('status') == 'completed']
        
        if completed_this_week:
            found_any = True
            task_report += f"#### {tl['title']}\n"
            for t in completed_this_week:
                task_report += f"- [x] {t['title']}\n"
                
    if not found_any:
        task_report += "- Keine Aufgaben als erledigt markiert in dieser Woche.\n"
    return task_report

def get_weekly_drive(service):
    now = datetime.datetime.now()
    start_of_week = now - datetime.timedelta(days=7)
    rfc_start = start_of_week.isoformat() + "Z"
    
    drive_report = "### 📂 Drive Aktivitäten (Letzte 7 Tage)\n"
    
    # Query for modified files
    q = f"modifiedTime > '{rfc_start}' and trashed = false"
    results = service.files().list(q=q, orderBy="modifiedTime desc", pageSize=10, fields="files(name, mimeType, modifiedTime)").execute().get('files', [])
    
    if not results:
        drive_report += "- Keine nennenswerten Datei-Aktivitäten.\n"
    else:
        for f in results:
            drive_report += f"- {f['name']} ({f['mimeType'].split('/')[-1]})\n"
            
    return drive_report

def create_report():
    print("Sammle Daten für den Wochenrückblick...")
    
    fit_service = get_service('fitness', 'v1')
    tasks_service = get_service('tasks', 'v1')
    drive_service = get_service('drive', 'v3')
    
    now = datetime.datetime.now()
    week_num = now.isocalendar()[1]
    year = now.year
    month_name = now.strftime('%B').upper()
    month_num_name = now.strftime('%m_%B').upper() # E.g., 01_JANUARY
    
    # Pfad zum Monatsordner
    month_dir = os.path.join(JOURNAL_BASE, month_num_name)
    if not os.path.exists(month_dir):
        # Fallback to simple month name if the complex one doesn't exist
        month_dir = os.path.join(JOURNAL_BASE, f"{now.strftime('%m')}_{now.strftime('%B').upper()}")
        if not os.path.exists(month_dir):
            os.makedirs(month_dir, exist_ok=True)

    filename = f"WOCHENRUECKBLICK_{year}_KW{week_num:02d}.md"
    filepath = os.path.join(month_dir, filename)
    
    report = f"""---
tags: [review, weekly, automation]
date: {now.strftime('%Y-%m-%d')}
kw: {week_num}
---

# 📅 Wochenrückblick {year} - KW {week_num}
({(now - datetime.timedelta(days=6)).strftime('%d.%m.')} - {now.strftime('%d.%m.%Y')})

"""
    report += get_weekly_fit(fit_service) + "\n"
    report += get_weekly_tasks(tasks_service) + "\n"
    report += get_weekly_drive(drive_service) + "\n"
    
    report += """
### 🧠 Reflexion
- **Was lief gut?**
- **Was kann verbessert werden?**
- **Fokus für die nächste Woche:**
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(report)
        
    print(f"Wochenrückblick erfolgreich erstellt: {filepath}")

if __name__ == "__main__":
    create_report()
