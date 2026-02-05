# MD Verkleinerer - Anleitung

Dieser Ordner hilft dir dabei, sehr lange Markdown-Dateien automatisch in kleinere Teile aufzusplitten (ideal für Programme, die bei ca. 2000 Zeilen abschneiden).

## So benutzt du es:

1. Kopiere deine lange `.md` Datei einfach **direkt in diesen Ordner** (`verkleiner/`).
2. Führe das Skript aus. Du kannst mich (Gemini) bitten: *"Gemini, lass den Verkleinerer laufen"* oder du nutzt die Konsole im Ordner:
   ```powershell
   python split_md.py
   ```
3. **Ergebnis:**
   - Ein neuer **Unterordner** mit dem Namen deiner Datei wird erstellt. Darin liegen die durchnummerierten Einzelteile (z.B. `01_Einleitung.md`).
   - Deine **Originaldatei** wird automatisch in den Ordner `backup/` verschoben, damit der Hauptordner sauber bleibt.

## Logik:
Das Skript versucht intelligent an Überschriften (`#`, `##`, `###`) zu trennen, damit die Texte logisch zusammenbleiben und nicht mitten im Satz abgeschnitten werden.
