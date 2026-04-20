#!/usr/bin/env python3
"""
LOTR Wiki-Link Case Normalisation — cleanup pass

Fixes case inconsistencies in [[wiki-links]] introduced by re.IGNORECASE matching
in the chapter formatting script.

Replacements applied (in LOTR-Formatted.md):
  [[THE PRANCING PONY]]     -> [[The Prancing Pony]]
  [[The Shire]]             -> [[the Shire]]
  [[the black gate]]        -> [[the Black Gate]]
  [[The Anduin]]            -> [[the Anduin]]
  [[The prancing pony]]     -> [[The Prancing Pony]]
  [[Lothlrien]] / variants  -> [[Lothlórien]]

Run: python lotr_wikilink_normalize.py
"""

import re
import os

VAULT  = r"d:\10_pur3v4d3r's-vault"
TARGET = os.path.join(VAULT, "LOTR-Formatted.md")

# (find_pattern, replacement) — order matters, more specific first
REPLACEMENTS = [
    # All-caps OCR artifact
    (r"\[\[THE PRANCING PONY\]\]",      "[[The Prancing Pony]]"),
    # Mixed-case variants
    (r"\[\[[Tt]he [Pp]racing [Pp]ony\]\]", "[[The Prancing Pony]]"),
    (r"\[\[The Shire\]\]",              "[[the Shire]]"),
    (r"\[\[the black gate\]\]",         "[[the Black Gate]]"),
    (r"\[\[The Anduin\]\]",             "[[the Anduin]]"),
    (r"\[\[The anduin\]\]",             "[[the Anduin]]"),
    (r"\[\[The one ring\]\]",           "[[the One Ring]]"),
    (r"\[\[The old forest\]\]",         "[[Old Forest]]"),
    (r"\[\[The dead marshes\]\]",       "[[Dead Marshes]]"),
    # Lothlórien encoding variants (OCR may have stripped the accent)
    (r"\[\[Lothlorien\]\]",             "[[Lothlórien]]"),
    (r"\[\[Lothlrien\]\]",              "[[Lothlórien]]"),
]


def main():
    print("Wiki-Link Case Normalisation")
    print("=" * 40)

    with open(TARGET, "r", encoding="utf-8") as f:
        text = f.read()

    total_changes = 0
    for pattern, replacement in REPLACEMENTS:
        new_text, count = re.subn(pattern, replacement, text)
        if count:
            print(f"  {count:>3}x  {pattern[:45]!r:47} -> {replacement}")
            total_changes += count
            text = new_text

    if total_changes == 0:
        print("  No changes needed.")
    else:
        with open(TARGET, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"\nTotal replacements: {total_changes}")
        print(f"File updated: {os.path.basename(TARGET)}")


if __name__ == "__main__":
    main()
