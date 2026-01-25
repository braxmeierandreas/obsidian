import os
import re
import shutil

# ANPASSUNG FÜR ANDREAS BRAXMEIER
# Relative Pfade basierend auf Speicherort des Skripts (16_BLOG)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OBSIDIAN_ROOT = os.path.dirname(SCRIPT_DIR) # Geht eine Ebene hoch zu "Obsidian"

posts_dir = os.path.join(SCRIPT_DIR, "my_blog", "content", "posts")
attachments_dir = os.path.join(OBSIDIAN_ROOT, "02_JOURNAL", "07_ATTACHMENTS") 
static_images_dir = os.path.join(SCRIPT_DIR, "my_blog", "static", "images")

# Sicherstellen, dass der Zielordner existiert
if not os.path.exists(static_images_dir):
    os.makedirs(static_images_dir)

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Step 2: Find all image links in the format [[image.png]]
        images = re.findall(r'\[\[([^]]*\.(?:png|jpg|jpeg|gif|webp))\]\]', content)
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown-compatible link with %20 replacing spaces
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)
            else:
                print(f"Warnung: Bild nicht gefunden: {image_source}")

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown Dateien wurden verarbeitet und Bilder kopiert.")
