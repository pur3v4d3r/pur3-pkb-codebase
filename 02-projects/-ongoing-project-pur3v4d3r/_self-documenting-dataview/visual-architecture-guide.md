# 🗺️ Self-Documenting Knowledge System: Visual Architecture Guide

---
tags: #pkm #system-architecture #visual-guide #dataview #reference-note
aliases: [System Architecture Overview, Visual Reference Guide, Self-Documenting System Map]
---

> [!abstract] Document Purpose
> This visual reference provides **architectural diagrams**, **workflow maps**, and **decision trees** for understanding and implementing the self-documenting knowledge system. Use this as a companion to the implementation guides when you need to see "the big picture" or understand how components interact.

---

## 🏗️ System Architecture: Three-Layer Model

```mermaid
graph TB
    subgraph "Layer 1: Foundation (Universal)"
        A1[Self-Discovery<br/>Query Pattern]
        A2[Progress<br/>Tracking]
        A3[Relationship<br/>Mapping]
    end
    
    subgraph "Layer 2: Configuration (Domain-Specific)"
        B1[Taxonomy<br/>Definition]
        B2[Metadata<br/>Schema]
        B3[Folder<br/>Structure]
        B4[Status<br/>Tasks]
    end
    
    subgraph "Layer 3: Implementation (Content)"
        C1[Concept<br/>Notes]
        C2[Application<br/>Notes]
        C3[Synthesis<br/>Notes]
        C4[MOC<br/>Notes]
    end
    
    A1 --> B2
    A2 --> B4
    A3 --> B3
    
    B1 --> C1
    B2 --> C2
    B3 --> C3
    B4 --> C4
    
    C2 -.Automatically<br/>appears in.-> C1
    
    style A1 fill:#e1f5ff
    style A2 fill:#e1f5ff
    style A3 fill:#e1f5ff
    style B1 fill:#fff4e1
    style B2 fill:#fff4e1
    style B3 fill:#fff4e1
    style B4 fill:#fff4e1
    style C1 fill:#e1ffe1
    style C2 fill:#e1ffe1
    style C3 fill:#e1ffe1
    style C4 fill:#e1ffe1
```

> [!definition]
> **Layer 1 (Foundation)**: Core mechanics that work identically across ALL domains. These never change.
>
> **Layer 2 (Configuration)**: Domain-specific settings and schemas. Customize once per domain.
>
> **Layer 3 (Implementation)**: Your actual content - concepts, applications, synthesis. Grows continuously.

---

## 🔄 The Intelligence Loop: How Self-Discovery Works

```mermaid
sequenceDiagram
    participant U as You (User)
    participant A as Application Note
    participant C as Concept Note
    participant D as Dataview Query
    
    U->>A: Create application note
    U->>A: Add metadata fields
    U->>A: Link to [[Concept]]
    A->>A: Save file
    
    Note over C,D: Automatic process (no manual action)
    
    D->>D: Query scans vault
    D->>A: Finds link to concept
    D->>A: Extracts metadata
    D->>C: Updates display
    
    C->>U: Shows application<br/>in query results
    
    Note over U,C: Zero manual<br/>maintenance required!
```

**The Magic**:
1. You create notes and link concepts naturally
2. Queries automatically discover these links
3. Concept notes self-update with usage information
4. No manual cross-reference maintenance needed

---

## 📁 Folder Architecture: Standard Structure

```mermaid
graph LR
    A[Knowledge Domains] --> B1[Domain 1]
    A --> B2[Domain 2]
    A --> B3[Domain 3]
    A --> B4[Domain N...]
    
    B1 --> C1[00-Concepts]
    B1 --> C2[01-Applications]
    B1 --> C3[02-Synthesis]
    B1 --> C4[03-Meta]
    
    C1 --> D1[Theory.md]
    C1 --> D2[Method.md]
    C1 --> D3[Model.md]
    
    C2 --> E1[Study-2024.md]
    C2 --> E2[Experiment-2024.md]
    C2 --> E3[Analysis-2024.md]
    
    C3 --> F1[Literature Review.md]
    C3 --> F2[Meta-Analysis.md]
    
    C4 --> G1[_Domain-Config.md]
    C4 --> G2[_Concept-Template.md]
    C4 --> G3[_Application-Template.md]
    C4 --> G4[Domain Overview MOC.md]
    
    style A fill:#e1f5ff
    style B1 fill:#fff4e1
    style B2 fill:#fff4e1
    style B3 fill:#fff4e1
    style C1 fill:#e1ffe1
    style C2 fill:#ffe1e1
    style C3 fill:#f0e1ff
    style C4 fill:#ffe1f0
```

**Naming Conventions**:
- `00-` = Concept documentation (self-documenting notes)
- `01-` = Applications (notes that USE concepts)
- `02-` = Synthesis (cross-concept analysis)
- `03-` = Meta (configuration and templates)

**Numbers ensure proper sort order** in file explorer.

---

## 🎯 Concept Note Anatomy

```mermaid
graph TD
    A[Concept Note] --> B[🔝 Frontmatter]
    A --> C[📊 Status Field]
    A --> D[📝 Definition & Characteristics]
    A --> E[🔬 Self-Discovery Query]
    A --> F[✅ Status Tasks]
    A --> G[🌐 Knowledge Graph]
    
    B --> B1[Type: Theory/Method/etc]
    B --> B2[MOC: Link to domain]
    B --> B3[Aliases: Alternative names]
    
    C --> C1[Auto-updating progress bar]
    C --> C2[Based on Status Tasks]
    
    D --> D1[Core definition]
    D --> D2[Key characteristics]
    D --> D3[Principles/components]
    
    E --> E1[FLATTEN outlinks pattern]
    E --> E2[WHERE matches this file]
    E --> E3[Shows applications automatically]
    
    F --> F1[Documentation checklist]
    F --> F2[Drives progress tracking]
    
    G --> G1[Inbound links to/from this concept]
    G --> G2[Visual relationship mapping]
    
    style A fill:#e1f5ff
    style E fill:#ffe1e1
    style C fill:#e1ffe1
```

---

## 📄 Application Note Anatomy

```mermaid
graph TD
    A[Application Note] --> B[🔝 Frontmatter]
    A --> C[📊 Inline Metadata]
    A --> D[🧠 Concepts Applied Section]
    A --> E[📝 Main Content]
    
    B --> B1[Type: Application]
    B --> B2[MOC: Link to domain]
    B --> B3[Tags: Domain-specific]
    
    C --> C1[Field1:: Primary classification]
    C --> C2[Field2:: Links to concepts]
    C --> C3[Field3:: Additional context]
    
    D --> D1[List of concept links]
    D --> D2[How each is applied]
    D --> D3[Wiki-link format required]
    
    E --> E1[Study summary]
    E --> E2[Implementation details]
    E --> E3[Analysis/results]
    
    style A fill:#ffe1e1
    style C2 fill:#e1ffe1
    style D1 fill:#e1ffe1
```

**Critical Connection**: `Field2` (metadata) + Section D (Concepts Applied) create wiki-links that self-discovery queries detect.

---

## 🔍 Self-Discovery Query: Technical Flow

```mermaid
graph TB
    A[Self-Discovery Query Executes] --> B[FROM: Scan Applications Folder]
    B --> C[FLATTEN: Expand outlinks Array]
    C --> D{WHERE: Does outlink path<br/>match THIS file?}
    D -->|Yes| E[Include in Results]
    D -->|No| F[Skip]
    E --> G[GROUP BY: Deduplicate]
    G --> H[TABLE: Display with Metadata]
    
    H --> I1[Column 1: File Link]
    H --> I2[Column 2: Metadata Field 1]
    H --> I3[Column 3: Metadata Field 2]
    H --> I4[Column 4: Metadata Field 3]
    
    style A fill:#e1f5ff
    style D fill:#fff4e1
    style E fill:#e1ffe1
    style H fill:#ffe1e1
```

**Query Breakdown**:

```dataview
TABLE WITHOUT ID               ← No ID column
  file.link as "📄 Note",     ← Display file as link
  Field1,                      ← Show metadata field
  Field2,
  Field3
FROM "Domain/01-Applications"  ← Search this folder
FLATTEN file.outlinks as links ← Expand outlinks array
WHERE meta(links).path = this.file.path  ← Filter: only links TO this concept
GROUP BY file.link             ← Remove duplicates
```

---

## ⚙️ Progress Tracking: DataviewJS Flow

```mermaid
graph TD
    A[User Checks Task in<br/>Status Tasks Section] --> B[Save Note]
    B --> C[DataviewJS Executes]
    C --> D[Count Total Tasks in<br/>'Status Tasks' Section]
    C --> E[Count Completed Tasks<br/>checked = true]
    D --> F[Calculate Percentage:<br/>completed / total × 100]
    E --> F
    F --> G[Generate HTML Progress Bar]
    G --> H[Update status:: Field]
    H --> I[User Sees Updated<br/>Progress Bar]
    
    style A fill:#e1f5ff
    style F fill:#fff4e1
    style I fill:#e1ffe1
```

**Technical Details**:

```javascript
// 1. Get current file path
const setPage = dv.current().file.path;

// 2. Count completed tasks in "Status Tasks" section
const pgText = dv.current().file.tasks
    .where(t => t.section.subpath === "Status Tasks" && t.checked === true)
    .length;

// 3. Count total tasks in same section
const pgTotal = dv.current().file.tasks
    .where(t => t.section.subpath === "Status Tasks")
    .length;

// 4. Calculate percentage
const setPercent = Math.round((pgText / pgTotal) * 100);

// 5. Update status field with HTML progress bar
fm["status"] = "<progress value='" + setPercent + "' max='100'> </progress> " + setPercent + "%";
```

---

## 🎨 Domain Instantiation: Implementation Sequence

```mermaid
graph TD
    A[Start] --> B{Choose Domain Type}
    
    B -->|Pre-made| C[Template A, B, C, or D]
    B -->|Custom| D[Template E:<br/>Complete Worksheet]
    
    C --> E[Phase 2: Create Folders]
    D --> E
    
    E --> F[00-Concepts/<br/>01-Applications/<br/>02-Synthesis/<br/>03-Meta/]
    
    F --> G[Phase 3: Install Templates]
    
    G --> H[Copy Domain Config<br/>Copy Concept Template<br/>Copy Application Template<br/>Create MOC]
    
    H --> I[Phase 4: First Concept]
    
    I --> J[Duplicate Template<br/>Fill Frontmatter<br/>Write Definition<br/>Configure Query]
    
    J --> K[Phase 5: First Application]
    
    K --> L[Duplicate Template<br/>Add Metadata<br/>Link to Concept<br/>Write Content]
    
    L --> M{Validation:<br/>Does Application<br/>Appear in Query?}
    
    M -->|Yes| N[✅ System Operational!]
    M -->|No| O[Troubleshooting:<br/>Check Links,<br/>Verify Paths,<br/>Fix Field Names]
    
    O --> M
    
    N --> P[Phase 7: Expansion<br/>Add More Concepts<br/>Add More Applications<br/>System Self-Organizes]
    
    style A fill:#e1f5ff
    style N fill:#90EE90
    style O fill:#FFD700
    style P fill:#e1ffe1
```

**Timeline Estimates**:
- Pre-made Domain: **2-3 hours** to operational system
- Custom Domain: **3-4 hours** (includes planning)

---

## 🌐 Knowledge Graph: Relationship Mapping

```mermaid
graph LR
    A[Concept A] -->|outlinks| B[Concept B]
    A -->|outlinks| C[Concept C]
    
    D[Application 1] -.inlinks.-> A
    E[Application 2] -.inlinks.-> A
    F[Application 3] -.inlinks.-> A
    
    G[Application 4] -.inlinks.-> B
    G -.inlinks.-> C
    
    H[Synthesis Note] -.inlinks.-> A
    H -.inlinks.-> B
    H -.inlinks.-> C
    
    style A fill:#e1f5ff
    style B fill:#e1f5ff
    style C fill:#e1f5ff
    style D fill:#ffe1e1
    style E fill:#ffe1e1
    style F fill:#ffe1e1
    style G fill:#ffe1e1
    style H fill:#f0e1ff
    
    linkStyle 0,1 stroke:#333,stroke-width:2px
    linkStyle 2,3,4,5,6,7,8,9 stroke:#999,stroke-width:1px,stroke-dasharray: 5 5
```

**Legend**:
- **Solid Arrows** (→): Outlinks (Concept A references B and C)
- **Dashed Arrows** (-.->): Inlinks (Applications reference concepts)
- **Blue Nodes**: Concept Notes (documented entities)
- **Red Nodes**: Application Notes (usage examples)
- **Purple Nodes**: Synthesis Notes (cross-concept analysis)

**Knowledge Graph Section Shows**:
- **Inbound Links**: Other notes that reference this concept
- **Outbound Links**: Other concepts this note builds on

---

## 🔀 Multi-Domain System Architecture

```mermaid
graph TB
    A[PKB Root] --> B[Knowledge Domains]
    
    B --> C1[Cognitive Science]
    B --> C2[PKM Methodology]
    B --> C3[Prompt Engineering]
    B --> C4[Cosmology]
    B --> C5[Custom Domain N...]
    
    C1 --> D1[Concepts<br/>15 notes]
    C1 --> E1[Applications<br/>32 notes]
    
    C2 --> D2[Concepts<br/>12 notes]
    C2 --> E2[Applications<br/>25 notes]
    
    C3 --> D3[Concepts<br/>8 notes]
    C3 --> E3[Applications<br/>18 notes]
    
    C4 --> D4[Concepts<br/>10 notes]
    C4 --> E4[Applications<br/>15 notes]
    
    F[Meta-System Layer] --> G1[Domain Registry]
    F --> G2[Cross-Domain Analytics]
    F --> G3[System Health Dashboard]
    
    G1 -.monitors.-> C1
    G1 -.monitors.-> C2
    G1 -.monitors.-> C3
    G1 -.monitors.-> C4
    
    H[Shared Concepts] -.appears in.-> C1
    H -.appears in.-> C3
    H -.appears in.-> C4
    
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style F fill:#f0e1ff
    style H fill:#ffe1e1
```

**Domain Independence**: Each domain operates autonomously with its own:
- Taxonomy
- Metadata schema
- Folder structure
- Templates

**Meta-System Integration**: Domain Registry tracks all domains, enabling:
- Cross-domain queries
- Shared concept identification
- System-wide analytics

---

## 📊 Domain Health Monitoring Flow

```mermaid
graph TD
    A[Domain Health Dashboard] --> B[Concept Coverage Query]
    A --> C[Orphan Detection Query]
    A --> D[Application Distribution Query]
    A --> E[Completion Status Query]
    
    B --> B1{High Usage Concepts}
    B --> B2{Low Usage Concepts}
    
    C --> C1{Orphan Concepts<br/>Found?}
    C1 -->|Yes| C2[Create Applications<br/>OR<br/>Remove Concept]
    C1 -->|No| C3[✅ Full Coverage]
    
    D --> D1[Metadata Field<br/>Distribution]
    D --> D2[Identify Gaps<br/>in Coverage]
    
    E --> E1{Incomplete Concepts}
    E1 --> E2[Prioritize<br/>Documentation]
    
    style A fill:#e1f5ff
    style C2 fill:#FFD700
    style C3 fill:#90EE90
    style E2 fill:#FFD700
```

**Health Indicators**:
- ✅ **Green**: All concepts have applications, all documentation complete
- ⚠️ **Yellow**: Some orphans or incomplete documentation (normal during growth)
- 🚨 **Red**: Many orphans, stagnant growth (needs attention)

---

## 🔄 Content Creation Workflow

```mermaid
graph TD
    A[Daily Work:<br/>Reading, Research,<br/>Implementation] --> B{Encounter<br/>New Concept?}
    
    B -->|Yes| C[Create Concept Note<br/>Using Template]
    B -->|No| D{Use Existing<br/>Concept?}
    
    C --> E[Document Definition<br/>Characteristics<br/>Principles]
    
    D -->|Yes| F[Create Application Note<br/>Using Template]
    
    F --> G[Add Metadata<br/>Link to Concepts<br/>Write Content]
    
    G --> H[System Updates Automatically]
    
    H --> I[Concept's Self-Discovery<br/>Query Shows Application]
    
    I --> J[Knowledge Graph<br/>Expands]
    
    J --> K{Weekly Review}
    
    K --> L[Check Domain Health]
    K --> M[Identify Orphans]
    K --> N[Review Incomplete Docs]
    
    L --> O[Continue Daily Work]
    M --> O
    N --> O
    
    O --> A
    
    style A fill:#e1f5ff
    style H fill:#90EE90
    style K fill:#fff4e1
```

**Key Insight**: The system maintains itself. You create content naturally; queries handle organization automatically.

---

## 🎯 Decision Tree: Troubleshooting Path

```mermaid
graph TD
    A[Problem Detected] --> B{What's the Issue?}
    
    B -->|Application Not<br/>in Query| C{Is Concept<br/>Linked?}
    C -->|No| C1[Add [[Concept]] Link]
    C -->|Yes| C2{Is Path<br/>Correct?}
    C2 -->|No| C3[Fix FROM Path]
    C2 -->|Yes| C4{Are Field<br/>Names Right?}
    C4 -->|No| C5[Match Field Names<br/>to Config]
    C4 -->|Yes| C6[Refresh Note]
    
    B -->|Status Bar<br/>Not Working| D{DataviewJS<br/>Enabled?}
    D -->|No| D1[Enable in Settings]
    D -->|Yes| D2{Tasks in<br/>'Status Tasks'?}
    D2 -->|No| D3[Fix Section Name]
    D2 -->|Yes| D4[Wait & Refresh]
    
    B -->|Metadata<br/>Not Showing| E{Field Names<br/>Match Config?}
    E -->|No| E1[Fix Field Names<br/>Case-Sensitive!]
    E -->|Yes| E2{Fields in<br/>Query?}
    E2 -->|No| E3[Add to TABLE]
    E2 -->|Yes| E4[Check Application<br/>Has Fields]
    
    B -->|Query<br/>Error| F{Check<br/>Console}
    F --> F1[Ctrl+Shift+I<br/>View Error]
    F1 --> F2[Fix Syntax<br/>Based on Message]
    
    style A fill:#ffe1e1
    style C1 fill:#90EE90
    style C3 fill:#90EE90
    style C5 fill:#90EE90
    style D1 fill:#90EE90
    style E1 fill:#90EE90
```

**Troubleshooting Principle**: Start with most common issues (linking, paths, field names) before investigating complex problems.

---

## 📈 Growth Trajectory: Expected Development

```mermaid
gantt
    title Self-Documenting System Growth Timeline
    dateFormat YYYY-MM-DD
    
    section Foundation
    Choose & Configure Domain           :a1, 2025-01-01, 3d
    First 3-5 Concepts                  :a2, after a1, 7d
    First 10 Applications               :a3, after a2, 7d
    System Validation                   :a4, after a3, 3d
    
    section Expansion
    Reach 15 Concepts                   :b1, after a4, 14d
    Reach 30 Applications               :b2, after a4, 14d
    First Synthesis Notes               :b3, after b1, 7d
    Domain Health Dashboard             :b4, after b2, 3d
    
    section Maturity
    Instantiate Second Domain           :c1, after b4, 14d
    Cross-Domain Patterns               :c2, after c1, 14d
    Automated Analytics                 :c3, after c2, 7d
    
    section Scale
    4+ Domains Operational              :d1, after c3, 30d
    100+ Total Concepts                 :d2, after c3, 30d
    Network Effects Visible             :d3, after c3, 30d
```

**Milestones**:
- **Week 1**: System operational, validation complete
- **Week 2-3**: Foundation solid (15 concepts, 30 applications)
- **Month 2**: Second domain active
- **Month 3+**: Self-sustaining ecosystem with visible network effects

---

## 🎓 Skill Progression Map

```mermaid
graph LR
    A[Beginner] --> B[Intermediate]
    B --> C[Advanced]
    C --> D[Expert]
    
    A --> A1[Copy Templates]
    A --> A2[Create Simple Notes]
    A --> A3[Understand Query Basics]
    
    B --> B1[Customize Templates]
    B --> B2[Multi-Domain Setup]
    B --> B3[Modify Queries]
    
    C --> C1[Design Custom Domains]
    C --> C2[Advanced Query Patterns]
    C --> C3[Cross-Domain Synthesis]
    
    D --> D1[Build Meta-Analytics]
    D --> D2[Optimize Performance]
    D --> D3[Train Others]
    
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#ffe1e1
    style D fill:#e1ffe1
```

**Learning Path**:
1. **Beginner (Week 1-2)**: Follow templates exactly, focus on understanding mechanics
2. **Intermediate (Week 3-6)**: Customize for your needs, experiment with variations
3. **Advanced (Month 2-3)**: Design custom domains, optimize queries, create synthesis
4. **Expert (Month 3+)**: Meta-system design, performance optimization, methodology innovation

---

## 🔗 System Integration: Six-Pillar Hub Architecture

```mermaid
graph TB
    A[Self-Documenting<br/>Knowledge System] --> B[Six-Pillar Hub]
    
    B --> C1[Project Management]
    B --> C2[Navigation]
    B --> C3[Tracking]
    B --> C4[Analytics]
    B --> C5[Maintenance]
    B --> C6[Learning & Development]
    
    C1 --> D1[Track domain<br/>instantiation as projects]
    C2 --> D2[Link to Domain Registry<br/>Quick-access to MOCs]
    C3 --> D3[Monitor concept<br/>documentation progress]
    C4 --> D4[Aggregate cross-domain<br/>statistics & trends]
    C5 --> D5[Schedule orphan detection<br/>& concept reviews]
    C6 --> D6[Link active learning<br/>topics to concepts]
    
    style A fill:#e1f5ff
    style B fill:#fff4e1
```

**Integration Points**:
- Each pillar connects to self-documenting system
- Domain Registry serves as central navigation hub
- Health dashboards feed into Analytics pillar
- Review scheduling managed by Maintenance pillar

---

# 🔗 Related Topics for PKB Expansion

1. **[[Mermaid Diagram Best Practices for PKB]]**
   - *Connection*: Visual system documentation crucial for complex architectures
   - *Depth Potential*: Advanced diagram types, interactive elements, automatic generation
   - *Knowledge Graph Role*: Makes implicit system structure explicit and shareable

2. **[[Query Performance Optimization in Large Vaults]]**
   - *Connection*: As system scales to hundreds of notes, query efficiency matters
   - *Depth Potential*: Caching strategies, query optimization, folder scoping techniques
   - *Knowledge Graph Role*: Maintains system responsiveness as knowledge graph grows

3. **[[Domain Taxonomy Evolution Strategies]]**
   - *Connection*: Taxonomies need refinement as understanding deepens
   - *Depth Potential*: Versioning systems, migration patterns, backwards compatibility
   - *Knowledge Graph Role*: Allows knowledge architecture to mature without breaking existing notes

4. **[[Visual Knowledge Graph Generation]]**
   - *Connection*: Transform self-documenting metadata into visual network diagrams
   - *Depth Potential*: Force-directed layouts, clustering algorithms, interactive visualization
   - *Knowledge Graph Role*: Makes relationship patterns visible, reveals structural insights

---

> [!helpful-tip] Using This Visual Guide
> - **During Planning**: Review architecture diagrams to understand system design
> - **During Implementation**: Follow workflow sequences for step-by-step guidance
> - **During Troubleshooting**: Use decision trees to diagnose issues systematically
> - **For Training**: Share diagrams with collaborators to explain system mechanics
