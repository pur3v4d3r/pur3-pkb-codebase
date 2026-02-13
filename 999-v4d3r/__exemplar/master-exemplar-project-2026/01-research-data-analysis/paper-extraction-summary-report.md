# Paper Extraction Summary Report

**Project**: Master Exemplar Document Series
**Phase**: 0 - Paper Extraction & Technique Mapping
**Date**: 2026-02-13

---

## Executive Summary

- **Total Papers Processed**: 1,464
- **Papers with Techniques**: 1,184 (80.9%)
- **Papers without Techniques**: 280 (19.1%)
- **Unique Techniques Identified**: 31
- **Average Techniques per Paper**: 1.74
- **Median Techniques per Paper**: 1
- **Maximum Techniques in Single Paper**: 7

---

## Top 20 Most Common Techniques

1. **Few-Shot**: 212 papers (14.5%)
2. **Prompt Engineering**: 161 papers (11.0%)
3. **Zero-Shot**: 143 papers (9.8%)
4. **Fine-tuning**: 106 papers (7.2%)
5. **In-Context Learning**: 87 papers (5.9%)
6. **Few-Shot Prompting**: 67 papers (4.6%)
7. **Chain-of-Thought**: 63 papers (4.3%)
8. **Automatic Prompt**: 14 papers (1.0%)
9. **Prompt Tuning**: 14 papers (1.0%)
10. **One-Shot**: 12 papers (0.8%)
11. **Jailbreaking**: 11 papers (0.8%)
12. **Decomposed Prompting**: 11 papers (0.8%)
13. **Boosting**: 7 papers (0.5%)
14. **RAG**: 7 papers (0.5%)
15. **Instruction Following**: 7 papers (0.5%)
16. **RLHF**: 6 papers (0.4%)
17. **Self-Consistency**: 5 papers (0.3%)
18. **ReAct**: 3 papers (0.2%)
19. **Self-Ask**: 3 papers (0.2%)
20. **Analogical Prompting**: 2 papers (0.1%)

---

## Technique Coverage Analysis

- **High Coverage** (≥100 papers): 4 techniques
- **Medium Coverage** (20-99 papers): 3 techniques
- **Low Coverage** (5-19 papers): 10 techniques
- **Rare Coverage** (<5 papers): 14 techniques

---

## Top 10 Technique Co-occurrences

1. **Fine-tuning** + **Few-Shot**: 138 papers
2. **Few-Shot** + **Zero-Shot**: 127 papers
3. **Few-Shot** + **In-Context Learning**: 92 papers
4. **Few-Shot** + **Few-Shot Prompting**: 78 papers
5. **Fine-tuning** + **In-Context Learning**: 68 papers
6. **In-Context Learning** + **Zero-Shot**: 61 papers
7. **Fine-tuning** + **Zero-Shot**: 58 papers
8. **Few-Shot** + **Chain-of-Thought**: 53 papers
9. **Prompt Engineering** + **Zero-Shot**: 49 papers
10. **Fine-tuning** + **Prompt Engineering**: 46 papers

---

## Most Comprehensive Papers

Papers mentioning the most diverse set of techniques:

### 1. 7 Techniques

**Paper ID**: `d5a6fc6aa139066e3b66ba63002e7d84c109aebc`

**Techniques**: Boosting, Chain-of-Thought, Few-Shot, Few-Shot Prompting, In-Context Learning, Prompt Engineering, Zero-Shot

**Excerpt**: Large language models (LLMs) have shown remarkable capabilities in Natural Language Processing (NLP), especially in domains where labeled data is scarce or expensive, such as clinical domain. However,...

### 2. 6 Techniques

**Paper ID**: `370cea8b4220917f45a69358c0303df71f5063c7`

**Techniques**: Analogical Prompting, Chain-of-Thought, Few-Shot, In-Context Learning, Prompt Engineering, Zero-Shot

**Excerpt**: Large language models (LLMs) have a substantial capacity for high-level analogical reasoning: reproducing patterns in linear text that occur in their training data (zero-shot evaluation) or in the pro...

### 3. 6 Techniques

**Paper ID**: `cc43306e22dbfd5bc35251ab8c8ba37e4fc2a1b3`

**Techniques**: Chain-of-Thought, Few-Shot, Few-Shot Prompting, Fine-tuning, Prompt Engineering, Zero-Shot

**Excerpt**: Large language models that are capable of zero or few-shot prompting approaches have given rise to the new research area of prompt engineering. Recent advances showed that for example Chain-of-Thought...

### 4. 6 Techniques

**Paper ID**: `None`

**Techniques**: Few-Shot, Few-Shot Prompting, Fine-tuning, In-Context Learning, Prompt Engineering, Self-Consistency

**Excerpt**:   Text-to-SQL aims to automate the process of generating SQL queries on adatabase from natural language text. In this work, we propose "SQLPrompt",tailored to improve the few-shot prompting capabiliti...

### 5. 5 Techniques

**Paper ID**: `4ee96f0757e517928590a2300af5d40ba768a5a7`

**Techniques**: Chain-of-Thought, Decomposed Prompting, Few-Shot, Few-Shot Prompting, Zero-Shot

**Excerpt**: Strategies such as chain-of-thought prompting improve the performance of large language models (LLMs) on complex reasoning tasks by decomposing input examples into intermediate steps. However, it rema...

### 6. 5 Techniques

**Paper ID**: `4610ffb1b016acaa82a2065ffd1a3adbae1ce722`

**Techniques**: Automatic Prompt, Few-Shot, In-Context Learning, Prompt Engineering, Zero-Shot

**Excerpt**: By conditioning on natural language instructions, large language models (LLMs) have displayed impressive capabilities as general-purpose computers. However, task performance depends significantly on t...

### 7. 5 Techniques

**Paper ID**: `994a6040fab375669a92cab0e67fb2fd203cd67f`

**Techniques**: Few-Shot, Fine-tuning, One-Shot, Prompt Engineering, Zero-Shot

**Excerpt**: Rare diseases (RDs) are collectively common and affect 300 million people worldwide. Accurate phenotyping is critical for informing diagnosis and treatment, but RD phenotypes are often embedded in uns...

### 8. 5 Techniques

**Paper ID**: `04e838c16f3d1fb8d69d34fe0a0a92c59717875b`

**Techniques**: Chain-of-Thought, Few-Shot, Few-Shot Prompting, In-Context Learning, Zero-Shot

**Excerpt**: Language models are achieving impressive performance on various tasks by aggressively adopting inference-time prompting techniques, such as zero-shot and few-shot prompting. In this work, we introduce...

### 9. 5 Techniques

**Paper ID**: `ed40889e11e812ef33578506844be06d713f6092`

**Techniques**: Chain-of-Thought, Few-Shot, In-Context Learning, Self-Ask, Zero-Shot

**Excerpt**: "Thinking is for Doing."Humans can infer other people's mental states from observations--an ability called Theory-of-Mind (ToM)--and subsequently act pragmatically on those inferences. Existing questi...

### 10. 5 Techniques

**Paper ID**: `None`

**Techniques**: Few-Shot, Fine-tuning, In-Context Learning, Instruction Following, Zero-Shot

**Excerpt**:   Foundation models have received much attention due to their effectivenessacross a broad range of downstream applications. Though there is a bigconvergence in terms of architecture, most pretrained m...

---

## Output Files Generated

1. **paper_database.json** - Complete paper records with technique annotations
2. **technique_to_papers_mapping.json** - Cross-reference from techniques to papers
3. **technique_cooccurrence_matrix.json** - Co-occurrence analysis
4. **papers_by_technique/** - Individual markdown bibliographies per technique
5. **paper-extraction-summary-report.md** - This report

---

## Methodology

### Technique Detection

Techniques were identified using case-insensitive pattern matching against a comprehensive taxonomy:

**Basic Techniques**:
- Zero-Shot
- Few-Shot
- One-Shot
- Instruction Following

**Chain-of-Thought Variants**:
- Chain-of-Thought
- Faithful Chain-of-Thought
- Tabular Chain-of-Thought
- Chain-of-Verification
- Chain-of-Density
- Chain-of-Symbol
- Chain-of-Translation
- Chain-of-Draft

**Advanced Reasoning**:
- Tree-of-Thoughts
- Graph-of-Thoughts
- Chain-of-Verification
- Program-of-Thoughts
- Step-Back Prompting
- Least-to-Most Prompting

**Self-Optimization**:
- Self-Consistency
- Self-Refine
- Self-Ask
- Reflexion
- Meta-Prompting
- Meta-Cognitive

### Quality Metrics

- **Coverage Rate**: 80.9% of papers contained at least one identifiable technique
- **Average Technique Density**: 1.74 techniques per paper
- **Technique Diversity**: 31 distinct techniques identified

---

## Next Steps (Phase 1)

With this comprehensive database established, proceed to:

1. **Technique Deep-Dive Analysis** - Extract key insights for each major technique
2. **Exemplar Selection** - Identify best papers for each technique category
3. **Master Document Generation** - Create definitive guides per technique
4. **Cross-Reference Building** - Link related techniques and approaches

---

*Report generated by Research Mining Agent Alpha*
