import sys
import time
import random
import requests
import json
import os
import datetime

# --- KONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
STUDIES_DIR = os.path.join(ROOT_DIR, "01_Andreas", "05_KNOWLEDGE", "DAILY_STUDIES")

# Themengebiete basierend auf deinem Profil
TOPICS = [
    "Public Health",
    "Health Promotion",
    "Artificial Intelligence",
    "Large Language Models",
    "Clinical Psychology",
    "Exercise Physiology",
    "Behavioral Economics",
    "Sleep Science",
    "Nutrition Science"
]

# API Endpunkt
API_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_random_topic():
    return random.choice(TOPICS)

def fetch_paper(topic, retries=3):
    # Wir suchen nach relevanten Papern der letzten 3 Jahre
    current_year = datetime.datetime.now().year
    year_range = f"{current_year-2}-{current_year}"
    
    params = {
        "query": topic,
        "limit": 20,
        "fields": "title,authors,abstract,year,citationCount,url,venue,openAccessPdf",
        "year": year_range,
        "sort": "citationCount:desc"
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept": "application/json"
    }

    for attempt in range(retries):
        try:
            print(f"Suche nach Studie zum Thema: {topic} (Versuch {attempt+1}/{retries})...")
            response = requests.get(API_URL, params=params, headers=headers, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                if "data" in data and len(data["data"]) > 0:
                    paper = random.choice(data["data"])
                    return paper, topic
                else:
                    print(f"Keine Daten für '{topic}' gefunden.")
                    return None, None
            elif response.status_code == 429:
                wait_time = (attempt + 1) * 10
                print(f"API Rate Limit (429). Warte {wait_time} Sekunden...")
                time.sleep(wait_time)
            else:
                print(f"API Fehler: {response.status_code}")
                break # Bei anderen Fehlern nicht unbedingt sinnvoll zu retrien
                
        except Exception as e:
            print(f"Fehler bei der Verbindung: {e}")
            time.sleep(2)
    
    return None, None

def format_authors(author_list):
    if not author_list:
        return "Unknown Authors"
    # Ensure author_list is actually a list of dicts with 'name'
    try:
        names = [a.get('name', 'Unknown') for a in author_list]
        return ", ".join(names[:3]) + (" et al." if len(names) > 3 else "")
    except:
        return "Format Error"

def create_markdown(paper, topic):
    if not paper:
        return

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.datetime.now().strftime("%H%M%S")
    
    # Dateiname mit Timestamp um Konflikte zu vermeiden
    filename = f"STUDY_{today}_{timestamp}.md"
    filepath = os.path.join(STUDIES_DIR, filename)

    title = paper.get('title', 'No Title')
    abstract = paper.get('abstract')
    if not abstract:
        abstract = "Kein Abstract verfügbar. Bitte nutze den Link zur Originalquelle."
    
    authors = format_authors(paper.get('authors', []))
    year = paper.get('year', 'Unknown Year')
    citations = paper.get('citationCount', 0)
    url = paper.get('url', '')
    venue = paper.get('venue', 'Unknown Venue')
    
    pdf_link = ""
    if paper.get('openAccessPdf'):
        pdf_url = paper['openAccessPdf'].get('url')
        if pdf_url:
            pdf_link = f"\n> [!PDF] [Direktes PDF öffnen]({pdf_url})"

    content = f"""---
tags: [study, science, daily, {topic.replace(" ", "_").lower()}]
date: {today}
topic: "{topic}"
type: academic_paper
citations: {citations}
year: {year}
---

# 🎓 {title}

> **Thema:** {topic} | **Jahr:** {year} | **Zitationen:** {citations}
> **Journal/Venue:** {venue}
> **Autoren:** {authors}

---

## 📝 Abstract
{abstract}

---

## 🔗 Links
- [Zur Studie (Semantic Scholar)]({url})
{pdf_link}

"""
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ Studie erfolgreich gespeichert:\n📂 {filepath}\nTopic: {topic}\nTitel: {title}")
        return True
    except Exception as e:
        print(f"Fehler beim Speichern der Datei: {e}")
        return False

def main():
    ensure_dir(STUDIES_DIR)
    
    # Prüfen ob ein Thema übergeben wurde
    if len(sys.argv) > 1:
        # Alles nach dem Skriptnamen als ein Suchterm zusammenfügen
        user_topic = " ".join(sys.argv[1:])
        paper, topic_used = fetch_paper(user_topic)
        if paper:
            create_markdown(paper, topic_used)
            sys.exit(0)
        else:
            print(f"❌ Keine Studie zum Thema '{user_topic}' gefunden.")
            sys.exit(1)

    # Standard-Modus: Versuche bis zu 3 mal mit verschiedenen Themen aus der Liste
    topics_to_try = random.sample(TOPICS, 3)
    
    for topic in topics_to_try:
        paper, topic_used = fetch_paper(topic)
        if paper:
            success = create_markdown(paper, topic_used)
            if success:
                sys.exit(0) # Erfolgreich beenden
        
        # Kurze Pause vor dem nächsten Versuch
        time.sleep(2)

    print("❌ Konnte heute leider keine Studie abrufen (Alle Versuche fehlgeschlagen).")
    sys.exit(1) # Fehlercode senden

if __name__ == "__main__":
    main()