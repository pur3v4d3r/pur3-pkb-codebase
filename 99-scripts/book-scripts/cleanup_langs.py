import os
import argparse
import sys

# Configuration
TARGET_DIR = "."
# [cite_start]Extensions observed in the directory tree [cite: 1, 2]
TARGET_EXTENSIONS = ('.mdx', '.json')
# The language code we want to KEEP
KEEP_LANG = 'en'

def clean_directory(directory, dry_run=False):
    deleted_count = 0
    kept_count = 0
    bytes_freed = 0

    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' not found.")
        sys.exit(1)

    print(f"{'[DRY RUN]' if dry_run else '[LIVE]'} Scanning '{directory}'...")
    print("-" * 50)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip files that don't match our target extensions (.mdx, .json)
            # [cite_start]This protects files like _app.tsx, style.css, and api/*.js 
            if not file.endswith(TARGET_EXTENSIONS):
                kept_count += 1
                continue

            # Check for localization pattern
            # Logic: If it is an MDX/JSON file, but DOES NOT end in .en.mdx or .en.json
            if not file.endswith(f".{KEEP_LANG}.mdx") and not file.endswith(f".{KEEP_LANG}.json"):
                file_size = os.path.getsize(file_path)
                
                if dry_run:
                    print(f"Would delete: {file_path}")
                else:
                    try:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    except OSError as e:
                        print(f"Error deleting {file_path}: {e}")

                deleted_count += 1
                bytes_freed += file_size
            else:
                kept_count += 1

    print("-" * 50)
    status = "Potential cleanup" if dry_run else "Cleanup complete"
    print(f"{status} stats:")
    print(f"Files to remove: {deleted_count}")
    print(f"Files to keep:   {kept_count}")
    print(f"Space reclaimed: {bytes_freed / 1024:.2f} KB")

    if dry_run and deleted_count > 0:
        print("\nTo actually delete these files, run:")
        print(f"python {sys.argv[0]} --force")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove non-English translation files.")
    parser.add_argument("--force", action="store_true", help="Perform the actual deletion")
    args = parser.parse_args()

    clean_directory(TARGET_DIR, dry_run=not args.force)