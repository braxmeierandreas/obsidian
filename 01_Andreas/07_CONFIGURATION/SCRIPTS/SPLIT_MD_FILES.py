import os
import re
from pathlib import Path

# Configuration
MAX_LINES = 2000
TARGET_DIR = Path(".")  # Current directory (recursively)

def split_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if len(lines) <= MAX_LINES:
        return

    print(f"Processing: {file_path} ({len(lines)} lines)")
    
    # Create a directory for the parts
    base_name = file_path.stem
    output_dir = file_path.parent / base_name
    output_dir.mkdir(exist_ok=True)

    # Strategy: Find the best delimiter
    # 1. Try splitting by Level 1 headers (# )
    # 2. If chunks are still too big, try Level 2 (## )
    # 3. Fallback: Hard chunking
    
    chunks = []
    current_chunk = []
    
    # Simple regex for headers
    header_pattern = re.compile(r'^(#{1,3})\s+(.+)')
    
    # First pass: identify potential split points (headers)
    # We want to split BEFORE a header if the current chunk is getting big
    
    file_part_num = 1
    
    for line in lines:
        match = header_pattern.match(line)
        
        # logical_break = match and len(current_chunk) > 100 # Don't split immediately if chunk is tiny
        # size_break = len(current_chunk) >= MAX_LINES
        
        # Logic: Always add to current chunk. 
        # But if we hit a header AND the current chunk is "substantial" (e.g. > 500 lines) OR we are forcing a limit
        # then we save the current chunk and start a new one.
        
        is_header = match is not None
        chunk_len = len(current_chunk)
        
        if is_header and chunk_len > 1000:
             # Save current chunk
             save_chunk(output_dir, base_name, file_part_num, current_chunk)
             file_part_num += 1
             current_chunk = [line]
        elif chunk_len >= MAX_LINES:
             # Force split even if no header (try to find a paragraph break if possible, but for now simple split)
             save_chunk(output_dir, base_name, file_part_num, current_chunk)
             file_part_num += 1
             current_chunk = [line]
        else:
            current_chunk.append(line)
            
    # Save last chunk
    if current_chunk:
        save_chunk(output_dir, base_name, file_part_num, current_chunk)
        
    print(f"  -> Split into {file_part_num} parts in '{output_dir}'")

def save_chunk(output_dir, base_name, part_num, lines):
    # Try to find a title from the first few lines of the chunk
    title_suffix = ""
    for line in lines[:5]:
        m = re.match(r'^(#{1,6})\s+(.+)', line)
        if m:
            # Clean filename
            clean_title = "".join(c for c in m.group(2) if c.isalnum() or c in (' ', '_', '-')).strip()
            title_suffix = f"_{clean_title}"
            break
            
    filename = f"{part_num:02d}{title_suffix}.md"
    # limit filename length
    if len(filename) > 50:
        filename = f"{part_num:02d}{title_suffix[:40]}.md"
        
    output_path = output_dir / filename
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

def main():
    print(f"Scanning for .md files > {MAX_LINES} lines in {os.getcwd()}...")
    count = 0
    for file_path in Path(TARGET_DIR).rglob("*.md"):
        # Skip if already inside a split folder (simple heuristic: if parent is same name as file without extension? No, that's complex)
        # Just check line count.
        try:
            # Check size first to avoid reading massive files unnecessarily? 
            # Stat size is bytes. Readlines is safer for exact line count.
            # We'll just read.
            with open(file_path, "r", encoding="utf-8") as f:
                # Read just enough to count newlines? 
                # For simplicity in this script, readlines is fine for <100MB files.
                pass
            
            # Re-open in split function to process
            split_markdown_file(file_path)
            count += 1
        except Exception as e:
            print(f"Skipping {file_path}: {e}")
            
    print("Done.")

if __name__ == "__main__":
    main()
