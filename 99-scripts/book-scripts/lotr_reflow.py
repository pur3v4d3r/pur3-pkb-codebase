#!/usr/bin/env python3
"""
lotr_reflow.py - Reflow hard-wrapped prose paragraphs in LOTR-Formatted.md

OCR from physical book pages produces hard line breaks at ~70 chars (print
page width). This script:
  1. Joins hard-wrapped lines within prose paragraphs into single flowing lines
  2. Fixes OCR hyphenated line breaks  (prob-/lems -> problems, but
                                         well-/to-do -> well-to-do)
  3. Collapses multiple consecutive blank lines to a single blank line
  4. Strips trailing whitespace from every line

Preserved unchanged:
  - YAML frontmatter (--- block at file start)
  - Headings (#, ##, ###, ...)
  - Blockquotes and callouts (> ...)
  - Lists (-, *, +, 1. ...)
  - Horizontal rules (---)
  - Code fences (``` ...)
  - Tables (| ...)

Hyphen resolution algorithm:
  - If  stem + continuation  is a real English word  -> drop hyphen
    e.g.  prob-lems  -> problems,  state-ment -> statement
  - Elif  stem  alone is a real word  -> keep hyphen  (it's a compound)
    e.g.  three-volume,  well-to-do,  heavy-legged
  - Else  -> keep hyphen  (safe default)

Requirements (one of):
  pip install pyspellchecker     (lightweight, pure-Python, recommended)
  pip install nltk  +  python -c "import nltk; nltk.download('words')"
  System dictionary at /usr/share/dict/words  (Linux/Mac)
  Fallback: all hyphens kept (no package needed, but less clean)

Usage:
  python lotr_reflow.py                          # default paths, in-place
  python lotr_reflow.py input.md output.md       # custom paths
"""

import re
import sys
import shutil
from pathlib import Path

# ---------------------------------------------------------------------------
# Word list loader
# ---------------------------------------------------------------------------

WORD_SET = None  # populated lazily on first use


def _load_word_set():
    # 1. pyspellchecker - fast, pure Python
    try:
        from spellchecker import SpellChecker
        spell = SpellChecker()
        words = set(w.lower() for w in spell.word_frequency.words())
        print(f"Word list: pyspellchecker ({len(words):,} words)")
        return words
    except ImportError:
        pass

    # 2. NLTK words corpus
    try:
        import nltk
        try:
            wset = set(w.lower() for w in nltk.corpus.words.words())
        except LookupError:
            nltk.download('words', quiet=True)
            wset = set(w.lower() for w in nltk.corpus.words.words())
        print(f"Word list: NLTK ({len(wset):,} words)")
        return wset
    except ImportError:
        pass

    # 3. System dictionary (Linux / Mac)
    for path in ['/usr/share/dict/words', '/usr/dict/words']:
        p = Path(path)
        if p.exists():
            words = set(p.read_text(encoding='utf-8', errors='ignore').lower().split())
            print(f"Word list: {path} ({len(words):,} words)")
            return words

    print("WARNING: No word list found. Install pyspellchecker for better hyphen fixing.")
    print("         pip install pyspellchecker")
    print("         All ambiguous hyphens will be kept (safe but imperfect).")
    return set()


def _ensure_words():
    global WORD_SET
    if WORD_SET is None:
        WORD_SET = _load_word_set()


def is_word(w):
    _ensure_words()
    return bool(WORD_SET) and w.lower() in WORD_SET


# ---------------------------------------------------------------------------
# Hyphen break resolution
# ---------------------------------------------------------------------------

def resolve_hyphen(stem, continuation):
    """
    Decide what to produce when a line ends with 'stem-' and the next line
    starts with 'continuation'.

    Returns: joined text (either 'stemcontinuation' or 'stem-continuation').
    """
    _ensure_words()

    if not WORD_SET:
        # No word list - keep hyphen (safe)
        return stem + '-' + continuation

    combined = stem + continuation

    # Rule 1: combined (no hyphen) is a real word -> it was a line-break hyphen
    if is_word(combined):
        return combined

    # Rule 2: stem alone is a real word -> it's a genuine compound hyphen
    if is_word(stem):
        return stem + '-' + continuation

    # Rule 3: unknown - keep hyphen (conservative)
    return stem + '-' + continuation


# ---------------------------------------------------------------------------
# Line classification
# ---------------------------------------------------------------------------

def is_markdown_special(line):
    """
    Return True for lines that must NOT be joined with adjacent prose.
    """
    stripped = line.strip()

    if not stripped:
        return True  # blank

    if stripped.startswith('#'):
        return True  # heading

    if stripped.startswith('>'):
        return True  # blockquote / callout

    if re.match(r'^[-*_]{3,}$', stripped):
        return True  # horizontal rule  (--- or *** or ___)

    if re.match(r'^[-*+] ', stripped):
        return True  # unordered list

    if re.match(r'^\d+[.)]\s', stripped):
        return True  # ordered list

    if stripped.startswith('|'):
        return True  # table

    if stripped.startswith('```') or stripped.startswith('~~~'):
        return True  # code fence

    if re.match(r'^<[a-zA-Z/]', stripped):
        return True  # HTML tag (span, div, etc.)

    # Indented code block (4 spaces or tab)
    if line.startswith('    ') or line.startswith('\t'):
        return True

    return False


# ---------------------------------------------------------------------------
# Paragraph joining
# ---------------------------------------------------------------------------

def join_paragraph(lines):
    """
    Join a list of accumulated prose lines into one flowing paragraph,
    resolving OCR hyphenated line breaks along the way.
    """
    if not lines:
        return ''
    if len(lines) == 1:
        return lines[0].rstrip()

    # Strip trailing whitespace from each line
    stripped = [l.rstrip() for l in lines]

    result = stripped[0]

    for chunk in stripped[1:]:
        next_text = chunk.lstrip()
        if not next_text:
            continue

        if result.endswith('-'):
            # Potential OCR hyphenated break at end of result
            m_stem = re.search(r'(\w+)-$', result)
            if m_stem:
                stem = m_stem.group(1)
                m_cont = re.match(r'^(\w+)', next_text)
                if m_cont:
                    cont = m_cont.group(1)
                    resolved = resolve_hyphen(stem, cont)
                    # Splice: replace 'stem-' at end of result with resolved,
                    # then append the remainder of next_text after 'cont'
                    result = result[:m_stem.start()] + resolved + next_text[len(cont):]
                else:
                    result = result + next_text
            else:
                result = result + next_text
        else:
            result = result + ' ' + next_text

    return result


# ---------------------------------------------------------------------------
# Main reflow
# ---------------------------------------------------------------------------

def reflow_file(input_path, output_path):
    print(f"Reading:  {input_path}")
    text = Path(input_path).read_text(encoding='utf-8')
    lines = text.split('\n')
    print(f"Input:    {len(lines):,} lines")

    result = []
    in_frontmatter = False
    in_code_block = False
    current_para = []
    consecutive_blanks = 0

    def flush():
        if current_para:
            result.append(join_paragraph(current_para))
            current_para.clear()

    for i, raw_line in enumerate(lines):
        stripped = raw_line.strip()

        # ---- YAML frontmatter (only the very first --- block) ----
        if i == 0 and stripped == '---':
            in_frontmatter = True
            result.append(raw_line.rstrip())
            continue

        if in_frontmatter:
            result.append(raw_line.rstrip())
            if stripped == '---' and i > 0:
                in_frontmatter = False
            continue

        # ---- Code fences ----
        if stripped.startswith('```') or stripped.startswith('~~~'):
            flush()
            in_code_block = not in_code_block
            result.append(raw_line.rstrip())
            continue

        if in_code_block:
            result.append(raw_line.rstrip())
            continue

        # ---- Blank line ----
        if not stripped:
            flush()
            consecutive_blanks += 1
            if consecutive_blanks <= 1:
                result.append('')
            # else: skip - collapse multiple blanks to one
            continue

        consecutive_blanks = 0

        # ---- Special markdown (headings, blockquotes, lists, etc.) ----
        if is_markdown_special(raw_line):
            flush()
            result.append(raw_line.rstrip())
            continue

        # ---- Regular prose line: accumulate for paragraph joining ----
        current_para.append(raw_line)

    flush()

    # Second pass: remove OCR running headers / noise and fix sentence joins
    result = fix_ocr_artifacts(result)

    output = '\n'.join(result)
    output = output.rstrip('\n') + '\n'

    Path(output_path).write_text(output, encoding='utf-8')

    out_lines = output.count('\n')
    reduction = len(lines) - out_lines
    print(f"Output:   {out_lines:,} lines  ({reduction:,} lines removed)")
    print(f"Written:  {output_path}")


# ---------------------------------------------------------------------------
# Second pass: remove OCR running headers and mid-sentence page breaks
# ---------------------------------------------------------------------------

# Real section headings that look like running heads but must be kept.
# These will be left as-is (they are proper ALL-CAPS section titles in the text).
_KEEP_HEADINGS = {
    'NOTE ON THE SHIRE RECORDS',
    'OF THE ORDERING OF THE SHIRE',
    'OF THE FINDING OF THE RING',
    'OF HERBS AND STEWED RABBIT',
    'THE GREY PILGRIM',
}

_TERMINAL_PUNCT = re.compile(r'[.!?)\u2019\u201d\u0027\u0022\*]\s*$')


def is_ocr_artifact(line):
    """
    Return True if this line looks like an OCR running header or noise fragment
    that should be removed.  Criteria (all must hold):
      - It is short (≤ 75 chars)
      - It is not a markdown structural line
      - It looks like one of the known OCR patterns:
          a) Contains "THE LORD OF THE RINGS" (always a running head)
          b) ALL-CAPS chapter name + short trailing OCR page-number suffix
          c) Very short all-caps noise (≤ 15 chars)
    """
    s = line.strip()
    if not s or len(s) > 75:
        return False
    # Never remove markdown structural lines
    if any(s.startswith(c) for c in ['#', '>', '-', '*', '|', '[', '`']):
        return False

    # Pattern (a): book-title running heads
    if 'THE LORD OF THE RINGS' in s:
        return True

    # Check overall uppercase ratio
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return len(s) <= 15  # pure non-alpha noise like "---" caught elsewhere
    caps_ratio = sum(1 for c in letters if c.isupper()) / len(letters)

    # Pattern (b): ALL-CAPS chapter-name running heads (≥ 85% uppercase)
    # e.g. "THREE IS COMPANY TI", "FLIGHT TO THE FORD", "TOM BOMBADIL"
    if caps_ratio >= 0.85:
        # Keep known real section headings
        if s in _KEEP_HEADINGS:
            return False
        # Must look like a chapter/section name (≥ 3 words OR short ≤ 20 chars)
        words = s.split()
        if len(words) >= 2:
            return True

    # Pattern (c): short junk fragments (≤ 12 chars, high caps)
    if len(s) <= 12 and caps_ratio >= 0.7:
        return True

    return False


def fix_ocr_artifacts(lines):
    """
    Second pass over reflowed lines.  Removes isolated OCR running headers /
    noise fragments and, where the surrounding paragraphs form a mid-sentence
    break, joins them.

    An "isolated" artifact is one that appears as its own paragraph block
    (surrounded by blank lines, or at file start/end).
    """
    # Work on a list so we can modify in-place and track position
    result = list(lines)

    i = 0
    removed = 0
    joined = 0
    while i < len(result):
        line = result[i]
        stripped = line.strip()

        # Skip blank lines and non-artifact lines
        if not stripped or not is_ocr_artifact(line):
            i += 1
            continue

        # Found a candidate artifact.  Verify it is isolated (surrounded by blanks).
        prev_blank = (i == 0) or (not result[i - 1].strip())
        next_blank = (i >= len(result) - 1) or (not result[i + 1].strip())

        if not (prev_blank and next_blank):
            i += 1
            continue

        # --- It's an isolated artifact.  Remove it. ---
        removed += 1

        # Find the paragraph immediately before the artifact
        # (skip backwards over blank lines)
        before_idx = i - 1
        while before_idx >= 0 and not result[before_idx].strip():
            before_idx -= 1

        # Find the paragraph immediately after the artifact
        # (skip forward over the artifact line and trailing blanks)
        after_idx = i + 1
        while after_idx < len(result) and not result[after_idx].strip():
            after_idx += 1

        # Decide whether to join the surrounding paragraphs.
        # Join if: preceding paragraph doesn't end with terminal punctuation
        #          AND following paragraph starts with a lowercase letter.
        do_join = False
        if 0 <= before_idx < len(result) and after_idx < len(result):
            before_line = result[before_idx].strip()
            after_line  = result[after_idx].strip()
            # Skip markdown special lines from joining
            if (before_line and after_line
                    and not any(before_line.startswith(c) for c in ['#', '>', '-', '*', '|'])
                    and not any(after_line.startswith(c)  for c in ['#', '>', '-', '*', '|'])
                    and not _TERMINAL_PUNCT.search(before_line)
                    and re.match(r'^[a-z\(]', after_line)):
                do_join = True

        if do_join:
            # Merge after_line onto before_line, then delete everything in between
            # (blanks + artifact + blanks + after_line)
            result[before_idx] = result[before_idx].rstrip() + ' ' + result[after_idx].strip()
            # Delete from (before_idx+1) through after_idx inclusive
            del result[before_idx + 1 : after_idx + 1]
            joined += 1
            # Don't advance i — the splice shifted things, recheck from before_idx+1
            i = before_idx + 1
        else:
            # Just remove the artifact line (and collapse surrounding blanks)
            # Remove blank before + artifact + blank after as a unit
            start_del = i
            end_del   = i + 1  # exclusive
            if start_del > 0 and not result[start_del - 1].strip():
                start_del -= 1
            if end_del < len(result) and not result[end_del].strip():
                end_del += 1
            del result[start_del:end_del]
            # Insert one blank line to preserve paragraph separation
            result.insert(start_del, '')
            i = start_del + 1

    print(f"Artifacts removed: {removed}  ({joined} with sentence join)")
    return result


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    vault_root = Path(r"d:\10_pur3v4d3r's-vault")
    default_input = vault_root / "999-ebook-project" / "LOTR-Formatted.md"

    input_path  = Path(sys.argv[1]) if len(sys.argv) >= 2 else default_input
    output_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else input_path  # in-place

    if not input_path.exists():
        print(f"Error: file not found: {input_path}")
        sys.exit(1)

    # Always create a backup before touching the file
    backup = input_path.with_suffix('.md.bak')
    shutil.copy2(input_path, backup)
    print(f"Backup:   {backup}")

    # Preload word list before processing
    _ensure_words()

    reflow_file(input_path, output_path)
    print("Done.")


if __name__ == '__main__':
    main()
