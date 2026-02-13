# Day 11 Integration Guide
## Citation Integration for Master Exemplar Documents

**Purpose**: Step-by-step instructions for integrating enriched citations into the four Tier 1 master documents.

**Date**: 2026-02-13
**Status**: Ready for Integration
**Match Rate**: 86.4% (19/22 papers fully enriched)

---

## Overview

This guide provides systematic instructions for adding IEEE-formatted citations to each document. All citations have been extracted, enriched with metadata, and formatted for seamless integration.

**Files Prepared**:
- `doc1-bibliography-formatted.md` - 16 citations
- `doc2-bibliography-formatted.md` - 13 citations
- `doc3-bibliography-formatted.md` - 13 citations
- `doc4-bibliography-formatted.md` - 6 citations

---

## Phase 1: Add References Section

### Step 1.1: Locate Insertion Point

For each document, add the References section **before** the final section (usually "Related Topics" or "Conclusion").

**Location Pattern**:
```markdown
[... main content ...]

## 8. Best Practices
[content]

---

## References    <-- INSERT HERE

[1] Author, "Title," source, year.
[2] Author, "Title," source, year.
...

---

## 9. Related Topics for PKB Expansion
[existing content]
```

### Step 1.2: Copy References from Bibliography Files

For each document:

1. Open corresponding `docN-bibliography-formatted.md`
2. Copy the **References** section (numbered citations only)
3. Paste into document at insertion point
4. Verify formatting is preserved

**Example Reference Format**:
```markdown
## References

[1] Freda Shi, "Large Language Models Can Be Easily Distracted by Irrelevant Context," 2023.

[2] Zhihan Liu, "Reason for Future, Act for Now: A Principled Framework for Autonomous LLM Agents with Provable Sample Efficiency," 2023.

[3] Hejia Geng, "UPAR: A Kantian-Inspired Prompting Framework for Enhancing Large Language Model Capabilities," 2023.
```

---

## Phase 2: Add Inline Citations

### Step 2.1: Identify Claims Needing Citations

Search for these types of statements:
- Performance benchmarks (e.g., "achieves 74.5% on GSM8K")
- Technique descriptions (e.g., "Chain-of-Thought improves reasoning")
- Research findings (e.g., "studies show that...")
- Definitions of techniques
- Comparison statements

### Step 2.2: Citation Placement Patterns

**Pattern 1: End of Sentence**
```markdown
BEFORE:
> Chain-of-Thought prompting significantly improves reasoning performance on math word problems.

AFTER:
> Chain-of-Thought prompting significantly improves reasoning performance on math word problems [1].
```

**Pattern 2: Multiple Citations**
```markdown
BEFORE:
> Self-consistency methods aggregate multiple reasoning paths to improve accuracy.

AFTER:
> Self-consistency methods aggregate multiple reasoning paths to improve accuracy [3, 7, 8, 9].
```

**Pattern 3: Inline Citation**
```markdown
BEFORE:
> The ReAct framework combines reasoning and acting capabilities.

AFTER:
> The ReAct framework [2] combines reasoning and acting capabilities.
```

**Pattern 4: Benchmarks**
```markdown
BEFORE:
| Technique | GSM8K | SVAMP | Accuracy |
|-----------|-------|-------|----------|
| CoT | 74.5% | 82.1% | High |

AFTER:
| Technique | GSM8K | SVAMP | Accuracy | Source |
|-----------|-------|-------|----------|--------|
| CoT | 74.5% | 82.1% | High | [1] |
```

### Step 2.3: Citation Mapping by Technique

Use the **Citation Map by Technique** section in each bibliography file to identify which citations support which techniques.

**Example Mapping** (from doc1-bibliography-formatted.md):

```markdown
### Self-Consistency
- [1] Large Language Models Can Be Easily Distracted... **HIGH**
- [7] A Chat About Boring Problems...
- [8] (Paper pending metadata)
- [9] Better patching using LLM prompting...

### ReAct
- [2] Reason for Future, Act for Now... **HIGH**
- [10] Can Large Language Models be Good Path Planners...
- [11] FireAct: Toward Language Agent Fine-tuning...
```

**Application**:

When discussing **Self-Consistency** in the document:
- Primary citation: [1] (high relevance)
- Supporting citations: [7, 9]
- Pending: [8] (use but note needs review)

When discussing **ReAct**:
- Primary citation: [2] (high relevance)
- Supporting citations: [10, 11]

---

## Phase 3: Update Performance Tables

### Step 3.1: Add Citation Column

For tables with benchmark results, add a **Source** column:

**Before**:
```markdown
| Technique | Benchmark | Performance |
|-----------|-----------|-------------|
| CoT | GSM8K | 74.5% |
| Zero-Shot CoT | GSM8K | 65.4% |
| Self-Consistency | MATH | 82.1% |
```

**After**:
```markdown
| Technique | Benchmark | Performance | Source |
|-----------|-----------|-------------|--------|
| CoT | GSM8K | 74.5% | [1] |
| Zero-Shot CoT | GSM8K | 65.4% | [13] |
| Self-Consistency | MATH | 82.1% | [1, 7] |
```

### Step 3.2: Verify Accuracy

Cross-reference performance numbers with cited papers:
1. Open enriched JSON file for document
2. Check `citation_context` field for each paper
3. Verify benchmark numbers match source claims
4. Flag discrepancies for review

---

## Phase 4: Quality Assurance

### Step 4.1: Citation Validation Checklist

- [ ] All references numbered sequentially [1], [2], [3]...
- [ ] No broken citation numbers (e.g., [1], [3], [5] - missing [2], [4])
- [ ] Citations match numbering in References section
- [ ] High-relevance papers cited in primary technique sections
- [ ] Tables include Source column where appropriate
- [ ] No duplicate citations for same statement

### Step 4.2: Formatting Validation

- [ ] IEEE citation format maintained
- [ ] Author names consistent with References section
- [ ] Years included for all enriched citations
- [ ] URLs included where available (arXiv papers)
- [ ] Pending citations flagged with [Metadata pending]

### Step 4.3: Coverage Validation

For each major technique section:
- [ ] At least 1 high-relevance citation
- [ ] Supporting citations for key claims
- [ ] Benchmark tables have sources
- [ ] Example code includes citation if from paper

---

## Phase 5: Handle Unmatched Papers

### Papers Requiring Manual Review (3 papers)

Three papers could not be automatically matched to arXiv metadata. These require manual lookup:

#### 1. Paper ID: 22d5459d...
- **Technique**: Self-Consistency
- **Abstract**: "Large language Models (LLMs) have achieved promising performance on arithmetic reasoning tasks by incorporating step-by-step chain-of-thought (CoT) pr..."
- **Action**: Search arXiv for abstract text, add full metadata
- **Temporary Citation**: `[8] Paper on Self-Consistency: Abstract excerpt... [Paper ID: 22d5459d]`

#### 2. Paper ID: 6384921f...
- **Technique**: Meta-Prompting
- **Abstract**: "Systematic reviews (SRs) are a critical component of evidence-based medicine, but the process of screening titles and abstracts is time-consuming..."
- **Action**: Medical domain paper, search PubMed or arXiv
- **Temporary Citation**: `[16] Paper on Meta-Prompting: Abstract excerpt... [Paper ID: 6384921f]`

#### 3. Paper ID: 191e300e...
- **Technique**: RAG
- **Abstract**: "Text-to-SQL aims at generating SQL queries for the given natural language questions and thus helping users to query databases..."
- **Action**: Search for Text-to-SQL + RAG papers
- **Temporary Citation**: `[17] Paper on RAG: Abstract excerpt... [Paper ID: 191e300e]`

**Process**:
1. Search academic databases for abstract text
2. Extract full metadata (title, authors, year, DOI/arXiv ID)
3. Update JSON files with enriched metadata
4. Re-run `generate_bibliographies.py`
5. Update integrated citations in documents

---

## Phase 6: Document-Specific Guidance

### DOC 1: LLM Reasoning Techniques - Operational Manual

**Key Sections Needing Citations**:
- Section 3.1: Self-Consistency → Use citations [1, 7, 8, 9]
- Section 3.2: ReAct → Use citations [2, 10, 11]
- Section 3.3: Reflexion → Use citation [6]
- Section 3.4: RAG → Use citations [4, 12]
- Section 3.5: Prompt Engineering → Use citation [5]

**Integration Priority**: High
**Estimated Time**: 2-3 hours

### DOC 2: Extended Thinking Architecture - Implementation Guide

**Key Sections Needing Citations**:
- RAG Implementation → Use citations [1, 2, 3, 4, 5, 6, 11]
- Prompt Engineering Patterns → Use citation [7]
- Reflexion Loop → Use citation [8]
- In-Context Learning → Use citation [9]
- Few-Shot Examples → Use citation [10]

**Integration Priority**: High
**Estimated Time**: 2-3 hours

### DOC 3: Advanced Reasoning Architectures - Theory to Practice

**Key Sections Needing Citations**:
- Self-Consistency Deep Dive → Use citations [1, 7, 8, 9, 10]
- ReAct Framework → Use citations [2, 11, 12]
- RAG Architectures → Use citations [3, 4, 5, 13]
- Reflexion → Use citation [6]

**Integration Priority**: Medium-High
**Estimated Time**: 2 hours

### DOC 4: Agentic Workflow Design Patterns

**Key Sections Needing Citations**:
- ReAct Patterns → Use citations [1, 4, 5]
- RAG in Agents → Use citations [2, 6]
- Reflexion Loops → Use citation [3]

**Integration Priority**: Medium
**Estimated Time**: 1-2 hours

---

## Phase 7: Automation Opportunities

### Future Enhancements

1. **Citation Insertion Script**
   - Parse technique sections
   - Auto-insert citations based on keyword matching
   - Flag ambiguous placements for manual review

2. **Validation Script**
   - Check citation numbering
   - Verify all references are cited
   - Identify orphan citations

3. **Metadata Update Pipeline**
   - Periodic re-enrichment against updated arXiv dataset
   - DOI resolution for better metadata
   - Author disambiguation

---

## Timeline Estimate

| Phase | Task | Time Estimate |
|-------|------|---------------|
| 1 | Add References Sections | 30 min |
| 2 | Inline Citations (all docs) | 4-6 hours |
| 3 | Update Tables | 1 hour |
| 4 | Quality Assurance | 1 hour |
| 5 | Manual Review (3 papers) | 1-2 hours |
| **Total** | **Complete Integration** | **7.5-10.5 hours** |

---

## Success Criteria

- [ ] All 4 documents have References sections
- [ ] All key claims and techniques have citations
- [ ] All performance tables include sources
- [ ] IEEE formatting maintained throughout
- [ ] 3 unmatched papers resolved manually
- [ ] Citation numbering validated (no gaps)
- [ ] High-relevance papers cited in primary sections
- [ ] Integration validation checklist complete

---

## Next Steps (Day 12+)

After citation integration is complete:

1. **Visual Enhancements** (Day 12)
   - Add diagrams for ReAct, Self-Consistency, RAG architectures
   - Create technique comparison flowcharts
   - Add code execution trace visualizations

2. **Code Examples** (Day 13)
   - Add working implementations for each technique
   - Include benchmark reproduction code
   - Provide prompt templates

3. **Cross-Document Linking** (Day 14)
   - Add internal references between documents
   - Create technique cross-reference matrix
   - Build navigation guide

4. **Final Polish** (Day 15)
   - Consistency review across all 4 documents
   - Terminology standardization
   - Executive summary generation

---

## Support Resources

- **Enriched Citation Files**: `docN-citations-enriched.json`
- **Formatted Bibliographies**: `docN-bibliography-formatted.md`
- **Master Citation List**: `master-tier1-citations-enriched.json`
- **Citation Map**: Available in each bibliography file
- **Unmatched Papers**: Listed in enrichment report

For questions or issues during integration, refer to the Day 11 Metadata Enrichment Report.
