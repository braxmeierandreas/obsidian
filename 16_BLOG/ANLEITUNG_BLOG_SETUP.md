# 🚀 1:1 Anleitung: Dein Obsidian Blog mit Hugo (Windows)

Diese Anleitung basiert auf dem NetworkChuck Tutorial und ist speziell für dein System (`win32`) und deinen Pfad (`C:\Users\braxm\Meine Ablage\Obsidian`) angepasst.

## Schritt 1: Tools installieren (Einmalig)
Du brauchst drei Programme auf deinem Windows-Rechner:
1. **Git:** [Hier herunterladen](https://git-scm.com/download/win) (Standard-Einstellungen beim Installieren lassen).
2. **Go:** [Hier herunterladen](https://go.dev/dl/) (Wichtig für Hugo).
3. **Hugo:** 
   - Am einfachsten über den Terminal (PowerShell als Admin öffnen):
   - `winget install Hugo.Hugo.Extended` (Die "Extended" Version ist besser für viele Themes).

**Prüfen:** Öffne ein Terminal und tippe `hugo version`. Wenn eine Versionsnummer kommt, bist du bereit.

---

## Schritt 2: Den Blog-Ordner in Obsidian vorbereiten
1. Du hast bereits den Ordner `16_BLOG`.
2. Erstelle darin einen Unterordner namens `posts`. Hier schreibst du deine Blog-Beiträge als `.md` Dateien.
   - *Pfad:* `C:\Users\braxm\Meine Ablage\Obsidian\16_BLOG\posts`

---

## Schritt 3: Die Hugo-Webseite erstellen
1. Öffne ein Terminal im Verzeichnis `16_BLOG`.
2. Führe aus:
   ```powershell
   hugo new site my_blog
   cd my_blog
   git init
   git submodule add -f https://github.com/panr/hugo-theme-terminal.git themes/terminal
   ```
3. Kopiere den Inhalt der `hugo.toml` aus dem `NetworkChuck_Tutorial.md` in die Datei `my_blog/hugo.toml`.

---

## Schritt 4: Automatisierung (Der "Magische" Teil)
Damit deine Obsidian-Notizen automatisch zu Blog-Posts werden, nutzen wir zwei Skripte, die ich dir vorbereitet habe.

### 4.1 Bild-Skript (`images.py`)
Dieses Skript sorgt dafür, dass Obsidian-Bilder (`[[bild.png]]`) in das Hugo-Format umgewandelt und kopiert werden.
**Ich habe es bereits in `16_BLOG/images.py` für dich erstellt.**

### 4.2 Sync-Skript (`deploy_blog.ps1`)
Erstelle eine Datei `16_BLOG/deploy_blog.ps1` mit folgendem Inhalt (angepasst auf deine Pfade):
```powershell
$sourcePath = "C:\Users\braxm\Meine Ablage\Obsidian\16_BLOG\posts"
$destinationPath = "C:\Users\braxm\Meine Ablage\Obsidian\16_BLOG\my_blog\content\posts"

# 1. Sync Posts
robocopy $sourcePath $destinationPath /mir

# 2. Bilder fixen
python ..\images.py

# 3. Hugo Vorschau starten
cd my_blog
hugo server -D
```

---

## Schritt 5: Dein erster Post
1. Erstelle eine Datei `C:\Users\braxm\Meine Ablage\Obsidian\16_BLOG\posts\hallo-welt.md`.
2. **Wichtig:** Jeder Post muss diesen Kopf (Frontmatter) haben:
   ```markdown
   ---
   title: "Mein erster Blogpost"
   date: 2026-01-21
   draft: false
   ---
   Hier steht mein Text!
   ```

## Schritt 6: Blog anschauen
Führe das PowerShell-Skript `deploy_blog.ps1` aus. Dein Blog ist dann unter `http://localhost:1313` im Browser erreichbar.

---

### Was ist mit GitHub?
Sobald dein lokaler Blog läuft, können wir im nächsten Schritt die GitHub-Verbindung einrichten, damit er weltweit erreichbar ist. Sag mir einfach Bescheid!
