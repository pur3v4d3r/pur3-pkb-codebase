# Scaling PDF to Markdown Conversion with Marker + Local LLMs

This is a rough outline for a pipeline for converting approximatley 1100 academic PDFs into Markdown files suitable for Obsidian, using Marker for the heavy lifting and a local LLM for post-processing enrichment.
- Desgin this pipeline using your knowledge of python and scripting.
- Test the pipeline on small batches at first so we dont end up hurting gpu by overheating, it should handle this fine though I have a RTX4090.
- **Local Model to use** -> `qwen2.5:14b-instruct-q5_K_M`
- For the LLM pass lets just stick with a complete metadata for each markdownfile using the template below, for guidence on how to prompt the Local LLM. And not worry aboput adding in wiki links for now, we can add that in later if we want to.


## Key Locations:

`D:\10_pur3v4d3r's-vault\999-v4d3r\__prompt-engineering-guidance\research-papers\pdfs` → Your raw PDFs


`D:\10_pur3v4d3r's-vault\99-scripts` -> Where you can put the scripts

`D:\10_pur3v4d3r's-vault\999-v4d3r\__exemplar\01-research-data-analysis` -> some information from another project that maybe useful

`D:\10_pur3v4d3r's-vault\999-report-organizing\pdf-to-markdown` -> where you can put the converted markdown files

## Phase 1: Triage First

Don't convert everything blindly. Classify the corpus first:

```python
import fitz
import os
from pathlib import Path

def classify_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    page = doc[0]
    text = page.get_text()
    
    # Scanned PDFs have near-zero extractable text
    if len(text.strip()) < 100:
        return "scanned"
    return "digital"

pdf_dir = Path("your_pdfs/")
digital, scanned = [], []

for pdf in pdf_dir.glob("**/*.pdf"):
    category = classify_pdf(pdf)
    (digital if category == "digital" else scanned).append(pdf)

print(f"Digital: {len(digital)} | Scanned: {len(scanned)}")
```

This splits your workload — digital PDFs get fast Marker conversion, scanned ones need the vision LLM pipeline.

---

## Phase 2: Batch Conversion with Marker

Marker is built for this. With your 4090 you can run aggressive parallelization:

```python
import subprocess
from pathlib import Path
import concurrent.futures
import json
from datetime import datetime

OUTPUT_DIR = Path("D:/10_pur3v4d3r's-vault/your-papers-dir/")
INPUT_DIR = Path("your_pdfs/")
LOG_FILE = Path("conversion_log.json")

def convert_single(pdf_path: Path) -> dict:
    out_path = OUTPUT_DIR / pdf_path.stem
    out_path.mkdir(parents=True, exist_ok=True)
    
    result = subprocess.run([
        "marker_single", str(pdf_path), str(out_path),
        "--langs", "English",
        "--batch_multiplier", "4",   # Scale with VRAM
    ], capture_output=True, text=True)
    
    return {
        "file": str(pdf_path.name),
        "status": "success" if result.returncode == 0 else "failed",
        "error": result.stderr if result.returncode != 0 else None,
        "timestamp": datetime.now().isoformat()
    }

def batch_convert(pdf_list: list, workers: int = 4):
    log = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(convert_single, p): p for p in pdf_list}
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            result = future.result()
            log.append(result)
            print(f"[{i+1}/{len(pdf_list)}] {result['file']} → {result['status']}")
    
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)
    
    return log

log = batch_convert(digital_pdfs)
```

> **VRAM note:** `--batch_multiplier 4` is aggressive for a 4090 (24GB). Start at 2, scale up. Monitor with `nvidia-smi` during first run.

---

## Phase 3: Obsidian Post-Processing

This is where your PKB integration lives. After Marker outputs raw Markdown, a local LLM pass enforces your vault's schema:

```python
from ollama import Client  # or however you're serving local LLMs
import re

client = Client()

FRONTMATTER_PROMPT = """
You are a PKB metadata architect. Given this academic paper converted to Markdown,
generate YAML frontmatter and inject Obsidian [[Wiki-Links]] for key concepts.

Rules:
- Extract: title, authors, year, venue, tags (from content)
- Wiki-link all significant concepts, models, techniques
- Add a #summary callout block at the top (3-4 sentences)
- Output the COMPLETE document with frontmatter prepended

Paper content:
{content}
"""

def enrich_markdown(md_path: Path) -> str:
    content = md_path.read_text(encoding="utf-8")
    
    # Truncate for context window if needed — use first 8k chars for metadata extraction
    sample = content[:8000]
    
    response = client.generate(
        model="qwen2.5:72b",  # or whatever you're running
        prompt=FRONTMATTER_PROMPT.format(content=sample),
    )
    
    enriched = response['response'] + "\n\n---\n\n" + content
    md_path.write_text(enriched, encoding="utf-8")
    return enriched
```

---

## Phase 4: Deduplication (Critical at 1000+ Scale)

You almost certainly have duplicates — same paper, different filenames:

```python
import hashlib
from collections import defaultdict

def find_duplicates(pdf_dir: Path) -> dict:
    hashes = defaultdict(list)
    
    for pdf in pdf_dir.glob("**/*.pdf"):
        file_hash = hashlib.md5(pdf.read_bytes()).hexdigest()
        hashes[file_hash].append(pdf)
    
    duplicates = {h: files for h, files in hashes.items() if len(files) > 1}
    print(f"Found {len(duplicates)} duplicate groups")
    return duplicates
```

---

## Recommended Run Order

```
1. classify_pdfs()          → splits digital / scanned
2. deduplicate()            → removes redundant work  
3. batch_convert(digital)   → Marker, overnight run
4. enrich_markdown()        → local LLM frontmatter pass
5. manual review scanned    → vision LLM on remainder
```

---

## Realistic Time Estimates (RTX 4090)

| Stage | Est. Time |
|---|---|
| Classification (1000 PDFs) | ~5 min |
| Marker batch (digital) | 2–6 hrs depending on PDF density |
| LLM enrichment pass | 4–10 hrs at 72B |
| Total end-to-end | ~overnight |










# PKB Metadata Template
This final section is a YAML Metadata template that should be included at the beginning of each report.
- Ensuring consistent documentation and classification across my PKB.

```yaml
---
# DOCUMENT IDENTIFICATION

doc_id: {{Unique identifier for this document, e.g., "Foundational_Report_001"}}
doc_type: Foundational Report
doc_created: {{Creation date, e.g., "2024-06-01"}}
doc_modified: {{Last modified date, e.g., "2024-06-01"}}
author: {{Author's name, e.g., "ChatGPT"}}

# CLASSIFICATION & DISCOVERY
primary_domain: {{Primary domain of knowledge, e.g., "Cognitive Science"}}
secondary_domains: {{List of secondary domains, e.g., ["Philosophy", "Neuroscience"]}}
related_concepts: {{List of related concepts, e.g., ["[[Concept-A]]", "[[Theory B]]"]}}
knowledge_level: {{Level of depth, e.g., "Encyclopedic overview", "In-depth technical analysis", "Historical context"}}
tags: {{List of relevant tags, e.g., ["#cognition", "#philosophy", "#neuroscience"]}}

# QUALITY & STATUS
status: {{Current status of the document, e.g., "evergreen", "draft", "needs review"}}
maturity: {{Maturity level, e.g., "highly developed", "in progress", "conceptual"}}
confidence: {{Confidence level in the content, e.g., "high", "medium", "low"}}

# REASONING ARCHITECTURE
reasoning_tier: {{Tier of reasoning, e.g., "Tier 1: Foundational Understanding", "Tier 2: Analytical Depth", "Tier 3: Synthesis & Innovation"}}
reasoning_methods: {{List of reasoning methods used, e.g., ["Deductive reasoning", "Inductive reasoning", "Analogical reasoning"]}}
reasoning_technique: {{Specific techniques employed, e.g., "Socratic questioning", "Thought experiments", "Comparative analysis"}}

# EPISTEMIC & VALIDATION
epistemic_status: {{Epistemic status, e.g., "well-established", "emerging theory", "speculative"}}
validation_methods: {{Methods used for validation, e.g., "Peer review", "Empirical evidence", "Logical consistency"}}
test_coverage: {{Scope of testing, e.g., "Comprehensive", "Limited", "Theoretical"}}
validation_results: {{Summary of validation results, e.g., "Consistent with existing literature", "Requires further empirical testing", "Contradicted by recent studies"}}
validation_date: {{Date of last validation, e.g., "2024-06-01"}}
factual_verification: {{Status of factual verification, e.g., "Verified", "Partially verified", "Not verified"}}
hallucination_check: {{Status of hallucination check, e.g., "True", "False"}}

# SOURCE & ATTRIBUTION
source: {{Primary source of information, e.g., "Academic journals", "Books", "Expert interviews", "claude-sonnet-4.5"}}
based_on_prompts: {{List of prompts used to generate the content, e.g., ["Prompt 1: Define the core principles of cognitive science", "Prompt 2: Explain the historical development of cognitive science"]}}

# KNOWLEDGE GRAPH INTEGRATION
related_concepts:
  - "[[Concept-A]]"
  - "[[Theory B]]"

prerequisites:
  - "[[Prerequisite Concept 1]]"
  - "[[Prerequisite Concept 2]]"

builds_on:
  - "[[Theory X]]"
  - "[[Concept-Y]]"

extends:
  - "[[Concept Z]]"
  - "[[Theory W]]"

# ALIASES & LINKING
aliases:
  - "[[Alias 1]]"
  - "[[Alias 2]]"

link_up: "[[Higher-Level Concept]]"
link_down: "[[Lower-Level Concept]]"
link_related:
  - "[[Related Concept 1]]"
  - "[[Related Concept 2]]"

# ADDITIONAL METADATA
summary: {{A brief summary of the document, e.g., "This report provides an in-depth analysis of the core principles of cognitive science, exploring its historical development, key theories, and implications for understanding human cognition."}}
keywords: {{List of keywords, e.g., ["cognition", "neuroscience", "philosophy", "cognitive science"]}}

---
```







# Complete Metadata Template Explanation

This is How the Yaml at the front Must look in order to be consistent with the rest of the PKB and to ensure that it is properly integrated into the knowledge graph. Each field should be filled out with accurate and relevant information to facilitate discovery, classification, and connection within the PKB.

---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Critical Thinking Skills and Metacognitive Self-Regulation"
aliases:
  - Critical Thinking Deployment
  - Metacognitive Self-Regulation in Reasoning
  - Applied Critical Thinking Framework
  - PENCRISAL-MAI Integration
  - CT-MSR Framework
  - Situational Critical Thinking
  - Metacognitive Control of Reasoning
  - Critical Thinking Architecture
type: permanent-note
status: evergreen
confidence: high

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  # Content Type
  - permanent-note
  - academic-synthesis
  - reference-note
  - practical-framework
  
  # Domain (hierarchical)
  - cognitive-psychology/metacognition
  - cognitive-psychology/critical-thinking
  - educational-psychology/learning-strategies
  - cognitive-psychology/self-regulation
  
  # Methodology
  - empirical-research
  - assessment-frameworks
  - systematic-protocols
  - practical-application
  - evidence-based
  
  # Specific Frameworks
  - pencrisal-framework
  - mai-framework
  - epistemic-vigilance
  
  # Core Competencies
  - reasoning-skills
  - error-detection
  - transfer-learning
  - calibration-training
  - deployment-strategies
  
  # Status
  - evergreen
  - comprehensive
  - research-grounded

domain: cognitive-psychology
subdomains:
  - metacognition
  - critical-thinking
  - educational-psychology
  - self-regulated-learning

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-02-01
updated: 2026-02-01

# ═══════════════════════════════════════════════════════════════════════════
# ACADEMIC METADATA
# ═══════════════════════════════════════════════════════════════════════════
source-type: academic-synthesis
research-base: empirical-studies
evidence-quality: high
peer-validation: multiple-frameworks

key-frameworks:
  - name: PENCRISAL
    description: "Five-dimensional critical thinking assessment (Deductive Reasoning, Inductive Reasoning, Practical Reasoning, Decision-Making, Problem-Solving)"
    developers: "Rivas & Saiz (2012)"
    validation: "psychometric-validated"
  
  - name: MAI
    description: "Metacognitive Awareness Inventory - 8 subdimensions across Knowledge and Regulation of Cognition"
    developers: "Schraw & Dennison (1994)"
    validation: "widely-validated"
  
  - name: EEVF
    description: "Extended Epistemic Vigilance Framework - 3-dimensional evaluation (Source, Claim, Receiver)"
    developers: "Sperber et al. (2010), Bielik & Krüger (2024)"
    validation: "empirically-supported"
  
  - name: Halpern Transfer Model
    description: "Four-component framework for critical thinking transfer across domains"
    developers: "Halpern (1998)"
    validation: "empirically-validated"

key-researchers:
  - Diane Halpern
  - Gregory Schraw
  - Carlos Saiz
  - Dan Sperber
  - Hugo Mercier
  - Raymond Dennison

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
word-count: 6200
complexity-level: advanced-practitioner
target-audience: "Intermediate to Advanced learners in cognitive psychology, educators, professionals seeking systematic reasoning improvement"
depth-level: comprehensive
treatment-type: practical-deployment-focused

practical-components:
  - operational-templates
  - decision-protocols
  - calibration-exercises
  - debugging-workflows
  - self-assessment-tools
  - monitoring-checklists

# ═══════════════════════════════════════════════════════════════════════════
# CORE CONCEPTS
# ═══════════════════════════════════════════════════════════════════════════
core-concepts:
  - Metacognitive Self-Regulation as Cognitive Control System
  - PENCRISAL Five-Dimensional Framework
  - Transfer Problem and Domain-Specificity
  - Recognition Patterns for Deployment Triggers
  - Knowledge of Cognition (Declarative, Procedural, Conditional)
  - Regulation of Cognition (Planning, Monitoring, Evaluation, Information Management, Debugging)
  - Epistemic Vigilance Three-Dimensional Model
  - Confidence Calibration Training
  - Structural Encoding for Transfer
  - Systematic Error Debugging Protocols

key-distinctions:
  - "Domain-General vs Domain-Specific Critical Thinking"
  - "Monitoring vs Control in Metacognition"
  - "Knowledge of Cognition vs Regulation of Cognition"
  - "Immersion vs Infusion Instructional Approaches"
  - "System 1 vs System 2 Deployment Triggers"
  - "Overconfidence vs Underconfidence Calibration Errors"

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  - "[[introduction-to-critical-thinking]]"
  - "[[Metacognition Fundamentals]]"
  - "[[Basic Argument Analysis]]"
  - "[[Logical Reasoning Foundations]]"

related:
  - "[[metacognition]]"
  - "[[PENCRISAL Assessment Framework]]"
  - "[[Metacognitive-Awareness-Inventory]]"
  - "[[epistemic-vigilance]]"
  - "[[dual-process-theory]]"
  - "[[Cognitive Load Theory (CLT)]]"
  - "[[argument-analysis]]"
  - "[[Decision-Making-Under-Uncertainty]]"
  - "[[Cognitive Biases and Debiasing]]"
  - "[[scientific-reasoning]]"
  - "[[transfer-of-learning]]"
  - "[[self-regulated-learning]]"
  - "[[confirmation-bias]]"
  - "[[availability-heuristic]]"
  - "[[Anchoring-Bias]]"

broader:
  - "[[cognitive-psychology]]"
  - "[[educational-psychology]]"
  - "[[Applied Epistemology]]"
  - "[[Rationality Studies]]"

narrower:
  - "[[Deductive Reasoning Techniques]]"
  - "[[Inductive Reasoning Strategies]]"
  - "[[Practical Reasoning in Real-World Contexts]]"
  - "[[Metacognitive Monitoring Protocols]]"
  - "[[Calibration Training Methods]]"
  - "[[Debugging Strategies for Reasoning Errors]]"
  - "[[Structural Encoding Techniques]]"

see-also:
  - "[[Working Memory and Executive Function]]"
  - "[[expertise-development]]"
  - "[[reflective-judgment-model]]"
  - "[[intellectual-humility]]"
  - "[[Bayesian-Reasoning]]"
  - "[[Argument-Mapping]]"
  - "[[socratic-questioning]]"
  - "[[pre-mortem-analysis]]"
  - "[[red-team-thinking]]"
  - "[[cognitive-forcing-functions]]"

contrasts-with:
  - "[[Heuristic-Based Decision Making]]"
  - "[[Intuitive Judgment]]"
  - "[[Unconscious Competence]]"

applied-in:
  - "[[Professional Decision Making]]"
  - "[[Academic Research]]"
  - "[[strategic-planning]]"
  - "[[Problem Solving in Complex Domains]]"
  - "[[evidence-based-practice]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  - "[[foundational-logic]]"
  - "[[cognitive-development-theory]]"
  - "[[information-processing-models]]"

enables:
  - "[[Advanced Reasoning Techniques]]"
  - "[[Domain-Specific Critical Thinking]]"
  - "[[Debiasing-Interventions]]"
  - "[[Metacognitive Instruction Design]]"
  - "[[Epistemic Virtue Development]]"

expansion-topics:
  - topic: "[[Domain-Specific Critical Thinking Standards]]"
    description: "Field-specific criteria and recognition patterns for professional contexts"
    priority: high
  
  - topic: "[[Metacognitive Intervention Design]]"
    description: "Systematic protocols for targeting specific metacognitive deficiencies"
    priority: high
  
  - topic: "[[Cognitive Bias Mitigation Protocols]]"
    description: "Operational detection and correction algorithms for specific biases"
    priority: medium
  
  - topic: "[[Transfer-Enabling Pedagogical Frameworks]]"
    description: "Instructional design for building transferable competencies"
    priority: medium
  
  - topic: "[[Epistemic Humility and Intellectual Virtue]]"
    description: "Dispositional foundations supporting critical thinking deployment"
    priority: medium

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICAL APPLICATION
# ═══════════════════════════════════════════════════════════════════════════
use-cases:
  - Personal decision-making improvement
  - Professional reasoning enhancement
  - Educational instruction design
  - Research methodology
  - Strategic planning
  - Quality assurance protocols

deployment-contexts:
  - High-stakes decisions
  - Persuasive communication evaluation
  - Complex problem-solving
  - Evidence assessment
  - Strategic planning
  - Learning and skill development

tools-provided:
  - Pre-task planning protocol
  - Monitoring checkpoint template
  - Post-task reflection framework
  - Error debugging workflow
  - Calibration training exercise
  - MAI self-assessment guide
  - Recognition pattern checklist

# ═══════════════════════════════════════════════════════════════════════════
# QUALITY INDICATORS
# ═══════════════════════════════════════════════════════════════════════════
empirical-support:
  - PENCRISAL validation studies (Rivas & Saiz, 2012, 2015)
  - MAI psychometric validation (Schraw & Dennison, 1994)
  - Transfer research (Halpern, 1998; Tiruneh et al., 2017)
  - Epistemic vigilance studies (Sperber et al., 2010)
  - Metacognition-CT relationship studies (Magno, 2010; Ku & Ho, 2010)

validation-evidence:
  - Longitudinal persistence of training effects
  - Cross-cultural replication
  - Convergent validity with multiple instruments
  - Predictive validity for academic performance
  - Structural equation modeling support

limitations-noted:
  - Optimal balance of explicit vs implicit instruction remains debated
  - Domain specificity vs generality tension
  - Limited long-term naturalistic validation
  - Individual difference moderators not fully characterized

# ═══════════════════════════════════════════════════════════════════════════
# DOCUMENT STRUCTURE
# ═══════════════════════════════════════════════════════════════════════════
sections:
  - Abstract and Executive Overview
  - Architectural Foundation (Metacognitive Engine)
  - Deployment Challenge (Recognition Patterns)
  - Critical Thinking Skills (PENCRISAL Framework)
  - Transfer Problem
  - Metacognitive Deployment Protocols
  - Error Detection and Correction
  - Self-Assessment Frameworks
  - Bridging Transfer Gap
  - Synthesis and Integration
  - References and Resources

document-features:
  - callouts: 17
  - wiki-links: 27+
  - empirical-citations: 15+
  - operational-templates: 7
  - framework-integrations: 4
  - practical-examples: 12+

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: budding
importance: critical
foundational-for-future-learning: true

connection-strength:
  high:
    - Metacognition
    - Critical Thinking
    - Transfer of Learning
  medium:
    - Cognitive Biases
    - Decision Making
    - Self-Regulated Learning
  exploratory:
    - Expertise Development
    - Instructional Design
    - Epistemic Virtue

# ═══════════════════════════════════════════════════════════════════════════
# CUSTOM METADATA
# ═══════════════════════════════════════════════════════════════════════════
pencrisal-dimensions:
  - Deductive Reasoning
  - Inductive Reasoning
  - Practical Reasoning
  - Decision-Making
  - Problem-Solving

mai-dimensions:
  knowledge:
    - Declarative Knowledge
    - Procedural Knowledge
    - Conditional Knowledge
  regulation:
    - Planning
    - Information Management
    - Comprehension Monitoring
    - Debugging Strategies
    - Evaluation

eevf-dimensions:
  - Source Evaluation
  - Claim Evaluation
  - Receiver Self-Evaluation

assessment-instruments:
  - PENCRISAL (35 items, 0-70 scale)
  - MAI (52 items, two-factor structure)
  - Holistic Critical Thinking Scoring Rubric
  - Watson-Glaser Critical Thinking Test (referenced)
  - Cornell Critical Thinking Tests (referenced)

---
