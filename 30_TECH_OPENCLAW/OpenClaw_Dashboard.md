---
created: 2026-02-05
tags:
  - tool
  - ai
  - agent
  - homelab
  - software
status: Setup Required
website: https://openclaw.ai
docs: https://docs.openclaw.ai
---

# 🦞 OpenClaw Dashboard

**OpenClaw** ist ein persönlicher KI-Agent, der lokal läuft und sich mit Messengern wie WhatsApp, Telegram oder Discord verbinden kann. Er kann deinen PC steuern, Aufgaben automatisieren und als "Second Brain" Interface dienen.

> **🚨 WICHTIG:** Bevor du startest, lies unbedingt das **[Sicherheitskonzept & Hosting-Strategie](SECURITY_AND_HOSTING.md)**. Installiere den Agenten **nicht** einfach blind auf deinem Haupt-Rechner, wenn er 24/7 laufen soll!

## 🚀 Schnellstart (Windows Test-Modus)

Ich habe dir Batch-Skripte in diesen Ordner gelegt, damit du die Installation und Updates mit einem Doppelklick ausführen kannst.

### 1. Installation
Da du **Node.js (v24.12.0)** bereits installiert hast, kannst du direkt loslegen:
1. Führe `00_INSTALL_AGENT.bat` aus.
   *(Installiert OpenClaw global via npm)*

### 2. Einrichtung (Onboarding)
1. Führe `01_START_WIZARD.bat` aus.
2. Der Wizard führt dich durch:
   - **LLM Provider wählen:** (z.B. OpenAI, Anthropic oder lokal via Ollama).
   - **Kanäle verbinden:** (z.B. Telegram Bot Token).
   - **Skills aktivieren.**

### 3. Updates
- Führe `02_UPDATE_AGENT.bat` aus, um die neueste Version zu ziehen.

---

## 🛠 Konfiguration & Befehle

### Manuelle Befehle (Terminal)
Falls du lieber das Terminal nutzt:

| Befehl | Beschreibung |
| :--- | :--- |
| `openclaw onboard` | Startet den Konfigurations-Wizard |
| `openclaw doctor` | Prüft auf Probleme |
| `openclaw start` | Startet den Agenten (Daemon) |
| `openclaw dashboard` | Öffnet das Web-Interface |

### Verknüpfung mit Homelab
- **Ollama:** OpenClaw kann lokale Modelle nutzen. Stelle sicher, dass Ollama läuft (`ollama serve`).
- **Obsidian:** Langfristig könnte man Logs oder Outputs hierher leiten.

---

## ℹ️ Ressourcen
- [Offizielle Webseite](https://openclaw.ai)
- [GitHub Repository](https://github.com/openclaw/openclaw)
- [Dokumentation](https://docs.openclaw.ai)

> [!NOTE] Game vs. AI
> Es gibt auch ein Spiel namens "OpenClaw" (Captain Claw Remake). Dieser Ordner fokussiert sich auf den **KI-Agenten**. Falls du das Spiel wolltest, findest du es [hier](https://github.com/pjasicek/OpenClaw).
