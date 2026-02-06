import sys
import time
import random
import requests
import json
import os
import datetime
import xml.etree.ElementTree as ET

import sys
import time
import random
import requests
import json
import os
import datetime
import xml.etree.ElementTree as ET

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

# --- GEMINI AI SUMMARY (Via Direct API Key) ---
def get_gemini_summary(abstract, title, topic):
    """
    Nutzt die Google Generative Language API (Gemini) via API Key.
    """
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

    # Versuche den Pfad: Gemini 2.0 Flash (Top aktuell und verfügbar für diesen Key)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        print(f"🤖 Generiere Zusammenfassung mit Google Gemini (2.0 Flash)...")
        response = requests.post(url, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result and result['candidates']:
                return result['candidates'][0]['content']['parts'][0]['text']
            else:
                return "⚠️ KI hat keine Antwort generiert (leeres Ergebnis)."
        else:
            return f"⚠️ API Fehler: {response.status_code} - {response.text[:100]}"
            
    except Exception as e:
        return f"⚠️ Verbindungsfehler: {str(e)[:100]}..."

# --- SOURCE 1: SEMANTIC SCHOLAR ---
def fetch_semantic_scholar(topic):
    print(f"🌍 Suche Semantic Scholar: '{topic}'...")
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    current_year = datetime.datetime.now().year
    params = {
        "query": topic,
        "limit": 10,
        "fields": "title,authors,abstract,year,citationCount,url,venue,openAccessPdf",
        "year": f"{current_year-3}-{current_year}",
        "sort": "citationCount:desc"
    }
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, params=params, headers=headers, timeout=10)
        if r.status_code == 200:
            data = r.json()
            if data.get("data"):
                paper = random.choice(data["data"])
                return {
                    "title": paper.get("title"),
                    "authors": ", ".join([a["name"] for a in paper.get("authors", [])][:3]),
                    "year": paper.get("year"),
                    "abstract": paper.get("abstract"),
                    "url": paper.get("url"),
                    "citations": paper.get("citationCount", 0),
                    "venue": paper.get("venue", "Semantic Scholar"),
                    "pdf": paper.get("openAccessPdf", {}).get("url"),
                    "source": "Semantic Scholar"
                }
    except:
        pass
    return None

# --- SOURCE 2: PUBMED (IMPROVED PARSER) ---
def fetch_pubmed(topic):
    print(f"🧬 Suche PubMed: '{topic}'...")
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    s_params = {
        "db": "pubmed",
        "term": f"{topic} AND (free full text[sb] OR review[pt])", 
        "retmode": "json",
        "retmax": "20",
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
        
        # --- IMPROVED ABSTRACT PARSING ---
        abstract_parts = []
        abstract_elem = article.find(".//Abstract")
        if abstract_elem is not None:
            # Manchmal ist der Text direkt im AbstractText
            for text_elem in abstract_elem.findall("AbstractText"):
                label = text_elem.get("Label")
                text = text_elem.text
                if text:
                    if label:
                        abstract_parts.append(f"**{label}:** {text}")
                    else:
                        abstract_parts.append(text)
        
        abstract = "\n\n".join(abstract_parts) if abstract_parts else "Kein Abstract verfügbar."
        
        authors = []
        for au in article.findall(".//Author"):
            last = au.findtext("LastName")
            initials = au.findtext("Initials")
            if last and initials: authors.append(f"{last} {initials}")
        author_str = ", ".join(authors[:3])
        
        year = article.findtext(".//PubDate/Year")
        if not year: year = datetime.datetime.now().year
        
        return {
            "title": title,
            "authors": author_str,
            "year": year,
            "abstract": abstract,
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "citations": "N/A (PubMed)",
            "venue": "PubMed / NIH",
            "pdf": None, 
            "source": "PubMed"
        }
            
    except Exception as e:
        print(f"⚠️ PubMed Fehler: {e}")
    return None

def create_markdown(paper, topic):
    if not paper: return False

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.datetime.now().strftime("%H%M%S")
    filename = f"STUDY_{today}_{timestamp}.md"
    filepath = os.path.join(STUDIES_DIR, filename)

    # Gemini Summary abrufen
    llm_summary = get_gemini_summary(paper['abstract'], paper['title'], topic)
    
    pdf_link = ""
    if paper.get('pdf'):
        pdf_link = f"\n> [!PDF] [Direktes PDF öffnen]({paper['pdf']})"

    content = f"""---
tags: [study, science, daily, {topic.replace(" ", "_").lower()}]
date: {today}
topic: "{topic}"
type: academic_paper
year: {paper['year']}
source: {paper['source']}
---

# 🎓 {paper['title']}

> **Thema:** {topic} | **Quelle:** {paper['source']} | **Jahr:** {paper['year']}
> **Autoren:** {paper['authors']}

---

## 🤖 KI-Zusammenfassung & Action Plan
{llm_summary}

---

## 📝 Original Abstract (Englisch)
{paper['abstract']}

---

## 🔗 Links
- [Zur Studie]({paper['url']})
{pdf_link}
"""
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✅ Studie erfolgreich gespeichert!\n📂 {filepath}\nTopic: {topic}\nTitel: {paper['title']}")
        return True
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")
        return False

def main():
    ensure_dir(STUDIES_DIR)
    
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
        random_mode = False
    else:
        topic = random.choice(TOPICS)
        random_mode = True

    # Reihenfolge: Semantic Scholar -> PubMed
    paper = fetch_semantic_scholar(topic)
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