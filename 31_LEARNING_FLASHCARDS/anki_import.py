import os
import glob
import re
import requests
import json
import sys

# --- KONFIGURATION ---
ANKI_CONNECT_URL = "http://localhost:8765"

# Finde den Ordner mit den Karteikarten (Das Skript liegt jetzt direkt im Zielordner '19_FLASHCARDS')
try:
    KARTEIKARTEN_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
except Exception:
    # Fallback, falls die Struktur sich ändert
    print("Konnte den Haupt-Karteikarten-Ordner nicht automatisch finden.")
    print("Bitte den Pfad zu '19_Karteikarten' manuell im Skript eintragen.")
    sys.exit(1)
# --- ENDE KONFIGURATION ---

def invoke(action, **params):
    """Sendet eine Anfrage an die AnkiConnect API."""
    requestJson = json.dumps({'action': action, 'version': 6, 'params': params})
    try:
        response = requests.post(ANKI_CONNECT_URL, data=requestJson, timeout=3).json()
    except requests.exceptions.RequestException as e:
        print(f"Fehler: Konnte keine Verbindung zu Anki herstellen auf {ANKI_CONNECT_URL}.")
        print("Stelle sicher, dass Anki läuft und das AnkiConnect Add-on korrekt installiert ist.")
        sys.exit(1)
    
    if 'error' in response and response['error'] is not None:
        raise Exception(response['error'])
    return response.get('result', None)

def parse_markdown_cards(file_path):
    """Parst eine einzelne Markdown-Datei und extrahiert die Karten."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    cards = []
    # Splitten der Datei in einzelne Karten-Abschnitte (erlaubt Leerzeichen um ---)
    parts = re.split(r'\n\s*---\s*\n', content)
    
    for part in parts:
        part = part.strip()
        # Suche nach Frage (Header 1-6, optional "Frage X:")
        question_match = re.search(r'^(?:#{1,6})\s*(?:Frage\s*\d*:)?\s*(.+)', part)
        if not question_match:
            continue
            
        question_text = question_match.group(1).strip()
        
        # Alles nach der Frage-Zeile wird zur Antwort
        answer_raw = part[question_match.end():].strip()
        
        # Optional: **Antwort:** entfernen, falls vorhanden
        if answer_raw.lower().startswith(('**antwort:**', 'antwort:')):
            answer_raw = re.sub(r'^\*?\*?antwort:\*?\*?', '', answer_raw, flags=re.IGNORECASE).strip()

        if question_text and answer_raw:
            answer_html = markdown_to_html(answer_raw)
            question_html = markdown_to_html(question_text)
            
            cards.append({
                'modelName': 'Basic',
                'fields': {
                    'Front': question_html,
                    'Back': answer_html
                },
                'tags': ['ObsidianImport']
            })
            
    return cards

def markdown_to_html(text):
    """Wandelt einfaches Markdown in HTML für Anki um."""
    html = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    html = html.replace('\n', '<br>')
    # Fett: **text** oder __text__
    html = re.sub(r'(\*\*|__)(?=\S)(.+?)(?<=\S)\1', r'<b>\2</b>', html)
    # Kursiv: *text* oder _text_
    html = re.sub(r'(\*|_)(?=\S)(.+?)(?<=\S)\1', r'<i>\2</i>', html)
    # Listenpunkte: - oder *
    html = re.sub(r'^\s*([*-])\s+(.*)', r'<ul><li>\2</li></ul>', html, flags=re.MULTILINE)
    # Mehrere Listenpunkte zusammenfassen
    html = html.replace('</ul><ul>', '')
    return html

def main():
    print(f"Suche nach Karteikarten in: {KARTEIKARTEN_ROOT_DIR}")
    
    if not os.path.isdir(KARTEIKARTEN_ROOT_DIR):
        print(f"Fehler: Das Verzeichnis '{KARTEIKARTEN_ROOT_DIR}' wurde nicht gefunden.")
        print("Bitte erstelle den Ordner '19_Karteikarten' in deinem Obsidian Vault.")
        return

    # Finde alle .md Dateien rekursiv
    all_md_files = glob.glob(os.path.join(KARTEIKARTEN_ROOT_DIR, "**", "*.md"), recursive=True)
    all_md_files = [f for f in all_md_files if os.path.basename(f).lower() != 'readme.md']
    
    if not all_md_files:
        print("Keine Markdown-Dateien (.md) im Ordner gefunden.")
        return
        
    total_added = 0
    total_skipped = 0
    
    for file_path in all_md_files:
        try:
            # Deck-Namen aus Ordner- und Dateistruktur ableiten
            # .../19_Karteikarten/01_Thema/MeineKarten.md -> 01_Thema::MeineKarten
            relative_path = os.path.relpath(file_path, KARTEIKARTEN_ROOT_DIR)
            path_parts = relative_path.split(os.sep)
            
            # Dateiname ohne .md als letzter Teil des Decks
            path_parts[-1] = os.path.splitext(path_parts[-1])[0]
            
            deck_name = "::".join(path_parts)
            
            # Parse die Karten aus der Datei
            cards = parse_markdown_cards(file_path)
            if not cards:
                continue

            print(f"\nVerarbeite '{relative_path}' für Deck '{deck_name}'...")
            
            # Erstelle Deck in Anki
            invoke('createDeck', deck=deck_name)
            
            # Füge Notizen hinzu
            notes_to_add = []
            for card in cards:
                note = {
                    'deckName': deck_name,
                    **card
                }
                notes_to_add.append(note)

            # Duplikate effizienter prüfen mit `canAddNotes`
            can_add_results = invoke('canAddNotes', notes=notes_to_add)
            
            notes_to_actually_add = []
            for i, can_add in enumerate(can_add_results):
                if can_add:
                    notes_to_actually_add.append(notes_to_add[i])
                else:
                    print(f"  . Duplikat übersprungen: {notes_to_add[i]['fields']['Front'][:40]}...")
                    total_skipped += 1
            
            if notes_to_actually_add:
                invoke('addNotes', notes=notes_to_actually_add)
                total_added += len(notes_to_actually_add)
                print(f"  + {len(notes_to_actually_add)} neue Karte(n) hinzugefügt.")

        except Exception as e:
            print(f"Fehler bei der Verarbeitung von '{file_path}': {e}")

    print(f"\n--- Import abgeschlossen ---")
    print(f"Neue Karten hinzugefügt: {total_added}")
    print(f"Duplikate übersprungen: {total_skipped}")

if __name__ == "__main__":
    main()