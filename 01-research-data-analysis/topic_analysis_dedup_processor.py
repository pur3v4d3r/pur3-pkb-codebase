"""
Phase 0 Days 5-6: Topic Analysis & Three-Tier Deduplication Protocol
Research Mining Agent Beta + Deduplication Specialist

Processes:
1. Topic model HTML parsing (10/25/50 topics)
2. Topic taxonomy generation
3. Three-tier deduplication (intra-source, cross-source, semantic)
4. Canonical technique definitions
"""

import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Set
from html.parser import HTMLParser
from difflib import SequenceMatcher
import hashlib

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
# PART 1: HTML TOPIC MODEL PARSER
# =============================================================================

class TopicModelParser(HTMLParser):
    """Parse topic model HTML files to extract topics and papers"""

    def __init__(self):
        super().__init__()
        self.topics = []
        self.current_topic = None
        self.current_element = None
        self.in_abstract = False
        self.in_summary = False
        self.current_doc = None

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            classes = dict(attrs).get('class', '')
            if 'topic-container' in classes:
                self.current_topic = {
                    'id': None,
                    'label': '',
                    'keywords': [],
                    'papers': []
                }
            elif 'topic' in classes:
                self.current_element = 'topic_label'

        elif tag == 'input' and self.current_topic is not None:
            self.current_element = 'checkbox'

        elif tag == 'a' and self.current_topic is not None:
            href = dict(attrs).get('href', '')
            if href:
                self.current_doc = {
                    'url': href,
                    'title': '',
                    'abstract': ''
                }
                self.current_element = 'paper_title'

        elif tag == 'summary' and self.current_doc is not None:
            self.in_summary = True

        elif tag == 'p' and self.in_summary:
            self.in_abstract = True
            self.current_element = 'abstract'

    def handle_endtag(self, tag):
        if tag == 'div' and self.current_topic is not None:
            if self.current_topic.get('label'):
                # Parse topic ID and keywords from label
                label_text = self.current_topic['label']
                match = re.match(r'(\d+):\s*(.+)', label_text)
                if match:
                    self.current_topic['id'] = int(match.group(1))
                    keywords = match.group(2).split()
                    self.current_topic['keywords'] = keywords[:20]  # Limit keywords

                self.topics.append(self.current_topic)
                self.current_topic = None

        elif tag == 'a' and self.current_doc is not None:
            if self.current_topic and self.current_doc.get('title'):
                self.current_topic['papers'].append(self.current_doc)
            self.current_doc = None
            self.current_element = None

        elif tag == 'summary':
            self.in_summary = False

        elif tag == 'p' and self.in_abstract:
            self.in_abstract = False
            self.current_element = None

    def handle_data(self, data):
        data = data.strip()
        if not data:
            return

        if self.current_element == 'topic_label' and self.current_topic is not None:
            self.current_topic['label'] += data

        elif self.current_element == 'paper_title' and self.current_doc is not None:
            self.current_doc['title'] += data

        elif self.current_element == 'abstract' and self.current_doc is not None:
            self.current_doc['abstract'] += data

def parse_topic_model_file(filepath: Path, n_topics: int) -> List[Dict]:
    """Parse a single topic model HTML file"""
    parser = TopicModelParser()
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        parser.feed(content)

    # Add metadata
    for topic in parser.topics:
        topic['n_topics_model'] = n_topics
        topic['paper_count'] = len(topic['papers'])

    return parser.topics

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
    results = {
        'total_papers': len(papers),
        'duplicate_ids': [],
        'near_duplicates': [],
        'hash_duplicates': []
    }

    # Check for exact ID duplicates
    id_counts = Counter(p['id'] for p in papers)
    results['duplicate_ids'] = [id for id, count in id_counts.items() if count > 1]

    # Check for hash duplicates (identical content)
    hash_to_papers = defaultdict(list)
    for paper in papers:
        text_hash = compute_text_hash(paper['text'])
        hash_to_papers[text_hash].append(paper['id'])

    results['hash_duplicates'] = [ids for ids in hash_to_papers.values() if len(ids) > 1]

    # Check for near-duplicates (>95% similarity)
    print(f"Checking near-duplicates for {len(papers)} papers...")
    for i in range(len(papers)):
        for j in range(i + 1, len(papers)):
            if papers[i]['id'] != papers[j]['id']:
                sim = similarity_ratio(papers[i]['text'], papers[j]['text'])
                if sim > 0.95:
                    results['near_duplicates'].append({
                        'id1': papers[i]['id'],
                        'id2': papers[j]['id'],
                        'similarity': sim
                    })

        if (i + 1) % 100 == 0:
            print(f"  Processed {i + 1}/{len(papers)} papers...")

    return results

# =============================================================================
# PART 3: TIER 2 - CROSS-SOURCE DEDUPLICATION
# =============================================================================

def extract_techniques_from_text(text: str) -> Set[str]:
    """Extract known techniques from text"""
    found = set()
    text_lower = text.lower()
    for technique in KNOWN_TECHNIQUES:
        # Check various forms
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
    exemplar_techniques = {}

    # Directories to scan
    exemplar_subdirs = [
        'advanced-prompt-engineering-techniques',
        'claude-reasoning-documentation-series',
        '2026-01-07-exemplar-document-series',
        'prompt-engineering-specialist-package'
    ]

    for subdir in exemplar_subdirs:
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
                print(f"Error reading {md_file}: {e}")

    return exemplar_techniques

def tier2_deduplication(papers: List[Dict]) -> Dict:
    """
    Tier 2: Cross-source deduplication
    Compare research papers with exemplar documents
    """
    print("Scanning exemplar documents...")
    exemplar_techniques = scan_exemplar_documents()

    print("Extracting techniques from research papers...")
    paper_techniques = {}
    for paper in papers:
        techniques = extract_techniques_from_text(paper['text'])
        if techniques:
            paper_techniques[paper['id']] = techniques

    # Analyze overlap
    technique_counts = Counter()
    for techniques in exemplar_techniques.values():
        technique_counts.update(techniques)

    paper_technique_counts = Counter()
    for techniques in paper_techniques.values():
        paper_technique_counts.update(techniques)

    # Identify novel techniques in papers (not in exemplars)
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
    technique_descriptions = defaultdict(list)

    for paper in papers:
        text = paper['text']
        techniques = extract_techniques_from_text(text)

        for technique in techniques:
            # Find sentences containing the technique
            sentences = re.split(r'[.!?]+', text)
            for sentence in sentences:
                if technique.lower() in sentence.lower():
                    technique_descriptions[technique].append(sentence.strip())

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
    print("Extracting technique descriptions...")
    technique_descriptions = extract_technique_descriptions(papers)

    # Compute pairwise similarity matrix
    techniques = list(technique_descriptions.keys())
    similarity_matrix = []
    high_similarity_pairs = []

    print(f"Computing similarity for {len(techniques)} techniques...")
    for i, tech1 in enumerate(techniques):
        for j in range(i + 1, len(techniques)):
            tech2 = techniques[j]

            # Simple word-based similarity
            words1 = set(re.findall(r'\w+', ' '.join(technique_descriptions[tech1]).lower()))
            words2 = set(re.findall(r'\w+', ' '.join(technique_descriptions[tech2]).lower()))

            jaccard_sim = compute_jaccard_similarity(words1, words2)

            if jaccard_sim > 0.5:  # High similarity threshold
                high_similarity_pairs.append({
                    'technique1': tech1,
                    'technique2': tech2,
                    'similarity': round(jaccard_sim, 3)
                })

    results = {
        'techniques_analyzed': len(techniques),
        'high_similarity_pairs': high_similarity_pairs,
        'technique_description_samples': {
            tech: descs[:2]  # First 2 descriptions per technique
            for tech, descs in technique_descriptions.items()
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
            topics = parse_topic_model_file(filepath, n_topics)
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
    print(f"\n  ✓ Saved topic taxonomy to {taxonomy_path}")

    # -------------------------------------------------------------------------
    # PART 2: TIER 1 DEDUPLICATION
    # -------------------------------------------------------------------------
    print("\n[PART 2] Tier 1: Intra-source deduplication...")

    papers = load_master_papers()
    tier1_results = tier1_deduplication(papers)

    tier1_path = OUTPUT_DIR / "tier1_deduplication_log.json"
    with open(tier1_path, 'w', encoding='utf-8') as f:
        json.dump(tier1_results, f, indent=2)
    print(f"  ✓ Saved Tier 1 results to {tier1_path}")
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
    print(f"  ✓ Saved Tier 2 results to {tier2_path}")
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
    print(f"  ✓ Saved Tier 3 results to {tier3_path}")
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
    print(f"  ✓ Saved summary to {summary_path}")

    # -------------------------------------------------------------------------
    # COMPLETION
    # -------------------------------------------------------------------------
    print("\n" + "="*80)
    print("PHASE 0 DAYS 5-6 COMPLETE")
    print("="*80)
    print(f"Redundancy Rate: {redundancy_rate:.2f}% (Target: <5%)")
    print(f"Recommendation: {summary['overall_assessment']['recommendation']}")
    print("\nNext: Generate markdown reports")

if __name__ == '__main__':
    main()
