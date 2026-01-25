import os
from google_auth import get_service

def setup_nutrition_tracking():
    try:
        forms_service = get_service('forms', 'v1')
        drive_service = get_service('drive', 'v3')
        
        title = "Nutrition & Gewicht Log (Andreas)"
        
        # 1. Formular erstellen
        form_body = {"info": {"title": title, "documentTitle": title}}
        form = forms_service.forms().create(body=form_body).execute()
        form_id = form['formId']
        
        # 2. Fragen hinzufügen (Kalorien, Protein, Gewicht)
        update_body = {
            "requests": [
                {
                    "createItem": {
                        "item": {
                            "title": "Kalorien (kcal)",
                            "questionItem": {"question": {"required": True, "textQuestion": {}}}
                        },
                        "location": {"index": 0}
                    }
                },
                {
                    "createItem": {
                        "item": {
                            "title": "Protein (g)",
                            "questionItem": {"question": {"required": True, "textQuestion": {}}}
                        },
                        "location": {"index": 1}
                    }
                },
                {
                    "createItem": {
                        "item": {
                            "title": "Gewicht (kg)",
                            "questionItem": {"question": {"required": False, "textQuestion": {}}}
                        },
                        "location": {"index": 2}
                    }
                }
            ]
        }
        forms_service.forms().batchUpdate(formId=form_id, body=update_body).execute()
        
        form_url = f"https://docs.google.com/forms/d/{form_id}/viewform"
        
        # In Obsidian vermerken
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        health_path = os.path.join(base_dir, "04_GOALS", "01_HEALTH", "NUTRITION_LOG_INFO.md")
        
        os.makedirs(os.path.dirname(health_path), exist_ok=True)
        
        with open(health_path, "w", encoding="utf-8") as f:
            f.write(f"# 🥗 Nutrition Tracking Setup\n\n")
            f.write(f"Hier ist dein Link für das mobile Tracking:\n\n")
            f.write(f"🔗 **[ZUM FORMULAR]({form_url})**\n\n")
            f.write(f"ID: `{form_id}`\n\n")
            f.write(f"--- \n*Die Daten werden nachts automatisch in das Dashboard übertragen.*")

        print(f"✅ Formular erstellt!")
        print(f"🔗 Link: {form_url}")
        print(f"📄 Info gespeichert in: {health_path}")

    except Exception as e:
        print(f"❌ Fehler: {e}")

if __name__ == "__main__":
    setup_nutrition_tracking()
