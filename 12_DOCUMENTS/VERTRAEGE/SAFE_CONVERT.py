import pymupdf4llm
import pathlib

print('--- Starte sichere Konvertierung ---')
files = list(pathlib.Path('.').rglob('*.pdf'))

for f in files:
    try:
        # Versuche Konvertierung
        md = pymupdf4llm.to_markdown(str(f))
        f.with_suffix('.md').write_text(md, encoding='utf-8')
        print(f'OK: {f.name}')
    except ValueError:
        # Fängt verschlüsselte Dateien ab (z.B. Consors.pdf)
        print(f'SKIP (Verschlüsselt/Passwort): {f.name}')
    except Exception as e:
        print(f'ERROR bei {f.name}: {e}')

print('--- Fertig ---')
