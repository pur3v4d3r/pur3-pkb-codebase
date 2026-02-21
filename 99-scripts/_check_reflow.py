from pathlib import Path
import re

text = Path(r"d:\10_pur3v4d3r's-vault\999-ebook-project\LOTR-Formatted.md").read_text(encoding='utf-8')
lines = text.split('\n')

print("=== Final Stats ===")
print(f"Total lines:     {len(lines):,}")

blanks = max(len(m.group())-1 for m in re.finditer(r'\n{2,}', text))
print(f"Max blank lines: {blanks}  (want 1)")

prose = [l for l in lines if l.strip() and not l.strip()[0] in '#>-*|[`']
avg = int(sum(len(l) for l in prose) / len(prose)) if prose else 0
print(f"Avg prose chars: {avg}  (was ~70 before)")
print(f"Short prose <90: {sum(1 for l in prose if len(l)<90)} lines  (should be low - short ones are labels/bylines)")

print(f"Headings:        {sum(1 for l in lines if l.startswith('#'))}")
print(f"Callouts:        {sum(1 for l in lines if l.startswith('> [!'))}")
print(f"Verse lines:     {sum(1 for l in lines if l.startswith('> *'))}")
print(f"List items:      {sum(1 for l in lines if re.match(r'^[-*] ', l))}")
print(f"YAML intact:     {lines[0] == '---' and 'tags:' in lines[1]}")
