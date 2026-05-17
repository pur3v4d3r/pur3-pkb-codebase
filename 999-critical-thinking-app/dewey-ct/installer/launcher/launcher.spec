# -*- mode: python ; coding: utf-8 -*-
#
# launcher.spec  —  PyInstaller build spec for deweyct.exe
#
# Usage (from the dewey-ct/ root):
#   pyinstaller installer/launcher/launcher.spec
#
# Output:
#   installer/launcher/dist/deweyct/deweyct.exe  (onedir bundle)

import sys
from pathlib import Path

# Resolve paths relative to this spec file
SPEC_DIR = Path(SPECPATH)        # installer/launcher/
ROOT_DIR = SPEC_DIR.parent.parent  # dewey-ct/
ICON_PATH = str(SPEC_DIR / "assets" / "deweyct.ico")

a = Analysis(
    [str(SPEC_DIR / "launcher.py")],
    pathex=[str(ROOT_DIR)],
    binaries=[],
    datas=[],
    hiddenimports=[
        # tkinter is stdlib but PyInstaller sometimes misses sub-modules
        "tkinter",
        "tkinter.ttk",
        "tkinter.messagebox",
        "tkinter.font",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Not needed — keep the bundle tiny
        "numpy", "pandas", "matplotlib", "PIL", "pystray",
        "fastapi", "uvicorn", "ollama",
    ],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="deweyct",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,           # no console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=ICON_PATH if Path(ICON_PATH).exists() else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="deweyct",
)
