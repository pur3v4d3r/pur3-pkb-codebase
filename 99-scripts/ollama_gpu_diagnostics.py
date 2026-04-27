#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ollama_gpu_diagnostics.py — Diagnose Ollama GPU utilization issues on Windows.

Diagnoses why Ollama models run slowly or fail to load on an NVIDIA GPU
(RTX 4090 or other). Checks GPU visibility, VRAM availability, environment
variables, running model placement (GPU vs CPU), and Ollama configuration.

Usage:
    python ollama_gpu_diagnostics.py
    python ollama_gpu_diagnostics.py -v
    python ollama_gpu_diagnostics.py --show-log
    python ollama_gpu_diagnostics.py --show-log -v

Version:
    1.0.0

Python:
    >=3.10

Dependencies:
    stdlib only — no third-party packages required.

Author:
    Generated for RTX 4090 + Ollama diagnostics
"""
from __future__ import annotations

import argparse
import logging
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field

# ─────────────────────────────────────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────────────────────────────────────

__version__ = "1.0.0"

# Models the user likely has — (name, file_size_gb)
KNOWN_MODELS: list[tuple[str, float]] = [
    ("qwen3:30b",                                18.0),
    ("qwen3.6:27b",                              17.0),
    ("qwen2.5-coder:32b",                        19.0),
    ("deepseek-coder:33b",                       18.0),
    ("qwen2.5:32b",                              19.0),
    ("gpt-oss:20b",                              13.0),
    ("gemma3:27b-it-qat",                        18.0),
    ("qwen2.5:14b",                               9.0),
    ("qwen3:14b",                                 9.0),
    ("qwen2.5-coder:14b",                         9.0),
    ("gemma3:12b-it-qat",                         8.9),
    ("qwen3:8b",                                  5.2),
    ("deepseek-r1:8b",                            5.2),
    ("qwen2.5:7b-instruct-q5_K_M",               5.4),
    ("qwen2.5-coder:7b",                          4.7),
    ("mistral:7b",                                4.4),
    ("deepseek-coder:6.7b",                       3.8),
]

logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# Custom exceptions
# ─────────────────────────────────────────────────────────────────────────────

class DiagError(Exception):
    """Base exception for this script."""

class CommandNotFoundError(DiagError):
    """Raised when a required CLI tool is not on PATH."""

class CommandFailedError(DiagError):
    """Raised when a CLI command returns a non-zero exit code."""


# ─────────────────────────────────────────────────────────────────────────────
# Data types
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class GPUInfo:
    """Information about one NVIDIA GPU as reported by nvidia-smi."""
    index: int
    name: str
    vram_total_mb: int
    vram_used_mb: int
    vram_free_mb: int
    temperature_c: int
    utilization_pct: int
    driver_version: str
    cuda_version: str

    @property
    def vram_total_gb(self) -> float:
        return self.vram_total_mb / 1024

    @property
    def vram_used_gb(self) -> float:
        return self.vram_used_mb / 1024

    @property
    def vram_free_gb(self) -> float:
        return self.vram_free_mb / 1024


@dataclass
class RunningModel:
    """A model currently loaded in the Ollama runtime."""
    name: str
    size_gb: float
    processor: str   # e.g. "100% GPU", "100% CPU", "Mixed"


@dataclass
class DiagnosticResult:
    """All collected diagnostic data plus analysis outputs."""
    nvidia_smi_available: bool = False
    ollama_available: bool = False
    ollama_version: str = ""
    gpus: list[GPUInfo] = field(default_factory=list)
    running_models: list[RunningModel] = field(default_factory=list)
    env_vars: dict[str, str] = field(default_factory=dict)
    ollama_log_gpu_lines: list[str] = field(default_factory=list)
    issues: list[str] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)


# ─────────────────────────────────────────────────────────────────────────────
# Core business logic
# ─────────────────────────────────────────────────────────────────────────────

def estimate_vram_needed_gb(model_file_gb: float, context_tokens: int = 4096) -> float:
    """Estimate actual VRAM required to load and run a model.

    This is a heuristic — actual usage varies by quantization and context:
      - Weights load at roughly file size
      - KV cache adds ~0.5 GB per 4K context window per 14B params
      - Runtime overhead (CUDA kernels, activation buffers) ~ 10-15%

    Args:
        model_file_gb: On-disk size of the model in GB.
        context_tokens: Context window size in tokens.

    Returns:
        Estimated VRAM required in GB.
    """
    # NOTE: KV cache scales with both context length and model size
    kv_scale_factor = model_file_gb / 14.0   # normalised to 14B baseline
    kv_cache_gb = (context_tokens / 4096) * kv_scale_factor * 0.5
    overhead_gb = model_file_gb * 0.12       # ~12% runtime overhead
    return model_file_gb + kv_cache_gb + overhead_gb


def parse_nvidia_smi_output(stdout: str) -> list[GPUInfo]:
    """Parse CSV output from nvidia-smi --query-gpu into GPUInfo objects.

    Args:
        stdout: Raw stdout string from nvidia-smi.

    Returns:
        List of GPUInfo, one per physical GPU.
    """
    gpus: list[GPUInfo] = []
    for line in stdout.strip().splitlines():
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 9:
            logger.debug("Skipping malformed nvidia-smi line: %r", line)
            continue
        try:
            gpus.append(GPUInfo(
                index=int(parts[0]),
                name=parts[1],
                vram_total_mb=int(parts[2]),
                vram_used_mb=int(parts[3]),
                vram_free_mb=int(parts[4]),
                temperature_c=int(parts[5]),
                utilization_pct=int(parts[6]),
                driver_version=parts[7],
                cuda_version=parts[8],
            ))
        except (ValueError, IndexError) as e:
            logger.warning("Could not parse GPU line %r: %s", line, e)
    return gpus


def parse_ollama_ps_output(stdout: str) -> list[RunningModel]:
    """Parse the output of `ollama ps` into RunningModel objects.

    Args:
        stdout: Raw stdout from `ollama ps`.

    Returns:
        List of RunningModel instances.
    """
    models: list[RunningModel] = []
    lines = stdout.strip().splitlines()
    if len(lines) < 2:
        return models   # No models loaded

    for line in lines[1:]:    # Skip the header row
        if not line.strip():
            continue
        parts = line.split()

        name = parts[0] if parts else "unknown"

        # Extract size — look for a float followed by "GB" or "MB"
        size_gb = 0.0
        for i, tok in enumerate(parts):
            if tok.upper() in ("GB", "MB") and i > 0:
                try:
                    val = float(parts[i - 1])
                    size_gb = val if tok.upper() == "GB" else val / 1024
                except ValueError:
                    pass
            elif tok.upper().endswith("GB"):
                try:
                    size_gb = float(tok[:-2])
                except ValueError:
                    pass

        # Determine processor placement
        upper = line.upper()
        if "GPU" in upper and "CPU" not in upper:
            processor = "100% GPU"
        elif "CPU" in upper and "GPU" not in upper:
            processor = "100% CPU"
        elif "GPU" in upper and "CPU" in upper:
            processor = "Mixed GPU/CPU"
        else:
            processor = "Unknown"

        models.append(RunningModel(name=name, size_gb=size_gb, processor=processor))

    return models


def analyze(result: DiagnosticResult) -> None:
    """Run analysis on collected data, populating issues and recommendations.

    This is the core diagnostic engine. It operates on result in-place.

    Args:
        result: DiagnosticResult to analyze and annotate.
    """
    issues = result.issues
    recs = result.recommendations

    # ── 1. nvidia-smi ────────────────────────────────────────────────────────
    if not result.nvidia_smi_available:
        issues.append(
            "CRITICAL: nvidia-smi not found. NVIDIA drivers may not be installed."
        )
        recs.append(
            "Install NVIDIA drivers: https://www.nvidia.com/drivers\n"
            "After install, reboot and run: nvidia-smi"
        )
        return

    if not result.gpus:
        issues.append("CRITICAL: nvidia-smi ran but reported no GPUs.")
        recs.append(
            "Check Windows Device Manager for GPU status.\n"
            "Try: nvidia-smi -L   to list physical GPUs."
        )

    # ── 2. Baseline VRAM consumption ────────────────────────────────────────
    for gpu in result.gpus:
        if gpu.vram_used_gb > 4.0:
            issues.append(
                f"HIGH BASELINE VRAM: GPU {gpu.index} ({gpu.name}) has "
                f"{gpu.vram_used_gb:.1f} GB already in use before any Ollama model. "
                f"This can prevent large models from loading."
            )
            recs.append(
                f"Free VRAM by closing GPU-accelerated apps:\n"
                f"  • Chrome / Edge (disable GPU acceleration in settings)\n"
                f"  • Discord (Settings → Advanced → Hardware Acceleration OFF)\n"
                f"  • Any games or other ML processes\n"
                f"  Currently using {gpu.vram_used_gb:.1f} GB / {gpu.vram_total_gb:.1f} GB"
            )

    # ── 3. Environment variables ─────────────────────────────────────────────
    env = result.env_vars

    cuda_vis = env.get("CUDA_VISIBLE_DEVICES", "NOT SET")
    if cuda_vis in ("", "-1"):
        issues.append(
            f"CUDA_VISIBLE_DEVICES={cuda_vis!r} — this HIDES ALL GPUs from CUDA apps "
            f"including Ollama. This is almost certainly why models run on CPU."
        )
        recs.append(
            "Fix CUDA_VISIBLE_DEVICES (run in PowerShell, then restart Ollama):\n"
            "  Remove-Item Env:CUDA_VISIBLE_DEVICES\n"
            "  — or —\n"
            "  $env:CUDA_VISIBLE_DEVICES = '0'"
        )

    num_gpu = env.get("OLLAMA_NUM_GPU", "NOT SET")
    if num_gpu == "0":
        issues.append(
            "OLLAMA_NUM_GPU=0 forces Ollama into CPU-only mode. "
            "This is the #1 cause of unexpectedly slow inference."
        )
        recs.append(
            "Fix OLLAMA_NUM_GPU (run in PowerShell, then restart Ollama):\n"
            "  Remove-Item Env:OLLAMA_NUM_GPU\n"
            "  — or force all layers to GPU —\n"
            "  $env:OLLAMA_NUM_GPU = '-1'"
        )

    # ── 4. Running model placement ───────────────────────────────────────────
    for model in result.running_models:
        if "CPU" in model.processor and "GPU" not in model.processor:
            issues.append(
                f"'{model.name}' is running entirely on CPU ({model.processor}). "
                f"Expected 80–100 tok/s on RTX 4090; CPU gives ~2–5 tok/s."
            )
            recs.append(
                f"To fix '{model.name}' running on CPU:\n"
                f"  1. Stop model:        ollama stop {model.name}\n"
                f"  2. Restart service:   (Task Manager → Services → Ollama → Restart)\n"
                f"  3. Check env vars:    $env:OLLAMA_NUM_GPU  and  $env:CUDA_VISIBLE_DEVICES\n"
                f"  4. Reload model:      ollama run {model.name}\n"
                f"  5. Watch GPU:         nvidia-smi dmon -s u -d 1"
            )
        elif "Mixed" in model.processor:
            issues.append(
                f"'{model.name}' is split between GPU and CPU (partial offload). "
                f"Performance will be severely degraded — CPU layers bottleneck the whole pipeline."
            )
            recs.append(
                f"'{model.name}' is partially on CPU. Free more VRAM so all layers fit on GPU:\n"
                f"  1. Close GPU-accelerated apps (Chrome, Discord, etc.)\n"
                f"  2. Restart Ollama service\n"
                f"  3. Check free VRAM: nvidia-smi --query-gpu=memory.free --format=csv"
            )

    # ── 5. Ollama log GPU detection ──────────────────────────────────────────
    log_text = "\n".join(result.ollama_log_gpu_lines).lower()
    if "no gpu" in log_text or "cpu only" in log_text:
        issues.append(
            "Ollama server log contains 'no gpu' or 'cpu only' — Ollama could not detect "
            "your NVIDIA GPU at startup."
        )
        recs.append(
            "Ollama failed GPU detection. Steps to fix:\n"
            "  1. Verify CUDA is installed: nvcc --version\n"
            "  2. Verify driver version supports your CUDA: nvidia-smi\n"
            "  3. Reinstall Ollama (it bundles its own CUDA libs)\n"
            "  4. Check log: %USERPROFILE%\\.ollama\\logs\\server.log"
        )

    # ── 6. Ollama not found ──────────────────────────────────────────────────
    if not result.ollama_available:
        issues.append("CRITICAL: 'ollama' is not on PATH.")
        recs.append(
            "Install Ollama: https://ollama.com/download\n"
            "After install, restart your terminal."
        )

    # ── 7. No issues found ───────────────────────────────────────────────────
    if not issues:
        recs.append(
            "No configuration issues detected. Next steps:\n"
            "  1. Run 'ollama run qwen2.5:7b-instruct-q5_K_M \"say hello\"' and\n"
            "     simultaneously watch: nvidia-smi dmon -s u -d 1\n"
            "  2. If GPU util stays at 0%, check the Ollama server log for errors\n"
            "  3. Consider reinstalling Ollama if GPU detection still fails"
        )


# ─────────────────────────────────────────────────────────────────────────────
# I/O layer
# ─────────────────────────────────────────────────────────────────────────────

def run_cmd(cmd: list[str], timeout: int = 15) -> tuple[str, str, int]:
    """Run a subprocess command safely.

    Args:
        cmd: Command and arguments.
        timeout: Max seconds to wait.

    Returns:
        Tuple of (stdout, stderr, returncode).
    """
    try:
        r = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
        )
        return r.stdout, r.stderr, r.returncode
    except FileNotFoundError:
        return "", f"{cmd[0]!r} not found on PATH", 127
    except subprocess.TimeoutExpired:
        return "", f"Timed out after {timeout}s", -1


def collect_diagnostics() -> DiagnosticResult:
    """Gather all diagnostic data from the system.

    Returns:
        A populated DiagnosticResult ready for analysis.
    """
    result = DiagnosticResult()

    # ── GPU info via nvidia-smi ──────────────────────────────────────────────
    if shutil.which("nvidia-smi"):
        stdout, stderr, rc = run_cmd([
            "nvidia-smi",
            "--query-gpu=index,name,memory.total,memory.used,memory.free,"
            "temperature.gpu,utilization.gpu,driver_version,cuda_version",
            "--format=csv,noheader,nounits",
        ])
        if rc == 0:
            result.gpus = parse_nvidia_smi_output(stdout)
            result.nvidia_smi_available = True
            logger.info("Detected %d GPU(s).", len(result.gpus))
        else:
            logger.error("nvidia-smi failed (rc=%d): %s", rc, stderr.strip())
            result.nvidia_smi_available = True  # found but errored
    else:
        logger.warning("nvidia-smi not on PATH.")
        result.nvidia_smi_available = False

    # ── Ollama version + running models ─────────────────────────────────────
    if shutil.which("ollama"):
        result.ollama_available = True
        stdout, _, rc = run_cmd(["ollama", "--version"])
        result.ollama_version = stdout.strip() if rc == 0 else "unknown"

        stdout, _, rc = run_cmd(["ollama", "ps"])
        if rc == 0:
            result.running_models = parse_ollama_ps_output(stdout)
        else:
            logger.warning("'ollama ps' failed — is the Ollama service running?")
    else:
        result.ollama_available = False

    # ── Environment variables ────────────────────────────────────────────────
    result.env_vars = {
        var: os.environ.get(var, "NOT SET")
        for var in [
            "CUDA_VISIBLE_DEVICES",
            "OLLAMA_NUM_GPU",
            "OLLAMA_GPU_OVERHEAD",
            "OLLAMA_MAX_LOADED_MODELS",
            "OLLAMA_KEEP_ALIVE",
            "OLLAMA_HOST",
            "OLLAMA_DEBUG",
            "OLLAMA_MODELS",
        ]
    }

    # ── Ollama server log (GPU-relevant lines) ───────────────────────────────
    log_path = os.path.join(
        os.environ.get("USERPROFILE", os.path.expanduser("~")),
        ".ollama", "logs", "server.log",
    )
    try:
        with open(log_path, encoding="utf-8", errors="replace") as fh:
            all_lines = fh.readlines()
        gpu_keywords = ("gpu", "cuda", "vram", "offload", "error", "warn", "no gpu", "cpu only")
        result.ollama_log_gpu_lines = [
            line.rstrip()
            for line in all_lines[-200:]   # only scan the last 200 lines
            if any(kw in line.lower() for kw in gpu_keywords)
        ]
    except FileNotFoundError:
        logger.info("Ollama server log not found at %r", log_path)
    except PermissionError:
        logger.warning("Cannot read Ollama log at %r — permission denied", log_path)

    # ── Analysis ─────────────────────────────────────────────────────────────
    analyze(result)

    return result


# ─────────────────────────────────────────────────────────────────────────────
# Report printing
# ─────────────────────────────────────────────────────────────────────────────

def _bar(used: float, total: float, width: int = 32) -> str:
    """Render a simple ASCII progress bar."""
    if total <= 0:
        return "░" * width
    filled = int(width * used / total)
    return "█" * filled + "░" * (width - filled)


def print_report(result: DiagnosticResult, show_log: bool = False) -> None:
    """Print the full diagnostic report to stdout.

    Args:
        result: Populated DiagnosticResult.
        show_log: If True, include GPU-relevant Ollama log lines.
    """
    W = 72

    def section(title: str) -> None:
        print(f"\n{'═' * W}")
        print(f"  {title}")
        print(f"{'═' * W}")

    section("OLLAMA GPU DIAGNOSTICS  v" + __version__)
    print(f"  Ollama        : {result.ollama_version or ('found' if result.ollama_available else 'NOT FOUND')}")
    print(f"  nvidia-smi    : {'available' if result.nvidia_smi_available else 'NOT FOUND — drivers not installed?'}")

    # ── GPU info ─────────────────────────────────────────────────────────────
    section("GPU INFORMATION")
    if not result.gpus:
        print("  ✗ No GPUs detected!")
    for gpu in result.gpus:
        pct = gpu.vram_used_mb / gpu.vram_total_mb * 100 if gpu.vram_total_mb else 0
        print(f"\n  GPU {gpu.index}: {gpu.name}")
        print(f"  Driver: {gpu.driver_version}  |  CUDA Runtime: {gpu.cuda_version}")
        print(f"  Temp:   {gpu.temperature_c}°C  |  GPU Util: {gpu.utilization_pct}%")
        print(f"  VRAM:   [{_bar(gpu.vram_used_mb, gpu.vram_total_mb)}] {pct:.0f}%")
        print(f"          Used : {gpu.vram_used_gb:.2f} GB")
        print(f"          Free : {gpu.vram_free_gb:.2f} GB")
        print(f"          Total: {gpu.vram_total_gb:.1f} GB")

    # ── VRAM fit analysis ─────────────────────────────────────────────────────
    section("VRAM FIT ANALYSIS FOR YOUR MODELS")
    if result.gpus:
        gpu = result.gpus[0]
        total = gpu.vram_total_gb
        free  = gpu.vram_free_gb
        print(f"\n  Your GPU: {gpu.name}  ({total:.0f} GB total, {free:.1f} GB currently free)")
        print(f"\n  {'Model':<42} {'File':>6}  {'Est.VRAM':>9}  Status")
        print(f"  {'-'*42} {'-'*6}  {'-'*9}  {'-'*22}")
        for name, file_gb in KNOWN_MODELS:
            needed = estimate_vram_needed_gb(file_gb)
            if needed <= free:
                status = "✓ fits NOW"
            elif needed <= total:
                status = "⚠ fits if VRAM freed"
            else:
                status = "✗ too large for GPU"
            print(f"  {name:<42} {file_gb:>5.1f}G  {needed:>7.1f} GB  {status}")
    else:
        print("  (Cannot calculate — no GPU data)")

    # ── Currently loaded models ───────────────────────────────────────────────
    section("CURRENTLY LOADED MODELS  (ollama ps)")
    if not result.running_models:
        print("  No models currently loaded.")
    for m in result.running_models:
        if "100% GPU" in m.processor:
            icon = "✓ GPU"
        elif "CPU" in m.processor:
            icon = "✗ CPU  ← SLOW!"
        else:
            icon = "⚠ Mixed ← degraded"
        print(f"  {m.name:<40} {m.size_gb:.1f} GB  [{m.processor}]  {icon}")

    # ── Environment variables ─────────────────────────────────────────────────
    section("ENVIRONMENT VARIABLES")
    warning_vars = {
        "CUDA_VISIBLE_DEVICES": ("", "-1"),
        "OLLAMA_NUM_GPU": ("0",),
    }
    for var, val in result.env_vars.items():
        warn = ""
        if var in warning_vars and val in warning_vars[var]:
            warn = "  ← !! BLOCKING GPU !!"
        print(f"  {var:<35} = {val}{warn}")

    # ── Issues ────────────────────────────────────────────────────────────────
    section("DETECTED ISSUES")
    if not result.issues:
        print("  ✓ No critical issues detected.")
    for i, issue in enumerate(result.issues, 1):
        print(f"\n  [{i}] ⚠  {issue}")

    # ── Recommendations ───────────────────────────────────────────────────────
    section("RECOMMENDATIONS")
    if not result.recommendations:
        print("  System looks correctly configured.")
    for i, rec in enumerate(result.recommendations, 1):
        lines = rec.splitlines()
        print(f"\n  [{i}] {lines[0]}")
        for line in lines[1:]:
            print(f"      {line}")

    # ── Quick commands ────────────────────────────────────────────────────────
    section("QUICK COMMANDS — run these while a model is loading")
    print("""
  # Watch GPU util live (run in a second terminal):
  nvidia-smi dmon -s u -d 1

  # Watch VRAM live:
  nvidia-smi --query-gpu=memory.used,memory.free --format=csv -l 1

  # Force GPU for Ollama (PowerShell — run before starting Ollama):
  $env:OLLAMA_NUM_GPU = '-1'

  # Remove a blocking env var (PowerShell):
  Remove-Item Env:CUDA_VISIBLE_DEVICES
  Remove-Item Env:OLLAMA_NUM_GPU

  # Check Ollama sees GPU on startup:
  Select-String -Path "$env:USERPROFILE\\.ollama\\logs\\server.log" `
    -Pattern "gpu|cuda|offload" | Select-Object -Last 20

  # Inference speed test (should be 80-100+ tok/s on RTX 4090):
  ollama run qwen3:8b "count from 1 to 20, no commentary"
""")

    # ── Ollama log ────────────────────────────────────────────────────────────
    if show_log:
        section("OLLAMA SERVER LOG — GPU/CUDA relevant lines")
        if not result.ollama_log_gpu_lines:
            print("  (no GPU-related lines found, or log not accessible)")
        for line in result.ollama_log_gpu_lines[-60:]:
            print(f"  {line}")


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="ollama_gpu_diagnostics",
        description=(
            "Diagnose why Ollama models run slowly or fail to load "
            "on an NVIDIA GPU (RTX 4090 / Windows)."
        ),
        epilog=(
            "Examples:\n"
            "  python ollama_gpu_diagnostics.py\n"
            "  python ollama_gpu_diagnostics.py -v\n"
            "  python ollama_gpu_diagnostics.py --show-log\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="increase logging verbosity (-v = INFO, -vv = DEBUG)")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="suppress progress messages; show issues only")
    parser.add_argument("--show-log", action="store_true",
                        help="include GPU-relevant lines from Ollama server log")
    return parser


def configure_logging(verbosity: int, quiet: bool) -> None:
    """Configure root logger from CLI flags."""
    if quiet:
        level = logging.ERROR
    elif verbosity >= 2:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)-8s] %(message)s",
        datefmt="%H:%M:%S",
    )


def main(argv: list[str] | None = None) -> int:
    """Main entry point.

    Args:
        argv: CLI arguments (defaults to sys.argv[1:]).

    Returns:
        Exit code: 0 = no issues, 1 = issues found, 2 = critical issue, 130 = interrupted.
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    try:
        print("Collecting diagnostics…")
        result = collect_diagnostics()
        print_report(result, show_log=args.show_log)

        if any("CRITICAL" in iss for iss in result.issues):
            return 2
        return 1 if result.issues else 0

    except KeyboardInterrupt:
        print("\nInterrupted.")
        return 130
    except Exception:
        logger.exception("Unexpected error")
        return 1


if __name__ == "__main__":
    sys.exit(main())
