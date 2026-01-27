import re
import os

def clean_text(text):
    if not text: return ""
    text = re.sub(r'\[(.*?)\]\{.*?\}', r'\1', text)
    return text.strip()

def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = re.split(r'Kategorie (\d+):', content)
    
    all_actors = []
    
    for i in range(1, len(parts), 2):
        orig_cat = int(parts[i])
        text = parts[i+1]
        
        lines = text.split('\n')
        current_entry = None
        
        for line in lines:
            line = line.strip()
            if not line: continue
            if "Vorgeschlagener Akteur" in line or "-------" in line:
                continue
            
            cols = re.split(r'\s{2,}', line)
            
            if len(cols) >= 2:
                if current_entry:
                    all_actors.append(current_entry)
                
                name = clean_text(cols[0])
                type_ = clean_text(cols[1]) if len(cols) > 1 else ""
                city = clean_text(cols[2]) if len(cols) > 2 else ""
                
                current_entry = {
                    "Akteur": name,
                    "Angebotstyp": type_,
                    "Stadt": city,
                    "Orig_Cat": orig_cat
                }
            elif len(cols) == 1 and current_entry:
                val = clean_text(cols[0])
                if val:
                    current_entry["Akteur"] += " " + val
        
        if current_entry:
            all_actors.append(current_entry)

    return all_actors

def categorize_actor(actor):
    name = actor["Akteur"].lower()
    type_ = actor["Angebotstyp"].lower()
    
    cat1_keywords = ["schule", "gymnasium", "realschule", "grundschule", "gemeinschaftsschule", "sbbz", "kindergarten", "kita", "jugendhaus", "zentrum", "wirkstatt", "krippe"]
    if any(kw in name for kw in cat1_keywords):
        return 1
    
    if "jugendtanzgruppen" in name or "royal ranger" in name or "pfadfinder" in name:
        return 1
        
    cat2_keywords = ["freibad", "bad", "museum", "ferienprogramm", "polizei", "stiftung", "nachsorge", "bibliothek", "pass", "referat", "beratungsstelle", "aok", "bund", "naturfreunde", "caritas", "drk", "rotes kreuz", "feuerwehr"]
    if any(kw in name for kw in cat2_keywords):
        return 2
    
    cat3_keywords = ["verein", "club", "gruppe", "sport", "musik", "jungschar", "turnen", "tischtennis", "badminton", "kirche", "gemeinde", "pfarrei"]
    if any(kw in name for kw in cat3_keywords) or any(kw in type_ for kw in ["sport", "musik", "religion"]):
         return 3
    
    return 4

def generate_md_files(actors, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    cat_data = {1: [], 2: [], 3: [], 4: []}
    
    for a in actors:
        new_cat = categorize_actor(a)
        cat_data[new_cat].append(a)
        
    file_mapping = {
        1: "01_GROSSE_REICHWEITE_REGELMAESSIG.md",
        2: "02_GROSSE_REICHWEITE_GELEGENTLICH.md",
        3: "03_KLEINE_REICHWEITE_REGELMAESSIG.md",
        4: "04_KLEINE_REICHWEITE_GELEGENTLICH.md"
    }
    
    cat_names = {
        1: "Kategorie 1: Große Reichweite & Regelmäßiger Kontakt",
        2: "Kategorie 2: Große Reichweite & Gelegentlicher Kontakt",
        3: "Kategorie 3: Kleine Reichweite & Regelmäßiger Kontakt",
        4: "Kategorie 4: Kleine Reichweite & Gelegentlicher Kontakt"
    }
    
    for cat_id, filename in file_mapping.items():
        full_path = os.path.join(output_dir, filename)
        items = cat_data[cat_id]
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(f"# {cat_names[cat_id]}\n\n")
            f.write("| Kategorie | Akteur | Angebotstyp | Stadt/Gemeinde | URL | Telefonnummer | Email | Ansprechpartner |\n")
            # Dynamic separator
            sep = "| " + " | ".join(["---"] * 8) + " |\n"
            f.write(sep)
            
            for item in items:
                row = [
                    f"Kategorie {cat_id}",
                    item["Akteur"],
                    item["Angebotstyp"],
                    item["Stadt"],
                    "", "", "", ""
                ]
                f.write("| " + " | ".join(row) + " |\n")
        print(f"Generated {full_path} with {len(items)} items")

input_file = "neue akteure/Neuanschreiben_Akteure.md"
output_dir = "neue akteure/01_KATEGORIISIERT"
actors = parse_file(input_file)
generate_md_files(actors, output_dir)
