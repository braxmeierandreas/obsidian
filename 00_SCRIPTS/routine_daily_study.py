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

# ANSI Colors
C_GREEN = "\033[92m"
C_CYAN = "\033[96m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_BOLD = "\033[1m"
C_END = "\033[0m"

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
def get_gemini_summary(abstract, title, topic, full_text=None):
    if not abstract or len(abstract) < 50:
        return "⚠️ Abstract zu kurz für eine fundierte Analyse."

    # Falls Volltext vorhanden ist, nutzen wir einen Teil davon für eine tiefere Analyse
    context_text = full_text[:10000] if full_text else abstract

    prompt = f"""
    Du bist ein hochkarätiger wissenschaftlicher Analyst und persönlicher Coach für Andreas.
    Deine Aufgabe ist es, die vorliegende Studie zum Thema '{topic}' tiefgehend zu analysieren.
    
    Titel: {title}
    Textbasis: {context_text}

    Bitte erstelle eine strukturierte Zusammenfassung in professionellem, aber verständlichem Deutsch:

    1. **🎯 Problemstellung & Ziel:** Was genau wurde untersucht und warum ist das wichtig?
    2. **🧪 Methodik:** Wie sind die Forscher vorgegangen? (Studiendesign, Stichprobe, Methoden)
    3. **📊 Zentrale Ergebnisse:** Was sind die wichtigsten Zahlen, Daten oder Erkenntnisse?
    4. **💡 Diskussion & Einordnung:** Was bedeuten diese Ergebnisse für das Fachgebiet?
    5. **🚀 Action Plan für Andreas:** Erstelle 3-4 konkrete, praxisnahe "Takeaways". Wie kann Andreas dieses Wissen in seinem Alltag, Studium oder Beruf (Gesundheitsförderung/KI) anwenden?

    Formatierung: Nutze klare Überschriften, Fettungen und Listen.
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        print(f"   {C_CYAN}🤖 KI-Analyse wird generiert (Gemini 2.0 Flash)...{C_END}")
        response = requests.post(url, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result and result['candidates']:
                return result['candidates'][0]['content']['parts'][0]['text']
        else:
            print(f"   {C_RED}⚠️ API-Fehler: {response.status_code} - {response.text}{C_END}")
    except Exception as e:
        print(f"   {C_RED}⚠️ Verbindungsfehler: {e}{C_END}")
    return "⚠️ KI konnte keine detaillierte Zusammenfassung generieren. Bitte API-Key oder Verbindung prüfen."

# --- FULL TEXT EXTRACTOR (via pypdf) ---
def extract_text_from_pdf_url(pdf_url):
    """
    Lädt ein PDF herunter und extrahiert den Text.
    """
    if not pdf_url: return None
    
    try:
        print(f"   {C_YELLOW}📄 Lade PDF-Daten: {pdf_url[:60]}...{C_END}")
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(pdf_url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            pdf_file = BytesIO(response.content)
            reader = pypdf.PdfReader(pdf_file)
            text = ""
            # Wir nehmen max 20 Seiten um Zeit/Memory zu sparen
            num_pages = min(len(reader.pages), 20)
            for i in range(num_pages):
                text += reader.pages[i].extract_text() + "\n\n"
            
            text = text.strip()
            if len(text) < 100: return None
            
            print(f"   {C_GREEN}✅ {len(text)} Zeichen Text extrahiert.{C_END}")
            return text
    except Exception as e:
        print(f"   {C_RED}⚠️ PDF-Fehler: {e}{C_END}")
    
    return None

# --- SOURCE 1: SEMANTIC SCHOLAR ---
def fetch_semantic_scholar(topic):
    print(f"{C_BOLD}{C_CYAN}🌍 Suche Semantic Scholar (Open Access): '{topic}'...{C_END}")
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
        print(f"{C_RED}⚠️ Fehler: {e}{C_END}")
    return None

# --- SOURCE 2: PUBMED ---
def fetch_pubmed(topic):
    print(f"{C_BOLD}{C_CYAN}🧬 Suche PubMed (Free Full Text): '{topic}'...{C_END}")
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

    # Jetzt mit Volltext-Support für die KI
    llm_summary = get_gemini_summary(paper['abstract'], paper['title'], topic, paper.get('full_text'))
    
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
        preview_text = paper['full_text'][:20000] # Max 20k Zeichen
        full_text_section = f"""
## 📖 Extrahierter Volltext (Preview)
<details>
<summary><b>Klicken zum Ausklappen des extrahierten Textes</b></summary>

```text
{preview_text}
```

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
        
        print("\n" + C_YELLOW + "="*60 + C_END)
        print(f"{C_BOLD}{C_GREEN}✅ STUDIE GESPEICHERT{C_END}")
        print(C_YELLOW + "="*60 + C_END)
        print(f"{C_BOLD}📂 Pfad:{C_END}  {filepath}")
        print(f"{C_BOLD}🎯 Thema:{C_END} {topic}")
        print(f"{C_BOLD}📚 Titel:{C_END} {paper['title'][:70]}...")
        print(C_YELLOW + "="*60 + C_END + "\n")
        return True
    except Exception as e:
        print(f"{C_RED}❌ Fehler beim Speichern: {e}{C_END}")
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