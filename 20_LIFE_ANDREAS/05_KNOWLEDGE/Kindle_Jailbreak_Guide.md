# 📖 Kindle Paperwhite Jailbreak Guide (Adbreak Method)

> **Datum:** 22.01.2026  
> **Status:** Experimentell / Community-basiert  
> **Ziel:** Volle Kontrolle über die Hardware, KOReader, Werbefreiheit.

---

## ⚠️ Disclaimer
**Durchführung auf eigene Gefahr.** Ein Jailbreak kann zum Garantieverlust führen oder das Gerät unbrauchbar machen ("Bricking"). Achte penibel auf die Firmware-Version.

---

## 🔍 Vorbereitung & Checkliste

1. **Firmware prüfen:** `Einstellungen -> Geräteoptionen -> Geräteinfo`. 
   - Kompatibel mit den meisten Versionen bis 5.16.x / 5.17.x (Adbreak Exploit).
2. **Hardware-Check:** Verwende ein hochwertiges Datenkabel (das Originalkabel ist meist am sichersten).
3. **Akku:** Mindestens 80% Ladung.

---

## 🛠 Schritt-für-Schritt Anleitung

### Schritt 1: Update-Schutz (Speicher-Inflation)
Um zu verhindern, dass der Kindle während des Jailbreaks ein automatisches Update zieht:
- Verbinde den Kindle mit dem PC.
- Lade "Filler Files" oder kopiere große Dummy-Dateien auf den Kindle, bis nur noch ca. **100-200 MB frei** sind.
- Falls eine Datei namens `update.bin` im Hauptverzeichnis existiert: **Sofort löschen.**

### Schritt 2: Adbreak-Einstieg (Werbung nutzen)
Der Exploit nutzt das Werbesystem von Amazon.
- **Werbung aktivieren:** Falls deaktiviert, über das Amazon-Konto ("Inhalte und Geräte") reaktivieren.
- **Regionale Hürden:** Falls keine Werbung geladen wird, kurzzeitig auf einen **US-Account** mit US-Adresse ummelden.
- Sobald Werbung erscheint: **Flugmodus einschalten.**

### Schritt 3: Exploit installieren
- Kindle an PC anschließen. Versteckte Dateien sichtbar machen.
- Navigiere zu `system/assets/`. (Backup dieses Ordners auf dem PC erstellen!).
- Lade das **Adbreak-Paket** vom [Kindle Modding Wiki](https://kindlemodding.com) herunter.
- Dateien im `assets`-Ordner auf dem Kindle durch die Adbreak-Dateien ersetzen.
- **Windows:** Führe die `adbreak.bat` auf dem PC aus.
- Kindle sicher auswerfen und eine Werbung auf dem Gerät antippen. Der Jailbreak-Prozess sollte starten.

### Schritt 4: Persistenz (Hotfix & KUAL)
Damit der Jailbreak nach Updates nicht verschwindet:
1. **Jailbreak Hotfix:** `.bin`-Datei in das Hauptverzeichnis kopieren.
2. Am Kindle: `Einstellungen -> Geräteoptionen -> Kindle aktualisieren` wählen.
3. **MRPI & KUAL:** Ordner `extensions` und `mrpackages` auf den Kindle kopieren.
4. Suchleiste am Kindle: `;log mrpi` eingeben, um die Pakete final zu installieren.

### Schritt 5: Updates endgültig blockieren
- Öffne **KUAL** auf dem Kindle.
- Wähle die Erweiterung **"Rename OTA Binaries"** oder **"Block Updates"**.
- Erst danach ist es sicher, den Flugmodus dauerhaft zu deaktivieren.

---

## 🚀 Empfohlene Apps & Erweiterungen

| App | Nutzen |
| :--- | :--- |
| **KOReader** | Ersetzt die Lese-UI. Unterstützt ePub, PDF-Reflow und bietet bessere Akkulaufzeit. |
| **Kindle Forge** | Der "App Store" für Modding-Erweiterungen. |
| **Custom Screen Saver** | Eigene Bilder als Sperrbildschirm (vorausgesetzt Ads wurden via Script entfernt). |
| **KWordle / Games** | Kleine Zeitvertreiber für zwischendurch. |

---

## 🔗 Wichtige Ressourcen
- **Zentrale Anlaufstelle:** [Kindle Modding Wiki](https://kindlemodding.com)
- **Entwickler-Forum:** [MobileRead - Kindle Developer Corner](https://www.mobileread.com/forums/forumdisplay.php?f=150)
- **Discord:** Kindle Tweaks / Kindle Modding Community.

---
*Notiz von Andreas: Nach dem Jailbreak die Filler-Files aus Schritt 1 wieder löschen, um Platz für Bücher zu schaffen!*
