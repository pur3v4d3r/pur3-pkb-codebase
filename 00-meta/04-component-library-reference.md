---
tags:
aliases:
  - Component Reference
  - Library Guide
  - Building Blocks
  - Prompt Components
status: evergreen
certainty: verified
priority: high
created: 2025-12-24
type: reference
project: prompt-engineering-templater-system
link-up: "[[00-meta/01-spes-master-operations-manual]]"
---

# 🧩 Component Library Reference

> [!abstract] Complete Guide to Prompt Building Blocks
> This reference documents the **component library architecture**, all component types, their structures, and how to create, use, and maintain reusable prompt pieces. Components are the **atomic building blocks** that assemble into complete prompts.

---

## 🏗️ PART I: LIBRARY ARCHITECTURE

### 1.1 The Component Philosophy

> [!principle-point] Atomic-First Design
> The SPES component library follows an **atomic-first design philosophy**: create the smallest useful, reusable pieces first, then compose them into larger structures. This maximizes reusability and testability.

**Design Principles:**

| Principle | Meaning | Benefit |
|-----------|---------|---------|
| **Single Responsibility** | One component = one job | Easy to test, debug, replace |
| **Self-Contained** | Component works independently | Can be used in any context |
| **Well-Documented** | Clear when/why to use | Enables discovery and selection |
| **Version-Tracked** | Changes recorded | Supports iteration without loss |
| **Performance-Measured** | Quality tracked over uses | Data-driven optimization |

### 1.2 Library Structure

```
02-component-library/
│
├── atomic/                    ← Indivisible building blocks
│   ├── personas/              ← "You are a..."
│   ├── instructions/          ← "Analyze...", "Generate..."
│   ├── constraints/           ← "Do not...", "Always..."
│   ├── output-formats/        ← Structured output templates
│   └── context-framers/       ← Background and situation setters
│
├── composite/                 ← Assembled multi-component units
│   ├── sequential-chains/     ← A → B → C patterns
│   ├── parallel-branches/     ← Simultaneous processing paths
│   └── recursive-loops/       ← Self-improving iterations
│
└── specialized/               ← Domain-optimized templates
    ├── educational-content/   ← Pedagogy-optimized
    ├── technical-analysis/    ← Rigor and precision
    ├── creative-writing/      ← Style and narrative
    └── pkb-operations/        ← Knowledge management specific
```

### 1.3 Atomic vs Composite

> [!definition] Atomic Component
> A **single-purpose, indivisible** prompt piece that performs exactly one function. Cannot be meaningfully broken down further.

> [!definition] Composite Component
> A **pre-assembled combination** of multiple atomic components designed to work together for a specific pattern or workflow.

**When to Create Atomic:**
- The component serves a single, clear purpose
- It could be useful across many different prompts
- Testing it in isolation makes sense
- It represents a fundamental prompt pattern

**When to Create Composite:**
- Multiple atomics consistently work together
- A common pattern emerges from usage data
- Assembly order or connections are non-obvious
- Users frequently combine the same components

---

## 📁 PART II: COMPONENT TYPES

### 2.1 Personas

> [!what-this-does] Persona Purpose
> Personas establish the **identity, expertise, and behavioral frame** for the LLM. They answer: "Who should the LLM be while completing this task?"

**Location:** `02-component-library/atomic/personas/`

**Core Elements:**

```markdown
## Persona Components Include:

### Identity Statement
"You are a [role] with [qualifications]..."

### Expertise Frame
"You have deep expertise in [domains]..."

### Behavioral Traits
"You approach problems by [methodology]..."

### Communication Style
"You communicate in a [tone] manner..."
```

**Example Persona Component:**

```markdown
---
type: component
component-type: persona
atomic-composite: atomic
domain: technical
id: 20251224150001
status: active
version: "1.0.0"
tags: ["year/2025", "prompt-engineering", "component-type/persona", "domain/technical"]
---

# Expert Code Reviewer Persona

> [!definition] Component Purpose
> Establishes LLM as a senior software engineer conducting thorough code reviews.

## Component Text

```prompt
You are a senior software engineer with 15+ years of experience conducting code reviews. You have:

- Deep expertise in software architecture, design patterns, and clean code principles
- Experience across multiple languages and paradigms (OOP, functional, systems)
- A track record of mentoring junior developers through constructive feedback
- Knowledge of security vulnerabilities and performance optimization

Your approach to code review:
- You examine code systematically, starting with architecture before details
- You explain the "why" behind suggestions, not just the "what"
- You acknowledge good patterns before suggesting improvements
- You prioritize issues by severity: critical → important → minor → stylistic
- You offer concrete code examples when suggesting changes
```

## When to Use
- Code review tasks
- Debugging assistance
- Architecture discussions
- Teaching programming concepts

## When NOT to Use
- Creative writing (too technical)
- General conversation (overly formal)
- Non-technical analysis

## Works Well With
- [[detailed-analysis-instruction]]
- [[constructive-feedback-constraint]]
- [[markdown-code-blocks-format]]

## Conflicts With
- [[casual-friend-persona]] - Contradictory tones
- [[brief-responses-constraint]] - This persona is thorough
```

**Persona Subcategories:**

| Subcategory | Focus | Example Use Cases |
|-------------|-------|-------------------|
| **Expert Analyst** | Domain expertise, rigor | Technical analysis, research |
| **Teacher/Tutor** | Explanation, pedagogy | Learning content, tutorials |
| **Creative Writer** | Style, narrative | Stories, marketing, content |
| **Advisor/Consultant** | Strategy, recommendations | Planning, decision support |
| **Conversational** | Friendly engagement | Chat, support, guidance |

---

### 2.2 Instructions

> [!what-this-does] Instruction Purpose
> Instructions are **task directives** that tell the LLM what action to perform. They answer: "What should the LLM do?"

**Location:** `02-component-library/atomic/instructions/`

**Core Elements:**

```markdown
## Instruction Components Include:

### Primary Directive
"Analyze...", "Generate...", "Compare...", "Explain..."

### Scope Definition
"Focus on [specific aspects]..."

### Process Guidance
"First..., then..., finally..."

### Success Criteria
"The output should demonstrate..."
```

**Example Instruction Component:**

```markdown
---
type: component
component-type: instruction
atomic-composite: atomic
domain: general
id: 20251224150002
status: active
version: "1.0.0"
tags: ["year/2025", "prompt-engineering", "component-type/instruction", "task/analysis"]
---

# Comparative Analysis Instruction

> [!definition] Component Purpose
> Directs LLM to systematically compare two or more items across defined criteria.

## Component Text

```prompt
Conduct a systematic comparative analysis of the provided items:

1. IDENTIFY the key dimensions relevant for comparison
2. ANALYZE each item against these dimensions individually
3. COMPARE items directly, highlighting:
   - Similarities and shared strengths
   - Key differences and trade-offs
   - Situational advantages for each option
4. SYNTHESIZE findings into a clear recommendation framework:
   - "Choose A when [conditions]"
   - "Choose B when [conditions]"
5. ACKNOWLEDGE limitations of the comparison and areas needing more information
```

## When to Use
- Product/tool comparisons
- Approach/methodology evaluation
- Decision support tasks
- Trade-off analysis

## Parameters
- **Items to compare**: User provides
- **Comparison criteria**: Can be auto-generated or user-specified
- **Depth**: Adjustable via constraint component

## Works Well With
- [[expert-analyst-persona]]
- [[structured-table-format]]
- [[evidence-based-constraint]]
```

**Instruction Subcategories:**

| Subcategory | Action Type | Examples |
|-------------|-------------|----------|
| **Analysis** | Examine, evaluate | "Analyze...", "Assess...", "Evaluate..." |
| **Generation** | Create, produce | "Generate...", "Create...", "Write..." |
| **Transformation** | Convert, modify | "Rewrite...", "Translate...", "Summarize..." |
| **Extraction** | Pull out, identify | "Extract...", "Identify...", "Find..." |
| **Explanation** | Clarify, teach | "Explain...", "Describe...", "Illustrate..." |
| **Organization** | Structure, arrange | "Organize...", "Categorize...", "Outline..." |

---

### 2.3 Constraints

> [!what-this-does] Constraint Purpose
> Constraints establish **boundaries, restrictions, and quality requirements** for LLM output. They answer: "What should the LLM NOT do or ALWAYS do?"

**Location:** `02-component-library/atomic/constraints/`

**Core Elements:**

```markdown
## Constraint Components Include:

### Prohibitions
"Do not [action]...", "Never [behavior]..."

### Requirements
"Always [action]...", "Must include..."

### Boundaries
"Limit to [scope]...", "Focus only on..."

### Quality Standards
"Ensure [quality criteria]..."
```

**Example Constraint Component:**

```markdown
---
type: component
component-type: constraint
atomic-composite: atomic
domain: general
id: 20251224150003
status: active
version: "1.0.0"
tags: ["year/2025", "prompt-engineering", "component-type/constraint", "quality/accuracy"]
---

# Evidence-Based Claims Constraint

> [!definition] Component Purpose
> Requires LLM to support claims with evidence and acknowledge uncertainty.

## Component Text

```prompt
Adhere to evidence-based communication standards:

REQUIREMENTS:
- Support factual claims with specific evidence, examples, or logical reasoning
- Clearly distinguish between established facts, likely interpretations, and speculation
- Use epistemic markers appropriately:
  - "Research indicates..." for well-supported claims
  - "It's likely that..." for reasonable inferences
  - "One possibility is..." for speculation
- Cite sources when referencing specific studies, statistics, or authoritative statements

PROHIBITIONS:
- Do not present speculation as fact
- Do not use authoritative language for uncertain claims
- Do not fabricate statistics, studies, or quotes
- Do not ignore contradicting evidence

UNCERTAINTY ACKNOWLEDGMENT:
- Explicitly state when you lack sufficient information
- Offer to clarify what additional information would help
- Present multiple interpretations when evidence is ambiguous
```

## When to Use
- Research synthesis
- Factual analysis
- Educational content
- Decision support

## When NOT to Use
- Creative fiction (speculation is the point)
- Brainstorming (premature constraints limit ideation)
- Hypothetical scenarios

## Works Well With
- [[expert-analyst-persona]]
- [[comparative-analysis-instruction]]
- [[structured-argument-format]]

## Conflicts With
- [[creative-speculation-instruction]]
- [[stream-of-consciousness-format]]
```

**Constraint Subcategories:**

| Subcategory | Focus | Examples |
|-------------|-------|----------|
| **Accuracy** | Truthfulness, evidence | No speculation, cite sources |
| **Scope** | Boundaries, focus | Stay on topic, length limits |
| **Tone** | Communication style | Professional, friendly, academic |
| **Safety** | Harmful content prevention | No violence, no medical advice |
| **Format** | Structural requirements | Include sections, use headers |

---

### 2.4 Output Formats

> [!what-this-does] Output Format Purpose
> Output formats define the **structure, organization, and presentation** of LLM responses. They answer: "How should the output be organized?"

**Location:** `02-component-library/atomic/output-formats/`

**Core Elements:**

```markdown
## Output Format Components Include:

### Structure Template
"Organize your response as follows:..."

### Section Definitions
"Each section should include..."

### Formatting Rules
"Use [markdown/headers/lists] for..."

### Length Guidelines
"This section should be approximately..."
```

**Example Output Format Component:**

```markdown
---
type: component
component-type: format
atomic-composite: atomic
domain: general
id: 20251224150004
status: active
version: "1.0.0"
tags: ["year/2025", "prompt-engineering", "component-type/format", "format/structured"]
---

# Structured Analysis Report Format

> [!definition] Component Purpose
> Provides a template for comprehensive analytical reports with clear sections.

## Component Text

```prompt
Structure your analysis using this format:

## Executive Summary
[2-3 sentences capturing the key finding and recommendation]

## Background Context
[Brief relevant context that frames the analysis - 1-2 paragraphs]

## Analysis

### [Aspect 1 Name]
[Detailed examination - include evidence, implications]

### [Aspect 2 Name]
[Detailed examination - include evidence, implications]

### [Additional aspects as needed]

## Key Findings
[Numbered list of 3-5 most important discoveries]

## Recommendations
[Prioritized, actionable recommendations with rationale]

## Limitations & Caveats
[What this analysis cannot address, assumptions made]

## Next Steps
[Specific follow-up actions or questions to explore]
```

## When to Use
- Business analysis
- Research synthesis
- Evaluation reports
- Strategic recommendations

## Customization Points
- Number of analysis sections (adjustable)
- Depth of executive summary
- Recommendation detail level

## Works Well With
- [[expert-analyst-persona]]
- [[comparative-analysis-instruction]]
- [[evidence-based-constraint]]
```

**Output Format Subcategories:**

| Subcategory | Structure Type | Examples |
|-------------|---------------|----------|
| **Reports** | Formal documents | Analysis reports, summaries |
| **Lists** | Itemized output | Rankings, checklists, inventories |
| **Tables** | Comparative grids | Comparisons, specifications |
| **Narrative** | Flowing prose | Stories, explanations, essays |
| **Code** | Technical output | Functions, documentation, configs |
| **Hybrid** | Mixed formats | Tutorials (prose + code) |

---

### 2.5 Context Framers

> [!what-this-does] Context Framer Purpose
> Context framers provide **background information, situational context, and framing** for tasks. They answer: "What context does the LLM need to understand the task?"

**Location:** `02-component-library/atomic/context-framers/`

**Core Elements:**

```markdown
## Context Framer Components Include:

### Situation Description
"In this context...", "Given that..."

### Background Information
"The relevant background is..."

### User Characteristics
"The target audience is..."

### Goal Clarification
"The ultimate objective is..."
```

**Example Context Framer Component:**

```markdown
---
type: component
component-type: context
atomic-composite: atomic
domain: pkb
id: 20251224150005
status: active
version: "1.0.0"
tags: ["year/2025", "prompt-engineering", "component-type/context", "domain/pkb"]
---

# PKB Obsidian Environment Context

> [!definition] Component Purpose
> Establishes context for tasks within an Obsidian-based Personal Knowledge Base.

## Component Text

```prompt
Context: You are working within an Obsidian-based Personal Knowledge Base (PKB) system.

ENVIRONMENT DETAILS:
- Platform: Obsidian markdown editor with wiki-link support
- Key plugins: Dataview (queries), Templater (automation), Meta-Bind (interactive fields)
- Linking: [[Double bracket]] wiki-links for internal connections
- Structure: Hierarchical folders with MOC (Map of Content) navigation hubs

FORMATTING EXPECTATIONS:
- All key concepts formatted as [[Wiki-Links]]
- Frontmatter metadata in YAML format
- Callouts using > [!type] syntax
- Prose-dominant content (minimal bullet lists)

USER CONTEXT:
- The user is building a systematic knowledge base
- Emphasizes connections and discoverability
- Follows Zettelkasten-influenced methodology
- Values comprehensive, well-linked documentation

OUTPUT SHOULD:
- Be ready to paste directly into Obsidian
- Include proper wiki-links for referenced concepts
- Use appropriate callout types for semantic structure
- Support knowledge graph building through connections
```

## When to Use
- Any PKB-related task
- Creating notes for Obsidian
- Generating wiki-link-rich content
- Building knowledge graph content

## Works Well With
- [[pkb-architect-persona]]
- [[note-creation-instruction]]
- [[obsidian-format]]
```

---

## 📋 PART III: COMPONENT CREATION

### 3.1 Standard Component Template

```markdown
---
# REQUIRED FIELDS
type: component
id: YYYYMMDDHHmmss
component-type: persona | instruction | constraint | format | context | example
atomic-composite: atomic | composite
domain: general | technical | creative | educational | pkb
status: active
version: "1.0.0"
rating: "0.0"
confidence: speculative
maturity: seedling
source: original | claude-sonnet-4.5 | claude-opus-4.5 | other
created: YYYY-MM-DD
modified: YYYY-MM-DD
usage-count: 0

# REQUIRED TAGS
tags:
  - "year/YYYY"
  - "prompt-engineering"
  - "component-type/[type]"
  - "domain/[domain]"

# OPTIONAL BUT VALUABLE
aliases: []
performance-score: "0.0"
conflicts-with: []
synergies-with: []
used-in-prompts: []
---

# [Component Name]

> [!definition] Component Purpose
> [One sentence describing what this component accomplishes]

## Component Text

```prompt
[The actual prompt text to copy/paste into prompts]
```

## When to Use
[Scenarios where this component excels]
- [Use case 1]
- [Use case 2]

## When NOT to Use
[Scenarios where this component fails or is inappropriate]
- [Anti-pattern 1]
- [Anti-pattern 2]

## Parameters
[If the component has customizable elements]
- **Parameter 1**: [Description]
- **Parameter 2**: [Description]

## Works Well With
[Components that synergize]
- [[component-1]] - [Why they work together]
- [[component-2]] - [Synergy description]

## Conflicts With
[Components that shouldn't be combined]
- [[component-3]] - [Conflict reason]

## Performance Notes
[Testing results, usage patterns, quality observations]

## Version History
- 1.0.0 (YYYY-MM-DD): Initial version
```

### 3.2 Creation Workflow

```
1. IDENTIFY NEED
   └─ Notice repeated prompt pattern
   └─ Receive request for new capability
   └─ Optimize existing high-use pattern

2. CHECK DUPLICATES
   └─ Search existing library
   └─ Query: component-type + domain + keywords
   └─ If similar exists: consider extending vs. new

3. DESIGN COMPONENT
   └─ Define single responsibility
   └─ Write core prompt text
   └─ Identify parameters
   └─ Document use/anti-use cases

4. CREATE NOTE
   └─ Use standard template
   └─ Complete all required fields
   └─ Add appropriate tags
   └─ Set initial status: active, maturity: seedling

5. TEST ISOLATION
   └─ Use component alone
   └─ Verify it works independently
   └─ Document test results

6. TEST INTEGRATION
   └─ Combine with common partners
   └─ Identify synergies and conflicts
   └─ Update works-well-with and conflicts-with

7. CONNECT TO GRAPH
   └─ Add to appropriate folder
   └─ Link from relevant MOC
   └─ Add backlinks from related components
```

### 3.3 Quality Criteria

**A well-designed component:**

- [ ] **Single Purpose**: Does exactly one thing well
- [ ] **Self-Documenting**: Usage clear from component text
- [ ] **Testable**: Can be evaluated in isolation
- [ ] **Composable**: Works with other components without modification
- [ ] **Parameterized**: Customization points clearly marked
- [ ] **Documented**: When to use, when not to use, conflicts, synergies
- [ ] **Versioned**: Changes tracked through version history
- [ ] **Connected**: Links to related components in knowledge graph

---

## 🔍 PART IV: COMPONENT DISCOVERY

### 4.1 Search Strategies

**By Type:**
```dataview
TABLE domain, usage-count, performance-score
FROM "02-component-library"
WHERE component-type = "persona"
SORT usage-count DESC
```

**By Domain:**
```dataview
TABLE component-type, usage-count, performance-score
FROM "02-component-library"
WHERE domain = "technical"
SORT component-type, usage-count DESC
```

**By Performance:**
```dataview
TABLE component-type, domain, usage-count
FROM "02-component-library"
WHERE performance-score >= 8.0
SORT performance-score DESC
```

**By Tags:**
```
tag:#persona tag:#expert - Expert personas
tag:#constraint tag:#accuracy - Accuracy constraints
tag:#format tag:#structured - Structured output formats
```

### 4.2 Discovery Queries

**Find underutilized high-performers:**
```dataview
TABLE component-type, performance-score, usage-count
FROM "02-component-library"
WHERE performance-score >= 8.0 AND usage-count < 5
SORT performance-score DESC
```

**Find components needing testing:**
```dataview
TABLE component-type, domain, created
FROM "02-component-library"
WHERE confidence = "speculative" AND maturity = "seedling"
SORT created DESC
```

**Find component gaps:**
```dataview
TABLE component-type, COUNT(file.name) as count
FROM "02-component-library"
GROUP BY component-type
```

### 4.3 Synergy Discovery

**Components frequently used together:**
```dataviewjs
// Query prompts to find component co-occurrence
const prompts = dv.pages('"08-active-prompts"')
    .where(p => p.type === "prompt" && p["components-used"]);

// Count co-occurrences
// (Full implementation would analyze components-used arrays)
```

---

## 📊 PART V: COMPONENT MAINTENANCE

### 5.1 Lifecycle Stages

```
SEEDLING 🌱
├─ Just created
├─ Unvalidated
├─ May have issues
└─ Review: 7 days

     ↓ (Testing + 3+ successful uses)

DEVELOPING 🌿
├─ Some validation
├─ Patterns emerging
├─ Minor refinements needed
└─ Review: 14 days

     ↓ (Consistent performance + 10+ uses)

BUDDING 🌸
├─ Well-tested
├─ Reliable in context
├─ Documentation complete
└─ Review: 30 days

     ↓ (Proven across contexts + 25+ uses)

EVERGREEN 🌳
├─ Mature, stable
├─ Widely applicable
├─ Gold standard quality
└─ Review: 90 days

     ↓ (Superseded or obsolete)

DEPRECATED ⚠️
├─ No longer recommended
├─ Replacement available
├─ Kept for history
└─ Archive after transition period
```

### 5.2 Maintenance Tasks

**After Each Use:**
- Increment `usage-count`
- Update `last-used` if tracking
- Note any issues observed

**After Testing:**
- Update `rating` based on quality score
- Adjust `confidence` level
- Update `maturity` if warranted
- Add test result link

**Periodic Review:**
- Check usage patterns
- Identify optimization opportunities
- Update documentation
- Verify synergies/conflicts still accurate
- Update version if modified

### 5.3 Deprecation Protocol

```
1. IDENTIFY FOR DEPRECATION
   └─ Better alternative exists
   └─ Pattern no longer relevant
   └─ Consistently poor performance

2. DOCUMENT REASON
   └─ Update status: deprecated
   └─ Add deprecation note in body
   └─ Link to replacement (if exists)

3. NOTIFY DEPENDENTS
   └─ Find prompts using this component
   └─ Flag prompts for update
   └─ Update prompts to use replacement

4. ARCHIVE
   └─ After transition period (30 days)
   └─ Move to archive folder
   └─ Maintain for historical reference
```

---

## 🔗 Related Topics for PKB Expansion

### 1. **[[Prompt Assembly Patterns]]**
- *Connection*: How to combine components effectively
- *Priority*: High - Essential for prompt creation

### 2. **[[Component Testing Methodology]]**
- *Connection*: How to validate component quality
- *Priority*: High - Ensures library quality

### 3. **[[Composite Component Design]]**
- *Connection*: When and how to create composite components
- *Priority*: Medium - Advanced library usage

### 4. **[[Component Analytics Dashboard]]**
- *Connection*: Monitoring library health and usage
- *Priority*: Medium - System optimization

---

*Reference Version: 1.0.0 | Created: 2025-12-24 | Status: Production Ready*
*Authoritative Reference for Component Library Operations*
