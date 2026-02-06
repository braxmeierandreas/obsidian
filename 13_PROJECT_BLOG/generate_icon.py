from PIL import Image, ImageDraw

# Bildgröße
size = (512, 512)
# Farben (HFU Blau / Indigo)
bg_color = "#4B0082" 
text_color = "white"
dot_color = "#00FFCC"

# Bild erstellen
img = Image.new('RGB', size, color=bg_color)
d = ImageDraw.Draw(img)

# Wir malen ein minimalistisches "A" (als Dreieck/Winkel)
# Koordinaten für 512x512
d.line([(150, 350), (256, 150), (362, 350)], fill=text_color, width=40)
d.line([(200, 280), (312, 280)], fill=text_color, width=40)

# Der "Node" Punkt
r = 30
d.ellipse([(256-r, 150-r), (256+r, 150+r)], fill=dot_color)

import os

# Relative Pfade
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(SCRIPT_DIR, "my_blog", "static")

# Sicherstellen, dass der Zielordner existiert
os.makedirs(STATIC_DIR, exist_ok=True)

path_png = os.path.join(STATIC_DIR, "favicon.png")
path_ico = os.path.join(STATIC_DIR, "favicon.ico")
path_apple = os.path.join(STATIC_DIR, "apple-touch-icon.png")

img.save(path_png)
img.save(path_apple)
# ICO speichern (enthält oft mehrere Größen, hier einfachheitshalber das große runterskaliert)
img.resize((32,32)).save(path_ico)

print("Icons erfolgreich generiert!")
