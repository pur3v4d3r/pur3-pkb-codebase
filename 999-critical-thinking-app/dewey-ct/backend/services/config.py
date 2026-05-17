"""
Runtime path configuration for DeweyCT backend.

Resolves DATA_DIR and DB_PATH correctly for both modes:

  Dev mode  — running `uvicorn main:app` from the backend/ directory.
              DATA_DIR  → dewey-ct/data/
              DB_PATH   → dewey-ct/deweyct.db

  Packaged  — running from portable Python inside the installer layout:
              APP_ROOT/python/python.exe  APP_ROOT/backend/run_server.py
              The launcher sets two env vars before spawning:
                DEWEYCT_PACKAGED=1
                DEWEYCT_APP_ROOT=<install dir>

              DATA_DIR  → <install dir>/data/
              DB_PATH   → %APPDATA%/DeweyctCT/deweyct.db
                          (user-writable; Program Files is read-only)
"""

import os
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Mode detection
# ---------------------------------------------------------------------------

_IS_PACKAGED: bool = bool(os.environ.get("DEWEYCT_PACKAGED"))


# ---------------------------------------------------------------------------
# App root resolution
# ---------------------------------------------------------------------------

def _resolve_root() -> Path:
    if _IS_PACKAGED:
        root_env = os.environ.get("DEWEYCT_APP_ROOT")
        if root_env:
            return Path(root_env).resolve()
        # Fallback: python.exe is at  APP_ROOT/python/python.exe
        return Path(sys.executable).resolve().parent.parent
    # Dev: this file lives at  backend/services/config.py  →  3 parents up → dewey-ct/
    return Path(__file__).resolve().parent.parent.parent


_APP_ROOT: Path = _resolve_root()


# ---------------------------------------------------------------------------
# Public paths
# ---------------------------------------------------------------------------

#: Read-only JSON content shipped with the application.
DATA_DIR: Path = _APP_ROOT / "data"

#: Read-write SQLite database.
#: In packaged mode we must write to APPDATA (Program Files is read-only).
if _IS_PACKAGED:
    _appdata = Path(os.environ.get("APPDATA", str(Path.home() / "AppData" / "Roaming")))
    _user_dir = _appdata / "DeweyctCT"
    _user_dir.mkdir(parents=True, exist_ok=True)
    DB_PATH: Path = _user_dir / "deweyct.db"
else:
    DB_PATH: Path = _APP_ROOT / "deweyct.db"
