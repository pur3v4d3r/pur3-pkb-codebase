# DeweyCT — Packaging Guide

This document explains how to build the `DeweyctInstaller.exe` Windows installer from source.

---

## Prerequisites

Install and verify each item before running the build script.

| Requirement | Version | Notes |
|-------------|---------|-------|
| Windows 10 / 11 (x64) | — | Build machine must be Windows |
| Node.js | ≥ 20 LTS | <https://nodejs.org> — must be on `PATH` |
| Python | ≥ 3.11 | <https://python.org> — must be on `PATH` |
| Inno Setup 6 | 6.x | <https://jrsoftware.org/isinfo.php> — install to default path |
| PyInstaller | ≥ 6.0 | Installed automatically by the build script if absent |
| Internet access | — | Needed to download portable Node.js + Ollama binaries |

---

## What gets bundled

| Component | Source | Destination in installer |
|-----------|--------|--------------------------|
| Launcher (`deweyct.exe`) | PyInstaller build from `installer/launcher/launcher.py` | `{app}\deweyct\` |
| Python runtime + packages | venv + pip install | `{app}\python\` |
| FastAPI backend source | `backend/` | `{app}\backend\` |
| Next.js standalone server | `npm run build` → `.next/standalone/` | `{app}\frontend\` |
| Portable Node.js | Downloaded from nodejs.org | `{app}\node\node.exe` |
| Ollama portable binary | Downloaded from GitHub releases | `{app}\ollama\ollama.exe` |
| Content data files | `data/` | `{app}\data\` |
| Default config | `.env` | `{app}\.env` |

**NOT bundled:** AI models (~2–5 GB each). They are downloaded on first launch via the built-in setup wizard.

---

## Build steps

Run this **once**, from the `dewey-ct/` repository root:

```powershell
.\installer\build-installer.ps1
```

The script will:

1. Validate all prerequisites  
2. Download portable Node.js and Ollama into `installer/cache/` (cached, not re-downloaded on rebuild)  
3. Run `npm run build` to produce the Next.js standalone output  
4. Run `PyInstaller` to compile `deweyct.exe`  
5. Assemble everything into `installer/release/`  
6. Invoke Inno Setup to produce `DeweyctInstaller.exe` in the `dewey-ct/` root  

Expected total time: **5–15 minutes** on first run (network-dependent).

---

## Output

```
dewey-ct/
  DeweyctInstaller.exe   ← distribute this file
  installer/
    cache/               ← downloaded binaries (safe to delete to force re-download)
    release/             ← staging directory (safe to delete; rebuilt every time)
    launcher/
      build/             ← PyInstaller workdir (can be deleted)
      dist/              ← compiled launcher (can be deleted)
```

---

## Rebuilding after code changes

| Change | What to re-run |
|--------|---------------|
| Frontend only | `npm run build` in `frontend/`, then re-run the full script |
| Backend Python only | Re-run the full script (backend is copied as source, no compile) |
| Launcher (`launcher.py`) | Re-run the full script (triggers PyInstaller re-compile) |
| Inno Setup script only | `& "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer\deweyct.iss` |
| Everything | Re-run `.\installer\build-installer.ps1` |

---

## File layout after installation

When `DeweyctInstaller.exe` is run on a target machine:

```
C:\Program Files\DeweyCT\
  deweyct\
    deweyct.exe        ← double-click to launch
    _internal\         ← PyInstaller runtime support files
  backend\             ← FastAPI source
  python\              ← portable Python interpreter
  frontend\            ← Next.js standalone
  node\
    node.exe           ← portable Node.js
  ollama\
    ollama.exe         ← Ollama inference engine
  data\                ← JSON content files
  .env                 ← default config

%APPDATA%\DeweyctCT\
  deweyct.db           ← SQLite database (user data)
  .setup-complete      ← flag written after first-run wizard completes
```

---

## First-run experience

1. User double-clicks the desktop shortcut or Start Menu entry.  
2. On the **very first launch** only, a setup wizard appears.  
3. The wizard lets the user choose between two AI models:
   - **phi3:3.8b** (~2.2 GB, fast, works on most hardware)  
   - **qwen3:8b-q4_K_M** (~5.2 GB, higher quality, requires 8 GB+ RAM/VRAM)  
4. The selected model is downloaded via `ollama pull` (internet required, ~minutes).  
5. The chosen model is saved to `%APPDATA%\DeweyctCT\.setup-complete` and `.env`.  
6. All subsequent launches start immediately — no wizard, no download.

---

## Customising the default model

Edit `dewey-ct/.env` **before building**:

```dotenv
OLLAMA_MODEL=phi3:3.8b
```

Users can also change it after install by editing `C:\Program Files\DeweyCT\.env`.

---

## Adding an application icon

1. Create a 256×256 ICO file and save it to `installer/launcher/assets/deweyct.ico`.  
2. The `launcher.spec` and `deweyct.iss` scripts already reference that path.  
3. Re-run the build script.

---

## Troubleshooting

### `next build` fails with "output: 'standalone' not set"
Verify `frontend/next.config.mjs` contains `output: 'standalone'` inside the `nextConfig` object.

### PyInstaller error: "tkinter not found"
Ensure you installed Python from python.org (includes tkinter), not from the Microsoft Store (tkinter may be missing).

### `ollama.exe` not found after extraction
The Ollama GitHub release zip structure sometimes changes. Inspect `installer/cache/ollama-windows-amd64.zip` and adjust the extraction path in `build-installer.ps1`.

### Installer runs but `deweyct.exe` crashes on launch
Run `deweyct.exe` from a terminal to see the error output:

```powershell
cd "C:\Program Files\DeweyCT\deweyct"
.\deweyct.exe
```

Common causes:
- `python\python.exe` is missing required DLLs — check the portable Python copy step.
- `node\node.exe` not found — re-run the build.
- Port 8000 or 3001 already in use — kill other processes using those ports.

### Backend health check times out
The backend prints errors to `%APPDATA%\DeweyctCT\backend.log` (if you add logging to `run_server.py`). Check Ollama is serving on port 11434 first.

---

## Version bumping

Update the version in **two** places:

1. `installer/deweyct.iss` — `#define MyAppVersion "X.Y.Z"`  
2. `frontend/package.json` — `"version": "X.Y.Z"`

---

## Clean build

To start completely fresh:

```powershell
Remove-Item .\installer\release  -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item .\installer\launcher\build -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item .\installer\launcher\dist  -Recurse -Force -ErrorAction SilentlyContinue
# To also re-download binaries:
# Remove-Item .\installer\cache -Recurse -Force
.\installer\build-installer.ps1
```
