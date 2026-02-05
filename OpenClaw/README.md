# OpenClaw Installation Guide

This folder contains information for **OpenClaw**. Since there are two popular projects with this name, instructions for both are provided below.

---

## 1. OpenClaw (AI Agent / Personal Assistant)
*A personal AI agent that runs locally and connects to apps like WhatsApp, Telegram, and Discord.*

### Prerequisites
- **Node.js**: Version 18+ (v22 recommended).
- **OS**: macOS, Linux, or Windows (WSL2 recommended).

### Installation (CLI)
The easiest way to install is via `npm` (Node Package Manager) or the install script.

#### Option A: NPM (Recommended for Windows)
```bash
npm install -g openclaw@latest
```
*Note: If you run into issues with `sharp`, try:*
```bash
SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
```

#### Option B: Curl (Linux/macOS/WSL)
```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

### Setup
After installation, run the onboarding wizard to configure your AI model and channels:
```bash
openclaw onboard
```

---

## 2. OpenClaw (Game Engine - Captain Claw Reimplementation)
*A fan-made, open-source reimplementation of the classic 1997 platformer "Captain Claw".*

### Prerequisites
- **Original Game Assets**: You need the `CLAW.REZ` file from the original game.
- **Project URL**: [https://github.com/pjasicek/OpenClaw](https://github.com/pjasicek/OpenClaw)

### Installation
1.  **Download**: Get the latest release from the [GitHub Releases page](https://github.com/pjasicek/OpenClaw/releases) or clone the repo to build from source.
2.  **Assets**: Place your `CLAW.REZ` file into the `Build_Release` (or root) directory where the executable is.
3.  **Run**: Execute `OpenClaw.exe` (Windows) or the binary (Linux).

### Building from Source (Windows)
1.  Clone the repository.
2.  Open the solution file (VS2017+) or use CMake.
3.  Ensure dependencies (SDL2, Box2D, etc.) are linked correctly.
4.  Build and Run.
