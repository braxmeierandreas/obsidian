
if __name__ == "__main__":
    print("Starte Abruf von Trading 212 (Live)...")
    # Note: get_data now returns 4 values
    result = get_data()
    
    if result and result[0]:
        cash_data, positions_data, ticker_mapping, div_data = result
        content = create_markdown(cash_data, positions_data, ticker_mapping, div_data)
        
        # Sicherstellen, dass der Ordner existiert
        os.makedirs(os.path.dirname(OBSIDIAN_FILE), exist_ok=True)
        
        # Datei schreiben
        with open(OBSIDIAN_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"✅ Erfolgreich! Datei erstellt unter:\n{OBSIDIAN_FILE}")
    else:
        print("❌ Fehler: Keine Daten empfangen. Bitte prüfe die API-Zugangsdaten.")

