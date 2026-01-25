from pyzotero import zotero
import os
import re

# Konfiguration
LIBRARY_ID = "12839350"
LIBRARY_TYPE = "user"
API_KEY = "C7tNAKFURGW8VPErBMD14Bx4"
BASE_OUTPUT_DIR = r"03_UNIVERSITY\05_KNOWLEDGE_BASE_LITERATURE"

def sanitize_name(name):
    """Entfernt ungültige Zeichen für Dateinamen und Pfade."""
    return re.sub(r'[\\/*?:\"<>|]', "", name).strip()

def get_collection_paths(zot):
    """Ruft alle Collections ab und baut einen Pfad-Index (Key -> Pfadname)."""
    collections = zot.collections()
    col_dict = {c['key']: c for c in collections}
    paths = {}

    for c_key, c_data in col_dict.items():
        path_parts = []
        current = c_data
        # Pfad rekonstruieren (für verschachtelte Ordner)
        while current:
            path_parts.insert(0, sanitize_name(current['data']['name']))
            parent_key = current['data'].get('parentCollection')
            current = col_dict.get(parent_key) if parent_key else None
        
        paths[c_key] = os.path.join(*path_parts)
    
    return paths

def sync_zotero_to_obsidian():
    zot = zotero.Zotero(LIBRARY_ID, LIBRARY_TYPE, API_KEY)
    
    print("--- Rufe Collection-Struktur ab ---")
    collection_paths = get_collection_paths(zot)
    
    print("--- Synchronisiere Items ---")
    items = zot.top(limit=50) # Erhöht auf 50, um mehr Struktur zu sehen
    
    count = 0
    for item in items:
        data = item.get("data", {})
        item_type = data.get("itemType", "")
        
        if item_type in ["attachment", "note"]:
            continue
            
        # Bestimme den Unterordner basierend auf der Collection
        item_collections = data.get('collections', [])
        if item_collections:
            # Wir nehmen die erste Collection, in der das Item ist
            sub_path = collection_paths.get(item_collections[0], "Unsortiert")
        else:
            sub_path = "Unsortiert"

        # Zielverzeichnis erstellen
        target_dir = os.path.join(BASE_OUTPUT_DIR, sub_path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # Metadaten extrahieren
        title = data.get("title", "Unbenannt")
        abstract = data.get("abstractNote", "Kein Abstract vorhanden.")
        publication = data.get("publicationTitle", data.get("university", data.get("publisher", "Unbekannte Quelle")))
        date = data.get("date", "Unbekannt")
        year = date[:4] if len(date) >= 4 else "Unbekannt"
        
        creators = data.get("creators", [])
        author_list = [c.get("lastName", c.get("name", "Unbekannt")) for c in creators]
        primary_author = author_list[0] if author_list else "Unbekannter Autor"
        all_authors = ", ".join(author_list)

        zotero_tags = [tag.get('tag') for tag in data.get('tags', [])]
        obsidian_tags = " ".join([f"#{tag.replace(' ', '_')}" for tag in zotero_tags])

        filename = sanitize_name(f"{primary_author} {year} - {title}") + ".md"
        filepath = os.path.join(target_dir, filename)

        # Markdown Inhalt
        content = f"""
---
type: literature
itemType: {item_type}
author: [{all_authors}]
year: {year}
collection: \"{sub_path}\" 
zotero_link: {item.get('links', {}).get('alternate', {}).get('href', '')}
---

# {title}

> [!abstract] Abstract
> {abstract}

## 📋 Metadaten
- **Autoren:** {all_authors}
- **Quelle:** {publication}
- **Zotero Ordner:** {sub_path}
- **Zotero Link:** [Öffnen]({item.get('links', {}).get('alternate', {}).get('href', '')})

## 🔍 Tags
{obsidian_tags} #literature

---
"""
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        # In Zotero markieren
        if 'synced_to_obsidian' not in zotero_tags:
            try:
                zot.add_tags(item, 'synced_to_obsidian')
                print(f"Neu: [{sub_path}] {filename}")
            except:
                pass
        else:
            print(f"Aktualisiert: [{sub_path}] {filename}")
            
        count += 1

    print(f"\nFertig! {count} Items in Ordnerstruktur einsortiert.")

if __name__ == "__main__":
    sync_zotero_to_obsidian()
