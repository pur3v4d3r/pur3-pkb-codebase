---
title:
aliases:
  - Tag Taxonomy
  - Prompt Engineering Tag Taxonomy
tags:
  - year/2025
  - source/llm/claude/sonnet
  - prompt-engineering
  - pkm/automation
  - informational-architecture
id: "20251119004801"
created: 2025-11-19T00:48:01
week: "[[2025-W47]]"
month: "[[2025-11]]"
quarter: "[[2025-Q4]]"
year: "[[2025]]"
type: reference
link-up:
  - 
link-related:
  - "[[2025-11-19|Daily-Note]]"
  - "[[permeant-note_moc]]"
---

---
tags:
  - pkm/taxonomy
  - reference-guide
  - prompt-engineering/meta
  - ai/documentation
  - obsidian/configuration
aliases:
  - Prompt Engineering Tag System
  - PE Taxonomy
  - AI Prompting Tags
  - LLM Interaction Taxonomy
---

> [!the-purpose]
> **This note provides a complete, hierarchical Tag Taxonomy for the Prompt Engineering domain of your PKB.** It covers prompting techniques, LLM capabilities, prompt patterns, model architectures, evaluation methods, safety considerations, and the evolving craft of effective human-AI interaction. This taxonomy supports both theoretical understanding and practical experimentation.

> [!core-principle]
> **Design Philosophy:** This taxonomy treats prompt engineering as an **emerging discipline** at the intersection of cognitive science, linguistics, software engineering, and human-computer interaction. It balances **proven techniques** with **experimental methods**, enabling you to document both established patterns and your own discoveries as the field evolves.

---

## 📚 Taxonomy Overview

This taxonomy organizes the **Prompt Engineering** domain into a three-level hierarchical structure:

```
#domain/subdomain/concept
```

**Temporal note:** Prompt engineering evolves rapidly. This taxonomy includes mechanisms for tracking technique versions, model generations, and deprecated patterns.

---

## 🏗️ Complete Domain Tag Hierarchy

### 1️⃣ Core Domain: Prompt Engineering Fundamentals

```yaml
#prompt-engineering
  #prompt-engineering/theory
    #prompt-engineering/theory/foundations
    #prompt-engineering/theory/linguistics
    #prompt-engineering/theory/cognitive-basis
    #prompt-engineering/theory/information-theory
  
  #prompt-engineering/principles
    #prompt-engineering/principles/clarity
    #prompt-engineering/principles/specificity
    #prompt-engineering/principles/context
    #prompt-engineering/principles/constraints
    #prompt-engineering/principles/iteration
  
  #prompt-engineering/anatomy
    #prompt-engineering/anatomy/instruction
    #prompt-engineering/anatomy/context
    #prompt-engineering/anatomy/examples
    #prompt-engineering/anatomy/output-format
    #prompt-engineering/anatomy/constraints
  
  #prompt-engineering/evaluation
    #prompt-engineering/evaluation/testing
    #prompt-engineering/evaluation/metrics
    #prompt-engineering/evaluation/comparison
    #prompt-engineering/evaluation/iteration
  
  #prompt-engineering/optimization
    #prompt-engineering/optimization/refinement
    #prompt-engineering/optimization/compression
    #prompt-engineering/optimization/efficiency
    #prompt-engineering/optimization/cost
```

> [!definition]
> **#prompt-engineering** — The systematic practice of designing, testing, and refining prompts to elicit desired behaviors from large language models. Encompasses both the craft of effective communication with AI and the science of understanding model capabilities and limitations.

---

### 2️⃣ Core Domain: Prompting Techniques

```yaml
#prompting-technique
  #prompting-technique/zero-shot
    #prompting-technique/zero-shot/instruction
    #prompting-technique/zero-shot/task-specification
  
  #prompting-technique/few-shot
    #prompting-technique/few-shot/example-selection
    #prompting-technique/few-shot/example-ordering
    #prompting-technique/few-shot/diversity
  
  #prompting-technique/chain-of-thought
    #prompting-technique/chain-of-thought/basic
    #prompting-technique/chain-of-thought/zero-shot
    #prompting-technique/chain-of-thought/self-consistency
  
  #prompting-technique/reasoning
    #prompting-technique/reasoning/step-by-step
    #prompting-technique/reasoning/decomposition
    #prompting-technique/reasoning/tree-of-thoughts
    #prompting-technique/reasoning/graph-of-thoughts
  
  #prompting-technique/react
    #prompting-technique/react/reasoning-acting
    #prompting-technique/react/tool-use
    #prompting-technique/react/iteration
  
  #prompting-technique/reflection
    #prompting-technique/reflection/self-critique
    #prompting-technique/reflection/refinement
    #prompting-technique/reflection/verification
  
  #prompting-technique/meta-prompting
    #prompting-technique/meta-prompting/prompt-generation
    #prompting-technique/meta-prompting/self-improvement
    #prompting-technique/meta-prompting/optimization
```

> [!definition]
> **#prompting-technique** — Specific, named strategies and patterns for structuring prompts to achieve particular outcomes. These are reusable approaches that have demonstrated effectiveness across various tasks and models.

---

### 3️⃣ Core Domain: Prompt Patterns

```yaml
#prompt-pattern
  #prompt-pattern/persona
    #prompt-pattern/persona/role-assignment
    #prompt-pattern/persona/expertise
    #prompt-pattern/persona/style
  
  #prompt-pattern/template
    #prompt-pattern/template/fill-in-blank
    #prompt-pattern/template/structured
    #prompt-pattern/template/formulaic
  
  #prompt-pattern/context-control
    #prompt-pattern/context-control/framing
    #prompt-pattern/context-control/perspective
    #prompt-pattern/context-control/constraints
  
  #prompt-pattern/output-format
    #prompt-pattern/output-format/structured-data
    #prompt-pattern/output-format/markdown
    #prompt-pattern/output-format/code
    #prompt-pattern/output-format/creative
  
  #prompt-pattern/error-handling
    #prompt-pattern/error-handling/clarification
    #prompt-pattern/error-handling/fallback
    #prompt-pattern/error-handling/validation
  
  #prompt-pattern/multi-turn
    #prompt-pattern/multi-turn/conversation
    #prompt-pattern/multi-turn/state-management
    #prompt-pattern/multi-turn/context-threading
```

> [!definition]
> **#prompt-pattern** — Reusable structural templates and design patterns for constructing prompts. Patterns are more abstract than specific techniques and can be combined or nested to create complex prompting strategies.

---

### 4️⃣ Core Domain: LLM Capabilities & Limitations

```yaml
#llm-capability
  #llm-capability/reasoning
    #llm-capability/reasoning/logical
    #llm-capability/reasoning/mathematical
    #llm-capability/reasoning/causal
    #llm-capability/reasoning/analogical
  
  #llm-capability/knowledge
    #llm-capability/knowledge/factual
    #llm-capability/knowledge/procedural
    #llm-capability/knowledge/domain-specific
    #llm-capability/knowledge/cutoff-date
  
  #llm-capability/generation
    #llm-capability/generation/creative
    #llm-capability/generation/technical
    #llm-capability/generation/structured
    #llm-capability/generation/code
  
  #llm-capability/understanding
    #llm-capability/understanding/comprehension
    #llm-capability/understanding/inference
    #llm-capability/understanding/context
    #llm-capability/understanding/ambiguity
  
  #llm-limitation
    #llm-limitation/hallucination
    #llm-limitation/reasoning-failures
    #llm-limitation/knowledge-gaps
    #llm-limitation/instruction-following
    #llm-limitation/consistency
    #llm-limitation/bias
```

> [!definition]
> **#llm-capability** — What language models can and cannot reliably do. Understanding capabilities and limitations is essential for effective prompt engineering, as it informs which techniques to apply and what expectations to set.

---

### 5️⃣ Core Domain: Model Architectures & Families

```yaml
#llm-architecture
  #llm-architecture/transformer
    #llm-architecture/transformer/attention
    #llm-architecture/transformer/decoder-only
    #llm-architecture/transformer/encoder-decoder
  
  #llm-architecture/model-family
    #llm-architecture/model-family/gpt
    #llm-architecture/model-family/claude
    #llm-architecture/model-family/gemini
    #llm-architecture/model-family/llama
    #llm-architecture/model-family/mistral
  
  #llm-architecture/model-size
    #llm-architecture/model-size/small
    #llm-architecture/model-size/medium
    #llm-architecture/model-size/large
    #llm-architecture/model-size/frontier
  
  #llm-architecture/training
    #llm-architecture/training/pretraining
    #llm-architecture/training/fine-tuning
    #llm-architecture/training/rlhf
    #llm-architecture/training/constitutional-ai
  
  #llm-architecture/context-window
    #llm-architecture/context-window/length
    #llm-architecture/context-window/management
    #llm-architecture/context-window/optimization
```

> [!definition]
> **#llm-architecture** — The technical foundations of language models, including architectural choices, model families, and training methodologies. Understanding architecture helps predict model behavior and informs prompting strategies.

---

### 6️⃣ Core Domain: Advanced Prompting Systems

```yaml
#advanced-prompting
  #advanced-prompting/agents
    #advanced-prompting/agents/autonomous
    #advanced-prompting/agents/tool-use
    #advanced-prompting/agents/multi-agent
    #advanced-prompting/agents/planning
  
  #advanced-prompting/rag
    #advanced-prompting/rag/retrieval
    #advanced-prompting/rag/context-injection
    #advanced-prompting/rag/hybrid-search
  
  #advanced-prompting/function-calling
    #advanced-prompting/function-calling/tool-definition
    #advanced-prompting/function-calling/parameter-extraction
    #advanced-prompting/function-calling/orchestration
  
  #advanced-prompting/multi-modal
    #advanced-prompting/multi-modal/vision
    #advanced-prompting/multi-modal/audio
    #advanced-prompting/multi-modal/code
  
  #advanced-prompting/programming
    #advanced-prompting/programming/code-generation
    #advanced-prompting/programming/debugging
    #advanced-prompting/programming/refactoring
    #advanced-prompting/programming/documentation
  
  #advanced-prompting/chain-systems
    #advanced-prompting/chain-systems/sequential
    #advanced-prompting/chain-systems/parallel
    #advanced-prompting/chain-systems/conditional
    #advanced-prompting/chain-systems/recursive
```

> [!definition]
> **#advanced-prompting** — Complex prompting architectures that combine multiple techniques, integrate external systems, or orchestrate multiple model calls to accomplish sophisticated tasks beyond single-prompt interactions.

---

### 7️⃣ Core Domain: Safety & Alignment

```yaml
#prompt-safety
  #prompt-safety/adversarial
    #prompt-safety/adversarial/jailbreaking
    #prompt-safety/adversarial/prompt-injection
    #prompt-safety/adversarial/defense
  
  #prompt-safety/alignment
    #prompt-safety/alignment/values
    #prompt-safety/alignment/constitutional
    #prompt-safety/alignment/harmlessness
    #prompt-safety/alignment/honesty
  
  #prompt-safety/bias
    #prompt-safety/bias/detection
    #prompt-safety/bias/mitigation
    #prompt-safety/bias/fairness
  
  #prompt-safety/content-policy
    #prompt-safety/content-policy/restrictions
    #prompt-safety/content-policy/boundaries
    #prompt-safety/content-policy/compliance
  
  #prompt-safety/information-security
    #prompt-safety/information-security/pii
    #prompt-safety/information-security/confidentiality
    #prompt-safety/information-security/data-handling
```

> [!definition]
> **#prompt-safety** — Practices and considerations for ensuring safe, aligned, and responsible use of language models through prompt design. Includes both defensive techniques and proactive alignment strategies.

---

### 8️⃣ Core Domain: Context Management

```yaml
#context-management
  #context-management/window
    #context-management/window/limits
    #context-management/window/optimization
    #context-management/window/chunking
  
  #context-management/memory
    #context-management/memory/short-term
    #context-management/memory/long-term
    #context-management/memory/retrieval
    #context-management/memory/summarization
  
  #context-management/compression
    #context-management/compression/summarization
    #context-management/compression/extraction
    #context-management/compression/prioritization
  
  #context-management/injection
    #context-management/injection/document
    #context-management/injection/knowledge-base
    #context-management/injection/dynamic
```

> [!definition]
> **#context-management** — Strategies for efficiently using limited context windows, maintaining conversation state, and injecting relevant information at the right time to maximize model performance.

---

### 9️⃣ Core Domain: Prompt Development Workflow

```yaml
#prompt-workflow
  #prompt-workflow/ideation
    #prompt-workflow/ideation/brainstorming
    #prompt-workflow/ideation/requirements
    #prompt-workflow/ideation/use-case
  
  #prompt-workflow/prototyping
    #prompt-workflow/prototyping/drafting
    #prompt-workflow/prototyping/iteration
    #prompt-workflow/prototyping/testing
  
  #prompt-workflow/evaluation
    #prompt-workflow/evaluation/manual
    #prompt-workflow/evaluation/automated
    #prompt-workflow/evaluation/ab-testing
    #prompt-workflow/evaluation/benchmark
  
  #prompt-workflow/version-control
    #prompt-workflow/version-control/tracking
    #prompt-workflow/version-control/comparison
    #prompt-workflow/version-control/rollback
  
  #prompt-workflow/deployment
    #prompt-workflow/deployment/production
    #prompt-workflow/deployment/monitoring
    #prompt-workflow/deployment/maintenance
```

> [!definition]
> **#prompt-workflow** — The end-to-end process of developing, testing, refining, and deploying prompts from initial concept through production use and ongoing maintenance.

---

### 🔟 Core Domain: Application Domains

```yaml
#prompt-application
  #prompt-application/writing
    #prompt-application/writing/content-creation
    #prompt-application/writing/editing
    #prompt-application/writing/style
  
  #prompt-application/analysis
    #prompt-application/analysis/data
    #prompt-application/analysis/text
    #prompt-application/analysis/research
  
  #prompt-application/education
    #prompt-application/education/tutoring
    #prompt-application/education/assessment
    #prompt-application/education/curriculum
  
  #prompt-application/coding
    #prompt-application/coding/generation
    #prompt-application/coding/review
    #prompt-application/coding/debugging
  
  #prompt-application/creative
    #prompt-application/creative/storytelling
    #prompt-application/creative/ideation
    #prompt-application/creative/design
  
  #prompt-application/productivity
    #prompt-application/productivity/summarization
    #prompt-application/productivity/organization
    #prompt-application/productivity/automation
```

> [!definition]
> **#prompt-application** — Specific use cases and domain applications where prompt engineering is applied. This helps organize prompts by their intended purpose and user context.

---

### Cross-Cutting Concepts

```yaml
#concept/emergence
#concept/instruction-following
#concept/in-context-learning
#concept/token-probability
#concept/temperature-control
#concept/top-p-sampling
#concept/prompt-chaining
#concept/task-decomposition
#concept/output-validation
#concept/error-correction
#concept/few-shot-exemplars
#concept/semantic-similarity
#concept/attention-mechanism
#concept/transformer-architecture
#concept/prompt-template
#concept/system-message
#concept/role-prompting
```

> [!helpful-tip]
> **Usage for PE Concepts:**
> Cross-cutting concepts appear across multiple techniques and contexts. Example:
> ```yaml
> tags:
>   - prompting-technique/chain-of-thought
>   - concept/task-decomposition
>   - concept/step-by-step
>   - llm-capability/reasoning/logical
> ```

---

## 🎯 Multi-Dimensional Tagging Framework

Combine **domain tags** with **functional tags**:

### Dimension 1: Note Type

```yaml
#type/technique         # Documented prompting technique
#type/pattern           # Reusable prompt pattern
#type/template          # Actual prompt template
#type/experiment        # Prompt experiment/test
#type/analysis          # Analysis of technique/results
#type/literature        # Notes from PE resources
#type/reference         # Quick reference guide
#type/case-study        # Real-world application example
#type/tutorial          # How-to guide
#type/comparison        # Comparative analysis
#type/prompt-library    # Collection of prompts
```

### Dimension 2: Development Status

```yaml
#status/experimental    # Testing/not validated
#status/proven          # Consistently effective
#status/deprecated      # Outdated/superseded
#status/under-revision  # Being updated
#status/production      # In active use
#status/archived        # Historical record
```

### Dimension 3: Technique Maturity

```yaml
#maturity/emerging      # New, not widely adopted
#maturity/established   # Proven, well-documented
#maturity/standard      # Industry best practice
#maturity/deprecated    # Replaced by better methods
```

### Dimension 4: Model Compatibility

```yaml
#model/claude          # Claude-specific
#model/gpt             # GPT models
#model/gemini          # Gemini models
#model/open-source     # Open-source models
#model/agnostic        # Works across models
```

### Dimension 5: Complexity Level

```yaml
#complexity/basic      # Fundamental techniques
#complexity/intermediate
#complexity/advanced
#complexity/expert     # Cutting-edge methods
```

### Dimension 6: Validation Status

```yaml
#validation/tested     # Personally tested
#validation/reported   # From reliable sources
#validation/theoretical # Not yet validated
#validation/failed     # Didn't work as expected
```

---

## 📋 Practical Tag Combinations: Examples

> [!use-cases-and-examples]
> **Real-World Prompt Engineering Tagging:**

### Example 1: Chain-of-Thought Technique Documentation

```yaml
---
tags:
  - type/technique
  - prompting-technique/chain-of-thought/basic
  - llm-capability/reasoning/logical
  - complexity/intermediate
  - maturity/established
  - model/agnostic
  - status/proven
  - validation/tested
aliases:
  - CoT Prompting
  - Step-by-Step Reasoning
  - Think Step by Step
source: "Wei et al. 2022"
effectiveness: high
---
```

**Rationale:** Well-established technique with proven effectiveness across models, validated through personal testing and literature.

---

### Example 2: Experimental Prompt Template

```yaml
---
tags:
  - type/template
  - prompt-pattern/persona/expertise
  - prompt-application/writing/content-creation
  - complexity/basic
  - status/experimental
  - validation/tested
  - model/claude
application: blog post generation
iterations: 3
best-temperature: 0.7
---
```

**Rationale:** An actual working prompt template, tested but still experimental, specific to Claude for content creation.

---

### Example 3: Literature Note on ReAct Framework

```yaml
---
tags:
  - type/literature
  - prompting-technique/react/reasoning-acting
  - advanced-prompting/agents/tool-use
  - complexity/advanced
  - maturity/established
  - model/agnostic
author: "Yao et al."
year: 2022
paper: "ReAct: Synergizing Reasoning and Acting in Language Models"
---
```

**Rationale:** Academic paper notes on an established advanced technique applicable across models.

---

### Example 4: Failed Experiment Log

```yaml
---
tags:
  - type/experiment
  - prompting-technique/tree-of-thoughts
  - prompt-application/analysis/research
  - complexity/advanced
  - status/archived
  - validation/failed
date: 2025-11-15
hypothesis: "Tree-of-Thoughts would improve research synthesis"
result: "Too complex; simple CoT performed better"
---
```

**Rationale:** Documentation of what didn't work—valuable for avoiding future dead ends.

---

### Example 5: Persona Pattern Reference

```yaml
---
tags:
  - type/pattern
  - prompt-pattern/persona/role-assignment
  - prompt-engineering/principles/context
  - complexity/basic
  - maturity/standard
  - model/agnostic
  - status/proven
  - validation/tested
aliases:
  - Role Assignment
  - Expert Persona
  - "Act As" Pattern
---
```

**Rationale:** Fundamental, widely-used pattern that works across all models and contexts.

---

### Example 6: Multi-Modal Vision Prompting Guide

```yaml
---
tags:
  - type/tutorial
  - advanced-prompting/multi-modal/vision
  - prompt-application/creative/design
  - complexity/intermediate
  - model/claude
  - model/gpt
  - status/production
  - validation/tested
aliases:
  - Image Analysis Prompting
  - Vision API Guide
last-updated: 2025-11-18
---
```

**Rationale:** Practical guide for specific multi-modal capability, tested with multiple models.

---

### Example 7: Prompt Injection Defense Case Study

```yaml
---
tags:
  - type/case-study
  - prompt-safety/adversarial/prompt-injection
  - prompt-safety/adversarial/defense
  - complexity/advanced
  - maturity/emerging
  - validation/tested
incident-date: 2025-10-12
attack-vector: "User input containing hidden instructions"
mitigation: "Input sanitization + constitutional constraints"
---
```

**Rationale:** Real security incident documentation with defensive techniques employed.

---

### Example 8: Prompt Library for Code Generation

```yaml
---
tags:
  - type/prompt-library
  - prompt-application/coding/generation
  - advanced-prompting/programming/code-generation
  - complexity/intermediate
  - model/claude
  - status/production
languages: [Python, JavaScript, TypeScript]
prompt-count: 15
---
```

**Rationale:** Collection of working prompts for specific programming tasks.

---

### Example 9: Comparative Analysis of CoT Variants

```yaml
---
tags:
  - type/comparison
  - prompting-technique/chain-of-thought
  - prompt-engineering/evaluation/comparison
  - complexity/advanced
  - validation/tested
variants:
  - Basic CoT
  - Zero-shot CoT
  - Self-Consistency CoT
  - Least-to-Most
metrics: [accuracy, coherence, cost]
---
```

**Rationale:** Systematic comparison of related techniques with quantitative evaluation.

---

### Example 10: Constitutional AI System Prompt

```yaml
---
tags:
  - type/template
  - prompt-safety/alignment/constitutional
  - prompt-pattern/context-control/constraints
  - llm-architecture/training/constitutional-ai
  - complexity/advanced
  - model/claude
  - status/production
  - validation/tested
purpose: "Ensure helpful, harmless, honest outputs"
principles: 12
---
```

**Rationale:** Production system prompt implementing constitutional AI principles for Claude.

---

## 🔍 Essential Dataview Queries for This Domain

> [!what-this-does]
> **Transform your prompt engineering knowledge into actionable views.**

### Query 1: Proven Techniques by Complexity

```
TABLE complexity, model as "Model Compatibility", validation
FROM #type/technique
WHERE status = "proven"
SORT complexity ASC, file.name ASC
```

**Use-case:** Find established techniques appropriate for your skill level.

---

### Query 2: Experimental Prompts Needing Validation

```
TABLE tags as "Categories", file.ctime as "Created"
FROM #status/experimental
WHERE validation = "theoretical" OR !validation
SORT file.ctime DESC
```

**Use-case:** Track which experimental prompts need testing.

---

### Query 3: Model-Specific Techniques

```
LIST
FROM #model/claude
WHERE type = "technique" OR type = "template"
SORT complexity, file.name
```

**Use-case:** Find Claude-specific prompting approaches.

---

### Query 4: Failed Experiments for Learning

```
TABLE hypothesis, result, date
FROM #type/experiment
WHERE validation = "failed"
SORT date DESC
```

**Use-case:** Learn from what didn't work to avoid repeating mistakes.

---

### Query 5: Production-Ready Templates by Application

```
TABLE complexity, model, effectiveness
FROM #type/template
WHERE status = "production"
GROUP BY split(file.tags[2], "/")[2]
SORT file.name
```

**Use-case:** Quick access to battle-tested prompts for specific use cases.

---

### Query 6: Technique Evolution Tracker

```
TABLE maturity, status, file.mtime as "Last Updated"
FROM #type/technique
SORT maturity DESC, file.mtime DESC
```

**Use-case:** Monitor which techniques are emerging vs. deprecated.

---

### Query 7: Safety & Alignment Resources

```
LIST
FROM #prompt-safety
WHERE type = "technique" OR type = "pattern" OR type = "case-study"
SORT file.name
```

**Use-case:** Centralized access to safety-related prompting knowledge.

---

### Query 8: Prompt Library Inventory

```
let libraries = dv.pages('#type/prompt-library')
let totalPrompts = 0
let byApplication = {}

for (let lib of libraries) {
    let count = lib["prompt-count"] || 0
    totalPrompts += count
    let app = lib.application || "general"
    byApplication[app] = (byApplication[app] || 0) + count
}

dv.header(3, `Total Prompts in Libraries: ${totalPrompts}`)
dv.table(["Application", "Prompt Count"], 
    Object.entries(byApplication).sort((a,b) => b[1] - a[1])
)
```

**Use-case:** Overview of your prompt collection size and coverage.

---

### Query 9: Technique Effectiveness Analysis

```
TABLE effectiveness, validation, iterations
FROM #type/technique OR #type/template
WHERE effectiveness
SORT effectiveness DESC
```

**Use-case:** Identify your most effective prompting approaches.

---

### Query 10: Recent Prompt Engineering Activity

```
TABLE type, tags as "Focus", validation
FROM #prompt-engineering OR #prompting-technique OR #advanced-prompting
SORT file.mtime DESC
LIMIT 20
```

**Use-case:** Track your recent exploration and experimentation.

---

## 🗺️ Domain MOC Template

> [!how-to-use-this]
> **Create your Prompt Engineering knowledge hub:**

```markdown
---
tags:
  - type/moc
  - prompt-engineering
  - ai/llm
aliases:
  - PE Hub
  - Prompt Engineering Map
  - LLM Prompting System
---

# 🎯 Prompt Engineering MOC

> [!the-purpose]
> Central navigation hub for all prompt engineering knowledge: techniques, patterns, templates, experiments, safety considerations, and the evolving craft of effective LLM interaction.

---

## 📚 Core Techniques & Frameworks

### Fundamental Techniques
- [[Zero-Shot Prompting]]
- [[Few-Shot Learning]]
- [[Chain-of-Thought Prompting]]
- [[Role-Based Prompting]]

### Advanced Techniques
```dataview
TABLE complexity, maturity, status
FROM #prompting-technique
WHERE complexity = "advanced" OR complexity = "expert"
SORT maturity DESC, file.name
```

### Reasoning & Agent Systems
- [[ReAct Framework]]
- [[Tree of Thoughts]]
- [[Autonomous Agents]]
- [[Tool-Using Agents]]

---

## 🎨 Prompt Patterns Library

### By Pattern Type
```
LIST
FROM #prompt-pattern
WHERE type = "pattern"
GROUP BY split(file.tags[0], "/")[2]
SORT file.name
```

### Structural Patterns
- [[Persona Pattern]]
- [[Template Pattern]]
- [[Output Format Control]]
- [[Context Framing]]

---

## 📝 Production Prompt Templates

### By Application Domain
```
TABLE model as "Model", complexity, effectiveness
FROM #type/template
WHERE status = "production"
GROUP BY split(file.tags[2], "/")[2]
```

### Featured Templates
- [[Content Creation System Prompt]]
- [[Code Generation Template]]
- [[Research Assistant Prompt]]
- [[Analysis Framework Template]]

---

## 🧪 Experiments & Testing

### Active Experiments
```
TABLE hypothesis, date as "Started", iterations
FROM #type/experiment
WHERE status = "experimental"
SORT date DESC
```

### Validated Findings
```
TABLE result, validation, effectiveness
FROM #type/experiment
WHERE validation = "tested" AND effectiveness
SORT effectiveness DESC
```

### Failed Experiments (Lessons)
```
TABLE hypothesis, result
FROM #type/experiment
WHERE validation = "failed"
SORT date DESC
LIMIT 5
```

---

## 🤖 Model Knowledge Base

### Model Families & Capabilities
- [[Claude Model Family]]
- [[GPT Model Evolution]]
- [[Open Source LLMs]]
- [[Multi-Modal Models]]

### Capability Documentation
```
LIST
FROM #llm-capability
WHERE type = "reference" OR type = "analysis"
SORT file.name
```

### Known Limitations
```
LIST
FROM #llm-limitation
SORT file.name
```

---

## 🛡️ Safety & Alignment

### Security Considerations
- [[Prompt Injection Defenses]]
- [[Jailbreak Prevention]]
- [[Input Sanitization]]
- [[Output Validation]]

### Alignment Practices
```
LIST
FROM #prompt-safety/alignment
SORT file.name
```

---

## 🔧 Development Workflow

### Workflow Stages
- [[Prompt Ideation Process]]
- [[Rapid Prototyping Method]]
- [[Evaluation Framework]]
- [[Version Control for Prompts]]

### Evaluation Methods
```
TABLE validation, complexity
FROM #prompt-workflow/evaluation
SORT file.name
```

---

## 📖 Literature & Research

### Key Papers
```
TABLE author, year, file.ctime as "Added"
FROM #type/literature AND #prompt-engineering
WHERE author
SORT year DESC
```

### Case Studies
```
TABLE application, result
FROM #type/case-study
SORT file.ctime DESC
```

---

## 📊 Prompt Engineering Analytics

### Technique Distribution
```
let pages = dv.pages('#prompting-technique')
let maturityCount = {}
for (let page of pages) {
    let mat = page.maturity || "unclassified"
    maturityCount[mat] = (maturityCount[mat] || 0) + 1
}
dv.table(["Maturity Level", "Technique Count"], 
    Object.entries(maturityCount).sort((a,b) => b[1] - a[1])
)
```

### Model Coverage
```
let pages = dv.pages('#type/technique OR #type/template')
let modelCount = {}
for (let page of pages) {
    let models = page.file.tags.filter(t => t.startsWith('#model/'))
    for (let model of models) {
        let name = model.split('/')[1]
        modelCount[name] = (modelCount[name] || 0) + 1
    }
}
dv.table(["Model", "Resources"], 
    Object.entries(modelCount).sort((a,b) => b[1] - a[1])
)
```

### Validation Status
```
let pages = dv.pages('#type/technique OR #type/template OR #type/experiment')
let validationCount = {}
for (let page of pages) {
    let val = page.validation || "unvalidated"
    validationCount[val] = (validationCount[val] || 0) + 1
}
dv.table(["Validation Status", "Count"], 
    Object.entries(validationCount).sort((a,b) => b[1] - a[1])
)
```

---

## 🎯 Current Focus Areas

> [!project-link]
> **Active Prompt Engineering Projects:**
> - Optimizing research synthesis workflows
> - Testing multi-agent systems for coding
> - Building constitutional safety framework
> - Exploring vision + text multi-modal patterns

---

## 🔗 Related MOCs
- [[Cognitive Abilities MOC]]
- [[PKM System Hub]]
- [[AI & Machine Learning MOC]]
- [[Programming & Software Engineering MOC]]

---

## 📚 Learning Paths

### Beginner Path
1. [[Prompt Engineering Fundamentals]]
2. [[Basic Prompt Anatomy]]
3. [[Zero-Shot vs Few-Shot]]
4. [[Simple Persona Patterns]]
5. [[Testing Your First Prompts]]

### Intermediate Path
1. [[Chain-of-Thought Deep Dive]]
2. [[Prompt Pattern Catalog]]
3. [[Context Management Strategies]]
4. [[Systematic Evaluation]]
5. [[Building Prompt Libraries]]

### Advanced Path
1. [[Agent Architectures]]
2. [[RAG Systems Design]]
3. [[Adversarial Robustness]]
4. [[Multi-Model Orchestration]]
5. [[Production Deployment]]

---

## 🔄 Maintenance Schedule

- **Weekly:** Review new experiments, update effectiveness ratings
- **Monthly:** Audit deprecated techniques, consolidate learnings
- **Quarterly:** Systematic comparison of technique evolution
- **Yearly:** Major taxonomy revision for field evolution
```

---

## 🎓 Tag Usage Guidelines

> [!core-principle]
> **Consistency Protocol for Prompt Engineering:**

### Rule 1: Distinguish Technique from Implementation
- **Technique** = The abstract method (e.g., Chain-of-Thought)
- **Template** = The actual prompt text implementing that technique
- **Experiment** = Testing of technique in specific context

**Example:**
```yaml
# A note explaining CoT theory:
tags:
  - type/technique
  - prompting-technique/chain-of-thought

# An actual CoT prompt you use:
tags:
  - type/template
  - prompting-technique/chain-of-thought
  - prompt-application/analysis/research
  - status/production
```

### Rule 2: Model Compatibility Tagging
Always tag with model compatibility:
- `#model/agnostic` = Works across all models
- `#model/claude`, `#model/gpt`, etc. = Model-specific
- Can have multiple model tags if tested across models

### Rule 3: Validation is Mandatory
Every technique or template should have validation status:
- `#validation/tested` = You've personally validated it
- `#validation/reported` = From reliable sources but not personally tested
- `#validation/theoretical` = Untested concept
- `#validation/failed` = Tested and didn't work as expected

### Rule 4: Status vs. Maturity
- **Status** = Where this specific note is in your workflow
  - `#status/experimental`, `#status/production`, `#status/archived`
- **Maturity** = Where this technique is in the field
  - `#maturity/emerging`, `#maturity/established`, `#maturity/deprecated`

### Rule 5: Track Failed Experiments
Failed experiments are valuable knowledge:
- Always use `#validation/failed` tag
- Document what didn't work in the note
- Include hypothesis and actual result
- These help you avoid dead ends

### Rule 6: Application Context Matters
When creating templates, always tag the application:
```yaml
tags:
  - type/template
  - prompt-application/writing/content-creation
  - prompt-pattern/persona/expertise
```

This enables finding the right prompt for the right job.

### Rule 7: Complexity Calibration
Be honest about complexity ratings:
- `#complexity/basic` = Anyone can use this
- `#complexity/intermediate` = Requires PE fundamentals
- `#complexity/advanced` = Requires deep understanding
- `#complexity/expert` = Cutting-edge/experimental

---

## 🔄 Tag Maintenance Schedule

> [!methodology-and-sources]
> **Quarterly Maintenance for Prompt Engineering:**

### Every 3 Months: Technique Evolution Audit

**Step 1: Deprecation Check**
The PE field evolves rapidly. Check for deprecated techniques:
```
TABLE maturity, status, file.mtime as "Last Updated"
FROM #type/technique
WHERE file.mtime < date(today) - dur(180 days)
SORT file.mtime ASC
```

**Step 2: Model Update Impact**
When new model versions release, review affected prompts:
```
LIST
FROM #model/claude OR #model/gpt
WHERE status = "production"
```
Test each against new model versions and update effectiveness ratings.

**Step 3: Consolidate Learnings**
Review experiments and extract patterns:
```
TABLE validation, result
FROM #type/experiment
WHERE validation = "tested"
SORT date DESC
```
Promote successful experiments to proven techniques.

**Step 4: Safety Review**
Audit safety-related prompts for new attack vectors:
```
LIST
FROM #prompt-safety
SORT file.mtime DESC
```

---

## 📖 Semantic Definitions: Deep Dive

> [!definition]
> **Detailed Tag Meanings:**

### `#prompting-technique/chain-of-thought`
**Definition:** A prompting strategy that encourages the model to show its reasoning process step-by-step before arriving at a final answer, improving accuracy on complex tasks.

**Use for:**
- Notes about CoT methodology and theory
- Variants (zero-shot CoT, self-consistency CoT)
- Research papers on CoT effectiveness
- Techniques for implementing CoT

**Do NOT use for:**
- A specific prompt that uses CoT (tag that as ``#type/template`)`
- General reasoning (use ``#llm-capability/reasoning`)`
- Just because the output shows steps (the technique is about *prompting* for steps)

---

### `#advanced-prompting/agents/autonomous`
**Definition:** Systems where the LLM makes decisions about what actions to take, what tools to use, and how to decompose tasks, with minimal human intervention.

**Use for:**
- Agent architecture documentation
- Autonomous decision-making patterns
- Tool orchestration by agents
- Planning and execution systems

**Do NOT use for:**
- Simple function calling (use `#advanced-prompting/function-calling`)
- Chatbots (unless truly autonomous)
- Multi-turn conversations (unless agent-driven)

---

### `#prompt-safety/adversarial/prompt-injection`
**Definition:** Attack vectors where malicious input attempts to override system instructions or extract sensitive information through carefully crafted prompts.

**Use for:**
- Documentation of injection attacks
- Defense mechanisms and mitigations
- Case studies of successful/prevented attacks
- Testing frameworks for robustness

**Do NOT use for:**
- General safety (use `#prompt-safety`)
- Jailbreaking (use `#prompt-safety/adversarial/jailbreaking`)
- Content policy violations (use `#prompt-safety/content-policy`)

---

### `#llm-capability/reasoning/mathematical`
**Definition:** The model's ability to perform mathematical reasoning, including arithmetic, algebra, geometry, and formal proofs.

**Use for:**
- Analysis of mathematical reasoning capabilities
- Known limitations in math tasks
- Techniques for improving math performance
- Benchmarks and evaluations

**Do NOT use for:**
- Prompts that happen to involve math (tag by prompting technique instead)
- Mathematical content in your knowledge base (use domain-specific tags)

---

### `#prompt-pattern/persona/role-assignment`
**Definition:** A structural pattern where the prompt assigns a specific role, expertise, or perspective to the model (e.g., "You are an expert physicist").

**Use for:**
- Documentation of persona patterns
- Analysis of role-assignment effectiveness
- Guidelines for choosing personas
- Examples of effective role definitions

**Do NOT use for:**
- Every prompt that uses a persona (only tag notes *about* the pattern)
- Personality traits (this is about expertise/role, not personality)

---

## ⚠️ Common Tagging Mistakes

> [!warning]
> **Anti-Patterns in PE Tagging:**

### ❌ Mistake 1: Confusing Technique Documentation with Template

**Bad:**
```yaml
# A note that IS a working prompt
tags:
  - type/technique
  - prompting-technique/chain-of-thought
```

**Good:**
```yaml
# A note that IS a working prompt
tags:
  - type/template
  - prompting-technique/chain-of-thought
  - prompt-application/coding/debugging
  - status/production
```

**Why:** Techniques are abstract methods; templates are concrete implementations.

---

### ❌ Mistake 2: Not Tracking Failed Experiments

**Bad:**
```yaml
# Experiment didn't work, so I deleted it
```

**Good:**
```yaml
# Documented failed experiment
tags:
  - type/experiment
  - prompting-technique/tree-of-thoughts
  - validation/failed
  - status/archived
hypothesis: "ToT would improve code refactoring"
result: "Too slow; simple CoT better for this task"
lesson: "Complexity doesn't always help"
```

**Why:** Failed experiments teach you what NOT to do—extremely valuable knowledge.

---

### ❌ Mistake 3: Forgetting Model Compatibility

**Bad:**
```yaml
tags:
  - type/template
  - prompt-application/writing
  - status/production
```

**Good:**
```yaml
tags:
  - type/template
  - prompt-application/writing
  - status/production
  - model/claude
  - model/gpt
```

**Why:** Knowing which models a technique works with is critical for reusability.

---

### ❌ Mistake 4: Over-Tagging Applications

**Bad:**
```yaml
# A general CoT tutorial
tags:
  - prompt-application/writing
  - prompt-application/coding
  - prompt-application/analysis
  - prompt-application/creative
```

**Good:**
```yaml
# A general CoT tutorial
tags:
  - type/tutorial
  - prompting-technique/chain-of-thought
  - complexity/intermediate
  - model/agnostic
```

**Why:** Only tag specific applications when the content is actually application-specific.

---

### ❌ Mistake 5: Ignoring Validation Status

**Bad:**
```yaml
# Saw this cool technique on Twitter
tags:
  - type/technique
  - prompting-technique/meta-prompting
  - status/proven
```

**Good:**
```yaml
# Saw this cool technique on Twitter
tags:
  - type/technique
  - prompting-technique/meta-prompting
  - validation/reported
  - status/experimental
source: "@AIresearcher on Twitter"
needs-testing: true
```

**Why:** Distinguish between what you've validated and what you've only read about.

---

## 🎯 Quick Reference: PE Tag Decision Tree

> [!quick-reference]
> **Tagging workflow for prompt engineering:**

```
┌─────────────────────────────────────┐
│ NEW PROMPT ENGINEERING NOTE         │
└──────────────┬──────────────────────┘
               │
               ▼
        ┌──────────────┐
        │ What IS this?│
        └──────┬───────┘
               │
   ┌───────────┼───────────┬──────────────┐
   ▼           ▼           ▼              ▼
[Abstract   [Actual    [Experiment]  [Analysis/
 technique]  prompt]                  Research]
   │           │           │              │
   ▼           ▼           ▼              ▼
type/       type/       type/          type/
technique   template    experiment     literature
   │           │           │          OR case-study
   │           │           │              │
   └───────────┴───────────┴──────────────┘
                    │
                    ▼
        ┌─────────────────────────┐
        │ Which prompting method? │
        │ (#prompting-technique/) │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Model compatibility?    │
        │ (#model/*)              │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Validation status?      │
        │ (#validation/*)         │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Development status?     │
        │ (#status/*)             │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Complexity level?       │
        │ (#complexity/*)         │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ OPTIONAL: Application?  │
        │ (#prompt-application/*) │
        └─────────────────────────┘
```

---

## 🚀 Implementation Checklist

> [!tasks]
> **Deploy your PE taxonomy:**

### Phase 1: Foundation
- [ ] **Create PE MOC:** Use template to create `[[Prompt Engineering Hub]]`
- [ ] **Save Taxonomy:** Store as `[[Tag Taxonomy - Prompt Engineering]]`
- [ ] **Link from Master:** Add to main PKB index
- [ ] **Create Sub-MOCs:** Consider separate hubs for Techniques, Safety, Applications

### Phase 2: Existing Content Audit
- [ ] **Find Untagged Prompts:** Search for prompt-related notes lacking proper tags
- [ ] **Classify Techniques:** Separate technique docs from actual templates
- [ ] **Add Validation Status:** Review all techniques/templates and add validation tags
- [ ] **Model Compatibility:** Tag all resources with appropriate model compatibility

### Phase 3: Template System
- [ ] **Technique Documentation Template:** Pre-tagged for documenting new techniques
- [ ] **Prompt Template Template:** Structure for saving actual prompts with metadata
- [ ] **Experiment Log Template:** Structured format for testing prompts
- [ ] **Case Study Template:** For documenting real-world applications

### Phase 4: Testing Framework
- [ ] **Define Evaluation Metrics:** How you'll measure prompt effectiveness
- [ ] **Create Test Harness:** System for systematically testing prompts
- [ ] **Build Comparison Framework:** Template for A/B testing techniques
- [ ] **Set Up Version Control:** Track prompt evolution over time

### Phase 5: Knowledge Capture
- [ ] **Prompt Library Setup:** Organized collection of production prompts
- [ ] **Failed Experiments Archive:** Don't lose valuable negative results
- [ ] **Literature Database:** Track papers and resources on PE
- [ ] **Safety Checklist:** Reference for adversarial robustness

---

## 🔗 Integration with Broader PKB

> [!connections-and-links]
> **Connecting PE to your knowledge ecosystem:**

### Upstream (Foundation)
- [[Master Tag Taxonomy]]
- [[PKB Architecture]]
- [[Cognitive Abilities MOC]] — Understanding how prompting relates to cognition

### Parallel Domains
- [[Programming & Software Engineering MOC]] — Code generation, debugging
- [[Writing & Communication MOC]] — Content creation applications
- [[Research Methods MOC]] — Using LLMs for research workflows

### Downstream (Applications)
- [[Content Creation Workflow]] — Uses production prompt templates
- [[Code Review System]] — Leverages coding prompts
- [[Research Synthesis Pipeline]] — Integrates analysis prompts
- [[Daily Workflow]] — Quick-access prompt library

### Meta-Layer
This taxonomy enables:
- Systematic prompt development
- Knowledge accumulation about effective prompting
- Experimentation tracking
- Continuous improvement of PE skills

---

# 🔗 Related Topics for PKB Expansion

1. **[[LLM Architecture Deep Dive]]**
   - *Connection*: Understanding model internals informs effective prompting strategies
   - *Depth Potential*: Transformer architecture, attention mechanisms, training objectives
   - *Knowledge Graph Role*: Bridges theory with practical prompt engineering

2. **[[Evaluation Frameworks for LLM Outputs]]**
   - *Connection*: Systematic evaluation is essential for prompt optimization
   - *Depth Potential*: Metrics, benchmarks, human evaluation, automated testing
   - *Knowledge Graph Role*: Enables data-driven prompt improvement

3. **[[Multi-Agent Systems & Orchestration]]**
   - *Connection*: Advanced application of prompting in agent architectures
   - *Depth Potential*: Agent communication, planning, tool use, multi-agent collaboration
   - *Knowledge Graph Role*: Represents frontier of practical PE applications

4. **[[AI Safety & Alignment in Practice]]**
   - *Connection*: Safety considerations are fundamental to responsible prompting
   - *Depth Potential*: Red-teaming, robustness testing, alignment techniques
   - *Knowledge Graph Role*: Ensures ethical and safe deployment of prompt-based systems

5. **[[Retrieval-Augmented Generation (RAG) Systems]]**
   - *Connection*: Combines prompting with external knowledge retrieval
   - *Depth Potential*: Vector databases, hybrid search, context injection strategies
   - *Knowledge Graph Role*: Key technique for overcoming context window limitations

6. **[[Prompt Engineering for Specific Domains]]**
   - *Connection*: Domain-specific considerations and best practices
   - *Depth Potential*: Medical, legal, scientific, creative writing applications
   - *Knowledge Graph Role*: Builds specialized expertise on top of general techniques


```
<thinking>
The user wants a comprehensive tag taxonomy for Prompt Engineering, following the same system I used for Cognitive Abilities and PKM/Knowledge Work. This is a rapidly evolving domain that spans:

- Prompt engineering theory and techniques
- LLM capabilities and limitations
- Specific prompting strategies (Chain-of-Thought, ReAct, etc.)
- Prompt patterns and templates
- AI model families and their characteristics
- Evaluation and testing
- Safety and alignment
- Prompt optimization
- Multi-modal prompting
- Agent systems and workflows
- Tool use and function calling
- Context management
- Few-shot learning
- Instruction design
- System prompts vs user prompts
- Constitutional AI and values alignment
- Retrieval-augmented generation
- Prompt libraries and repositories

I need to create:
1. Complete hierarchical tag structure (3 levels)
2. Multi-dimensional tagging framework
3. Practical examples with real scenarios
4. Dataview queries specific to prompt engineering
5. MOC template
6. Usage guidelines
7. Semantic definitions
8. Common mistakes
9. Implementation checklist

This domain is particularly interesting because it's:
- Highly technical
- Rapidly evolving (new techniques emerge frequently)
- Spans theory and practice heavily
- Involves experimentation and iteration
- Has strong connections to cognitive science (how models "think")
- Includes both craft knowledge and systematic methods

Key considerations:
- Distinguish between prompt techniques vs model capabilities
- Separate prompt patterns from specific implementations
- Cover both single-turn and multi-turn interactions
- Include safety and alignment considerations
- Account for different modalities (text, vision, code, etc.)
- Handle versioning and evolution of techniques
- Support experimentation and testing workflows
</thinking>
```