---
memory-type: core
created: 2026-01-06
modified: 2026-01-06
project: pkb-vault-operations
tags: [#memory-system, #core, #architecture, #patterns, #design-decisions]
confidence: verified
status: active
---

# System Patterns & Architecture Decisions

> [!abstract] Architectural Foundation
> This document captures the fundamental architecture patterns, design decisions, and system principles governing the vault's structure. It serves as the single source of truth for "how and why" things are built the way they are.

## Context

This vault implements a **Meta-Cognitive PKB Architecture** that bridges human knowledge management with AI agent memory systems. The architecture decisions documented here enable:
- Persistent cross-session context for agents
- Semantic retrieval via embeddings
- Multi-LLM coordination
- Knowledge graph navigation

%%QA:architecture:meta-cognitive-pkb%%
The Meta-Cognitive PKB Architecture combines human-readable knowledge management with agent-accessible memory structures through dual-layer design and semantic retrieval integration.

---

## Core Architectural Patterns

### 1. Dual-Layer Memory Architecture

**Pattern**: Complementary Separation

**Structure**:
```
Vault Root/
├── 00-meta/           ← Authoritative Metadata Layer
│   ├── session-memory.md
│   ├── project-tracker.md
│   ├── user-preferences.md
│   └── vault-map.md
│
└── .claude/           ← Agent-Optimized Memory Layer
    ├── core/          (Long-Term Memory)
    ├── task-logs/     (Short-Term Memory)
    ├── plans/         (Working Memory)
    └── errors/        (Error Memory)
```

**Rationale**:
- `00-meta/` = **Human-First Design**
  - Authoritative source for vault metadata
  - Readable documentation
  - System-level configuration
  - Project tracking and user preferences

- `.claude/` = **Agent-First Design**
  - Semantic search optimized (query anchors)
  - MCP-accessible for automated retrieval
  - Granular task logging
  - Event-driven automation hooks

**Trade-offs**:
- ✅ Clear separation of concerns
- ✅ Preserves existing 00-meta structure
- ✅ Agent-optimized without human overhead
- ⚠️ Potential duplication (mitigated via cross-references)

**Decision Date**: 2026-01-06

**Status**: ✅ Implemented

%%QA:architecture:dual-layer%%
Dual-layer architecture separates authoritative human metadata (00-meta/) from agent-optimized memory (.claude/) to optimize for both human navigation and AI semantic retrieval.

---

### 2. Three-Layer Memory Hierarchy

**Pattern**: Time-Based Memory Stratification

**Layers**:

**Layer 1: Long-Term Memory** (`.claude/core/`)
- **Persistence**: Permanent, rarely deleted
- **Update Frequency**: Infrequent (architectural changes only)
- **Purpose**: Strategic context, architectural decisions
- **Files**: [[projectbrief]], [[systemPatterns]], [[techContext]], [[activeContext]], [[progress]]

**Layer 2: Short-Term Memory** (`.claude/task-logs/`)
- **Persistence**: 30-day rolling window
- **Update Frequency**: Per-task (high frequency)
- **Purpose**: Detailed execution logs, decision tracking
- **Format**: `YYYY-MM-DD-HH-MM_task-description.md`

**Layer 3: Working Memory** (`.claude/plans/`)
- **Persistence**: Session-duration or until task completion
- **Update Frequency**: Real-time during planning
- **Purpose**: Active analysis, draft implementations
- **Cleanup**: Archived or deleted post-completion

%%QA:architecture:memory-layers%%
Three-layer memory hierarchy organizes information by persistence duration: long-term core files (permanent), short-term task logs (30-day rolling), and working memory plans (session-duration).

**Rationale**:
- Mirrors human memory systems (Long-Term, Short-Term, Working)
- Enables efficient pruning (task-logs older than 30 days)
- Prevents core memory bloat
- Supports temporal queries ("What was decided last week?")

**Trade-offs**:
- ✅ Prevents information overload
- ✅ Automatic cleanup possible
- ⚠️ Requires discipline to maintain boundaries

**Decision Date**: 2026-01-06

**Status**: ✅ Structure created, automation pending

---

### 3. Semantic Retrieval via Smart Connections + MCP

**Pattern**: Auto-Embedding with Protocol Bridge

**Architecture**:
```
Agent Request
      ↓
MCP Server (ob-smart-connections-mcp)
      ↓
Smart Connections Plugin (Obsidian)
      ↓
Embeddings (.smart-env/multi/)
      ↓
Query Results (ranked by similarity)
```

**Components**:

1. **Smart Connections Plugin**
   - Model: TaylorAI/bge-micro-v2 (local, 384 dimensions)
   - Auto-embeds on file save
   - Stores embeddings as AJSON in `.smart-env/multi/`

2. **MCP Server**
   - Bridge between agents and Smart Connections
   - Provides `lookup`, `connection`, `stats`, `validate` tools
   - Configured in Claude Desktop config

3. **Query Anchor Protocol**
   - Syntax: `%%QA:domain:specific-topic%%`
   - Creates semantic search landmarks
   - Enables precise retrieval

%%QA:architecture:semantic-retrieval%%
Semantic retrieval uses Smart Connections for auto-embedding with MCP server as protocol bridge, enabling agents to query vault content by meaning rather than keywords.

**Rationale**:
- Traditional search (keywords) misses conceptual connections
- Embeddings capture semantic similarity
- MCP provides standardized agent interface
- Query anchors enable precision when needed

**Trade-offs**:
- ✅ Discovers non-obvious connections
- ✅ Works across terminology variations
- ⚠️ Embedding generation has 30-second latency
- ⚠️ Requires Obsidian running for indexing

**Decision Date**: 2026-01-06

**Status**: ⚙️ MCP configuration pending

---

### 4. Query Anchor Protocol

**Pattern**: Semantic Landmarks for Precision Retrieval

**Syntax**: `%%QA:domain:specific-topic%%`

**Namespacing Guidelines**:
- `%%QA:architecture:*%%` — System design decisions
- `%%QA:memory:*%%` — Memory system specifics
- `%%QA:errors:*%%` — Error patterns and solutions
- `%%QA:workflow:*%%` — Process and methodology
- `%%QA:tools:*%%` — Technology and tool usage
- `%%QA:strategy:*%%` — Strategic context and goals
- `%%QA:success:*%%` — Success metrics and outcomes

**Example Implementation**:
```markdown
%%QA:architecture:embedding-model%%
Smart Connections uses TaylorAI/bge-micro-v2 model for local embedding generation.
Dimensions: 384, stored as AJSON in .smart-env/multi/ directory.
```

%%QA:retrieval:query-anchors%%
Query anchors use %%QA:domain:topic%% format to create semantic search landmarks. Namespacing by domain enables precise retrieval of specific knowledge areas without keyword ambiguity.

**Rationale**:
- Enhances semantic search with precision targeting
- Organizes knowledge by domain
- Enables cross-project pattern extraction
- Complements embedding-based similarity search

**Trade-offs**:
- ✅ Precise retrieval when needed
- ✅ Self-documenting knowledge organization
- ⚠️ Requires manual anchor placement
- ⚠️ Over-use can create noise

**Decision Date**: 2026-01-06

**Status**: ✅ Protocol defined, implementation in progress

---

### 5. Document Chain Navigation

**Pattern**: Linked Learning Paths

**Implementation**: Notes link to "next logical documents" via:
- `Related Topics` sections
- `link-related` frontmatter field
- Explicit next-step guidance

**Example Chain**:
```
[[projectbrief]]
  → [[systemPatterns]]
    → [[techContext]]
      → [[activeContext]]
```

%%QA:workflow:document-chains%%
Document chains create learning paths where each note links to the next logical document, enabling cumulative context building through sequential reading.

**Rationale**:
- Mirrors human learning (cumulative context)
- Guides agents through complex topics
- Prevents context gaps
- Enables verification (follow chain to validate understanding)

**Trade-offs**:
- ✅ Clear navigation paths
- ✅ Progressive disclosure of complexity
- ⚠️ Requires maintenance as structure evolves

**Decision Date**: Inherited from [[__LOCAL-REPO/CLAUDE]] system prompt

**Status**: ✅ Implemented via Related Memories sections

---

### 6. Wiki-Link Graph Building

**Pattern**: High-Density Semantic Network

**Guidelines**:
- Every note has 2+ [[wiki-link|Wiki-Links]] in and out
- Concepts mentioned ≥2 times become links
- Over-link toward graph density (err on side of more links)
- Orphan notes <5% of total

**Target Densities**:
- Simple notes: 3-8 links
- Reference notes: 15-40 links
- MOCs: 20-50+ links

%%QA:architecture:wiki-link-density%%
Wiki-link density target is 2+ links in and out for every note, with reference notes having 15-40 links to create a navigable knowledge graph.

**Rationale**:
- Enables graph-based navigation
- Surfaces unexpected connections
- Facilitates Obsidian graph view
- Supports semantic search (links indicate relatedness)

**Trade-offs**:
- ✅ Rich interconnections
- ✅ Serendipitous discovery
- ⚠️ Can become maintenance overhead

**Decision Date**: Inherited from [[__LOCAL-REPO/CLAUDE]] principles

**Status**: ✅ Active policy

---

## Multi-LLM Coordination Patterns

### 7. Claude + Gemini Complementary Roles

**Pattern**: Strengths-Based Delegation

**Role Distribution**:

**[[Claude-Code]]**:
- **Strengths**: Extended thinking, nuanced language, system prompts
- **Responsibilities**:
  - Complex reasoning and planning
  - Long-form content generation
  - Cross-domain synthesis
  - Prompt engineering
  - Architecture design

**[[Gemini-Code-Assist]]**:
- **Strengths**: Structured reasoning, code execution, quick iterations
- **Responsibilities**:
  - Technical documentation
  - Code generation
  - Task decomposition
  - Implementation execution
  - Testing and validation

%%QA:workflow:multi-llm-coordination%%
Claude and Gemini coordinate via complementary roles: Claude handles complex reasoning and architecture, while Gemini executes structured tasks and code generation. Shared memory via 00-meta/session-memory.md enables hand-offs.

**Hand-off Protocol**:
1. Outgoing LLM updates [[00-meta/system/session-memory]]
2. Documents current state, what's complete, blockers
3. Specifies what incoming LLM should work on
4. Incoming LLM reads session-memory, acknowledges handoff
5. Continues from documented state

**Rationale**:
- Leverages unique strengths
- Prevents task duplication
- Enables parallel work on independent tasks
- Shared memory maintains continuity

**Trade-offs**:
- ✅ Optimal use of each LLM's capabilities
- ✅ Faster completion via parallelization
- ⚠️ Requires clear hand-off documentation

**Decision Date**: Inherited from user's multi-LLM setup

**Status**: ✅ Active pattern

---

## Data Management Patterns

### 8. Metadata Standardization

**Pattern**: Unified Frontmatter Schema

**Standard Format**:
```yaml
---
memory-type: [core | task-log | plan | error]
created: YYYY-MM-DD
modified: YYYY-MM-DD
project: project-identifier
tags: [#domain, #type, #status]
confidence: [speculative | provisional | moderate | established | verified]
status: [active | completed | deprecated]
---
```

%%QA:memory:metadata-schema%%
Standardized metadata schema ensures consistent frontmatter across all memory files with fields for memory-type, dates, project, tags, confidence level, and status.

**Rationale**:
- Enables automated queries via [[Dataview]]
- Consistent structure aids agents
- Confidence levels track knowledge maturity
- Status tracking prevents stale information

**Trade-offs**:
- ✅ Queryable metadata
- ✅ Consistent structure
- ⚠️ Overhead for every file

**Decision Date**: 2026-01-06

**Status**: ✅ Defined, implementation in progress

---

### 9. Task Log Retention (30-Day Rolling Window)

**Pattern**: Automatic Pruning

**Implementation**:
- Task logs in `.claude/task-logs/`
- Retention: 30 days
- Format: `YYYY-MM-DD-HH-MM_task-description.md`
- Automated cleanup script (planned)

%%QA:memory:task-log-retention%%
Task logs use a 30-day rolling window to prevent memory bloat while maintaining recent context. Automated cleanup script planned for Phase 4.

**Rationale**:
- Prevents memory bloat
- Recent context (30 days) sufficient for most queries
- Important decisions migrate to core files
- Old logs rarely referenced

**Trade-offs**:
- ✅ Bounded memory growth
- ✅ Automatic cleanup possible
- ⚠️ Permanent loss after 30 days (mitigated: important info moved to core)

**Decision Date**: 2026-01-06

**Status**: 📝 Policy defined, automation pending (Phase 4)

---

## Formatting & Presentation Patterns

### 10. Obsidian Formatting Stack

**Pattern**: Production-Ready Markdown

**Components** (from [[__LOCAL-REPO/CLAUDE]] system prompt):

1. **Metadata Headers** (YAML frontmatter)
2. **Wiki-Links** (`[[like-this]]`)
3. **Semantic Callouts** (`> [!type]`)
4. **Semantic Color Coding** (HTML spans with hex colors)
5. **Dataview Inline Fields** (`[**Field**:: value]`)

%%QA:tools:formatting-stack%%
Formatting stack includes YAML frontmatter, Wiki-Links, semantic callouts, color coding with HTML spans, and Dataview inline fields for queryable content.

**Rationale**:
- Native Obsidian compatibility
- Enhanced readability
- Dataview query support
- Semantic structure aids understanding

**Trade-offs**:
- ✅ Rich, structured content
- ✅ No post-processing needed
- ⚠️ More verbose than plain markdown

**Decision Date**: Inherited from [[__LOCAL-REPO/CLAUDE]] principles

**Status**: ✅ Active policy

---

## Error Handling & Recovery Patterns

### 11. Error Memory System

**Pattern**: Learn from Failures

**Structure**:
- Location: `.claude/errors/`
- Format: `YYYY-MM-DD_error-type.md`
- Contents: Error trace, root cause analysis, resolution steps

**Template**:
```markdown
# Error: [Description]

## Context
What was being attempted?

## Error Details
Trace, logs, symptoms

## Root Cause
Why did this happen?

## Resolution
How was it fixed?

## Prevention
How to avoid in future?

## Related Patterns
- [[systemPatterns]] — architectural changes needed?
- [[techContext]] — tooling issues?
```

%%QA:errors:error-memory%%
Error memory system logs failures in .claude/errors/ with trace, root cause, resolution, and prevention guidance to enable learning from mistakes.

**Rationale**:
- Prevents repeating failures
- Builds institutional knowledge
- Patterns emerge from multiple errors
- Agents learn from past mistakes

**Trade-offs**:
- ✅ Cumulative learning
- ✅ Pattern recognition
- ⚠️ Requires discipline to document

**Decision Date**: 2026-01-06

**Status**: ✅ Structure created, awaiting first error

---

## Related Memories

- [[projectbrief]] — Strategic context and goals
- [[techContext]] — Technology implementations of these patterns
- [[activeContext]] — Current implementation status
- [[progress]] — Architecture evolution timeline
- [[memory-index]] — Navigation hub

---

## Query Anchors Summary

This document contains query anchors for:
- `%%QA:architecture:*%%` — All architectural patterns
- `%%QA:workflow:*%%` — Process and coordination
- `%%QA:memory:*%%` — Memory system specifics
- `%%QA:retrieval:*%%` — Semantic search patterns
- `%%QA:tools:*%%` — Technology implementations
- `%%QA:errors:*%%` — Error handling

---

## Document History

- **2026-01-06**: Initial creation, documented 11 core patterns
- **Status**: Active, evolving as patterns emerge

---

_This is a living document. Update when architectural decisions change or new patterns emerge._
