import os
import shutil
import re

TRANSLATIONS = {
    # Top level
    "ANDREAS": "ANDREAS",
    "TAGEBUCH": "JOURNAL",
    "STUDIUM": "UNIVERSITY",
    "ZIELE": "GOALS",
    "BUSINESS": "BUSINESS",
    "HAUSHALT": "HOUSEHOLD",
    "AUTO": "CAR",
    "KOCHBUCH": "COOKBOOK",
    "SPANISCH_LERNEN": "LEARNING_SPANISH",
    "PROMPT_ENGINEERING": "PROMPT_ENGINEERING",
    "EXCALIDRAW": "EXCALIDRAW",
    "DOKUMENTE": "DOCUMENTS",
    "OFA": "OFA",
    
    # Sub-folders General
    "DASHBOARD": "DASHBOARD",
    "TAEGLICH": "DAILY",
    "PERSONEN": "PEOPLE",
    "LEBEN": "LIFE",
    "WISSEN": "KNOWLEDGE",
    "REFERENZ": "REFERENCE",
    "KONFIGURATION": "CONFIGURATION",
    "DOKUMENTEN_OPTIMIERUNG": "DOCUMENT_OPTIMIZATION",
    "BLOCKIERTE_SEITEN": "BLOCKED_SITES",
    "ARCHIV": "ARCHIVE",
    "VORLAGEN": "TEMPLATES",
    "KATEGORIEN": "CATEGORIES",
    "KALENDER": "CALENDAR",
    "ANHAENGE": "ATTACHMENTS",
    "RESEARCH_PROJECT": "RESEARCH_PROJECT",
    "DOZENTEN": "LECTURERS",
    "FORSCHUNGSPROJEKT": "RESEARCH_PROJECT_WORK",
    "FORMULARE": "FORMS",
    "SPO": "REGULATIONS",
    "WRITINGSTYLE": "WRITING_STYLE",
    "GESUNDHEIT": "HEALTH",
    "VERMOEGEN": "WEALTH",
    "BEZIEHUNGEN": "RELATIONSHIPS",
    "SINN": "PURPOSE",
    "LONDON_REISE_JESSICA": "LONDON_TRIP_JESSICA",
    "EXECUTIVE_SUMMARY": "EXECUTIVE_SUMMARY",
    "GESCHAEFTSIDEE_KONZEPT": "BUSINESS_IDEA_CONCEPT",
    "MARKTANALYSE": "MARKET_ANALYSIS",
    "WETTBEWERBSANALYSE": "COMPETITOR_ANALYSIS",
    "GESCHAEFTSMODELL": "BUSINESS_MODEL",
    "MARKETING_VERTRIEB": "MARKETING_SALES",
    "FINANZPLANUNG": "FINANCIAL_PLANNING",
    "ORGANISATION_PERSONAL": "ORGANIZATION_PERSONNEL",
    "RISIKOANALYSE": "RISK_ANALYSIS",
    "IMPLEMENTIERUNGSPLAN": "IMPLEMENTATION_PLAN",
    "ANHANG": "APPENDIX",
    "VORRAETE": "SUPPLIES",
    "GRUNDLAGEN": "BASICS",
    "VORSPEISEN_UND_KLEINE_GERICHTE": "STARTERS_AND_SMALL_DISHES",
    "SUPPEN_UND_EINTOEPFE": "SOUPS_AND_STEWS",
    "HAUPTGERICHTE": "MAIN_DISHES",
    "BEILAGEN_UND_GEMUESE": "SIDES_AND_VEGETABLES",
    "BACKWAREN_UND_DESSERTS": "BAKED_GOODS_AND_DESSERTS",
    "SNACKS_UND_STREETFOOD": "SNACKS_AND_STREETFOOD",
    "GRAMMATIK": "GRAMMAR",
    "VOKABULAR": "VOCABULARY",
    "AUSSPRACHE": "PRONUNCIATION",
    "UEBUNGEN": "EXERCISES",
    "RESSOURCEN": "RESOURCES",
    "NOTIZEN_AUS_KURSEN": "COURSE_NOTES",
    "TEXTE": "TEXTS",
    "META_PROMPTS": "META_PROMPTS",
    "DATENANALYSE": "DATA_ANALYSIS",
    "CODE_GENERIERUNG": "CODE_GENERATION",
    "TEXTZUSAMMENFASSUNG": "TEXT_SUMMARIZATION",
    "BILDGENERIERUNG": "IMAGE_GENERATION",
    "SPRACHENLERNEN": "LANGUAGE_LEARNING",
    "EINGANG": "INBOX",
    "LEBENSBEREICHE_SCHNELLZUGRIFF": "LIFE_AREAS_QUICK_ACCESS",
    "RUECKBLICKE": "REVIEWS",
    "ROUTINEN": "ROUTINES",
    "ARBEIT": "WORK",
    "FAMILIE": "FAMILY",
    "FREUNDE": "FRIENDS",
    "GEBURTSTAGE_FREUNDE": "FRIEND_BIRTHDAYS",
    "LEBENSBEREICHE": "LIFE_AREAS",
    "SKILL_ENTWICKLUNG": "SKILL_DEVELOPMENT",
    "KONZEPTE_UND_PRINZIPIEN": "CONCEPTS_AND_PRINCIPLES",
    "GERAETE": "DEVICES",
    "SICHERHEIT": "SECURITY",
    "SCRIPTS": "SCRIPTS",
    "METHODIK_HANDBUCH": "METHODOLOGY_HANDBOOK",
    "BEWERBUNGS_MANAGEMENT": "APPLICATION_MANAGEMENT",
    "AKADEMISCHE_STRUKTURIERUNG": "ACADEMIC_STRUCTURING",
    "JANUAR": "JANUARY",
    "FEBRUAR": "FEBRUARY",
    "MAERZ": "MARCH",
    "APRIL": "APRIL",
    "MAI": "MAY",
    "JUNI": "JUNE",
    "JULI": "JULY",
    "AUGUST": "AUGUST",
    "SEPTEMBER": "SEPTEMBER",
    "OKTOBER": "OCTOBER",
    "NOVEMBER": "NOVEMBER",
    "DEZEMBER": "DECEMBER",
    "TRAINING": "TRAINING",
    "ERNAEHRUNG": "NUTRITION",
    "MENTAL": "MENTAL",
    "REGENERATION": "RECOVERY",
    "TRAINING_UND_AUFZEICHNUNGEN": "TRAINING_AND_LOGS",
    "TRAININGSPLAENE": "TRAINING_PLANS",
    "AUSGABEN": "EXPENSES",
    "BUDGETPLANUNG": "BUDGET_PLANNING",
    "EINNAHMEN": "INCOME",
    "SCHULDEN": "DEBTS",
    "STEUERN": "TAXES",
    "VERMOEGEN_UND_INVESTMENTS": "ASSETS_AND_INVESTMENTS",
    "LESEPLAN": "READING_PLAN",
    "BIBELSTUDIUM": "BIBLE_STUDY",
    "GEBETE": "PRAYERS",
    "GEDANKEN_UND_FRAGEN": "THOUGHTS_AND_QUESTIONS",
    "PASTA_UND_NUDELN": "PASTA_AND_NOODLES",
    "REISGERICHTE": "RICE_DISHES",
    "FLEISCH_UND_GEFLUEGEL": "MEAT_AND_POULTRY",
    "VEGETARISCH_UND_VEGAN": "VEGETARIAN_AND_VEGAN",
    "FITNESSTRAINER": "FITNESS_TRAINER",
    "ERNÄHRUNGSBERATER": "NUTRITIONIST",
    "PERSONAL_TRAINER": "PERSONAL_TRAINER",
    "C_LIZENZ": "C_LICENSE",
    "B_LIZENZ": "B_LICENSE",
    "A_LIZENZ": "A_LICENSE",
    "LIZENZEN": "LICENSES",
    "ERNÄHRUNGSBERATER": "NUTRITIONIST",
    "ERNAEHRUNGSBERATER": "NUTRITIONIST",
    
    # Specific University Modules/Folders
    "BEWEGUNG_UND_GESUNDHEIT": "MOVEMENT_AND_HEALTH",
    "DIGITALISIERUNG_IM_GESUNDHEITSWESEN": "DIGITALIZATION_IN_HEALTHCARE",
    "EVIDENZ_BASED_PRACTICE": "EVIDENCE_BASED_PRACTICE",
    "GLOBAL_HEALTH": "GLOBAL_HEALTH",
    "REGIONAL_HEALTH_PROMOTION": "REGIONAL_HEALTH_PROMOTION",
    "REVIEW_VERFAHREN": "REVIEW_PROCESS",
    "WISSENSCHAFTSTHEORIE": "PHILOSOPHY_OF_SCIENCE",
    "AUSARBEITUNG": "ELABORATION",
    "PROJEKTORGANISATION": "PROJECT_ORGANIZATION",
    "TAG_DER_GESUNDHEIT": "HEALTH_DAY",
    "ERGEBNISSE": "RESULTS",
    "ABSCHLUSSARBEIT": "THESIS",
    "VORGAENGERPROJEKT": "PREVIOUS_PROJECT",
    "DATEN_&_ANALYSE": "DATA_AND_ANALYSIS",
    "AKTEURE": "ACTORS",
    "ARBEITSAUFRAG_KICK_OFF": "WORK_ORDER_KICK_OFF",
    "EXPOS": "EXPOSE",
    "PROJEKT_MANAGEMENT": "PROJECT_MANAGEMENT",
    "DATENSATZ_DESTATIS": "DATASET_DESTATIS",
    "DETERMINANTEN_FUER_GESUNDHEIT": "DETERMINANTS_OF_HEALTH",
    "EMPIRISCHE_METHODEN": "EMPIRICAL_METHODS",
    "VERSORGUNGSFORSCHUNG": "HEALTH_SERVICES_RESEARCH",
    "WAHLPFLICHTMODUL": "ELECTIVE_MODULE",
    "RESONANZ_PRAESENTATION": "RESONANCE_PRESENTATION",
    "UNBENANNT": "UNTITLED",
    "VERKLEINER": "REDUCER",
    "DATENERHEBUNG": "DATA_COLLECTION",
    "AKTEURSDATENBANK": "ACTOR_DATABASE",
    "ANALYSE": "ANALYSIS",
    "PROJEKTDOKUMENTE": "PROJECT_DOCUMENTS",
    "ANSCHREIBEN_INTERVIEWS": "INTERVIEW_COVER_LETTERS",
    "SONSTIGE_NOTIZEN": "OTHER_NOTES",
    "BRAINSTORMING": "BRAINSTORMING"
}

def translate_name(name):
    # Standardize spaces and dashes to underscores first
    name = name.replace(' ', '_').replace('-', '_')
    
    # Split number and text
    match = re.match(r'^(\d+)[._\-\s]+(.*)', name)
    if match:
        prefix = match.group(1)
        text = match.group(2).upper()
        if text in TRANSLATIONS:
            return f"{int(prefix):02d}_{TRANSLATIONS[text]}"
        return f"{int(prefix):02d}_{text}"
    
    # No number prefix
    text = name.upper()
    if text in TRANSLATIONS:
        return TRANSLATIONS[text]
    return text

def process_directory(root_dir='.'):
    try:
        items = os.listdir(root_dir)
    except PermissionError:
        return

    # Filter directories
    dirs = [d for d in items if os.path.isdir(os.path.join(root_dir, d)) and d not in ['.obsidian', '.Papierkorb', '.git']]
    
    # 1. Renaming pass for this level
    moves = {}
    for d in dirs:
        target = translate_name(d)
        if target not in moves:
            moves[target] = []
        moves[target].append(d)
        
    for target, sources in moves.items():
        primary = sources[0]
        primary_path = os.path.join(root_dir, primary)
        
        # Merge duplicates at this level
        for other in sources[1:]:
            other_path = os.path.join(root_dir, other)
            print(f"Merging {other_path} -> {primary_path}")
            try:
                for item in os.listdir(other_path):
                    s = os.path.join(other_path, item)
                    d_path = os.path.join(primary_path, item)
                    if os.path.exists(d_path):
                        base, ext = os.path.splitext(item)
                        d_path = os.path.join(primary_path, f"{base}_DUP{ext}")
                    shutil.move(s, d_path)
                os.rmdir(other_path)
            except Exception as e:
                print(f"Error merging {other}: {e}")
        
        # Rename primary to target (handles CAPS and English)
        final_path = os.path.join(root_dir, target)
        if primary != target:
            try:
                os.rename(primary_path, final_path)
                print(f"Renamed: {primary_path} -> {final_path}")
            except OSError:
                # Try temp rename
                temp_path = os.path.join(root_dir, f"{target}_TEMP_{os.getpid()}")
                try:
                    os.rename(primary_path, temp_path)
                    os.rename(temp_path, final_path)
                    print(f"Renamed (via temp): {primary_path} -> {final_path}")
                except Exception as e:
                    print(f"Failed to rename {primary_path} -> {final_path}: {e}")

    # 2. Recurse pass
    # Get the (possibly renamed) dirs again
    try:
        current_items = os.listdir(root_dir)
        current_dirs = [d for d in current_items if os.path.isdir(os.path.join(root_dir, d)) and d not in ['.obsidian', '.Papierkorb', '.git']]
        for d in current_dirs:
            process_directory(os.path.join(root_dir, d))
    except Exception:
        pass

def rename_root_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f not in ['standardize_final.py', 'GEMINI.md', 'rename_script.ps1']]
    for f in files:
        base, ext = os.path.splitext(f)
        new_base = base.upper().replace(' ', '_').replace('-', '_')
        if base != new_base:
            try:
                os.rename(f, new_base + ext)
                print(f"Renamed root file: {f} -> {new_base + ext}")
            except Exception:
                pass

if __name__ == "__main__":
    process_directory()
    rename_root_files()
