from auth_helper import get_service

def list_recent_files():
    try:
        service = get_service('drive', 'v3')
        
        print("--- Letzte 20 bearbeitete Dateien ---")
        # Query for non-trashed files, ordered by modified time desc
        results = service.files().list(
            pageSize=20, 
            q="trashed = false",
            orderBy="modifiedTime desc",
            fields="nextPageToken, files(id, name, mimeType, modifiedTime)"
        ).execute()
        items = results.get('files', [])

        if not items:
            print('Keine Dateien gefunden.')
        else:
            for item in items:
                print(f"{item['name']} ({item['mimeType']})")
                print(f"  ID: {item['id']}")

    except Exception as e:
        print(f"Fehler: {e}")

def search_files(query_term):
    try:
        service = get_service('drive', 'v3')
        q = f"name contains '{query_term}' and trashed = false"
        
        print(f"\n--- Suche nach '{query_term}' ---")
        results = service.files().list(
            pageSize=10, 
            q=q,
            fields="files(id, name, mimeType)"
        ).execute()
        items = results.get('files', [])
        
        if not items:
            print(f"Nichts gefunden für '{query_term}'.")
        else:
            for item in items:
                print(f"* {item['name']}")

    except Exception as e:
        print(f"Fehler: {e}")

def analyze_storage():
    """Analyzes storage usage and exports top files to CSV."""
    import csv
    
    try:
        service = get_service('drive', 'v3')
        
        # 1. Get Storage Quota
        about = service.about().get(fields='storageQuota').execute()
        quota = about.get('storageQuota', {})
        usage_bytes = int(quota.get('usage', 0))
        limit_bytes = int(quota.get('limit', 0))
        
        usage_gb = usage_bytes / (1024**3)
        limit_gb = limit_bytes / (1024**3)
        
        print(f"\n=== Google Drive Speicheranalyse ===")
        print(f"Genutzt: {usage_gb:.2f} GB von {limit_gb:.2f} GB ({(usage_bytes/limit_bytes)*100:.1f}%)")
        
        # 2. Find Largest Files
        print("\nSuche die größten Dateien (Top 10)...")
        # Query: Not trashed
        # Order by: quotaBytesUsed desc (correct field name for sorting by size)
        results = service.files().list(
            pageSize=10,
            q="trashed = false",
            orderBy="quotaBytesUsed desc",
            fields="files(id, name, quotaBytesUsed, mimeType, webViewLink)"
        ).execute()
        
        files = results.get('files', [])
        
        print(f"{'Größe (MB)':<12} | {'Name':<40} | {'Typ'}")
        print("-" * 80)
        
        csv_data = []
        
        for f in files:
            size_bytes = int(f.get('quotaBytesUsed', 0))
            size_mb = size_bytes / (1024**2)
            name = f.get('name', 'Unbekannt')[:38] # Truncate for display
            mime = f.get('mimeType', '').split('/')[-1]
            
            print(f"{size_mb:<12.2f} | {name:<40} | {mime}")
            
            csv_data.append([f.get('name'), size_mb, f.get('mimeType'), f.get('webViewLink')])
            
        # 3. Export to CSV
        csv_filename = 'drive_analysis.csv'
        with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Dateiname', 'Größe (MB)', 'Typ', 'Link'])
            writer.writerows(csv_data)
            
        print(f"\nDetailanalyse exportiert nach: {csv_filename}")

    except Exception as e:
        print(f"Fehler bei der Analyse: {e}")

def analyze_folders():
    """Aggregates file sizes by their parent folders to find the largest directories."""
    try:
        service = get_service('drive', 'v3')
        print("\n--- Analysiere Ordnerstrukturen (kann kurz dauern) ---")
        
        # 1. Get all folders (to resolve names)
        folders = {}
        page_token = None
        while True:
            results = service.files().list(
                q="mimeType = 'application/vnd.google-apps.folder' and trashed = false",
                fields="nextPageToken, files(id, name)",
                pageToken=page_token
            ).execute()
            for f in results.get('files', []):
                folders[f['id']] = f['name']
            page_token = results.get('nextPageToken')
            if not page_token: break
            
        # 2. Get all files with their sizes and parents
        folder_sizes = {} # folder_id -> total_size
        page_token = None
        file_count = 0
        
        while True:
            results = service.files().list(
                q="mimeType != 'application/vnd.google-apps.folder' and trashed = false",
                fields="nextPageToken, files(id, quotaBytesUsed, parents)",
                pageToken=page_token
            ).execute()
            
            for f in results.get('files', []):
                size = int(f.get('quotaBytesUsed', 0))
                parents = f.get('parents', [])
                for p in parents:
                    folder_sizes[p] = folder_sizes.get(p, 0) + size
                file_count += 1
            
            page_token = results.get('nextPageToken')
            if not page_token: break
            
        # 3. Sort and Display
        sorted_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)
        
        print(f"\nTop 10 Ordner nach Speicherverbrauch (direkt enthaltene Dateien):")
        print(f"{'Größe (MB)':<12} | {'Ordnername'}")
        print("-" * 40)
        
        for folder_id, size in sorted_folders[:10]:
            name = folders.get(folder_id, f"Unbekannt ({folder_id})")
            print(f"{size / (1024**2):<12.2f} | {name}")
            
    except Exception as e:
        print(f"Fehler bei der Ordneranalyse: {e}")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'analyze':
            analyze_storage()
        elif sys.argv[1] == 'folders':
            analyze_folders()
    else:
        print("1. Letzte Dateien anzeigen")
        print("2. Suchen")
        print("3. Speicheranalyse (Top 10 Dateien)")
        print("4. Ordneranalyse (Größte Ordner)")
        choice = input("Wähle eine Option (1-4): ")
        
        if choice == '1':
            list_recent_files()
        elif choice == '2':
            q = input("Suchbegriff: ")
            search_files(q)
        elif choice == '3':
            analyze_storage()
        elif choice == '4':
            analyze_folders()
