### Anleitung: Konvertierung von Word (.docx), PDF (.pdf), Excel (.xlsx) und PowerPoint (.pptx) nach Markdown (.md)

Diese Anleitung beschreibt, wie du verschiedene Dateiformate in Markdown (`.md`)-Dateien umwandelst.

#### Voraussetzungen

Stelle sicher, dass die folgenden Tools auf deinem System installiert sind:

1.  **Pandoc**: Für die Konvertierung von Word-Dateien. Lade es hier herunter: [Pandoc Installation](https://pandoc.org/installing.html)
2.  **Python & pip**: Für die Konvertierung von PDF-, Excel- und PowerPoint-Dateien. Wenn nicht installiert, kannst du es über den Microsoft Store oder von [python.org](https://www.python.org/downloads/windows/) installieren. Pip wird normalerweise mit Python installiert.

#### Schritte zur Konvertierung

**Wichtig**: Ersetze `"C:\Dein\Pfad\Zu\Den\Dateien"` durch den tatsächlichen Pfad, in dem sich deine Dateien befinden.

---

##### 1. Word (.docx) nach Markdown (.md) konvertieren

**Zusammenfassung:** Wir verwenden `pandoc`, um `.docx`-Dateien in Markdown zu konvertieren.

```powershell
# 1. Navigiere zu dem Ordner mit deinen .docx-Dateien.
# Ersetze den Platzhalter durch deinen tatsächlichen Pfad.
cd "C:\Dein\Pfad\Zu\Den\Dateien"

# 2. Führe den folgenden Befehl aus, um alle .docx-Dateien im aktuellen Verzeichnis UND allen Unterordnern zu konvertieren.
# Für jede .docx-Datei wird eine entsprechende .md-Datei im selben Ordner erstellt.
Get-ChildItem -Filter *.docx -Recurse | ForEach-Object {
    pandoc $_.FullName -o (Join-Path $_.DirectoryName ($_.BaseName + ".md"))
}
```

---

##### 2. PDF (.pdf) nach Markdown (.md) konvertieren

**Zusammenfassung:** Wir verwenden das Python-Paket `pymupdf4llm`, um den Text aus PDF-Dateien zu extrahieren und in Markdown zu formatieren.

```powershell
# 1. Navigiere zu dem Ordner mit deinen .pdf-Dateien.
# Ersetze den Platzhalter durch deinen tatsächlichen Pfad.
cd "C:\Dein\Pfad\Zu\Den\Dateien"

# 2. Stelle sicher, dass pymupdf4llm installiert ist (falls noch nicht geschehen).
py -m pip install pymupdf4llm

# 3. Führe den folgenden Python-Einzeiler aus, um alle .pdf-Dateien im aktuellen Verzeichnis UND allen Unterordnern zu konvertieren.
# Für jede .pdf-Datei wird eine entsprechende .md-Datei im selben Ordner erstellt.
py -c "import pymupdf4llm; import pathlib; [f.with_suffix('.md').write_text(pymupdf4llm.to_markdown(str(f)), encoding='utf-8') for f in pathlib.Path('.').rglob('*.pdf')]"
```

---

##### 3. Excel (.xlsx) nach Markdown (.md) konvertieren

**Zusammenfassung:** Wir verwenden das Python-Paket `pandas`, um Tabellen aus Excel-Dateien zu lesen und als Markdown-Tabellen zu speichern.

```powershell
# 1. Navigiere zu dem Ordner mit deinen .xlsx-Dateien.
# Ersetze den Platzhalter durch deinen tatsächlichen Pfad.
cd "C:\Dein\Pfad\Zu\Den\Dateien"

# 2. Installiere die benötigten Pakete.
py -m pip install pandas openpyxl tabulate

# 3. Führe den folgenden Python-Einzeiler aus.
# Für jede .xlsx-Datei wird eine entsprechende .md-Datei im selben Ordner erstellt.
py -c "import pandas as pd; import pathlib; [f.with_suffix('.md').write_text(pd.read_excel(f).to_markdown(index=False), encoding='utf-8') for f in pathlib.Path('.').rglob('*.xlsx')]"
```

---

##### 4. PowerPoint (.pptx) nach Markdown (.md) konvertieren

**Zusammenfassung:** Wir verwenden ein kleines Python-Skript (benötigt `python-pptx`), um den Text aus den Folien zu extrahieren.

```powershell
# 1. Navigiere zu dem Ordner mit deinen .pptx-Dateien.
# Ersetze den Platzhalter durch deinen tatsächlichen Pfad.
cd "C:\Dein\Pfad\Zu\Den\Dateien"

# 2. Installiere das benötigte Paket.
py -m pip install python-pptx

# 3. Führe den folgenden Python-Einzeiler aus.
# Er iteriert rekursiv durch alle Ordner, extrahiert Titel und Text aus jeder Folie und speichert sie als .md-Datei.
py -c "
import pathlib
from pptx import Presentation

for f in pathlib.Path('.').rglob('*.pptx'):
    md_content = []
    try:
        prs = Presentation(f)
        for i, slide in enumerate(prs.slides):
            md_content.append(f'## Slide {i+1}\n')
            if slide.shapes.title and slide.shapes.title.text:
                 md_content.append(f'### {slide.shapes.title.text}\n')
            for shape in slide.shapes:
                if hasattr(shape, 'text') and shape.text and shape != slide.shapes.title:
                    md_content.append(f'{shape.text}\n')
            md_content.append('---\n')
        f.with_suffix('.md').write_text('\n'.join(md_content), encoding='utf-8')
        print(f'Converted: {f}')
    except Exception as e:
        print(f'Error converting {f}: {e}')
"
```



foreach ($file in Get-ChildItem -Filter *.md) {
    pandoc $file.FullName -o ($file.BaseName + ".docx")
}