# Database Usage Guide

**Phase 0 Output Reference**
**For use in Phases 1-5 of Master Exemplar Document Series**

---

## Quick Start

All Phase 0 outputs are located in:
```
D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\master-exemplar-project-2026\01-research-data-analysis\
```

---

## File Descriptions

### 1. paper_database.json

**Purpose**: Complete corpus with technique annotations

**Structure**:
```json
{
  "papers": [
    {
      "id": "paper_hash_string",
      "text": "full abstract text",
      "techniques_mentioned": ["Technique1", "Technique2"],
      "technique_count": 2,
      "text_length": 1234,
      "primary_focus": "Technique1"
    }
  ],
  "summary": {
    "total_papers": 1464,
    "papers_with_techniques": 1184,
    "average_techniques_per_paper": 1.74,
    "technique_distribution": {...}
  }
}
```

**Use Cases**:
- Find all papers mentioning specific technique
- Identify most comprehensive papers (high technique_count)
- Analyze primary focus distribution
- Extract abstracts for specific papers

**Python Usage**:
```python
import json

# Load database
with open('paper_database.json') as f:
    db = json.load(f)

# Find papers with Chain-of-Thought
cot_papers = [p for p in db['papers']
              if 'Chain-of-Thought' in p['techniques_mentioned']]

# Get most comprehensive papers
top_papers = sorted(db['papers'],
                   key=lambda x: x['technique_count'],
                   reverse=True)[:10]

# Papers focused on specific technique
rag_focused = [p for p in db['papers']
               if p['primary_focus'] == 'RAG']
```

---

### 2. technique_to_papers_mapping.json

**Purpose**: Reverse index from techniques to papers

**Structure**:
```json
{
  "technique_map": {
    "Chain-of-Thought": {
      "paper_count": 63,
      "paper_ids": ["id1", "id2", ...],
      "canonical_name": "Chain-of-Thought",
      "aliases": ["chain-of-thought", "cot", ...]
    }
  },
  "statistics": {
    "total_techniques_identified": 31,
    "most_common_techniques": [...],
    "papers_per_technique_avg": 38.26
  }
}
```

**Use Cases**:
- Get all papers for a technique
- Check technique popularity
- Find canonical names and aliases
- Compare technique coverage

**Python Usage**:
```python
import json

# Load mapping
with open('technique_to_papers_mapping.json') as f:
    mapping = json.load(f)

# Get all Chain-of-Thought papers
cot_papers = mapping['technique_map']['Chain-of-Thought']['paper_ids']
print(f"Found {len(cot_papers)} papers")

# Find techniques with >50 papers
popular = {tech: info['paper_count']
          for tech, info in mapping['technique_map'].items()
          if info['paper_count'] > 50}

# Check aliases for a technique
aliases = mapping['technique_map']['Chain-of-Thought']['aliases']
```

---

### 3. technique_cooccurrence_matrix.json

**Purpose**: Analyze which techniques are studied together

**Structure**:
```json
{
  "cooccurrence_matrix": {
    "Few-Shot": {
      "Zero-Shot": 127,
      "Chain-of-Thought": 53,
      ...
    }
  },
  "strong_cooccurrences": [
    {
      "technique_1": "Few-Shot",
      "technique_2": "Zero-Shot",
      "cooccurrence_count": 127
    }
  ],
  "summary": {
    "total_technique_pairs": 38,
    "strong_pairs_count": 38
  }
}
```

**Use Cases**:
- Find related techniques
- Identify common combinations
- Discover research trends
- Plan document cross-references

**Python Usage**:
```python
import json

# Load co-occurrence data
with open('technique_cooccurrence_matrix.json') as f:
    cooccur = json.load(f)

# Find techniques commonly used with Chain-of-Thought
cot_related = cooccur['cooccurrence_matrix'].get('Chain-of-Thought', {})
cot_related_sorted = sorted(cot_related.items(),
                           key=lambda x: x[1],
                           reverse=True)

# Get top 10 strongest pairs overall
top_pairs = cooccur['strong_cooccurrences'][:10]
```

---

### 4. papers_by_technique/*.md

**Purpose**: Human-readable bibliographies per technique

**Structure** (Markdown):
```markdown
# Papers on [Technique]

**Total Papers**: X
**Canonical Name**: [Name]
**Aliases**: [list]

## Papers (Sorted by comprehensiveness)

### 1. Paper
**Paper ID**: `hash`
**Techniques Mentioned** (N): [list]
**Abstract Excerpt**: [text...]

## Statistics
- Average techniques per paper: X.XX
- Top Co-occurring Techniques: [list]
```

**Use Cases**:
- Quick reference for technique research
- Identify exemplar papers
- Understand technique context
- Select papers for deep-dive analysis

**Recommended Reading Order**:
1. Start with high-coverage techniques (Few-Shot, Prompt Engineering, Zero-Shot)
2. Review papers sorted by comprehensiveness (top papers in each file)
3. Note co-occurring techniques for cross-referencing

---

## Common Queries

### Query 1: Find Best Papers for Technique X

```python
import json

# Load databases
with open('paper_database.json') as f:
    papers_db = json.load(f)
with open('technique_to_papers_mapping.json') as f:
    mapping = json.load(f)

def get_best_papers(technique, top_n=5):
    # Get paper IDs for this technique
    paper_ids = set(mapping['technique_map'][technique]['paper_ids'])

    # Filter and sort by technique count (comprehensiveness)
    papers = [p for p in papers_db['papers'] if p['id'] in paper_ids]
    papers.sort(key=lambda x: x['technique_count'], reverse=True)

    return papers[:top_n]

# Example: Get 5 best Chain-of-Thought papers
best_cot = get_best_papers('Chain-of-Thought', 5)
for p in best_cot:
    print(f"ID: {p['id']}")
    print(f"Techniques: {p['technique_count']}")
    print(f"Focus: {p['primary_focus']}")
    print()
```

### Query 2: Find Papers Combining Multiple Techniques

```python
def find_multi_technique_papers(techniques, papers_db):
    """Find papers mentioning all specified techniques."""
    matching = []
    for paper in papers_db['papers']:
        if all(tech in paper['techniques_mentioned'] for tech in techniques):
            matching.append(paper)
    return matching

# Example: Papers using both CoT and Few-Shot
combo_papers = find_multi_technique_papers(
    ['Chain-of-Thought', 'Few-Shot'],
    papers_db
)
print(f"Found {len(combo_papers)} papers")
```

### Query 3: Technique Popularity Ranking

```python
def rank_techniques(mapping):
    """Rank techniques by paper count."""
    techs = mapping['technique_map']
    ranked = sorted(techs.items(),
                   key=lambda x: x[1]['paper_count'],
                   reverse=True)

    for i, (tech, info) in enumerate(ranked, 1):
        pct = (info['paper_count'] / 1464) * 100
        print(f"{i}. {tech}: {info['paper_count']} papers ({pct:.1f}%)")

rank_techniques(mapping)
```

### Query 4: Get Full Abstract by Paper ID

```python
def get_paper_by_id(paper_id, papers_db):
    """Retrieve full paper record by ID."""
    for paper in papers_db['papers']:
        if paper['id'] == paper_id:
            return paper
    return None

# Example
paper = get_paper_by_id('d5a6fc6aa139066e3b66ba63002e7d84c109aebc', papers_db)
print(paper['text'])  # Full abstract
```

### Query 5: Analyze Technique Relationships

```python
def get_related_techniques(technique, cooccur_data, threshold=10):
    """Find techniques commonly paired with target technique."""
    matrix = cooccur_data['cooccurrence_matrix']
    related = matrix.get(technique, {})

    # Filter by threshold
    related_filtered = {k: v for k, v in related.items() if v >= threshold}

    # Sort by frequency
    return sorted(related_filtered.items(), key=lambda x: x[1], reverse=True)

# Example: What's commonly used with Chain-of-Thought?
related = get_related_techniques('Chain-of-Thought', cooccur, threshold=10)
for tech, count in related:
    print(f"{tech}: {count} papers")
```

---

## Phase 1 Workflows

### Workflow A: Technique Deep-Dive

**Goal**: Create comprehensive document for one technique

**Steps**:
1. Load `papers_by_technique/[technique]_papers.md`
2. Identify top 5-10 papers by comprehensiveness
3. Load full abstracts from `paper_database.json`
4. Extract key methodologies and insights
5. Note co-occurring techniques for cross-references
6. Create master document with examples

**Python Template**:
```python
import json

# 1. Select technique
technique = "Chain-of-Thought"

# 2. Load data
with open('paper_database.json') as f:
    papers_db = json.load(f)
with open('technique_to_papers_mapping.json') as f:
    mapping = json.load(f)

# 3. Get papers for this technique
paper_ids = mapping['technique_map'][technique]['paper_ids']
papers = [p for p in papers_db['papers'] if p['id'] in paper_ids]

# 4. Sort by comprehensiveness
papers.sort(key=lambda x: x['technique_count'], reverse=True)

# 5. Select top papers for analysis
top_papers = papers[:10]

# 6. Extract abstracts
for paper in top_papers:
    print(f"\n{'='*80}")
    print(f"Paper ID: {paper['id']}")
    print(f"Techniques: {', '.join(paper['techniques_mentioned'])}")
    print(f"Primary Focus: {paper['primary_focus']}")
    print(f"\nAbstract:")
    print(paper['text'])
```

### Workflow B: Cross-Technique Analysis

**Goal**: Understand relationships between techniques

**Steps**:
1. Select primary technique
2. Load co-occurrence data
3. Identify related techniques
4. Find papers using technique combinations
5. Extract common patterns
6. Create relationship documentation

**Python Template**:
```python
import json

# Load data
with open('paper_database.json') as f:
    papers_db = json.load(f)
with open('technique_cooccurrence_matrix.json') as f:
    cooccur = json.load(f)

# Primary technique
primary = "Chain-of-Thought"

# Get related techniques
related = cooccur['cooccurrence_matrix'].get(primary, {})
top_related = sorted(related.items(), key=lambda x: x[1], reverse=True)[:5]

print(f"Techniques commonly used with {primary}:")
for tech, count in top_related:
    print(f"  - {tech}: {count} papers")

    # Find example papers using both
    combo_papers = [p for p in papers_db['papers']
                   if primary in p['techniques_mentioned']
                   and tech in p['techniques_mentioned']]

    if combo_papers:
        best = max(combo_papers, key=lambda x: x['technique_count'])
        print(f"    Example: {best['id'][:16]}...")
```

### Workflow C: Exemplar Selection

**Goal**: Choose best papers for documentation

**Criteria**:
1. High technique density (comprehensive)
2. Primary focus matches target technique
3. Includes co-occurring techniques (for context)
4. Clear abstract (readable and informative)

**Python Template**:
```python
def score_paper_as_exemplar(paper, target_technique):
    """Score paper suitability as exemplar."""
    score = 0

    # Mentions target technique
    if target_technique in paper['techniques_mentioned']:
        score += 10

    # Primary focus is target
    if paper['primary_focus'] == target_technique:
        score += 20

    # Comprehensive (multiple techniques)
    score += paper['technique_count'] * 5

    # Longer abstract (more detail)
    score += min(paper['text_length'] / 100, 10)

    return score

# Rank papers for a technique
technique = "Chain-of-Thought"
paper_ids = mapping['technique_map'][technique]['paper_ids']
papers = [p for p in papers_db['papers'] if p['id'] in paper_ids]

# Score and rank
scored = [(p, score_paper_as_exemplar(p, technique)) for p in papers]
scored.sort(key=lambda x: x[1], reverse=True)

# Top 5 exemplars
print(f"Top 5 exemplar papers for {technique}:")
for i, (paper, score) in enumerate(scored[:5], 1):
    print(f"{i}. Score: {score:.1f}")
    print(f"   ID: {paper['id']}")
    print(f"   Techniques: {paper['technique_count']}")
    print(f"   Focus: {paper['primary_focus']}")
    print()
```

---

## Best Practices

### For Phase 1 Analysis

1. **Start with high-coverage techniques** (Few-Shot, Prompt Engineering, Zero-Shot)
   - More papers = more examples
   - Well-established methodologies
   - Clear patterns emerge

2. **Use comprehensiveness as quality proxy**
   - Papers mentioning multiple techniques tend to be surveys or comprehensive studies
   - Better for understanding relationships and context

3. **Cross-reference co-occurring techniques**
   - Understand why techniques are combined
   - Identify complementary approaches
   - Plan document structure

4. **Read markdown bibliographies first**
   - Get overview before diving into JSON
   - Understand technique context
   - Identify interesting papers

### For Document Generation

1. **Include multiple exemplars per technique**
   - Show variety of applications
   - Demonstrate different combinations
   - Cover edge cases

2. **Link related techniques**
   - Use co-occurrence data
   - Create cross-references
   - Build knowledge graph

3. **Cite paper IDs**
   - Enable traceability
   - Support verification
   - Allow future expansion

---

## Troubleshooting

### Issue: Paper ID not found

**Cause**: Paper has no ID (None value in database)

**Solution**: Filter None values
```python
papers = [p for p in papers_db['papers'] if p['id'] is not None]
```

### Issue: Technique not in mapping

**Cause**: Technique name mismatch or technique not detected

**Solution**: Check canonical names and aliases
```python
# List all techniques
techniques = list(mapping['technique_map'].keys())
print(techniques)

# Check aliases
for tech, info in mapping['technique_map'].items():
    if 'cot' in ' '.join(info['aliases']).lower():
        print(f"Found: {tech}")
```

### Issue: Empty co-occurrence data

**Cause**: Technique appears in <5 papers

**Solution**: Check paper count first
```python
count = mapping['technique_map'][technique]['paper_count']
if count < 5:
    print(f"Only {count} papers - insufficient for co-occurrence")
```

---

## Support Files

- **PHASE-0-COMPLETION-REPORT.md**: Detailed completion report
- **paper-extraction-summary-report.md**: Executive summary with statistics
- **extract_techniques.py**: Source code (for reference or modifications)

---

## Contact & Updates

For issues or questions about the database:
- Review PHASE-0-COMPLETION-REPORT.md for methodology
- Check technique_to_papers_mapping.json for canonical names
- Consult paper-extraction-summary-report.md for statistics

---

*Database Usage Guide - Phase 0 Output Reference*
*Last Updated: 2026-02-13*
