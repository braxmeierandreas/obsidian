# ✍️ 04_WRITING - Dein Redaktions-Büro

Hier schreiben wir Hausarbeiten, Blog-Posts, E-Mails und strukturieren komplexe Texte.

## 🛠 Verfügbare Power-Tools
1.  **Scribe Extension** (`/scribe`): Wenn installiert, für strukturierte Schreib-Workflows.
2.  **Critical Analysis** (`activate_skill`): Zum Überprüfen deiner Argumentation.
3.  **Google Docs** (`docs.create`, `docs.appendText`): Zum direkten Schreiben in deine Cloud.

## ⚡ Trigger & Beispiele

### 1. Hausarbeiten strukturieren
**Szenario:** Du hast eine grobe Idee für "BGM in KMUs", brauchst aber eine Gliederung.
> **Befehl:** `gemini "Erstelle eine detaillierte Gliederung für eine 15-seitige Hausarbeit zum Thema 'Herausforderungen von BGM in kleinen Unternehmen'. Integriere wissenschaftliche Methodik."`

### 2. Lektorat & Verbesserung
**Szenario:** Du hast einen Abschnitt geschrieben und willst ihn akademischer klingen lassen.
> **Befehl:** `gemini "Lies diesen Text: @{Entwurf.md}. Formuliere ihn um, sodass er akademischer klingt (Stil: sachlich, präzise), aber behalte die Kernaussage bei."`

### 3. Google Docs Integration
**Szenario:** Du willst den Entwurf direkt in Google Docs haben, um ihn mit Kommilitonen zu teilen.
> **Befehl:** `gemini "Erstelle ein neues Google Doc 'Hausarbeit BGM Entwurf' und füge die Gliederung ein, die wir gerade erstellt haben."`

---
**Pro-Tipp:** Nutze `activate_skill('peer-review')`, um Feedback wie von einem strengen Professor zu bekommen.
