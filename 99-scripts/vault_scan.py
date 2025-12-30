import os
import sys
import re
import difflib

# CONFIGURATION
# ------------------------------------------------------------------
# Directories to ignore during scan to save time/noise
IGNORE_DIRS = {'.git', '.obsidian', '.trash', '_scripts', 'node_modules'}
# ------------------------------------------------------------------

def parse_frontmatter(file_path):
    """
    Extracts aliases from a markdown file's YAML frontmatter.
    Target format: aliases: [Synonym 1, Synonym 2]
    """
    aliases = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to find YAML block between ---
        yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if yaml_match:
            yaml_content = yaml_match.group(1)
            
            # Find aliases line: aliases: [Item 1, Item 2]
            # Case 1: Inline list [A, B]
            inline_match = re.search(r'aliases:\s*\[(.*?)\]', yaml_content)
            if inline_match:
                # Split by comma, strip quotes and whitespace
                raw_list = inline_match.group(1).split(',')
                aliases = [a.strip().strip("'").strip('"') for a in raw_list if a.strip()]
            
            # Case 2: Bullet list (less common in your vault but good fallback)
            # aliases:
            #   - Item 1
            else:
                list_match = re.search(r'aliases:\s*\n((?:\s*-\s*.*\n?)+)', yaml_content)
                if list_match:
                    items = list_match.group(1).split('\n')
                    aliases = [i.strip().replace('- ', '').strip() for i in items if i.strip()]
                    
    except Exception as e:
        # Fail silently on read errors, just return empty
        pass
        
    return aliases

def scan_vault(root_dir, search_term):
    print(f"🔍 SCANNING VAULT FOR: '{search_term}'...")
    
    exact_matches = []
    alias_matches = []
    all_filenames = []
    
    search_lower = search_term.lower()

    # Walk the directory tree
    for root, dirs, files in os.walk(root_dir):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                filename = file[:-3] # Remove .md
                all_filenames.append(filename)
                
                # Check 1: Exact Filename Match
                if filename.lower() == search_lower:
                    exact_matches.append(full_path)
                
                # Check 2: Alias Match (Expensive, so we do it)
                aliases = parse_frontmatter(full_path)
                for alias in aliases:
                    if alias.lower() == search_lower:
                        alias_matches.append((full_path, alias))

    # --- REPORTING ---
    
    found = False
    
    if exact_matches:
        print(f"\n✅ EXACT FILENAME MATCH FOUND:")
        for path in exact_matches:
            print(f"   📂 {path}")
        found = True

    if alias_matches:
        print(f"\n🔗 ALIAS MATCH FOUND:")
        for path, alias in alias_matches:
            print(f"   📂 {path} (Alias: '{alias}')")
        found = True
        
    if not found:
        print(f"\n❌ NO DIRECT MATCHES for '{search_term}'.")
        
        # Fuzzy Logic: Find close spellings
        close_files = difflib.get_close_matches(search_term, all_filenames, n=3, cutoff=0.6)
        if close_files:
            print(f"⚠️  DID YOU MEAN ONE OF THESE?")
            for cf in close_files:
                print(f"   ❓ {cf}")
        else:
            print("✨ Term appears unique. Safe to create.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vault_scan.py 'Search Term'")
        sys.exit(1)
        
    scan_vault(".", sys.argv[1])