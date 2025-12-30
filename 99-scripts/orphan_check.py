import os
import re
from collections import defaultdict

# CONFIGURATION
IGNORE_DIRS = {'.git', '.obsidian', '.trash', '_scripts', 'node_modules'}
MIN_OUTGOING = 2
MIN_INCOMING = 2

def extract_wikilinks(file_path):
    """
    Extract all [[Wiki-Links]] from a markdown file.
    Returns list of link targets (without brackets).
    """
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Match [[Link]] or [[Link|Alias]]
        pattern = r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]'
        matches = re.findall(pattern, content)

        # Clean up links (strip whitespace)
        links = [m.strip() for m in matches]

    except Exception as e:
        pass

    return links

def build_graph(root_dir):
    """
    Builds a bidirectional graph of all notes and their connections.
    Returns: (files_dict, outgoing_links, incoming_links)
    """
    files_dict = {}  # filename (no .md) -> full_path
    outgoing_links = defaultdict(set)  # note -> set of notes it links to
    incoming_links = defaultdict(set)  # note -> set of notes that link to it

    # Phase 1: Catalog all notes
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                filename = file[:-3]  # Remove .md
                files_dict[filename] = full_path

    # Phase 2: Build connection graph
    for filename, full_path in files_dict.items():
        links = extract_wikilinks(full_path)

        for link in links:
            # Handle potential aliases or partial matches
            # For simplicity, exact match only (Obsidian's link resolution is complex)
            if link in files_dict:
                outgoing_links[filename].add(link)
                incoming_links[link].add(filename)

    return files_dict, outgoing_links, incoming_links

def find_orphans(files_dict, outgoing_links, incoming_links):
    """
    Identifies notes with insufficient connections.
    Returns dict of orphan types.
    """
    isolated = []  # No incoming AND no outgoing
    weak_outgoing = []  # <2 outgoing
    weak_incoming = []  # <2 incoming
    healthy = []

    for filename in files_dict.keys():
        out_count = len(outgoing_links.get(filename, set()))
        in_count = len(incoming_links.get(filename, set()))

        if out_count == 0 and in_count == 0:
            isolated.append((filename, out_count, in_count))
        elif out_count < MIN_OUTGOING and in_count < MIN_INCOMING:
            weak_outgoing.append((filename, out_count, in_count))
            weak_incoming.append((filename, out_count, in_count))
        elif out_count < MIN_OUTGOING:
            weak_outgoing.append((filename, out_count, in_count))
        elif in_count < MIN_INCOMING:
            weak_incoming.append((filename, out_count, in_count))
        else:
            healthy.append((filename, out_count, in_count))

    return {
        'isolated': isolated,
        'weak_outgoing': weak_outgoing,
        'weak_incoming': weak_incoming,
        'healthy': healthy
    }

def print_report(orphans, files_dict):
    """
    Outputs formatted report of orphan analysis.
    """
    total_notes = len(files_dict)
    isolated = orphans['isolated']
    weak_out = orphans['weak_outgoing']
    weak_in = orphans['weak_incoming']
    healthy = orphans['healthy']

    print("=" * 60)
    print("🏥 VAULT HEALTH: ORPHAN DETECTION REPORT")
    print("=" * 60)
    print(f"\n📊 Total Notes: {total_notes}")
    print(f"✅ Healthy (≥{MIN_OUTGOING} out, ≥{MIN_INCOMING} in): {len(healthy)} ({len(healthy)/total_notes*100:.1f}%)")
    print(f"⚠️  At-Risk Notes: {total_notes - len(healthy)} ({(total_notes - len(healthy))/total_notes*100:.1f}%)")

    # CRITICAL: Completely Isolated
    if isolated:
        print(f"\n🚨 CRITICAL: COMPLETELY ISOLATED ({len(isolated)})")
        print("   No incoming OR outgoing links\n")
        for filename, out, inc in sorted(isolated)[:10]:
            rel_path = os.path.relpath(files_dict[filename])
            print(f"   🔴 [[{filename}]]")
            print(f"      📂 {rel_path}")
        if len(isolated) > 10:
            print(f"\n   ... and {len(isolated) - 10} more")

    # WEAK OUTGOING
    if weak_out:
        print(f"\n⚠️  WEAK OUTGOING LINKS (<{MIN_OUTGOING}): {len(weak_out)}")
        print("   Notes not connecting to enough concepts\n")
        for filename, out, inc in sorted(weak_out, key=lambda x: x[1])[:5]:
            rel_path = os.path.relpath(files_dict[filename])
            print(f"   🟡 [[{filename}]] → {out} outgoing, {inc} incoming")
            print(f"      📂 {rel_path}")
        if len(weak_out) > 5:
            print(f"\n   ... and {len(weak_out) - 5} more")

    # WEAK INCOMING
    if weak_in:
        print(f"\n⚠️  WEAK INCOMING LINKS (<{MIN_INCOMING}): {len(weak_in)}")
        print("   Notes not referenced by enough sources\n")
        for filename, out, inc in sorted(weak_in, key=lambda x: x[2])[:5]:
            rel_path = os.path.relpath(files_dict[filename])
            print(f"   🟡 [[{filename}]] → {out} outgoing, {inc} incoming")
            print(f"      📂 {rel_path}")
        if len(weak_in) > 5:
            print(f"\n   ... and {len(weak_in) - 5} more")

    print("\n" + "=" * 60)
    print("💡 RECOMMENDATION:")
    print("   1. Review ISOLATED notes for deletion or integration")
    print("   2. Add outgoing links to WEAK OUTGOING notes")
    print("   3. Reference WEAK INCOMING notes from related content")
    print("=" * 60)

def main():
    print("🔍 Analyzing vault graph structure...\n")

    files_dict, outgoing, incoming = build_graph(".")
    orphans = find_orphans(files_dict, outgoing, incoming)
    print_report(orphans, files_dict)

if __name__ == "__main__":
    main()
