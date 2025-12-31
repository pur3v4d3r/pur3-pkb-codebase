---
tags: #spes #documentation #operations-manual #reference-note #system-documentation
aliases: [SPES Manual, Operations Guide, System Manual, Master Documentation]
status: evergreen
certainty: verified
priority: high
created: 2025-12-24
type: reference
project: prompt-engineering-templater-system
link-up: "[[00-prompt-engineering-system-design]]"
link-related:
  - "[[architecture-overview]]"
  - "[[metadata-schema-reference]]"
  - "[[vault-map]]"
---

# 📚 SPES Master Operations Manual

> [!abstract] Executive Summary
> This is the **authoritative operations manual** for the Sequential Prompt Engineering System (SPES) integrated with your Personal Knowledge Base (PKB). This document provides everything needed to understand, operate, and extend the system—whether you're the human operator (Pur3v4d3r) or an AI assistant (Claude) working within the system.

---

## 🏛️ PART I: SYSTEM ARCHITECTURE

### 1.1 What is SPES?

> [!definition] Sequential Prompt Engineering System (SPES)
> A **production-ready framework** for creating, testing, optimizing, and managing AI prompts through systematic workflows, reusable components, and intelligent automation. Built on [[Obsidian]] with [[Dataview]], [[Templater]], [[QuickAdd]], and [[Meta-Bind]] plugins.

The system serves three core functions:

1. **Creation**: Generate new prompts with minimal friction (< 30 seconds for quick capture, < 5 minutes for full prompts)
2. **Quality Assurance**: Enforce consistent metadata, validate structure, guide testing workflows
3. **Intelligence**: Auto-discover patterns, track usage analytics, recommend components

### 1.2 The Three-Pillar Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         SPES SYSTEM                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────────┐  ┌───────────────┐   ┌─────────────────────┐ │
│  │  PILLAR 1:    │  │  PILLAR 2:    │   │    PILLAR 3:        │ │
│  │  Component    │  │  Sequential   │   │    Intelligence     │ │
│  │  Library      │  │  Workflows    │   │    Layer            │ │
│  │               │  │               │   │                     │ │
│  │ • Personas    │  │ • Decomp.     │   │ • Dataview          │ │
│  │ • Instructions│  │ • Problem     │   │ • Analytics         │ │
│  │ • Constraints │  │   Types       │   │ • Discovery         │ │
│  │ • Formats     │  │ • Context     │   │ • Patterns          │ │
│  │ • Context     │  │   Handoff     │   │                     │ │
│  └───────┬───────┘  └───────┬───────┘   └──────────┬──────────┘ │
│          │                  │                      │            │
│          └──────────────────┴──────────────────────┘            │
│                             │                                   │
│              ┌──────────────┴──────────────────┐                │
│              │     CLAUDE LIBRARIAN            │                │
│              │     (Orchestration Layer)       │                │
│              └──────────────┬──────────────────┘                │
│                             │                                   │
│              ┌──────────────┴──────────────────┐                │
│              │     PKB FOUNDATION              │                │
│              │     (Obsidian Vault)            │                │
│              └─────────────────────────────────┘                │
└─────────────────────────────────────────────────────────────────┘
```

#### Pillar 1: Component Library

> [!what-this-does] Component Library Purpose
> The component library contains **reusable, tested prompt building blocks** organized by type and complexity. Think of it as a parts warehouse where you select pre-validated pieces to assemble into complete prompts.

**Structure:**
```
02-component-library/
├── atomic/                    # Single-purpose, indivisible components
│   ├── personas/              # Identity/role frames ("You are a...")
│   ├── instructions/          # Task directives ("Analyze...", "Generate...")
│   ├── constraints/           # Boundaries/restrictions ("Do not...", "Always...")
│   ├── output-formats/        # Templates for structured output
│   └── context-framers/       # Background/situation setters
│
├── composite/                 # Multi-component assembled workflows
│   ├── sequential-chains/     # A→B→C patterns
│   ├── parallel-branches/     # Simultaneous exploration paths
│   └── recursive-loops/       # Iterative refinement patterns
│
└── specialized/               # Domain-specific optimized templates
    ├── educational-content/   # Pedagogy-optimized prompts
    ├── technical-analysis/    # Rigor and precision focused
    ├── creative-writing/      # Style and narrative focused
    └── pkb-operations/        # Knowledge management specific
```

#### Pillar 2: Sequential Workflows

> [!what-this-does] Sequential Workflows Purpose
> Proven **decomposition patterns** for breaking complex problems into multi-turn sequences. Each workflow documents when to use it, how to execute it, and how to manage context between turns.

**Key Workflow Patterns:**

| Pattern | Use When | Typical Turns |
|---------|----------|---------------|
| [[least-to-most-prompting]] | Hierarchical problems needing foundation first | 3-5 |
| [[chain-of-verification]] | High-accuracy requirements | 2-4 |
| [[recursive-expansion-loop]] | Long-form content generation | 4-8 |
| [[parallel-convergence]] | Multiple perspectives needed | 3-5 |
| [[staged-generation]] | Complex multi-section documents | 4-10 |

#### Pillar 3: Intelligence Layer

> [!what-this-does] Intelligence Layer Purpose
> **Self-documenting metadata system** enabling discovery, analytics, and emergent intelligence through [[Dataview]] queries and pattern detection.

**Capabilities:**
- **Discovery**: Find components by type, domain, performance
- **Analytics**: Track usage counts, success rates, quality scores
- **Patterns**: Detect synergies, conflicts, and optimization opportunities
- **Health**: Monitor metadata compliance, orphan notes, broken links

---

## 🗂️ PART II: FOLDER STRUCTURE & ORGANIZATION

### 2.1 Complete Directory Map

```
d:\10_pur3v4d3r's-vault\
│
├── 00-inbox/
│   └── prompt-ideas/              ← Quick captures land here first
│
├── 00-meta/                       ← System memory & configuration
│   ├── session-memory.md          ← Current session context
│   ├── project-tracker.md         ← Active SPES tasks
│   ├── user-preferences.md        ← Workflow patterns
│   └── vault-map.md               ← Structural insights
│
├── 02-projects/
│   └── _spes-sequential-prompt-engineering-system/
│       │
│       ├── 00-project-meta/       ← Project documentation
│       │   ├── 00-prompt-engineering-system-design.md
│       │   ├── 01-implementation-tracker.md
│       │   └── 02-quick-reference-guide.md
│       │
│       ├── 02-component-library/  ← PILLAR 1: Reusable components
│       │   ├── atomic/
│       │   ├── composite/
│       │   └── specialized/
│       │
│       ├── 03-sequential-workflows/ ← PILLAR 2: Decomposition patterns
│       │   ├── decomposition-templates/
│       │   ├── problem-types/
│       │   └── context-handoff-patterns/
│       │
│       ├── 04-intelligence-layer/  ← PILLAR 3: Analytics & discovery
│       │   ├── dashboards/
│       │   ├── analytics/
│       │   └── discovery-queries/
│       │
│       ├── 05-testing-validation/  ← Quality assurance
│       │   ├── ab-tests/
│       │   ├── test-results/
│       │   └── debug-logs/
│       │
│       └── 08-active-prompts/      ← Working prompts in use
│           ├── agentic/            ← Claude Projects, Gemini Gems
│           ├── system-prompts/     ← Instruction prompts
│           ├── user-prompts/       ← Interaction prompts
│           └── chains/             ← Multi-step workflows
│
├── 06-dashboards/
│   └── prompt-engineering-dashboard.md  ← Master overview
│
└── 99-system/
    ├── 01-quickadd/
    │   ├── 01-macros/             ← JavaScript automation
    │   └── 02-templates/          ← Templater templates
    │
    └── 02-scripts/                ← Python diagnostic scripts
```

### 2.2 File Naming Conventions

> [!principle-point] Naming Standards
> Consistent naming enables reliable automation and intuitive navigation.

| Pattern | Example | When to Use |
|---------|---------|-------------|
| `kebab-case` | `chain-of-thought-template.md` | All note names |
| `_prefix` | `_spes-project-folder/` | Project folders (sorts first) |
| `NN-prefix` | `00-inbox/`, `02-projects/` | Top-level organization |
| `YYYYMMDD` | `20251224` | Date-based IDs |
| `YYYYMMDDHHmmss` | `20251224143022` | Timestamp-based unique IDs |

---

## 📊 PART III: METADATA SCHEMA

### 3.1 Universal Fields (All Note Types)

Every prompt, component, workflow, or test result note **MUST** include these fields:

```yaml
---
# CORE IDENTITY (Required)
type: "prompt" | "component" | "workflow" | "test-result"
id: "YYYYMMDDHHmmss"              # Unique timestamp-based ID
status: "active" | "testing" | "production" | "deprecated" | "archived"
version: "MAJOR.MINOR.PATCH"      # Semantic versioning (e.g., "1.2.0")

# QUALITY METRICS (Required)
rating: 0.0-10.0                  # User quality assessment
confidence: "speculative" | "provisional" | "moderate" | "established" | "high"
maturity: "seedling" | "developing" | "budding" | "evergreen"

# SOURCE & ATTRIBUTION (Required)
source: "claude-sonnet-4.5" | "claude-opus-4.5" | "gemini-3.0-pro" | 
        "gemini-3.0-flash" | "original" | "local-llm" | "other"

# TEMPORAL (Required)
created: "YYYY-MM-DD"
modified: "YYYY-MM-DD"

# USAGE TRACKING (Required)
usage-count: 0                    # Increment on deployment

# CATEGORIZATION (Required)
tags:
  - "year/YYYY"                   # Always include current year
  - "prompt-engineering"          # Umbrella category
  - [additional relevant tags]

# GRAPH INTEGRATION (Optional but recommended)
aliases: []                       # Alternative names for search
link-up: "[[prompt-engineering-moc]]"
link-related: []                  # Connected notes
---
```

### 3.2 Controlled Vocabularies

> [!important] Vocabulary Enforcement
> Using ONLY these predefined values ensures Dataview queries work correctly and maintains system consistency.

#### Status Values

| Value | Meaning | When to Use |
|-------|---------|-------------|
| `active` | Currently in use, maintained | Default for new prompts |
| `testing` | Under evaluation | During A/B testing or validation |
| `production` | Proven, deployed, stable | After successful testing |
| `deprecated` | Replaced, no longer recommended | When superseded |
| `archived` | Historical, no longer maintained | Project completed |

#### Confidence Values (Epistemic Status)

| Value | Meaning | Evidence Level |
|-------|---------|----------------|
| `speculative` | Unproven, experimental | Hypothesis only |
| `provisional` | Some testing, preliminary | 1-2 test results |
| `moderate` | Multiple tests, generally reliable | 3-5 successful uses |
| `established` | Extensively tested, consistently good | 10+ uses, documented |
| `high` | Proven excellent, gold standard | Validated across contexts |

#### Maturity Values (Development Stage)

| Value | Symbol | Description | Review Interval |
|-------|--------|-------------|-----------------|
| `seedling` | 🌱 | New, unrefined, needs development | 7 days |
| `developing` | 🌿 | Growing, improving, getting tested | 14 days |
| `budding` | 🌸 | Solid foundation, minor refinements | 30 days |
| `evergreen` | 🌳 | Mature, stable, proven over time | 90 days |

### 3.3 Type-Specific Fields

#### For Components (`type: "component"`)

```yaml
# Additional required fields
component-type: "persona" | "instruction" | "constraint" | "format" | "context" | "example"
atomic-composite: "atomic" | "composite"
domain: "general" | "technical" | "creative" | "educational" | "pkb"

# Optional but valuable
performance-score: 0.0-10.0       # Average quality across uses
conflicts-with: []                # Components that don't work together
synergies-with: []                # Components that enhance each other
used-in-prompts: []               # Track where component is deployed
```

#### For Test Results (`type: "test-result"`)

```yaml
# Required
prompt-tested: "[[prompt-name]]"
test-date: "YYYY-MM-DD"
test-type: "functional" | "quality" | "performance" | "ab-comparison"
success: true | false

# Optional
quality-score: 0.0-10.0
issues-found: []
recommendations: []
```

---

## ⚙️ PART IV: DAILY OPERATIONS

### 4.1 Creating New Prompts

#### Quick Capture (< 10 seconds)

For capturing ideas on the fly:

1. **Trigger**: QuickAdd macro → `Prompt Quick Capture`
2. **Input**: Title + brief description
3. **Output**: Idea note in `00-inbox/prompt-ideas/`
4. **Metadata**: Minimal (type, created, source)

```yaml
# Quick capture template
---
type: idea
created: 2025-12-24
source: original
status: seedling
---

# [Idea Title]

## Initial Thought
[One paragraph describing the prompt idea]

## Potential Use Cases
- [Use case 1]
- [Use case 2]

## Next Steps
- [ ] Develop into full prompt
- [ ] Identify components needed
```

#### Full Prompt Creation (2-5 minutes)

For complete, production-ready prompts:

1. **Trigger**: Templater → `_prompt-master-template.md`
2. **Guided Input**: 
   - Type selection (system, user, chain)
   - Target LLM selection
   - Domain classification
   - Component search and insertion
3. **Output**: Complete prompt in appropriate folder
4. **Metadata**: Full schema compliance

> [!methodology-and-sources] Workflow Decision Tree
> ```
> Is this a quick thought I might forget?
> ├─ YES → Quick Capture macro → Inbox
> └─ NO → Is this a complete prompt I'll use soon?
>     ├─ YES → Full Template → Active Prompts
>     └─ NO → Is this a reusable building block?
>         ├─ YES → Component Template → Component Library
>         └─ NO → Reference/Documentation note
> ```

### 4.2 Using the Component Library

#### Finding Components

**Method 1: Dataview Dashboard**

```dataview
TABLE component-type, domain, usage-count, performance-score
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"
WHERE type = "component"
SORT usage-count DESC, performance-score DESC
LIMIT 20
```

**Method 2: Tag-Based Search**

Use Obsidian search with tag filters:
- `tag:#persona` - All persona components
- `tag:#instruction tag:#technical` - Technical instructions
- `tag:#constraint tag:#pkb` - PKB-specific constraints

**Method 3: QuickAdd Macro**

Trigger `Component Search & Insert` macro for fuzzy search with preview.

#### Inserting Components

Once found, components are inserted via:

1. **Copy-paste**: Direct text extraction from component note
2. **Templater include**: `NaN`
3. **QuickAdd**: Automated insertion with usage tracking

> [!warning] Post-Insertion Requirements
> After inserting a component:
> 1. Update `components-used` field in prompt metadata
> 2. Add backlink to component's `used-in-prompts` field
> 3. Verify component version compatibility

### 4.3 Testing Prompts

#### Functional Testing

Basic verification that prompt produces expected output type:

```yaml
# Test documentation template
---
type: test-result
prompt-tested: "[[my-prompt]]"
test-date: 2025-12-24
test-type: functional
success: true
---

## Test Parameters
- **LLM**: Claude Sonnet 4.5
- **Temperature**: 0.7
- **Context Window**: Full

## Test Input
[Exact input used]

## Expected Output
[What we expected to receive]

## Actual Output
[What we actually received]

## Assessment
- [x] Output type matches specification
- [x] All required sections present
- [ ] Quality meets threshold (7/10)
```

#### A/B Comparison Testing

For comparing prompt variants:

1. Create two versions with identical inputs
2. Document differences in approach
3. Run both against same test cases
4. Score outputs independently
5. Document winner and rationale

### 4.4 Version Management

#### When to Bump Versions

| Change Type | Version Bump | Examples |
|-------------|--------------|----------|
| **MAJOR** | X.0.0 | Breaking changes, restructured prompt, new LLM target |
| **MINOR** | x.Y.0 | New feature, added section, enhanced capability |
| **PATCH** | x.y.Z | Bug fix, typo correction, minor wording adjustment |

#### Version Bump Workflow

```javascript
// QuickAdd version bump macro pseudocode
1. Read current version from frontmatter
2. Parse MAJOR.MINOR.PATCH
3. Prompt user: "What type of change?"
4. Increment appropriate segment
5. Update version field
6. Update modified date
7. Add changelog entry (optional)
```

---

## 🔍 PART V: DATAVIEW QUERIES & DASHBOARDS

### 5.1 Essential Queries

#### All Prompts by Status

```dataview
TABLE status, rating, maturity, usage-count as "Uses"
FROM "02-projects/_spes-sequential-prompt-engineering-system"
WHERE type = "prompt"
SORT status ASC, rating DESC
```

#### Components Needing Testing

```dataview
TABLE component-type, domain, confidence, created
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"
WHERE type = "component" AND confidence = "speculative"
SORT created DESC
```

#### Prompts Due for Review

```dataview
TABLE maturity, review-next, last-used
FROM "02-projects/_spes-sequential-prompt-engineering-system"
WHERE type = "prompt" AND review-next <= date(today)
SORT review-next ASC
```

#### High-Performance Components

```dataview
TABLE component-type, performance-score, usage-count
FROM "02-projects/_spes-sequential-prompt-engineering-system/02-component-library"
WHERE type = "component" AND performance-score >= 8.0
SORT performance-score DESC
```

#### Orphan Detection

```dataview
LIST
FROM "02-projects/_spes-sequential-prompt-engineering-system"
WHERE length(file.inlinks) = 0 AND length(file.outlinks) = 0
SORT file.name
```

### 5.2 Dashboard Template

```markdown
# 📊 SPES Dashboard

## Quick Stats

**Total Prompts**: `$= dv.pages('"02-projects/_spes"').where(p => p.type == "prompt").length`
**Active Components**: `$= dv.pages('"02-projects/_spes"').where(p => p.type == "component" && p.status == "active").length`
**Tests This Week**: `$= dv.pages('"02-projects/_spes"').where(p => p.type == "test-result" && p.test-date >= dv.date("today - 7 days")).length`

## Attention Required

### ⚠️ Prompts Needing Review
[Dataview query for overdue reviews]

### 🌱 Seedlings to Develop
[Dataview query for seedling status items]

### 🔗 Orphan Notes
[Dataview query for disconnected notes]

## Recent Activity

### Latest Prompts
[Dataview query sorted by created DESC LIMIT 5]

### Latest Test Results
[Dataview query sorted by test-date DESC LIMIT 5]
```

---

## 🧠 PART VI: LLM INTEGRATION PROTOCOL

> [!important] For AI Assistants
> This section defines how Claude and other LLMs should operate within SPES. If you are an AI assistant reading this, follow these protocols precisely.

### 6.1 Identity & Role

When operating in SPES context, Claude functions as the **SPES Librarian**:

> [!definition] SPES Librarian Role
> An intelligent orchestrator that:
> 1. **Understands** user problems and intent
> 2. **Searches** the component library for relevant pieces
> 3. **Recommends** workflows and components
> 4. **Executes** sequential workflows with the user
> 5. **Learns** from outcomes via metadata updates
> 6. **Improves** the system over time

### 6.2 Decision Framework

```
User Request Received
         ↓
[Is this a SPES task?]
├─ Prompt creation/editing
├─ Component search/creation
├─ Workflow recommendation
├─ Testing/validation
├─ System maintenance
         ↓
    YES → Enter SPES Librarian Mode
         ↓
[Is this complex?]
├─ Multiple components needed
├─ Multi-turn workflow required
├─ Optimization needed
├─ Testing required
         ↓
├─ YES → Recommend decomposition
│        Select workflow pattern
│        Search for components
│        Orchestrate execution
│
└─ NO → Recommend single component
        or direct execution
         ↓
After Execution:
├─ Update usage counts
├─ Log outcomes
├─ Detect patterns
└─ Update session memory
```

### 6.3 Core Operations

#### Operation: Create New Prompt

```
1. Clarify Requirements
   - Target LLM?
   - Task type?
   - Domain?
   - Quality requirements?

2. Search Component Library
   - Query: relevant components by type + domain
   - Present top 3-5 options per category
   - Explain synergies/conflicts

3. Assemble Prompt
   - Insert selected components
   - Add transitions/connecting tissue
   - Ensure logical flow

4. Validate
   - Check all required metadata fields
   - Verify wiki-link formatting
   - Confirm component compatibility

5. Document
   - Update components-used field
   - Create backlinks
   - Set appropriate status/maturity
```

#### Operation: Search Components

```
1. Parse Search Intent
   - Component type needed?
   - Domain filter?
   - Performance threshold?

2. Execute Query
   - Primary: Dataview by type + domain
   - Secondary: Tag-based search
   - Tertiary: Full-text search

3. Rank Results
   - Performance score
   - Usage count
   - Recency
   - Relevance to request

4. Present Options
   - Top 5 most relevant
   - Include: name, type, score, usage
   - Note any conflicts with already-selected components
```

#### Operation: Recommend Workflow

```
1. Classify Problem
   - Long-form generation? → recursive-expansion-loop
   - High accuracy needed? → chain-of-verification
   - Hierarchical structure? → least-to-most-prompting
   - Multiple dimensions? → parallel-convergence
   - Independent subtasks? → strict-isolation

2. Check Constraints
   - Token budget available
   - Turn limit acceptable
   - Quality threshold
   - Time constraints

3. Present Recommendation
   - Workflow name and link
   - Expected turns
   - Component suggestions per turn
   - Context handoff strategy
```

### 6.4 Metadata Maintenance

> [!principle-point] AI Metadata Responsibilities
> When creating or modifying SPES content, Claude MUST:

1. **Always include all required fields** - Never create notes with incomplete metadata
2. **Use controlled vocabularies** - Only values from approved lists
3. **Generate valid IDs** - Format: `YYYYMMDDHHmmss`
4. **Set appropriate defaults**:
   - New prompts: `status: active`, `maturity: seedling`, `confidence: speculative`
   - `rating: 0.0` (until tested)
   - `usage-count: 0`
5. **Update timestamps** - `modified` on every edit
6. **Maintain wiki-links** - Format all key concepts as `[[Wiki-Links]]`

### 6.5 Response Format Standards

When generating SPES content, Claude follows these formatting requirements:

```markdown
---
[Complete YAML frontmatter per schema]
---

# [Note Title]

> [!abstract] Purpose
> [One-sentence description of what this note provides]

## Section Structure

[Prose-dominant content with wiki-links for key concepts]

> [!definition] Term Name
> [Formal definition when introducing concepts]

> [!example] Concrete Illustration
> [Practical demonstration]

## [Additional Sections]

[Content following PKB formatting standards]

---

## 🔗 Related Topics for PKB Expansion

1. **[[Extension Topic 1]]**
   - *Connection*: [How this relates]
   - *Priority*: [High/Medium/Low]

[... 4 total expansion topics]
```

---

## 🔧 PART VII: TROUBLESHOOTING & MAINTENANCE

### 7.1 Common Issues

#### Issue: Dataview Query Returns Empty

**Symptoms**: Query shows no results when data exists

**Diagnosis**:
```markdown
1. Check path in FROM clause matches actual folder structure
2. Verify frontmatter syntax (proper YAML formatting)
3. Confirm field names match exactly (case-sensitive)
4. Look for invisible characters in metadata
```

**Solution**:
```dataview
// Debug query - shows all fields from a specific note
TABLE file.frontmatter
FROM "path/to/suspected/note"
```

#### Issue: Component Not Found in Search

**Symptoms**: Component exists but doesn't appear in searches

**Diagnosis**:
```markdown
1. Check component has type: "component" in frontmatter
2. Verify tags include correct type tag (#persona, #instruction, etc.)
3. Confirm note is in component library folder
4. Check for frontmatter parsing errors
```

**Solution**: Run metadata audit query:
```dataview
TABLE type, component-type, tags
FROM "02-component-library"
WHERE !type OR !component-type
```

#### Issue: Orphan Notes Accumulating

**Symptoms**: Notes with no incoming or outgoing links

**Diagnosis**:
```dataview
LIST
FROM "02-projects/_spes"
WHERE length(file.inlinks) = 0 OR length(file.outlinks) = 0
```

**Solution**:
1. Add minimum 2 outgoing links (related concepts)
2. Link from appropriate MOC or index
3. Add to `link-related` field in relevant notes

### 7.2 Health Checks

#### Daily Health Check

```markdown
## Daily SPES Health Check

- [ ] Review inbox for new captures
- [ ] Check dashboard for overdue reviews
- [ ] Verify no critical orphans created
- [ ] Process any failed test results
```

#### Weekly Health Check

```markdown
## Weekly SPES Health Check

### Metadata Compliance
Run: `metaudit` - Verify >90% compliance

### Graph Health  
Run: `orphan` - Target <20% orphan rate

### Link Integrity
Run: `linkcheck` - Target <10% broken links

### Usage Analytics
- Most used components this week
- Prompts with declining performance
- New patterns detected
```

#### Monthly Health Check

```markdown
## Monthly SPES Health Check

### System Review
- [ ] Archive prompts unused >90 days
- [ ] Update deprecated components
- [ ] Review and update MOCs
- [ ] Capacity planning (storage, performance)

### Quality Improvement
- [ ] Identify optimization opportunities
- [ ] Extract successful patterns to library
- [ ] Update documentation
- [ ] Review and refine workflows
```

### 7.3 Backup & Recovery

> [!warning] Data Protection
> The SPES system is built on plain markdown files—easily backed up but also easily lost without proper procedures.

**Backup Strategy**:
```bash
# Git-based backup (recommended)
git add .
git commit -m "SPES backup: $(date +%Y-%m-%d)"
git push origin master

# Alternative: File copy
cp -r "d:\10_pur3v4d3r's-vault" "d:\backup\vault-$(date +%Y%m%d)"
```

**Recovery Procedure**:
1. Identify last known good state (git log or backup timestamp)
2. Restore files from backup
3. Run full health check
4. Verify Dataview queries function
5. Test critical workflows

---

## 📋 PART VIII: QUICK REFERENCE CARDS

### 8.1 Metadata Quick Reference

```yaml
# MINIMUM VIABLE METADATA (copy this template)
---
type: prompt
id: # Generate: YYYYMMDDHHmmss
status: active
version: "1.0.0"
rating: "0.0"
confidence: speculative
maturity: seedling
source: original
created: # YYYY-MM-DD
modified: # YYYY-MM-DD
usage-count: 0
tags:
  - "year/2025"
  - "prompt-engineering"
---
```

### 8.2 Component Types Quick Reference

| Type | Purpose | Example |
|------|---------|---------|
| `persona` | Identity frame | "You are an expert data analyst..." |
| `instruction` | Task directive | "Analyze the following data and..." |
| `constraint` | Boundary | "Do not include speculation..." |
| `format` | Output template | "Structure your response as..." |
| `context` | Background | "Given the following context..." |
| `example` | Few-shot demo | "Here's an example of good output..." |

### 8.3 Callout Quick Reference

| Callout | Purpose | When to Use |
|---------|---------|-------------|
| `[!definition]` | Formal definitions | Introducing key terms |
| `[!example]` | Concrete illustrations | Demonstrating concepts |
| `[!warning]` | Critical cautions | Potential problems |
| `[!important]` | Must-know info | Key takeaways |
| `[!methodology-and-sources]` | Process explanation | How things work |
| `[!what-this-does]` | Functional description | Feature explanations |
| `[!helpful-tip]` | Practical advice | Best practices |

### 8.4 Workflow Selection Quick Reference

```
Problem Type               →  Recommended Workflow
─────────────────────────────────────────────────
Long-form content          →  recursive-expansion-loop
High accuracy required     →  chain-of-verification
Hierarchical structure     →  least-to-most-prompting
Multiple perspectives      →  parallel-convergence
Independent subtasks       →  strict-isolation
Complex document           →  staged-generation
```

---

## 🔗 Related Topics for PKB Expansion

### 1. **[[Templater Advanced Patterns]]**
- *Connection*: Core automation engine for SPES prompt creation
- *Depth Potential*: User scripts, conditional logic, dynamic templates
- *Knowledge Graph Role*: Technical implementation hub
- *Priority*: High - Essential for full system utilization

### 2. **[[Dataview Query Optimization]]**
- *Connection*: Powers all SPES intelligence layer queries
- *Depth Potential*: Performance tuning, complex aggregations, DataviewJS
- *Knowledge Graph Role*: Analytics infrastructure
- *Priority*: High - Critical for dashboard functionality

### 3. **[[Prompt Engineering Techniques Taxonomy]]**
- *Connection*: Theoretical foundation for component design
- *Depth Potential*: Chain-of-Thought, Few-Shot, Constitutional AI, Tree-of-Thoughts
- *Knowledge Graph Role*: Methodology reference hub
- *Priority*: Medium - Enhances component quality

### 4. **[[Knowledge Graph Theory & Practice]]**
- *Connection*: Underlying philosophy of PKB architecture
- *Depth Potential*: Link semantics, graph visualization, emergence patterns
- *Knowledge Graph Role*: Meta-level understanding
- *Priority*: Medium - Deepens system design intuition

---

*Document Version: 1.0.0 | Created: 2025-12-24 | Status: Production Ready*
*Authoritative Reference for SPES Operations*
