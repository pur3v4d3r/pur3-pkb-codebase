import pandas as pd
import json
from pathlib import Path
from fuzzywuzzy import fuzz
from collections import defaultdict

# Paths
base_dir = Path(r"D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\master-exemplar-project-2026\02-planning-documents\tier1-enhancement-plans")
csv_path = Path(r"D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\the-prompt-report-main\data\arxiv_papers_with_abstract.csv")

# Load arXiv metadata
print("Loading arXiv metadata CSV...")
arxiv_df = pd.read_csv(csv_path)
print(f"Total papers in CSV: {len(arxiv_df)}")
print(f"Columns: {list(arxiv_df.columns)}")

# Load Day 10 citation files
citation_files = [
    'doc1-citations-extracted.json',
    'doc2-citations-extracted.json',
    'doc3-citations-extracted.json',
    'doc4-citations-extracted.json'
]

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

# Function to extract arXiv ID from URL
def extract_arxiv_id(url):
    if pd.isna(url):
        return None
    # URLs like: https://arxiv.org/abs/2201.11903
    if 'arxiv.org/abs/' in url:
        return url.split('/abs/')[-1].strip()
    return None

# Function to extract year from date
def extract_year(date_str):
    if pd.isna(date_str):
        return None
    try:
        return date_str[:4]  # YYYY-MM-DD -> YYYY
    except:
        return None

# Function to format authors
def format_authors(author_str):
    if pd.isna(author_str):
        return "Unknown Author", "Unknown Author"

    # Clean the author string
    author_str = str(author_str).strip()

    # First author only
    first_author = author_str

    # For et al. format
    if len(author_str) > 30:
        # Get last name only for first author
        parts = author_str.split(',')[0] if ',' in author_str else author_str.split()[0]
        author_short = f"{parts} et al."
    else:
        author_short = author_str

    return author_short, author_str

# Match papers using abstract fuzzy matching
enriched_papers = []
matched_count = 0
unmatched_papers = []

print("\nMatching papers...")
for paper_id, paper_data in unique_papers.items():
    abstract_excerpt = paper_data.get('abstract_excerpt', '')

    # Try to find match in arXiv CSV
    matched = False
    best_match_score = 0
    best_match_idx = None

    # Search for abstract matches (first 150 chars for efficiency)
    search_text = abstract_excerpt[:150].lower() if abstract_excerpt else ""

    if search_text:
        for idx, row in arxiv_df.iterrows():
            arxiv_abstract = str(row.get('abstract', '')).lower()

            # Quick check: does abstract start with our excerpt?
            if arxiv_abstract.startswith(search_text[:50]):
                # More thorough fuzzy match
                score = fuzz.partial_ratio(search_text, arxiv_abstract[:200])
                if score > best_match_score:
                    best_match_score = score
                    best_match_idx = idx

    if best_match_score >= 85:  # High confidence threshold
        # Extract metadata
        matched_row = arxiv_df.iloc[best_match_idx]

        author_short, author_full = format_authors(matched_row.get('firstAuthor'))
        arxiv_id = extract_arxiv_id(matched_row.get('url'))
        year = extract_year(matched_row.get('dateSubmitted'))
        title = matched_row.get('title', 'Unknown Title')
        keywords = matched_row.get('keywords', '')

        # Format IEEE citation
        if arxiv_id and year:
            ieee_citation = f"{author_short}, \"{title},\" arXiv preprint arXiv:{arxiv_id}, {year}."
        else:
            ieee_citation = f"{author_short}, \"{title}.\""

        enriched_paper = {
            "paper_id": paper_id,
            "abstract_excerpt": abstract_excerpt,
            "metadata_enriched": True,
            "match_confidence": best_match_score,
            "metadata": {
                "title": title,
                "authors": author_short,
                "author_full": author_full,
                "year": int(year) if year and year.isdigit() else None,
                "venue": "arXiv",
                "arxiv_id": arxiv_id,
                "arxiv_url": f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None,
                "doi": None,  # Not available in dataset
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
        print(f"✓ Matched: {paper_id[:8]}... -> {title[:50]}... (Score: {best_match_score})")
    else:
        # No match found
        unmatched_paper = {
            "paper_id": paper_id,
            "abstract_excerpt": abstract_excerpt,
            "metadata_enriched": False,
            "match_confidence": best_match_score,
            "metadata": None,
            "citation_ieee": f"[Paper ID: {paper_id[:12]}] Abstract: {abstract_excerpt[:100]}... [Metadata pending]",
            "relevance": paper_data.get('relevance', 'medium'),
            "techniques": paper_data.get('techniques', []),
            "primary_technique": paper_data.get('primary_technique', ''),
            "mention_count": paper_data.get('mention_count', 0)
        }

        enriched_papers.append(unmatched_paper)
        unmatched_papers.append(unmatched_paper)
        print(f"✗ No match: {paper_id[:8]}... (Best score: {best_match_score})")

print(f"\n=== ENRICHMENT SUMMARY ===")
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

with open(base_dir / 'master-tier1-citations-enriched.json', 'w', encoding='utf-8') as f:
    json.dump(enriched_master, f, indent=2, ensure_ascii=False)

print(f"\n✓ Saved: master-tier1-citations-enriched.json")

# Now distribute enriched papers back to individual document citation files
print("\n=== DISTRIBUTING TO DOCUMENT FILES ===")

for doc_file in citation_files:
    # Load original doc citations
    with open(base_dir / doc_file, 'r', encoding='utf-8') as f:
        doc_citations = json.load(f)

    # Enrich papers in this document
    enriched_doc_papers = []

    for technique, papers in doc_citations['citations_by_technique'].items():
        enriched_technique_papers = []

        for paper in papers:
            paper_id = paper['paper_id']

            # Find enriched version
            enriched_version = next((p for p in enriched_papers if p['paper_id'] == paper_id), None)

            if enriched_version:
                enriched_technique_papers.append(enriched_version)
            else:
                # Shouldn't happen, but fallback
                enriched_technique_papers.append(paper)

        doc_citations['citations_by_technique'][technique] = enriched_technique_papers

    # Save enriched doc file
    output_file = doc_file.replace('-extracted.json', '-enriched.json')
    with open(base_dir / output_file, 'w', encoding='utf-8') as f:
        json.dump(doc_citations, f, indent=2, ensure_ascii=False)

    print(f"✓ Saved: {output_file}")

print("\n=== ENRICHMENT COMPLETE ===")
print(f"Files created:")
print(f"  - master-tier1-citations-enriched.json")
print(f"  - doc1-citations-enriched.json")
print(f"  - doc2-citations-enriched.json")
print(f"  - doc3-citations-enriched.json")
print(f"  - doc4-citations-enriched.json")
