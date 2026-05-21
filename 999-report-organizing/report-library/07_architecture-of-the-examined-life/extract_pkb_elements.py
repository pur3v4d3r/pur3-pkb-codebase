"""
PKB Elements Extractor for Architecture of the Examined Life Series
Extracts callouts, quotes, questions, examples, headings, and other valuable PKB building blocks
"""

import re
from collections import defaultdict, Counter
from pathlib import Path
from typing import Dict, List, Tuple
import json


class PKBElementExtractor:
    """Extract all valuable elements for PKB building."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        with open(file_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
            self.lines = self.content.split('\n')
        
        # Storage for extracted elements
        self.callouts = defaultdict(list)
        self.blockquotes = []
        self.headings = []
        self.questions = []
        self.examples = []
        self.key_claims = []
        self.definitions = []
        self.tables = []
        self.lists = []
        self.emphasis = {'bold': [], 'italic': []}
        self.cross_references = []
        self.tags = Counter()
        self.empirical_findings = []
        self.practical_applications = []
        self.frameworks = []
        self.principles = []
        self.warnings = []
        
    def extract_all(self):
        """Run all extraction methods."""
        print("🔍 Extracting PKB elements...")
        
        self._extract_callouts()
        self._extract_blockquotes()
        self._extract_headings()
        self._extract_questions()
        self._extract_examples()
        self._extract_key_claims()
        self._extract_definitions()
        self._extract_tables()
        self._extract_lists()
        self._extract_emphasis()
        self._extract_cross_references()
        self._extract_tags()
        self._extract_empirical_findings()
        self._extract_practical_applications()
        self._extract_frameworks()
        self._extract_principles()
        self._extract_warnings()
        
        print("✅ Extraction complete!")
        
    def _extract_callouts(self):
        """Extract all Obsidian callouts by type."""
        # Pattern: > [!type] content
        callout_pattern = r'>\s*\[!([^\]]+)\]\s*([^\n]*)\n((?:>.*\n?)*)'
        
        for match in re.finditer(callout_pattern, self.content):
            callout_type = match.group(1).strip()
            title = match.group(2).strip()
            content_lines = match.group(3).strip()
            
            # Clean up content (remove > prefix)
            content = '\n'.join(line[1:].strip() if line.startswith('>') else line 
                              for line in content_lines.split('\n'))
            
            self.callouts[callout_type].append({
                'title': title,
                'content': content,
                'position': match.start(),
                'section': self._find_section_at_position(match.start())
            })
    
    def _extract_blockquotes(self):
        """Extract regular blockquotes (not callouts)."""
        lines = self.content.split('\n')
        current_quote = []
        quote_start = -1
        
        for i, line in enumerate(lines):
            # Check if it's a blockquote but not a callout
            if line.startswith('>') and not re.match(r'>\s*\[!', line):
                if not current_quote:
                    quote_start = i
                current_quote.append(line[1:].strip())
            elif current_quote:
                # End of quote
                self.blockquotes.append({
                    'text': ' '.join(current_quote),
                    'line': quote_start,
                    'section': self._find_section_at_line(quote_start)
                })
                current_quote = []
    
    def _extract_headings(self):
        """Extract all headings with hierarchy."""
        heading_pattern = r'^(#{1,6})\s+(.+)$'
        
        for i, line in enumerate(self.lines):
            match = re.match(heading_pattern, line)
            if match:
                level = len(match.group(1))
                text = match.group(2).strip()
                
                # Remove any markdown formatting from heading
                clean_text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
                clean_text = re.sub(r'\*([^*]+)\*', r'\1', clean_text)
                clean_text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', clean_text)
                
                self.headings.append({
                    'level': level,
                    'text': text,
                    'clean_text': clean_text,
                    'line': i,
                    'parent': self._find_parent_heading(level, i)
                })
    
    def _find_parent_heading(self, level, line_num):
        """Find the parent heading for a given heading."""
        for heading in reversed(self.headings):
            if heading['level'] < level and heading['line'] < line_num:
                return heading['text']
        return None
    
    def _extract_questions(self):
        """Extract all questions from the text."""
        # Look for sentences ending in ?
        question_pattern = r'([A-Z][^.!?]*\?)'
        
        for match in re.finditer(question_pattern, self.content):
            question = match.group(1).strip()
            
            # Clean up wiki links for readability
            clean_q = re.sub(r'\[\[([^\]]+)\]\]', r'\1', question)
            
            # Skip very short questions (likely fragments)
            if len(clean_q) > 15:
                self.questions.append({
                    'text': clean_q,
                    'original': question,
                    'position': match.start(),
                    'section': self._find_section_at_position(match.start())
                })
    
    def _extract_examples(self):
        """Extract examples from the text."""
        # Pattern: "For example", "such as", "e.g.", ", say, "
        example_patterns = [
            r'[Ff]or example[,:]?\s*([^.!?]+[.!?])',
            r'[Ss]uch as\s+([^.!?]+[.!?])',
            r'e\.g\.,?\s*([^.!?]+[.!?])',
            r'[Cc]onsider[,:]?\s*([^.!?]+[.!?])',
            r'[Ii]magine[,:]?\s*([^.!?]+[.!?])',
        ]
        
        for pattern in example_patterns:
            for match in re.finditer(pattern, self.content):
                example = match.group(1).strip()
                
                if len(example) > 20:  # Meaningful examples
                    self.examples.append({
                        'text': example,
                        'position': match.start(),
                        'section': self._find_section_at_position(match.start())
                    })
    
    def _extract_key_claims(self):
        """Extract key claims and assertions."""
        # Patterns for important claims
        claim_patterns = [
            r'The key (?:point|insight|claim) is that ([^.!?]+[.!?])',
            r'The crucial (?:point|insight|claim) is that ([^.!?]+[.!?])',
            r'It is important to (?:note|recognize|understand) that ([^.!?]+[.!?])',
            r'The central (?:claim|argument|thesis) is ([^.!?]+[.!?])',
            r'This demonstrates that ([^.!?]+[.!?])',
            r'This reveals that ([^.!?]+[.!?])',
            r'This suggests that ([^.!?]+[.!?])',
        ]
        
        for pattern in claim_patterns:
            for match in re.finditer(pattern, self.content, re.IGNORECASE):
                claim = match.group(1).strip()
                
                if len(claim) > 20:
                    self.key_claims.append({
                        'text': claim,
                        'position': match.start(),
                        'section': self._find_section_at_position(match.start())
                    })
    
    def _extract_definitions(self):
        """Extract explicit definitions."""
        # Patterns for definitions
        def_patterns = [
            r'\*\*([^*]+)\*\*\s+is\s+defined\s+as\s+([^.!?]+[.!?])',
            r'\*\*([^*]+)\*\*\s+refers\s+to\s+([^.!?]+[.!?])',
            r'\*\*([^*]+)\*\*\s+means\s+([^.!?]+[.!?])',
            r'\[\[([^\]]+)\]\]\s+is\s+defined\s+as\s+([^.!?]+[.!?])',
            r'\[\[([^\]]+)\]\]\s+refers\s+to\s+([^.!?]+[.!?])',
            r'\[\[([^\]]+)\]\]\s+means\s+([^.!?]+[.!?])',
        ]
        
        for pattern in def_patterns:
            for match in re.finditer(pattern, self.content, re.IGNORECASE):
                term = match.group(1).strip()
                definition = match.group(2).strip()
                
                self.definitions.append({
                    'term': term,
                    'definition': definition,
                    'position': match.start(),
                    'section': self._find_section_at_position(match.start())
                })
    
    def _extract_tables(self):
        """Extract markdown tables."""
        # Find table blocks
        in_table = False
        current_table = []
        table_start_line = -1
        
        for i, line in enumerate(self.lines):
            if '|' in line and line.strip().startswith('|'):
                if not in_table:
                    in_table = True
                    table_start_line = i
                current_table.append(line)
            elif in_table:
                # End of table
                if len(current_table) >= 2:  # At least header + separator
                    self.tables.append({
                        'lines': current_table,
                        'start_line': table_start_line,
                        'section': self._find_section_at_line(table_start_line),
                        'rows': len(current_table) - 2  # Subtract header and separator
                    })
                in_table = False
                current_table = []
    
    def _extract_lists(self):
        """Extract bulleted and numbered lists."""
        # Patterns for list items
        bullet_pattern = r'^[\s]*[-*+]\s+(.+)$'
        number_pattern = r'^[\s]*\d+\.\s+(.+)$'
        
        current_list = {'type': None, 'items': [], 'line': -1}
        
        for i, line in enumerate(self.lines):
            bullet_match = re.match(bullet_pattern, line)
            number_match = re.match(number_pattern, line)
            
            if bullet_match or number_match:
                item_text = bullet_match.group(1) if bullet_match else number_match.group(1)
                list_type = 'bullet' if bullet_match else 'numbered'
                
                if current_list['type'] == list_type or current_list['type'] is None:
                    if current_list['type'] is None:
                        current_list['line'] = i
                        current_list['type'] = list_type
                        current_list['section'] = self._find_section_at_line(i)
                    current_list['items'].append(item_text.strip())
                else:
                    # Different list type - save current and start new
                    if current_list['items']:
                        self.lists.append(dict(current_list))
                    current_list = {
                        'type': list_type,
                        'items': [item_text.strip()],
                        'line': i,
                        'section': self._find_section_at_line(i)
                    }
            else:
                # Not a list item
                if current_list['items']:
                    self.lists.append(dict(current_list))
                    current_list = {'type': None, 'items': [], 'line': -1}
    
    def _extract_emphasis(self):
        """Extract bold and italic text."""
        # Bold: **text** or __text__
        bold_pattern = r'\*\*([^*]+)\*\*|__([^_]+)__'
        for match in re.finditer(bold_pattern, self.content):
            text = match.group(1) or match.group(2)
            if len(text.strip()) > 2:  # Skip very short emphasis
                self.emphasis['bold'].append({
                    'text': text.strip(),
                    'position': match.start(),
                    'section': self._find_section_at_position(match.start())
                })
        
        # Italic: *text* or _text_ (but not part of bold)
        italic_pattern = r'(?<!\*)\*([^*]+)\*(?!\*)|(?<!_)_([^_]+)_(?!_)'
        for match in re.finditer(italic_pattern, self.content):
            text = match.group(1) or match.group(2)
            if text and len(text.strip()) > 2:
                self.emphasis['italic'].append({
                    'text': text.strip(),
                    'position': match.start(),
                    'section': self._find_section_at_position(match.start())
                })
    
    def _extract_cross_references(self):
        """Extract cross-references to other reports/sections."""
        # Patterns: "Report X", "Phase X", "See Report X", "as discussed in"
        ref_patterns = [
            r'(?:See |see |As discussed in |as discussed in |From )?Report\s+(\d+)',
            r'(?:See |see |As discussed in |as discussed in |From )?Phase\s+([IVX]+)',
            r'(?:as|As)\s+(?:noted|discussed|described|explained)\s+in\s+([^,.!?]+)',
        ]
        
        for pattern in ref_patterns:
            for match in re.finditer(pattern, self.content):
                ref = match.group(0).strip()
                self.cross_references.append({
                    'text': ref,
                    'position': match.start(),
                    'section': self._find_section_at_position(match.start())
                })
    
    def _extract_tags(self):
        """Extract all hashtags."""
        tag_pattern = r'#([\w-]+)'
        
        for match in re.finditer(tag_pattern, self.content):
            tag = match.group(1)
            self.tags[tag] += 1
    
    def _extract_empirical_findings(self):
        """Extract research findings and statistics."""
        # Patterns for empirical data
        empirical_patterns = [
            r'((?:research|study|studies|evidence|data|findings?)\s+(?:show|shows|demonstrate|demonstrates|reveal|reveals|suggest|suggests)\s+[^.!?]+[.!?])',
            r'(\([^\)]*(?:p\s*[<>=]\s*[\d.]+|r\s*=\s*[\d.]+|CFI\s*=\s*[\d.]+|RMSEA\s*=\s*[\d.]+)[^\)]*\))',
            r'([\d.]+%\s+of\s+[^.!?]+[.!?])',
        ]
        
        for pattern in empirical_patterns:
            for match in re.finditer(pattern, self.content, re.IGNORECASE):
                finding = match.group(1).strip()
                if len(finding) > 15:
                    self.empirical_findings.append({
                        'text': finding,
                        'position': match.start(),
                        'section': self._find_section_at_position(match.start())
                    })
    
    def _extract_practical_applications(self):
        """Extract practical how-to and application content."""
        # Patterns for practical guidance
        practical_patterns = [
            r'((?:To|to)\s+(?:practice|develop|cultivate|improve)\s+[^.!?]+[.!?])',
            r'((?:The|the)\s+practitioner\s+(?:should|must|can|might)\s+[^.!?]+[.!?])',
            r'((?:A|a)\s+practical\s+(?:approach|strategy|method)\s+[^.!?]+[.!?])',
            r'((?:This|this)\s+requires\s+[^.!?]+[.!?])',
        ]
        
        for pattern in practical_patterns:
            for match in re.finditer(pattern, self.content):
                practice = match.group(1).strip()
                if len(practice) > 20:
                    self.practical_applications.append({
                        'text': practice,
                        'position': match.start(),
                        'section': self._find_section_at_position(match.start())
                    })
    
    def _extract_frameworks(self):
        """Extract mentions of frameworks and models."""
        # Look for capitalized multi-word concepts that might be frameworks
        framework_pattern = r'(?:the\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\s+(?:framework|model|theory|approach|paradigm)'
        
        for match in re.finditer(framework_pattern, self.content):
            framework = match.group(1).strip()
            if framework not in [f['name'] for f in self.frameworks]:
                self.frameworks.append({
                    'name': framework,
                    'position': match.start(),
                    'section': self._find_section_at_position(match.start())
                })
    
    def _extract_principles(self):
        """Extract stated principles."""
        # Patterns for principles
        principle_patterns = [
            r'The principle (?:of |is that )([^.!?]+[.!?])',
            r'(?:A |The )(?:key |core |fundamental )?principle[:\s]+([^.!?]+[.!?])',
            r'Principle[:\s]+([^.!?]+[.!?])',
        ]
        
        for pattern in principle_patterns:
            for match in re.finditer(pattern, self.content, re.IGNORECASE):
                principle = match.group(1).strip()
                if len(principle) > 15:
                    self.principles.append({
                        'text': principle,
                        'position': match.start(),
                        'section': self._find_section_at_position(match.start())
                    })
    
    def _extract_warnings(self):
        """Extract cautions and warnings."""
        warning_patterns = [
            r'((?:Be|be)\s+careful\s+(?:not\s+to|to\s+avoid)\s+[^.!?]+[.!?])',
            r'((?:A|a)\s+(?:common|frequent|typical)\s+(?:mistake|error|pitfall)\s+[^.!?]+[.!?])',
            r'((?:It|it)\s+is\s+important\s+(?:not\s+to|to\s+avoid)\s+[^.!?]+[.!?])',
            r'((?:Do|do)\s+not\s+[^.!?]+[.!?])',
        ]
        
        for pattern in warning_patterns:
            for match in re.finditer(pattern, self.content):
                warning = match.group(1).strip()
                if len(warning) > 15:
                    self.warnings.append({
                        'text': warning,
                        'position': match.start(),
                        'section': self._find_section_at_position(match.start())
                    })
    
    def _find_section_at_position(self, position):
        """Find section heading for a character position."""
        line_num = self.content[:position].count('\n')
        return self._find_section_at_line(line_num)
    
    def _find_section_at_line(self, line_num):
        """Find section heading for a line number."""
        for heading in reversed(self.headings):
            if heading['line'] <= line_num:
                return heading['text']
        return "Document Start"
    
    def get_summary(self):
        """Get extraction summary."""
        return {
            'callouts': sum(len(v) for v in self.callouts.values()),
            'callouts_by_type': {k: len(v) for k, v in self.callouts.items()},
            'blockquotes': len(self.blockquotes),
            'headings': len(self.headings),
            'questions': len(self.questions),
            'examples': len(self.examples),
            'key_claims': len(self.key_claims),
            'definitions': len(self.definitions),
            'tables': len(self.tables),
            'lists': len(self.lists),
            'bold_emphasis': len(self.emphasis['bold']),
            'italic_emphasis': len(self.emphasis['italic']),
            'cross_references': len(self.cross_references),
            'tags': len(self.tags),
            'empirical_findings': len(self.empirical_findings),
            'practical_applications': len(self.practical_applications),
            'frameworks': len(self.frameworks),
            'principles': len(self.principles),
            'warnings': len(self.warnings),
        }


def generate_pkb_elements_report(extractor: PKBElementExtractor, output_path: str):
    """Generate comprehensive PKB elements report."""
    
    md = []
    
    # Header
    md.append("# 📦 PKB Elements Extraction Report")
    md.append("*Complete catalog of reusable content elements*\n")
    md.append("---\n")
    
    # TOC
    md.append("## 📑 Table of Contents\n")
    md.append("1. [Extraction Summary](#extraction-summary)")
    md.append("2. [Callouts by Type](#callouts-by-type)")
    md.append("3. [Document Structure](#document-structure)")
    md.append("4. [Questions](#questions)")
    md.append("5. [Examples](#examples)")
    md.append("6. [Key Claims](#key-claims)")
    md.append("7. [Definitions](#definitions)")
    md.append("8. [Tables](#tables)")
    md.append("9. [Empirical Findings](#empirical-findings)")
    md.append("10. [Practical Applications](#practical-applications)")
    md.append("11. [Frameworks & Models](#frameworks--models)")
    md.append("12. [Principles](#principles)")
    md.append("13. [Warnings & Cautions](#warnings--cautions)")
    md.append("14. [Cross-References](#cross-references)")
    md.append("15. [Tags](#tags)")
    md.append("16. [PKB Templates](#pkb-templates)\n")
    md.append("---\n")
    
    # 1. Summary
    summary = extractor.get_summary()
    md.append("## 📊 Extraction Summary\n")
    
    # Calculate total (excluding the callouts_by_type dict)
    total_elements = sum(v for k, v in summary.items() if k != 'callouts_by_type' and isinstance(v, int))
    md.append(f"**Total Elements Extracted**: {total_elements}\n")
    
    md.append("| Element Type | Count |")
    md.append("|--------------|-------|")
    for elem_type, count in sorted(((k, v) for k, v in summary.items() if isinstance(v, int)), 
                                    key=lambda x: x[1], reverse=True):
        if count > 0:
            display_name = elem_type.replace('_', ' ').title()
            md.append(f"| {display_name} | {count} |")
    
    md.append("\n---\n")
    
    # 2. Callouts by Type
    md.append("## 🎯 Callouts by Type\n")
    md.append("*Structured content blocks for direct PKB reuse*\n")
    
    callout_counts = Counter({k: len(v) for k, v in extractor.callouts.items()})
    
    for callout_type, count in callout_counts.most_common():
        md.append(f"\n### [{callout_type.upper()}] Callouts ({count})\n")
        
        for callout in extractor.callouts[callout_type][:10]:  # First 10 of each type
            md.append(f"**Section**: {callout['section']}")
            if callout['title']:
                md.append(f"**Title**: {callout['title']}")
            md.append(f"\n{callout['content'][:300]}{'...' if len(callout['content']) > 300 else ''}\n")
            md.append("---\n")
    
    md.append("\n---\n")
    
    # 3. Document Structure
    md.append("## 🗂️ Document Structure\n")
    md.append("*Complete heading hierarchy for navigation*\n")
    
    # Build hierarchy visualization
    for heading in extractor.headings:
        indent = "  " * (heading['level'] - 1)
        md.append(f"{indent}- {heading['text']}")
    
    md.append("\n---\n")
    
    # 4. Questions
    md.append("## ❓ Questions\n")
    md.append("*All questions for FAQ and reflection prompts*\n")
    
    # Group by section
    questions_by_section = defaultdict(list)
    for q in extractor.questions:
        questions_by_section[q['section']].append(q['text'])
    
    for section, questions in sorted(questions_by_section.items()):
        md.append(f"\n### {section}\n")
        for q in questions[:5]:  # Top 5 per section
            md.append(f"- {q}")
    
    md.append(f"\n**Total Questions**: {len(extractor.questions)}")
    md.append("\n---\n")
    
    # 5. Examples
    md.append("## 💡 Examples\n")
    md.append("*Concrete illustrations for concept notes*\n")
    
    for i, example in enumerate(extractor.examples[:30], 1):
        md.append(f"\n{i}. **{example['section']}**")
        md.append(f"   {example['text']}")
    
    md.append(f"\n**Total Examples**: {len(extractor.examples)}")
    md.append("\n---\n")
    
    # 6. Key Claims
    md.append("## 🎯 Key Claims\n")
    md.append("*Central arguments and assertions*\n")
    
    for i, claim in enumerate(extractor.key_claims[:25], 1):
        md.append(f"\n{i}. **{claim['section']}**")
        md.append(f"   {claim['text']}")
    
    md.append(f"\n**Total Key Claims**: {len(extractor.key_claims)}")
    md.append("\n---\n")
    
    # 7. Definitions
    md.append("## 📖 Definitions\n")
    md.append("*Explicit term definitions for glossary*\n")
    
    for defn in sorted(extractor.definitions, key=lambda x: x['term']):
        md.append(f"\n**{defn['term']}**")
        md.append(f"> {defn['definition']}")
        md.append(f"*From: {defn['section']}*\n")
    
    md.append(f"\n**Total Definitions**: {len(extractor.definitions)}")
    md.append("\n---\n")
    
    # 8. Tables
    md.append("## 📊 Tables\n")
    md.append("*Structured data for reference notes*\n")
    
    for i, table in enumerate(extractor.tables, 1):
        md.append(f"\n### Table {i}: {table['section']}\n")
        md.append(f"**Rows**: {table['rows']}\n")
        for line in table['lines'][:5]:  # First 5 rows
            md.append(line)
        if len(table['lines']) > 5:
            md.append("*[...more rows]*")
        md.append("")
    
    md.append(f"\n**Total Tables**: {len(extractor.tables)}")
    md.append("\n---\n")
    
    # 9. Empirical Findings
    md.append("## 🔬 Empirical Findings\n")
    md.append("*Research results and statistics*\n")
    
    for i, finding in enumerate(extractor.empirical_findings[:20], 1):
        md.append(f"\n{i}. {finding['text']}")
        md.append(f"   *{finding['section']}*")
    
    md.append(f"\n**Total Findings**: {len(extractor.empirical_findings)}")
    md.append("\n---\n")
    
    # 10. Practical Applications
    md.append("## 🛠️ Practical Applications\n")
    md.append("*How-to guidance and practice methods*\n")
    
    for i, practice in enumerate(extractor.practical_applications[:25], 1):
        md.append(f"\n{i}. {practice['text']}")
        md.append(f"   *{practice['section']}*")
    
    md.append(f"\n**Total Applications**: {len(extractor.practical_applications)}")
    md.append("\n---\n")
    
    # 11. Frameworks
    md.append("## 🧩 Frameworks & Models\n")
    md.append("*Theoretical frameworks for linking*\n")
    
    for framework in sorted(extractor.frameworks, key=lambda x: x['name']):
        md.append(f"- **[[{framework['name']}]]** *(from {framework['section']})*")
    
    md.append(f"\n**Total Frameworks**: {len(extractor.frameworks)}")
    md.append("\n---\n")
    
    # 12. Principles
    md.append("## ⚖️ Principles\n")
    md.append("*Core principles for principle notes*\n")
    
    for i, principle in enumerate(extractor.principles[:20], 1):
        md.append(f"\n{i}. {principle['text']}")
        md.append(f"   *{principle['section']}*")
    
    md.append(f"\n**Total Principles**: {len(extractor.principles)}")
    md.append("\n---\n")
    
    # 13. Warnings
    md.append("## ⚠️ Warnings & Cautions\n")
    md.append("*Common pitfalls and mistakes to avoid*\n")
    
    for i, warning in enumerate(extractor.warnings[:15], 1):
        md.append(f"\n{i}. {warning['text']}")
        md.append(f"   *{warning['section']}*")
    
    md.append(f"\n**Total Warnings**: {len(extractor.warnings)}")
    md.append("\n---\n")
    
    # 14. Cross-References
    md.append("## 🔗 Cross-References\n")
    md.append("*Internal references for link structure*\n")
    
    ref_counts = Counter([ref['text'] for ref in extractor.cross_references])
    
    for ref, count in ref_counts.most_common(30):
        md.append(f"- {ref} ({count}×)")
    
    md.append(f"\n**Total Cross-References**: {len(extractor.cross_references)}")
    md.append("\n---\n")
    
    # 15. Tags
    md.append("## 🏷️ Tags\n")
    md.append("*Hashtag taxonomy for PKB organization*\n")
    
    md.append("\n| Tag | Frequency |")
    md.append("|-----|-----------|")
    for tag, count in extractor.tags.most_common(50):
        md.append(f"| #{tag} | {count}× |")
    
    md.append("\n---\n")
    
    # 16. PKB Templates
    md.append("## 📝 PKB Templates\n")
    md.append("*Ready-to-use note templates based on extracted elements*\n")
    
    md.append("\n### Template: Question Note\n")
    md.append("```markdown")
    md.append("---")
    md.append("tags: #question #examined-life")
    md.append("type: reflective-question")
    md.append("related-concepts: []")
    md.append("---\n")
    md.append("# [Question Text]\n")
    md.append("## Context")
    md.append("[From which section/report]\n")
    md.append("## Reflection Space")
    md.append("[Personal response]\n")
    md.append("## Related Concepts")
    md.append("- [[Concept 1]]")
    md.append("- [[Concept 2]]")
    md.append("```\n")
    
    md.append("\n### Template: Example Note\n")
    md.append("```markdown")
    md.append("---")
    md.append("tags: #example #examined-life")
    md.append("illustrates: []")
    md.append("---\n")
    md.append("# Example: [Brief Title]\n")
    md.append("## The Example")
    md.append("[Example text]\n")
    md.append("## What It Illustrates")
    md.append("This example demonstrates [[Concept]]...\n")
    md.append("## Application")
    md.append("How to apply this in practice...")
    md.append("```\n")
    
    md.append("\n### Template: Principle Note\n")
    md.append("```markdown")
    md.append("---")
    md.append("tags: #principle #examined-life")
    md.append("applies-to: []")
    md.append("---\n")
    md.append("# Principle: [Name]\n")
    md.append("## Statement")
    md.append("> [Principle text]\n")
    md.append("## Rationale")
    md.append("Why this principle matters...\n")
    md.append("## Application Examples")
    md.append("1. Example 1")
    md.append("2. Example 2\n")
    md.append("## Related Principles")
    md.append("- [[Related Principle]]")
    md.append("```\n")
    
    md.append("---\n")
    
    # Footer
    md.append("## 💡 Using This Report\n")
    md.append("""
This extraction provides the raw materials for building your PKB:

1. **Callouts**: Copy directly into relevant concept notes
2. **Questions**: Create reflective prompt notes for family learning
3. **Examples**: Add to concept notes as concrete illustrations
4. **Definitions**: Build glossary entries
5. **Tables**: Extract as reference materials
6. **Frameworks**: Create framework overview notes
7. **Principles**: Develop principle notes with applications
8. **Structure**: Use heading hierarchy for PKB organization

**Next Steps**:
- Combine with wiki-links catalog for complete PKB scaffolding
- Use templates to systematically create notes
- Group related elements for coherent note clusters

---

*Auto-generated from source document. Regenerate after updates.*
""")
    
    # Write file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    
    print(f"✅ PKB elements report generated!")
    print(f"📄 Output: {output_path}")


def main():
    """Main execution."""
    input_file = "the-architecture-of-the-examined-life.md"
    output_file = "pkb-elements-extraction.md"
    
    print("🚀 Starting PKB Elements Extraction...")
    print(f"📖 Input: {input_file}\n")
    
    # Create extractor
    extractor = PKBElementExtractor(input_file)
    
    # Extract all elements
    extractor.extract_all()
    
    # Get summary
    summary = extractor.get_summary()
    
    # Generate report
    print("\n📝 Generating comprehensive report...")
    generate_pkb_elements_report(extractor, output_file)
    
    # Print summary
    print(f"\n📊 Extraction Summary:")
    print(f"   - {summary['callouts']} total callouts")
    for callout_type, count in sorted(summary['callouts_by_type'].items(), key=lambda x: x[1], reverse=True):
        print(f"     • {callout_type}: {count}")
    print(f"   - {summary['headings']} headings")
    print(f"   - {summary['questions']} questions")
    print(f"   - {summary['examples']} examples")
    print(f"   - {summary['key_claims']} key claims")
    print(f"   - {summary['definitions']} explicit definitions")
    print(f"   - {summary['tables']} tables")
    print(f"   - {summary['empirical_findings']} empirical findings")
    print(f"   - {summary['practical_applications']} practical applications")
    print(f"   - {summary['frameworks']} frameworks")
    print(f"   - {summary['principles']} principles")
    print(f"   - {summary['tags']} unique tags")
    
    total = sum(v for k, v in summary.items() if k != 'callouts_by_type' and isinstance(v, int))
    print(f"\n✨ Total elements extracted: {total}")
    print("✅ Done! Check the PKB elements report.")


if __name__ == "__main__":
    main()
