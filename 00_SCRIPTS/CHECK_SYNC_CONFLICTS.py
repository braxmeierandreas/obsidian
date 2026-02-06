import os

# --- KONFIGURATION ---
VAULT_DIR = r"C:\Users\braxm\obsidian"
CONFLICT_PATTERNS = ["conflicted copy", "konfliktkopie", "conflict", "(1)", "(2)", "sync-conflict"]

def find_conflicts():
    print(f"--- 🔍 Suche nach Sync-Konflikten ---")
    conflict_files = []

    for root, dirs, files in os.walk(VAULT_DIR):
        if any(x in root for x in [".git", ".obsidian", ".trash"]):
            continue

        for filename in files:
            lower_name = filename.lower()
            if any(pattern in lower_name for pattern in CONFLICT_PATTERNS):
                full_path = os.path.join(root, filename)
                conflict_files.append(full_path)

    if not conflict_files:
        print("✅ Keine offensichtlichen Konflikt-Dateien gefunden.")
    else:
        print(f"⚠️  {len(conflict_files)} potenzielle Konflikt-Dateien gefunden:")
        for f in conflict_files:
            print(f"📄 {os.path.relpath(f, VAULT_DIR)}")

if __name__ == "__main__":
    find_conflicts()
    input("Suche beendet. Druecke Enter...")