import datetime
import os
import json
import re
import random
import urllib.request
import urllib.parse
import sys

# Ensure imports work from subfolders
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from GOOGLE.google_auth import get_service

# Pfade (Relativ zum Skript in 00_SCRIPTS)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR) # Ein Level höher (Obsidian Root)

BRIEFING_DIR = os.path.join(ROOT_DIR, "02_JOURNAL", "08_BRIEFING")
FINANCE_PATH = os.path.join(ROOT_DIR, "14_TRADING", "02_DATA", "banking_snapshot.json")
PORTFOLIO_PATH = os.path.join(ROOT_DIR, "14_TRADING", "02_DATA", "portfolio_snapshot.json")
GEMINI_MD_PATH = os.path.join(ROOT_DIR, "GEMINI.md")
SPANISH_DIR = os.path.join(ROOT_DIR, "09_LEARNING_SPANISH", "02_VOCABULARY")

def get_calendar_events():
    try:
        service = get_service('calendar', 'v3')
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        end_of_day = (datetime.datetime.utcnow().replace(hour=23, minute=59, second=59)).isoformat() + 'Z'
        
        calendars = [
            {'id': 'primary', 'name': 'Persönlich'},
            {'id': 'b8c614cae6a22dc62c1e60d444beff5ce38c5c7f9bf2d88168582af9cd386966@group.calendar.google.com', 'name': 'Studium/Arbeit'},
            {'id': 'hanne.bornschein@gmx.de', 'name': 'Hannah'}
        ]
        
        all_events = []
        for cal in calendars:
            try:
                events_result = service.events().list(
                    calendarId=cal['id'], 
                    timeMin=now, 
                    timeMax=end_of_day, 
                    singleEvents=True, 
                    orderBy='startTime'
                ).execute()
                events = events_result.get('items', [])
                for e in events:
                    e['_cal_name'] = cal['name']
                    all_events.append(e)
            except:
                continue # Skip calendars if no access or error
        
        if not all_events: return "Keine Termine für heute."
        
        # Sort combined events by start time
        def get_start(e):
            s = e['start'].get('dateTime', e['start'].get('date'))
            return s
            
        all_events.sort(key=get_start)
        
        lines = []
        for e in all_events:
            start = e['start'].get('dateTime', e['start'].get('date'))
            time_str = start[11:16] if 'T' in start else "Ganztägig"
            lines.append(f"- **{time_str}**: {e['summary']} *({e['_cal_name']})*")
        return "\n".join(lines)
    except Exception as e:
        return f"Fehler Kalender: {e}"

def get_tasks():
    try:
        service = get_service('tasks', 'v1')
        tasklists = service.tasklists().list().execute().get('items', [])
        lines = []
        for tl in tasklists:
            tasks = service.tasks().list(tasklist=tl['id'], showCompleted=False).execute().get('items', [])
            if tasks:
                for t in tasks[:5]:
                    lines.append(f"- [ ] {t['title']} ({tl['title']})")
        return "\n".join(lines) if lines else "Keine offenen Aufgaben."
    except Exception as e:
        return f"Fehler Tasks: {e}"

def get_unread_emails():
    try:
        service = get_service('gmail', 'v1')
        results = service.users().messages().list(userId='me', q='is:unread', maxResults=5).execute()
        messages = results.get('messages', [])
        if not messages: return "Keine ungelesenen E-Mails."
        lines = []
        for msg in messages:
            m = service.users().messages().get(userId='me', id=msg['id'], format='metadata').execute()
            headers = m['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(Kein Betreff)')
            sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unbekannt')
            lines.append(f"- {subject} (von: {sender[:30]}...)")
        return "\n".join(lines)
    except Exception as e:
        return f"Fehler E-Mail: {e}"

def get_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=48.05&longitude=8.21&current_weather=true&hourly=temperature_2m,precipitation_probability&daily=sunrise,sunset&timezone=Europe%2FBerlin"
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode())
        
        curr = data['current_weather']
        hourly_temp = data['hourly']['temperature_2m']
        hourly_rain = data['hourly']['precipitation_probability']
        daily = data['daily']
        
        # Sunrise/Sunset (nur Zeit extrahieren "YYYY-MM-DDTHH:MM" -> "HH:MM")
        sunrise = daily['sunrise'][0][-5:]
        sunset = daily['sunset'][0][-5:]

        # Indizes für 08:00, 13:00, 18:00
        h8, h13, h18 = 8, 13, 18
        
        def fmt_hour(idx):
            return f"{hourly_temp[idx]}°C ({hourly_rain[idx]}% ☔)"

        summary = f"🌡️ **Aktuell: {curr['temperature']}°C**\n"
        summary += f"🌅 {sunrise} Uhr  |  🌇 {sunset} Uhr\n"
        summary += f"- 🕗 Morgens: {fmt_hour(h8)}\n"
        summary += f"- ☀️ Mittags: {fmt_hour(h13)}\n"
        summary += f"- 🌙 Abends: {fmt_hour(h18)}"
        
        return summary
    except Exception as e:
        return f"Wetterdaten nicht verfügbar ({e})."

def get_travel_info():
    # Logik für Furtwangen (Bregstraße -> Bibliothek)
    # Da alles nah ist, ist die Basiszeit 5 Min.
    # Bei Temperaturen unter 0°C (Schneegefahr) addieren wir Puffer.
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=48.05&longitude=8.21&current_weather=true"
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode())
        temp = data['current_weather']['temperature']
        
        base_time = 6 
        delay = 0
        warning = ""
        
        if temp < 0:
            delay = 5
            warning = " ❄️ **Glättegefahr im Schwarzwald!**"
        
        return f"🚗 **Wegzeit zur Bibliothek:** {base_time + delay} Min.{warning}"
    except:
        return "🚗 **Wegzeit:** ca. 6 Min. (Standard)"

def get_deadlines():
    try:
        if os.path.exists(GEMINI_MD_PATH):
            with open(GEMINI_MD_PATH, 'r', encoding='utf-8') as f:
                content = f.read()
            match = re.search(r"Aktuelle Deadlines.*?(?=\n\n|###)", content, re.DOTALL)
            if match:
                deadlines = match.group(0).strip()
                lines = [l.strip() for l in deadlines.split('\n') if l.strip().startswith('- **')]
                return "\n".join(lines)
        return "Keine Deadlines gefunden."
    except:
        return "Fehler Deadlines."

def get_fit_comprehensive():
    try:
        service = get_service('fitness', 'v1')
        now_dt = datetime.datetime.now()
        
        # 1. Schritte & Aktivität & Hydration (Aggregate)
        start_of_month = now_dt.replace(day=1, hour=0, minute=0, second=0)
        body = {
            "aggregateBy": [
                {"dataTypeName": "com.google.step_count.delta"},
                {"dataTypeName": "com.google.calories.expended"},
                # {"dataTypeName": "com.google.hydration"} # 403 Forbidden
            ],
            "bucketByTime": {"durationMillis": 86400000},
            "startTimeMillis": int(start_of_month.timestamp() * 1000),
            "endTimeMillis": int(now_dt.timestamp() * 1000)
        }
        res = service.users().dataset().aggregate(userId="me", body=body).execute()
        
        total_steps_month = 0
        today_steps = 0
        today_cals = 0
        today_hydro = 0
        yesterday_steps = 0
        today_str = now_dt.strftime('%Y-%m-%d')
        yesterday_str = (now_dt - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        
        for bucket in res.get('bucket', []):
            start_ts = int(bucket['startTimeMillis']) / 1000
            d_str = datetime.datetime.fromtimestamp(start_ts).strftime('%Y-%m-%d')
            
            s = 0
            c = 0
            h = 0
            for ds in bucket.get('dataset', []):
                for p in ds.get('point', []):
                    for v in p.get('value', []):
                        val = v.get('intVal') if v.get('intVal') is not None else v.get('fpVal', 0)
                        if "step_count" in ds['dataSourceId']: s += val
                        if "calories" in ds['dataSourceId']: c += int(val)
                        if "hydration" in ds['dataSourceId']: h += val
            
            total_steps_month += s
            if d_str == today_str: 
                today_steps = s
                today_cals = c
                today_hydro = h
            if d_str == yesterday_str: yesterday_steps = s

        # 2. Gewicht & Body Fat (Raw Data - Letzter Eintrag der letzten 30 Tage)
        weight_val = 0.0
        bf_val = 0.0
        try:
            # Helper for fetching last point
            def get_last_val(ds_id, days=30):
                start = int((now_dt - datetime.timedelta(days=days)).timestamp() * 1000000000)
                end = int(now_dt.timestamp() * 1000000000)
                r = service.users().dataSources().datasets().get(userId="me", dataSourceId=ds_id, datasetId=f"{start}-{end}").execute()
                pts = r.get('point', [])
                if pts: return pts[-1]['value'][0]['fpVal']
                return 0.0

            weight_val = get_last_val("derived:com.google.weight:com.google.android.gms:merge_weight")
            bf_val = get_last_val("derived:com.google.body.fat.percentage:com.google.android.gms:merge_body_fat_percentage")
        except:
            pass

        # 3. Schlaf (Sessions der letzten Nacht)
        sleep_hours = 0.0
        try:
            yesterday_noon = (now_dt - datetime.timedelta(days=1)).replace(hour=12, minute=0)
            today_noon = now_dt.replace(hour=12, minute=0)
            
            s_res = service.users().sessions().list(
                userId="me", 
                startTime=yesterday_noon.isoformat() + "Z", 
                endTime=today_noon.isoformat() + "Z",
                activityType=[72] 
            ).execute()
            
            for sess in s_res.get('session', []):
                start = int(sess['startTimeMillis'])
                end = int(sess['endTimeMillis'])
                duration_ms = end - start
                sleep_hours += (duration_ms / 1000 / 3600)
        except:
            sleep_hours = 0.0

        # --- COACHING LOGIK (3000 KCAL + 20% BF LIMIT) ---
        days_passed = now_dt.day
        avg_month = total_steps_month / days_passed
        remaining_today_avg = max(0, (days_passed * 10000) - (total_steps_month - today_steps) - today_steps)
        
        msgs = []
        
        # 1. Kalorien (Das Wichtigste)
        target_cals = 3000
        current_hour = now_dt.hour
        # Simple projection: By 12:00 should have ~1000, by 18:00 ~2000
        if today_cals < (target_cals * 0.2) and current_hour > 10:
             msgs.append(f"🍗 **Essen!** Erst {today_cals} kcal. Frühstück vergessen? Ziel: 3.000 kcal (ca. 750 kcal pro Mahlzeit)!")
        elif today_cals >= target_cals:
             msgs.append(f"✅ **Kalorienziel erreicht!** ({today_cals} kcal). Jetzt wachsen.")
        else:
             needed = target_cals - today_cals
             msgs.append(f"🍽️ **Noch {needed} kcal essen.** Ziel: 4 Mahlzeiten à 750 kcal.")

        # 2. Body Fat Check
        if bf_val > 20:
            msgs.append(f"🛑 **WARNUNG:** KFA bei {bf_val:.1f}% (>20%). Kalorienüberschuss reduzieren! Mehr Cardio.")
        elif bf_val > 0:
            msgs.append(f"⚖️ KFA: {bf_val:.1f}% (OK).")

        # 3. Schlaf
        if sleep_hours > 0:
            if sleep_hours < 6.5:
                msgs.append("😴 **Schlaf-Mangel!** Heute Abend Prio 1: Früher ins Bett.")
            elif sleep_hours > 8:
                msgs.append("🔋 **Top Erholung!**")
        else:
            msgs.append("⚠️ Kein Schlaf getrackt.")

        # 4. Aktivität
        if avg_month < 9500:
            msgs.append(f"🚶‍♂️ **Beweg dich!** Schnitt nur {int(avg_month):,}.")

        coach_final = " ".join(msgs)
        if not coach_final: coach_final = "Bleib diszipliniert. Tracke deine Daten."

        # Output Formatierung
        report = f"**💪 IRON ANDREAS COACHING:**\n"
        report += f"> \"{coach_final}\"\n\n"
        report += f"**📊 Live-Status:**\n"
        report += f"- **Kalorien:** {int(today_cals):,} / 3.000 kcal\n"
        report += f"- **Körper:** {weight_val:.1f} kg | {bf_val:.1f}% KFA (Max: 20%)\n"
        report += f"- **Schlaf:** {sleep_hours:.1f} Std.\n"
        report += f"- **Schritte:** {today_steps:,} (Monats-Ø: {int(avg_month):,})"
        
        return report

    except Exception as e:
        return f"Fehler Fit: {e}"

def get_bible_verse():
    try:
        verses = [
            ("Denn ich weiß wohl, was ich für Gedanken über euch habe, spricht der HERR: Gedanken des Friedens und nicht des Leides, dass ich euch gebe das Ende, des ihr wartet.", "Jeremia 29:11"),
            ("Der HERR ist mein Hirte, mir wird nichts mangeln.", "Psalm 23:1"),
            ("Alle eure Sorge werft auf ihn; denn er sorgt für euch.", "1. Petrus 5:7"),
            ("Gott ist unsre Zuversicht und Stärke, eine Hilfe in den großen Nöten, die uns getroffen haben.", "Psalm 46:2"),
            ("Seid fröhlich in Hoffnung, geduldig in Trübsal, beharrlich im Gebet.", "Römer 12:12")
        ]
        text, ref = random.choice(verses)
        return f"> \"{text}\"\n> \n> — *{ref}*"
    except:
        return "> \"Denn ich weiß wohl, was ich für Gedanken über euch habe, spricht der HERR...\"\n> \n> — *Jeremia 29:11*"

def get_spanish_vocab():
    try:
        files = [f for f in os.listdir(SPANISH_DIR) if f.endswith('.md')]
        chosen_file = random.choice(files)
        with open(os.path.join(SPANISH_DIR, chosen_file), 'r', encoding='utf-8') as f:
            content = f.read()
        
        tables = re.findall(r'\|.*\|', content)
        if not tables: return "Keine Vokabeln gefunden."
        
        rows = [r for r in tables if '|' in r and '---' not in r and ':---' not in r and 'Spanisch' not in r]
        if not rows: return "Vokabeln-Format nicht erkannt."
        
        # Wähle 3 zufällige, einzigartige Zeilen (oder weniger wenn Liste klein)
        count = min(3, len(rows))
        selected_rows = random.sample(rows, count)
        
        vocab_list = []
        for row in selected_rows:
            parts = [p.strip() for p in row.split('|') if p.strip()]
            if len(parts) >= 2:
                vocab_list.append(f"🇪🇸 **{parts[0]}** = 🇩🇪 {parts[1]}")
        
        return "\n".join(vocab_list)
    except:
        return "Keine Vokabel heute (Fehler beim Laden)."

def get_finance_stats():
    try:
        stats = []
        if os.path.exists(FINANCE_PATH):
            with open(FINANCE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
            nw = data['net_worth_history'][-1]['Total_Net_Worth']
            cash = data['sparkasse_balance'] + data['revolut_balance']
            stats.append(f"- Net Worth: **{nw:,.2f} €**")
            stats.append(f"- Liquide Mittel: {cash:,.2f} €")
        
        if os.path.exists(PORTFOLIO_PATH):
            with open(PORTFOLIO_PATH, 'r', encoding='utf-8') as f:
                port = json.load(f)
            invested = port['cash']['invested']
            result = port['cash']['result']
            status_emoji = "📈" if result >= 0 else "📉"
            stats.append(f"- Portfolio-Status {status_emoji}: **{invested + result:,.2f} €**")
            stats.append(f"- Gesamtgewinn/-verlust: {'+' if result >= 0 else ''}{result:,.2f} € ({'✅' if result >= 0 else '⚠️'})")
            if 'positions' in port and port['positions']:
                top_pos = max(port['positions'], key=lambda x: x.get('ppl', 0))
                stats.append(f"- Top Performer: {top_pos['ticker'].split('_')[0]} (+{top_pos['ppl']:.2f} €)")
        return "\n".join(stats) if stats else "Keine Finanzdaten gefunden."
    except Exception as e:
        return f"Fehler Finanzen: {e}"

import xml.etree.ElementTree as ET

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext.strip()

def fetch_rss(url, limit=3):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        
        # RSS 2.0 uses 'channel/item', Atom uses 'entry' (simplified handling)
        items = root.findall('.//item')
        if not items:
            items = root.findall('.//{http://www.w3.org/2005/Atom}entry')
            
        news_entries = []
        for item in items[:limit]:
            # Title
            title_elem = item.find('title')
            title = title_elem.text if title_elem is not None else "Kein Titel"
            
            # Description
            desc = ""
            desc_elem = item.find('description')
            if desc_elem is not None and desc_elem.text:
                desc = clean_html(desc_elem.text)
            
            # Fallback for Google News which sometimes puts source in description
            if len(desc) < 5:
                # Try content:encoded or similar if needed, or just leave empty
                pass
                
            # Limit description length
            if len(desc) > 200: desc = desc[:197] + "..."
            
            # Formatting
            entry = f"- **{title.strip()}**\n  _{desc}_"
            news_entries.append(entry)
            
        return "\n".join(news_entries) if news_entries else "Keine News gefunden."
    except Exception as e:
        return f"Quelle momentan nicht erreichbar ({str(e)[:50]})."

def get_all_news():
    news_blocks = []
    
    # 1. Global / Tagesschau
    news_blocks.append("**🌍 Global (Tagesschau):**\n" + fetch_rss("https://www.tagesschau.de/infoservices/alle-meldungen-100~rss2.xml"))
    
    # 2. Tech (Golem)
    news_blocks.append("**💻 Tech (Golem):**\n" + fetch_rss("https://rss.golem.de/rss.php?feed=RSS2.0", 3))

    # 3. Business / Finance (WirtschaftsWoche) - Deutsch & Relevant
    news_blocks.append("**💼 Business (WiWo):**\n" + fetch_rss("https://www.wiwo.de/contentexport/feed/rss/schlagzeilen", 3))
    
    return "\n\n".join(news_blocks)

def get_habits_from_checklist():
    checklist_path = os.path.join(ROOT_DIR, "01_Andreas", "02_DAILY", "02_ROUTINES", "01_MASTER_CHECKLISTE.md")
    try:
        with open(checklist_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Wir extrahieren alles ab der ersten "##" Überschrift, um den Header/Intro wegzulassen
        lines = content.split('\n')
        relevant_content = []
        capture = False
        for line in lines:
            if line.startswith("## 🌅"): # Startpunkt erkennen
                capture = True
            if capture:
                relevant_content.append(line)
        
        return "\n".join(relevant_content) if relevant_content else "Keine Habits gefunden (Format prüfen)."
    except Exception as e:
        return f"Fehler beim Laden der Habits: {e}"

def save_briefing():
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")
    filename = f"BRIEFING_{date_str}.md"
    filepath = os.path.join(BRIEFING_DIR, filename)
    
    content = f"""
--- tags: [briefing, daily, automation]
date: {date_str}
created: {date_str} {time_str}
---

# ☕ Morning Briefing - {now.strftime('%d.%m.%Y')}

## 🧘‍♂️ Geistiger Anker
**Bibelvers des Tages:**
{get_bible_verse()}

**Spanisch Vokabeln:**
{get_spanish_vocab()}

---

## 🎯 Daily Habits & Routine
{get_habits_from_checklist()}

---

## 🌤️ Wetter & Logistik
**Furtwangen:** {get_weather()}
**Anfahrt:** {get_travel_info()}

{get_all_news()}

---

## 📅 Termine & Deadlines
**Heute im Kalender:**
{get_calendar_events()}

**Wichtige Deadlines (Uni):**
{get_deadlines()}

---

## ✅ To-Dos & E-Mails
**Offene Aufgaben:**
{get_tasks()}

**Ungelesene Mails:**
{get_unread_emails()}

---

## 🏃‍♂️ Fitness & Gesundheit (Coach Modus)
{get_fit_comprehensive()}

---

## 💰 Finanzen Snapshot
{get_finance_stats()}

---
*Zuletzt aktualisiert: {now.strftime('%H:%M')} Uhr. Viel Erfolg heute, Andreas!*
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Update: Vollständiges Briefing (Coach & Anchor & Habits) gespeichert.")

if __name__ == "__main__":
    save_briefing()