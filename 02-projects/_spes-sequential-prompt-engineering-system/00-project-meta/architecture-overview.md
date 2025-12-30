---
tags: #spes #project-meta #architecture #system-design
aliases: [SPES Architecture, System Design, Technical Overview]
status: reference
certainty: ^verified
created: 2025-12-16
---

# SPES Architecture Overview

> [!abstract] Purpose
> Technical architecture and system design for the Sequential Prompt Engineering System (SPES). Describes the three-pillar architecture, data flows, integration points, and implementation decisions.

---

## 🏛️ SYSTEM ARCHITECTURE

### Three-Pillar Design

```
┌─────────────────────────────────────────────────────────────┐
│                    SPES SYSTEM                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐  ┌─────────────────┐   ┌────────────┐  │
│  │   PILLAR 1:     │  │   PILLAR 2:     │   │  PILLAR 3: │  │
│  │   Component     │  │   Sequential    │   │Intelligence│  │
│  │   Library       │  │   Workflows     │   │   Layer    │  │
│  └────────┬────────┘  └────────┬────────┘   └─────┬──────┘  │
│           │                    │                  │         │
│           │      ┌─────────────┴──────────────┐   │         │
│           │      │                            │   │         │
│           └──────┤   CLAUDE LIBRARIAN         ├───┘         │
│                  │   (Orchestration Layer)    │             │
│                  └────────────┬───────────────┘             │
│                               │                             │
│                  ┌────────────┴───────────────┐             │
│                  │   PKB Foundation           │             │
│                  │   (Obsidian Vault)         │             │
│                  └────────────────────────────┘             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🏗️ PILLAR 1: COMPONENT LIBRARY

### Purpose
**Reusable, tested prompt building blocks** that can be composed into complex workflows.

### Structure

```
02-component-library/
├── atomic/                    # Single-purpose components
│   ├── personas/              # Identity/role frames
│   ├── instructions/          # Directives
│   ├── constraints/           # Restrictions
│   ├── output-formats/        # Templates
│   └── context-framers/       # Background setters
│
├── composite/                 # Multi-component workflows
│   ├── sequential-chains/     # A→B→C patterns
│   ├── parallel-branches/     # Simultaneous prompts
│   └── recursive-loops/       # Iterative refinement
│
└── specialized/               # Domain-specific templates
    ├── educational-content/   # Pedagogy-optimized
    ├── technical-analysis/    # Rigor-focused
    ├── creative-writing/      # Style-focused
    └── pkb-operations/        # Graph-aware
```

### Component Anatomy

Every component is an Obsidian note with:

```markdown
---
[Rich YAML metadata - See metadata-tagging-standards]
---

# Component Name

> [!definition] Purpose
> One-sentence description

## 🎯 When to Use
[Scenarios where this component excels]

## 🚫 When NOT to Use
[Scenarios where this component fails]

## 📝 Component Text
```
[Copy-paste ready prompt text]
```

## 🔗 Works Well With
- [[component-a]] → Synergy description

## ⚠️ Conflicts With
- [[component-b]] → Conflict description

## 📊 Performance Notes
[Testing results, success rate, quality scores]
```

### Data Flow

```
1. User Problem
     ↓
2. Claude searches component library
     ↓
3. Claude recommends relevant components
     ↓
4. User (or Claude) composes components into prompt
     ↓
5. Prompt executed
     ↓
6. Result assessed
     ↓
7. Component metadata updated (usage++, quality score)
```

### Key Design Decisions

**Decision**: Markdown files, not database
**Rationale**:
- Native Obsidian integration
- Human-readable and editable
- Version control via Git
- Leverages existing vault infrastructure

**Decision**: Rich metadata in YAML frontmatter
**Rationale**:
- Enables Dataview queries (intelligence layer)
- Machine-readable for analytics
- Future-proof for automation

**Decision**: Atomic-first decomposition
**Rationale**:
- Maximum reusability (small pieces, loosely joined)
- Easier to test and validate
- Composites built from validated atomics

---

## 🏗️ PILLAR 2: SEQUENTIAL WORKFLOWS

### Purpose
**Proven decomposition patterns** for breaking complex problems into multi-turn sequences.

### Structure

```
03-sequential-workflows/
├── decomposition-templates/       # Core patterns
│   ├── least-to-most-prompting.md
│   ├── chain-of-verification.md
│   ├── recursive-expansion-loop.md
│   ├── parallel-convergence.md
│   └── staged-generation.md
│
├── problem-types/                 # Problem → Workflow mapping
│   ├── long-form-generation.md
│   ├── technical-explanation.md
│   ├── comparative-analysis.md
│   └── research-synthesis.md
│
└── context-handoff-patterns/      # Context management
    ├── strict-isolation.md
    ├── sequential-building.md
    └── parallel-convergence.md
```

### Workflow Anatomy

Every workflow document contains:

```markdown
---
[Rich YAML metadata including problem-types, typical-turns, context-strategy]
---

# Workflow Name

## 🎯 When to Use
[Problem characteristics that match this workflow]

## 📋 Protocol
### Turn 1: [Phase Name]
**Prompt Template**: [Exact prompt structure]
**Components Used**: [[component-a]], [[component-b]]
**Expected Output**: [What you should get]

### Turn 2: [Phase Name]
[...]

## 🔀 Context Handoff Strategy
[Full context / Summary window / Sliding window / Isolation]

## 📊 Performance Data
**Success Rate**: [%]
**Typical Turns**: [N]
**Average Quality**: [X/10]

## 💡 Tips & Tricks
[Learned insights from usage]

## 🚨 Common Pitfalls
[What to avoid]
```

### Workflow Selection Algorithm

```
INPUT: Problem description + Constraints

STEP 1: Classify Problem Type
├─ Long-form generation?     → recursive-expansion-loop
├─ High accuracy required?    → chain-of-verification
├─ Hierarchical structure?    → least-to-most-prompting
├─ Multiple dimensions?       → parallel-convergence
└─ Independent sub-tasks?     → strict-isolation

STEP 2: Check Constraints
├─ Token budget?              → Influences context strategy
├─ Turn budget?               → May simplify workflow
├─ Quality threshold?         → May add verification turns
└─ Time constraint?           → May prefer simpler workflow

STEP 3: Recommend Workflow
OUTPUT: Workflow pattern + Components + Context strategy
```

### Key Design Decisions

**Decision**: Document workflows as templates, not code
**Rationale**:
- User needs flexibility to adapt
- Manual execution allows verification
- Learning happens through doing
- Automation can come later

**Decision**: Separate problem-types from patterns
**Rationale**:
- Same pattern applies to multiple problem types
- Enables "this problem is like that problem" reasoning
- Clear mapping: problem → pattern selection

**Decision**: Context-handoff as first-class concern
**Rationale**:
- Context management is critical to success
- Explicit strategies prevent instruction drift
- Documented patterns make it repeatable

---

## 🏗️ PILLAR 3: INTELLIGENCE LAYER

### Purpose
**Self-documenting metadata system** that enables discovery, analytics, and emergent intelligence.

### Structure

```
04-intelligence-layer/
├── dataview-queries/              # Discovery & analytics
│   ├── component-relationships.md
│   ├── usage-patterns.md
│   ├── performance-tracking.md
│   └── knowledge-gaps.md
│
├── 16-integration-systems/        # PKB integration protocols
│   ├── epistemic-encoding.md
│   ├── relationship-typing.md
│   ├── cognitive-load-markers.md
│   └── [... other 13 systems]
│
└── metadata-schema/               # Specifications
    ├── component-metadata-spec.md
    └── workflow-metadata-spec.md
```

### Intelligence Mechanisms

#### 1. Metadata-Driven Discovery

**Query**: "Find components for technical accuracy"
```dataview
TABLE component-type, success-rate, usage-count
FROM "02-component-library"
WHERE contains(tags, "#technical") OR contains(tags, "#accuracy")
SORT success-rate DESC, usage-count DESC
```

**Result**: Ranked list of relevant components with performance data

#### 2. Synergy Detection

**Pattern Recognition**:
```
Track: Which components used together?
Measure: Combined success rate vs individual rates
Detect: If combined > sum(individual) → Synergy
Document: Update component metadata with findings
```

**Example**:
```
[[technical-accuracy-persona]] + [[example-rich-format]]
Used together: 8 times, 100% success
Used separately: 70% success average
→ Document synergy in both component files
```

#### 3. Usage Analytics

**Automatic Tracking**:
- Component usage-count (increments on use)
- Success-rate (updates based on outcomes)
- Quality scores (averages over uses)
- Co-usage patterns (graph analysis)

**Dashboard Queries**:
- Most valuable components (usage × quality)
- Underutilized gems (high quality, low usage)
- Declining performers (quality trend down)
- Knowledge gaps (needs without components)

#### 4. Pattern Emergence

**From Usage Data** → **To System Knowledge**

```
Example Pattern Discovery:

OBSERVATION (Data):
- Workflows with verification step: 85% success
- Workflows without verification: 65% success
- Delta: +20 percentage points

INSIGHT (Analysis):
Verification steps significantly improve accuracy

ACTION (System Update):
- Add verification to default workflows
- Create [[verification-step]] component
- Document in workflow best practices
```

### Key Design Decisions

**Decision**: Dataview for queries, not custom code
**Rationale**:
- Already available in Obsidian
- Familiar to user
- No additional dependencies
- Good enough for MVP

**Decision**: Manual pattern detection initially
**Rationale**:
- Automated ML would be overkill
- Human pattern recognition is powerful
- Systematic tracking + human insight = effective
- Automation later if needed

**Decision**: Metadata as intelligence substrate
**Rationale**:
- Persists across sessions (Claude's memory)
- Enables complex queries
- Supports emergent insights
- Future-proof for advanced analytics

---

## 🧠 ORCHESTRATION LAYER: CLAUDE LIBRARIAN

### Role

Claude operates as the **intelligent orchestrator** that:
1. **Understands** user problems
2. **Searches** component library
3. **Recommends** workflows and components
4. **Executes** sequential workflows (with user)
5. **Learns** from outcomes
6. **Improves** system over time

### Operating Procedures

Defined in 7 instruction files:

1. **[[00-librarian-core-identity]]** - Who Claude is, prime directive
2. **[[01-component-management-sop]]** - How to create/modify/retire components
3. **[[02-sequential-workflow-protocols]]** - How to decompose problems
4. **[[03-context-handoff-procedures]]** - How to manage multi-turn context
5. **[[04-quality-assurance-checklist]]** - How to validate quality
6. **[[05-metadata-tagging-standards]]** - How to structure metadata
7. **[[06-usage-analytics-protocols]]** - How to track and learn

### Decision-Making Framework

```
User Request
     ↓
[Is this a SPES task?]
     ├─ YES → Switch to SPES Librarian mode
     │         Read relevant instruction files
     │         Apply SPES protocols
     │
     └─ NO → Use standard PKB Librarian mode
              Apply general CLAUDE.md protocols

Within SPES Mode:
     ↓
[Is this complex?]
     ├─ YES → Recommend decomposition
     │         Select workflow pattern
     │         Search for components
     │         Orchestrate execution
     │
     └─ NO → Recommend one-shot
              Search for single component
              Execute directly

After Execution:
     ↓
[Update metadata]
├─ Increment usage counts
├─ Log outcomes
├─ Detect patterns
└─ Update session-memory
```

---

## 🔗 INTEGRATION POINTS

### Integration 1: PKB Foundation (Obsidian)

**What**: SPES built on existing Obsidian vault infrastructure

**Integration**:
- Lives in `02-projects/_spes-sequential-prompt-engineering-system/`
- Uses standard wiki-links for connections
- Leverages Dataview for queries
- Follows PKB metadata standards (5-tag system)
- Participates in vault graph

**Benefits**:
- No separate tool/system to manage
- Native linking to other vault notes
- Existing workflows (Git, backups, etc.)
- Familiar interface

### Integration 2: Session Memory System

**What**: SPES state persists in `00-meta/` files

**Integration**:
```
00-meta/
├── session-memory.md      → Current session context
├── project-tracker.md     → Active SPES tasks
├── user-preferences.md    → Workflow patterns
└── vault-map.md          → Structural insights
```

**Protocol**:
- Claude reads memory files at session start
- Claude updates memory files after significant work
- Memory provides context continuity across sessions

### Integration 3: Diagnostic Tools

**What**: Vault health scripts support SPES quality assurance

**Tools**:
- `vscan` → Anti-duplication (search before creating)
- `orphan` → Graph health (≥2 in, ≥2 out)
- `linkcheck` → Link integrity (no broken links)
- `metaudit` → Metadata compliance (5-tag system)

**Usage in SPES**:
- Run before creating components (avoid duplication)
- Run after creating components (verify quality)
- Run periodically (maintain system health)

### Integration 4: Existing Prompt Work

**What**: Migrate existing prompts into SPES structure

**Sources**:
- `02-projects/_project-prompt-engineering/` → Sequential patterns
- `000_databsae/` → Existing prompt components
- User's copilot prompts → Can be atomized into components

**Migration Strategy**:
1. Analyze existing prompt for atomic components
2. Extract reusable pieces as atomic components
3. Document as workflow pattern if sequential
4. Test and validate
5. Mark originals as archived with link to SPES version

---

## 📊 DATA FLOWS

### Flow 1: Component Creation

```
1. User/Claude identifies need for new component
2. Claude searches existing (vscan)
3. If not exists: Claude creates component file
4. Component includes rich metadata
5. Component linked to related components (≥2 outgoing)
6. Metadata validated (metaudit)
7. Graph connectivity validated (orphan check)
8. Component marked status: seedling
9. Component ready for testing
```

### Flow 2: Workflow Execution

```
1. User presents problem
2. Claude classifies problem type
3. Claude recommends workflow pattern
4. Claude searches components for workflow
5. Claude presents workflow + components
6. User approves or adjusts
7. Execute Turn 1 with selected components
8. Assess output quality
9. Execute Turn 2 with context handoff
10. Repeat through final turn
11. Log results (usage counts, quality scores)
12. Update component metadata
13. Detect patterns if applicable
```

### Flow 3: Pattern Detection

```
1. Usage data accumulates (metadata updates)
2. Claude or user runs analytics queries
3. Patterns emerge (synergies, conflicts, trends)
4. Patterns documented as insights
5. System updated based on insights:
   ├─ Component metadata updated
   ├─ New composite components created
   ├─ Workflow recommendations adjusted
   └─ SOPs refined if needed
6. Patterns validated through continued usage
7. Loop continues (system improves)
```

---

## 🔐 QUALITY ASSURANCE

### Quality Gates

**Component Quality**:
- ✅ Metadata 100% compliant
- ✅ Graph connected (≥2 in, ≥2 out)
- ✅ No broken links
- ✅ Unit tested (isolation)
- ✅ Integration tested (with ≥2 others)
- ✅ Used successfully in ≥1 workflow

**Workflow Quality**:
- ✅ Documented with examples
- ✅ System tested (≥3 real problems)
- ✅ Success rate ≥70%
- ✅ Context strategy specified
- ✅ Component dependencies documented

**System Quality**:
- ✅ Metadata compliance >90%
- ✅ Orphan rate <20%
- ✅ Broken link rate <10%
- ✅ Analytics dashboards functional
- ✅ Session memory updated regularly

### Testing Levels

```
Level 1: Unit Tests (Individual Components)
├─ Syntax validation
├─ Isolation test (component alone)
└─ Edge case handling

Level 2: Integration Tests (Component Combinations)
├─ Synergy validation
├─ Conflict detection
└─ Order sensitivity testing

Level 3: System Tests (Full Workflows)
├─ Real problem scenarios
├─ Quality vs one-shot baseline
└─ Reproducibility check

Level 4: System Health (Overall SPES)
├─ Metadata compliance scan
├─ Graph health analysis
└─ Usage pattern validation
```

---

## 🚀 SCALABILITY CONSIDERATIONS

### Current Scale (Phase 1)

- **Components**: 10-50
- **Workflows**: 5-10
- **Users**: 1
- **Queries**: Manual Dataview
- **Storage**: Markdown files

**Performance**: Excellent (instant search, lightweight)

### Medium Scale (Phase 2-3)

- **Components**: 50-200
- **Workflows**: 10-30
- **Users**: 1-3
- **Queries**: Complex Dataview
- **Storage**: Markdown files

**Performance**: Good (Dataview may slow at complex queries)
**Optimization**: Index commonly-used queries, cache results

### Large Scale (Future)

- **Components**: 200-1000+
- **Workflows**: 30-100+
- **Users**: Multiple
- **Queries**: May need database
- **Storage**: Hybrid (Markdown + DB?)

**Performance**: May degrade without optimization
**Solutions**:
- Database backend for analytics
- API layer for queries
- Caching strategy
- Search index

**Current Decision**: Optimize for Phase 1-2 scale, revisit if needed

---

## 🔮 FUTURE ENHANCEMENTS

### Potential Additions (Not Current Scope)

1. **Automated Multi-Turn Execution**
   - API integration to run workflows automatically
   - Context management handled programmatically
   - User reviews final output only

2. **Component Generator**
   - Templates for common component types
   - Guided creation with validation
   - Auto-metadata population

3. **Advanced Analytics**
   - ML-based pattern detection
   - Predictive recommendations
   - Quality forecasting

4. **MCP Integration**
   - External tool access during workflows
   - Web search, code execution, etc.
   - Expanded capability space

5. **Multi-Domain Expansion**
   - Apply SPES to research synthesis
   - Apply SPES to creative writing
   - Apply SPES to data analysis
   - Generic sequential problem-solving framework

6. **Collaboration Features**
   - Shared component libraries
   - Community patterns
   - Rating/review systems

---

## 🔗 RELATED DOCUMENTATION

- [[project-charter]] → Vision, objectives, success criteria
- [[implementation-roadmap]] → Phased execution plan
- [[01-claude-librarian-instructions/]] → Operational procedures
- [[00-meta/project-tracker]] → Current task status

---

*Architecture Version: 1.0 | Last Updated: 2025-12-16*
