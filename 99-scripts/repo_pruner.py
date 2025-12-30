import os
import shutil
import logging
import time
from pathlib import Path

# ==============================================================================
# ⚙️ CONFIGURATION - TARGETING LOCAL REPO
# ==============================================================================

# 1. PATHS (Using Raw Strings r"" to handle Windows backslashes)
# We target the specific folder inside your vault.
SOURCE_DIR = r"D:/10_pur3v4d3r's-vault/__LOCAL-REPO"
# We place the quarantine INSIDE that folder for atomic moves (faster on Windows)
DEST_DIR = r"D:/10_pur3v4d3r's-vault/05-archive/pruning-pkb-2025-12-30"

# 2. FILE EXTENSIONS TO PRUNE (The 6GB likely comes from these)
MEDIA_EXTENSIONS = {
    '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.ico', '.svg', # Images
    '.mp4', '.mov', '.avi', '.mkv', '.webm',                          # Video
    '.mp3', '.wav', '.flac', '.aac',                                  # Audio
    '.pdf', '.docx', '.pptx', '.xlsx', '.zip', '.tar', '.gz', '.7z',  # Docs/Archives
    '.exe', '.dll', '.so', '.bin', '.iso', '.dmg'                     # Binaries
}

# 3. DIRECTORIES TO PRUNE ENTIRELY (Dev artifacts & Cloned Repos)
BLOAT_DIRS = {
    'node_modules', '__pycache__', '.git', '.github', '.vscode', '.idea',
    'venv', '.venv', 'env', 'build', 'dist', 'target',
    '_generative-ai-for-beginners-main', 
    'site-packages'
}

# 4. CLUTTER PATTERNS (Filenames that indicate bulk generation/noise)
CLUTTER_PREFIXES = (
    "Personalized ", "ProductLanding", "Subscription-Based", 
    "Recipe Sharing", "Travel Planning", "Social Media Platform",
    "SAASDashboard", "QuickSilver", "SuperPrompt"
)

# 5. SIZE THRESHOLDS
LARGE_FILE_THRESHOLD_MB = 50 

# ==============================================================================
# 🛠️ UTILITY CLASS
# ==============================================================================

class RepoPruner:
    def __init__(self, source, dest, dry_run=False):
        self.source = Path(source).resolve()
        self.dest = Path(dest).resolve()
        self.dry_run = dry_run
        
        # Stats tracking
        self.stats = {
            'moved_files': 0,
            'moved_dirs': 0,
            'bytes_cleared': 0,
            'categories': {}
        }

        # Setup Logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler("prune_log.txt", encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def _get_category(self, file_path):
        """Determines the quarantine category for a file."""
        name = file_path.name
        ext = file_path.suffix.lower()

        # Skip the quarantine folder itself if it exists
        if self.dest in file_path.parents or file_path == self.dest:
            return None

        # Check size first (Windows stat calls can differ, adding try-catch)
        try:
            if file_path.stat().st_size > (LARGE_FILE_THRESHOLD_MB * 1024 * 1024):
                return "large_files"
        except OSError:
            pass 
        
        if ext in MEDIA_EXTENSIONS:
            return "media_assets"
        
        if name.startswith(CLUTTER_PREFIXES):
            return "bulk_generated_clutter"
        
        return None

    def move_item(self, src_path, category):
        """Moves a file or directory to the quarantine destination."""
        
        # Calculate relative path to maintain structure inside quarantine
        try:
            rel_path = src_path.relative_to(self.source)
        except ValueError:
            rel_path = src_path.name

        dest_path = self.dest / category / rel_path

        if self.dry_run:
            self.logger.info(f"[DRY RUN] Would move: {src_path.name} -> {category}")
            return

        # Create parent directories
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            if src_path.is_dir():
                if dest_path.exists():
                    self.logger.warning(f"Destination exists, skipping dir: {dest_path}")
                else:
                    shutil.move(str(src_path), str(dest_path))
                    self.stats['moved_dirs'] += 1
                    self.logger.info(f"Moved Directory: {src_path.name} -> {category}")
            else:
                shutil.move(str(src_path), str(dest_path))
                self.stats['moved_files'] += 1
                self.stats['bytes_cleared'] += dest_path.stat().st_size
                
            self.stats['categories'][category] = self.stats['categories'].get(category, 0) + 1

        except PermissionError:
            self.logger.error(f"❌ PERMISSION DENIED: {src_path} - Is the file open in Obsidian?")
        except Exception as e:
            self.logger.error(f"Failed to move {src_path}: {e}")

    def scan_and_prune(self):
        """Main execution loop."""
        self.logger.info(f"Starting Scan. Source: {self.source}")
        
        if not self.source.exists():
            self.logger.error(f"❌ Source directory NOT FOUND: {self.source}")
            self.logger.error("Check the path in the script and ensure the drive is mounted.")
            return

        # 1. Prune specific directory names first (Top-down)
        for root, dirs, files in os.walk(self.source, topdown=True):
            root_path = Path(root)
            
            # Skip Quarantine folder explicitly during walk
            if self.dest in root_path.parents or root_path == self.dest:
                dirs[:] = [] # Clear subdirs to stop recursion
                continue

            # Identify Directories to Move
            dirs_to_move = [d for d in dirs if d in BLOAT_DIRS]
            
            for d in dirs_to_move:
                src_dir = root_path / d
                self.move_item(src_dir, "dev_bloat_and_repos")
                dirs.remove(d) 
            
            # 2. Prune Files
            for f in files:
                file_path = root_path / f
                category = self._get_category(file_path)
                if category:
                    self.move_item(file_path, category)

        self._print_summary()

    def _print_summary(self):
        size_mb = self.stats['bytes_cleared'] / (1024 * 1024)
        print("\n" + "="*40)
        print(f"✅ PRUNING COMPLETE ({'DRY RUN' if self.dry_run else 'LIVE'})")
        print("="*40)
        print(f"📂 Directories Moved: {self.stats['moved_dirs']}")
        print(f"📄 Files Moved:       {self.stats['moved_files']}")
        print(f"💾 Space Reclaimed:   {size_mb:.2f} MB")
        print("\nBreakdown by Category:")
        for cat, count in self.stats['categories'].items():
            print(f" - {cat}: {count} items")
        print("="*40 + "\n")

if __name__ == "__main__":
    # ==========================================================================
    # ⚠️ SAFETY SWITCH: Change dry_run to False to enable actual moving
    # ==========================================================================
    pruner = RepoPruner(
        source=SOURCE_DIR, 
        dest=DEST_DIR, 
        dry_run=True  # <--- SET TO False TO ACTIVATE
    )
    
    print(f"Targeting Vault: {SOURCE_DIR}")
    if pruner.dry_run:
        print("⚠️  DRY RUN MODE: No files will be moved.")
    else:
        print("🚨 LIVE MODE: Files WILL be moved to quarantine.")
        time.sleep(2) # Give user a second to read
        
    pruner.scan_and_prune()