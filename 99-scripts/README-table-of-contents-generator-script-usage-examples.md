# Table of Contents Generator Script Usage Examples

# Preview only (dry run, safe)
python _scripts/generate_toc.py "path/to/file.md"

# Write TOC into file (creates .bak backup automatically)
python _scripts/generate_toc.py "path/to/file.md" --execute

# Skip H1 title in TOC entries, only show H2-H4
python _scripts/generate_toc.py "path/to/file.md" --execute --skip-h1 --min-depth 2 --max-depth 4

# Skip backup
python _scripts/generate_toc.py "path/to/file.md" --execute --no-backup

