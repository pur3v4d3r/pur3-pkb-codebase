"""
Wiki Link Extractor for Architecture of the Examined Life Series
Extracts all [[wiki-links]] from the markdown document and generates a comprehensive report
"""

import re
from collections import defaultdict, Counter
from pathlib import Path
from typing import Dict, List, Tuple


def extract_wiki_links(file_path: str) -> Dict:
    """
    Extract all wiki links from a markdown file and analyze their usage.
    
    Returns a dictionary with:
    - links: List of all unique wiki links
    - occurrences: Count of each link
    - contexts: First occurrence context for each link
    - sections: Section where each link first appears
    - reports: Report numbers where each link appears
    - link_positions: All positions for each link
    """
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match [[wiki-links]]
    wiki_link_pattern = r'\[\[([^\]]+)\]\]'
    
    # Find all wiki links with their positions
    all_links = []
    for match in re.finditer(wiki_link_pattern, content):
        link_text = match.group(1)
        position = match.start()
        all_links.append((link_text, position))
    
    # Count occurrences
    link_texts = [link[0] for link in all_links]
    occurrence_counts = Counter(link_texts)
    
    # Get unique links
    unique_links = sorted(set(link_texts))
    
    # Identify report boundaries
    report_boundaries = find_report_boundaries(content)
    
    # Extract context for first occurrence of each link and track reports
    contexts = {}
    sections = {}
    link_positions = defaultdict(list)
    link_reports = defaultdict(set)
    
    for link in unique_links:
        # Get all positions for this link
        positions = [pos for text, pos in all_links if text == link]
        link_positions[link] = positions
        
        # Find first occurrence
        first_pos = positions[0]
        
        # Extract surrounding context (100 chars before and after)
        context_start = max(0, first_pos - 100)
        context_end = min(len(content), first_pos + len(link) + 100)
        context = content[context_start:context_end].replace('\n', ' ').strip()
        contexts[link] = context
        
        # Find the section/heading this appears under
        section = find_section(content, first_pos)
        sections[link] = section
        
        # Determine which report(s) this link appears in
        for pos in positions:
            report = determine_report(pos, report_boundaries)
            if report:
                link_reports[link].add(report)
    
    return {
        'links': unique_links,
        'occurrences': occurrence_counts,
        'contexts': contexts,
        'sections': sections,
        'reports': link_reports,
        'link_positions': link_positions,
        'total_links': len(all_links),
        'unique_count': len(unique_links),
        'report_boundaries': report_boundaries
    }


def find_section(content: str, position: int) -> str:
    """Find the most recent heading before the given position."""
    # Look backwards from position to find the most recent heading
    text_before = content[:position]
    
    # Pattern for markdown headings
    heading_pattern = r'^(#{1,6})\s+(.+)$'
    
    # Find all headings before this position
    headings = []
    for match in re.finditer(heading_pattern, text_before, re.MULTILINE):
        level = len(match.group(1))
        title = match.group(2).strip()
        headings.append((level, title, match.start()))
    
    if headings:
        # Return the most recent heading
        return headings[-1][1]
    else:
        return "Document Start"


def find_report_boundaries(content: str) -> List[Tuple[int, int, str]]:
    """
    Find the boundaries of each report in the document.
    Returns a list of (start_pos, end_pos, report_name) tuples.
    """
    boundaries = []
    
    # Pattern to match report headers - looking for "Report XX" or "Phase" markers
    # Adjust this pattern based on your document structure
    report_pattern = r'^##?\s+(Report\s+\d+[:|—].*?|Phase\s+[IVX]+:.*?)$'
    
    matches = list(re.finditer(report_pattern, content, re.MULTILINE))
    
    for i, match in enumerate(matches):
        report_name = match.group(1).strip()
        start_pos = match.start()
        
        # End position is the start of the next report, or end of document
        if i < len(matches) - 1:
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(content)
        
        boundaries.append((start_pos, end_pos, report_name))
    
    return boundaries


def determine_report(position: int, report_boundaries: List[Tuple[int, int, str]]) -> str:
    """
    Determine which report a given position belongs to.
    """
    for start, end, name in report_boundaries:
        if start <= position < end:
            # Clean up the report name for display
            # Extract just "Report XX" or "Phase X" if possible
            if 'Report' in name:
                match = re.search(r'Report\s+(\d+)', name)
                if match:
                    return f"Report {match.group(1)}"
            elif 'Phase' in name:
                match = re.search(r'Phase\s+([IVX]+)', name)
                if match:
                    return f"Phase {match.group(1)}"
            return name[:50]  # Truncate long names
    
    return None


def find_section(content: str, position: int) -> str:
    """Find the most recent heading before the given position."""
    # Look backwards from position to find the most recent heading
    text_before = content[:position]
    
    # Pattern for markdown headings
    heading_pattern = r'^(#{1,6})\s+(.+)$'
    
    # Find all headings before this position
    headings = []
    for match in re.finditer(heading_pattern, text_before, re.MULTILINE):
        level = len(match.group(1))
        title = match.group(2).strip()
        headings.append((level, title, match.start()))
    
    if headings:
        # Return the most recent heading
        return headings[-1][1]
    else:
        return "Document Start"


def categorize_links(links: List[str]) -> Dict[str, List[str]]:
    """
    Categorize wiki links based on common patterns and keywords.
    """
    categories = {
        '🧠 Cognitive Concepts': [],
        '📚 Philosophical Frameworks': [],
        '🔬 Research & Empirical': [],
        '🎯 Practices & Methods': [],
        '👤 Virtue & Character': [],
        '🌟 Key Insights': [],
        '📖 Authors & Thinkers': [],
        '🔗 Cross-References': [],
        '🌍 Cultural & Social': [],
        '⚡ Miscellaneous': []
    }
    
    for link in links:
        link_lower = link.lower()
        
        # Categorization logic
        if any(word in link_lower for word in ['metacogn', 'cognit', 'thinking', 'reasoning', 'mind', 'mental', 'processing']):
            categories['🧠 Cognitive Concepts'].append(link)
        elif any(word in link_lower for word in ['virtue', 'character', 'intellectual', 'epistemic']):
            categories['👤 Virtue & Character'].append(link)
        elif any(word in link_lower for word in ['practice', 'method', 'technique', 'exercise', 'examination']):
            categories['🎯 Practices & Methods'].append(link)
        elif any(word in link_lower for word in ['framework', 'model', 'theory', 'philosophy', 'stoic', 'aristotle']):
            categories['📚 Philosophical Frameworks'].append(link)
        elif any(word in link_lower for word in ['research', 'study', 'empirical', 'evidence', 'experiment', 'neuroscience']):
            categories['🔬 Research & Empirical'].append(link)
        elif any(word in link_lower for word in ['insight', 'emergent', 'discovery', 'integration', 'personhood']):
            categories['🌟 Key Insights'].append(link)
        elif any(word in link_lower for word in ['report', 'phase', 'tier', 'dimension']):
            categories['🔗 Cross-References'].append(link)
        elif any(word in link_lower for word in ['cultural', 'social', 'ubuntu', 'confucian', 'buddhist']):
            categories['🌍 Cultural & Social'].append(link)
        elif link[0].isupper() and ' ' not in link and len(link) < 30:
            # Likely a person's name or proper noun
            categories['📖 Authors & Thinkers'].append(link)
        else:
            categories['⚡ Miscellaneous'].append(link)
    
    # Remove empty categories
    return {k: v for k, v in categories.items() if v}


def generate_markdown_report(data: Dict, output_path: str):
    """Generate a comprehensive markdown report of wiki links."""
    
    links = data['links']
    occurrences = data['occurrences']
    contexts = data['contexts']
    sections = data['sections']
    link_reports = data.get('reports', {})
    report_boundaries = data.get('report_boundaries', [])
    
    # Categorize links
    categorized = categorize_links(links)
    
    # Generate markdown
    md_content = []
    
    # Header
    md_content.append("# 📊 Wiki Links Catalog: Architecture of the Examined Life Series\n")
    md_content.append(f"*Generated on: {Path().absolute()}*\n")
    md_content.append("---\n")
    
    # Summary statistics
    md_content.append("## 📈 Summary Statistics\n")
    md_content.append(f"- **Total Wiki Links**: {data['total_links']}")
    md_content.append(f"- **Unique Concepts**: {data['unique_count']}")
    md_content.append(f"- **Categories**: {len(categorized)}\n")
    
    # Most referenced links
    md_content.append("## 🔥 Most Referenced Concepts\n")
    md_content.append("*Top concepts by frequency of mention*\n")
    most_common = occurrences.most_common(15)
    for i, (link, count) in enumerate(most_common, 1):
        if count > 1:
            md_content.append(f"{i}. **[[{link}]]** — {count} occurrences")
    md_content.append("")
    
    # Categorized links
    md_content.append("---\n")
    md_content.append("## 🗂️ Categorized Wiki Links\n")
    
    for category, category_links in categorized.items():
        md_content.append(f"\n### {category}\n")
        md_content.append(f"*{len(category_links)} concepts*\n")
        
        # Sort by occurrence count (descending)
        sorted_links = sorted(category_links, key=lambda x: occurrences[x], reverse=True)
        
        for link in sorted_links:
            count = occurrences[link]
            section = sections[link]
            
            # Format based on frequency
            if count > 1:
                md_content.append(f"- **[[{link}]]** ({count}×)")
            else:
                md_content.append(f"- [[{link}]]")
            
            # Add section info if useful
            if section and section != "Document Start":
                md_content.append(f"  - *First appears in: {section}*")
        
        md_content.append("")
    
    # Alphabetical index
    md_content.append("---\n")
    md_content.append("## 📖 Alphabetical Index\n")
    md_content.append("*Complete alphabetical listing of all wiki links*\n")
    
    current_letter = None
    for link in links:
        first_letter = link[0].upper()
        if first_letter != current_letter:
            current_letter = first_letter
            md_content.append(f"\n### {current_letter}\n")
        
        count = occurrences[link]
        if count > 1:
            md_content.append(f"- [[{link}]] — {count}×")
        else:
            md_content.append(f"- [[{link}]]")
    
    # Detailed reference table
    md_content.append("\n---\n")
    md_content.append("## 📋 Detailed Reference Table\n")
    md_content.append("*Complete reference with usage statistics*\n")
    md_content.append("\n| Wiki Link | Occurrences | First Mentioned In |\n")
    md_content.append("|-----------|-------------|--------------------|\n")
    
    for link in links:
        count = occurrences[link]
        section = sections[link]
        # Truncate section name if too long
        if len(section) > 50:
            section = section[:47] + "..."
        md_content.append(f"| [[{link}]] | {count} | {section} |\n")
    
    # Wiki Links by Report section
    if link_reports:
        md_content.append("\n---\n")
        md_content.append("## 📑 Wiki Links by Report/Phase\n")
        md_content.append("*Shows which reports or phases each concept appears in*\n")
        
        # Group reports for easier organization
        all_reports = set()
        for reports in link_reports.values():
            all_reports.update(reports)
        
        sorted_reports = sorted(all_reports, key=lambda x: (x.split()[0], int(x.split()[1]) if len(x.split()) > 1 and x.split()[1].isdigit() else 0))
        
        if sorted_reports:
            md_content.append(f"\n**Total Reports/Phases Detected**: {len(sorted_reports)}\n")
            md_content.append("\n### Concepts by Report\n")
            
            # Create a reverse index: report -> links
            reports_to_links = defaultdict(list)
            for link, reports in link_reports.items():
                for report in reports:
                    reports_to_links[report].append(link)
            
            for report in sorted_reports:
                links_in_report = sorted(reports_to_links[report])
                md_content.append(f"\n#### {report}\n")
                md_content.append(f"*{len(links_in_report)} concepts*\n")
                
                # Show top concepts by frequency in this report
                for link in links_in_report[:20]:  # Show top 20 per report
                    count = occurrences[link]
                    if count > 1:
                        md_content.append(f"- [[{link}]] ({count}× total)")
                    else:
                        md_content.append(f"- [[{link}]]")
                
                if len(links_in_report) > 20:
                    md_content.append(f"\n*...and {len(links_in_report) - 20} more concepts*\n")
            
            # Also show it the other way: link -> reports
            md_content.append("\n### Concept Distribution Across Reports\n")
            md_content.append("*Concepts that appear in multiple reports*\n")
            
            # Find concepts that appear in multiple reports
            multi_report_links = [(link, reports) for link, reports in link_reports.items() if len(reports) > 1]
            multi_report_links.sort(key=lambda x: (len(x[1]), occurrences[x[0]]), reverse=True)
            
            if multi_report_links:
                md_content.append("\n| Concept | Reports | Total Occurrences |\n")
                md_content.append("|---------|---------|-------------------|\n")
                
                for link, reports in multi_report_links[:30]:  # Show top 30 multi-report concepts
                    report_list = ", ".join(sorted(reports, key=lambda x: (x.split()[0], int(x.split()[1]) if len(x.split()) > 1 and x.split()[1].isdigit() else 0)))
                    count = occurrences[link]
                    md_content.append(f"| [[{link}]] | {report_list} | {count} |\n")
                
                if len(multi_report_links) > 30:
                    md_content.append(f"\n*...and {len(multi_report_links) - 30} more multi-report concepts*\n")
            else:
                md_content.append("\n*No concepts found in multiple reports.*\n")
    
    # Usage notes
    md_content.append("\n---\n")
    md_content.append("## 💡 Usage Notes\n")
    md_content.append("""
This catalog provides a comprehensive overview of all conceptual links used throughout 
the Architecture of the Examined Life series. Each wiki link represents a concept, 
framework, or idea that is referenced within the series.

### How to Use This Catalog:

1. **Exploration**: Browse categories to discover related concepts
2. **Navigation**: Use wiki links to create new notes expanding on these concepts
3. **Research**: Track which concepts are most central to the framework
4. **Learning**: Follow high-frequency concepts to understand core ideas
5. **Development**: Use this as a roadmap for PKB expansion

### Legend:

- **Bold links** indicate concepts mentioned multiple times
- *Italics* show where concepts first appear
- Numbers in parentheses (e.g., 5×) show occurrence count
- Categories group related conceptual domains

---

*This catalog is generated automatically and should be regenerated when the source document is updated.*
""")
    
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_content))
    
    print(f"✅ Wiki links catalog generated successfully!")
    print(f"📄 Output file: {output_path}")
    print(f"📊 Stats: {data['unique_count']} unique links from {data['total_links']} total references")


def main():
    """Main execution function."""
    # File paths
    input_file = "the-architecture-of-the-examined-life.md"
    output_file = "wiki-links-catalog.md"
    
    print("🔍 Extracting wiki links from Architecture of the Examined Life series...")
    print(f"📖 Reading: {input_file}")
    
    # Extract links
    data = extract_wiki_links(input_file)
    
    print(f"\n📊 Found {data['unique_count']} unique concepts in {data['total_links']} total references")
    
    # Generate report
    print(f"\n📝 Generating markdown catalog...")
    generate_markdown_report(data, output_file)
    
    print("\n✨ Done! Check the generated catalog for a comprehensive overview.")


if __name__ == "__main__":
    main()
