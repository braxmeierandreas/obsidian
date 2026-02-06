$scriptDir = $PSScriptRoot
$sourcePath = Join-Path $scriptDir "posts"
$destinationPath = Join-Path $scriptDir "my_blog\content\posts"

# --- HELPER: FIND EXECUTABLES ---
function Get-ExecutablePath {
    param($Name, $CommonPaths)
    
    if (Get-Command $Name -ErrorAction SilentlyContinue) {
        return $Name
    }
    
    foreach ($path in $CommonPaths) {
        if (Test-Path $path) {
            Write-Host "Found $Name at custom path: $path" -ForegroundColor DarkGray
            return $path
        }
    }
    
    return $null
}

$gitPath = Get-ExecutablePath "git" @(
    "C:\Program Files\Git\cmd\git.exe",
    "C:\Program Files\Git\bin\git.exe"
)

$hugoPath = Get-ExecutablePath "hugo" @(
    "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\Hugo.Hugo.Extended_Microsoft.Winget.Source_8wekyb3d8bbwe\hugo.exe",
    "$env:LOCALAPPDATA\Microsoft\WinGet\Links\hugo.exe"
)

if (-not $gitPath) { Write-Error "Git not found! Please install Git."; exit }
if (-not $hugoPath) { Write-Error "Hugo not found! Please install Hugo."; exit }

# 1. Sync Posts
Write-Host "Syncing posts..." -ForegroundColor Green
# Robocopy returns exit codes that are not always errors. 
# 1 = One or more files were copied successfully (that is successful).
# We suppress the output slightly to keep it clean, but let basic info show.
robocopy $sourcePath $destinationPath /mir /njh /njs /ndl /nc /ns
if ($LASTEXITCODE -ge 8) {
    Write-Error "Robocopy failed with exit code $LASTEXITCODE"
    exit
}

# 2. Bilder fixen
Write-Host "Processing images..." -ForegroundColor Green
$imagesScript = Join-Path $scriptDir "images.py"
python $imagesScript

# 3. Hugo Build (Webseite generieren)
Write-Host "Building site..." -ForegroundColor Cyan
$hugoDir = Join-Path $scriptDir "my_blog"
cd $hugoDir
& $hugoPath

# 4. Zu GitHub hochladen
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
& $gitPath add .
& $gitPath commit -m "New blog post update $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
& $gitPath push origin master

Write-Host "Done! Your blog should be updated in a few minutes." -ForegroundColor Green
