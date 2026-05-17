"""
DeweyCT Launcher
================
Bootstraps Ollama, the FastAPI backend, and the Next.js frontend;
opens the browser once everything is ready; provides a status window
so users can see what is happening and stop the app cleanly.

Compiled to  deweyct.exe  via PyInstaller (see launcher.spec).
Only stdlib + tkinter are used — no third-party runtime dependencies.
"""

from __future__ import annotations

import os
import sys
import subprocess
import threading
import time
import socket
import urllib.request
import urllib.error
import webbrowser
import json
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

# ---------------------------------------------------------------------------
# App constants
# ---------------------------------------------------------------------------

APP_NAME = "DeweyCT"
FRONTEND_URL = "http://localhost:3001"
BACKEND_HEALTH_URL = "http://localhost:8000/health"
OLLAMA_URL = "http://localhost:11434"
BACKEND_PORT = 8000
FRONTEND_PORT = 3001

MODELS: dict[str, dict] = {
    "phi3:3.8b": {
        "label": "Fast  —  phi3:3.8b  (~2.2 GB, works on most computers)",
        "size": "~2.2 GB",
    },
    "qwen3:8b-q4_K_M": {
        "label": "High Quality  —  qwen3:8b Q4_K_M  (~5.2 GB, needs 8 GB+ RAM/GPU)",
        "size": "~5.2 GB",
    },
}

# ---------------------------------------------------------------------------
# Path resolution
# ---------------------------------------------------------------------------

if getattr(sys, "frozen", False):
    # PyInstaller bundle: deweyct.exe lives in {install_root}\deweyct\
    # All other directories (ollama, python, node, etc.) are siblings of deweyct\
    APP_DIR = Path(sys.executable).parent.parent
else:
    # Dev: installer/launcher/launcher.py  →  up 2 levels  →  dewey-ct/
    APP_DIR = Path(__file__).parent.parent.parent

OLLAMA_EXE   = APP_DIR / "ollama"  / "ollama.exe"
PYTHON_EXE   = APP_DIR / "python"  / "python.exe"
BACKEND_DIR  = APP_DIR / "backend"
RUN_SERVER   = BACKEND_DIR / "run_server.py"
NODE_EXE     = APP_DIR / "node"    / "node.exe"
FRONTEND_DIR = APP_DIR / "frontend"
SERVER_JS    = FRONTEND_DIR / "server.js"
ENV_FILE     = APP_DIR / ".env"

APPDATA       = Path(os.environ.get("APPDATA", str(Path.home() / "AppData" / "Roaming")))
USER_DATA_DIR = APPDATA / "DeweyctCT"
SETUP_FLAG    = USER_DATA_DIR / ".setup-complete"

# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def _port_open(port: int, host: str = "127.0.0.1", timeout: float = 1.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _http_ok(url: str, timeout: float = 2.0) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            return resp.status < 400
    except Exception:
        return False


def _read_env_model() -> str:
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith("OLLAMA_MODEL="):
                return line.split("=", 1)[1].strip()
    return "phi3:3.8b"


def _write_env_model(model: str) -> None:
    content = ENV_FILE.read_text(encoding="utf-8") if ENV_FILE.exists() else ""
    lines = content.splitlines()
    updated = False
    for i, ln in enumerate(lines):
        if ln.startswith("OLLAMA_MODEL="):
            lines[i] = f"OLLAMA_MODEL={model}"
            updated = True
            break
    if not updated:
        lines.append(f"OLLAMA_MODEL={model}")
    ENV_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _is_model_available(model: str) -> bool:
    try:
        result = subprocess.run(
            [str(OLLAMA_EXE), "list"],
            capture_output=True, text=True, timeout=10,
        )
        return model.lower() in result.stdout.lower()
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Process management
# ---------------------------------------------------------------------------

_procs: list[subprocess.Popen] = []
_stop_event = threading.Event()


def _spawn(cmd: list[str], env_extra: dict | None = None, cwd: str | None = None) -> subprocess.Popen:
    env = os.environ.copy()
    if env_extra:
        env.update(env_extra)
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=env,
        cwd=cwd,
    )
    _procs.append(proc)
    return proc


def _stop_all() -> None:
    _stop_event.set()
    for proc in reversed(_procs):
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except Exception:
            try:
                proc.kill()
            except Exception:
                pass


# ---------------------------------------------------------------------------
# First-run setup wizard (model selection + download)
# ---------------------------------------------------------------------------

class SetupWizard(tk.Toplevel):
    """Modal window shown on first run to pick a model and download it."""

    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.title(f"{APP_NAME} — First-time Setup")
        self.resizable(False, False)
        self.grab_set()
        self._chosen_model: str | None = None
        self._build_ui()
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    # ── UI ──────────────────────────────────────────────────────────────────

    def _build_ui(self) -> None:
        pad = {"padx": 16, "pady": 8}

        tk.Label(
            self,
            text="Welcome to DeweyCT!",
            font=("Segoe UI", 13, "bold"),
        ).pack(**pad)

        tk.Label(
            self,
            text=(
                "DeweyCT needs an AI model to power its critical-thinking\n"
                "tools. Please choose one to download on first run.\n\n"
                "The download happens once; subsequent launches are instant."
            ),
            justify="left",
        ).pack(**pad)

        tk.Label(self, text="Choose a model:", font=("Segoe UI", 10, "bold")).pack(
            anchor="w", padx=16
        )

        self._var = tk.StringVar(value="phi3:3.8b")
        for model_id, info in MODELS.items():
            tk.Radiobutton(
                self,
                text=info["label"],
                variable=self._var,
                value=model_id,
                anchor="w",
            ).pack(fill="x", padx=24, pady=2)

        self._log_text = tk.Text(self, height=6, width=60, state="disabled", bg="#1e1e1e", fg="#cccccc")
        self._log_text.pack(padx=16, pady=(8, 4))

        self._progress = ttk.Progressbar(self, mode="indeterminate", length=400)
        self._progress.pack(padx=16, pady=4)

        self._btn = tk.Button(
            self,
            text="Download and Continue",
            font=("Segoe UI", 10),
            command=self._start_download,
            width=24,
        )
        self._btn.pack(pady=(8, 16))

    def _log(self, msg: str) -> None:
        self._log_text.configure(state="normal")
        self._log_text.insert("end", msg + "\n")
        self._log_text.see("end")
        self._log_text.configure(state="disabled")

    # ── Download ────────────────────────────────────────────────────────────

    def _start_download(self) -> None:
        model = self._var.get()
        self._btn.configure(state="disabled")
        self._progress.start(12)
        threading.Thread(target=self._download_worker, args=(model,), daemon=True).start()

    def _download_worker(self, model: str) -> None:
        self._log(f"Checking Ollama service...")

        # Ensure Ollama is running before pulling
        if not _port_open(11434):
            self._log("Starting Ollama service...")
            _spawn([str(OLLAMA_EXE), "serve"])
            for _ in range(30):
                if _port_open(11434):
                    break
                time.sleep(1)
            else:
                self._log("ERROR: Could not start Ollama. Check installation.")
                self.after(0, self._reset_btn)
                return

        if _is_model_available(model):
            self._log(f"Model '{model}' already downloaded. ✓")
        else:
            self._log(f"Downloading '{model}'  ({MODELS[model]['size']})...")
            self._log("This may take several minutes — please wait.\n")
            try:
                proc = subprocess.Popen(
                    [str(OLLAMA_EXE), "pull", model],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True, encoding="utf-8", errors="replace",
                )
                for line in proc.stdout:
                    stripped = line.rstrip()
                    if stripped:
                        self.after(0, self._log, stripped)
                proc.wait()
                if proc.returncode != 0:
                    self._log("ERROR: Download failed. Check your internet connection.")
                    self.after(0, self._reset_btn)
                    return
            except Exception as exc:
                self._log(f"ERROR: {exc}")
                self.after(0, self._reset_btn)
                return

        # Write chosen model to .env
        _write_env_model(model)
        self._log(f"\nModel set to: {model}")

        # Mark setup as complete
        USER_DATA_DIR.mkdir(parents=True, exist_ok=True)
        SETUP_FLAG.write_text(model, encoding="utf-8")

        self._chosen_model = model
        self.after(0, self._finish)

    def _finish(self) -> None:
        self._progress.stop()
        self._log("\nSetup complete! Starting DeweyCT...")
        self.after(800, self.destroy)

    def _reset_btn(self) -> None:
        self._progress.stop()
        self._btn.configure(state="normal")

    def _on_close(self) -> None:
        if messagebox.askyesno("Quit", "Setup not complete. Quit DeweyCT?", parent=self):
            _stop_all()
            self.master.destroy()


# ---------------------------------------------------------------------------
# Main launcher window
# ---------------------------------------------------------------------------

class LauncherApp(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title(APP_NAME)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self._build_ui()
        self.after(200, self._start_sequence)

    # ── UI ──────────────────────────────────────────────────────────────────

    def _build_ui(self) -> None:
        self._status_var = tk.StringVar(value="Initialising…")
        self._detail_var = tk.StringVar(value="")

        frame = tk.Frame(self, padx=20, pady=16)
        frame.pack(fill="both", expand=True)

        tk.Label(
            frame,
            text=APP_NAME,
            font=("Segoe UI", 16, "bold"),
            fg="#1e40af",
        ).pack(anchor="w")

        tk.Label(frame, textvariable=self._status_var, font=("Segoe UI", 10)).pack(
            anchor="w", pady=(4, 0)
        )
        tk.Label(
            frame,
            textvariable=self._detail_var,
            font=("Segoe UI", 8),
            fg="#6b7280",
            wraplength=300,
        ).pack(anchor="w")

        self._progress = ttk.Progressbar(frame, mode="indeterminate", length=320)
        self._progress.pack(pady=(10, 6))
        self._progress.start(10)

        self._open_btn = tk.Button(
            frame,
            text="Open in Browser",
            state="disabled",
            command=lambda: webbrowser.open(FRONTEND_URL),
            width=18,
        )
        self._open_btn.pack(side="left", pady=(4, 0))

        tk.Button(
            frame,
            text="Stop DeweyCT",
            command=self._on_close,
            width=14,
        ).pack(side="right", pady=(4, 0))

    def _set_status(self, msg: str, detail: str = "") -> None:
        self._status_var.set(msg)
        self._detail_var.set(detail)

    # ── Startup sequence (runs on background thread) ─────────────────────────

    def _start_sequence(self) -> None:
        threading.Thread(target=self._run_startup, daemon=True).start()

    def _run_startup(self) -> None:
        try:
            self._do_first_run_check()
            self._start_ollama()
            self._start_backend()
            self._start_frontend()
            self._wait_ready()
        except Exception as exc:
            self.after(0, self._fatal, str(exc))

    def _do_first_run_check(self) -> None:
        if not SETUP_FLAG.exists():
            # Block until wizard is closed
            done = threading.Event()

            def _open_wizard() -> None:
                wizard = SetupWizard(self)
                self.wait_window(wizard)
                done.set()

            self.after(0, _open_wizard)
            done.wait()

            if not SETUP_FLAG.exists():
                raise RuntimeError("Setup was cancelled.")

    def _start_ollama(self) -> None:
        if _port_open(11434):
            self.after(0, self._set_status, "Ollama already running  ✓")
            return

        self.after(0, self._set_status, "Starting Ollama…", "This takes a few seconds on first launch")
        _spawn([str(OLLAMA_EXE), "serve"])

        for _ in range(30):
            if _port_open(11434):
                self.after(0, self._set_status, "Ollama ready  ✓")
                return
            time.sleep(1)

        raise RuntimeError("Ollama did not start within 30 seconds.")

    def _start_backend(self) -> None:
        self.after(0, self._set_status, "Starting backend…")
        env_extra = {
            "DEWEYCT_PACKAGED": "1",
            "DEWEYCT_APP_ROOT": str(APP_DIR),
        }
        _spawn(
            [str(PYTHON_EXE), str(RUN_SERVER)],
            env_extra=env_extra,
            cwd=str(BACKEND_DIR),
        )
        for _ in range(30):
            if _http_ok(BACKEND_HEALTH_URL):
                self.after(0, self._set_status, "Backend ready  ✓")
                return
            time.sleep(1)
        raise RuntimeError("Backend did not start within 30 seconds.")

    def _start_frontend(self) -> None:
        self.after(0, self._set_status, "Starting frontend…")
        _spawn(
            [str(NODE_EXE), str(SERVER_JS)],
            env_extra={
                "PORT": str(FRONTEND_PORT),
                "HOSTNAME": "127.0.0.1",
            },
            cwd=str(FRONTEND_DIR),
        )
        for _ in range(30):
            if _port_open(FRONTEND_PORT):
                self.after(0, self._set_status, "Frontend ready  ✓")
                return
            time.sleep(1)
        raise RuntimeError("Frontend did not start within 30 seconds.")

    def _wait_ready(self) -> None:
        model = _read_env_model()
        self.after(0, self._set_status, f"DeweyCT is running  🟢", f"Model: {model}")
        self.after(0, self._progress.stop)
        self.after(0, lambda: self._open_btn.configure(state="normal"))
        # Auto-open browser
        time.sleep(0.5)
        webbrowser.open(FRONTEND_URL)

    def _fatal(self, msg: str) -> None:
        self._progress.stop()
        self._set_status("Startup failed", msg)
        messagebox.showerror(APP_NAME, f"DeweyCT could not start:\n\n{msg}", parent=self)

    # ── Shutdown ─────────────────────────────────────────────────────────────

    def _on_close(self) -> None:
        if messagebox.askyesno("Stop DeweyCT", "Stop DeweyCT and close all services?", parent=self):
            self._set_status("Shutting down…")
            _stop_all()
            self.destroy()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    USER_DATA_DIR.mkdir(parents=True, exist_ok=True)
    app = LauncherApp()
    app.mainloop()


if __name__ == "__main__":
    main()
