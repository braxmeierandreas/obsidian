# Personal Intelligence & Homelab – Masterplan

> Ziel: Ein lokales, sicheres, erweiterbares KI‑, Wissens‑ und Automationssystem, das Technik, Lernen und persönliche Identität vereint.

---

## 1. Grundprinzipien

- Local‑first
- Docker‑first
- Markdown‑first
- Security‑by‑default
- Identitätsbewusst

---

## 2. Wissens‑ & Schreibsystem

### 2.1 Journal / World of Text

```
/journal
  /daily
  /themes
```

Daily Template:

```md
# Datum

## Zustand
- Energie:
- Fokus:
- Emotion:

## Gedankenstrom

## Erkenntnisse

## Nächste Schritte
```

---

## 3. Talos – persönlicher Wissenskern

```
/talos
 ├─ security
 ├─ intelligence
 ├─ automation
 ├─ personal
 │   ├─ skills.md
 │   ├─ studies.md
 │   ├─ profile.md
 │   └─ evolution.md
```

---

## 4. Sepia (Arbeitsprinzip)

1. Quelle lesen  
2. Kernaussagen extrahieren  
3. Verdichten  
4. Eigene Interpretation  
5. In Talos einordnen  

---

## 5. Bücher scrapen & komprimieren

```
Text / Buch
 → Import / Scraper
 → Chunking
 → Kompression (≤ 2000 Lines)
 → MD/TXT
 → Gemini CLI
```

---

## 6. Homelab & Infrastruktur

### 6.1 Heimserver

- Hauptrechner = KI‑Server
- GPU mit hohem VRAM
- Docker + Docker Compose

```
/server
 ├─ docker-compose.yml
 ├─ .env
 ├─ /services
 └─ /data
```

### 6.2 Netzwerk

- Ethernet‑Anschluss
- Always‑on VPN
- Always DNS (Cloudflare)
- Keine offenen Ports

### 6.3 Raspberry Pi

- DNS
- Monitoring
- Edge‑Services

---

## 7. Automation (n8n)

- Journal versionieren
- Talos indexieren
- Scraper‑Outputs verarbeiten

---

## 8. Security & Access

### Cloudflare Zero Trust
### TwinGate (Zero Trust Learning)

---

## 9. KI & Intelligence

### 9.1 Lokale LLMs
### 9.2 MCP – Multi‑Context Protocol
### 9.3 Voice Assistant (eigene Stimme, lokal)

---

## 10. Terminal‑Wissen

```
/terminal
 ├─ docker.md
 ├─ network.md
 ├─ vpn.md
 └─ system.md
```

---

## 11. Obsidian

Zentrale Wissensoberfläche für:
- Journal
- Talos
- Terminal‑Commands

---

## 12. Physische & mentale Skills

### Lockpicking
- nur eigene Schlösser
- Lern‑ & Sicherheitsverständnis

### Jonglieren
- Fokus
- Koordination
- Flow

---

## 13. Hardware‑Security – Flipper Zero

- RFID / NFC
- Sub‑GHz
- IR
- GPIO

Nur an eigenen Systemen. Dokumentation in Talos.

---

## 14. Notizen an mich selbst

- Mehr schreiben
- Schreiben = Denken
- Unfertig ist erlaubt

---

## 15. Second Brain

**Buch:** Building a Second Brain  
**Autor:** Tiago Forte

CODE‑Prinzip:
- Capture
- Organize
- Distill
- Express

---

## 16. Eigener Blog (automatisiert)

Inspiration: Network Chuck

```
Journal / Talos
 → n8n
 → Static Site Generator
 → Veröffentlichung
```

Grundsatz:
> Inhalte entstehen zuerst für mich.

---

> Diese Datei ist ein lebendes System. Änderungen sind erwünscht.
