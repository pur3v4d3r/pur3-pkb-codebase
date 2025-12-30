import os
import re
from collections import defaultdict

# CONFIGURATION
IGNORE_DIRS = {'.git', '.obsidian', '.trash', '_scripts', 'node_modules'}
GHOST_LINK_MARKER = "Ghost Link"  # Optional: mark intentional future notes

def extract_wikilinks_with_context(file_path):
    """
    Extract all [[Wiki-Links]] with line numbers for reporting.
    Returns list of tuples: (link_target, line_number, link_text)
    """
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line_num, line in enumerate(lines, start=1):
            # Match [[Link]] or [[Link|Alias]] or [[Link#Heading]] etc.
            pattern = r'\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]'
            matches = re.finditer(pattern, line)

            for match in matches:
                link_target = match.group(1).strip()
                link_text = match.group(0)

                # Check if this is marked as Ghost Link
                is_ghost = GHOST_LINK_MARKER in line

                links.append((link_target, line_num, link_text, is_ghost))

    except Exception as e:
        pass

    return links

def build_file_catalog(root_dir):
    """
    Build a catalog of all markdown files in the vault.
    Returns dict: filename (no .md) -> full_path
    """
    files_dict = {}

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                filename = file[:-3]  # Remove .md
                files_dict[filename] = full_path

    return files_dict

def check_broken_links(root_dir):
    """
    Scan all notes for broken wiki-links.
    Returns dict of broken links by file.
    """
    files_dict = build_file_catalog(root_dir)
    broken_by_file = defaultdict(list)
    ghost_links = defaultdict(list)
    total_links = 0
    broken_count = 0
    ghost_count = 0

    for filename, full_path in files_dict.items():
        links = extract_wikilinks_with_context(full_path)
        total_links += len(links)

        for link_target, line_num, link_text, is_ghost in links:
            # Check if target exists in vault
            if link_target not in files_dict:
                if is_ghost:
                    ghost_links[filename].append((link_target, line_num, link_text))
                    ghost_count += 1
                else:
                    broken_by_file[filename].append((link_target, line_num, link_text))
                    broken_count += 1

    return {
        'files_dict': files_dict,
        'broken_by_file': broken_by_file,
        'ghost_links': ghost_links,
        'total_links': total_links,
        'broken_count': broken_count,
        'ghost_count': ghost_count
    }

def print_report(results):
    """
    Output formatted report of broken link analysis.
    """
    files_dict = results['files_dict']
    broken_by_file = results['broken_by_file']
    ghost_links = results['ghost_links']
    total_links = results['total_links']
    broken_count = results['broken_count']
    ghost_count = results['ghost_count']

    total_notes = len(files_dict)
    files_with_broken = len(broken_by_file)
    files_with_ghosts = len(ghost_links)

    print("=" * 60)
    print("🔗 VAULT HEALTH: BROKEN LINK DETECTION REPORT")
    print("=" * 60)
    print(f"\n📊 Statistics:")
    print(f"   Total Notes: {total_notes}")
    print(f"   Total Wiki-Links: {total_links}")
    print(f"   Valid Links: {total_links - broken_count - ghost_count} ({(total_links - broken_count - ghost_count)/total_links*100:.1f}%)")
    print(f"   🔴 Broken Links: {broken_count} ({broken_count/total_links*100:.1f}%)")
    print(f"   👻 Ghost Links (Intentional): {ghost_count}")

    # BROKEN LINKS
    if broken_by_file:
        print(f"\n{'='*60}")
        print(f"🚨 BROKEN LINKS DETECTED: {files_with_broken} files affected")
        print(f"{'='*60}\n")

        # Show top 10 files with most broken links
        sorted_files = sorted(broken_by_file.items(), key=lambda x: len(x[1]), reverse=True)

        for filename, broken_links in sorted_files[:10]:
            rel_path = os.path.relpath(files_dict[filename])
            print(f"📄 [[{filename}]] ({len(broken_links)} broken)")
            print(f"   📂 {rel_path}\n")

            for link_target, line_num, link_text in broken_links[:5]:
                print(f"   ❌ Line {line_num}: {link_text}")
                print(f"      → Target not found: [[{link_target}]]")

            if len(broken_links) > 5:
                print(f"   ... and {len(broken_links) - 5} more broken links")
            print()

        if files_with_broken > 10:
            remaining_broken = sum(len(links) for _, links in sorted_files[10:])
            print(f"... and {files_with_broken - 10} more files with {remaining_broken} broken links\n")

    else:
        print("\n✅ NO BROKEN LINKS DETECTED! Graph integrity is excellent.")

    # GHOST LINKS (Optional info)
    if ghost_links:
        print(f"\n{'='*60}")
        print(f"👻 GHOST LINKS (Intentional Future Notes): {ghost_count}")
        print(f"{'='*60}")
        print("These are marked as intentional - no action needed.\n")

        for filename, links in list(ghost_links.items())[:3]:
            rel_path = os.path.relpath(files_dict[filename])
            print(f"📄 [[{filename}]]")
            for link_target, _, _ in links[:2]:
                print(f"   👻 [[{link_target}]]")

        if len(ghost_links) > 3:
            print(f"\n   ... and {len(ghost_links) - 3} more files with ghost links")

    print("\n" + "=" * 60)
    print("💡 RECOMMENDATIONS:")
    if broken_by_file:
        print("   1. Review broken links - are they typos or deleted notes?")
        print("   2. Fix typos in link targets")
        print("   3. Create missing notes if concepts are needed")
        print("   4. Remove links to permanently deleted concepts")
        print("   5. Mark intentional future notes with 'Ghost Link' comment")
    else:
        print("   ✅ No action needed - all links are valid!")
    print("=" * 60)

def main():
    print("🔍 Scanning vault for broken wiki-links...\n")

    results = check_broken_links(".")
    print_report(results)

if __name__ == "__main__":
    main()
