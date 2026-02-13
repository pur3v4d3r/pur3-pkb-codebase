import json
from pathlib import Path

base_dir = Path(r"D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\master-exemplar-project-2026\02-planning-documents\tier1-enhancement-plans")

# Document names
doc_names = {
    "doc1": "LLM Reasoning Techniques - Operational Manual",
    "doc2": "Extended Thinking Architecture - Implementation Guide",
    "doc3": "Advanced Reasoning Architectures - Theory to Practice",
    "doc4": "Agentic Workflow Design Patterns"
}

# Load enriched files and generate bibliographies
for doc_num in range(1, 5):
    doc_file = f"doc{doc_num}-citations-enriched.json"
    doc_name = doc_names[f"doc{doc_num}"]

    with open(base_dir / doc_file, 'r', encoding='utf-8') as f:
        doc_data = json.load(f)

    # Collect all unique papers used in this document
    all_papers = []
    paper_ids_seen = set()

    for technique, papers in doc_data['citations_by_technique'].items():
        for paper in papers:
            paper_id = paper['paper_id']
            if paper_id not in paper_ids_seen:
                all_papers.append(paper)
                paper_ids_seen.add(paper_id)

    # Sort by primary technique and then by relevance
    all_papers.sort(key=lambda x: (x.get('primary_technique', 'Unknown'), x.get('relevance', 'medium') != 'high'))

    # Generate bibliography markdown
    bibliography_md = f"""# {doc_name}
## Bibliography

This document references {len(all_papers)} research papers covering advanced LLM prompting and reasoning techniques.

---

## References

"""

    # Generate numbered citations
    for i, paper in enumerate(all_papers, 1):
        if paper.get('metadata_enriched'):
            metadata = paper['metadata']
            title = metadata.get('title', 'Unknown Title')
            authors = metadata.get('authors', 'Unknown Author')
            year = metadata.get('year', 'n.d.')
            arxiv_id = metadata.get('arxiv_id', 'N/A')
            arxiv_url = metadata.get('arxiv_url', '')

            # Format citation
            if arxiv_url:
                citation = f"[{i}] {authors}, \"{title},\" {arxiv_url}, {year}."
            elif arxiv_id and arxiv_id != 'N/A':
                citation = f"[{i}] {authors}, \"{title},\" arXiv:{arxiv_id}, {year}."
            else:
                citation = f"[{i}] {authors}, \"{title},\" {year}."
        else:
            # Unmatched paper
            citation = paper['citation_ieee']

        bibliography_md += f"{citation}\n\n"

    # Add citation mapping by technique
    bibliography_md += """---

## Citation Map by Technique

This section maps citations to the specific techniques they support.

"""

    # Group by technique
    by_technique = {}
    for technique, papers in doc_data['citations_by_technique'].items():
        by_technique[technique] = []
        for paper in papers:
            paper_id = paper['paper_id']
            # Find citation number
            citation_num = None
            for i, p in enumerate(all_papers, 1):
                if p['paper_id'] == paper_id:
                    citation_num = i
                    break

            if citation_num:
                by_technique[technique].append({
                    'num': citation_num,
                    'title': paper.get('metadata', {}).get('title', '') if paper.get('metadata_enriched') else '',
                    'relevance': paper.get('relevance', 'medium'),
                    'context': paper.get('citation_context', '')
                })

    # Output by technique
    for technique in sorted(by_technique.keys()):
        bibliography_md += f"### {technique}\n\n"

        citations = by_technique[technique]
        for citation in citations:
            title_preview = citation['title'][:60] + "..." if len(citation['title']) > 60 else citation['title']
            relevance_marker = "**HIGH**" if citation['relevance'] == 'high' else ""

            bibliography_md += f"- [{citation['num']}] {title_preview} {relevance_marker}\n"
            if citation['context']:
                bibliography_md += f"  - *Usage*: {citation['context']}\n"

        bibliography_md += "\n"

    # Add enrichment statistics
    enriched_count = sum(1 for p in all_papers if p.get('metadata_enriched'))
    bibliography_md += f"""---

## Enrichment Statistics

- **Total Citations**: {len(all_papers)}
- **Fully Enriched**: {enriched_count} ({enriched_count/len(all_papers)*100:.1f}%)
- **Pending Manual Review**: {len(all_papers) - enriched_count}
- **Techniques Covered**: {len(doc_data['citations_by_technique'])}

"""

    # Save bibliography file
    output_file = f"doc{doc_num}-bibliography-formatted.md"
    with open(base_dir / output_file, 'w', encoding='utf-8') as f:
        f.write(bibliography_md)

    print(f"[OK] Generated: {output_file}")

print("\n[OK] All bibliographies generated successfully")
