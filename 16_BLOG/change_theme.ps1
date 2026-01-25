# Skript zum Wechseln des Hugo-Themes (Robust Version)
# Methode: Clone + Un-Git (Vermeidet Submodule-Probleme auf Windows)

$scriptDir = $PSScriptRoot
$blogDir = Join-Path $scriptDir "my_blog"

# 1. Eingabe der URL
Write-Host "--- Hugo Theme Switcher (Robust) ---" -ForegroundColor Cyan
$themeUrl = Read-Host "Bitte die GitHub-URL des neuen Themes einfuegen (z.B. https://github.com/user/theme.git)"

if ([string]::IsNullOrWhiteSpace($themeUrl)) {
    Write-Error "Keine URL eingegeben."
    exit
}

# Theme-Namen aus der URL extrahieren
$themeName = $themeUrl.Split("/")[-1].Replace(".git", "")
Write-Host "Neues Theme: $themeName" -ForegroundColor Yellow

cd $blogDir

# 2. ALTES Theme entfernen (Brutal aber effektiv)
Write-Host "Entferne alte Themes..." -ForegroundColor Yellow
$themesPath = Join-Path $blogDir "themes"

# Git Cache bereinigen, falls vorhanden
git rm -r --cached themes 2>$null

# Ordner physisch loeschen
if (Test-Path $themesPath) {
    Remove-Item -Recurse -Force $themesPath -ErrorAction SilentlyContinue
}
# Ordner neu erstellen
New-Item -ItemType Directory -Force -Path $themesPath | Out-Null

# 3. NEUES Theme installieren (Clone & Detach)
Write-Host "Lade $themeName herunter..." -ForegroundColor Green
$newThemePath = Join-Path $themesPath $themeName
git clone $themeUrl $newThemePath

# Wichtig: Den .git Ordner im Theme loeschen, damit es normale Dateien werden
$innerGit = Join-Path $newThemePath ".git"
if (Test-Path $innerGit) {
    Remove-Item -Recurse -Force $innerGit -ErrorAction SilentlyContinue
}

# 4. hugo.toml anpassen (NUR den Namen, Rest ist Handarbeit!)
Write-Host "Aktualisiere hugo.toml..." -ForegroundColor Green
$configFile = Join-Path $blogDir "hugo.toml"
if (Test-Path $configFile) {
    $content = Get-Content $configFile
    # Ersetze theme = "..." mit dem neuen Namen
    $newContent = $content -replace 'theme = ".*"', "theme = `"$themeName`""
    $newContent | Set-Content $configFile
}

# 5. Hochladen
Write-Host "Lade Dateien zu GitHub hoch..." -ForegroundColor Cyan
git add .
git commit -m "Switched theme to $themeName (via Script)"
git push

Write-Host "------------------------------------------------" -ForegroundColor Magenta
Write-Host "ACHTUNG - WICHTIG:"
Write-Host "1. Das Theme wurde ausgetauscht."
Write-Host "2. Jedes Theme hat andere Einstellungen in der 'hugo.toml'."
Write-Host "   -> Es kann sein, dass der Build erst klappt, wenn du die"
Write-Host "      'hugo.toml' an die Anleitung des neuen Themes anpasst!"
Write-Host "------------------------------------------------" -ForegroundColor Magenta
pause