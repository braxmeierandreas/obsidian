# 🎵 Wildes Format-Chaos & Medien-Alchemie 🎥

Hier ist das angeforderte Sammelsurium an Konvertierungs-Befehlen. Die meisten nutzen **FFmpeg**, das Schweizer Taschenmesser für Multimedia.

## 🛠️ Die Klassiker (Langweilig aber nützlich)

### Video zu Audio (MP4 -> MP3)
Schnell nur den Ton extrahieren:
```bash
ffmpeg -i input.mp4 -q:a 0 -map a output.mp3
```

### WAV zu MP3 (Platz sparen)
Komprimieren für den MP3-Player von 2005:
```bash
ffmpeg -i recording.wav -codec:a libmp3lame -qscale:a 2 song.mp3
```

### M4A zu WAV (Für die Audiophilen)
Zurück zur unkomprimierten Wahrheit:
```bash
ffmpeg -i track.m4a output.wav
```

---

## 🌪️ "Wild gemischt" & Esoterische Konvertierungen

### MP3 zu MP4 (Das "Schwarze Loch" Video)
Macht aus einer Audiodatei ein Video mit schwarzem Bild (praktisch für YouTube-Uploads):
```bash
ffmpeg -f lavfi -i color=c=black:s=1280x720:r=5 -i input.mp3 -crf 0 -c:a copy -shortest video_aus_audio.mp4
```

### MP4 zu GIF (Das Internet-Meme-Format)
Verwandle die ersten 5 Sekunden eines Videos in ein GIF:
```bash
ffmpeg -i video.mp4 -ss 0 -t 5 -vf "fps=10,scale=320:-1:flags=lanczos" -c:v gif output.gif
```

### Video in eine Reihe von Bildern zerlegen (MP4 -> JPG)
Jedes Frame ein Bild. Festplatte voll in 3... 2... 1...
```bash
ffmpeg -i movie.mp4 frame_%04d.jpg
```

### Bilder wieder zu Video zusammenkleben (JPG -> MP4)
Rückwärtsgang!
```bash
ffmpeg -framerate 24 -i frame_%04d.jpg -c:v libx264 -pix_fmt yuv420p slideshow.mp4
```

### Das "Alles in FLAC" Manöver (M4A -> FLAC)
Apple-Audio in Free Lossless Audio Codec:
```bash
ffmpeg -i podcast.m4a -c:a flac podcast.flac
```

### Video-Container Swap (MKV -> MP4)
Ohne Neukodierung, einfach nur umpacken (super schnell):
```bash
ffmpeg -i film.mkv -codec copy film.mp4
```

### Der "Zerstörer" (Bitrate in den Keller)
Mach dein HD-Video zu Pixel-Matsche (Retro-Style?):
```bash
ffmpeg -i 4k_video.mp4 -b:v 64k -b:a 32k pixel_art.mp4
```

### Audio-Geschwindigkeit verdoppeln (Nightcore light?)
```bash
ffmpeg -i slow_song.mp3 -filter:a "atempo=2.0" fast_song.mp3
```

## 📜 Installation (Falls FFmpeg fehlt)

**Windows (via Winget):**
```powershell
winget install Gyan.FFmpeg
```

**Mac (via Homebrew):**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt install ffmpeg
```
