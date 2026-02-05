# 🦞 AWS Clawdbot Setup & Cheat Sheet (Januar 2026)

## 📌 Kern-Konfiguration

- **Provider:** Groq Cloud (via OpenAI-Schnittstelle)
    
- **Base URL:** `https://api.groq.com/openai/v1`
    
- **Primary Model:** `openai/llama-3.3-70b-versatile`
    
- **Interface:** Telegram (@AndreasCLAW_bot)
    

## 🛠️ Wichtige CLI-Befehle

### Dienst-Steuerung

| **Aktion**        | **Befehl**                       |
| ----------------- | -------------------------------- |
| **Neustart**      | `clawdbot daemon restart`        |
| **Status prüfen** | `clawdbot daemon status`         |
| **Start / Stopp** | `clawdbot daemon start` / `stop` |
| **Echtzeit-Logs** | `clawdbot daemon logs`           |

### Konfiguration

- **Config bearbeiten:** `nano ~/.clawdbot/clawdbot.json`
    
- **Änderungen anwenden:** `clawdbot config apply`
    
- **Credentials prüfen:** `cat ~/.clawdbot/.env`
    

## 📂 Dateipfade auf AWS

- **Hauptkonfiguration:** `/home/ubuntu/.clawdbot/clawdbot.json`
    
- **API Keys / Secrets:** `/home/ubuntu/.clawdbot/.env`
    
- **Workspace:** `~/clawd`
    
- **Sessions/Gedächtnis:** `~/.clawdbot/agents/main/sessions`
    

## 💡 Troubleshooting-Routine

Falls der Telegram-Bot nicht antwortet:

1. SSH-Verbindung zur AWS Instanz aufbauen.
    
2. `clawdbot daemon status` prüfen.
    
3. Falls "active", aber keine Antwort: `clawdbot daemon logs` prüfen (oft Rate-Limits bei Groq).
    
4. `clawdbot doctor --fix` ausführen, um Berechtigungen zu reparieren.
    

## ⚙️ Backup-Strategie (für Obsidian)

Kopiere regelmäßig den Inhalt der `clawdbot.json` in dieses Dokument, um bei einem Server-Reset (Full Reset) die Struktur der Hooks und Fallbacks sofort wiederherstellen zu können.