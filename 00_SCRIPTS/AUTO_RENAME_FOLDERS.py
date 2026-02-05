import os
import re

# --- KONFIGURATION ---
VAULT_DIR = r"C:\Users\braxm\obsidian"

# 1. DAS GROSSE MASTER-MAPPING (00-99)
# Hier wird ALLES einem Platz zugewiesen.
TOP_LEVEL_MAPPING = {
    # --- 00-09 SYSTEM & INBOX ---
    "Templates": "02_TEMPLATES",
    "26_TASK_MANAGER": "05_TASK_MANAGER",
    
    # --- 10-19 PROJECTS (Arbeit & Studium) ---
    "05_BUSINESS": "10_BUSINESS",
    "03_UNIVERSITY": "11_UNIVERSITY_MASTER",
    "13_OFA": "12_PROJECT_OFA",
    "16_BLOG": "13_PROJECT_BLOG",
    "22_GEDA": "14_PROJECT_GEDA",
    "23_MARKET_RESEARCH": "15_MARKET_RESEARCH",
    
    # --- 20-29 AREAS (Leben & Verantwortung) ---
    "01_Andreas": "20_LIFE_ANDREAS",
    "18_PROFIL": "20_LIFE_PROFILE",
    "04_GOALS": "20_LIFE_GOALS_LEGACY",
    "27_REFLECTION_AND_GROWTH": "20_LIFE_REFLECTION",
    "26_CALORIE_TRACKER": "21_HEALTH_TRACKER",
    "21_BGM": "21_HEALTH_BGM",
    "17_HABITS": "21_HEALTH_HABITS",
    "10_THERAPY": "21_HEALTH_MENTAL",
    "14_TRADING": "22_FINANCE_TRADING",
    "comdirect": "22_FINANCE_DOCS",
    "06_HOUSEHOLD": "23_HOUSEHOLD",
    "07_CAR": "24_CAR",
    
    # --- 30-39 RESOURCES (Wissen & Tech) ---
    "10_PROMPT_ENGINEERING": "30_TECH_PROMPTING",
    "25_GEMINI_CLI": "30_TECH_GEMINI",
    "OpenClaw": "30_TECH_OPENCLAW",
    "15_GOOGLE": "30_TECH_GOOGLE",
    "09_LEARNING_SPANISH": "31_LANGUAGES",
    "19_FLASHCARDS": "31_LEARNING_FLASHCARDS",
    "08_COOKBOOK": "32_COOKBOOK",
    "11_EXCALIDRAW": "35_ASSETS_EXCALIDRAW",
    "20_Antigravity": "36_INTEREST_ANTIGRAVITY",
    "26_PHILOSOPHY": "37_PHILOSOPHY",
    
    # --- 90-99 ARCHIVE & MISC ---
    "02_JOURNAL": "90_JOURNAL",
    "12_DOCUMENTS": "95_ARCHIVE_DOCS",
    "24_CLIPPING": "98_CLIPPINGS",
    "nanobanana-output": "99_TEMP_NANOBANANA",
    "Obsidian": "99_CHECK_IF_TRASH" # Sieht nach falschem Ordner aus
}

def clean_subfolder_names(root_path):
    """
    Durchsucht rekursiv Ordner und repariert Namen wie '01_01_Name' -> '01_Name'
    """
    for dirpath, dirnames, filenames in os.walk(root_path, topdown=False):
        for dirname in dirnames:
            old_full_path = os.path.join(dirpath, dirname)
            
            new_dirname = dirname
            
            # REGEL 1: Entferne doppelte Nummerierung (z.B. "01_01_Start" -> "01_Start")
            # Regex sucht nach: Start, 2 Ziffern, Underscore, Nochmal die GLEICHEN 2 Ziffern, Underscore
            match_double = re.match(r"^(\d{2})_\1_(.+)$", dirname)
            if match_double:
                new_dirname = f"{match_double.group(1)}_{match_double.group(2)}"
            
            # REGEL 2: Entferne "REDUCER" Ordnernamen-Artefakte falls gewünscht
            if dirname == "REDUCER":
                new_dirname = "99_REDUCER"

            if new_dirname != dirname:
                new_full_path = os.path.join(dirpath, new_dirname)
                try:
                    os.rename(old_full_path, new_full_path)
                    print(f"      ✨ Cleaned: {dirname} -> {new_dirname}")
                except Exception as e:
                    print(f"      ❌ Error cleaning {dirname}: {e}")

def rename_folders():
    print("--- 🏷️ MEGA-RENAME gestartet ---")
    
    # 1. Top Level Ordner umbenennen
    print("\n[Phase 1] Hauptordner strukturieren...")
    for old_name, new_name in TOP_LEVEL_MAPPING.items():
        old_path = os.path.join(VAULT_DIR, old_name)
        new_path = os.path.join(VAULT_DIR, new_name)
        
        if os.path.exists(old_path) and not os.path.exists(new_path):
            try:
                os.rename(old_path, new_path)
                print(f"✅ ROOT: {old_name} -> {new_name}")
            except Exception as e:
                print(f"❌ ROOT ERROR {old_name}: {e}")
        elif os.path.exists(old_path) and os.path.exists(new_path):
             print(f"⚠️  ROOT SKIP: {old_name} -> {new_name} (Ziel existiert schon - evtl manuell mergen)")

    # 2. Rekursives Aufräumen aller Unterordner
    print("\n[Phase 2] Unterordner bereinigen (Auto-Clean)...")
    # Wir iterieren durch die neuen Hauptordner (oder alle Ordner im Vault)
    # Um sicherzugehen, scannen wir einfach die Top-Level Ordner des Vaults
    for item in os.listdir(VAULT_DIR):
        full_path = os.path.join(VAULT_DIR, item)
        if os.path.isdir(full_path):
            # Ignoriere Systemordner
            if item.startswith(".") or item in ["00_SCRIPTS", "00_VAULT_ORGANIZATION"]:
                continue
            
            # Starte Reinigung für diesen Hauptordner
            clean_subfolder_names(full_path)

    print("\n--- Fertig! Dein Vault ist jetzt strukturiert. ---")

if __name__ == "__main__":
    rename_folders()
