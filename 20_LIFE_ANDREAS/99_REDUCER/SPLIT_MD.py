import os
import re
import shutil
from pathlib import Path

# Konfiguration
MAX_LINES = 2000
SCRIPT_DIR = Path(__file__).parent
BACKUP_DIR = SCRIPT_DIR / "backup"

def save_chunk(output_dir, base_name, part_num, lines):
    # Sucht nach einer Überschrift für den Dateinamen
    title_suffix = ""
    for line in lines[:10]:
        m = re.match(r'^(#{1,6})\s+(.+)', line)
        if m:
            clean_title = "".join(c for c in m.group(2) if c.isalnum() or c in (' ', '_', '-')).strip()
            title_suffix = f"_{clean_title}"
            break
            
    filename = f"{part_num:02d}{title_suffix}.md"
    if len(filename) > 60:
        filename = f"{part_num:02d}{title_suffix[:50]}.md"
        
    output_path = output_dir / filename
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

def split_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if len(lines) <= MAX_LINES:
        print(f"  -> Datei ist kurz genug ({len(lines)} Zeilen).")
        return False

    print(f"  -> Teile {file_path.name} ({len(lines)} Zeilen)...")
    
    # Calculate optimal split size
    import math
    num_parts = math.ceil(len(lines) / MAX_LINES)
    # Ensure at least 2 parts if it's borderline (though the check above handles <= MAX_LINES)
    if num_parts < 2 and len(lines) > MAX_LINES:
        num_parts = 2
        
    target_lines = len(lines) // num_parts
    print(f"  -> Ziel: ~{target_lines} Zeilen pro Datei (in {num_parts} Teilen)")

    base_name = file_path.stem
    output_dir = SCRIPT_DIR / base_name
    output_dir.mkdir(exist_ok=True)

    file_part_num = 1
    current_chunk = []
    header_pattern = re.compile(r'^(#{1,3})\s+(.+)')
    
    for line in lines:
        match = header_pattern.match(line)
        chunk_len = len(current_chunk)
        
        # Split-Logik: 
        # 1. Wir haben das Ziel erreicht UND sind an einer Überschrift
        # 2. ODER wir haben das absolute Limit erreicht (MAX_LINES)
        # 3. Wir wollen aber nicht ZU früh splitten, also z.B. erst ab 90% des Targets nach Headern suchen
        
        split_at_header = match and chunk_len >= target_lines
        # Force split if we exceed target significantly (e.g. +50 lines) or hit MAX
        # This ensures equal sizing even without headers (like in big tables)
        force_split = chunk_len >= (target_lines + 50) or chunk_len >= MAX_LINES
        
        if split_at_header or force_split:
             save_chunk(output_dir, base_name, file_part_num, current_chunk)
             file_part_num += 1
             current_chunk = [line]
        else:
            current_chunk.append(line)
            
    if current_chunk:
        save_chunk(output_dir, base_name, file_part_num, current_chunk)
        
    print(f"  -> In {file_part_num} Teile aufgeteilt in '{output_dir.name}/'")
    return True

def main():
    print("--- MD Verkleinerer gestartet ---")
    files_processed = 0
    
    # Scanne nur MD Dateien im aktuellen Verzeichnis
    for file_path in SCRIPT_DIR.glob("*.md"):
        # Ignoriere README oder das Skript selbst (falls es ein MD wäre)
        if file_path.name.lower() == "readme.md":
            continue
            
        print(f"Prüfe: {file_path.name}")
        try:
            was_split = split_markdown_file(file_path)
            
            # Verschiebe die Originaldatei ins Backup
            if not BACKUP_DIR.exists():
                BACKUP_DIR.mkdir()
            
            shutil.move(str(file_path), str(BACKUP_DIR / file_path.name))
            print(f"  -> Original verschoben nach backup/")
            files_processed += 1
            
        except Exception as e:
            print(f"Fehler bei {file_path.name}: {e}")
            
    if files_processed == 0:
        print("Keine neuen .md Dateien zum Verarbeiten gefunden.")
    else:
        print(f"\nFertig! {files_processed} Datei(en) verarbeitet.")

if __name__ == "__main__":
    main()
