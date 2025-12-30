---
# === LEGACY METADATA (Preserved) ===
type: prompt-component
id: "20251212205052"
status: active
version: 2.0.0
rating: "8.2"
source: pur3v4d3r
title: "Generate Dataview Query Reference (Comprehensive)"
description: "Instruction component that directs LLM to generate comprehensive collections of Dataview queries, inline queries, and DataviewJS for index notes/dashboards. Produces reference compendiums rather than explanations."
key-takeaway: "Specialized generator for Dataview query collections - focuses on breadth and variety rather than explanatory depth. Produces immediately usable code snippets."
last-used: "[[2025-12-12]]"
tags:
  - year/2025
  - llm-capability/generation
  - prompt-workflow/deployment
  - prompt-pattern
  - prompt-engineering/anatomy
  - spes/atomic
  - spes/instruction
  - obsidian/dataview
aliases:
  - Dataview Query Generator
  - Dataview Reference Builder
  - Index Note Query Collection
  - Dashboard Query Compendium
link-up: "[[moc-agentic-instruction-sets-2025117044009]]"
link-related:
  - "[[format-inline-field-definitions-v1.0.0]]"
  - "[[claude-system-instructions-pkb-architect-v2.0.0]]"
  - "[[02-projects/_spes-sequential-prompt-engineering-system/02-component-library/atomic/instructions/]]"

# === SPES METADATA (Added) ===
component-type: atomic
component-category: instruction
atomic-type: instruction

# Intelligence Layer
concepts::
  - "[[Dataview]]"
  - "[[DataviewJS]]"
  - "[[Inline Queries]]"
  - "[[Query Generation]]"
  - "[[Index Notes]]"
  - "[[Dashboard Design]]"
  - "[[Obsidian Automation]]"
  - "[[Reference Generation]]"
  - "[[Code Snippet Collections]]"
  - "[[PKB Intelligence Layer]]"

use-cases::
  - Generating comprehensive Dataview query reference libraries
  - Building index note dashboards with pre-built queries
  - Creating folder-specific analytics queries
  - Assembling Dataview snippet collections for documentation
  - Exploring advanced/novel Dataview use cases
  - Producing queryable metadata patterns for PKB

synergies::
  - "[[format-inline-field-definitions-v1.0.0]]"
  - "[[claude-system-instructions-pkb-architect-v2.0.0]]"
  - "[[gemini-system-instructions-pkb-architect-v1.0.0]]"
  - "[[instruction-pkb-research-methodology-v1.0.0]]"

conflicts::
  - "[[instruction-brevity-first-responses]]"
  - "[[constraint-no-code-blocks]]"

prerequisites: []

performance-notes::
  - Quality: Produces high-quality, working Dataview queries (8-9 rating)
  - Speed: Fast generation due to code-focused output (no prose overhead)
  - Consistency: Very consistent query syntax and formatting
  - Breadth: Excellent variety (20-40 unique query patterns per use)
  - Novelty: Strong at generating advanced/creative Dataview patterns

# Analytics
usage-frequency: 8
success-rate: 0.88
avg-quality-score: 8.2
last-modified: "[[2025-12-12]]"
times-iterated: 1
migration-date: "[[2025-12-17]]"

# Problem-Type Mapping
problem-types::
  - Generating Dataview query reference libraries for PKB
  - Creating index note dashboards with automated queries
  - Building folder analytics and metadata queries
  - Producing comprehensive query snippet collections
  - Exploring novel Dataview use cases and patterns
  - Documenting Dataview capabilities with working examples

# Workflow position - typically used after system instructions
workflow-position: middle

test-status: passing
test-cases: 3
validation-method: manual
known-limitations::
  - Generates queries without explanatory prose (by design - trade-off for breadth)
  - May produce queries that require customization for specific vault structures
  - Does not validate query performance on large vaults
  - Assumes familiarity with Dataview syntax (not tutorial-focused)
  - Limited to Dataview plugin capabilities (no custom plugin integration)
---

> [!spes-component]
> ### SPES Component Metadata
>
> **Component-ID**: 20251212205052
> **Component-Type**: atomic | instruction
> **Version**: 2.0.0
> **Status**: active
> **Rating**: 8.2/10
>
> **Usage Stats**:
>
> - **Times Used**: 8
> - **Success Rate**: 88%
> - **Avg Quality**: 8.2/10
>
> **Workflow Position**: middle
> **Test Status**: passing (3 test cases)

> [!abstract] Component Purpose
> This atomic instruction component directs the LLM to generate **comprehensive Dataview query collections** rather than explanatory guides. It emphasizes breadth over depth, producing working code snippets for index notes, dashboards, and folder analytics. Optimized for building reference libraries of immediately usable Dataview patterns.

---

## 🎯 When to Use This Component

**Ideal Scenarios**:
- ✅ Building **index note dashboards** with pre-built query collections
- ✅ Creating **Dataview reference libraries** for vault documentation
- ✅ Generating **folder-specific analytics** queries
- ✅ Exploring **novel/advanced** Dataview use cases
- ✅ Producing **snippet collections** for quick copy-paste
- ✅ Documenting **Dataview capabilities** with working examples

**Suboptimal Scenarios**:
- ❌ Learning Dataview syntax (use tutorial-focused prompts instead)
- ❌ Generating single-purpose queries (this produces collections)
- ❌ Requiring extensive prose explanations (this is code-focused)
- ❌ Non-Dataview query needs (SQL, GraphQL, etc.)

---

## 🧩 Component Architecture

### Core Directives

**Goal Section** (Lines 112-114):
- Defines output type: **Comprehensive resource/compendium**
- Specifies query types: Dataview, Inline, DataviewJS
- Target use case: Index notes and dashboards

**Task Section** (Lines 115-120):
- Emphasizes **breadth** ("cover as many areas as you can")
- Clarifies output format: **Collection, not explanation**
- Requests **novel/advanced use cases**
- Defines purpose: Reference for building index notes

**Exemplar Section** (Lines 121-147):
- Provides 3 working query examples:
  1. **Basic table**: File creation/modification dates
  2. **Metrics aggregation**: Folder statistics (total, new, modified)
  3. **Orphan detection**: Notes without inlinks

### Design Pattern

This component uses the **exemplar-based instruction** pattern:
1. Set high-level goal (comprehensive collection)
2. Define task scope (breadth, variety, novelty)
3. Provide exemplars (working code samples)
4. Let LLM extrapolate to full collection

**Advantage**: Produces 20-40 unique queries from 3 examples through pattern recognition.

---

## 📊 Query Categories Generated

When this component is used, typical output includes queries across these categories:

### 1. Folder Analytics
- Total notes in folder
- Recent activity (created/modified in last N days)
- File size distributions
- Tag frequency analysis

### 2. Network Analysis
- Orphaned notes (no inlinks)
- Hub notes (high inlink count)
- Broken links detection
- Cross-folder link patterns

### 3. Temporal Queries
- Notes by creation date
- Staleness detection (old, unmodified)
- Activity timelines
- Date range filters

### 4. Metadata Aggregation
- Tag clouds/distributions
- Status tracking (in-progress, complete, etc.)
- Rating/priority rankings
- Custom field summaries

### 5. Advanced DataviewJS
- Semantic bridge detection (shared context)
- Dynamic graph visualizations
- Conditional formatting
- Complex aggregations

---

## 🔗 SPES Integration Points

**Prerequisites**: None (standalone instruction)

**Synergies**:
- [[format-inline-field-definitions-v1.0.0]] - Queries can target inline fields generated by this format
- [[claude-system-instructions-pkb-architect-v2.0.0]] - Combine for Dataview-enhanced reference notes
- [[gemini-system-instructions-pkb-architect-v1.0.0]] - Gemini equivalent for cross-model testing
- [[instruction-pkb-research-methodology-v1.0.0]] - Research pattern that benefits from query libraries

**Conflicts**:
- [[instruction-brevity-first-responses]] - This component favors comprehensive collections
- [[constraint-no-code-blocks]] - Output is code-heavy by design

---

## 📝 Usage Examples

### Example 1: Basic Index Note Dashboard

**Workflow**:
1. Apply [[claude-system-instructions-pkb-architect-v2.0.0]] for formatting
2. Apply this component
3. Request: "Generate Dataview query collection for folder index note"

**Expected Output**:
- 15-25 unique queries
- Categories: folder metrics, recent activity, network analysis
- Mix of Dataview and DataviewJS
- Ready to paste into index note

### Example 2: Advanced Analytics Dashboard

**Workflow**:
1. Apply this component
2. Request: "Generate advanced DataviewJS queries for knowledge graph analytics"

**Expected Output**:
- 10-15 DataviewJS queries
- Focus: semantic bridges, hub detection, orphan analysis
- Novel patterns: community detection, topic clustering

### Example 3: Temporal Activity Dashboard

**Workflow**:
1. Apply this component
2. Request: "Generate Dataview queries for tracking PKB activity over time"

**Expected Output**:
- 12-18 temporal queries
- Daily/weekly/monthly activity metrics
- Staleness detection
- Heatmap data structures

---

## 🧪 Test Cases

### Test 1: Basic Query Collection (PASSING)
**Input**: "Generate Dataview query collection for folder index note"
**Expected**: 20+ queries, folder-focused, mix of Dataview/DataviewJS
**Result**: ✅ 23 queries, folder metrics, activity, orphans, hub detection

### Test 2: Advanced DataviewJS Patterns (PASSING)
**Input**: "Generate advanced DataviewJS queries for semantic analysis"
**Expected**: 10+ DataviewJS queries, graph analysis, novel patterns
**Result**: ✅ 12 queries, semantic bridges, community detection, tag co-occurrence

### Test 3: Inline Query Compendium (PASSING)
**Input**: "Generate Dataview inline query reference for note templates"
**Expected**: 15+ inline queries using `= ` syntax
**Result**: ✅ 18 inline queries, metadata displays, dynamic calculations

---

## 🚧 Known Limitations

1. **No Explanatory Prose**
   - Generates queries without detailed explanations (by design)
   - **Mitigation**: Pair with [[claude-system-instructions-v2.0.0]] if context needed

2. **Vault Structure Assumptions**
   - Queries may assume specific folder/tag structures
   - **Mitigation**: Test and customize queries for your vault

3. **Performance Not Validated**
   - No testing on large vaults (1000+ notes)
   - Complex DataviewJS may be slow
   - **Mitigation**: Profile queries before deploying to production dashboards

4. **Syntax Familiarity Required**
   - Assumes user understands Dataview syntax
   - Not tutorial-focused
   - **Mitigation**: Consult Dataview documentation for syntax reference

5. **Limited Plugin Integration**
   - Focuses on core Dataview capabilities
   - Does not integrate with other plugin APIs
   - **Mitigation**: Manually extend queries with plugin-specific features

---

## 🔗 Related Topics for PKB Expansion

1. **[[Dataview Query Optimization Patterns]]**
   - *Connection*: Performance tuning for queries generated by this component
   - *Depth Potential*: Profiling, caching strategies, query complexity analysis
   - *Knowledge Graph Role*: Links query generation to vault performance management

2. **[[Index Note Architecture Patterns]]**
   - *Connection*: Dashboard designs that use these query collections
   - *Depth Potential*: Layout templates, visual hierarchy, query organization
   - *Knowledge Graph Role*: Bridges queries to structural PKB patterns

3. **[[DataviewJS Advanced Techniques]]**
   - *Connection*: Deep dive into JavaScript capabilities within Dataview
   - *Depth Potential*: Custom rendering, API integration, complex algorithms
   - *Knowledge Graph Role*: Extends Dataview capabilities beyond this component's scope

4. **[[PKB Intelligence Layer Design]]**
   - *Connection*: How Dataview queries form the intelligence/analytics layer of PKB
   - *Depth Potential*: Metadata architecture, query-driven workflows, dashboard ecosystems
   - *Knowledge Graph Role*: High-level framework for automated PKB insights

---

## 📦 Component Source

```prompt-component
----
Prompt-Component-ID: "2025121220"
Prompt-Component-Version: 2.0.0
----

<goal>
Comprehensive Resource that contains a collection of Dataview Queries, Dataview Inline Queries and Advanced Dataviejs Queries. Specifically, for use within an "indexing note", for me to use around my PKB.
</goal>

<task>
I need a comprehensive resource that covers all available "Dataview Queries", "Dataview Inline Queries" and "Advanced Dataviejs Queries" pertaining to Index Note Dashboards.

This reference isn't about these types of queries, it's a comprehensive resource/compendium that encompasses all known queries of this type that you find while conducting your tree of thoughts search.

I require you to cover as many areas as you can. My main purpose is to amass a collection of these, to pull from, as a resource to build various index notes/dashboards, that display information pertaining to the folder the notes are contained and links between the notes in the folder, among other novel uses.

Side Note: I'm also very interested to know what novel/advanced use cases there are.
</task>

<exemplar>
```dataview
TABLE file.ctime AS "Date Created", file.mtime AS "Last Modified"
FROM ""
WHERE file.folder = this.file.folder AND file.name != this.file.name
SORT file.name ASC
```

```dataview
TABLE WITHOUT ID
  length(rows) AS "Total Notes in Folder",
  length(filter(rows, (r) => date(r.file.ctime) >= date(today) - dur(7 days))) AS "New Notes (Last 7 Days)",
  length(filter(rows, (r) => date(r.file.mtime) >= date(today) - dur(7 days))) AS "Modified Notes (Last 7 Days)"
FLATTEN file.mtime as modified
WHERE file.folder = this.file.folder AND file.name != this.file.name
GROUP BY "Folder Metrics"
```

```dataview
TABLE WITHOUT ID
  file.link AS "Orphaned Note",
  length(file.outlinks) AS "Links Out"
FROM ""
WHERE file.folder = this.file.folder
  AND length(file.inlinks) = 0
  AND file.name != this.file.name
SORT file.name ASC
```
</exemplar>
```

---

*Migration Date: [[2025-12-17]] | Source: Legacy component library | Status: Production-ready*
