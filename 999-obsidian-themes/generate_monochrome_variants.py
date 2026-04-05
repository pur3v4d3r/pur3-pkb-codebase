#!/usr/bin/env python3
"""
V4D3R MONOCHROME SNIPPET GENERATOR
═══════════════════════════════════════════════════════════════════════════════

Generates 3 distinct Black-and-Grey snippet variants from the active Obsidian
snippets folder. All saturated (coloured) values are desaturated to their grey
equivalents; black and near-black backgrounds are left untouched.

VARIANTS GENERATED:
  ┌─────────────────────────────────────────────────────────────────────┐
  │ Charcoal  │ Neutral balanced grey. Neon accents → mid-grey #888–#CC │
  │ Ash       │ High contrast. Neon accents → near-white #B0–#F0        │
  │ Graphite  │ Dark compressed, subtle warm tint. Accents → #4A–#7A    │
  └─────────────────────────────────────────────────────────────────────┘

HOW CONVERSION WORKS:
  1. Hex (#RRGGBB), rgba(), and bare RGB triplet (--var: R, G, B) formats.
  2. Any color with HSL saturation >= sat_threshold is "coloured" and gets
     converted to its greyscale equivalent.
  3. Already-grey colors (low saturation) — including all dark backgrounds,
     surface colours, and text — are left completely unchanged.
  4. The new grey lightness is derived from the original lightness plus a
     variant-specific formula:
        new_l = clamp(orig_l * lightness_mult + sat_boost, 0.0, max_l)

USAGE:
    python generate_monochrome_variants.py              # all 3 variants
    python generate_monochrome_variants.py --variant charcoal
    python generate_monochrome_variants.py --variant ash
    python generate_monochrome_variants.py --variant graphite
    python generate_monochrome_variants.py --dry-run    # preview only
    python generate_monochrome_variants.py --install charcoal

REQUIREMENTS: Python 3.10+ (stdlib only — no pip installs needed)

@author   PKB Scripting Architect
@version  1.0.0
"""

import argparse
import colorsys
import re
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


# ═══════════════════════════════════════════════════════════════════════════════
# PATHS — adjust if your vault is in a different location
# ═══════════════════════════════════════════════════════════════════════════════

VAULT_ROOT   = Path(r"D:\10_pur3v4d3r's-vault")
SNIPPETS_SRC = VAULT_ROOT / ".obsidian" / "snippets"
OUTPUT_ROOT  = VAULT_ROOT / "999-obsidian-themes"


# ═══════════════════════════════════════════════════════════════════════════════
# VARIANT DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class MonoVariant:
    """Describes a monochrome conversion recipe."""
    name: str              # Display name, e.g. "Charcoal"
    slug: str              # File-safe slug, e.g. "charcoal"
    description: str       # For README and manifest

    # ── Conversion parameters ────────────────────────────────────────────────
    sat_threshold: float   # Min saturation to treat color as "coloured" (0–1)
    lightness_mult: float  # Multiplier applied to original HSL lightness
    sat_boost: float       # Added to lightness (rewards originally-saturated colors)
    max_l: float           # Hard cap on output lightness (0–1)

    # ── Optional tint ────────────────────────────────────────────────────────
    tint_hue: float = 0.0  # Hue for the residual tint (degrees, 0 = neutral)
    tint_sat: float = 0.0  # Saturation of the tint (0 = pure grey)
    # Tint is only applied for mid-range lightnesses (0.12 < new_l < 0.85)
    # so very dark and very bright values stay neutral.


VARIANTS: list[MonoVariant] = [

    # ── VARIANT 1: Charcoal ──────────────────────────────────────────────────
    # Neutral, balanced black-and-grey. Preserves the original lightness
    # relationships of accent colors without brightening or compressing.
    # Neon accents (~50% L): → ~#808080 (medium grey).
    # ─────────────────────────────────────────────────────────────────────────
    MonoVariant(
        name="Charcoal",
        slug="charcoal",
        description=(
            "Neutral balanced monochrome. "
            "Vibrant accent colours are converted to clean medium greys "
            "(~#808080–#CCCCCC). "
            "Dark backgrounds and text remain untouched. "
            "Classic black-and-grey look with balanced contrast."
        ),
        sat_threshold=0.06,
        lightness_mult=1.00,   # Preserve original lightness directly
        sat_boost=0.00,        # No artificial brightening
        max_l=0.88,            # Cap to avoid blown-out whites
        tint_hue=0.0,
        tint_sat=0.0,
    ),

    # ── VARIANT 2: Ash ───────────────────────────────────────────────────────
    # High-contrast variant. All accent colours are brightened towards white,
    # creating a dramatic light-grey / near-white on black aesthetic.
    # Neon accents (~50% L): → ~#B0B0B0–#EBEBEB.
    # ─────────────────────────────────────────────────────────────────────────
    MonoVariant(
        name="Ash",
        slug="ash",
        description=(
            "High-contrast monochrome. "
            "Accent colours are pushed towards light grey and near-white "
            "(~#B0B0B0–#EBEBEB) while backgrounds stay deep black. "
            "Creates a dramatic film-noir or blueprint aesthetic."
        ),
        sat_threshold=0.06,
        lightness_mult=1.00,
        sat_boost=0.35,        # Push converted colours towards white
        max_l=0.94,            # Allow near-white accents
        tint_hue=0.0,
        tint_sat=0.0,
    ),

    # ── VARIANT 3: Graphite ──────────────────────────────────────────────────
    # Dark, compressed palette with a subtle warm-grey tint.
    # Accent colours are darkened and muted, landing in the #404040–#707070
    # range for a refined, understated "brushed graphite" aesthetic.
    # ─────────────────────────────────────────────────────────────────────────
    MonoVariant(
        name="Graphite",
        slug="graphite",
        description=(
            "Dark compressed palette with a subtle warm-grey tint. "
            "Accent colours become muted, dark-to-mid greys (~#404040–#707070). "
            "Very understated and sophisticated — a brushed graphite / charcoal "
            "steel aesthetic with a hint of warmth."
        ),
        sat_threshold=0.06,
        lightness_mult=0.78,   # Compress everything downward
        sat_boost=0.00,
        max_l=0.72,            # Hard cap at medium grey
        tint_hue=22.0,         # Warm orange-grey hue
        tint_sat=0.04,         # 4% saturation — barely perceptible warmth
    ),
]


# ═══════════════════════════════════════════════════════════════════════════════
# COLOR UTILITIES
# ═══════════════════════════════════════════════════════════════════════════════

def rgb_to_hsl(r: int, g: int, b: int) -> tuple[float, float, float]:
    """Convert RGB (0-255) to HSL (h=0-360, s=0-1, l=0-1)."""
    rf, gf, bf = r / 255.0, g / 255.0, b / 255.0
    hue, lum, sat = colorsys.rgb_to_hls(rf, gf, bf)
    return hue * 360.0, sat, lum


def hsl_to_rgb(h: float, s: float, l: float) -> tuple[int, int, int]:
    """Convert HSL (h=0-360, s=0-1, l=0-1) to RGB (0-255)."""
    h_norm = (h % 360.0) / 360.0
    s = max(0.0, min(1.0, s))
    l = max(0.0, min(1.0, l))
    rf, gf, bf = colorsys.hls_to_rgb(h_norm, l, s)
    return (
        max(0, min(255, round(rf * 255))),
        max(0, min(255, round(gf * 255))),
        max(0, min(255, round(bf * 255))),
    )


def to_monochrome(r: int, g: int, b: int, variant: MonoVariant) -> tuple[int, int, int]:
    """
    Convert an RGB colour to its monochrome equivalent.

    Only transforms colours whose HSL saturation meets the variant's
    sat_threshold — leaving blacks, near-blacks, and existing greys untouched.
    """
    # Edge case: pure black / pure white — always leave unchanged
    if (r, g, b) in ((0, 0, 0), (255, 255, 255)):
        return r, g, b

    h, s, l = rgb_to_hsl(r, g, b)

    # Skip already-grey/black colours
    if s < variant.sat_threshold:
        return r, g, b

    # Compute new grey lightness
    new_l = l * variant.lightness_mult + variant.sat_boost
    new_l = max(0.0, min(variant.max_l, new_l))

    # Apply optional warm/cool tint — only in the mid-range
    if variant.tint_sat > 0.0 and 0.12 < new_l < 0.85:
        return hsl_to_rgb(variant.tint_hue, variant.tint_sat, new_l)

    # Pure grey
    return hsl_to_rgb(0.0, 0.0, new_l)


# ═══════════════════════════════════════════════════════════════════════════════
# HEX / RGBA HELPERS  (adapted from generate_color_variants.py)
# ═══════════════════════════════════════════════════════════════════════════════

def parse_hex(hex_str: str) -> Optional[tuple[int, int, int, Optional[int]]]:
    """Parse #RGB / #RGBA / #RRGGBB / #RRGGBBAA → (r, g, b, alpha|None)."""
    h = hex_str.lstrip("#")
    try:
        if len(h) == 3:
            r, g, b = int(h[0]*2, 16), int(h[1]*2, 16), int(h[2]*2, 16)
            return r, g, b, None
        elif len(h) == 4:
            return (int(h[0]*2, 16), int(h[1]*2, 16), int(h[2]*2, 16), int(h[3]*2, 16))
        elif len(h) == 6:
            return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), None
        elif len(h) == 8:
            return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16))
    except ValueError:
        pass
    return None


def rgb_to_hex(r: int, g: int, b: int,
               alpha: Optional[int] = None,
               lowercase: bool = True) -> str:
    if alpha is not None:
        s = f"#{r:02x}{g:02x}{b:02x}{alpha:02x}"
    else:
        s = f"#{r:02x}{g:02x}{b:02x}"
    return s if lowercase else s.upper()


# ═══════════════════════════════════════════════════════════════════════════════
# REGEX PATTERNS
# ═══════════════════════════════════════════════════════════════════════════════

RE_HEX = re.compile(r"#([0-9A-Fa-f]{3,4}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})\b")
RE_RGBA = re.compile(
    r"rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})"
    r"\s*(?:,\s*([0-9.]+)\s*)?\)"
)
# Matches  --css-var: R, G, B  at end of property line
RE_BARE_RGB = re.compile(
    r"(--[\w-]+\s*:\s*(?:/\*[^*]*\*/\s*)?)(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})"
    r"(?=\s*[;}\n])"
)


# ═══════════════════════════════════════════════════════════════════════════════
# CSS TRANSFORMATION
# ═══════════════════════════════════════════════════════════════════════════════

def _transform_hex(match: re.Match, variant: MonoVariant) -> str:
    parsed = parse_hex(match.group(0))
    if parsed is None:
        return match.group(0)
    r, g, b, alpha = parsed
    nr, ng, nb = to_monochrome(r, g, b, variant)
    if (nr, ng, nb) == (r, g, b):
        return match.group(0)               # unchanged — return original string
    was_upper = any(c.isupper() for c in match.group(1) if c.isalpha())
    return rgb_to_hex(nr, ng, nb, alpha, lowercase=not was_upper)


def _transform_rgba(match: re.Match, variant: MonoVariant) -> str:
    r, g, b = int(match.group(1)), int(match.group(2)), int(match.group(3))
    alpha_str = match.group(4)
    nr, ng, nb = to_monochrome(r, g, b, variant)
    if (nr, ng, nb) == (r, g, b):
        return match.group(0)
    if alpha_str is not None:
        return f"rgba({nr}, {ng}, {nb}, {alpha_str})"
    return f"rgb({nr}, {ng}, {nb})"


def _transform_bare_rgb(match: re.Match, variant: MonoVariant) -> str:
    prefix = match.group(1)
    r, g, b = int(match.group(2)), int(match.group(3)), int(match.group(4))
    nr, ng, nb = to_monochrome(r, g, b, variant)
    if (nr, ng, nb) == (r, g, b):
        return match.group(0)
    return f"{prefix}{nr}, {ng}, {nb}"


def transform_css(css: str, variant: MonoVariant) -> str:
    """Run all three regex passes over the CSS content."""
    css = RE_HEX.sub(lambda m: _transform_hex(m, variant), css)
    css = RE_RGBA.sub(lambda m: _transform_rgba(m, variant), css)
    css = RE_BARE_RGB.sub(lambda m: _transform_bare_rgb(m, variant), css)
    return css


def _count_changes(original: str, transformed: str) -> int:
    """Count lines that differ between original and transformed."""
    return sum(
        1 for a, b in zip(original.splitlines(), transformed.splitlines())
        if a != b
    ) + abs(len(original.splitlines()) - len(transformed.splitlines()))


# ═══════════════════════════════════════════════════════════════════════════════
# README GENERATOR
# ═══════════════════════════════════════════════════════════════════════════════

def _make_readme(variant: MonoVariant) -> str:
    return textwrap.dedent(f"""\
    # V4D3R {variant.name} — Black & Grey Snippet Set

    > {variant.description}

    ## Overview

    This snippet set was generated by `generate_monochrome_variants.py` from the
    live V4D3R snippets folder.  All saturated accent colours have been converted
    to greyscale; dark backgrounds, surfaces, and text colours are unchanged.

    **Variant:** {variant.name}  
    **Conversion:** sat_threshold={variant.sat_threshold}, lightness×{variant.lightness_mult}, boost+{variant.sat_boost}, max_l={variant.max_l}  
    {"**Warm tint:** hue=" + str(variant.tint_hue) + "°, sat=" + str(variant.tint_sat) if variant.tint_sat > 0 else "**Tint:** None (pure neutral grey)"}

    ## Installation

    1. Copy all `.css` files from this `snippets/` folder into your vault's  
       `.obsidian/snippets/` directory.
    2. In Obsidian: **Settings → Appearance → CSS Snippets** → enable the ones
       you want (same as your current setup, just with grey accents).

    ## Variants Comparison

    | Variant   | Character                       | Accent brightness            |
    |-----------|--------------------------------|------------------------------|
    | Charcoal  | Neutral balanced               | Medium grey  ~#808080–#CCCCCC |
    | Ash       | High contrast, near-white      | Light grey   ~#B0B0B0–#F0F0F0 |
    | Graphite  | Dark, compressed, warm-tinted  | Dark grey    ~#404040–#707070  |

    ## Notes

    - All callout types retain their structural CSS (borders, shadows, glows)
      but share similar grey shade ranges rather than distinct hue families.
    - To restore the original coloured set, switch back to the `.obsidian/snippets`
      copies or re-run the original `generate_color_variants.py`.
    """)


# ═══════════════════════════════════════════════════════════════════════════════
# GENERATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

def generate_variant(variant: MonoVariant, dry_run: bool = False) -> dict:
    """Generate one monochrome snippet variant.  Returns stats dict."""

    output_dir   = OUTPUT_ROOT / f"V4D3R-{variant.name}"
    snippets_dir = output_dir / "snippets"

    stats = {
        "variant": variant.name,
        "output_dir": str(output_dir),
        "files_written": 0,
        "files_unchanged": 0,
        "lines_changed": 0,
    }

    print(f"\n{'═' * 60}")
    print(f"  Variant : V4D3R {variant.name}")
    print(f"  Formula : L×{variant.lightness_mult} + {variant.sat_boost} (cap {variant.max_l})")
    if variant.tint_sat > 0:
        print(f"  Tint    : hue={variant.tint_hue}°, sat={variant.tint_sat} (warm grey)")
    else:
        print(f"  Tint    : none (pure neutral grey)")
    print(f"  Output  : {snippets_dir}")
    print(f"{'─' * 60}")

    if not dry_run:
        snippets_dir.mkdir(parents=True, exist_ok=True)

    snippet_files = sorted(SNIPPETS_SRC.glob("*.css"))
    if not snippet_files:
        print(f"  ✗ No .css files found in {SNIPPETS_SRC}")
        return stats

    for path in snippet_files:
        original = path.read_text(encoding="utf-8")
        transformed = transform_css(original, variant)
        n_changes = _count_changes(original, transformed)

        if not dry_run:
            (snippets_dir / path.name).write_text(transformed, encoding="utf-8")

        if n_changes > 0:
            print(f"  ✓ {path.name:<52} ({n_changes} lines changed)")
            stats["files_written"] += 1
            stats["lines_changed"] += n_changes
        else:
            stats["files_unchanged"] += 1

    if stats["files_unchanged"] > 0:
        print(f"  · {stats['files_unchanged']} snippet(s) had no coloured values — copied unchanged")

    # Write README
    if not dry_run:
        (output_dir / "README.md").write_text(_make_readme(variant), encoding="utf-8")
        print(f"  ✓ README.md")

    print(f"  ─── Total: {stats['lines_changed']} colour conversions across "
          f"{stats['files_written'] + stats['files_unchanged']} snippets ───")

    return stats


# ═══════════════════════════════════════════════════════════════════════════════
# INSTALL HELPER
# ═══════════════════════════════════════════════════════════════════════════════

def install_variant(slug: str) -> None:
    """Copy a generated variant's snippets into the active Obsidian snippets folder."""
    variant = next((v for v in VARIANTS if v.slug == slug), None)
    if not variant:
        print(f"Unknown variant '{slug}'. Available: {', '.join(v.slug for v in VARIANTS)}")
        sys.exit(1)

    src  = OUTPUT_ROOT / f"V4D3R-{variant.name}" / "snippets"
    dest = VAULT_ROOT / ".obsidian" / "snippets"

    if not src.exists():
        print(f"Variant '{slug}' not generated yet. Run generation first.")
        sys.exit(1)

    count = 0
    for f in src.glob("*.css"):
        dest_file = dest / f.name
        dest_file.write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
        count += 1

    print(f"\n✅ Installed {count} snippet files → {dest}")
    print(f"   Reload Obsidian or toggle snippets to see V4D3R {variant.name}.")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(
        description="V4D3R Monochrome Snippet Variant Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
        VARIANTS:
          charcoal   Neutral balanced monochrome (neons → mid-grey #808080–#CC)
          ash        High contrast (neons → near-white #B0–#F0)
          graphite   Dark compressed, warm tint (neons → dark-mid grey #40–#70)

        EXAMPLES:
          python generate_monochrome_variants.py
          python generate_monochrome_variants.py --variant charcoal
          python generate_monochrome_variants.py --dry-run
          python generate_monochrome_variants.py --install charcoal
        """),
    )
    parser.add_argument(
        "--variant", "-v", action="append", metavar="SLUG",
        choices=[v.slug for v in VARIANTS],
        help="Generate only this variant (can repeat). Default: all.",
    )
    parser.add_argument(
        "--dry-run", "-n", action="store_true",
        help="Show what would be generated without writing any files.",
    )
    parser.add_argument(
        "--install", "-i", metavar="SLUG",
        help="Copy a generated variant into your active .obsidian/snippets folder.",
    )
    parser.add_argument(
        "--list", "-l", action="store_true",
        help="List all available variants and exit.",
    )

    args = parser.parse_args()

    # ── List ──────────────────────────────────────────────────────────────────
    if args.list:
        print("\nAvailable monochrome variants:\n")
        for v in VARIANTS:
            print(f"  {v.slug:<12} {v.description}")
        print()
        return

    # ── Install ───────────────────────────────────────────────────────────────
    if args.install:
        install_variant(args.install)
        return

    # ── Validate source ───────────────────────────────────────────────────────
    if not SNIPPETS_SRC.exists():
        print(f"ERROR: Snippets source not found:\n  {SNIPPETS_SRC}")
        sys.exit(1)

    # ── Select variants ───────────────────────────────────────────────────────
    targets = (
        [v for v in VARIANTS if v.slug in args.variant]
        if args.variant
        else VARIANTS
    )

    # ── Header ────────────────────────────────────────────────────────────────
    mode = "DRY RUN (no files written)" if args.dry_run else "GENERATING FILES"
    print(f"\n{'═' * 60}")
    print(f"  V4D3R Monochrome Variant Generator — {mode}")
    print(f"  Source : {SNIPPETS_SRC}")
    print(f"  Output : {OUTPUT_ROOT}")
    print(f"{'═' * 60}")

    # ── Generate ──────────────────────────────────────────────────────────────
    all_stats = []
    for variant in targets:
        stats = generate_variant(variant, dry_run=args.dry_run)
        all_stats.append(stats)

    # ── Summary ───────────────────────────────────────────────────────────────
    print(f"\n{'═' * 60}")
    print(f"  SUMMARY")
    print(f"{'─' * 60}")
    total_lines = 0
    for s in all_stats:
        total_lines += s["lines_changed"]
        mode_tag = "[DRY RUN] " if args.dry_run else ""
        print(f"  {mode_tag}V4D3R {s['variant']:<12} → {s['output_dir']}")
        print(f"             {s['lines_changed']} colour conversions, "
              f"{s['files_written']} files modified, "
              f"{s['files_unchanged']} copied unchanged")

    print(f"{'─' * 60}")
    print(f"  Total colour conversions: {total_lines}")
    if not args.dry_run:
        print(f"\n  ✅ Done!  To install a variant:")
        for s in all_stats:
            slug = next(v.slug for v in VARIANTS if v.name == s["variant"])
            print(f"     python generate_monochrome_variants.py --install {slug}")
        print()
    else:
        print("\n  Pass without --dry-run to write files.\n")


if __name__ == "__main__":
    main()
