# -*- coding: utf-8 -*-
import os
import json
import requests
import locale
from icalendar import Calendar, Event
from datetime import datetime, date, time, timedelta
import pytz
from dateutil.rrule import rrulestr
from pathlib import Path
import sys

# --- CONFIGURATION ---

# Set locale
try:
    locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'German_Germany.1252')
    except locale.Error:
        print("Warnung: Deutsche Locale nicht verfügbar. Nutze System-Standard.")

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "Kalender-Dashboard"
DASHBOARD_FILE = OUTPUT_DIR / "_Kalender_Dashboard.md"
RAW_DATA_FILE = OUTPUT_DIR / "Kalender.md"
ROUTINES_FILE = BASE_DIR / "routines.json"
MANUAL_ICS_FILE = DATA_DIR / "manual.ics"

# Timezone
TIMEZONE = "Europe/Berlin"
LOCAL_TZ = pytz.timezone(TIMEZONE)

# Number of days to generate
RAW_DATA_DAYS = 365  # Expand routines for 365 days in the main list

# Google Calendar ICS URLs
ICAL_URLS = {
    "Persönlich": "https://calendar.google.com/calendar/ical/braxmeierandreas%40gmail.com/private-076035858b13cb12c3bfc5bae9b573f9/basic.ics",
    "Kalender 2": "https://calendar.google.com/calendar/ical/b8c614cae6a22dc62c1e60d444beff5ce38c5c7f9bf2d88168582af9cd386966%40group.calendar.google.com/private-84bbd681f705d5b16265316f67bbec0f/basic.ics"
}

# --- HELPER FUNCTIONS ---

def ensure_dir(path):
    path.mkdir(parents=True, exist_ok=True)

def load_routines():
    if not ROUTINES_FILE.exists():
        return []
    with open(ROUTINES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data.get("routines", [])

def download_ics(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"Fehler beim Laden von {url}: {e}")
        return None

def parse_ics_content(content, source_name):
    events = []
    if not content:
        return events
    try:
        cal = Calendar.from_ical(content)
    except Exception as e:
        print(f"Fehler beim Parsen des Kalenders '{source_name}': {e}")
        return events

    for component in cal.walk():
        if component.name == "VEVENT":
            try:
                summary = str(component.get('summary'))
                start_dt = component.get('dtstart').dt
                end_dt = component.get('dtend').dt

                if isinstance(start_dt, date) and not isinstance(start_dt, datetime):
                    start_dt = datetime.combine(start_dt, time.min)
                if isinstance(end_dt, date) and not isinstance(end_dt, datetime):
                    end_dt = datetime.combine(end_dt, time.min)

                if not start_dt.tzinfo:
                    start_dt = LOCAL_TZ.localize(start_dt)
                else:
                    start_dt = start_dt.astimezone(LOCAL_TZ)
                
                if not end_dt.tzinfo:
                    end_dt = LOCAL_TZ.localize(end_dt)
                else:
                    end_dt = end_dt.astimezone(LOCAL_TZ)

                events.append({
                    "summary": summary,
                    "start": start_dt,
                    "end": end_dt,
                    "rrule": component.get('rrule'),
                    "source": source_name
                })
            except Exception:
                continue
    return events

def get_routine_events(routines, start_date, days):
    events = []
    end_date = start_date + timedelta(days=days)
    day_map = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    
    for routine in routines:
        r_days = routine.get("days", [])
        target_weekdays = {day_map[d] for d in r_days if d in day_map}
        try:
            r_start_time = datetime.strptime(routine["start_time"], "%H:%M").time()
            r_end_time = datetime.strptime(routine["end_time"], "%H:%M").time()
        except ValueError:
            continue

        current = start_date
        while current < end_date:
            if current.weekday() in target_weekdays:
                start_dt = LOCAL_TZ.localize(datetime.combine(current, r_start_time))
                end_dt = LOCAL_TZ.localize(datetime.combine(current, r_end_time))
                events.append({"summary": routine["summary"], "start": start_dt, "end": end_dt, "rrule": None, "source": "Routine"})
            current += timedelta(days=1)
    return events

def generate_markdown(all_events):
    ensure_dir(OUTPUT_DIR)
    
    # 1. Dashboard
    with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
        f.write("# Kalender Dashboard\n\n---\n\n")
        f.write("## Übersicht\n\n")
        f.write(f"- [[{RAW_DATA_FILE.name.replace('.md', '')}|Vollständiger Kalender (nächste 90 Tage)]]\n")
        f.write("- [[00_Overview|Projekt-Übersicht]]\n")

    # 2. Raw Data (The main "Kalender" file)
    with open(RAW_DATA_FILE, 'w', encoding='utf-8') as f:
        f.write("# Kalender\n\n")
        all_events.sort(key=lambda x: x['start'])
        
        last_date = None
        for e in all_events:
            curr_date = e['start'].date()
            if curr_date != last_date:
                f.write(f"\n### {curr_date.strftime('%A, %d.%m.%Y')}\n")
                last_date = curr_date
            
            start_s = e['start'].strftime('%H:%M')
            f.write(f"- **{start_s}**: {e['summary']} ({e['source']})\n")

def main():
    print("Aktualisiere Kalender...")
    all_events = []
    routines = load_routines()
    today = datetime.now(LOCAL_TZ).date()
    all_events.extend(get_routine_events(routines, today, RAW_DATA_DAYS))

    for name, url in ICAL_URLS.items():
        print(f"- Lade Google Kalender: {name}...")
        content = download_ics(url)
        all_events.extend(parse_ics_content(content, name))

    if MANUAL_ICS_FILE.exists():
        with open(MANUAL_ICS_FILE, 'rb') as f:
            all_events.extend(parse_ics_content(f.read(), "Manuell"))

    now = datetime.now(LOCAL_TZ)
    all_events = [e for e in all_events if e['end'] >= now]
    generate_markdown(all_events)
    print("Fertig!")

if __name__ == "__main__":
    main()