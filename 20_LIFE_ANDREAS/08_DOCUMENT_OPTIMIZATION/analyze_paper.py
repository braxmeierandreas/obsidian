import os
import sys
import re

def check_paper_optimization(paper_path, keywords_path):
    """
    Checks an academic paper for keyword density and structural markers.
    """
    if not os.path.exists(paper_path):
        print(f"Error: Paper not found at {paper_path}")
        return

    # Load keywords
    keywords = []
    if os.path.exists(keywords_path):
        with open(keywords_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Basic extraction of keywords from markdown list
            keywords = re.findall(r'- **(.*?)**', content)
    
    if not keywords:
        # Fallback common academic high-value terms if file is empty
        keywords = ["Signifikanz", "Methodik", "Empirie", "Diskussion", "Limitationen"]

    with open(paper_path, 'r', encoding='utf-8') as f:
        text = f.read()

    print(f"--- Analysis for: {os.path.basename(paper_path)} ---")
    
    # 1. Keyword Density
    print("\n[1] Keyword Alignment:")
    for kw in keywords:
        count = len(re.findall(rf'\b{re.escape(kw)}\b', text, re.IGNORECASE))
        status = "✅" if count > 0 else "❌"
        print(f"  {status} {kw}: {count} occurrences")

    # 2. Structure Check
    print("\n[2] Structural Integrity (IMRaD):")
    markers = {
        "Einleitung/Introduction": r"(Einleitung|Introduction|Problemstellung)",
        "Methodik/Methodology": r"(Methodik|Methoden|Research Design)",
        "Ergebnisse/Results": r"(Ergebnisse|Findings|Analysis)",
        "Diskussion/Discussion": r"(Diskussion|Interpretation)",
        "Fazit/Conclusion": r"(Fazit|Schlussbetrachtung|Summary)"
    }
    
    for section, pattern in markers.items():
        found = re.search(pattern, text, re.IGNORECASE)
        status = "✅ Found" if found else "⚠️ Missing or unlabelled"
        print(f"  {section}: {status}")

    # 3. Tone Analysis (Heuristic)
    print("\n[3] Tone & Scientific Style:")
    weak_words = ["vielleicht", "irgendwie", "natürlich", "krass", "man"]
    for word in weak_words:
        count = len(re.findall(rf'\b{re.escape(word)}\b', text, re.IGNORECASE))
        if count > 0:
            print(f"  ⚠️ Potential weak phrasing found: '{word}' ({count}x)")

if __name__ == "__main__":
    # Example usage: python check_paper.py my_thesis.md
    if len(sys.argv) > 1:
        check_paper_optimization(sys.argv[1], "02_APPLICATION_MANAGEMENT/STRATEGISCHE_KEYWORDS.md")
    else:
        print("Usage: python analyze_paper.py <path_to_paper.md>")
