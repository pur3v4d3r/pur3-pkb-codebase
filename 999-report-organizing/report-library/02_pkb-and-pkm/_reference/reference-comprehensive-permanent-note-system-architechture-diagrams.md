












# Permanent Note System Architecture

---
tags: #system-architecture #visual-guide #mermaid-diagram
aliases: [System Diagram, Architecture Overview]
---

> [!abstract] Overview
> Visual representation of the complete permanent note system, showing how Templater, Dataview, Meta Bind, and Tasks plugins interact to create an intelligent knowledge management ecosystem.

## 🏗️ System Architecture Diagram

```mermaid
graph TB
    subgraph "User Interface"
        A[User Creates Note]
        B[User Reviews Note]
        C[User Updates Status]
    end
    
    subgraph "Templater Template Engine"
        D[Enhanced Template]
        E[User Prompts]
        F[Metadata Generation]
        G[Review Task Creation]
    end
    
    subgraph "Note Structure"
        H[Frontmatter Fields]
        I[Interactive Buttons]
        J[Dataview Queries]
        K[Review Tasks]
    end
    
    subgraph "Meta Bind Plugin"
        L[Status Buttons]
        M[Progress Bars]
        N[Input Fields]
        O[View Fields]
    end
    
    subgraph "Dataview Plugin"
        P[Knowledge Graph Queries]
        Q[Review Analytics]
        R[Temporal Views]
        S[Maturity Dashboards]
    end
    
    subgraph "Tasks Plugin"
        T[Review Task Index]
        U[Recurrence Engine]
        V[Due Date Tracking]
        W[Completion Detection]
    end
    
    subgraph "Data Storage"
        X[(Frontmatter Metadata)]
        Y[(Task Definitions)]
        Z[(File Relationships)]
    end
    
    subgraph "Automated Workflows"
        AA[Spaced Repetition]
        AB[Status Progression]
        AC[Analytics Generation]
        AD[Review Scheduling]
    end
    
    A --> D
    D --> E
    E --> F
    F --> H
    F --> G
    G --> K
    
    H --> X
    K --> Y
    
    C --> L
    L --> X
    L --> I
    
    I --> M
    I --> N
    I --> O
    
    B --> T
    T --> V
    V --> W
    W --> U
    U --> Y
    
    X --> P
    X --> Q
    X --> R
    X --> S
    
    Y --> T
    Z --> P
    
    P --> AC
    Q --> AC
    R --> AC
    S --> AC
    
    V --> AD
    X --> AD
    AD --> AA
    
    L --> AB
    AB --> X
    
    style A fill:#e1f5ff
    style B fill:#e1f5ff
    style C fill:#e1f5ff
    style D fill:#fff4e1
    style L fill:#f0e1ff
    style P fill:#e1ffe1
    style T fill:#ffe1e1
    style AA fill:#ffd700
    style AB fill:#ffd700
    style AC fill:#ffd700
    style AD fill:#ffd700
```

## 📊 Data Flow: Note Creation

```mermaid
sequenceDiagram
    participant U as User
    participant TE as Templater Engine
    participant FM as Frontmatter
    participant MB as Meta Bind
    participant DV as Dataview
    participant TP as Tasks Plugin
    
    U->>TE: Run Template
    TE->>U: Prompt for Title
    U->>TE: Enter "Working Memory"
    TE->>U: Prompt for Maturity
    U->>TE: Select "seedling"
    TE->>U: Prompt for Confidence
    U->>TE: Select "provisional"
    
    TE->>FM: Write metadata fields
    FM-->>FM: maturity: seedling
    FM-->>FM: confidence: provisional
    FM-->>FM: next-review: 2024-11-28
    FM-->>FM: review-count: 0
    
    TE->>MB: Inject button templates
    MB-->>MB: Render status buttons
    MB-->>MB: Render view fields
    
    TE->>DV: Inject query blocks
    DV-->>FM: Read metadata
    DV-->>DV: Execute queries
    
    TE->>TP: Create review task
    TP-->>TP: Parse recurrence rule
    TP-->>TP: Set due date: 2024-11-28
    TP-->>TP: Link to note
    
    TE->>U: Display completed note
```

## 🔄 Data Flow: Review Completion

```mermaid
sequenceDiagram
    participant U as User
    participant MB as Meta Bind Button
    participant FM as Frontmatter
    participant TP as Tasks Plugin
    participant DV as Dataview
    
    U->>MB: Click "Complete Review"
    
    MB->>FM: Increment review-count
    FM-->>FM: review-count: 1
    
    MB->>FM: Update modified date
    FM-->>FM: modified: 2024-11-21T14:30:00
    
    MB->>FM: Calculate next review
    Note over MB: Based on maturity level
    FM-->>FM: next-review: 2024-11-28
    
    MB->>U: Display success
    
    U->>TP: Check review task
    TP->>TP: Mark task completed
    TP->>TP: Trigger recurrence
    TP-->>TP: Create new task instance
    TP-->>TP: Set due: 2024-11-28
    
    DV->>FM: Read updated metadata
    DV-->>DV: Refresh dashboard queries
    DV->>U: Display updated metrics
```

## 🎯 Data Flow: Status Progression

```mermaid
flowchart TD
    A[New Note Created] --> B{Maturity Level}
    
    B -->|seedling| C[Review Interval: 1 week]
    B -->|budding| D[Review Interval: 2 weeks]
    B -->|developing| E[Review Interval: 1 month]
    B -->|evergreen| F[Review Interval: 3 months]
    
    C --> G{Confidence Level}
    D --> G
    E --> G
    F --> G
    
    G -->|speculative/provisional| H[Halve interval]
    G -->|moderate| I[Standard interval]
    G -->|high/established| I
    
    H --> J[Create review task]
    I --> J
    
    J --> K[Wait for due date]
    
    K --> L{User completes review}
    
    L -->|Yes| M[Update review-count]
    L -->|No| N[Mark overdue]
    
    M --> O{Assess maturity}
    
    O -->|Advance| P[Increase maturity level]
    O -->|Maintain| Q[Keep current level]
    O -->|Regress| R[Decrease maturity level]
    
    P --> S[Recalculate interval]
    Q --> S
    R --> S
    
    S --> T[Schedule next review]
    T --> K
    
    N --> U[Appear in overdue query]
    U --> L
    
    style A fill:#e1f5ff
    style M fill:#90EE90
    style N fill:#FFB6C1
    style P fill:#FFD700
    style T fill:#98FB98
```

## 🧠 Knowledge Graph Interaction

```mermaid
graph LR
    subgraph "Note Network"
        A[Concept A: Working Memory]
        B[Concept B: Attention]
        C[Concept C: Cognitive Load]
        D[Concept D: Executive Function]
        E[Concept E: Schema Theory]
    end
    
    subgraph "Metadata Layer"
        A1[maturity: evergreen<br/>confidence: high]
        B1[maturity: developing<br/>confidence: moderate]
        C1[maturity: budding<br/>confidence: provisional]
        D1[maturity: evergreen<br/>confidence: established]
        E1[maturity: seedling<br/>confidence: speculative]
    end
    
    subgraph "Query Results"
        Q1[Hub Analysis Query]
        Q2[Confidence Distribution]
        Q3[Maturity Dashboard]
        Q4[Orphan Detection]
    end
    
    A -.->|links to| B
    A -.->|links to| C
    A -.->|links to| D
    B -.->|links to| C
    C -.->|links to| D
    D -.->|links to| E
    
    A --> A1
    B --> B1
    C --> C1
    D --> D1
    E --> E1
    
    A1 --> Q1
    B1 --> Q1
    C1 --> Q1
    D1 --> Q1
    E1 --> Q1
    
    A1 --> Q2
    B1 --> Q2
    C1 --> Q2
    D1 --> Q2
    E1 --> Q2
    
    A1 --> Q3
    B1 --> Q3
    C1 --> Q3
    D1 --> Q3
    E1 --> Q3
    
    A -.-> Q4
    B -.-> Q4
    C -.-> Q4
    D -.-> Q4
    E -.-> Q4
    
    style A fill:#90EE90
    style D fill:#90EE90
    style E fill:#FFB6C1
    style Q1 fill:#e1ffe1
    style Q2 fill:#e1ffe1
    style Q3 fill:#e1ffe1
    style Q4 fill:#ffe1e1
```

## 🔗 Plugin Interaction Matrix

```mermaid
graph TB
    subgraph "Templater (Creation)"
        T1[Generate Metadata]
        T2[Create Structure]
        T3[Initialize Tasks]
    end
    
    subgraph "Meta Bind (Interaction)"
        M1[Status Buttons]
        M2[Progress Bars]
        M3[Input Fields]
    end
    
    subgraph "Dataview (Analytics)"
        D1[Query Metadata]
        D2[Aggregate Stats]
        D3[Generate Views]
    end
    
    subgraph "Tasks (Review)"
        TP1[Schedule Reviews]
        TP2[Track Completion]
        TP3[Manage Recurrence]
    end
    
    subgraph "Frontmatter (Storage)"
        FM[Central Metadata Store]
    end
    
    T1 --> FM
    T2 --> M1
    T3 --> TP1
    
    M1 --> FM
    M2 --> FM
    M3 --> FM
    
    FM --> D1
    D1 --> D2
    D2 --> D3
    
    FM --> TP1
    TP2 --> FM
    TP3 --> TP1
    
    D1 --> M2
    TP1 --> D1
    
    style FM fill:#ffd700
    style T1 fill:#fff4e1
    style M1 fill:#f0e1ff
    style D1 fill:#e1ffe1
    style TP1 fill:#ffe1e1
```

## 📈 Review System State Machine

```mermaid
stateDiagram-v2
    [*] --> Created: New note created
    
    Created --> Scheduled: Initial review task generated
    
    Scheduled --> DueToday: Date arrives
    Scheduled --> DueThisWeek: Approaching deadline
    
    DueToday --> InReview: User opens note
    DueThisWeek --> DueToday: Date arrives
    
    InReview --> Completed: Review finished
    InReview --> Deferred: User skips
    
    Completed --> MaturityAssessed: Evaluate development
    
    MaturityAssessed --> Advanced: Maturity increased
    MaturityAssessed --> Maintained: Maturity unchanged
    MaturityAssessed --> Regressed: Maturity decreased
    
    Advanced --> Rescheduled: Longer interval
    Maintained --> Rescheduled: Same interval
    Regressed --> Rescheduled: Shorter interval
    
    Rescheduled --> Scheduled: New task created
    
    Deferred --> Overdue: Deadline passed
    Overdue --> InReview: User eventually reviews
    Overdue --> Flagged: Persistent neglect
    
    Flagged --> UrgentReview: Manual intervention
    UrgentReview --> InReview: User addresses
    
    state Completed {
        [*] --> MetadataUpdate
        MetadataUpdate --> ReviewCountIncrement
        ReviewCountIncrement --> ModifiedDateUpdate
        ModifiedDateUpdate --> NextReviewCalculation
        NextReviewCalculation --> [*]
    }
    
    state MaturityAssessed {
        [*] --> ConfidenceCheck
        ConfidenceCheck --> ContentEvaluation
        ContentEvaluation --> ConnectionsReview
        ConnectionsReview --> MaturityDecision
        MaturityDecision --> [*]
    }
```

## 🎓 Learning Pathways

```mermaid
mindmap
  root((Permanent Note System))
    Foundational Layer
      Templater Template
        Metadata Fields
        User Prompts
        Auto-generated Structure
      Enhanced Frontmatter
        Status Tracking
        Review Scheduling
        Analytics Fields
    
    Interactive Layer
      Meta Bind Buttons
        Maturity Controls
        Confidence Updates
        Review Completion
      Visual Indicators
        Progress Bars
        Status Badges
        View Fields
    
    Query Layer
      Dataview Analytics
        Development Metrics
        Knowledge Graph
        Temporal Analysis
      Discovery Queries
        Hub Detection
        Orphan Identification
        Confidence Distribution
    
    Automation Layer
      Tasks Integration
        Spaced Repetition
        Recurrence Rules
        Due Date Tracking
      Workflow Automation
        Review Scheduling
        Status Progression
        Analytics Updates
    
    Advanced Extensions
      Dashboard Consolidation
      Custom Analytics
      AI Integration
      Knowledge Graph Visualization
```

---

## 🔍 Component Responsibility Map

| Component | Primary Responsibility | Writes To | Reads From |
|-----------|----------------------|-----------|------------|
| **Templater** | Initial note creation, structure generation | Frontmatter, Body content | User input prompts |
| **Meta Bind** | Interactive metadata editing | Frontmatter fields | Frontmatter fields |
| **Dataview** | Query and display metadata | None (read-only) | Frontmatter, File system |
| **Tasks** | Review task management | Task state, Task metadata | Task definitions, Due dates |
| **Frontmatter** | Metadata storage | File YAML header | N/A (storage layer) |

---

## 🚀 Future Architecture Extensions

### Planned Enhancement: AI Integration

```mermaid
graph LR
    A[Note Content] --> B[AI Analysis]
    B --> C{Suggested Actions}
    
    C -->|Low Quality| D[Flag for Revision]
    C -->|Missing Links| E[Suggest Connections]
    C -->|Confidence Assessment| F[Update Confidence]
    C -->|Maturity Evaluation| G[Advance Status]
    
    D --> H[Update Frontmatter]
    E --> I[Create Link Suggestions]
    F --> H
    G --> H
    
    H --> J[Trigger Review Task]
    I --> K[Display in Sidebar]
    
    style B fill:#e1f5ff
    style C fill:#ffd700
```

### Planned Enhancement: Collaborative Features

```mermaid
graph TB
    A[Your PKB] -->|Share Query| B[Shared Dashboard]
    C[Collaborator PKB] -->|Share Query| B
    
    B --> D[Aggregate Metrics]
    D --> E[Knowledge Overlap Analysis]
    D --> F[Complementary Concept Detection]
    D --> G[Review Pattern Comparison]
    
    E --> H[Visualization]
    F --> I[Recommendation Engine]
    G --> J[Best Practices Extraction]
    
    style B fill:#e1ffe1
    style D fill:#ffd700
```

---

**Architecture Version**: 1.0  
**Last Updated**: 2024-11-21  
**System Status**: Production-Ready