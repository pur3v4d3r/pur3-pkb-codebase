"""
Phase 0 Days 5-6: Topic Analysis & Three-Tier Deduplication Protocol
Research Mining Agent Beta + Deduplication Specialist - Version 2

Simplified, regex-based approach for maximum reliability.
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Set
from difflib import SequenceMatcher
import hashlib

# Force UTF-8 encoding for console output
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# =============================================================================
# CONFIGURATION
# =============================================================================

BASE_DIR = Path(r"D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\the-prompt-report-main\data")
TOPIC_MODEL_DIR = BASE_DIR / "topic-model-data" / "sample-outputs"
MASTER_PAPERS_PATH = BASE_DIR.parent.parent / "topic-gpt-data" / "master_papers.jsonl"
OUTPUT_DIR = Path(r"D:\10_pur3v4d3r's-vault\01-research-data-analysis")
EXEMPLAR_DIR = Path(r"D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar")

# Known techniques from previous Phase 0 work
KNOWN_TECHNIQUES = [
    "Chain-of-Thought", "Few-Shot Learning", "Zero-Shot Learning",
    "Prompt Engineering", "In-Context Learning", "Prompt Injection",
    "Jailbreak Prompts", "Constitutional AI", "Retrieval-Augmented Generation",
    "Self-Consistency", "Tree-of-Thoughts", "Graph-of-Thoughts",
    "ReAct Framework", "Program-Aided Language Models", "Decomposed Prompting",
    "Meta-Prompting", "Instruction Tuning", "Soft Prompting", "Discrete Prompting",
    "Modular Prompting", "Query Rewriting", "Generate-then-Read",
    "Reasoning Frameworks", "Multi-Modal Prompting", "Red Teaming",
    "Adversarial Prompting", "Persona Modulation", "Automatic Prompt Engineering",
    "Prompt Compression", "Iterative Refinement", "Self-Refinement", "Meta-Learning"
]

# =============================================================================
# PART 1: PARSE TOPIC MODELS WITH REGEX
# =============================================================================

def parse_topic_model_regex(filepath: Path, n_topics: int) -> List[Dict]:
    """Parse topic model HTML using regex patterns"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    topics = []

    # Pattern: <input type="checkbox" class="topic-checkbox">TOPIC_ID: keywords...</div>
    topic_pattern = r'<input[^>]*class="topic-checkbox">(\d+):\s*([^<]+)</div>'

    for match in re.finditer(topic_pattern, content):
        topic_id = int(match.group(1))
        keywords_text = match.group(2).strip()
        keywords = keywords_text.split()[:20]  # First 20 keywords

        # Count papers for this topic by finding papers in the following details section
        # Find the text between this topic and the next topic or end
        topic_start = match.end()
        next_topic = re.search(topic_pattern, content[topic_start:])
        topic_end = topic_start + next_topic.start() if next_topic else len(content)
        topic_section = content[topic_start:topic_end]

        # Count paper links
        paper_links = re.findall(r'<a href=([^>]+)>([^<]+)</a>', topic_section)
        paper_count = len(paper_links)

        topics.append({
            'id': topic_id,
            'label': f"{topic_id}: {keywords_text}",
            'keywords': keywords,
            'paper_count': paper_count,
            'n_topics_model': n_topics
        })

    return topics

# =============================================================================
# PART 2: TIER 1 - INTRA-SOURCE DEDUPLICATION
# =============================================================================

def load_master_papers() -> List[Dict]:
    """Load papers from master_papers.jsonl"""
    papers = []
    with open(MASTER_PAPERS_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                papers.append(json.loads(line))
    return papers

def compute_text_hash(text: str) -> str:
    """Compute MD5 hash of normalized text"""
    normalized = re.sub(r'\s+', ' ', text.lower().strip())
    return hashlib.md5(normalized.encode()).hexdigest()

def similarity_ratio(text1: str, text2: str) -> float:
    """Compute similarity ratio between two texts"""
    return SequenceMatcher(None, text1, text2).ratio()

def tier1_deduplication(papers: List[Dict]) -> Dict:
    """
    Tier 1: Intra-source deduplication
    Find duplicate papers within master_papers.jsonl
    """
    print("  Running Tier 1 deduplication...")
    results = {
        'total_papers': len(papers),
        'duplicate_ids': [],
        'near_duplicates': [],
        'hash_duplicates': []
    }

    # Check for exact ID duplicates
    id_counts = Counter(p['id'] for p in papers)
    results['duplicate_ids'] = [pid for pid, count in id_counts.items() if count > 1]

    # Check for hash duplicates (identical content)
    hash_to_papers = defaultdict(list)
    for paper in papers:
        text_hash = compute_text_hash(paper['text'])
        hash_to_papers[text_hash].append(paper['id'])

    results['hash_duplicates'] = [ids for ids in hash_to_papers.values() if len(ids) > 1]

    # Check for near-duplicates (>95% similarity) - sample only first 200 papers
    sample_size = min(200, len(papers))
    print(f"    Checking near-duplicates for {sample_size} sampled papers...")

    for i in range(sample_size):
        for j in range(i + 1, sample_size):
            if papers[i]['id'] != papers[j]['id']:
                sim = similarity_ratio(papers[i]['text'][:500], papers[j]['text'][:500])
                if sim > 0.95:
                    results['near_duplicates'].append({
                        'id1': papers[i]['id'],
                        'id2': papers[j]['id'],
                        'similarity': round(sim, 3)
                    })

    return results

# =============================================================================
# PART 3: TIER 2 - CROSS-SOURCE DEDUPLICATION
# =============================================================================

def extract_techniques_from_text(text: str) -> Set[str]:
    """Extract known techniques from text"""
    found = set()
    text_lower = text.lower()
    for technique in KNOWN_TECHNIQUES:
        variants = [
            technique.lower(),
            technique.lower().replace('-', ' '),
            technique.lower().replace(' ', '-')
        ]
        if any(variant in text_lower for variant in variants):
            found.add(technique)
    return found

def scan_exemplar_documents() -> Dict[str, Set[str]]:
    """Scan exemplar documents for techniques"""
    print("  Scanning exemplar documents...")
    exemplar_techniques = {}

    subdirs = [
        'advanced-prompt-engineering-techniques',
        'claude-reasoning-documentation-series',
        '2026-01-07-exemplar-document-series',
        'prompt-engineering-specialist-package'
    ]

    for subdir in subdirs:
        dir_path = EXEMPLAR_DIR / subdir
        if not dir_path.exists():
            continue

        for md_file in dir_path.glob('*.md'):
            try:
                content = md_file.read_text(encoding='utf-8')
                techniques = extract_techniques_from_text(content)
                if techniques:
                    exemplar_techniques[str(md_file.relative_to(EXEMPLAR_DIR))] = techniques
            except Exception as e:
                print(f"    Warning: Error reading {md_file.name}: {e}")

    return exemplar_techniques

def tier2_deduplication(papers: List[Dict]) -> Dict:
    """
    Tier 2: Cross-source deduplication
    Compare research papers with exemplar documents
    """
    print("  Running Tier 2 deduplication...")
    exemplar_techniques = scan_exemplar_documents()

    print("    Extracting techniques from research papers...")
    paper_techniques = {}
    for i, paper in enumerate(papers):
        techniques = extract_techniques_from_text(paper['text'])
        if techniques:
            paper_techniques[paper['id']] = techniques

        if (i + 1) % 200 == 0:
            print(f"      Processed {i + 1}/{len(papers)} papers...")

    # Analyze overlap
    technique_counts = Counter()
    for techniques in exemplar_techniques.values():
        technique_counts.update(techniques)

    paper_technique_counts = Counter()
    for techniques in paper_techniques.values():
        paper_technique_counts.update(techniques)

    # Identify novel techniques
    exemplar_set = set()
    for techniques in exemplar_techniques.values():
        exemplar_set.update(techniques)

    paper_set = set()
    for techniques in paper_techniques.values():
        paper_set.update(techniques)

    novel_in_papers = paper_set - exemplar_set
    missing_research_backing = exemplar_set - paper_set

    results = {
        'exemplar_files_scanned': len(exemplar_techniques),
        'papers_with_techniques': len(paper_techniques),
        'exemplar_technique_counts': dict(technique_counts.most_common()),
        'paper_technique_counts': dict(paper_technique_counts.most_common()),
        'novel_techniques_in_papers': list(novel_in_papers),
        'techniques_needing_research_backing': list(missing_research_backing),
        'overlap_techniques': list(exemplar_set & paper_set)
    }

    return results

# =============================================================================
# PART 4: TIER 3 - CONTENT-LEVEL SEMANTIC SIMILARITY
# =============================================================================

def extract_technique_descriptions(papers: List[Dict]) -> Dict[str, List[str]]:
    """Extract descriptions of each technique from papers"""
    print("  Extracting technique descriptions...")
    technique_descriptions = defaultdict(list)

    for paper in papers:
        text = paper['text']
        techniques = extract_techniques_from_text(text)

        for technique in techniques:
            sentences = re.split(r'[.!?]+', text)
            for sentence in sentences:
                if technique.lower() in sentence.lower():
                    clean = sentence.strip()
                    if len(clean) > 30 and len(clean) < 500:
                        technique_descriptions[technique].append(clean)

    return dict(technique_descriptions)

def compute_jaccard_similarity(set1: Set, set2: Set) -> float:
    """Compute Jaccard similarity between two sets"""
    if not set1 or not set2:
        return 0.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0

def tier3_deduplication(papers: List[Dict]) -> Dict:
    """
    Tier 3: Content-level semantic similarity
    Use simplified similarity metrics for technique descriptions
    """
    print("  Running Tier 3 deduplication...")
    technique_descriptions = extract_technique_descriptions(papers)

    techniques = list(technique_descriptions.keys())
    high_similarity_pairs = []

    print(f"    Computing similarity for {len(techniques)} techniques...")
    for i, tech1 in enumerate(techniques):
        for j in range(i + 1, len(techniques)):
            tech2 = techniques[j]

            # Simple word-based similarity
            words1 = set(re.findall(r'\w+', ' '.join(technique_descriptions[tech1][:5]).lower()))
            words2 = set(re.findall(r'\w+', ' '.join(technique_descriptions[tech2][:5]).lower()))

            jaccard_sim = compute_jaccard_similarity(words1, words2)

            if jaccard_sim > 0.5:
                high_similarity_pairs.append({
                    'technique1': tech1,
                    'technique2': tech2,
                    'similarity': round(jaccard_sim, 3)
                })

    results = {
        'techniques_analyzed': len(techniques),
        'high_similarity_pairs': high_similarity_pairs,
        'technique_description_samples': {
            tech: descs[:2]
            for tech, descs in list(technique_descriptions.items())[:10]
        }
    }

    return results

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Execute Phase 0 Days 5-6 processing"""

    print("="*80)
    print("PHASE 0 DAYS 5-6: TOPIC ANALYSIS & DEDUPLICATION PROTOCOL")
    print("="*80)

    # -------------------------------------------------------------------------
    # PART 1: PARSE TOPIC MODELS
    # -------------------------------------------------------------------------
    print("\n[PART 1] Parsing topic model HTML files...")

    topic_models = {}
    for n_topics in [10, 25, 50]:
        filepath = TOPIC_MODEL_DIR / f"topic_outputs-{n_topics}.html"
        if filepath.exists():
            print(f"  Processing {n_topics}-topic model...")
            topics = parse_topic_model_regex(filepath, n_topics)
            topic_models[n_topics] = topics
            print(f"    Extracted {len(topics)} topics")
        else:
            print(f"  WARNING: {filepath} not found")

    # Save topic taxonomy
    topic_taxonomy = {
        'topic_models': {
            f'{n}_topics': {
                'topics': topics
            }
            for n, topics in topic_models.items()
        },
        'metadata': {
            'total_papers': 1464,
            'techniques_identified': len(KNOWN_TECHNIQUES)
        }
    }

    taxonomy_path = OUTPUT_DIR / "topic_taxonomy.json"
    with open(taxonomy_path, 'w', encoding='utf-8') as f:
        json.dump(topic_taxonomy, f, indent=2, ensure_ascii=False)
    print(f"\n  [OK] Saved topic taxonomy to {taxonomy_path}")

    # -------------------------------------------------------------------------
    # PART 2: TIER 1 DEDUPLICATION
    # -------------------------------------------------------------------------
    print("\n[PART 2] Tier 1: Intra-source deduplication...")

    papers = load_master_papers()
    tier1_results = tier1_deduplication(papers)

    tier1_path = OUTPUT_DIR / "tier1_deduplication_log.json"
    with open(tier1_path, 'w', encoding='utf-8') as f:
        json.dump(tier1_results, f, indent=2)
    print(f"  [OK] Saved Tier 1 results to {tier1_path}")
    print(f"    Duplicate IDs: {len(tier1_results['duplicate_ids'])}")
    print(f"    Hash duplicates: {len(tier1_results['hash_duplicates'])}")
    print(f"    Near-duplicates: {len(tier1_results['near_duplicates'])}")

    # -------------------------------------------------------------------------
    # PART 3: TIER 2 DEDUPLICATION
    # -------------------------------------------------------------------------
    print("\n[PART 3] Tier 2: Cross-source deduplication...")

    tier2_results = tier2_deduplication(papers)

    tier2_path = OUTPUT_DIR / "tier2_cross_source_analysis.json"
    with open(tier2_path, 'w', encoding='utf-8') as f:
        json.dump(tier2_results, f, indent=2, ensure_ascii=False)
    print(f"  [OK] Saved Tier 2 results to {tier2_path}")
    print(f"    Exemplar files scanned: {tier2_results['exemplar_files_scanned']}")
    print(f"    Papers with techniques: {tier2_results['papers_with_techniques']}")
    print(f"    Novel techniques in papers: {len(tier2_results['novel_techniques_in_papers'])}")

    # -------------------------------------------------------------------------
    # PART 4: TIER 3 DEDUPLICATION
    # -------------------------------------------------------------------------
    print("\n[PART 4] Tier 3: Content-level semantic similarity...")

    tier3_results = tier3_deduplication(papers)

    tier3_path = OUTPUT_DIR / "tier3_semantic_similarity_matrix.json"
    with open(tier3_path, 'w', encoding='utf-8') as f:
        json.dump(tier3_results, f, indent=2, ensure_ascii=False)
    print(f"  [OK] Saved Tier 3 results to {tier3_path}")
    print(f"    Techniques analyzed: {tier3_results['techniques_analyzed']}")
    print(f"    High-similarity pairs: {len(tier3_results['high_similarity_pairs'])}")

    # -------------------------------------------------------------------------
    # PART 5: GENERATE REPORTS
    # -------------------------------------------------------------------------
    print("\n[PART 5] Generating final reports...")

    # Calculate redundancy rate
    total_duplicate_instances = (
        len(tier1_results['duplicate_ids']) +
        len(tier1_results['hash_duplicates']) +
        len(tier1_results['near_duplicates'])
    )
    redundancy_rate = (total_duplicate_instances / tier1_results['total_papers']) * 100

    summary = {
        'phase': 'Phase 0 Days 5-6',
        'status': 'COMPLETE',
        'timestamp': '2026-02-13',
        'topic_analysis': {
            'models_processed': list(topic_models.keys()),
            'total_topics_10': len(topic_models.get(10, [])),
            'total_topics_25': len(topic_models.get(25, [])),
            'total_topics_50': len(topic_models.get(50, []))
        },
        'deduplication': {
            'tier1_intra_source': {
                'duplicate_ids': len(tier1_results['duplicate_ids']),
                'hash_duplicates': len(tier1_results['hash_duplicates']),
                'near_duplicates': len(tier1_results['near_duplicates'])
            },
            'tier2_cross_source': {
                'exemplar_files': tier2_results['exemplar_files_scanned'],
                'novel_techniques': len(tier2_results['novel_techniques_in_papers'])
            },
            'tier3_semantic': {
                'techniques_analyzed': tier3_results['techniques_analyzed'],
                'high_similarity_pairs': len(tier3_results['high_similarity_pairs'])
            }
        },
        'overall_assessment': {
            'redundancy_rate_pct': round(redundancy_rate, 2),
            'target_rate_pct': 5.0,
            'meets_target': redundancy_rate < 5.0,
            'recommendation': 'PROCEED' if redundancy_rate < 5.0 else 'NEEDS_REVIEW'
        }
    }

    summary_path = OUTPUT_DIR / "phase0_days5-6_summary.json"
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    print(f"  [OK] Saved summary to {summary_path}")

    # -------------------------------------------------------------------------
    # COMPLETION
    # -------------------------------------------------------------------------
    print("\n" + "="*80)
    print("PHASE 0 DAYS 5-6 COMPLETE")
    print("="*80)
    print(f"Redundancy Rate: {redundancy_rate:.2f}% (Target: <5%)")
    print(f"Recommendation: {summary['overall_assessment']['recommendation']}")
    print("\nOutputs:")
    print(f"  - {taxonomy_path}")
    print(f"  - {tier1_path}")
    print(f"  - {tier2_path}")
    print(f"  - {tier3_path}")
    print(f"  - {summary_path}")

if __name__ == '__main__':
    main()
