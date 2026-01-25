# Setup Start Script for Andreas
# Starts Chrome, Obsidian, and Warp

Write-Host "Starte Setup..." -ForegroundColor Cyan

# 1. Google Chrome starten
if (Test-Path "C:\Program Files\Google\Chrome\Application\chrome.exe") {
    Start-Process "C:\Program Files\Google\Chrome\Application\chrome.exe"
    Write-Host "[OK] Google Chrome" -ForegroundColor Green
} else {
    Write-Host "[!] Chrome Pfad nicht gefunden, versuche Standard-Befehl..." -ForegroundColor Yellow
    Start-Process "chrome.exe" -ErrorAction SilentlyContinue
}

# 2. Obsidian starten (via AppID)
Start-Process "shell:AppsFolder\md.obsidian"
Write-Host "[OK] Obsidian" -ForegroundColor Green

# 3. Warp starten
Start-Process "warp.cmd" -ErrorAction SilentlyContinue
Write-Host "[OK] Warp" -ForegroundColor Green

Write-Host "Setup abgeschlossen!" -ForegroundColor Cyan
Pause
