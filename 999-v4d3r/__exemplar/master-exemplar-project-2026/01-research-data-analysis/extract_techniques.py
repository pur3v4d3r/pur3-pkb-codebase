"""
Phase 0: Comprehensive Technique Extraction from Research Papers
Master Exemplar Document Series Project

Processes 1,464 papers from master_papers.jsonl to:
1. Extract all prompting techniques mentioned
2. Create paper database with technique mappings
3. Generate technique-to-papers cross-reference
4. Create per-technique bibliographies
5. Analyze co-occurrence patterns

Author: Research Mining Agent Alpha
Date: 2026-02-13
"""

import json
import re
from collections import defaultdict, Counter
from pathlib import Path
from typing import Dict, List, Set, Tuple
import statistics

# Define comprehensive technique taxonomy
TECHNIQUE_TAXONOMY = {
    # Basic Techniques
    "Zero-Shot": ["zero-shot", "zero shot", "0-shot", "zeroshot"],
    "Few-Shot": ["few-shot", "few shot", "k-shot", "fewshot", "n-shot"],
    "One-Shot": ["one-shot", "one shot", "1-shot", "oneshot"],
    "Instruction Following": ["instruction following", "instruction-following", "instructional prompting"],

    # Chain-of-Thought Variants
    "Chain-of-Thought": ["chain-of-thought", "chain of thought", "cot", "cot prompting", "chain-of-thought prompting", "chain-of-thought reasoning"],
    "Faithful Chain-of-Thought": ["faithful cot", "faithful chain-of-thought"],
    "Tabular Chain-of-Thought": ["tabular cot", "tabular chain-of-thought"],
    "Multi-Chain Reasoning": ["multi-chain", "multi-chain reasoning"],

    # Advanced Reasoning
    "Tree-of-Thoughts": ["tree-of-thoughts", "tree of thoughts", "tot", "thought tree"],
    "Graph-of-Thoughts": ["graph-of-thoughts", "graph of thoughts", "got", "thought graph"],
    "Chain-of-Verification": ["chain-of-verification", "cove", "chain of verification"],
    "Program-of-Thoughts": ["program-of-thoughts", "pot", "program of thoughts"],
    "Step-Back Prompting": ["step-back", "step back prompting"],
    "Least-to-Most Prompting": ["least-to-most", "least to most"],

    # Self-Optimization
    "Self-Consistency": ["self-consistency", "self consistency", "consistency decoding"],
    "Self-Refine": ["self-refine", "self refine", "self-refinement"],
    "Self-Ask": ["self-ask", "self ask"],
    "Reflexion": ["reflexion", "self-reflection", "reflective prompting"],
    "Meta-Prompting": ["meta-prompting", "meta prompting", "meta-prompt"],
    "Meta-Cognitive": ["meta-cognitive", "metacognitive", "meta-cognition"],

    # Chain-Based Specialized
    "Chain-of-Density": ["chain-of-density", "chain of density"],
    "Chain-of-Symbol": ["chain-of-symbol", "chain of symbol"],
    "Chain-of-Translation": ["chain-of-translation", "chain of translation"],
    "Chain-of-Draft": ["chain-of-draft", "chain of draft"],

    # Reasoning Approaches
    "ReAct": ["react", "reason+act", "reason and act", "reasoning and acting"],
    "Plan-and-Solve": ["plan-and-solve", "plan and solve", "planning-solving"],
    "Analogical Prompting": ["analogical prompting", "analogical reasoning", "analogy prompting"],
    "Decomposed Prompting": ["decomposed prompting", "decomposition", "task decomposition"],

    # Prompting Styles
    "Role Prompting": ["role prompting", "role-playing", "persona prompting"],
    "Emotion Prompting": ["emotion prompting", "emotional prompting", "emotion-based"],
    "In-Context Learning": ["in-context learning", "icl", "in context learning", "incontext learning"],

    # Knowledge Enhancement
    "Generated Knowledge": ["generated knowledge", "knowledge generation"],
    "RAG": ["rag", "retrieval-augmented generation", "retrieval augmented", "retrieval-augmented"],
    "Rewrite-Retrieve-Read": ["rewrite-retrieve-read", "rewrite retrieve read"],

    # Optimization
    "Prompt Engineering": ["prompt engineering", "prompt design", "prompt optimization"],
    "Prompt Tuning": ["prompt tuning", "soft prompting", "continuous prompting"],
    "Few-Shot Prompting": ["few-shot prompting", "few shot prompting"],
    "Automatic Prompt": ["automatic prompt", "automated prompting", "prompt generation"],

    # Model Training
    "Fine-tuning": ["fine-tuning", "fine tuning", "finetuning", "supervised fine-tuning"],
    "RLHF": ["rlhf", "reinforcement learning from human feedback"],

    # Adversarial
    "Jailbreaking": ["jailbreak", "jailbreaking", "adversarial prompts", "jailbreak prompt"],

    # Other Important
    "Boosting": ["boosting", "ensemble prompting"],
    "Code Prompting": ["code prompting", "code-based prompting", "programming prompts"],
    "Modular Prompting": ["modular prompting", "modular reasoning"],
}


def load_papers(jsonl_path: str) -> List[Dict]:
    """Load all papers from JSONL file."""
    papers = []
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                papers.append(json.loads(line))
    return papers


def extract_techniques(text: str) -> Set[str]:
    """
    Extract all techniques mentioned in text.
    Returns set of canonical technique names.
    """
    text_lower = text.lower()
    found_techniques = set()

    for canonical_name, aliases in TECHNIQUE_TAXONOMY.items():
        for alias in aliases:
            # Use word boundaries for better matching
            pattern = r'\b' + re.escape(alias) + r'\b'
            if re.search(pattern, text_lower):
                found_techniques.add(canonical_name)
                break  # Found this technique, no need to check other aliases

    return found_techniques


def identify_primary_focus(text: str, techniques: Set[str]) -> str:
    """
    Identify the primary technique focus based on frequency and prominence.
    """
    if not techniques:
        return "None"

    # Count mentions of each technique
    technique_counts = defaultdict(int)
    text_lower = text.lower()

    for technique in techniques:
        for alias in TECHNIQUE_TAXONOMY[technique]:
            pattern = r'\b' + re.escape(alias) + r'\b'
            technique_counts[technique] += len(re.findall(pattern, text_lower))

    # Return technique with highest count
    if technique_counts:
        return max(technique_counts.items(), key=lambda x: x[1])[0]

    return list(techniques)[0] if techniques else "None"


def process_papers(papers: List[Dict]) -> Tuple[List[Dict], Dict]:
    """
    Process all papers to extract techniques.

    Returns:
        - List of paper records with technique information
        - Dictionary mapping techniques to paper IDs
    """
    paper_records = []
    technique_to_papers = defaultdict(set)

    for paper in papers:
        paper_id = paper['id']
        text = paper['text']

        # Extract techniques
        techniques = extract_techniques(text)
        techniques_list = sorted(list(techniques))

        # Identify primary focus
        primary_focus = identify_primary_focus(text, techniques)

        # Create paper record
        record = {
            'id': paper_id,
            'text': text,
            'techniques_mentioned': techniques_list,
            'technique_count': len(techniques_list),
            'text_length': len(text),
            'primary_focus': primary_focus
        }

        paper_records.append(record)

        # Map techniques to papers
        for technique in techniques_list:
            technique_to_papers[technique].add(paper_id)

    return paper_records, technique_to_papers


def create_paper_database(paper_records: List[Dict], output_path: str):
    """Create comprehensive paper database JSON file."""

    # Calculate statistics
    papers_with_techniques = sum(1 for p in paper_records if p['technique_count'] > 0)
    technique_counts = [p['technique_count'] for p in paper_records if p['technique_count'] > 0]
    avg_techniques = statistics.mean(technique_counts) if technique_counts else 0.0

    # Technique distribution
    technique_distribution = Counter()
    for paper in paper_records:
        for technique in paper['techniques_mentioned']:
            technique_distribution[technique] += 1

    database = {
        'papers': paper_records,
        'summary': {
            'total_papers': len(paper_records),
            'papers_with_techniques': papers_with_techniques,
            'papers_without_techniques': len(paper_records) - papers_with_techniques,
            'average_techniques_per_paper': round(avg_techniques, 2),
            'median_techniques_per_paper': int(statistics.median(technique_counts)) if technique_counts else 0,
            'max_techniques_in_paper': max(technique_counts) if technique_counts else 0,
            'technique_distribution': dict(technique_distribution.most_common())
        }
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(database, f, indent=2, ensure_ascii=False)

    return database


def create_technique_mapping(technique_to_papers: Dict, paper_records: List[Dict], output_path: str):
    """Create technique-to-papers mapping JSON file."""

    # Build mapping with metadata
    technique_map = {}

    for technique, paper_ids in technique_to_papers.items():
        # Filter out None values and sort
        valid_ids = [pid for pid in paper_ids if pid is not None]
        technique_map[technique] = {
            'paper_count': len(valid_ids),
            'paper_ids': sorted(valid_ids),
            'canonical_name': technique,
            'aliases': TECHNIQUE_TAXONOMY[technique]
        }

    # Calculate statistics
    paper_counts = [info['paper_count'] for info in technique_map.values()]

    mapping = {
        'technique_map': technique_map,
        'statistics': {
            'total_techniques_identified': len(technique_map),
            'most_common_techniques': [
                {'technique': tech, 'count': info['paper_count']}
                for tech, info in sorted(technique_map.items(),
                                        key=lambda x: x[1]['paper_count'],
                                        reverse=True)[:20]
            ],
            'papers_per_technique_avg': round(statistics.mean(paper_counts), 2) if paper_counts else 0,
            'papers_per_technique_median': int(statistics.median(paper_counts)) if paper_counts else 0
        }
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)

    return mapping


def create_per_technique_bibliographies(technique_to_papers: Dict, paper_records: List[Dict], output_dir: str):
    """Create individual markdown files for each technique."""

    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)

    # Create paper lookup
    paper_lookup = {p['id']: p for p in paper_records}

    # Generate bibliography for techniques with ≥5 papers
    for technique, paper_ids in technique_to_papers.items():
        if len(paper_ids) < 5:
            continue

        filename = f"{technique.lower().replace(' ', '-').replace('-', '_')}_papers.md"
        filepath = output_path / filename

        # Collect papers with this technique
        papers = [paper_lookup[pid] for pid in paper_ids if pid in paper_lookup]

        # Sort by number of techniques (more comprehensive papers first)
        papers.sort(key=lambda x: x['technique_count'], reverse=True)

        # Analyze co-occurring techniques
        cooccurrence = Counter()
        for paper in papers:
            for tech in paper['techniques_mentioned']:
                if tech != technique:
                    cooccurrence[tech] += 1

        # Write markdown file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# Papers on {technique}\n\n")
            f.write(f"**Total Papers**: {len(papers)}\n")
            f.write(f"**Canonical Name**: {technique}\n")
            f.write(f"**Aliases**: {', '.join(TECHNIQUE_TAXONOMY[technique])}\n\n")

            f.write("## Papers (Sorted by comprehensiveness)\n\n")

            for i, paper in enumerate(papers, 1):
                f.write(f"### {i}. Paper\n\n")
                f.write(f"**Paper ID**: `{paper['id']}`\n\n")
                f.write(f"**Techniques Mentioned** ({paper['technique_count']}): {', '.join(paper['techniques_mentioned'])}\n\n")

                # Show first 300 chars of abstract
                excerpt = paper['text'][:300]
                if len(paper['text']) > 300:
                    excerpt += "..."
                f.write(f"**Abstract Excerpt**:\n> {excerpt}\n\n")

            f.write("---\n\n")
            f.write("## Statistics\n\n")
            f.write(f"- Average techniques per paper: {statistics.mean([p['technique_count'] for p in papers]):.2f}\n")
            f.write(f"- Median techniques per paper: {statistics.median([p['technique_count'] for p in papers]):.0f}\n\n")

            if cooccurrence:
                f.write("**Top Co-occurring Techniques**:\n")
                for tech, count in cooccurrence.most_common(10):
                    f.write(f"- {tech}: {count} papers ({count/len(papers)*100:.1f}%)\n")


def analyze_cooccurrence(paper_records: List[Dict], output_path: str):
    """Analyze technique co-occurrence patterns."""

    # Build co-occurrence matrix
    cooccurrence_matrix = defaultdict(lambda: defaultdict(int))

    for paper in paper_records:
        techniques = paper['techniques_mentioned']
        # Record all pairs
        for i, tech1 in enumerate(techniques):
            for tech2 in techniques[i+1:]:
                cooccurrence_matrix[tech1][tech2] += 1
                cooccurrence_matrix[tech2][tech1] += 1

    # Convert to regular dict for JSON serialization
    cooccurrence_dict = {
        tech1: dict(tech2_counts)
        for tech1, tech2_counts in cooccurrence_matrix.items()
    }

    # Find strongest co-occurrences
    strong_pairs = []
    processed_pairs = set()

    for tech1, tech2_counts in cooccurrence_matrix.items():
        for tech2, count in tech2_counts.items():
            pair_key = tuple(sorted([tech1, tech2]))
            if pair_key not in processed_pairs and count >= 5:
                strong_pairs.append({
                    'technique_1': tech1,
                    'technique_2': tech2,
                    'cooccurrence_count': count
                })
                processed_pairs.add(pair_key)

    strong_pairs.sort(key=lambda x: x['cooccurrence_count'], reverse=True)

    result = {
        'cooccurrence_matrix': cooccurrence_dict,
        'strong_cooccurrences': strong_pairs[:50],  # Top 50
        'summary': {
            'total_technique_pairs': len(processed_pairs),
            'strong_pairs_count': len(strong_pairs)
        }
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    return result


def generate_summary_report(paper_database: Dict, technique_mapping: Dict,
                            cooccurrence: Dict, output_path: str):
    """Generate comprehensive summary report."""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Paper Extraction Summary Report\n\n")
        f.write("**Project**: Master Exemplar Document Series\n")
        f.write("**Phase**: 0 - Paper Extraction & Technique Mapping\n")
        f.write("**Date**: 2026-02-13\n\n")

        f.write("---\n\n")
        f.write("## Executive Summary\n\n")

        summary = paper_database['summary']
        f.write(f"- **Total Papers Processed**: {summary['total_papers']:,}\n")
        f.write(f"- **Papers with Techniques**: {summary['papers_with_techniques']:,} ({summary['papers_with_techniques']/summary['total_papers']*100:.1f}%)\n")
        f.write(f"- **Papers without Techniques**: {summary['papers_without_techniques']:,} ({summary['papers_without_techniques']/summary['total_papers']*100:.1f}%)\n")
        f.write(f"- **Unique Techniques Identified**: {technique_mapping['statistics']['total_techniques_identified']}\n")
        f.write(f"- **Average Techniques per Paper**: {summary['average_techniques_per_paper']:.2f}\n")
        f.write(f"- **Median Techniques per Paper**: {summary['median_techniques_per_paper']}\n")
        f.write(f"- **Maximum Techniques in Single Paper**: {summary['max_techniques_in_paper']}\n\n")

        f.write("---\n\n")
        f.write("## Top 20 Most Common Techniques\n\n")

        for i, item in enumerate(technique_mapping['statistics']['most_common_techniques'][:20], 1):
            percentage = (item['count'] / summary['total_papers']) * 100
            f.write(f"{i}. **{item['technique']}**: {item['count']} papers ({percentage:.1f}%)\n")

        f.write("\n---\n\n")
        f.write("## Technique Coverage Analysis\n\n")

        # Categorize techniques by frequency
        tech_map = technique_mapping['technique_map']
        high_coverage = [t for t, info in tech_map.items() if info['paper_count'] >= 100]
        medium_coverage = [t for t, info in tech_map.items() if 20 <= info['paper_count'] < 100]
        low_coverage = [t for t, info in tech_map.items() if 5 <= info['paper_count'] < 20]
        rare_coverage = [t for t, info in tech_map.items() if info['paper_count'] < 5]

        f.write(f"- **High Coverage** (≥100 papers): {len(high_coverage)} techniques\n")
        f.write(f"- **Medium Coverage** (20-99 papers): {len(medium_coverage)} techniques\n")
        f.write(f"- **Low Coverage** (5-19 papers): {len(low_coverage)} techniques\n")
        f.write(f"- **Rare Coverage** (<5 papers): {len(rare_coverage)} techniques\n\n")

        f.write("---\n\n")
        f.write("## Top 10 Technique Co-occurrences\n\n")

        for i, pair in enumerate(cooccurrence['strong_cooccurrences'][:10], 1):
            f.write(f"{i}. **{pair['technique_1']}** + **{pair['technique_2']}**: {pair['cooccurrence_count']} papers\n")

        f.write("\n---\n\n")
        f.write("## Most Comprehensive Papers\n\n")
        f.write("Papers mentioning the most diverse set of techniques:\n\n")

        # Find papers with most techniques
        papers = paper_database['papers']
        top_papers = sorted(papers, key=lambda x: x['technique_count'], reverse=True)[:10]

        for i, paper in enumerate(top_papers, 1):
            f.write(f"### {i}. {paper['technique_count']} Techniques\n\n")
            f.write(f"**Paper ID**: `{paper['id']}`\n\n")
            f.write(f"**Techniques**: {', '.join(paper['techniques_mentioned'])}\n\n")
            excerpt = paper['text'][:200]
            if len(paper['text']) > 200:
                excerpt += "..."
            f.write(f"**Excerpt**: {excerpt}\n\n")

        f.write("---\n\n")
        f.write("## Output Files Generated\n\n")
        f.write("1. **paper_database.json** - Complete paper records with technique annotations\n")
        f.write("2. **technique_to_papers_mapping.json** - Cross-reference from techniques to papers\n")
        f.write("3. **technique_cooccurrence_matrix.json** - Co-occurrence analysis\n")
        f.write("4. **papers_by_technique/** - Individual markdown bibliographies per technique\n")
        f.write("5. **paper-extraction-summary-report.md** - This report\n\n")

        f.write("---\n\n")
        f.write("## Methodology\n\n")
        f.write("### Technique Detection\n\n")
        f.write("Techniques were identified using case-insensitive pattern matching against a comprehensive taxonomy:\n\n")

        # Group techniques by category
        categories = {
            "Basic Techniques": ["Zero-Shot", "Few-Shot", "One-Shot", "Instruction Following"],
            "Chain-of-Thought Variants": [k for k in TECHNIQUE_TAXONOMY.keys() if "Chain-of" in k or k == "Chain-of-Thought"],
            "Advanced Reasoning": ["Tree-of-Thoughts", "Graph-of-Thoughts", "Chain-of-Verification",
                                  "Program-of-Thoughts", "Step-Back Prompting", "Least-to-Most Prompting"],
            "Self-Optimization": ["Self-Consistency", "Self-Refine", "Self-Ask", "Reflexion",
                                 "Meta-Prompting", "Meta-Cognitive"],
        }

        for category, techniques in categories.items():
            f.write(f"**{category}**:\n")
            for tech in techniques:
                if tech in TECHNIQUE_TAXONOMY:
                    f.write(f"- {tech}\n")
            f.write("\n")

        f.write("### Quality Metrics\n\n")
        f.write(f"- **Coverage Rate**: {summary['papers_with_techniques']/summary['total_papers']*100:.1f}% of papers contained at least one identifiable technique\n")
        f.write(f"- **Average Technique Density**: {summary['average_techniques_per_paper']:.2f} techniques per paper\n")
        f.write(f"- **Technique Diversity**: {technique_mapping['statistics']['total_techniques_identified']} distinct techniques identified\n\n")

        f.write("---\n\n")
        f.write("## Next Steps (Phase 1)\n\n")
        f.write("With this comprehensive database established, proceed to:\n\n")
        f.write("1. **Technique Deep-Dive Analysis** - Extract key insights for each major technique\n")
        f.write("2. **Exemplar Selection** - Identify best papers for each technique category\n")
        f.write("3. **Master Document Generation** - Create definitive guides per technique\n")
        f.write("4. **Cross-Reference Building** - Link related techniques and approaches\n\n")

        f.write("---\n\n")
        f.write("*Report generated by Research Mining Agent Alpha*\n")


def main():
    """Main execution function."""

    # Paths
    input_file = r"D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\the-prompt-report-main\data\topic-gpt-data\master_papers.jsonl"
    output_dir = r"D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\master-exemplar-project-2026\01-research-data-analysis"

    print("="*80)
    print("PHASE 0: COMPREHENSIVE TECHNIQUE EXTRACTION")
    print("="*80)
    print()

    # Step 1: Load papers
    print("[1/7] Loading papers from master_papers.jsonl...")
    papers = load_papers(input_file)
    print(f"      [OK] Loaded {len(papers):,} papers")
    print()

    # Step 2: Process papers and extract techniques
    print("[2/7] Extracting techniques from all papers...")
    paper_records, technique_to_papers = process_papers(papers)
    papers_with_tech = sum(1 for p in paper_records if p['technique_count'] > 0)
    print(f"      [OK] Processed {len(paper_records):,} papers")
    print(f"      [OK] Found techniques in {papers_with_tech:,} papers ({papers_with_tech/len(paper_records)*100:.1f}%)")
    print(f"      [OK] Identified {len(technique_to_papers)} unique techniques")
    print()

    # Step 3: Create paper database
    print("[3/7] Creating paper database...")
    paper_db_path = Path(output_dir) / "paper_database.json"
    paper_database = create_paper_database(paper_records, str(paper_db_path))
    print(f"      [OK] Saved to: {paper_db_path}")
    print()

    # Step 4: Create technique mapping
    print("[4/7] Creating technique-to-papers mapping...")
    mapping_path = Path(output_dir) / "technique_to_papers_mapping.json"
    technique_mapping = create_technique_mapping(technique_to_papers, paper_records, str(mapping_path))
    print(f"      [OK] Saved to: {mapping_path}")
    print()

    # Step 5: Generate per-technique bibliographies
    print("[5/7] Generating per-technique bibliographies...")
    biblio_dir = Path(output_dir) / "papers_by_technique"
    create_per_technique_bibliographies(technique_to_papers, paper_records, str(biblio_dir))
    biblio_count = len([t for t, pids in technique_to_papers.items() if len(pids) >= 5])
    print(f"      [OK] Created {biblio_count} bibliography files")
    print(f"      [OK] Saved to: {biblio_dir}")
    print()

    # Step 6: Analyze co-occurrence
    print("[6/7] Analyzing technique co-occurrence patterns...")
    cooccur_path = Path(output_dir) / "technique_cooccurrence_matrix.json"
    cooccurrence = analyze_cooccurrence(paper_records, str(cooccur_path))
    print(f"      [OK] Analyzed {cooccurrence['summary']['total_technique_pairs']:,} technique pairs")
    print(f"      [OK] Found {cooccurrence['summary']['strong_pairs_count']} strong co-occurrences")
    print(f"      [OK] Saved to: {cooccur_path}")
    print()

    # Step 7: Generate summary report
    print("[7/7] Generating summary report...")
    report_path = Path(output_dir) / "paper-extraction-summary-report.md"
    generate_summary_report(paper_database, technique_mapping, cooccurrence, str(report_path))
    print(f"      [OK] Saved to: {report_path}")
    print()

    print("="*80)
    print("PHASE 0 COMPLETE")
    print("="*80)
    print()
    print("Summary:")
    print(f"  - {len(paper_records):,} papers processed")
    print(f"  - {len(technique_to_papers)} techniques identified")
    print(f"  - {papers_with_tech:,} papers with techniques ({papers_with_tech/len(paper_records)*100:.1f}%)")
    print(f"  - {biblio_count} technique bibliographies generated")
    print()
    print("All output files saved to:")
    print(f"  {output_dir}")
    print()
    print("Next: Review paper-extraction-summary-report.md for detailed analysis")


if __name__ == "__main__":
    main()
