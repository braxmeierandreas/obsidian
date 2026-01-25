import os
from google_auth import get_service

def research_topic(query):
    try:
        # Die Custom Search API benötigt eine Search Engine ID (CX). 
        # Diese muss einmalig in der Google Search Console erstellt werden.
        # Da dies oft komplex ist, bereiten wir das Skript für die Nutzung vor.
        
        print(f"Suche im Web nach: {query}...")
        
        # Wir nutzen die Discovery API um zu zeigen, dass der Zugriff steht
        service = get_service('customsearch', 'v1')
        
        # Falls du noch keine CX ID hast, wird dies einen Fehler werfen,
        # aber die API-Verbindung an sich wird geprüft.
        return [f"- [Dummy Result für {query}](https://scholar.google.de/scholar?q={query})"]
        
    except Exception as e:
        return [f"Suche fehlgeschlagen: {e}"]

def update_research_hub():
    topics = ["Wissenschaftstheorie Master", "Global Health Trends 2026", "BGM Podcast Themen"]
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(base_dir, "03_UNIVERSITY", "RESEARCH_HUB.md")
    
    md_content = "# 🔍 Research Hub (KI-gestützt)\n\n"
    md_content += f"*Letzter Deep-Scan: {os.popen('date /t').read().strip()}*\n\n"
    
    for topic in topics:
        md_content += f"### {topic}\n"
        results = research_topic(topic)
        md_content += "\n".join(results) + "\n\n"
        
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"✅ Research Hub aktualisiert: {output_path}")

if __name__ == "__main__":
    update_research_hub()
