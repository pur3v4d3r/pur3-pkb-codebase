import os
import shutil
from pathlib import Path

# Define root directory and target pruned folder
ROOT_DIR = Path("_openai-cookbooks")
PRUNED_DIR = ROOT_DIR / "_pruned_files"

# Create pruned folder if not exists
PRUNED_DIR.mkdir(exist_ok=True)

# List of paths to move (can be files or directories)
TO_PRUNE = [
    ROOT_DIR / "data" / "hotel_invoices" / "extracted_invoice_json",
    ROOT_DIR / "data" / "hotel_invoices" / "transformed_invoice_json",
    ROOT_DIR / "gpt-5" / "outputs",
    ROOT_DIR / "voice_solutions" / "one_way_translation_using_realtime_api" / "mirror-server",
    ROOT_DIR / "voice_solutions" / "one_way_translation_using_realtime_api" / "relay-server",
]

def move_to_pruned(src_path):
    """Move file or folder to _pruned_files while preserving structure."""
    rel_path = src_path.relative_to(ROOT_DIR)
    dest_path = PRUNED_DIR / rel_path
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Moving: {src_path} → {dest_path}")
    shutil.move(str(src_path), str(dest_path))

if __name__ == "__main__":
    for path in TO_PRUNE:
        if path.exists():
            move_to_pruned(path)
        else:
            print(f"[Warning] Path does not exist: {path}")