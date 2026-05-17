"""
run_server.py — packaged distribution entrypoint
=================================================
The launcher starts the backend with:

    APP_ROOT\\python\\python.exe  APP_ROOT\\backend\\run_server.py

This script sets the working directory to the backend folder (required for
uvicorn to find the `main:app` module) then starts the server.

Not used in development — use `uvicorn main:app --reload` directly.
"""

import os
import sys
from pathlib import Path

# Add this directory to sys.path so `import main` resolves correctly.
_BACKEND_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(_BACKEND_DIR))

# Set cwd so uvicorn can locate `main:app` and routers can find sibling imports.
os.chdir(_BACKEND_DIR)

import uvicorn  # noqa: E402  (must come after sys.path manipulation)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="warning",
    )
