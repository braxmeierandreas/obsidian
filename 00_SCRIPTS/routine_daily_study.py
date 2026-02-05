import os
import datetime
import urllib.request
import xml.etree.ElementTree as ET
import re
import html

# Pfade
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
STUDIES_DIR = os.path.join(ROOT_DIR, "01_Andreas", "05_KNOWLEDGE", "DAILY_STUDIES")

# Sicherstellen, dass der Ordner existiert
if not os.path.exists(STUDIES_DIR):
    os.makedirs(STUDIES_DIR)

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return html.unescape(cleantext).strip()

def fetch_study():
    # Liste von RSS Quellen (Priorisiert)
    sources = [
        {"url": "https://www.nature.com/nature.rss", "name": "Nature"},
        {"url": "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml", "name": "BBC Science"},
        {"url": "https://rss.nytimes.com/services/xml/rss/nyt/Science.xml", "name": "NYT Science"}
    ]
    
    for source in sources:
        try:
            print(f"Versuche Quelle: {source['name']}...")
            req = urllib.request.Request(source['url'], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=10) as response:
                xml_data = response.read()
                
            root = ET.fromstring(xml_data)
            
            # Namespace Handling für RSS vs Atom
            # Nature nutzt RDF/RSS 1.0, BBC RSS 2.0
            # Wir suchen generisch nach 'item'
            items = root.findall('.//{http://purl.org/rss/1.0/}item') # Nature
            if not items:
                items = root.findall('.//item') # Standard RSS 2.0
            
            if not items:
                continue
                
            # Wir nehmen das erste Item
            item = items[0]
            
            # Titel extrahieren
            title_elem = item.find('{http://purl.org/rss/1.0/}title')
            if title_elem is None: title_elem = item.find('title')
            title = title_elem.text if title_elem is not None else "Ohne Titel"

            # Link extrahieren
            link_elem = item.find('{http://purl.org/rss/1.0/}link')
            if link_elem is None: link_elem = item.find('link')
            link = link_elem.text if link_elem is not None else ""

            # Beschreibung extrahieren
            desc_elem = item.find('{http://purl.org/rss/1.0/}description')
            if desc_elem is None: desc_elem = item.find('description')
            description = desc_elem.text if desc_elem is not None else "Keine Beschreibung verfügbar."
            
            # Datum (Optional)
            date_elem = item.find('pubDate')
            pub_date = date_elem.text if date_elem is not None else datetime.datetime.now().strftime("%Y-%m-%d")
            
            # DC Date für Nature
            if date_elem is None:
                date_elem = item.find('{http://purl.org/dc/elements/1.1/}date')
                if date_elem is not None: pub_date = date_elem.text

            return {
                "title": title,
                "link": link,
                "description": clean_html(description),
                "date": pub_date,
                "source": source['name']
            }
        except Exception as e:
            print(f"Fehler bei {source['name']}: {e}")
            continue
            
    return None

def create_study_note():
    study = fetch_study()
    if not study:
        print("Keine Studie gefunden.")
        return

    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    filename = f"STUDY_{date_str}.md"
    filepath = os.path.join(STUDIES_DIR, filename)
    
    # Prüfen ob schon existiert
    if os.path.exists(filepath):
        print(f"Studie für heute ({filename}) existiert bereits.")
        return

    content = f"""---
tags: [study, science, daily, knowledge]
date: {date_str}
source: ScienceDaily
link: {study['link']}
---

# 🔬 {study['title']}

### 📅 Veröffentlicht: {study['date']}

## 📝 Zusammenfassung
{study['description']}

## 🔗 Quelle & Details
[Hier klicken um die ganze Studie zu lesen]({study['link']})

---
*Automatisch generiert von deinem Daily Study Script.*
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Neue Studie gespeichert: {filepath}")

if __name__ == "__main__":
    create_study_note()
