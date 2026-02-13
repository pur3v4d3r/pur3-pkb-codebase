#!/usr/bin/env python3
"""
Citation Extraction Script for Tier 1 Documents
Phase 1 - Day 10: Research Citation Extraction
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set

# File paths
BASE_DIR = Path(r"D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\master-exemplar-project-2026")
DATA_DIR = BASE_DIR / "01-research-data-analysis"
DOCS_DIR = Path(r"D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\claude-reasoning-documentation-series")
OUTPUT_DIR = BASE_DIR / "02-planning-documents" / "tier1-enhancement-plans"

# Load research database
def load_research_data():
    """Load all research data files"""
    print("Loading research database...")

    with open(DATA_DIR / "paper_database.json", encoding='utf-8') as f:
        paper_db = json.load(f)

    with open(DATA_DIR / "technique_to_papers_mapping.json", encoding='utf-8') as f:
        technique_mapping = json.load(f)

    # Create paper lookup by ID
    papers_by_id = {paper['id']: paper for paper in paper_db['papers']}

    print(f"[OK] Loaded {len(papers_by_id)} papers")
    print(f"[OK] Loaded {len(technique_mapping['technique_map'])} techniques")

    return papers_by_id, technique_mapping['technique_map']

# Analyze document to extract mentioned techniques
def extract_techniques_from_document(doc_path: Path, known_techniques: Set[str]) -> Dict[str, int]:
    """Extract techniques mentioned in a document"""
    print(f"\nAnalyzing: {doc_path.name}")

    with open(doc_path, encoding='utf-8') as f:
        content = f.read()

    # Count technique mentions
    technique_counts = defaultdict(int)

    for technique in known_techniques:
        # Case-insensitive search for technique names
        pattern = re.compile(re.escape(technique), re.IGNORECASE)
        matches = pattern.findall(content)
        if matches:
            technique_counts[technique] = len(matches)

    # Sort by frequency
    sorted_techniques = sorted(technique_counts.items(), key=lambda x: x[1], reverse=True)

    print(f"  Found {len(sorted_techniques)} techniques mentioned:")
    for tech, count in sorted_techniques[:10]:
        print(f"    - {tech}: {count} mentions")

    return dict(sorted_techniques)

# Select papers for a document
def select_papers_for_document(
    doc_techniques: Dict[str, int],
    technique_map: Dict,
    papers_by_id: Dict,
    target_count: int = 18
) -> Dict:
    """Select most relevant papers for a document"""

    selected_papers = []
    papers_by_technique = defaultdict(list)

    # Get papers for each technique
    for technique, mention_count in doc_techniques.items():
        if technique not in technique_map:
            continue

        paper_ids = technique_map[technique]['paper_ids']

        # Calculate papers to select per technique (proportional to mentions)
        total_mentions = sum(doc_techniques.values())
        technique_allocation = max(1, int((mention_count / total_mentions) * target_count))

        # Select top papers (first N from mapping)
        for paper_id in paper_ids[:technique_allocation]:
            if paper_id in papers_by_id:
                paper = papers_by_id[paper_id]
                selected_papers.append({
                    'paper_id': paper_id,
                    'techniques': paper.get('techniques_mentioned', []),
                    'abstract_excerpt': paper['text'][:200] + '...',
                    'relevance': 'high' if technique in paper.get('primary_focus', '') else 'medium',
                    'primary_technique': technique,
                    'mention_count': mention_count
                })
                papers_by_technique[technique].append(paper_id)

    # Deduplicate (keep papers with most technique coverage)
    unique_papers = {}
    for paper in selected_papers:
        paper_id = paper['paper_id']
        if paper_id not in unique_papers:
            unique_papers[paper_id] = paper
        else:
            # Keep paper with more techniques
            if len(paper['techniques']) > len(unique_papers[paper_id]['techniques']):
                unique_papers[paper_id] = paper

    # Limit to target count (prioritize by relevance)
    final_papers = sorted(unique_papers.values(),
                         key=lambda x: (x['relevance'] == 'high', x['mention_count']),
                         reverse=True)[:target_count]

    return {
        'papers': final_papers,
        'papers_by_technique': dict(papers_by_technique),
        'total_papers': len(final_papers)
    }

# Generate citation mapping JSON
def generate_citation_mapping(doc_name: str, doc_path: Path,
                             selected_papers: Dict,
                             doc_techniques: Dict) -> Dict:
    """Generate citation mapping JSON structure"""

    citations_by_technique = defaultdict(list)

    for paper in selected_papers['papers']:
        technique = paper['primary_technique']
        citations_by_technique[technique].append({
            'paper_id': paper['paper_id'],
            'abstract_excerpt': paper['abstract_excerpt'],
            'relevance': paper['relevance'],
            'techniques': paper['techniques'],
            'citation_context': f"Use for {technique} explanation and examples",
            'metadata_available': {
                'title': None,
                'authors': None,
                'year': None,
                'doi': None,
                'arxiv': None
            }
        })

    # Generate bibliography entries
    bibliography = []
    for i, paper in enumerate(selected_papers['papers'], 1):
        bibliography.append(
            f"[{i}] Paper ID {paper['paper_id']} - {paper['abstract_excerpt']}"
        )

    return {
        'document': doc_name,
        'citations_extracted': len(selected_papers['papers']),
        'techniques_covered': list(doc_techniques.keys())[:15],
        'citations_by_technique': dict(citations_by_technique),
        'bibliography': bibliography
    }

# Generate bibliography draft markdown
def generate_bibliography_draft(doc_num: int, citation_mapping: Dict) -> str:
    """Generate bibliography draft markdown"""

    md = f"# DOC-{doc_num} Bibliography Draft\n\n"
    md += f"## References\n\n"

    for technique, papers in citation_mapping['citations_by_technique'].items():
        md += f"### {technique}\n\n"

        for i, paper in enumerate(papers, 1):
            md += f"[{i}] **Paper ID**: {paper['paper_id']}  \n"
            md += f"**Abstract Excerpt**: {paper['abstract_excerpt']}  \n"
            md += f"**Techniques**: {', '.join(paper['techniques'])}  \n"
            md += f"**Relevance**: {paper['relevance']}  \n"
            md += f"**Use in Document**: {paper['citation_context']}\n\n"

    md += f"## Statistics\n\n"
    md += f"- Total papers: {citation_mapping['citations_extracted']}\n"
    md += f"- Techniques covered: {len(citation_mapping['techniques_covered'])}\n"
    md += f"- Papers with full metadata: 0 (needs enrichment)\n"
    md += f"- Papers needing metadata enrichment: {citation_mapping['citations_extracted']}\n"

    return md

# Main execution
def main():
    """Main citation extraction workflow"""

    print("="*70)
    print("PHASE 1 - DAY 10: RESEARCH CITATION EXTRACTION")
    print("="*70)

    # Load data
    papers_by_id, technique_map = load_research_data()
    known_techniques = set(technique_map.keys())

    # Document configurations
    docs = [
        {
            'num': 1,
            'name': 'doc1-llm-reasoning-techniques-operational-manual.md',
            'target_citations': 18
        },
        {
            'num': 2,
            'name': 'doc2-extended-thinking-architecture-implementation-guide.md',
            'target_citations': 18
        },
        {
            'num': 3,
            'name': 'doc3-advanced-reasoning-architectures-theory-to-practice.md',
            'target_citations': 18
        },
        {
            'num': 4,
            'name': 'doc4-agentic-workflow-design-patterns.md',
            'target_citations': 18
        }
    ]

    all_citations = []

    # Process each document
    for doc_config in docs:
        print(f"\n{'='*70}")
        print(f"Processing DOC-{doc_config['num']}")
        print(f"{'='*70}")

        doc_path = DOCS_DIR / doc_config['name']

        # Extract techniques from document
        doc_techniques = extract_techniques_from_document(doc_path, known_techniques)

        # Select papers
        selected_papers = select_papers_for_document(
            doc_techniques,
            technique_map,
            papers_by_id,
            target_count=doc_config['target_citations']
        )

        # Generate citation mapping
        citation_mapping = generate_citation_mapping(
            doc_config['name'],
            doc_path,
            selected_papers,
            doc_techniques
        )

        # Save citation mapping JSON
        output_json = OUTPUT_DIR / f"doc{doc_config['num']}-citations-extracted.json"
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(citation_mapping, f, indent=2, ensure_ascii=False)
        print(f"\n[OK] Saved: {output_json.name}")

        # Generate and save bibliography draft
        bib_draft = generate_bibliography_draft(doc_config['num'], citation_mapping)
        output_md = OUTPUT_DIR / f"doc{doc_config['num']}-bibliography-draft.md"
        with open(output_md, 'w', encoding='utf-8') as f:
            f.write(bib_draft)
        print(f"[OK] Saved: {output_md.name}")

        all_citations.extend(selected_papers['papers'])

    # Generate master citation database
    master_citations = {
        'total_papers': len(set(p['paper_id'] for p in all_citations)),
        'papers_by_document': {
            f'doc{i+1}': docs[i]['target_citations']
            for i in range(len(docs))
        },
        'all_papers': all_citations
    }

    master_file = OUTPUT_DIR / "master-tier1-citations.json"
    with open(master_file, 'w', encoding='utf-8') as f:
        json.dump(master_citations, f, indent=2, ensure_ascii=False)
    print(f"\n[OK] Saved master citation database: {master_file.name}")

    # Generate summary report
    print(f"\n{'='*70}")
    print("EXTRACTION COMPLETE")
    print(f"{'='*70}")
    print(f"Total unique papers extracted: {master_citations['total_papers']}")
    print(f"Papers per document: ~{sum(docs[i]['target_citations'] for i in range(len(docs))) // len(docs)}")
    print(f"\nAll deliverables saved to:\n  {OUTPUT_DIR}")

if __name__ == '__main__':
    main()
