# 🛡️ Haushalts-Held Backup Zentrale

Dieses Verzeichnis steuert dein wöchentliches Backup. 
**Starte einfach die Datei `START_BACKUP.bat`, um den Prozess zu beginnen.**

---

## 📂 Was wird automatisch gesichert?
Das Skript kopiert folgende lokale Daten in einen Ordner auf deinem Desktop (`BackUp - KW XX JJJJ`):

### 1. Dein "Gehirn" (Obsidian)
- **Quelle:** `%USERPROFILE%\obsidian`
- **Inhalt:** Alle Notizen, Anhänge, PDFs, Canvas-Dateien.
- **Exkludiert:** Mülleimer (`.trash`), Git-Verlauf (`.git`), Cache.

### 2. Wichtige Dokumente
- **Quelle:** `%USERPROFILE%\Documents`
- **Inhalt:** Alle Dateien in deinem Windows-Dokumente Ordner.

### 3. Fotos & Bilder
- **Quelle:** `%USERPROFILE%\Pictures`
- **Inhalt:** Alle Bilder, Screenshots und gespeicherten Fotos.

### 4. Entwickler-Schlüssel & Einstellungen
- **SSH-Keys:** `%USERPROFILE%\.ssh` (Deine Zugänge zu GitHub/Servern).
- **VS Code:** `%APPDATA%\Code\User` (Deine Settings, Snippets & Keybindings).

### 5. Browser Daten
- **Chrome:** Kopiert die `Bookmarks` Datei (Lesezeichen).

### 6. Downloads (Archiv)
- **Quelle:** `%USERPROFILE%\Downloads`
- **Zweck:** Dient als Archiv, falls du vergessen hast, etwas aufzuräumen.

---

## 📝 Deine Checkliste (Manuelle Schritte)
Das Skript wird dich interaktiv an diese Punkte erinnern:

1.  **Samsung Handy (S24 Ultra):**
    - Schließe das Handy an.
    - Nutze **Samsung Smart Switch** für ein Voll-Backup ODER kopiere den Ordner `DCIM` (Kamera) manuell in den Backup-Ordner.
2.  **Google Cloud (Drive/Fotos):**
    - Diese Daten liegen in der Cloud.
    - **Empfehlung:** Mache alle 3-6 Monate einen [Google Takeout](https://takeout.google.com/), um diese Daten physisch herunterzuladen.
3.  **Windows System:**
    - Das Skript versucht, einen Wiederherstellungspunkt zu setzen.
4.  **Obsidian schließen:**
    - Wichtig, damit keine Schreibkonflikte entstehen.

---

## ⚙️ Technische Infos
- **Technologie:** Das Skript nutzt `robocopy` (Robust File Copy).
- **Modus:** Es ist so eingestellt, dass es bei Fehlern kurz wartet und es erneut versucht (`/R:1 /W:1`).
- **Zielort:** Immer dein Desktop. Von dort aus kannst du den Ordner auf eine **externe Festplatte** verschieben (empfohlen!).
