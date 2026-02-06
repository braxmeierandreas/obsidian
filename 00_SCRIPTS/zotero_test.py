from pyzotero import zotero
import os

LIBRARY_ID = "12839350"
LIBRARY_TYPE = "user"
API_KEY = "C7tNAKFURGW8VPErBMD14Bx4"

zot = zotero.Zotero(LIBRARY_ID, LIBRARY_TYPE, API_KEY)

print(f"--- Abfrage für Library {LIBRARY_ID} gestartet ---\n")

items = zot.top(limit=10)

for item in items:
    data = item.get("data", {})
    title = data.get("title", "Kein Titel")
    item_type = data.get("itemType", "Unbekannt")
    date_added = data.get("dateAdded", "")

    print(f"Titel: {title}")
    print(f"Typ:   {item_type}")
    print(f"Hinzugefügt am: {date_added}")
    print("-" * 30)
