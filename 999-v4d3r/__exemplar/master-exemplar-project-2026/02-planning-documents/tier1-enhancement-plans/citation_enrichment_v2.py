import pandas as pd
import json
from pathlib import Path
from difflib import SequenceMatcher

# Paths
base_dir = Path(r"D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\master-exemplar-project-2026\02-planning-documents\tier1-enhancement-plans")
csv_path = Path(r"D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\the-prompt-report-main\data\arxiv_papers_with_abstract.csv")

# Simple similarity function
def similarity_ratio(a, b):
    """Calculate similarity between two strings (0-100)"""
    return SequenceMatcher(None, a, b).ratio() * 100

# Load arXiv metadata
print("Loading arXiv metadata CSV...")
arxiv_df = pd.read_csv(csv_path)
print(f"Total papers in CSV: {len(arxiv_df)}")
print(f"Columns: {list(arxiv_df.columns)}")

# Create index for faster lookups - use first 100 chars of abstract
print("\nIndexing abstracts for faster matching...")
arxiv_df['abstract_key'] = arxiv_df['abstract'].fillna('').str.lower().str[:100]

# Load master citations
with open(base_dir / 'master-tier1-citations.json', 'r', encoding='utf-8') as f:
    master_citations = json.load(f)

all_papers = master_citations['all_papers']
unique_papers = {}

# Deduplicate and organize papers
for paper in all_papers:
    paper_id = paper['paper_id']
    if paper_id not in unique_papers:
        unique_papers[paper_id] = paper
    else:
        # Merge mention counts
        unique_papers[paper_id]['mention_count'] = unique_papers[paper_id].get('mention_count', 0) + paper.get('mention_count', 0)

print(f"\nUnique papers to enrich: {len(unique_papers)}")

# Helper functions
def extract_arxiv_id(url):
    if pd.isna(url):
        return None
    if 'arxiv.org/abs/' in str(url):
        return str(url).split('/abs/')[-1].strip()
    return None

def extract_year(date_str):
    if pd.isna(date_str):
        return None
    try:
        return str(date_str)[:4]
    except:
        return None

def format_authors(author_str):
    if pd.isna(author_str):
        return "Unknown Author", "Unknown Author"

    author_str = str(author_str).strip()

    # For short citations
    if ',' in author_str:
        # Format: "Last, First" or "Last, First and ..."
        first_part = author_str.split(',')[0]
        if ' and ' in author_str or len(author_str) > 40:
            author_short = f"{first_part} et al."
        else:
            author_short = author_str
    else:
        # Just use first name/initial
        parts = author_str.split()
        if len(parts) > 0:
            if len(author_str) > 40:
                author_short = f"{parts[0]} et al."
            else:
                author_short = author_str
        else:
            author_short = author_str

    return author_short, author_str

# Match papers
enriched_papers = []
matched_count = 0
unmatched_papers = []

print("\nMatching papers...")
for i, (paper_id, paper_data) in enumerate(unique_papers.items(), 1):
    abstract_excerpt = paper_data.get('abstract_excerpt', '')

    # Prepare search text (first 100 chars, lowercase)
    search_text = abstract_excerpt[:100].lower().strip() if abstract_excerpt else ""

    print(f"[{i}/{len(unique_papers)}] Processing {paper_id[:8]}...")

    matched = False
    best_match_score = 0
    best_match_idx = None

    if search_text:
        # First pass: exact substring match (fast)
        exact_matches = arxiv_df[arxiv_df['abstract_key'].str.contains(search_text[:50], case=False, na=False, regex=False)]

        if len(exact_matches) > 0:
            # Found potential matches, do detailed comparison
            for idx in exact_matches.index:
                arxiv_abstract = str(arxiv_df.at[idx, 'abstract']).lower()
                score = similarity_ratio(search_text, arxiv_abstract[:150])

                if score > best_match_score:
                    best_match_score = score
                    best_match_idx = idx

    if best_match_score >= 70:  # Threshold for match confidence
        # Extract metadata
        matched_row = arxiv_df.iloc[best_match_idx]

        author_short, author_full = format_authors(matched_row.get('firstAuthor'))
        arxiv_id = extract_arxiv_id(matched_row.get('url'))
        year = extract_year(matched_row.get('dateSubmitted'))
        title = str(matched_row.get('title', 'Unknown Title')).strip()
        keywords = str(matched_row.get('keywords', '')).strip()

        # Format IEEE citation
        if arxiv_id and year:
            ieee_citation = f"{author_short}, \"{title},\" arXiv preprint arXiv:{arxiv_id}, {year}."
        else:
            ieee_citation = f"{author_short}, \"{title}.\""

        enriched_paper = {
            "paper_id": paper_id,
            "abstract_excerpt": abstract_excerpt,
            "metadata_enriched": True,
            "match_confidence": round(best_match_score, 1),
            "metadata": {
                "title": title,
                "authors": author_short,
                "author_full": author_full,
                "year": int(year) if year and year.isdigit() else None,
                "venue": "arXiv",
                "arxiv_id": arxiv_id,
                "arxiv_url": f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None,
                "doi": None,
                "keywords": keywords.split(', ') if keywords else []
            },
            "citation_ieee": ieee_citation,
            "relevance": paper_data.get('relevance', 'medium'),
            "techniques": paper_data.get('techniques', []),
            "primary_technique": paper_data.get('primary_technique', ''),
            "mention_count": paper_data.get('mention_count', 0)
        }

        enriched_papers.append(enriched_paper)
        matched_count += 1
        print(f"  [OK] Matched: {title[:60]}... (Score: {best_match_score:.1f})")
    else:
        # No match found
        unmatched_paper = {
            "paper_id": paper_id,
            "abstract_excerpt": abstract_excerpt,
            "metadata_enriched": False,
            "match_confidence": round(best_match_score, 1),
            "metadata": None,
            "citation_ieee": f"[Paper ID: {paper_id[:12]}] Abstract: \"{abstract_excerpt[:100]}...\" [Metadata pending manual review]",
            "relevance": paper_data.get('relevance', 'medium'),
            "techniques": paper_data.get('techniques', []),
            "primary_technique": paper_data.get('primary_technique', ''),
            "mention_count": paper_data.get('mention_count', 0)
        }

        enriched_papers.append(unmatched_paper)
        unmatched_papers.append(unmatched_paper)
        print(f"  [FAIL] No match (Best score: {best_match_score:.1f})")

print(f"\n{'='*60}")
print(f"ENRICHMENT SUMMARY")
print(f"{'='*60}")
print(f"Total unique papers: {len(unique_papers)}")
print(f"Successfully matched: {matched_count} ({matched_count/len(unique_papers)*100:.1f}%)")
print(f"Unmatched papers: {len(unmatched_papers)} ({len(unmatched_papers)/len(unique_papers)*100:.1f}%)")

# Save enriched master citations
enriched_master = {
    "total_papers": len(enriched_papers),
    "matched_papers": matched_count,
    "unmatched_papers": len(unmatched_papers),
    "match_rate_percent": round(matched_count/len(unique_papers)*100, 1),
    "papers": enriched_papers
}

output_file = base_dir / 'master-tier1-citations-enriched.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(enriched_master, f, indent=2, ensure_ascii=False)

print(f"\n[OK] Saved: master-tier1-citations-enriched.json")

# Load and enrich individual document files
print(f"\n{'='*60}")
print(f"DISTRIBUTING TO DOCUMENT FILES")
print(f"{'='*60}")

citation_files = [
    'doc1-citations-extracted.json',
    'doc2-citations-extracted.json',
    'doc3-citations-extracted.json',
    'doc4-citations-extracted.json'
]

for doc_file in citation_files:
    with open(base_dir / doc_file, 'r', encoding='utf-8') as f:
        doc_citations = json.load(f)

    # Enrich papers by technique
    for technique, papers in doc_citations['citations_by_technique'].items():
        enriched_technique_papers = []

        for paper in papers:
            paper_id = paper['paper_id']

            # Find enriched version
            enriched_version = next((p for p in enriched_papers if p['paper_id'] == paper_id), None)

            if enriched_version:
                # Merge citation context from original
                enriched_version['citation_context'] = paper.get('citation_context', '')
                enriched_technique_papers.append(enriched_version)
            else:
                enriched_technique_papers.append(paper)

        doc_citations['citations_by_technique'][technique] = enriched_technique_papers

    # Update bibliography with enriched citations
    new_bibliography = []
    for i, paper in enumerate(enriched_papers, 1):
        # Check if this paper is used in this document
        used_in_doc = any(
            paper['paper_id'] in [p['paper_id'] for p in tech_papers]
            for tech_papers in doc_citations['citations_by_technique'].values()
        )

        if used_in_doc:
            new_bibliography.append(f"[{i}] {paper['citation_ieee']}")

    doc_citations['bibliography'] = new_bibliography

    # Save enriched doc file
    output_name = doc_file.replace('-extracted.json', '-enriched.json')
    with open(base_dir / output_name, 'w', encoding='utf-8') as f:
        json.dump(doc_citations, f, indent=2, ensure_ascii=False)

    print(f"[OK] Saved: {output_name}")

print(f"\n{'='*60}")
print(f"ENRICHMENT COMPLETE")
print(f"{'='*60}")
print(f"Files created:")
print(f"  - master-tier1-citations-enriched.json")
print(f"  - doc1-citations-enriched.json")
print(f"  - doc2-citations-enriched.json")
print(f"  - doc3-citations-enriched.json")
print(f"  - doc4-citations-enriched.json")

# Print unmatched papers for manual review
if unmatched_papers:
    print(f"\n{'='*60}")
    print(f"UNMATCHED PAPERS REQUIRING MANUAL REVIEW ({len(unmatched_papers)})")
    print(f"{'='*60}")
    for i, paper in enumerate(unmatched_papers, 1):
        print(f"\n{i}. Paper ID: {paper['paper_id']}")
        print(f"   Primary Technique: {paper['primary_technique']}")
        print(f"   Abstract: {paper['abstract_excerpt'][:150]}...")
        print(f"   Best Match Score: {paper['match_confidence']:.1f}%")
