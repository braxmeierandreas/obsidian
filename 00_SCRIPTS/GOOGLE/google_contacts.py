import os
from google_auth import get_service

def fetch_contacts():
    try:
        service = get_service('people', 'v1')
        
        print("Lade ALLE Kontakt-Details...")
        # Wir fragen explizit alle nützlichen Felder ab
        fields = 'names,emailAddresses,phoneNumbers,organizations,addresses,birthdays,biographies,urls,relations'
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=1000,
            personFields=fields
        ).execute()
        
        connections = results.get('connections', [])
        
        if not connections:
            print("Keine Kontakte gefunden.")
            return

        # --- 1. TEIL: Kompakte Tabelle (Übersicht) ---
        md_content = "# 📒 Google Kontakte (Master-Liste)\n\n"
        md_content += f"*Automatisch synchronisiert am {os.popen('date /t').read().strip()}*\n\n"
        
        md_content += "## 📋 Schnelle Übersicht\n"
        md_content += "| Name | Firma | Telefon | E-Mail | Ort |\n"
        md_content += "| :--- | :--- | :--- | :--- | :--- |\n"

        # Wir sammeln die Details für den zweiten Teil
        details_list = []

        count = 0
        for person in connections:
            # --- Daten Extraktion ---
            names = person.get('names', [])
            name = names[0].get('displayName', 'Unbekannt') if names else "Unbekannt"
            
            phones = person.get('phoneNumbers', [])
            phone_str = phones[0].get('value', '') if phones else ""
            
            emails = person.get('emailAddresses', [])
            email_str = emails[0].get('value', '') if emails else ""
            
            orgs = person.get('organizations', [])
            org_str = orgs[0].get('name', '') if orgs else ""
            title_str = orgs[0].get('title', '') if orgs else "" # Jobtitel
            
            addrs = person.get('addresses', [])
            addr_str = addrs[0].get('formattedValue', '').replace('\n', ', ') if addrs else ""
            
            birthdays = person.get('birthdays', [])
            bday_str = ""
            if birthdays:
                b = birthdays[0].get('date', {})
                if 'year' in b:
                    bday_str = f"{b.get('day')}.{b.get('month')}.{b.get('year')}"
                else:
                    bday_str = f"{b.get('day')}.{b.get('month')}." # Ohne Jahr

            notes = person.get('biographies', [])
            note_str = notes[0].get('value', '') if notes else ""
            
            urls = person.get('urls', [])
            url_str = ", ".join([f"[{u.get('type', 'Link')}]({u.get('value')})" for u in urls])

            # Zur Tabelle hinzufügen (Gekürzt)
            md_content += f"| [[#👤 {name}]] | {org_str} | {phone_str} | {email_str} | {addr_str[:30]}... |\n"
            
            # Details speichern
            details_list.append({
                'name': name,
                'org': org_str,
                'title': title_str,
                'phones': [p.get('value') for p in phones],
                'emails': [e.get('value') for e in emails],
                'addresses': [a.get('formattedValue') for a in addrs],
                'bday': bday_str,
                'notes': note_str,
                'urls': urls
            })
            count += 1

        md_content += "\n---\n\n"
        md_content += "## 🗂️ Detaillierte Kartei\n"

        # --- 2. TEIL: Detaillierte Karten ---
        # Sortieren nach Name
        details_list.sort(key=lambda x: x['name'])

        for d in details_list:
            md_content += f"### 👤 {d['name']}\n"
            
            # Basis Info Block
            if d['org'] or d['title']:
                full_org = f"{d['title']} bei {d['org']}" if d['title'] and d['org'] else (d['org'] or d['title'])
                md_content += f"🏢 **Arbeit:** {full_org}\n\n"
            
            if d['bday']:
                md_content += f"🎂 **Geburtstag:** {d['bday']}\n\n"
            
            # Kontakt Block
            if d['phones']:
                md_content += "**📞 Telefon:**\n"
                for p in d['phones']: md_content += f"- {p}\n"
            
            if d['emails']:
                md_content += "**📧 E-Mail:**\n"
                for e in d['emails']: md_content += f"- {e}\n"
            
            if d['addresses']:
                md_content += "**🏠 Adresse:**\n"
                for a in d['addresses']:
                    clean_addr = a.replace('\n', ', ')
                    md_content += f"- {clean_addr}\n"
            
            if d['urls']:
                md_content += "**🔗 Links:**\n"
                for u in d['urls']: md_content += f"- {u.get('type', 'Web')}: {u.get('value')}\n"

            if d['notes']:
                md_content += "\n**📝 Notizen:**\n"
                clean_notes = d['notes'].replace('\n', '\n> ')
                md_content += f"> {clean_notes}\n"

            md_content += "\n---\n"

        # Speichern in Obsidian
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_path = os.path.join(base_dir, "01_Andreas", "03_PEOPLE", "ALLE_KONTAKTE.md")
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        print(f"✅ {count} Kontakte vollständig (mit Details) synchronisiert.")

    except Exception as e:
        print(f"❌ Fehler: {e}")

if __name__ == "__main__":
    fetch_contacts()
