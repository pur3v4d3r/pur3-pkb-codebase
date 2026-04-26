#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""install_all_themes.py — Bulk-install generated V4D3R variants into Obsidian.

Walks ``999-obsidian-themes/`` for ``V4D3R-*`` variant directories produced
by ``generate_color_variants_v2.py`` and copies (or moves) the inner theme
folder of each into the vault's ``.obsidian/themes/`` directory. Optionally
also installs CSS snippets into ``.obsidian/snippets/``.

A variant directory looks like::

    V4D3R-Teal/
    ├── preview.svg
    ├── snippets/
    │   └── *.css
    └── V4D3R Teal/                ← this is the installable Obsidian theme
        ├── manifest.json
        ├── README.md
        └── theme.css

Usage:
    python install_all_themes.py                        # copy all to .obsidian/themes
    python install_all_themes.py --dry-run              # preview only
    python install_all_themes.py --move                 # move instead of copy
    python install_all_themes.py --with-snippets        # also install snippets
    python install_all_themes.py --pattern "V4D3R-T*"   # subset by glob
    python install_all_themes.py --vault /path/to/vault # explicit vault root

Version:
    1.0.0

Python:
    >=3.10

Dependencies:
    Standard library only.
"""
from __future__ import annotations

import argparse
import logging
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

# ═════════════════════════════════════════════════════════════════════════
# Constants
# ═════════════════════════════════════════════════════════════════════════

__version__ = "1.0.0"

DEFAULT_VAULT_ROOT = Path(r"D:\10_pur3v4d3r's-vault")
DEFAULT_VARIANTS_DIR_REL = Path("999-obsidian-themes")
THEMES_SUBDIR = Path(".obsidian") / "themes"
SNIPPETS_SUBDIR = Path(".obsidian") / "snippets"
VARIANT_PREFIX = "V4D3R-"


# ═════════════════════════════════════════════════════════════════════════
# Logging
# ═════════════════════════════════════════════════════════════════════════

logger = logging.getLogger(__name__)


# ═════════════════════════════════════════════════════════════════════════
# Custom exceptions
# ═════════════════════════════════════════════════════════════════════════

class InstallError(Exception):
    """Base exception for installer errors."""


class VaultNotFoundError(InstallError):
    """Raised when the vault root or its .obsidian directory is missing."""


# ═════════════════════════════════════════════════════════════════════════
# Data types
# ═════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class VariantPaths:
    """Resolved paths for a single variant about to be installed.

    Attributes:
        outer: The ``V4D3R-{Slug}`` directory under ``999-obsidian-themes``.
        inner: The installable ``V4D3R {Name}`` subfolder containing
            ``manifest.json`` and ``theme.css``.
        snippets_src: The ``snippets/`` subfolder of the variant
            (may be missing — set to ``None`` if absent).
    """
    outer: Path
    inner: Path
    snippets_src: Path | None


# ═════════════════════════════════════════════════════════════════════════
# Discovery
# ═════════════════════════════════════════════════════════════════════════

def find_variants(variants_dir: Path, pattern: str) -> list[VariantPaths]:
    """Locate every ``V4D3R-*`` variant directory matching ``pattern``.

    Args:
        variants_dir: Root containing the ``V4D3R-*`` directories.
        pattern: Glob pattern relative to ``variants_dir`` (e.g. ``V4D3R-*``).

    Returns:
        A list of resolved ``VariantPaths``. Variants missing the inner
        installable folder are skipped with a warning.
    """
    found: list[VariantPaths] = []
    for outer in sorted(variants_dir.glob(pattern)):
        if not outer.is_dir() or not outer.name.startswith(VARIANT_PREFIX):
            continue
        # Inner folder has a space and matches the variant suffix
        candidates = [p for p in outer.iterdir()
                      if p.is_dir() and (p / "manifest.json").exists()]
        if not candidates:
            logger.warning("Skipping %s: no inner theme folder with manifest.json", outer.name)
            continue
        if len(candidates) > 1:
            logger.warning("Multiple inner folders in %s; using %s",
                           outer.name, candidates[0].name)
        snippets = outer / "snippets"
        found.append(VariantPaths(
            outer=outer,
            inner=candidates[0],
            snippets_src=snippets if snippets.is_dir() else None,
        ))
    return found


# ═════════════════════════════════════════════════════════════════════════
# Install operations
# ═════════════════════════════════════════════════════════════════════════

def install_one(
    variant: VariantPaths,
    themes_dir: Path,
    snippets_dir: Path | None,
    move: bool,
    overwrite: bool,
    dry_run: bool,
) -> tuple[int, int]:
    """Install a single variant into the vault.

    Args:
        variant: The resolved variant paths.
        themes_dir: Destination ``.obsidian/themes`` directory.
        snippets_dir: Destination ``.obsidian/snippets`` if snippets are
            being installed; ``None`` to skip snippets.
        move: If True, move the inner theme; if False, copy.
        overwrite: If True, replace any existing destination folder.
        dry_run: If True, log what would happen but make no changes.

    Returns:
        ``(themes_installed, snippets_installed)`` — counts (0 or 1 themes,
        0+ snippet files).
    """
    target = themes_dir / variant.inner.name
    op = "MOVE" if move else "COPY"

    if target.exists():
        if not overwrite:
            logger.warning("Skip %s — already installed (use --overwrite)", target.name)
            return 0, 0
        if dry_run:
            logger.info("[dry-run] Would remove existing %s", target)
        else:
            shutil.rmtree(target)

    if dry_run:
        logger.info("[dry-run] %s %s → %s", op, variant.inner, target)
    else:
        if move:
            shutil.move(str(variant.inner), str(target))
        else:
            shutil.copytree(variant.inner, target)
        logger.info("%s installed: %s", op.title(), target.name)

    snippets_installed = 0
    if snippets_dir is not None and variant.snippets_src is not None:
        for snip in sorted(variant.snippets_src.glob("*.css")):
            dest = snippets_dir / snip.name
            if dest.exists() and not overwrite:
                continue
            if dry_run:
                logger.info("[dry-run] copy snippet %s", snip.name)
            else:
                shutil.copy2(snip, dest)
            snippets_installed += 1

    return 1, snippets_installed


def install_all(
    variants: list[VariantPaths],
    themes_dir: Path,
    snippets_dir: Path | None,
    move: bool,
    overwrite: bool,
    dry_run: bool,
) -> tuple[int, int, int]:
    """Install every variant.

    Returns:
        ``(themes_installed, snippets_installed, errors)``.
    """
    if not dry_run:
        themes_dir.mkdir(parents=True, exist_ok=True)
        if snippets_dir is not None:
            snippets_dir.mkdir(parents=True, exist_ok=True)

    themes_total = 0
    snippets_total = 0
    errors = 0
    for v in variants:
        try:
            t, s = install_one(v, themes_dir, snippets_dir, move, overwrite, dry_run)
            themes_total += t
            snippets_total += s
        except (OSError, shutil.Error) as e:
            logger.error("Failed to install %s: %s", v.inner.name, e)
            errors += 1
    return themes_total, snippets_total, errors


# ═════════════════════════════════════════════════════════════════════════
# CLI
# ═════════════════════════════════════════════════════════════════════════

def build_parser() -> argparse.ArgumentParser:
    """Construct the argument parser."""
    p = argparse.ArgumentParser(
        prog="install_all_themes",
        description="Bulk-install generated V4D3R color variants into Obsidian.",
        epilog=(
            "Examples:\n"
            "  install_all_themes.py                          # copy every variant\n"
            "  install_all_themes.py --dry-run                # preview only\n"
            "  install_all_themes.py --move --overwrite       # move + replace existing\n"
            "  install_all_themes.py --with-snippets          # also install snippets\n"
            "  install_all_themes.py --pattern 'V4D3R-T*'     # subset by glob\n"
            "  install_all_themes.py --vault D:\\my\\vault     # explicit vault root\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    p.add_argument("-v", "--verbose", action="count", default=0,
                   help="increase logging verbosity (-v, -vv)")
    p.add_argument("-q", "--quiet", action="store_true",
                   help="suppress non-error output")
    p.add_argument("-n", "--dry-run", action="store_true",
                   help="preview actions; make no changes")
    p.add_argument("--vault", type=Path, default=DEFAULT_VAULT_ROOT,
                   help=f"vault root (default: {DEFAULT_VAULT_ROOT})")
    p.add_argument("--variants-dir", type=Path, default=None,
                   help=f"variants directory (default: VAULT/{DEFAULT_VARIANTS_DIR_REL})")
    p.add_argument("--pattern", default=f"{VARIANT_PREFIX}*",
                   help=f"glob pattern for variant dirs (default: {VARIANT_PREFIX}*)")
    p.add_argument("--move", action="store_true",
                   help="move inner theme folders instead of copying "
                        "(removes them from the variants directory)")
    p.add_argument("--overwrite", action="store_true",
                   help="replace any existing destination theme folder")
    p.add_argument("--with-snippets", action="store_true",
                   help="also install per-variant CSS snippets into .obsidian/snippets")
    return p


def configure_logging(verbosity: int, quiet: bool) -> None:
    """Configure root logger from CLI verbosity flags."""
    if quiet:
        level = logging.ERROR
    elif verbosity >= 2:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.INFO  # Default to INFO so users see progress
    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s",
    )


def main(argv: list[str] | None = None) -> int:
    """Main entry point.

    Exit codes:
        0: success
        1: uncaught error
        2: vault or variants directory not found
        3: no variants matched
        4: one or more install operations failed
        130: interrupted (Ctrl+C)
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    configure_logging(args.verbose, args.quiet)

    try:
        vault: Path = args.vault.resolve()
        if not vault.is_dir():
            raise VaultNotFoundError(f"Vault not found: {vault}")

        themes_dir = vault / THEMES_SUBDIR
        if not themes_dir.parent.is_dir():
            raise VaultNotFoundError(
                f"Not an Obsidian vault (no .obsidian/): {vault}"
            )

        variants_dir: Path = (args.variants_dir.resolve() if args.variants_dir
                              else vault / DEFAULT_VARIANTS_DIR_REL)
        if not variants_dir.is_dir():
            raise VaultNotFoundError(f"Variants dir not found: {variants_dir}")

        snippets_dir = vault / SNIPPETS_SUBDIR if args.with_snippets else None

        variants = find_variants(variants_dir, args.pattern)
        if not variants:
            logger.error("No variants matched %r in %s", args.pattern, variants_dir)
            return 3

        action = "Moving" if args.move else "Copying"
        mode = " (DRY RUN)" if args.dry_run else ""
        logger.info("%s %d variant(s) → %s%s", action, len(variants), themes_dir, mode)
        if snippets_dir is not None:
            logger.info("Snippets target: %s", snippets_dir)

        themes_n, snippets_n, errors = install_all(
            variants, themes_dir, snippets_dir,
            move=args.move, overwrite=args.overwrite, dry_run=args.dry_run,
        )

        logger.info("Done. Themes: %d   Snippets: %d   Errors: %d",
                    themes_n, snippets_n, errors)
        if errors:
            return 4
        return 0

    except VaultNotFoundError as e:
        logger.error("%s", e)
        return 2
    except KeyboardInterrupt:
        logger.warning("Interrupted by user")
        return 130
    except Exception:
        logger.exception("Unexpected error")
        return 1


# ═════════════════════════════════════════════════════════════════════════
# Entry-point guard
# ═════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    sys.exit(main())
