# 🔄 Massen-Konverter (Batch Processing)

Hier sind Befehle, die **automatisch alle Dateien in einem Ordner** umwandeln.
Du musst die Dateinamen **nicht** einzeln anpassen. Die Skripte nehmen einfach alles, was sie finden.

Da du auf **Windows** bist, sind diese Befehle für die **PowerShell** optimiert.

---

## 🎵 Audio Massen-Konvertierung

### Alle `WAV` zu `MP3` komprimieren
Macht aus jedem `.wav` Lied im Ordner eine MP3-Datei.
```powershell
Get-ChildItem *.wav | ForEach-Object { ffmpeg -i $_.Name -codec:a libmp3lame -qscale:a 2 ($_.BaseName + ".mp3") }
```

### Alle `M4A` (Apple) zu `MP3` umwandeln
```powershell
Get-ChildItem *.m4a | ForEach-Object { ffmpeg -i $_.Name -codec:a libmp3lame -qscale:a 2 ($_.BaseName + ".mp3") }
```

### Alle `MP3` zu `WAV` (zurück zum Rohformat)
```powershell
Get-ChildItem *.mp3 | ForEach-Object { ffmpeg -i $_.Name ($_.BaseName + ".wav") }
```

---

## 🎥 Video Massen-Konvertierung

### Audio aus allen `MP4`-Videos ziehen (-> `MP3`)
Extrahiert den Ton aus jedem Video im Ordner.
```powershell
Get-ChildItem *.mp4 | ForEach-Object { ffmpeg -i $_.Name -q:a 0 -map a ($_.BaseName + ".mp3") }
```

### Alle `MKV` Videos zu `MP4` umpacken (schnell)
Ändert nur den "Container", ohne Qualitätsverlust.
```powershell
Get-ChildItem *.mkv | ForEach-Object { ffmpeg -i $_.Name -codec copy ($_.BaseName + ".mp4") }
```

### Alle `MOV` (iPhone Videos) zu `MP4`
```powershell
Get-ChildItem *.mov | ForEach-Object { ffmpeg -i $_.Name -vcodec h264 -acodec mp2 ($_.BaseName + ".mp4") }
```

---

## 🛠️ Anleitung: Wie nutze ich das?

1.  Öffne den Ordner mit deinen Dateien im Explorer.
2.  Klicke mit **Rechtsklick** in einen leeren Bereich und wähle **"In Terminal öffnen"** (oder halte Shift + Rechtsklick -> "PowerShell-Fenster hier öffnen").
3.  Kopiere einen der Code-Blöcke von oben.
4.  Füge ihn in das blaue Fenster ein (Rechtsklick fügt oft automatisch ein) und drücke **Enter**.

⚠️ **Wichtig:** Du brauchst **FFmpeg** installiert, damit das funktioniert (siehe vorherige Anleitung).
