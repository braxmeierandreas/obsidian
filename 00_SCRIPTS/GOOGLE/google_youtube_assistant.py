import os
from google_auth import get_service

def search_youtube(query):
    try:
        service = get_service('youtube', 'v3')
        
        request = service.search().list(
            q=query,
            part='snippet',
            maxResults=3,
            type='video'
        )
        response = request.execute()
        
        results = []
        for item in response.get('items', []):
            title = item['snippet']['title']
            video_id = item['id']['videoId']
            url = f"https://www.youtube.com/watch?v={video_id}"
            results.append(f"- [{title}]({url})")
        return results
    except Exception as e:
        return [f"Fehler bei Suche '{query}': {e}"]

def update_learning_resources():
    topics = {
        "🇪🇸 Spanisch A1": "Spanish A1 learning for beginners",
        "🔬 Wissenschaftstheorie": "Wissenschaftstheorie Grundlagen",
        "🌍 Global Health": "Global Health current challenges 2025"
    }
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(base_dir, "01_Andreas", "02_DAILY", "YOUTUBE_LEARNING.md")
    
    md_content = "# 📺 YouTube Lern-Ressourcen\n\n"
    md_content += f"*Zuletzt aktualisiert: {os.popen('date /t').read().strip()}*\n\n"
    
    for display_name, query in topics.items():
        print(f"Suche YouTube Videos für: {display_name}...")
        videos = search_youtube(query)
        md_content += f"## {display_name}\n"
        md_content += "\n".join(videos) + "\n\n"
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    
    print(f"✅ Lern-Ressourcen aktualisiert in: {output_path}")

if __name__ == "__main__":
    update_learning_resources()
