import argparse
from google_auth import get_service

def create_doc(title="Unbenanntes Dokument"):
    try:
        service = get_service('docs', 'v1')
        body = {'title': title}
        doc = service.documents().create(body=body).execute()
        print(f"✅ Google Doc erstellt: {doc.get('title')} (ID: {doc.get('documentId')})")
        print(f"🔗 Link: https://docs.google.com/document/d/{doc.get('documentId')}")
        return doc
    except Exception as e:
        print(f"❌ Fehler bei Doc: {e}")

def create_sheet(title="Unbenannte Tabelle"):
    try:
        service = get_service('sheets', 'v4')
        body = {'properties': {'title': title}}
        sheet = service.spreadsheets().create(body=body).execute()
        print(f"✅ Google Sheet erstellt: {sheet.get('properties').get('title')} (ID: {sheet.get('spreadsheetId')})")
        print(f"🔗 Link: {sheet.get('spreadsheetUrl')}")
        return sheet
    except Exception as e:
        print(f"❌ Fehler bei Sheet: {e}")

def create_slide(title="Unbenannte Präsentation"):
    try:
        service = get_service('slides', 'v1')
        body = {'title': title}
        slide = service.presentations().create(body=body).execute()
        print(f"✅ Google Slide erstellt: {slide.get('title')} (ID: {slide.get('presentationId')})")
        print(f"🔗 Link: https://docs.google.com/presentation/d/{slide.get('presentationId')}")
        return slide
    except Exception as e:
        print(f"❌ Fehler bei Slide: {e}")

def create_form(title="Unbenanntes Formular"):
    try:
        service = get_service('forms', 'v1')
        body = {"info": {"title": title}}
        form = service.forms().create(body=body).execute()
        print(f"✅ Google Form erstellt: {form.get('info').get('title')} (ID: {form.get('formId')})")
        print(f"🔗 Link: https://docs.google.com/forms/d/{form.get('formId')}")
        return form
    except Exception as e:
        print(f"❌ Fehler bei Form: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Erstelle Google Dateien (Docs, Sheets, Slides, Forms).')
    parser.add_argument('--type', type=str, choices=['doc', 'sheet', 'slide', 'form'], help='Typ der Datei')
    parser.add_argument('--title', type=str, default="Neu erstellt von Gemini", help='Titel der Datei')
    
    args = parser.parse_args()

    if args.type == 'doc':
        create_doc(args.title)
    elif args.type == 'sheet':
        create_sheet(args.title)
    elif args.type == 'slide':
        create_slide(args.title)
    elif args.type == 'form':
        create_form(args.title)
    else:
        print("ℹ️ Bitte nutze Argumente: --type [doc|sheet|slide|form] --title 'Mein Titel'")
        print("Beispiel-Testlauf wird gestartet (Erstellt ein Test-Doc)...")
        create_doc("Gemini Test Dokument")
