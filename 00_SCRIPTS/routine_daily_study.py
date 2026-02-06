import sys
import time
import random
import requests
import json
import os
import datetime
import xml.etree.ElementTree as ET
from io import BytesIO
import pypdf

# --- KONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
STUDIES_DIR = os.path.join(ROOT_DIR, "01_Andreas", "05_KNOWLEDGE", "DAILY_STUDIES")

# API Key für Gemini (Google AI)
GEMINI_API_KEY = "AIzaSyAh_5x6xR5qj1ih7ZGqksYd97tx8SFvzts"

TOPICS = [
    "Public Health", "Health Promotion", "Artificial Intelligence", 
    "Large Language Models", "Clinical Psychology", "Exercise Physiology", 
    "Behavioral Economics", "Sleep Science", "Nutrition Science"
]

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# --- GEMINI AI SUMMARY ---
def get_gemini_summary(abstract, title, topic):
    if not abstract or len(abstract) < 50:
        return "⚠️ Abstract zu kurz für Zusammenfassung."

    prompt = f"""
    Du bist ein persönlicher wissenschaftlicher Coach für Andreas.
    Analysiere diesen wissenschaftlichen Text zum Thema '{topic}'.
    
    Titel: {title}
    Text: {abstract}

    Deine Aufgabe:
    1. Fasse die Kernaussagen in EINFACHEM Deutsch zusammen (Max 3-4 Sätze).
    2. Erstelle eine Liste mit 3 konkreten "Action Items" oder "Takeaways" für mein persönliches Leben. Wie kann ich das anwenden?

    Format:
    **🧠 Was wurde gefunden?**
    [Deine Zusammenfassung]

    **🚀 Action Plan (Wie nutze ich das?)**
    - [Punkt 1]
    - [Punkt 2]
    - [Punkt 3]
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        print(f"🤖 Generiere Zusammenfassung mit Google Gemini (2.0 Flash)...")
        response = requests.post(url, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result and result['candidates']:
                return result['candidates'][0]['content']['parts'][0]['text']
    except:
        pass
    return "⚠️ KI hat keine Antwort generiert."

# --- FULL TEXT EXTRACTOR (via pypdf) ---
def extract_text_from_pdf_url(pdf_url):
    """
    Lädt ein PDF herunter und extrahiert den Text.
    """
    if not pdf_url: return None
    
    try:
        print(f"📄 Lade PDF herunter: {pdf_url} ...")
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(pdf_url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            print("📄 Extrahiere Text aus PDF...")
            pdf_file = BytesIO(response.content)
            reader = pypdf.PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n\n"
            
            # Bereinigung (einfach)
            text = text.strip()
            if len(text) < 100: return None # Zu wenig Text (vllt. Bild-PDF)
            
            return text
        else:
            print(f"⚠️ PDF Download Fehler: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Fehler beim PDF-Parsing: {e}")
    
    return None

# --- SOURCE 1: SEMANTIC SCHOLAR ---
def fetch_semantic_scholar(topic):
    print(f"🌍 Suche Semantic Scholar (Open Access): '{topic}'...")
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    current_year = datetime.datetime.now().year
    params = {
        "query": topic,
        "limit": 40,
        "fields": "title,authors,abstract,year,citationCount,url,venue,openAccessPdf,isOpenAccess",
        "year": f"{current_year-3}-{current_year}",
        "sort": "citationCount:desc",
        "openAccessPdf": "" 
    }
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, params=params, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            candidates = []
            if data.get("data"):
                # Filter: Nur Papers mit ECHTEM PDF Link
                for p in data["data"]:
                    if p.get("openAccessPdf") and p.get("openAccessPdf").get("url"):
                        candidates.append(p)
                
                # Wenn keine PDFs, nimm normale Ergebnisse als Fallback
                if not candidates:
                    candidates = data["data"]
                
                paper = random.choice(candidates)
                
                # Versuch Full Text zu holen
                pdf_url = paper.get("openAccessPdf", {}).get("url")
                full_text = extract_text_from_pdf_url(pdf_url)
                
                return {
                    "title": paper.get("title"),
                    "authors": ", ".join([a["name"] for a in paper.get("authors", [])][:3]),
                    "year": paper.get("year"),
                    "abstract": paper.get("abstract"),
                    "url": paper.get("url"),
                    "citations": paper.get("citationCount", 0),
                    "venue": paper.get("venue", "Semantic Scholar"),
                    "pdf": pdf_url,
                    "full_text": full_text,
                    "source": "Semantic Scholar"
                }
    except Exception as e:
        print(f"⚠️ Fehler: {e}")
    return None

# --- SOURCE 2: PUBMED ---
def fetch_pubmed(topic):
    print(f"🧬 Suche PubMed (Free Full Text): '{topic}'...")
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    s_params = {
        "db": "pubmed",
        "term": f"{topic} AND (free full text[sb])", 
        "retmode": "json",
        "retmax": "30",
        "sort": "date"
    }
    try:
        r = requests.get(search_url, params=s_params, timeout=10)
        if r.status_code != 200: return None
        id_list = r.json().get("esearchresult", {}).get("idlist", [])
        if not id_list: return None
        pmid = random.choice(id_list)
        
        fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        f_params = {"db": "pubmed", "id": pmid, "retmode": "xml"}
        r_det = requests.get(fetch_url, params=f_params, timeout=10)
        root = ET.fromstring(r_det.content)
        article = root.find(".//Article")
        
        title = article.findtext(".//ArticleTitle")
        
        # Abstract Parsing
        abstract_parts = []
        abstract_elem = article.find(".//Abstract")
        if abstract_elem is not None:
            for text_elem in abstract_elem.findall("AbstractText"):
                label = text_elem.get("Label")
                text = text_elem.text
                if text:
                    if label: abstract_parts.append(f"**{label}:** {text}")
                    else: abstract_parts.append(text)
        abstract = "\n\n".join(abstract_parts) if abstract_parts else "Kein Abstract."

        authors = []
        for au in article.findall(".//Author"):
            l = au.findtext("LastName")
            i = au.findtext("Initials")
            if l and i: authors.append(f"{l} {i}")
        
        # PMC Link (Versuch PDF zu holen, wenn PMC ID existiert - hier vereinfacht)
        pdf_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/pmid/{pmid}/pdf"
        # Bei PubMed ist PDF Scaping schwerer (oft geblockt), wir probieren es trotzdem
        full_text = None # extract_text_from_pdf_url(pdf_url) # Oft geblockt bei PMC

        return {
            "title": title,
            "authors": ", ".join(authors[:3]),
            "year": article.findtext(".//PubDate/Year") or "2024",
            "abstract": abstract,
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "citations": "N/A",
            "venue": "PubMed",
            "pdf": None, # PMC Links sind oft keine direkten PDFs ohne Auth
            "full_text": full_text,
            "source": "PubMed"
        }
    except:
        return None

def create_markdown(paper, topic):
    if not paper: return False

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.datetime.now().strftime("%H%M%S")
    filename = f"STUDY_{today}_{timestamp}.md"
    filepath = os.path.join(STUDIES_DIR, filename)

    llm_summary = get_gemini_summary(paper['abstract'], paper['title'], topic)
    
    pdf_section = ""
    if paper.get('pdf'):
        pdf_section = f"""
## 📄 Volltext-Zugriff
> [!PDF] **HIER KLICKEN FÜR PDF**
> [{paper['pdf']}]({paper['pdf']})
"""
    
    full_text_section = ""
    if paper.get('full_text'):
        # Text kürzen falls extrem lang
        preview_text = paper['full_text'][:15000] # Max 15k Zeichen für Markdown Performance
        full_text_section = f"""
## 📖 Extrahierter Volltext (Preview)
<details>
<summary>Klicken zum Lesen des Volltextes</summary>

{preview_text}

*(Text automatisch extrahiert, Formatierung kann abweichen)*
</details>
"""

    content = f"""---
tags: [study, science, daily, {topic.replace(" ", "_").lower()}]
date: {today}
topic: "{topic}"
type: academic_paper
year: {paper['year']}
source: {paper['source']}
has_full_text: {str(paper.get('full_text') is not None).lower()}
---

# 🎓 {paper['title']}

> **Thema:** {topic} | **Quelle:** {paper['source']} | **Jahr:** {paper['year']}
> **Autoren:** {paper['authors']}

---

## 🤖 KI-Zusammenfassung & Action Plan
{llm_summary}

---

## 📝 Abstract
{paper['abstract']}

---

{full_text_section}

{pdf_section}

## 🔗 Original-Link
- [Zur Webseite der Studie]({paper['url']})
"""
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ Studie erfolgreich gespeichert!\n📂 {filepath}\nTopic: {topic}\nTitel: {paper['title']}")
        return True
    except Exception as e:
        print(f"Fehler: {e}")
        return False

def main():
    ensure_dir(STUDIES_DIR)
    
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
        random_mode = False
    else:
        topic = random.choice(TOPICS)
        random_mode = True

    # 1. Semantic Scholar (Mit PDF Parsing)
    paper = fetch_semantic_scholar(topic)
    
    # 2. PubMed (Full Text Filter)
    if not paper:
        paper = fetch_pubmed(topic)
    
    if not paper and random_mode:
        print("Erstes Thema leer, versuche ein anderes...")
        topic = random.choice(TOPICS)
        paper = fetch_semantic_scholar(topic) or fetch_pubmed(topic)

    if paper:
        create_markdown(paper, topic)
        sys.exit(0)
    else:
        print(f"❌ Nichts gefunden für '{topic}'.")
        sys.exit(1)

if __name__ == "__main__":
    main()