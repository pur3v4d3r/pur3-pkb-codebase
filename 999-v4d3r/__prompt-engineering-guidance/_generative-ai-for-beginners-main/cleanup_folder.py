import os
import fnmatch
import argparse
import shutil

# --- Default Configuration ---
# Patterns to DELETE (excluding .ipynb now)
DEFAULT_PATTERNS_TO_DELETE = [
    "*.png", "*.jpg", "*.jpeg", "*.gif", "*.webp",  # Images
    "package-lock.json",
    "requirements.txt",
    "*.dib",
    "*.sh", "*.bat", "*.ps1",
    "embedding_index_3m.json"
]

# Exclude these even if they match delete patterns
EXCLUDE_PATTERNS = [
    "*.ipynb"  # Keep Jupyter notebooks
]

# --- End Configuration ---

def matches_any_pattern(filename, patterns):
    return any(fnmatch.fnmatch(filename, pat) for pat in patterns)

def should_delete_file(filepath, delete_patterns, exclude_patterns):
    filename = os.path.basename(filepath)
    if matches_any_pattern(filename, exclude_patterns):
        return False
    return matches_any_pattern(filename, delete_patterns)

def clean_directory(root_dir, delete_patterns, exclude_patterns, dry_run=False, remove_empty_dirs=False, verbose=False):
    deleted_files = 0
    deleted_dirs = 0

    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Delete matching files
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)
            if should_delete_file(fpath, delete_patterns, exclude_patterns):
                if verbose or dry_run:
                    print(f"[{'DRY RUN' if dry_run else 'DELETE'}] {fpath}")
                if not dry_run:
                    try:
                        os.remove(fpath)
                        deleted_files += 1
                    except Exception as e:
                        print(f"[ERROR] Could not delete {fpath}: {e}")

        # Optionally remove empty directories
        if remove_empty_dirs and not any(os.scandir(dirpath)):
            if verbose or dry_run:
                print(f"[{'DRY RUN' if dry_run else 'RMDIR'}] {dirpath}")
            if not dry_run:
                try:
                    os.rmdir(dirpath)
                    deleted_dirs += 1
                except Exception as e:
                    print(f"[ERROR] Could not remove directory {dirpath}: {e}")

    print(f"\n✅ Deleted {deleted_files} files.")
    if remove_empty_dirs:
        print(f"🗑️  Removed {deleted_dirs} empty directories.")

def main():
    parser = argparse.ArgumentParser(description="Remove unwanted files from a folder tree.")
    parser.add_argument("root_dir", help="Root directory to clean")
    parser.add_argument("--patterns", nargs="*", default=DEFAULT_PATTERNS_TO_DELETE,
                        help="File patterns to delete (e.g., *.png)")
    parser.add_argument("--exclude", nargs="*", default=EXCLUDE_PATTERNS,
                        help="Patterns to exclude from deletion")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview deletions without actually deleting")
    parser.add_argument("--remove-empty-dirs", action="store_true",
                        help="Remove empty directories after cleaning")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable verbose output")

    args = parser.parse_args()

    if not os.path.isdir(args.root_dir):
        print(f"[ERROR] Directory '{args.root_dir}' does not exist.")
        return

    clean_directory(
        root_dir=args.root_dir,
        delete_patterns=args.patterns,
        exclude_patterns=args.exclude,
        dry_run=args.dry_run,
        remove_empty_dirs=args.remove_empty_dirs,
        verbose=args.verbose
    )

if __name__ == "__main__":
    main()


    