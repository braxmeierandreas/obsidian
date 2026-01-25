import spoonacular as sp
import os
import json
import re
import argparse
from dotenv import load_dotenv
from datetime import datetime
from deep_translator import GoogleTranslator

# Setup paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
COOKBOOK_DIR = os.path.join(ROOT_DIR, '08_COOKBOOK')
ENV_PATH = os.path.join(os.path.dirname(SCRIPT_DIR), '.env')

# Load environment variables
load_dotenv(dotenv_path=ENV_PATH)
API_KEY = os.getenv('SPOONACULAR_API_KEY')

# Translator instance
translator = GoogleTranslator(source='en', target='de')

# Folder Mapping
CATEGORY_MAPPING = {
    'sauce': '01_BASICS',
    'marinade': '01_BASICS',
    'fingerfood': '01_BASICS',
    'appetizer': '02_STARTERS_AND_SMALL_DISHES',
    'salad': '02_STARTERS_AND_SMALL_DISHES',
    'antipasti': '02_STARTERS_AND_SMALL_DISHES',
    'soup': '03_SOUPS_AND_STEWS',
    'stew': '03_SOUPS_AND_STEWS',
    'main course': '04_MAIN_DISHES',
    'side dish': '05_SIDES_AND_VEGETABLES',
    'vegetable': '05_SIDES_AND_VEGETABLES',
    'dessert': '06_BAKED_GOODS_AND_DESSERTS',
    'bread': '06_BAKED_GOODS_AND_DESSERTS',
    'breakfast': '06_BAKED_GOODS_AND_DESSERTS',
    'snack': '07_SNACKS_AND_STREETFOOD',
    'beverage': '07_SNACKS_AND_STREETFOOD',
    'drink': '07_SNACKS_AND_STREETFOOD',
}

DEFAULT_CATEGORY = '04_MAIN_DISHES'

def clean_filename(title):
    return re.sub(r'[<>:"/\\|?*]', '', title).strip()

def translate_safe(text):
    if not text: return ""
    try:
        # GoogleTranslator has a limit per request, but for recipes it should be fine.
        # Strip HTML tags if any (summary often has them)
        clean_text = re.sub('<[^<]+?>', '', text)
        return translator.translate(clean_text)
    except Exception as e:
        print(f"Übersetzungsfehler: {e}")
        return text

def get_category_folder(dish_types):
    for dish_type in dish_types:
        if dish_type in CATEGORY_MAPPING:
            return CATEGORY_MAPPING[dish_type]
    return DEFAULT_CATEGORY

def format_recipe_markdown(recipe_details):
    title_en = recipe_details.get('title', 'Unbenanntes Rezept')
    print(f"Übersetze Titel: {title_en}...")
    title_de = translate_safe(title_en)
    
    servings = recipe_details.get('servings', 1)
    ready_in_minutes = recipe_details.get('readyInMinutes', 0)
    source_url = recipe_details.get('sourceUrl', '')
    image_url = recipe_details.get('image', '')
    
    summary_en = recipe_details.get('summary', '')
    print("Übersetze Zusammenfassung...")
    summary_de = translate_safe(summary_en.split('.')[0] + '.' if summary_en else '')

    # Nutrition
    calories = "N/A"
    protein = "N/A"
    carbs = "N/A"
    fat = "N/A"
    
    if 'nutrition' in recipe_details and 'nutrients' in recipe_details['nutrition']:
        for nutrient in recipe_details['nutrition']['nutrients']:
            if nutrient['name'] == 'Calories':
                calories = f"{nutrient['amount']} {nutrient['unit']}"
            elif nutrient['name'] == 'Protein':
                protein = f"{nutrient['amount']} {nutrient['unit']}"
            elif nutrient['name'] == 'Carbohydrates':
                carbs = f"{nutrient['amount']} {nutrient['unit']}"
            elif nutrient['name'] == 'Fat':
                fat = f"{nutrient['amount']} {nutrient['unit']}"

    # Ingredients
    print("Übersetze Zutaten...")
    ingredients_list = []
    if 'extendedIngredients' in recipe_details:
        for ing in recipe_details['extendedIngredients']:
            original = ing.get('original', '')
            ingredients_list.append(f"- {translate_safe(original)}")
    
    # Instructions
    print("Übersetze Zubereitungsschritte...")
    instructions_list = []
    if 'analyzedInstructions' in recipe_details and recipe_details['analyzedInstructions']:
        for step in recipe_details['analyzedInstructions'][0].get('steps', []):
            number = step.get('number')
            desc = step.get('step')
            instructions_list.append(f"{number}. {translate_safe(desc)}")
    elif 'instructions' in recipe_details:
         instructions_list.append(translate_safe(recipe_details['instructions']))

    # Dish Types for Tags
    dish_types = recipe_details.get('dishTypes', [])
    tags = [f"#{dt.replace(' ', '_')}" for dt in dish_types]
    tags.append("#rezept")
    
    markdown = f"""
---
erstellt: {datetime.now().strftime('%Y-%m-%d %H:%M')}
tags: [{' '.join(tags)}]
quelle: {source_url}
kalorien: {calories}
protein: {protein}
kohlenhydrate: {carbs}
fett: {fat}
portionen: {servings}
zeit: {ready_in_minutes} min
---

# 🥘 {title_de}

![Rezeptbild]({image_url})

> {summary_de}

## 📊 Nährwerte (pro Portion)
| Kalorien | Protein | Kohlenhydrate | Fett |
| :--- | :--- | :--- | :--- |
| **{calories}** | {protein} | {carbs} | {fat} |

## 🛒 Zutaten
*Für {servings} Portionen*

{chr(10).join(ingredients_list)}

## 👩‍🍳 Zubereitung

{chr(10).join(instructions_list)}

---
*Automatisch übersetzt und erstellt mit Gemini CLI & Spoonacular API*
"""
    return markdown, get_category_folder(dish_types), title_de

def search_and_save_recipe(initial_query=None):
    if not API_KEY:
        print("❌ FEHLER: SPOONACULAR_API_KEY nicht in .env gefunden.")
        return

    api = sp.API(API_KEY)
    
    first_run = True

    while True:
        if first_run and initial_query:
            query = initial_query
            first_run = False
        else:
            query = input("\n🔍 Was möchtest du kochen? (Eingabe auf Deutsch möglich): ")
        
        if not query: break
        
        # If query is German, we might want to translate it to English for the API
        query_en = GoogleTranslator(source='auto', target='en').translate(query)
        print(f"Suche nach '{query}' (API-Anfrage: '{query_en}')...")
        
        try:
            results = api.search_recipes_complex(query_en, number=5, addRecipeInformation=True)
            recipes = results.json().get('results', [])
            
            if not recipes:
                print("Keine Rezepte gefunden.")
                continue
            
            print("\nGefundene Rezepte (übersetze Titel für Vorschau...):")
            translated_titles = []
            for idx, recipe in enumerate(recipes):
                t_title = translate_safe(recipe['title'])
                translated_titles.append(t_title)
                print(f"{idx + 1}. {t_title} ({recipe['title']})")
                
            choice = input("\nWelches Rezept möchtest du speichern? (Nummer oder 'n' für neue Suche, 'q' für Ende): ")
            
            if choice.lower() == 'q':
                break
            if choice.lower() == 'n':
                continue
                
            try:
                selection_idx = int(choice) - 1
                if 0 <= selection_idx < len(recipes):
                    selected_recipe = recipes[selection_idx]
                    
                    print(f"Lade Details für '{translated_titles[selection_idx]}'...")
                    details_response = api.get_recipe_information(selected_recipe['id'], includeNutrition=True)
                    details = details_response.json()
                    
                    # Create content (now with translation)
                    content, category_folder, final_title_de = format_recipe_markdown(details)
                    
                    # Save file
                    safe_filename = clean_filename(final_title_de) + ".md"
                    target_dir = os.path.join(COOKBOOK_DIR, category_folder)
                    target_path = os.path.join(target_dir, safe_filename)
                    
                    os.makedirs(target_dir, exist_ok=True)
                    
                    with open(target_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                        
                    print(f"✅ Rezept gespeichert in: {category_folder}/{safe_filename}")
                    
                else:
                    print("Ungültige Auswahl.")
            except ValueError:
                print("Bitte eine Zahl eingeben.")
                
        except Exception as e:
            print(f"Fehler bei der API-Anfrage: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kochbuch Manager")
    parser.add_argument("query", nargs="?", help="Suchbegriff für Rezept (optional)")
    args = parser.parse_args()

    print("=== 🍳 Kochbuch Manager (JETZT AUF DEUTSCH) ===")
    search_and_save_recipe(initial_query=args.query)