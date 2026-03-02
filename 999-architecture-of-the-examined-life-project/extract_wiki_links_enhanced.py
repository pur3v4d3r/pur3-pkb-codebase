"""
Enhanced Wiki Link Extractor for Architecture of the Examined Life Series
Comprehensive PKB analysis tool with multiple advanced features
"""

import re
from collections import defaultdict, Counter
from pathlib import Path
from typing import Dict, List, Tuple, Set
import json


class WikiLinkAnalyzer:
    """Comprehensive analyzer for wiki links in markdown documents."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        with open(file_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
        
        self.wiki_link_pattern = r'\[\[([^\]]+)\]\]'
        self.citation_pattern = r'\[!cite\].*?(?:\n|$)'
        self.definition_pattern = r'\[!definition\].*?\n>(.*?)(?:\n\n|\n>|$)'
        
        # Core data structures
        self.all_links = []
        self.link_positions = defaultdict(list)
        self.link_reports = defaultdict(set)
        self.link_contexts = {}
        self.link_sections = {}
        self.definitions = {}
        self.citations_by_concept = defaultdict(list)
        self.co_occurrences = defaultdict(lambda: defaultdict(int))
        self.context_types = defaultdict(lambda: defaultdict(int))
        self.hierarchical_relationships = defaultdict(set)
        self.concept_depth = {}
        
    def analyze(self):
        """Run complete analysis."""
        print("🔍 Running comprehensive wiki link analysis...")
        
        self._extract_links()
        self._find_report_boundaries()
        self._extract_definitions()
        self._analyze_citations()
        self._analyze_co_occurrences()
        self._classify_contexts()
        self._detect_hierarchies()
        self._analyze_depth()
        self._detect_missing_links()
        
        print("✅ Analysis complete!")
        
    def _extract_links(self):
        """Extract all wiki links with positions."""
        for match in re.finditer(self.wiki_link_pattern, self.content):
            link_text = match.group(1)
            position = match.start()
            self.all_links.append((link_text, position))
            self.link_positions[link_text].append(position)
            
            # Get context and section
            if link_text not in self.link_contexts:
                context = self._get_context(position, 150)
                self.link_contexts[link_text] = context
                self.link_sections[link_text] = self._find_section(position)
    
    def _find_report_boundaries(self):
        """Identify report/phase boundaries."""
        report_pattern = r'^##?\s+(Report\s+\d+[:|—].*?|Phase\s+[IVX]+:.*?)$'
        matches = list(re.finditer(report_pattern, self.content, re.MULTILINE))
        
        self.report_boundaries = []
        for i, match in enumerate(matches):
            report_name = match.group(1).strip()
            start_pos = match.start()
            end_pos = matches[i + 1].start() if i < len(matches) - 1 else len(self.content)
            self.report_boundaries.append((start_pos, end_pos, report_name))
        
        # Assign links to reports
        for link, positions in self.link_positions.items():
            for pos in positions:
                report = self._determine_report(pos)
                if report:
                    self.link_reports[link].add(report)
    
    def _extract_definitions(self):
        """Extract inline definitions from callouts and text."""
        # Extract from [!definition] callouts
        def_pattern = r'\[!definition\]\s*\[\[([^\]]+)\]\]\s*\n>(.*?)(?=\n\n|\n>|$)'
        for match in re.finditer(def_pattern, self.content, re.DOTALL):
            concept = match.group(1)
            definition = match.group(2).strip()
            # Clean up the definition text
            definition = re.sub(r'\s+', ' ', definition)
            self.definitions[concept] = {
                'text': definition,
                'type': 'callout',
                'length': len(definition)
            }
        
        # Extract from "is defined as" patterns
        for link in self.link_positions.keys():
            if link not in self.definitions:
                # Look for patterns like "[[X]] is defined as..."
                pattern = rf'\[\[{re.escape(link)}\]\]\s+(?:is\s+defined\s+as|refers\s+to|means)\s+([^.]+\.)'
                match = re.search(pattern, self.content, re.IGNORECASE)
                if match:
                    definition = match.group(1).strip()
                    self.definitions[link] = {
                        'text': definition,
                        'type': 'inline',
                        'length': len(definition)
                    }
    
    def _analyze_citations(self):
        """Track which concepts appear near citations."""
        cite_pattern = r'\[!cite\]([^\n]+)'
        
        for cite_match in re.finditer(cite_pattern, self.content):
            citation = cite_match.group(1).strip()
            cite_pos = cite_match.start()
            
            # Find concepts mentioned nearby (within 500 chars)
            nearby_start = max(0, cite_pos - 500)
            nearby_end = min(len(self.content), cite_pos + 500)
            nearby_text = self.content[nearby_start:nearby_end]
            
            for link in self.link_positions.keys():
                if f'[[{link}]]' in nearby_text:
                    self.citations_by_concept[link].append(citation)
    
    def _analyze_co_occurrences(self, window_size=500):
        """Analyze which concepts appear together."""
        # For each link position, find what other links appear nearby
        for link1, positions in self.link_positions.items():
            for pos1 in positions:
                window_start = max(0, pos1 - window_size)
                window_end = min(len(self.content), pos1 + window_size)
                
                for link2, positions2 in self.link_positions.items():
                    if link1 != link2:
                        for pos2 in positions2:
                            if window_start <= pos2 <= window_end:
                                self.co_occurrences[link1][link2] += 1
    
    def _classify_contexts(self):
        """Classify HOW each concept is used in context."""
        context_patterns = {
            'defining': r'(is\s+defined\s+as|refers\s+to|means|is\s+the)',
            'explaining': r'(helps\s+us\s+understand|explains|illuminates|reveals)',
            'questioning': r'(what\s+(?:is|does)|how\s+(?:does|can)|why)',
            'exemplifying': r'(for\s+example|such\s+as|instance|illustrated\s+by)',
            'contrasting': r'(unlike|in\s+contrast|however|whereas|but)',
            'integrating': r'(connects\s+to|relates\s+to|synthesizes|combines)',
            'citing': r'(\(Report|\[!cite\]|research|study|evidence)'
        }
        
        for link, positions in self.link_positions.items():
            for pos in positions:
                context = self._get_context(pos, 200).lower()
                
                for ctx_type, pattern in context_patterns.items():
                    if re.search(pattern, context):
                        self.context_types[link][ctx_type] += 1
    
    def _detect_hierarchies(self):
        """Detect parent-child concept relationships."""
        # Patterns indicating hierarchy
        hierarchy_patterns = [
            (r'\[\[([^\]]+)\]\]\s+(?:is\s+a\s+type\s+of|is\s+a\s+form\s+of)\s+\[\[([^\]]+)\]\]', 'child', 'parent'),
            (r'\[\[([^\]]+)\]\]\s+includes\s+\[\[([^\]]+)\]\]', 'parent', 'child'),
            (r'\[\[([^\]]+)\]\]\s*—\s*\[\[([^\]]+)\]\]', 'specific', 'general'),
        ]
        
        for pattern, rel1, rel2 in hierarchy_patterns:
            for match in re.finditer(pattern, self.content):
                concept1 = match.group(1)
                concept2 = match.group(2)
                
                if rel1 == 'child':
                    self.hierarchicalical_relationships[concept2].add(concept1)
                else:
                    self.hierarchical_relationships[concept1].add(concept2)
    
    def _analyze_depth(self):
        """Measure how deeply each concept is explored."""
        for link in self.link_positions.keys():
            # Count paragraphs mentioning the concept
            paragraphs = self.content.split('\n\n')
            para_count = sum(1 for p in paragraphs if f'[[{link}]]' in p)
            
            # Count words in paragraphs mentioning the concept
            word_count = sum(
                len(p.split()) for p in paragraphs if f'[[{link}]]' in p
            )
            
            # Check if it appears in headings
            heading_pattern = rf'^#+\s+.*\[\[{re.escape(link)}\]\]'
            in_heading = bool(re.search(heading_pattern, self.content, re.MULTILINE))
            
            self.concept_depth[link] = {
                'paragraphs': para_count,
                'words': word_count,
                'in_heading': in_heading,
                'depth_score': para_count * 10 + (100 if in_heading else 0)
            }
    
    def _detect_missing_links(self):
        """Find concept mentions that should be wiki-linked but aren't."""
        self.missing_links = defaultdict(int)
        
        # For each existing wiki link, look for unlinked mentions
        for link in self.link_positions.keys():
            # Skip very short or common words
            if len(link) < 4 or link.lower() in ['the', 'and', 'for', 'with']:
                continue
            
            # Look for the text appearing without wiki-link formatting
            # Negative lookbehind for [[ and negative lookahead for ]]
            pattern = rf'(?<!\[\[){re.escape(link)}(?!\]\])'
            
            unlinked_matches = list(re.finditer(pattern, self.content, re.IGNORECASE))
            
            # Exclude matches that are already part of other wiki links
            for match in unlinked_matches:
                pos = match.start()
                # Check if this is inside a wiki link
                if not self._is_inside_wikilink(pos):
                    self.missing_links[link] += 1
    
    def _is_inside_wikilink(self, pos):
        """Check if a position is inside a wiki link."""
        # Look backwards for [[ and forwards for ]]
        backward_text = self.content[max(0, pos-100):pos]
        forward_text = self.content[pos:min(len(self.content), pos+100)]
        
        last_open = backward_text.rfind('[[')
        last_close = backward_text.rfind(']]')
        next_close = forward_text.find(']]')
        
        # If we find [[ before ]] going backward, and ]] going forward, we're inside
        return last_open > last_close and next_close != -1
    
    def _get_context(self, position, size=150):
        """Extract context around a position."""
        start = max(0, position - size)
        end = min(len(self.content), position + size)
        return self.content[start:end].replace('\n', ' ').strip()
    
    def _find_section(self, position):
        """Find the section heading before a position."""
        text_before = self.content[:position]
        heading_pattern = r'^(#{1,6})\s+(.+)$'
        
        headings = []
        for match in re.finditer(heading_pattern, text_before, re.MULTILINE):
            level = len(match.group(1))
            title = match.group(2).strip()
            headings.append((level, title, match.start()))
        
        if headings:
            return headings[-1][1]
        return "Document Start"
    
    def _determine_report(self, position):
        """Determine which report a position belongs to."""
        for start, end, name in self.report_boundaries:
            if start <= position < end:
                if 'Report' in name:
                    match = re.search(r'Report\s+(\d+)', name)
                    if match:
                        return f"Report {match.group(1)}"
                elif 'Phase' in name:
                    match = re.search(r'Phase\s+([IVX]+)', name)
                    if match:
                        return f"Phase {match.group(1)}"
                return name[:50]
        return None
    
    def get_statistics(self):
        """Get comprehensive statistics."""
        occurrence_counts = Counter([link for link, _ in self.all_links])
        unique_links = sorted(set(link for link, _ in self.all_links))
        
        return {
            'total_links': len(self.all_links),
            'unique_concepts': len(unique_links),
            'links': unique_links,
            'occurrences': occurrence_counts,
            'contexts': self.link_contexts,
            'sections': self.link_sections,
            'reports': dict(self.link_reports),
            'definitions': self.definitions,
            'citations': dict(self.citations_by_concept),
            'co_occurrences': dict(self.co_occurrences),
            'context_types': dict(self.context_types),
            'hierarchies': dict(self.hierarchical_relationships),
            'depth': self.concept_depth,
            'missing_links': dict(self.missing_links),
            'report_boundaries': self.report_boundaries
        }


def generate_comprehensive_report(data: Dict, output_path: str):
    """Generate comprehensive markdown report with all analyses."""
    
    md = []
    
    # Header
    md.append("# 📊 Comprehensive Wiki Links Analysis")
    md.append("*Architecture of the Examined Life Series*\n")
    md.append("---\n")
    
    # Table of Contents
    md.append("## 📑 Table of Contents\n")
    md.append("1. [Summary Statistics](#summary-statistics)")
    md.append("2. [Most Referenced Concepts](#most-referenced-concepts)")
    md.append("3. [Concept Definitions](#concept-definitions)")
    md.append("4. [Co-Occurrence Analysis](#co-occurrence-analysis)")
    md.append("5. [Context Classification](#context-classification)")
    md.append("6. [Citation Tracking](#citation-tracking)")
    md.append("7. [Hierarchical Relationships](#hierarchical-relationships)")
    md.append("8. [Depth Analysis](#depth-analysis)")
    md.append("9. [Missing Links Detection](#missing-links-detection)")
    md.append("10. [Learning Pathways](#learning-pathways)")
    md.append("11. [Quality Report](#quality-report)")
    md.append("12. [Dataview Queries](#dataview-queries)")
    md.append("13. [Concept Stubs for PKB](#concept-stubs-for-pkb)")
    md.append("14. [Reports Distribution](#reports-distribution)\n")
    md.append("---\n")
    
    # 1. Summary Statistics
    md.append("## 📈 Summary Statistics\n")
    md.append(f"- **Total Wiki Links**: {data['total_links']}")
    md.append(f"- **Unique Concepts**: {data['unique_concepts']}")
    md.append(f"- **Concepts with Definitions**: {len(data['definitions'])}")
    md.append(f"- **Concepts with Citations**: {len(data['citations'])}")
    md.append(f"- **Detected Hierarchies**: {sum(len(children) for children in data['hierarchies'].values())}")
    md.append(f"- **Missing Link Opportunities**: {sum(data['missing_links'].values())}\n")
    md.append("---\n")
    
    # 2. Most Referenced Concepts
    md.append("## 🔥 Most Referenced Concepts\n")
    most_common = data['occurrences'].most_common(20)
    for i, (link, count) in enumerate(most_common, 1):
        depth = data['depth'].get(link, {})
        depth_score = depth.get('depth_score', 0)
        md.append(f"{i}. **[[{link}]]** — {count}× mentions, {depth_score} depth score")
    md.append("\n---\n")
    
    # 3. Concept Definitions
    md.append("## 📖 Concept Definitions\n")
    md.append("*Automatically extracted definitions from the text*\n")
    
    for concept, def_data in sorted(data['definitions'].items()):
        md.append(f"\n### [[{concept}]]\n")
        md.append(f"**Type**: {def_data['type'].title()}")
        md.append(f"**Length**: {def_data['length']} characters\n")
        md.append(f"> {def_data['text']}\n")
    
    md.append("---\n")
    
    # 4. Co-Occurrence Analysis
    md.append("## 🔗 Co-Occurrence Analysis\n")
    md.append("*Concepts that frequently appear together (within 500 chars)*\n")
    
    # Find strongest co-occurrences
    all_co_occur = []
    for concept1, related in data['co_occurrences'].items():
        for concept2, count in related.items():
            if count >= 3:  # Only show significant co-occurrences
                # Avoid duplicates (A-B and B-A)
                pair = tuple(sorted([concept1, concept2]))
                all_co_occur.append((pair, count))
    
    # Remove duplicates and sort
    unique_co_occur = {}
    for pair, count in all_co_occur:
        if pair not in unique_co_occur:
            unique_co_occur[pair] = count
        else:
            unique_co_occur[pair] = max(unique_co_occur[pair], count)
    
    sorted_co_occur = sorted(unique_co_occur.items(), key=lambda x: x[1], reverse=True)[:30]
    
    md.append("\n| Concept Pair | Co-occurrences |")
    md.append("|--------------|----------------|")
    for (c1, c2), count in sorted_co_occur:
        md.append(f"| [[{c1}]] ↔ [[{c2}]] | {count}× |")
    
    md.append("\n---\n")
    
    # 5. Context Classification
    md.append("## 🎯 Context Classification\n")
    md.append("*How concepts are used in the text*\n")
    
    # Show top concepts by usage type
    usage_types = ['defining', 'explaining', 'questioning', 'exemplifying', 'contrasting', 'integrating', 'citing']
    
    for usage_type in usage_types:
        md.append(f"\n### {usage_type.title()} Contexts\n")
        
        concepts_of_type = []
        for concept, types in data['context_types'].items():
            if usage_type in types and types[usage_type] > 0:
                concepts_of_type.append((concept, types[usage_type]))
        
        concepts_of_type.sort(key=lambda x: x[1], reverse=True)
        
        for concept, count in concepts_of_type[:15]:
            md.append(f"- [[{concept}]] — {count}× {usage_type}")
    
    md.append("\n---\n")
    
    # 6. Citation Tracking
    md.append("## 📚 Citation Tracking\n")
    md.append("*Concepts linked to scholarly sources*\n")
    
    cited_concepts = [(c, cites) for c, cites in data['citations'].items() if cites]
    cited_concepts.sort(key=lambda x: len(x[1]), reverse=True)
    
    for concept, citations in cited_concepts[:20]:
        md.append(f"\n### [[{concept}]]\n")
        md.append(f"**{len(citations)} citation(s)**\n")
        for cite in citations[:3]:  # Show first 3
            md.append(f"- {cite[:100]}...")
    
    md.append("\n---\n")
    
    # 7. Hierarchical Relationships
    md.append("## 🌳 Hierarchical Relationships\n")
    md.append("*Parent-child concept structures*\n")
    
    if data['hierarchies']:
        for parent, children in sorted(data['hierarchies'].items()):
            if children:
                md.append(f"\n### [[{parent}]]\n")
                for child in sorted(children):
                    md.append(f"- [[{child}]]")
    else:
        md.append("*No explicit hierarchical relationships detected*\n")
    
    md.append("\n---\n")
    
    # 8. Depth Analysis
    md.append("## 📊 Depth Analysis\n")
    md.append("*How thoroughly each concept is explored*\n")
    
    # Sort by depth score
    depth_sorted = sorted(
        data['depth'].items(),
        key=lambda x: x[1]['depth_score'],
        reverse=True
    )[:30]
    
    md.append("\n| Concept | Paragraphs | Words | In Heading | Depth Score |")
    md.append("|---------|------------|-------|------------|-------------|")
    
    for concept, depth in depth_sorted:
        heading_mark = "✓" if depth['in_heading'] else ""
        md.append(f"| [[{concept}]] | {depth['paragraphs']} | {depth['words']} | {heading_mark} | {depth['depth_score']} |")
    
    md.append("\n---\n")
    
    # 9. Missing Links Detection
    md.append("## ⚠️ Missing Links Detection\n")
    md.append("*Concepts mentioned but not wiki-linked*\n")
    
    missing_sorted = sorted(data['missing_links'].items(), key=lambda x: x[1], reverse=True)[:30]
    
    md.append("\n| Concept | Unlinked Mentions |")
    md.append("|---------|-------------------|")
    
    for concept, count in missing_sorted:
        if count > 2:  # Only show significant cases
            md.append(f"| {concept} | {count}× |")
    
    md.append("\n*Recommendation: Consider adding wiki-links for consistency*\n")
    md.append("---\n")
    
    # 10. Learning Pathways
    md.append("## 🎓 Learning Pathways\n")
    md.append("*Suggested reading order based on concept dependencies*\n")
    
    # Create beginner, intermediate, advanced based on depth and co-occurrence
    beginner = []
    intermediate = []
    advanced = []
    
    for concept, depth in data['depth'].items():
        occurrences = data['occurrences'][concept]
        co_occur_count = len(data['co_occurrences'].get(concept, {}))
        
        if depth['in_heading'] and occurrences >= 10:
            beginner.append((concept, occurrences))
        elif co_occur_count >= 5:
            intermediate.append((concept, co_occur_count))
        elif occurrences >= 3:
            advanced.append((concept, occurrences))
    
    md.append("\n### 🌱 Beginner Path (Core Framework Concepts)\n")
    md.append("*Start with these foundational concepts*\n")
    for concept, _ in sorted(beginner, key=lambda x: x[1], reverse=True)[:10]:
        md.append(f"- [[{concept}]]")
    
    md.append("\n### 🌿 Intermediate Path (Integrated Concepts)\n")
    md.append("*Concepts that connect to many others*\n")
    for concept, _ in sorted(intermediate, key=lambda x: x[1], reverse=True)[:10]:
        md.append(f"- [[{concept}]]")
    
    md.append("\n### 🌳 Advanced Path (Specialized Topics)\n")
    md.append("*Deep dives and specialized applications*\n")
    for concept, _ in sorted(advanced, key=lambda x: x[1], reverse=True)[:10]:
        md.append(f"- [[{concept}]]")
    
    md.append("\n---\n")
    
    # 11. Quality Report
    md.append("## ✅ Quality Report\n")
    md.append("*PKB health check and recommendations*\n")
    
    # Calculate metrics
    total_concepts = data['unique_concepts']
    defined_concepts = len(data['definitions'])
    cited_concepts = len([c for c, cites in data['citations'].items() if cites])
    orphan_concepts = len([c for c, d in data['depth'].items() if d['paragraphs'] == 1])
    deep_concepts = len([c for c, d in data['depth'].items() if d['depth_score'] > 50])
    
    md.append(f"\n### Coverage Metrics\n")
    md.append(f"- **Definition Coverage**: {defined_concepts}/{total_concepts} ({100*defined_concepts//total_concepts}%)")
    md.append(f"- **Citation Coverage**: {cited_concepts}/{total_concepts} ({100*cited_concepts//total_concepts if total_concepts > 0 else 0}%)")
    md.append(f"- **Deep Exploration**: {deep_concepts}/{total_concepts} ({100*deep_concepts//total_concepts}%)")
    md.append(f"- **Orphan Concepts**: {orphan_concepts} (mentioned only once)")
    
    md.append(f"\n### Recommendations\n")
    if defined_concepts < total_concepts * 0.3:
        md.append("- ⚠️ Add more explicit definitions for key concepts")
    if orphan_concepts > total_concepts * 0.4:
        md.append("- ⚠️ Expand development of single-mention concepts or remove them")
    md.append("- ✓ Continue building connections between related concepts")
    md.append("- ✓ Use the stub notes (below) to systematically build out the PKB")
    
    md.append("\n---\n")
    
    # 12. Dataview Queries
    md.append("## 📊 Dataview Queries for Obsidian\n")
    md.append("*Ready-to-use queries for your PKB*\n")
    
    md.append('\n### List All Concepts by Category\n')
    md.append('```dataview')
    md.append('TABLE')
    md.append('  tags as "Tags",')
    md.append('  length(file.inlinks) as "Backlinks",')
    md.append('  length(file.outlinks) as "Outlinks"')
    md.append('WHERE contains(tags, "#examined-life")')
    md.append('SORT length(file.inlinks) DESC')
    md.append('```\n')
    
    md.append('### Concepts Mentioned Most Frequently\n')
    md.append('```dataview')
    md.append('TABLE')
    md.append('  occurrences as "Mentions",')
    md.append('  reports as "Reports"')
    md.append('WHERE contains(tags, "#concept")')
    md.append('SORT occurrences DESC')
    md.append('LIMIT 20')
    md.append('```\n')
    
    md.append('### Undefined Concepts (Need Development)\n')
    md.append('```dataview')
    md.append('TABLE')
    md.append('  file.inlinks as "Mentioned In"')
    md.append('WHERE contains(tags, "#concept") AND !defined')
    md.append('SORT length(file.inlinks) DESC')
    md.append('```\n')
    
    md.append("---\n")
    
    # 13. Concept Stubs for PKB
    md.append("## 📝 Auto-Generated Concept Stubs\n")
    md.append("*Copy these to create skeleton notes for top concepts*\n")
    
    top_concepts = data['occurrences'].most_common(20)
    
    for concept, count in top_concepts:
        md.append(f"\n### Stub: {concept}.md\n")
        md.append("```markdown")
        md.append("---")
        md.append("tags: #concept #examined-life #needs-development")
        
        # Add relevant report tags
        if concept in data['reports']:
            reports = sorted(data['reports'][concept])
            md.append(f"reports: {', '.join(reports)}")
        
        md.append(f"occurrences: {count}")
        
        if concept in data['definitions']:
            md.append("defined: true")
        
        md.append("---\n")
        md.append(f"# {concept}\n")
        
        # Add definition if available
        if concept in data['definitions']:
            md.append("## Definition\n")
            md.append(f"> {data['definitions'][concept]['text']}\n")
        else:
            md.append("## Definition\n")
            md.append("*Definition needed*\n")
        
        # Add related concepts
        if concept in data['co_occurrences']:
            related = sorted(
                data['co_occurrences'][concept].items(),
                key=lambda x: x[1],
                reverse=True
            )[:5]
            if related:
                md.append("## Related Concepts\n")
                for related_concept, co_count in related:
                    md.append(f"- [[{related_concept}]] ({co_count}× co-occurrence)")
                md.append("")
        
        # Add where it appears
        if concept in data['reports']:
            md.append("## Appears In\n")
            for report in sorted(data['reports'][concept]):
                md.append(f"- {report}")
            md.append("")
        
        # Add citations if available
        if concept in data['citations'] and data['citations'][concept]:
            md.append("## Key Citations\n")
            for citation in data['citations'][concept][:2]:
                md.append(f"- {citation[:100]}...")
            md.append("")
        
        md.append("## Notes\n")
        md.append("*Add your synthesis and insights here*\n")
        
        md.append("## Development Status\n")
        md.append("- [ ] Definition added")
        md.append("- [ ] Examples provided")
        md.append("- [ ] Connections mapped")
        md.append("- [ ] Practice applications identified")
        
        md.append("```\n")
    
    md.append("---\n")
    
    # 14. Reports Distribution
    md.append("## 📑 Concept Distribution Across Reports\n")
    
    # Group concepts by report
    report_concepts = defaultdict(list)
    for concept, reports in data['reports'].items():
        for report in reports:
            report_concepts[report].append((concept, data['occurrences'][concept]))
    
    for report in sorted(report_concepts.keys()):
        concepts = sorted(report_concepts[report], key=lambda x: x[1], reverse=True)
        md.append(f"\n### {report}\n")
        md.append(f"*{len(concepts)} concepts*\n")
        
        for concept, count in concepts[:15]:  # Top 15 per report
            md.append(f"- [[{concept}]] ({count}×)")
        
        if len(concepts) > 15:
            md.append(f"\n*...and {len(concepts) - 15} more*\n")
    
    # Multi-report concepts
    md.append("\n### Cross-Report Integration\n")
    md.append("*Concepts appearing in multiple reports*\n")
    
    multi_report = [(c, rs) for c, rs in data['reports'].items() if len(rs) > 1]
    multi_report.sort(key=lambda x: len(x[1]), reverse=True)
    
    md.append("\n| Concept | Reports | Occurrences |")
    md.append("|---------|---------|-------------|")
    
    for concept, reports in multi_report[:20]:
        report_list = ", ".join(sorted(reports))
        count = data['occurrences'][concept]
        md.append(f"| [[{concept}]] | {report_list} | {count}× |")
    
    md.append("\n---\n")
    
    # Footer
    md.append("## 💡 Using This Analysis\n")
    md.append("""
This comprehensive analysis provides multiple entry points for building your PKB:

1. **Start with Definitions**: Use the extracted definitions to create initial notes
2. **Follow Co-occurrences**: Build connections between related concepts
3. **Use Depth Analysis**: Prioritize well-developed concepts for early PKB building
4. **Apply Learning Pathways**: Create guided reading experiences for family
5. **Generate Stubs**: Use the auto-generated stubs as templates
6. **Track Missing Links**: Improve document consistency
7. **Monitor Quality**: Use metrics to guide PKB development priorities

---

*This analysis is automatically generated. Regenerate after document updates.*
""")
    
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    
    print(f"✅ Comprehensive report generated!")
    print(f"📄 Output: {output_path}")


def main():
    """Main execution."""
    input_file = "the-architecture-of-the-examined-life.md"
    output_file = "wiki-links-comprehensive-analysis.md"
    
    print("🚀 Starting Enhanced Wiki Link Analysis...")
    print(f"📖 Input: {input_file}\n")
    
    # Create analyzer
    analyzer = WikiLinkAnalyzer(input_file)
    
    # Run analysis
    analyzer.analyze()
    
    # Get statistics
    data = analyzer.get_statistics()
    
    # Generate report
    print("\n📝 Generating comprehensive report...")
    generate_comprehensive_report(data, output_file)
    
    print(f"\n📊 Analysis Summary:")
    print(f"   - {data['total_links']} total wiki link references")
    print(f"   - {data['unique_concepts']} unique concepts")
    print(f"   - {len(data['definitions'])} concepts with definitions")
    print(f"   - {len(data['citations'])} concepts with citations")
    print(f"   - {sum(len(children) for children in data['hierarchies'].values())} hierarchical relationships")
    print(f"   - {sum(data['missing_links'].values())} missing link opportunities")
    
    print("\n✨ Done! Check the comprehensive analysis file.")


if __name__ == "__main__":
    main()
