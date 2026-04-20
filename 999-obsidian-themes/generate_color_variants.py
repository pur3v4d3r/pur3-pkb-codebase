#!/usr/bin/env python3
"""
V4D3R THEME COLOR VARIANT GENERATOR
═══════════════════════════════════════════════════════════════════════════════

Generates color variants of the V4D3R Crimson Obsidian theme and all
associated CSS snippets. Uses HSL hue rotation to transform every red-family
color in the source files to the target color scheme — no manual color
mapping needed.

FEATURES:
  - HSL-based hue rotation (handles hundreds of unique reds automatically)
  - CSS variable renaming (--v4d3r-red-* → --v4d3r-{color}-*)
  - rgba() and bare RGB triplet transformation
  - Comment and description text updates
  - manifest.json generation per variant
  - Dual-tone support (e.g. Crimson + Gold)
  - Dry-run mode for preview

USAGE:
    python generate_color_variants.py                   # Generate ALL schemes
    python generate_color_variants.py --scheme teal     # Generate one scheme
    python generate_color_variants.py --dry-run         # Preview without writing
    python generate_color_variants.py --list            # List available schemes

REQUIREMENTS: Python 3.10+ (no external dependencies)

@author   PKB Scripting Architect
@version  1.1.0
"""

import colorsys
import json
import os
import re
import sys
import argparse
import textwrap
from pathlib import Path
from dataclasses import dataclass
from typing import Optional


# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class ColorScheme:
    """Defines a color variant for generation."""
    name: str                                  # Display name, e.g. "Teal"
    slug: str                                  # Folder/variable-safe, e.g. "teal"
    target_hue: float                          # Target hue (0-360) for primary accent
    description: str                           # For manifest.json and README
    secondary_hue: Optional[float] = None      # Dual-tone: hue for dark tones
    saturation_mult: float = 1.0               # Saturation scaling (1.0 = unchanged)
    lightness_offset: float = 0.0              # Lightness shift (-0.1 to 0.1)


# ── COLOR SCHEMES ─────────────────────────────────────────────────────────────
# Edit this list to add/remove/modify color variants.
# target_hue: 0=Red, 30=Orange, 60=Yellow, 120=Green, 180=Cyan, 240=Blue, 300=Magenta

COLOR_SCHEMES: list[ColorScheme] = [
    ColorScheme(
        name="Teal",
        slug="teal",
        target_hue=178.0,
        description="Dark theme with vibrant Teal, Black, and Grey palette",
    ),
    ColorScheme(
        name="Purple",
        slug="purple",
        target_hue=275.0,
        description="Dark theme with vibrant Purple, Black, and Grey palette",
    ),
    ColorScheme(
        name="Lime",
        slug="lime",
        target_hue=82.0,
        description="Dark theme with vibrant Lime Green, Black, and Grey palette",
        saturation_mult=1.1,
    ),
    ColorScheme(
        name="Crimson Gold",
        slug="crimson-gold",
        target_hue=45.0,          # Gold for bright accent tones
        secondary_hue=0.0,        # Crimson for dark/deep tones
        description="Dark theme with Crimson and Gold palette",
    ),
    ColorScheme(
        name="Blue",
        slug="blue",
        target_hue=215.0,
        description="Dark theme with vibrant Blue, Black, and Grey palette",
    ),
    ColorScheme(
        name="Orange",
        slug="orange",
        target_hue=25.0,
        description="Dark theme with vibrant Orange, Black, and Grey palette",
        saturation_mult=1.05,
    ),
    ColorScheme(
        name="Pink",
        slug="pink",
        target_hue=330.0,
        description="Dark theme with vibrant Pink, Black, and Grey palette",
    ),
    ColorScheme(
        name="Emerald",
        slug="emerald",
        target_hue=155.0,
        description="Dark theme with Emerald Green, Black, and Grey palette",
    ),
    ColorScheme(
        name="Amber",
        slug="amber",
        target_hue=38.0,
        description="Dark theme with Amber, Black, and Grey palette",
        saturation_mult=1.1,
    ),
    ColorScheme(
        name="Cyan",
        slug="cyan",
        target_hue=192.0,
        description="Dark theme with vibrant Cyan, Black, and Grey palette",
        saturation_mult=1.05,
    ),
    ColorScheme(
        name="Magenta",
        slug="magenta",
        target_hue=300.0,
        description="Dark theme with vibrant Magenta, Black, and Grey palette",
        saturation_mult=1.05,
    ),
    ColorScheme(
        name="Yellow",
        slug="yellow",
        target_hue=60.0,
        description="Dark theme with vibrant Yellow, Black, and Grey palette",
        saturation_mult=1.1,
    ),
    ColorScheme(
        name="Green",
        slug="green",
        target_hue=120.0,
        description="Dark theme with vibrant Green, Black, and Grey palette",
    ),
    ColorScheme(
        name="Red",
        slug="red",
        target_hue=0.0,
        description="Dark theme with vibrant Red, Black, and Grey palette",
    ),
    ColorScheme(
        name="Indigo",
        slug="indigo",
        target_hue=245.0,
        description="Dark theme with vibrant Indigo, Black, and Grey palette",
    ),
    ColorScheme(
        name="Violet",
        slug="violet",
        target_hue=270.0,
        description="Dark theme with vibrant Violet, Black, and Grey palette",
    ),
    ColorScheme(
        name="Golden",
        slug="golden",
        target_hue=45.0,
        description="Dark theme with vibrant Golden, Black, and Grey palette",
        saturation_mult=1.1,
    ),
    ColorScheme(
        name="Rose",
        slug="rose",
        target_hue=345.0,
        description="Dark theme with vibrant Rose, Black, and Grey palette",
    ),

    # ── RED FAMILY SHADES ─────────────────────────────────────────────────
    ColorScheme(
        name="Scarlet",
        slug="scarlet",
        target_hue=4.0,
        description="Dark theme with vivid Scarlet, Black, and Grey palette",
        saturation_mult=1.08,
    ),
    ColorScheme(
        name="Rust",
        slug="rust",
        target_hue=8.0,
        description="Dark theme with earthy Rust Red, Black, and Grey palette",
        saturation_mult=0.85,
        lightness_offset=-0.04,
    ),
    ColorScheme(
        name="Coral",
        slug="coral",
        target_hue=12.0,
        description="Dark theme with warm Coral, Black, and Grey palette",
        saturation_mult=1.05,
    ),
    ColorScheme(
        name="Peach",
        slug="peach",
        target_hue=18.0,
        description="Dark theme with soft Peach, Black, and Grey palette",
        saturation_mult=0.85,
        lightness_offset=0.03,
    ),
    ColorScheme(
        name="Copper",
        slug="copper",
        target_hue=22.0,
        description="Dark theme with warm Copper, Black, and Grey palette",
        saturation_mult=0.88,
    ),
    ColorScheme(
        name="Burgundy",
        slug="burgundy",
        target_hue=338.0,
        description="Dark theme with deep Burgundy Wine, Black, and Grey palette",
        saturation_mult=0.78,
        lightness_offset=-0.05,
    ),
    ColorScheme(
        name="Maroon",
        slug="maroon",
        target_hue=352.0,
        description="Dark theme with deep Maroon, Black, and Grey palette",
        saturation_mult=1.1,
        lightness_offset=-0.03,
    ),

    # ── YELLOW-GREEN SHADES ───────────────────────────────────────────────
    ColorScheme(
        name="Chartreuse",
        slug="chartreuse",
        target_hue=88.0,
        description="Dark theme with electric Chartreuse, Black, and Grey palette",
        saturation_mult=1.12,
    ),
    ColorScheme(
        name="Sage",
        slug="sage",
        target_hue=105.0,
        description="Dark theme with muted Sage Green, Black, and Grey palette",
        saturation_mult=0.68,
    ),
    ColorScheme(
        name="Neon Green",
        slug="neon-green",
        target_hue=112.0,
        description="Dark theme with electric Neon Green, Black, and Grey palette",
        saturation_mult=1.2,
    ),
    ColorScheme(
        name="Forest",
        slug="forest",
        target_hue=128.0,
        description="Dark theme with deep Forest Green, Black, and Grey palette",
        saturation_mult=0.82,
        lightness_offset=-0.04,
    ),
    ColorScheme(
        name="Mint",
        slug="mint",
        target_hue=148.0,
        description="Dark theme with fresh Mint Green, Black, and Grey palette",
        saturation_mult=0.9,
        lightness_offset=0.03,
    ),

    # ── BLUE-GREEN SHADES ─────────────────────────────────────────────────
    ColorScheme(
        name="Turquoise",
        slug="turquoise",
        target_hue=172.0,
        description="Dark theme with vivid Turquoise, Black, and Grey palette",
    ),

    # ── BLUE SHADES ───────────────────────────────────────────────────────
    ColorScheme(
        name="Sky",
        slug="sky",
        target_hue=200.0,
        description="Dark theme with bright Sky Blue, Black, and Grey palette",
        saturation_mult=0.88,
        lightness_offset=0.04,
    ),
    ColorScheme(
        name="Azure",
        slug="azure",
        target_hue=206.0,
        description="Dark theme with vibrant Azure Blue, Black, and Grey palette",
    ),
    ColorScheme(
        name="Steel",
        slug="steel",
        target_hue=210.0,
        description="Dark theme with cool Steel Blue, Black, and Grey palette",
        saturation_mult=0.65,
    ),
    ColorScheme(
        name="Navy",
        slug="navy",
        target_hue=222.0,
        description="Dark theme with deep Navy Blue, Black, and Grey palette",
        saturation_mult=0.82,
        lightness_offset=-0.05,
    ),
    ColorScheme(
        name="Cobalt",
        slug="cobalt",
        target_hue=229.0,
        description="Dark theme with deep Cobalt Blue, Black, and Grey palette",
        saturation_mult=1.05,
    ),

    # ── PURPLE SHADES ─────────────────────────────────────────────────────
    ColorScheme(
        name="Periwinkle",
        slug="periwinkle",
        target_hue=237.0,
        description="Dark theme with soft Periwinkle Blue-Violet, Black, and Grey palette",
        saturation_mult=0.85,
    ),
    ColorScheme(
        name="Lavender",
        slug="lavender",
        target_hue=250.0,
        description="Dark theme with soft Lavender, Black, and Grey palette",
        saturation_mult=0.75,
    ),
    ColorScheme(
        name="Deep Purple",
        slug="deep-purple",
        target_hue=262.0,
        description="Dark theme with deep Royal Purple, Black, and Grey palette",
        saturation_mult=1.08,
    ),
    ColorScheme(
        name="Lilac",
        slug="lilac",
        target_hue=283.0,
        description="Dark theme with soft Lilac, Black, and Grey palette",
        saturation_mult=0.78,
    ),
    ColorScheme(
        name="Orchid",
        slug="orchid",
        target_hue=292.0,
        description="Dark theme with vibrant Orchid, Black, and Grey palette",
        saturation_mult=1.02,
    ),

    # ── PINK-PURPLE SHADES ────────────────────────────────────────────────
    ColorScheme(
        name="Fuchsia",
        slug="fuchsia",
        target_hue=312.0,
        description="Dark theme with electric Fuchsia, Black, and Grey palette",
        saturation_mult=1.08,
    ),
    ColorScheme(
        name="Hot Pink",
        slug="hot-pink",
        target_hue=322.0,
        description="Dark theme with vivid Hot Pink, Black, and Grey palette",
        saturation_mult=1.05,
    ),

    # ── DUAL-TONE VARIANTS ────────────────────────────────────────────────
    ColorScheme(
        name="Ocean",
        slug="ocean",
        target_hue=195.0,
        secondary_hue=215.0,
        description="Dark theme with Ocean Blue dual-tone, Black, and Grey palette",
    ),
    ColorScheme(
        name="Aurora",
        slug="aurora",
        target_hue=160.0,
        secondary_hue=270.0,
        description="Dark theme with Aurora dual-tone (Teal-Violet), Black, and Grey palette",
    ),
    ColorScheme(
        name="Sunset",
        slug="sunset",
        target_hue=30.0,
        secondary_hue=340.0,
        description="Dark theme with Sunset dual-tone (Orange-Rose), Black, and Grey palette",
    ),
]

# ── PATHS ─────────────────────────────────────────────────────────────────────
VAULT_ROOT = Path(r"D:\10_pur3v4d3r's-vault")
THEME_SOURCE = VAULT_ROOT / ".obsidian" / "themes" / "V4D3R Crimson"
SNIPPETS_SOURCE = VAULT_ROOT / ".obsidian" / "snippets"
OUTPUT_ROOT = VAULT_ROOT / "999-obsidian-themes"

# ── RED DETECTION THRESHOLDS ──────────────────────────────────────────────────
# Colors with hue in [RED_HUE_LOW..360] or [0..RED_HUE_HIGH] AND
# saturation above RED_SAT_MIN are considered "red family" and transformed.
RED_HUE_LOW = 320       # Lower bound (pink-red)
RED_HUE_HIGH = 40       # Upper bound (orange-red)
RED_SAT_MIN = 0.12      # Minimum saturation to be "colored" (excludes greys)


# ═══════════════════════════════════════════════════════════════════════════════
# COLOR UTILITIES
# ═══════════════════════════════════════════════════════════════════════════════

def rgb_to_hsl(r: int, g: int, b: int) -> tuple[float, float, float]:
    """Convert RGB (0-255) to HSL (h=0-360, s=0-1, l=0-1)."""
    rf, gf, bf = r / 255.0, g / 255.0, b / 255.0
    h, l, s = colorsys.rgb_to_hls(rf, gf, bf)
    return h * 360.0, s, l


def hsl_to_rgb(h: float, s: float, l: float) -> tuple[int, int, int]:
    """Convert HSL (h=0-360, s=0-1, l=0-1) to RGB (0-255)."""
    h_norm = (h % 360) / 360.0
    s = max(0.0, min(1.0, s))
    l = max(0.0, min(1.0, l))
    rf, gf, bf = colorsys.hls_to_rgb(h_norm, l, s)
    return (
        max(0, min(255, round(rf * 255))),
        max(0, min(255, round(gf * 255))),
        max(0, min(255, round(bf * 255))),
    )


def is_red_family(r: int, g: int, b: int) -> bool:
    """Check if an RGB color belongs to the red family."""
    if r == 0 and g == 0 and b == 0:
        return False  # Pure black is not red
    h, s, l = rgb_to_hsl(r, g, b)
    if s < RED_SAT_MIN:
        return False  # Too desaturated (grey)
    return h >= RED_HUE_LOW or h <= RED_HUE_HIGH


def lerp_hue(h1: float, h2: float, t: float) -> float:
    """Linearly interpolate between two hues on the circular (0-360) scale."""
    diff = ((h2 - h1 + 180) % 360) - 180
    return (h1 + t * diff) % 360


def transform_color(
    r: int, g: int, b: int, scheme: ColorScheme
) -> tuple[int, int, int]:
    """Transform a red-family color to the target scheme using hue rotation."""
    h, s, l = rgb_to_hsl(r, g, b)

    # Calculate hue offset from red center (0°)
    offset = h if h <= 180 else h - 360

    if scheme.secondary_hue is not None:
        # Dual-tone: interpolate between secondary (dark) and primary (bright)
        # t=0 at very dark, t=1 at bright
        t = max(0.0, min(1.0, (l - 0.10) / 0.55))
        base_hue = lerp_hue(scheme.secondary_hue, scheme.target_hue, t)
    else:
        base_hue = scheme.target_hue

    new_h = (base_hue + offset) % 360
    new_s = max(0.0, min(1.0, s * scheme.saturation_mult))
    new_l = max(0.0, min(1.0, l + scheme.lightness_offset))

    return hsl_to_rgb(new_h, new_s, new_l)


# ═══════════════════════════════════════════════════════════════════════════════
# HEX COLOR PARSING
# ═══════════════════════════════════════════════════════════════════════════════

def parse_hex(hex_str: str) -> Optional[tuple[int, int, int, Optional[int]]]:
    """Parse a hex color string (#RGB, #RGBA, #RRGGBB, #RRGGBBAA).
    Returns (r, g, b, alpha) where alpha is None for 6-char hex, or 0-255."""
    h = hex_str.lstrip("#")
    if len(h) == 3:
        r, g, b = int(h[0]*2, 16), int(h[1]*2, 16), int(h[2]*2, 16)
        return r, g, b, None
    elif len(h) == 4:
        r, g, b, a = int(h[0]*2, 16), int(h[1]*2, 16), int(h[2]*2, 16), int(h[3]*2, 16)
        return r, g, b, a
    elif len(h) == 6:
        r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        return r, g, b, None
    elif len(h) == 8:
        r, g, b, a = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), int(h[6:8], 16)
        return r, g, b, a
    return None


def rgb_to_hex(r: int, g: int, b: int, alpha: Optional[int] = None,
               lowercase: bool = True) -> str:
    """Convert RGB(A) to hex string."""
    if alpha is not None:
        hex_str = f"#{r:02x}{g:02x}{b:02x}{alpha:02x}"
    else:
        hex_str = f"#{r:02x}{g:02x}{b:02x}"
    return hex_str if lowercase else hex_str.upper()


# ═══════════════════════════════════════════════════════════════════════════════
# CSS TRANSFORMATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

# Regex: Match hex colors (#RGB, #RGBA, #RRGGBB, #RRGGBBAA)
RE_HEX = re.compile(r"#([0-9A-Fa-f]{3,4}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})\b")

# Regex: Match rgba(R, G, B, A) and rgb(R, G, B)
RE_RGBA = re.compile(
    r"rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*"
    r"(?:,\s*([0-9.]+)\s*)?\)"
)

# Regex: Bare RGB triplets like "220, 20, 60" in any CSS custom property
# Matches: --any-variable: R, G, B  (followed by ; or end-of-value)
RE_BARE_RGB = re.compile(
    r"(--[\w-]+\s*:\s*(?:\/\*[^*]*\*\/\s*)?)(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})(?=\s*[;}\n])"
)


def transform_hex_match(match: re.Match, scheme: ColorScheme) -> str:
    """Replace a hex color if it's in the red family."""
    original = match.group(0)
    parsed = parse_hex(original)
    if parsed is None:
        return original

    r, g, b, alpha = parsed
    if not is_red_family(r, g, b):
        return original

    nr, ng, nb = transform_color(r, g, b, scheme)

    # Preserve case style of original
    was_upper = any(c.isupper() for c in match.group(1) if c.isalpha())

    hex_result = rgb_to_hex(nr, ng, nb, alpha, lowercase=not was_upper)
    return hex_result


def transform_rgba_match(match: re.Match, scheme: ColorScheme) -> str:
    """Replace an rgba()/rgb() color if it's in the red family."""
    original = match.group(0)
    r, g, b = int(match.group(1)), int(match.group(2)), int(match.group(3))
    alpha_str = match.group(4)

    if not is_red_family(r, g, b):
        return original

    nr, ng, nb = transform_color(r, g, b, scheme)

    if alpha_str is not None:
        return f"rgba({nr}, {ng}, {nb}, {alpha_str})"
    else:
        return f"rgb({nr}, {ng}, {nb})"


def transform_bare_rgb_match(match: re.Match, scheme: ColorScheme) -> str:
    """Replace bare RGB triplet (e.g. --interactive-accent-rgb: 220, 20, 60)."""
    prefix = match.group(1)
    r, g, b = int(match.group(2)), int(match.group(3)), int(match.group(4))

    if not is_red_family(r, g, b):
        return match.group(0)

    nr, ng, nb = transform_color(r, g, b, scheme)
    return f"{prefix}{nr}, {ng}, {nb}"


def transform_css_colors(css: str, scheme: ColorScheme) -> str:
    """Transform all red-family colors in a CSS string."""
    # 1. Transform hex colors
    css = RE_HEX.sub(lambda m: transform_hex_match(m, scheme), css)
    # 2. Transform rgba/rgb colors
    css = RE_RGBA.sub(lambda m: transform_rgba_match(m, scheme), css)
    # 3. Transform bare RGB triplets
    css = RE_BARE_RGB.sub(lambda m: transform_bare_rgb_match(m, scheme), css)
    return css


# ═══════════════════════════════════════════════════════════════════════════════
# TEXT REPLACEMENT ENGINE (variable names, comments, descriptions)
# ═══════════════════════════════════════════════════════════════════════════════

def build_text_replacements(scheme: ColorScheme) -> list[tuple[str, str]]:
    """Build ordered list of (old, new) text replacements for a scheme.
    Order matters — longer/more specific patterns first to avoid partial matches."""
    name = scheme.name
    slug = scheme.slug
    NAME_UPPER = name.upper()
    NAME_TITLE = name

    replacements = [
        # ── THEME HEADER / DESCRIPTIONS ──
        ("V4D3R CRIMSON THEME", f"V4D3R {NAME_UPPER} THEME"),
        ("V4D3R Crimson Theme", f"V4D3R {NAME_TITLE} Theme"),
        ("V4D3R Crimson", f"V4D3R {NAME_TITLE}"),
        ("Red, Black, and Grey palette", f"{NAME_TITLE}, Black, and Grey palette"),
        ("Red, Black, Grey palette", f"{NAME_TITLE}, Black, Grey palette"),

        # ── SECTION HEADERS ──
        ("RED SPECTRUM - Primary Theme Accents", f"{NAME_UPPER} SPECTRUM - Primary Theme Accents"),
        ("RED SPECTRUM", f"{NAME_UPPER} SPECTRUM"),
        ("Red Spectrum - Primary Theme Accents", f"{NAME_TITLE} Spectrum - Primary Theme Accents"),
        ("Red Spectrum", f"{NAME_TITLE} Spectrum"),
        ("COLOR PALETTE - RED, BLACK, GREY SYSTEM", f"COLOR PALETTE - {NAME_UPPER}, BLACK, GREY SYSTEM"),
        ("RED, BLACK, GREY SYSTEM", f"{NAME_UPPER}, BLACK, GREY SYSTEM"),

        # ── VARIABLE NAMES: --v4d3r-*red* ──
        # These cover definitions AND var() references automatically
        ("--v4d3r-gradient-red-to-black", f"--v4d3r-gradient-{slug}-to-black"),
        ("--v4d3r-shadow-red-", f"--v4d3r-shadow-{slug}-"),
        ("--v4d3r-neon-red",    f"--v4d3r-neon-{slug}"),
        ("--v4d3r-red-",        f"--v4d3r-{slug}-"),

        # ── SNIPPET VARIABLE NAMES ──
        ("--red-glow-bright",   f"--{slug}-glow-bright"),
        ("--red-glow:",         f"--{slug}-glow:"),
        ("--red-glow)",         f"--{slug}-glow)"),
        ("--red-glow;",         f"--{slug}-glow;"),
        ("--red-shadow",        f"--{slug}-shadow"),

        # ── DESCRIPTIVE COMMENTS ──
        ("Crimson Red - Primary accent",   f"{NAME_TITLE} - Primary accent"),
        ("Crimson Red",                     NAME_TITLE),
        ("Dark Red - Borders",              f"Dark {NAME_TITLE} - Borders"),
        ("Dark Red",                        f"Dark {NAME_TITLE}"),
        ("Salmon Red - Highlights",         f"Bright {NAME_TITLE} - Highlights"),
        ("Salmon Red",                      f"Bright {NAME_TITLE}"),
        ("Pure Red - Critical elements",    f"Vivid {NAME_TITLE} - Critical elements"),
        ("Pure Red",                        f"Vivid {NAME_TITLE}"),
        ("Deep Red - Shadows",              f"Deep {NAME_TITLE} - Shadows"),
        ("Deep Red",                        f"Deep {NAME_TITLE}"),
        ("Primary Reds - Main accent",      f"Primary {NAME_TITLE}s - Main accent"),
        ("Primary Reds",                    f"Primary {NAME_TITLE}s"),
        ("Red Variants",                    f"{NAME_TITLE} Variants"),
        ("Red glow shadows",                f"{NAME_TITLE} glow shadows"),
        ("red neon",                        f"{slug} neon"),
        ("Strong red neon glow",            f"Strong {slug} neon glow"),
        ("Subtle red neon glow",            f"Subtle {slug} neon glow"),
        ("Soft red neon glow",              f"Soft {slug} neon glow"),
        ("faint red effect",                f"faint {slug} effect"),
        ("Primary Glow: #",                 f"Primary Glow: #"),  # Will be handled by hex transform

        # ── OPACITY COMMENTS ──
        ("% Crimson", f"% {NAME_TITLE}"),
    ]

    return replacements


def apply_text_replacements(content: str, scheme: ColorScheme) -> str:
    """Apply all text replacements to content string."""
    replacements = build_text_replacements(scheme)
    for old, new in replacements:
        content = content.replace(old, new)
    return content


# ═══════════════════════════════════════════════════════════════════════════════
# FILE PROCESSING
# ═══════════════════════════════════════════════════════════════════════════════

def process_css_file(content: str, scheme: ColorScheme) -> str:
    """Full pipeline: transform colors, then rename variables/text."""
    # Step 1: Transform color values (hex, rgba, bare RGB)
    result = transform_css_colors(content, scheme)
    # Step 2: Rename variables and update descriptive text
    result = apply_text_replacements(result, scheme)
    return result


def generate_manifest(scheme: ColorScheme) -> str:
    """Generate manifest.json for the theme variant."""
    manifest = {
        "name": f"V4D3R {scheme.name}",
        "version": "1.0.0",
        "minAppVersion": "1.5.0",
        "author": "Pur3v4d3r",
        "authorUrl": "https://github.com/pur3v4d3r",
    }
    return json.dumps(manifest, indent=4)


def generate_readme(scheme: ColorScheme) -> str:
    """Generate README.md for the theme variant."""
    return textwrap.dedent(f"""\
    # V4D3R {scheme.name}

    > {scheme.description}

    ## About

    A color variant of the **V4D3R Crimson** Obsidian theme, auto-generated using
    HSL hue rotation to transform all red-family accent colors to **{scheme.name}**.
    Black and grey tones are preserved unchanged.

    **Version:** 1.0.0
    **Base Theme:** V4D3R Crimson
    **Author:** Pur3v4d3r

    ## Installation

    ### Theme
    1. Copy the `V4D3R {scheme.name}` folder (containing `theme.css`, `manifest.json`,
       and this `README.md`) into your vault's `.obsidian/themes/` directory.
    2. In Obsidian: Settings → Appearance → Themes → Select **V4D3R {scheme.name}**.

    ### Snippets
    1. Copy all `.css` files from the `snippets/` folder into your vault's
       `.obsidian/snippets/` directory — replacing existing files if needed.
    2. In Obsidian: Settings → Appearance → CSS Snippets → Enable desired snippets.

    > ⚠️ **Note:** The snippets contain hardcoded colors matching this theme variant.
    > If you switch themes, you may want to switch snippet sets too.

    ## Color Palette

    Generated via HSL hue rotation from the original Crimson palette:
    - **Target Hue:** {scheme.target_hue}°
    {"- **Secondary Hue:** " + str(scheme.secondary_hue) + "° (dual-tone)" if scheme.secondary_hue is not None else ""}
    - **Saturation:** {"Boosted " + str(round((scheme.saturation_mult - 1) * 100)) + "%" if scheme.saturation_mult != 1.0 else "Preserved from original"}
    """)


# ═══════════════════════════════════════════════════════════════════════════════
# GENERATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

def generate_scheme(scheme: ColorScheme, dry_run: bool = False) -> dict:
    """Generate a complete theme variant. Returns stats dict."""
    theme_name = f"V4D3R {scheme.name}"
    output_dir = OUTPUT_ROOT / f"V4D3R-{scheme.slug.title().replace(' ', '-')}"
    theme_dir = output_dir / f"V4D3R {scheme.name}"
    snippets_dir = output_dir / "snippets"

    stats = {
        "scheme": scheme.name,
        "output_dir": str(output_dir),
        "files_written": 0,
        "colors_transformed": 0,
    }

    print(f"\n{'─' * 60}")
    print(f"  Generating: {theme_name}")
    print(f"  Target hue: {scheme.target_hue}°"
          + (f" + secondary {scheme.secondary_hue}°" if scheme.secondary_hue is not None else ""))
    print(f"  Output: {output_dir}")
    print(f"{'─' * 60}")

    if not dry_run:
        theme_dir.mkdir(parents=True, exist_ok=True)
        snippets_dir.mkdir(parents=True, exist_ok=True)

    # ── Process theme.css ──────────────────────────────────────────────────
    theme_css_path = THEME_SOURCE / "theme.css"
    if theme_css_path.exists():
        original = theme_css_path.read_text(encoding="utf-8")
        transformed = process_css_file(original, scheme)
        color_count = _count_transformations(original, transformed)
        stats["colors_transformed"] += color_count

        if not dry_run:
            (theme_dir / "theme.css").write_text(transformed, encoding="utf-8")
            stats["files_written"] += 1
        print(f"  ✓ theme.css ({color_count} color transformations)")
    else:
        print(f"  ✗ theme.css NOT FOUND at {theme_css_path}")

    # ── Process manifest.json ──────────────────────────────────────────────
    if not dry_run:
        (theme_dir / "manifest.json").write_text(
            generate_manifest(scheme), encoding="utf-8"
        )
        stats["files_written"] += 1
    print(f"  ✓ manifest.json")

    # ── Process README.md ──────────────────────────────────────────────────
    if not dry_run:
        (theme_dir / "README.md").write_text(
            generate_readme(scheme), encoding="utf-8"
        )
        stats["files_written"] += 1
    print(f"  ✓ README.md")

    # ── Process snippets ───────────────────────────────────────────────────
    snippet_files = sorted(SNIPPETS_SOURCE.glob("*.css"))
    snippet_count = 0

    for snippet_path in snippet_files:
        original = snippet_path.read_text(encoding="utf-8")
        transformed = process_css_file(original, scheme)
        color_count = _count_transformations(original, transformed)
        stats["colors_transformed"] += color_count

        if not dry_run:
            (snippets_dir / snippet_path.name).write_text(
                transformed, encoding="utf-8"
            )
            stats["files_written"] += 1
        snippet_count += 1

        if color_count > 0:
            print(f"  ✓ {snippet_path.name} ({color_count} transforms)")

    remaining = snippet_count - sum(
        1 for s in snippet_files
        if _count_transformations(
            s.read_text(encoding="utf-8"),
            process_css_file(s.read_text(encoding="utf-8"), scheme),
        ) > 0
    )
    if remaining > 0:
        print(f"  ✓ {remaining} snippet(s) copied unchanged (no red colors)")

    return stats


def _count_transformations(original: str, transformed: str) -> int:
    """Rough count of changed lines between original and transformed."""
    orig_lines = original.splitlines()
    trans_lines = transformed.splitlines()
    changes = 0
    for ol, tl in zip(orig_lines, trans_lines):
        if ol != tl:
            changes += 1
    changes += abs(len(orig_lines) - len(trans_lines))
    return changes


# ═══════════════════════════════════════════════════════════════════════════════
# INSTALL HELPER
# ═══════════════════════════════════════════════════════════════════════════════

def install_scheme(scheme_slug: str) -> None:
    """Copy a generated scheme into the active Obsidian config."""
    scheme = next((s for s in COLOR_SCHEMES if s.slug == scheme_slug), None)
    if not scheme:
        print(f"Unknown scheme: {scheme_slug}")
        return

    source_dir = OUTPUT_ROOT / f"V4D3R-{scheme.slug.title().replace(' ', '-')}"
    theme_source = source_dir / f"V4D3R {scheme.name}"
    snippets_source = source_dir / "snippets"

    if not source_dir.exists():
        print(f"Scheme not generated yet. Run generation first.")
        return

    # Copy theme
    theme_dest = VAULT_ROOT / ".obsidian" / "themes" / f"V4D3R {scheme.name}"
    theme_dest.mkdir(parents=True, exist_ok=True)
    for f in theme_source.iterdir():
        dest = theme_dest / f.name
        dest.write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"✓ Theme installed to: {theme_dest}")

    # Copy snippets
    snippets_dest = VAULT_ROOT / ".obsidian" / "snippets"
    count = 0
    for f in snippets_source.glob("*.css"):
        dest = snippets_dest / f.name
        dest.write_text(f.read_text(encoding="utf-8"), encoding="utf-8")
        count += 1
    print(f"✓ {count} snippets installed to: {snippets_dest}")
    print(f"\nSwitch in Obsidian: Settings → Appearance → Themes → V4D3R {scheme.name}")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="V4D3R Theme Color Variant Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
        EXAMPLES:
          python generate_color_variants.py                    # Generate all schemes
          python generate_color_variants.py --scheme teal      # Generate one scheme
          python generate_color_variants.py --scheme blue --scheme purple
          python generate_color_variants.py --dry-run          # Preview only
          python generate_color_variants.py --list             # Show available schemes
          python generate_color_variants.py --install teal     # Install a scheme
        """),
    )
    parser.add_argument(
        "--scheme", "-s", action="append", metavar="SLUG",
        help="Generate only specific scheme(s) by slug. Can be repeated.",
    )
    parser.add_argument(
        "--dry-run", "-n", action="store_true",
        help="Preview what would be generated without writing files.",
    )
    parser.add_argument(
        "--list", "-l", action="store_true",
        help="List all available color schemes and exit.",
    )
    parser.add_argument(
        "--install", "-i", metavar="SLUG",
        help="Install a generated scheme into the active Obsidian config.",
    )

    args = parser.parse_args()

    # ── List schemes ──────────────────────────────────────────────────────
    if args.list:
        print("\n  Available Color Schemes:")
        print(f"  {'─' * 50}")
        for s in COLOR_SCHEMES:
            dual = f" (dual-tone: {s.secondary_hue}° + {s.target_hue}°)" if s.secondary_hue is not None else ""
            print(f"  {s.slug:<16} {s.name:<18} hue={s.target_hue:>5.0f}°{dual}")
        print()
        return

    # ── Install a scheme ──────────────────────────────────────────────────
    if args.install:
        install_scheme(args.install)
        return

    # ── Validate sources ──────────────────────────────────────────────────
    if not THEME_SOURCE.exists():
        print(f"ERROR: Theme source not found: {THEME_SOURCE}")
        sys.exit(1)
    if not SNIPPETS_SOURCE.exists():
        print(f"ERROR: Snippets source not found: {SNIPPETS_SOURCE}")
        sys.exit(1)

    # ── Select schemes ────────────────────────────────────────────────────
    if args.scheme:
        schemes = []
        for slug in args.scheme:
            match = next((s for s in COLOR_SCHEMES if s.slug == slug), None)
            if match:
                schemes.append(match)
            else:
                print(f"WARNING: Unknown scheme '{slug}'. Use --list to see available schemes.")
        if not schemes:
            sys.exit(1)
    else:
        schemes = COLOR_SCHEMES

    # ── Generate ──────────────────────────────────────────────────────────
    print("═" * 60)
    print("  V4D3R THEME COLOR VARIANT GENERATOR")
    print(f"  Mode: {'DRY RUN' if args.dry_run else 'GENERATE'}")
    print(f"  Schemes: {len(schemes)}")
    print(f"  Source theme: {THEME_SOURCE}")
    print(f"  Source snippets: {SNIPPETS_SOURCE}")
    print(f"  Output: {OUTPUT_ROOT}")
    print("═" * 60)

    all_stats = []
    for scheme in schemes:
        stats = generate_scheme(scheme, dry_run=args.dry_run)
        all_stats.append(stats)

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"\n{'═' * 60}")
    print("  GENERATION SUMMARY")
    print(f"{'═' * 60}")
    total_files = sum(s["files_written"] for s in all_stats)
    total_transforms = sum(s["colors_transformed"] for s in all_stats)
    for s in all_stats:
        print(f"  {s['scheme']:<18} {s['files_written']:>3} files, "
              f"{s['colors_transformed']:>5} color transforms")
    print(f"  {'─' * 50}")
    print(f"  {'TOTAL':<18} {total_files:>3} files, {total_transforms:>5} transforms")

    if args.dry_run:
        print(f"\n  ⚠ DRY RUN — no files were written. Remove --dry-run to generate.")
    else:
        print(f"\n  ✓ All variants generated in: {OUTPUT_ROOT}")
        print(f"  Use --install SLUG to install a scheme into your active vault.")
    print()


if __name__ == "__main__":
    main()
