




# Table of Contents Generator Script Usage Examples


<!-- TOC START -->

## Table of Contents

- [Table of Contents Generator Script Usage Examples](#table-of-contents-generator-script-usage-examples)
- [Preview only (dry run, safe)](#preview-only-dry-run-safe)
- [Write TOC into file (creates .bak backup automatically)](#write-toc-into-file-creates-bak-backup-automatically)
- [Skip H1 title in TOC entries, only show H2-H4](#skip-h1-title-in-toc-entries-only-show-h2-h4)
- [Skip backup](#skip-backup)

<!-- TOC END -->

# Preview only (dry run, safe)
python 99-scripts/generate_toc.py "path/to/file.md"

# Write TOC into file (creates .bak backup automatically)
python 99-scripts/generate_toc.py "path/to/file.md" --execute

# Skip H1 title in TOC entries, only show H2-H4
python 99-scripts/generate_toc.py "path/to/file.md" --execute --skip-h1 --min-depth 2 --max-depth 4

# Skip backup
python 99-scripts/generate_toc.py "path/to/file.md" --execute --no-backup


