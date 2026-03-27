#!/usr/bin/env python3
"""
pipeline_logger.py — Structured Logging for the PKB Pipeline
═══════════════════════════════════════════════════════════════════════════════
Provides a unified logging interface that writes:
  1. Human-readable console output (with colour/emoji indicators)
  2. Machine-readable JSON log file (for post-run analysis)

USAGE:
  from pipeline_logger import get_logger

  log = get_logger("stage_extract")
  log.info("Processing batch", batch="first-principles", files=12)
  log.warn("Missing frontmatter", file="note.md")
  log.error("Parse failed", file="bad.json", reason="invalid JSON")
  log.stage_start(1, "Extraction")
  log.stage_end(1, "Extraction", success=True, duration=4.2)

REQUIRES: Python 3.10+ (stdlib only)
"""

import io
import json
import sys
import datetime
from pathlib import Path
from dataclasses import dataclass, field, asdict

# ══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

_PIPELINE_DIR = Path(__file__).parent
_LOG_DIR = _PIPELINE_DIR / "_pipeline-output" / "logs"
_LOG_DIR.mkdir(parents=True, exist_ok=True)

# Log level hierarchy
LEVELS = {"DEBUG": 10, "INFO": 20, "WARN": 30, "ERROR": 40, "STAGE": 50}

# Console level threshold (show INFO and above by default)
CONSOLE_LEVEL = LEVELS["INFO"]

# Emoji prefixes for console output
_LEVEL_PREFIX = {
    "DEBUG": "  🔍",
    "INFO":  "  ℹ️ ",
    "WARN":  "  ⚠️ ",
    "ERROR": "  ❌",
    "STAGE": "  📋",
}


# ══════════════════════════════════════════════════════════════════════════════
# LOG ENTRY
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class LogEntry:
    """A single structured log entry."""
    timestamp: str
    level: str
    source: str
    message: str
    data: dict = field(default_factory=dict)

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)

    def to_console(self) -> str:
        prefix = _LEVEL_PREFIX.get(self.level, "  ")
        extra = ""
        if self.data:
            kv = " ".join(f"{k}={v}" for k, v in self.data.items())
            extra = f"  [{kv}]"
        return f"{prefix} [{self.source}] {self.message}{extra}"


# ══════════════════════════════════════════════════════════════════════════════
# LOGGER
# ══════════════════════════════════════════════════════════════════════════════

class PipelineLogger:
    """Structured logger with console + JSON file output."""

    def __init__(self, source: str, log_file: Path | None = None,
                 console_level: int = CONSOLE_LEVEL):
        self.source = source
        self.console_level = console_level
        self._entries: list[LogEntry] = []
        self._log_file = log_file
        self._file_handle = None
        if log_file:
            log_file.parent.mkdir(parents=True, exist_ok=True)
            self._file_handle = open(log_file, "a", encoding="utf-8")

    def _log(self, level: str, message: str, **kwargs) -> None:
        entry = LogEntry(
            timestamp=datetime.datetime.now().isoformat(),
            level=level,
            source=self.source,
            message=message,
            data=kwargs,
        )
        self._entries.append(entry)

        # Console output
        if LEVELS.get(level, 0) >= self.console_level:
            try:
                print(entry.to_console())
            except UnicodeEncodeError:
                print(entry.to_console().encode("ascii", "replace").decode())

        # JSON file output
        if self._file_handle:
            self._file_handle.write(entry.to_json() + "\n")
            self._file_handle.flush()

    def debug(self, message: str, **kwargs) -> None:
        self._log("DEBUG", message, **kwargs)

    def info(self, message: str, **kwargs) -> None:
        self._log("INFO", message, **kwargs)

    def warn(self, message: str, **kwargs) -> None:
        self._log("WARN", message, **kwargs)

    def error(self, message: str, **kwargs) -> None:
        self._log("ERROR", message, **kwargs)

    def stage_start(self, num: int, name: str) -> None:
        self._log("STAGE", f"▶ Stage {num}: {name} — STARTED", stage=num)

    def stage_end(self, num: int, name: str, success: bool,
                  duration: float = 0.0, **kwargs) -> None:
        status = "✓ PASSED" if success else "✗ FAILED"
        self._log("STAGE", f"■ Stage {num}: {name} — {status} ({duration:.1f}s)",
                  stage=num, success=success, duration=duration, **kwargs)

    def get_entries(self, level: str | None = None) -> list[LogEntry]:
        """Get all log entries, optionally filtered by level."""
        if level:
            target = LEVELS.get(level, 0)
            return [e for e in self._entries if LEVELS.get(e.level, 0) >= target]
        return list(self._entries)

    def close(self) -> None:
        if self._file_handle:
            self._file_handle.close()
            self._file_handle = None


# ══════════════════════════════════════════════════════════════════════════════
# FACTORY
# ══════════════════════════════════════════════════════════════════════════════

_RUN_TIMESTAMP = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
_LOGGERS: dict[str, PipelineLogger] = {}


def get_logger(source: str, run_id: str | None = None) -> PipelineLogger:
    """Get or create a logger for the given source module."""
    if source not in _LOGGERS:
        rid = run_id or _RUN_TIMESTAMP
        log_file = _LOG_DIR / f"{rid}.jsonl"
        _LOGGERS[source] = PipelineLogger(source, log_file=log_file)
    return _LOGGERS[source]


def close_all() -> None:
    """Close all open loggers."""
    for logger in _LOGGERS.values():
        logger.close()
    _LOGGERS.clear()
