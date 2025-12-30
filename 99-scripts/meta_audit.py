import os
import re
from collections import defaultdict

# CONFIGURATION
IGNORE_DIRS = {'.git', '.obsidian', '.trash', '_scripts', 'node_modules'}

# Required YAML fields per CLAUDE.md protocol
REQUIRED_FIELDS = {
    'tags': list,  # Must be list
    'aliases': list,  # Must be list
    'status': str,  # Must be one of: seedling, evergreen, reference
    'certainty': str  # Must be one of: ^verified, ^speculative
}

VALID_STATUS = {'seedling', 'evergreen', 'reference'}
VALID_CERTAINTY = {'^verified', '^speculative'}

def parse_frontmatter_full(file_path):
    """
    Extracts full YAML frontmatter from a markdown file.
    Returns dict of parsed fields or None if no frontmatter.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file starts with ---
        if not content.startswith('---'):
            return None

        # Find YAML block between first and second ---
        yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not yaml_match:
            return None

        yaml_content = yaml_match.group(1)
        fields = {}

        # Parse each field
        # Tags (can be list or single line with commas)
        tags_match = re.search(r'tags:\s*\[(.*?)\]', yaml_content, re.DOTALL)
        if tags_match:
            raw_tags = tags_match.group(1)
            # Split by comma, clean up
            tags = [t.strip().strip("'\"") for t in raw_tags.split(',') if t.strip()]
            fields['tags'] = tags
        else:
            # Try single-line format: tags: #tag1 #tag2
            tags_line = re.search(r'tags:\s*(.+?)(?:\n|$)', yaml_content)
            if tags_line:
                tags_text = tags_line.group(1).strip()
                tags = [t.strip() for t in tags_text.split() if t.strip()]
                fields['tags'] = tags

        # Aliases
        aliases_match = re.search(r'aliases:\s*\[(.*?)\]', yaml_content, re.DOTALL)
        if aliases_match:
            raw_aliases = aliases_match.group(1)
            aliases = [a.strip().strip("'\"") for a in raw_aliases.split(',') if a.strip()]
            fields['aliases'] = aliases
        else:
            # Try bullet list format
            alias_list = re.search(r'aliases:\s*\n((?:\s*-\s*.*\n?)+)', yaml_content)
            if alias_list:
                items = alias_list.group(1).split('\n')
                aliases = [i.strip().replace('- ', '').strip() for i in items if i.strip()]
                fields['aliases'] = aliases

        # Status (simple string field)
        status_match = re.search(r'status:\s*(.+?)(?:\n|$)', yaml_content)
        if status_match:
            fields['status'] = status_match.group(1).strip().strip("'\"").strip('[]')

        # Certainty (simple string field)
        certainty_match = re.search(r'certainty:\s*(.+?)(?:\n|$)', yaml_content)
        if certainty_match:
            fields['certainty'] = certainty_match.group(1).strip().strip("'\"").strip('[]')

        return fields

    except Exception as e:
        return None

def audit_metadata(root_dir):
    """
    Audit all notes for metadata compliance.
    Returns categorized results.
    """
    results = {
        'no_frontmatter': [],
        'missing_fields': defaultdict(list),
        'invalid_status': [],
        'invalid_certainty': [],
        'empty_tags': [],
        'empty_aliases': [],
        'compliant': [],
        'total_notes': 0
    }

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                filename = file[:-3]
                results['total_notes'] += 1

                # Parse frontmatter
                fields = parse_frontmatter_full(full_path)

                # Check 1: No frontmatter at all
                if fields is None:
                    results['no_frontmatter'].append((filename, full_path))
                    continue

                # Check 2: Missing required fields
                is_compliant = True
                for field in REQUIRED_FIELDS:
                    if field not in fields:
                        results['missing_fields'][field].append((filename, full_path))
                        is_compliant = False

                # Check 3: Invalid status value
                if 'status' in fields:
                    if fields['status'] not in VALID_STATUS:
                        results['invalid_status'].append((filename, full_path, fields['status']))
                        is_compliant = False

                # Check 4: Invalid certainty value
                if 'certainty' in fields:
                    if fields['certainty'] not in VALID_CERTAINTY:
                        results['invalid_certainty'].append((filename, full_path, fields['certainty']))
                        is_compliant = False

                # Check 5: Empty tags
                if 'tags' in fields:
                    if not fields['tags'] or len(fields['tags']) == 0:
                        results['empty_tags'].append((filename, full_path))
                        is_compliant = False

                # Check 6: Empty aliases (optional but should not be empty list if present)
                if 'aliases' in fields:
                    if not fields['aliases'] or len(fields['aliases']) == 0:
                        results['empty_aliases'].append((filename, full_path))
                        # Not marking as non-compliant since aliases can be empty

                if is_compliant:
                    results['compliant'].append((filename, full_path))

    return results

def print_report(results):
    """
    Output formatted metadata audit report.
    """
    total = results['total_notes']
    compliant = len(results['compliant'])
    no_fm = len(results['no_frontmatter'])

    print("=" * 60)
    print("📋 VAULT HEALTH: METADATA COMPLIANCE AUDIT")
    print("=" * 60)
    print(f"\n📊 Summary:")
    print(f"   Total Notes: {total}")
    print(f"   ✅ Fully Compliant: {compliant} ({compliant/total*100:.1f}%)")
    print(f"   ❌ Non-Compliant: {total - compliant} ({(total - compliant)/total*100:.1f}%)")

    # Issue 1: No Frontmatter
    if no_fm > 0:
        print(f"\n{'='*60}")
        print(f"🚨 CRITICAL: NO FRONTMATTER ({no_fm} files)")
        print(f"{'='*60}")
        print("These notes completely lack YAML metadata.\n")

        for filename, full_path in results['no_frontmatter'][:10]:
            rel_path = os.path.relpath(full_path)
            print(f"   ❌ [[{filename}]]")
            print(f"      📂 {rel_path}")

        if no_fm > 10:
            print(f"\n   ... and {no_fm - 10} more")

    # Issue 2: Missing Required Fields
    for field, notes in results['missing_fields'].items():
        if notes:
            print(f"\n⚠️  MISSING FIELD: '{field}' ({len(notes)} files)")
            for filename, full_path in notes[:5]:
                rel_path = os.path.relpath(full_path)
                print(f"   🟡 [[{filename}]]")
            if len(notes) > 5:
                print(f"   ... and {len(notes) - 5} more")

    # Issue 3: Invalid Status Values
    if results['invalid_status']:
        print(f"\n⚠️  INVALID STATUS VALUES ({len(results['invalid_status'])} files)")
        print(f"   Valid: {', '.join(VALID_STATUS)}\n")
        for filename, full_path, value in results['invalid_status'][:5]:
            print(f"   🟡 [[{filename}]] → status: {value}")
        if len(results['invalid_status']) > 5:
            print(f"   ... and {len(results['invalid_status']) - 5} more")

    # Issue 4: Invalid Certainty Values
    if results['invalid_certainty']:
        print(f"\n⚠️  INVALID CERTAINTY VALUES ({len(results['invalid_certainty'])} files)")
        print(f"   Valid: {', '.join(VALID_CERTAINTY)}\n")
        for filename, full_path, value in results['invalid_certainty'][:5]:
            print(f"   🟡 [[{filename}]] → certainty: {value}")
        if len(results['invalid_certainty']) > 5:
            print(f"   ... and {len(results['invalid_certainty']) - 5} more")

    # Issue 5: Empty Tags
    if results['empty_tags']:
        print(f"\n⚠️  EMPTY TAGS FIELD ({len(results['empty_tags'])} files)")
        for filename, full_path in results['empty_tags'][:5]:
            print(f"   🟡 [[{filename}]]")
        if len(results['empty_tags']) > 5:
            print(f"   ... and {len(results['empty_tags']) - 5} more")

    print("\n" + "=" * 60)
    print("💡 RECOMMENDATIONS:")
    print("   1. Add YAML frontmatter to all notes without it")
    print("   2. Ensure all notes have: tags, aliases, status, certainty")
    print("   3. Use valid status values: seedling, evergreen, reference")
    print("   4. Use valid certainty values: ^verified, ^speculative")
    print("   5. Populate tags field with at least primary domain tag")
    print("=" * 60)

def main():
    print("🔍 Auditing vault metadata compliance...\n")

    results = audit_metadata(".")
    print_report(results)

if __name__ == "__main__":
    main()
