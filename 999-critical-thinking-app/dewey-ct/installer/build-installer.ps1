<#
.SYNOPSIS
    build-installer.ps1 — Builds the DeweyCT Windows installer.

.DESCRIPTION
    Orchestrates every step required to produce  DeweyctInstaller.exe:

      1. Validate prerequisites (Node, Python, Inno Setup, PyInstaller)
      2. Download portable assets (Node.js, Ollama) into installer/cache/
      3. Build the Next.js frontend  (npm run build → .next/standalone)
      4. Compile the launcher        (PyInstaller → installer/launcher/dist/)
      5. Assemble the release/       staging directory
      6. Compile the Inno Setup      installer script

    Run from the repo root (dewey-ct/):

        .\installer\build-installer.ps1

.NOTES
    Requirements:
      - Node.js  ≥ 20  (on PATH)
      - Python   ≥ 3.11 (on PATH; will install PyInstaller automatically)
      - Inno Setup 6  ( https://jrsoftware.org/isinfo.php )
      - Internet access to download Node portable + Ollama binary
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
$ScriptDir    = $PSScriptRoot                            # installer/
$RepoRoot     = Split-Path $ScriptDir -Parent            # dewey-ct/
$FrontendDir  = Join-Path $RepoRoot "frontend"
$BackendDir   = Join-Path $RepoRoot "backend"
$DataDir      = Join-Path $RepoRoot "data"
$EnvFile      = Join-Path $RepoRoot ".env"
$CacheDir     = Join-Path $ScriptDir "cache"             # downloaded binaries
$ReleaseDir   = Join-Path $ScriptDir "release"           # staging area
$LauncherDir  = Join-Path $ScriptDir "launcher"
$IssFile      = Join-Path $ScriptDir "deweyct.iss"
$IsccExe      = "C:\Program Files (x86)\Inno Setup 6\ISCC.exe"

# Portable asset versions / URLs
$NodeVersion  = "20.19.2"
$NodeZipUrl   = "https://nodejs.org/dist/v$NodeVersion/node-v$NodeVersion-win-x64.zip"
$NodeZipName  = "node-v$NodeVersion-win-x64.zip"
$NodeExeInZip = "node-v$NodeVersion-win-x64\node.exe"

$OllamaUrl    = "https://github.com/ollama/ollama/releases/latest/download/ollama-windows-amd64.zip"
$OllamaZip    = "ollama-windows-amd64.zip"

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
function Write-Step([string]$msg) {
    Write-Host "`n━━━  $msg  ━━━" -ForegroundColor Cyan
}

function Require-Command([string]$cmd) {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        throw "Required command not found: $cmd. Please install it and re-run."
    }
}

function Download-IfMissing([string]$url, [string]$dest) {
    if (-not (Test-Path $dest)) {
        Write-Host "  Downloading $(Split-Path $dest -Leaf)..."
        Invoke-WebRequest -Uri $url -OutFile $dest -UseBasicParsing
    } else {
        Write-Host "  Cached: $(Split-Path $dest -Leaf)"
    }
}

# ---------------------------------------------------------------------------
# Step 1 — Validate prerequisites
# ---------------------------------------------------------------------------
Write-Step "Validating prerequisites"

Require-Command "node"
Require-Command "python"

$nodeVer  = node --version
$pythonVer = python --version
Write-Host "  node   : $nodeVer"
Write-Host "  python : $pythonVer"

if (-not (Test-Path $IsccExe)) {
    throw "Inno Setup 6 not found at '$IsccExe'.`nDownload it from https://jrsoftware.org/isinfo.php and install, then re-run."
}
Write-Host "  Inno Setup 6 : found"

# Ensure PyInstaller is available (pip install is idempotent — skips if already present)
Write-Host "  Ensuring PyInstaller is installed..."
$oldEap = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
& python -m pip install pyinstaller --quiet 2>&1 | Out-Null
$ErrorActionPreference = $oldEap
if ($LASTEXITCODE -ne 0) { throw "Failed to install PyInstaller." }
Write-Host "  PyInstaller  : ok"

# ---------------------------------------------------------------------------
# Step 2 — Download portable assets
# ---------------------------------------------------------------------------
Write-Step "Downloading portable assets (cached in installer/cache/)"

New-Item -ItemType Directory -Force -Path $CacheDir | Out-Null

$nodeZipPath   = Join-Path $CacheDir $NodeZipName
$ollamaZipPath = Join-Path $CacheDir $OllamaZip

Download-IfMissing $NodeZipUrl   $nodeZipPath
Download-IfMissing $OllamaUrl    $ollamaZipPath

# ---------------------------------------------------------------------------
# Step 3 — Build Next.js frontend
# ---------------------------------------------------------------------------
Write-Step "Building Next.js frontend (npm run build)"

Push-Location $FrontendDir
try {
    npm ci --silent
    npm run build
    if ($LASTEXITCODE -ne 0) { throw "npm run build failed." }
} finally {
    Pop-Location
}

$StandaloneDir = Join-Path $FrontendDir ".next\standalone"
if (-not (Test-Path $StandaloneDir)) {
    throw "Expected .next\standalone\ not found.`nEnsure next.config.mjs has  output: 'standalone'."
}
Write-Host "  Standalone output: $StandaloneDir"

# ---------------------------------------------------------------------------
# Step 4 — Compile the launcher with PyInstaller
# ---------------------------------------------------------------------------
Write-Step "Compiling launcher (PyInstaller)"

$LauncherSpec = Join-Path $LauncherDir "launcher.spec"
$LauncherDist = Join-Path $LauncherDir "dist\deweyct"

Push-Location $RepoRoot
try {
    python -m PyInstaller $LauncherSpec --distpath (Join-Path $LauncherDir "dist") --workpath (Join-Path $LauncherDir "build") --noconfirm
    if ($LASTEXITCODE -ne 0) { throw "PyInstaller failed." }
} finally {
    Pop-Location
}

if (-not (Test-Path (Join-Path $LauncherDist "deweyct.exe"))) {
    throw "Launcher exe not found after PyInstaller build."
}
Write-Host "  Launcher compiled: $LauncherDist\deweyct.exe"

# ---------------------------------------------------------------------------
# Step 5 — Assemble the release/ staging directory
# ---------------------------------------------------------------------------
Write-Step "Assembling release/ staging directory"

# Clean and recreate
if (Test-Path $ReleaseDir) { Remove-Item $ReleaseDir -Recurse -Force }
New-Item -ItemType Directory -Force -Path $ReleaseDir | Out-Null

function Copy-Dir([string]$src, [string]$dst) {
    New-Item -ItemType Directory -Force -Path $dst | Out-Null
    Copy-Item "$src\*" $dst -Recurse -Force
}

# 5a. Launcher bundle
Write-Host "  Copying launcher..."
Copy-Dir $LauncherDist (Join-Path $ReleaseDir "deweyct")

# 5b. Backend source (excluding __pycache__ and .pyc)
Write-Host "  Copying backend..."
$relBackend = Join-Path $ReleaseDir "backend"
New-Item -ItemType Directory -Force -Path $relBackend | Out-Null
Get-ChildItem $BackendDir -Recurse |
    Where-Object { $_.FullName -notmatch '__pycache__' -and $_.Extension -ne '.pyc' } |
    ForEach-Object {
        $dest = $_.FullName.Replace($BackendDir, $relBackend)
        if ($_.PSIsContainer) { New-Item -ItemType Directory -Force -Path $dest | Out-Null }
        else { Copy-Item $_.FullName $dest -Force }
    }

# 5c. Install Python packages into a portable python/ layout
Write-Host "  Setting up portable Python runtime..."
$RelPython = Join-Path $ReleaseDir "python"
New-Item -ItemType Directory -Force -Path $RelPython | Out-Null

# Use a temporary venv to collect packages, then copy site-packages
$TmpVenv = Join-Path $CacheDir "build-venv"
if (-not (Test-Path $TmpVenv)) {
    python -m venv $TmpVenv
}
& "$TmpVenv\Scripts\pip.exe" install `
    fastapi uvicorn[standard] ollama pydantic python-dotenv slowapi `
    --quiet --target (Join-Path $RelPython "Lib\site-packages")

# Copy Python interpreter itself from the build venv
Copy-Item "$TmpVenv\Scripts\python.exe" (Join-Path $RelPython "python.exe") -Force
Copy-Item "$TmpVenv\Scripts\pythonw.exe" (Join-Path $RelPython "pythonw.exe") -Force -ErrorAction SilentlyContinue

# Copy Python standard library DLLs
$PythonDll = Get-ChildItem "$TmpVenv" -Filter "python3*.dll" -Recurse | Select-Object -First 1
if ($PythonDll) { Copy-Item $PythonDll.FullName $RelPython -Force }
$PythonDll2 = Get-ChildItem "$TmpVenv\Scripts" -Filter "*.dll" | Select-Object -First 5
foreach ($dll in $PythonDll2) { Copy-Item $dll.FullName $RelPython -Force -ErrorAction SilentlyContinue }

# Copy stdlib zip (pythonXY.zip) if present
$StdlibZip = Get-ChildItem "$TmpVenv" -Filter "python*.zip" -Recurse | Select-Object -First 1
if ($StdlibZip) { Copy-Item $StdlibZip.FullName $RelPython -Force }

Write-Host "  NOTE: Python runtime copy uses the build venv. For a fully"
Write-Host "        self-contained release, consider using the Python embeddable"
Write-Host "        package instead (see README-packaging.md)."

# 5d. Next.js standalone frontend
Write-Host "  Copying Next.js standalone output..."
$RelFrontend = Join-Path $ReleaseDir "frontend"
Copy-Dir $StandaloneDir $RelFrontend
# Also copy the public/ and .next/static/ that standalone needs at runtime
$PublicSrc  = Join-Path $FrontendDir "public"
$StaticSrc  = Join-Path $FrontendDir ".next\static"
if (Test-Path $PublicSrc) { Copy-Dir $PublicSrc (Join-Path $RelFrontend "public") }
if (Test-Path $StaticSrc) {
    New-Item -ItemType Directory -Force -Path (Join-Path $RelFrontend ".next\static") | Out-Null
    Copy-Dir $StaticSrc (Join-Path $RelFrontend ".next\static")
}

# 5e. Portable Node.js (extract single node.exe from ZIP)
Write-Host "  Extracting Node.js portable..."
$RelNode = Join-Path $ReleaseDir "node"
New-Item -ItemType Directory -Force -Path $RelNode | Out-Null
Add-Type -AssemblyName System.IO.Compression.FileSystem
$nodeZip = [System.IO.Compression.ZipFile]::OpenRead($nodeZipPath)
$nodeEntry = $nodeZip.Entries | Where-Object { $_.FullName -like "*\node.exe" } | Select-Object -First 1
if ($nodeEntry) {
    $nodeOut = Join-Path $RelNode "node.exe"
    [System.IO.Compression.ZipFileExtensions]::ExtractToFile($nodeEntry, $nodeOut, $true)
    Write-Host "  node.exe extracted."
} else {
    throw "Could not find node.exe inside $nodeZipPath"
}
$nodeZip.Dispose()

# 5f. Ollama portable binary
Write-Host "  Extracting Ollama..."
$RelOllama = Join-Path $ReleaseDir "ollama"
New-Item -ItemType Directory -Force -Path $RelOllama | Out-Null
Expand-Archive -Path $ollamaZipPath -DestinationPath $RelOllama -Force
# Flatten if ollama.exe is inside a subdirectory
$ollamaExeInner = Get-ChildItem $RelOllama -Filter "ollama.exe" -Recurse | Select-Object -First 1
if ($ollamaExeInner -and ($ollamaExeInner.DirectoryName -ne $RelOllama)) {
    Move-Item $ollamaExeInner.FullName (Join-Path $RelOllama "ollama.exe") -Force
}

# 5g. Data files (JSON content)
Write-Host "  Copying data/..."
Copy-Dir $DataDir (Join-Path $ReleaseDir "data")

# 5h. Default .env
Write-Host "  Copying .env..."
Copy-Item $EnvFile (Join-Path $ReleaseDir ".env") -Force

Write-Host ""
Write-Host "  Release directory assembled: $ReleaseDir"
Get-ChildItem $ReleaseDir | ForEach-Object { Write-Host "    $($_.Name)" }

# ---------------------------------------------------------------------------
# Step 6 — Compile the Inno Setup installer
# ---------------------------------------------------------------------------
Write-Step "Compiling Inno Setup installer"

Push-Location $ScriptDir
try {
    & $IsccExe $IssFile
    if ($LASTEXITCODE -ne 0) { throw "ISCC.exe failed with exit code $LASTEXITCODE." }
} finally {
    Pop-Location
}

$InstallerOut = Join-Path $RepoRoot "DeweyctInstaller.exe"
if (Test-Path $InstallerOut) {
    $size = [math]::Round((Get-Item $InstallerOut).Length / 1MB, 1)
    Write-Host ""
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Green
    Write-Host "  BUILD COMPLETE" -ForegroundColor Green
    Write-Host "  Installer: $InstallerOut" -ForegroundColor Green
    Write-Host "  Size     : $size MB" -ForegroundColor Green
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Green
} else {
    throw "Installer not found at expected location: $InstallerOut"
}
