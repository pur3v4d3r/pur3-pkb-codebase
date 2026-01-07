# Document Generation Quick Reference Card

## 🎯 Document Type Selection Matrix

| If you need... | Use Module | Output |
|----------------|------------|--------|
| System overview, how it works | **Technical Docs** | 10-100+ page manual |
| How to learn/use something | **Tutorial** | Step-by-step guide |
| API endpoint reference | **API Docs** | OpenAPI/REST spec |
| All options/parameters | **Reference** | Exhaustive listing |
| Why we chose X | **ADR** | Decision record |
| What changed in version | **Changelog** | Release notes |
| Project entry point | **README** | Getting started |
| How to build feature | **Implementation Plan** | TDD task list |
| How to respond to incident | **Runbook** | Operational playbook |
| Visual representation | **Diagram** | Mermaid diagram |

---

## 📁 File Location Standards

```
project/
├── README.md                    # Project overview
├── CHANGELOG.md                 # Version history
├── docs/
│   ├── architecture.md          # Technical docs
│   ├── api/                     # API documentation
│   │   └── [resource].md
│   ├── tutorials/               # Learning guides
│   │   └── [topic].md
│   ├── reference/               # Exhaustive references
│   │   └── [topic].md
│   ├── adr/                     # Architecture decisions
│   │   ├── README.md            # ADR index
│   │   └── ADR-NNNN-[title].md
│   ├── plans/                   # Implementation plans
│   │   └── YYYY-MM-DD-[feature].md
│   └── runbooks/                # Operational docs
│       └── [service].md
```

---

## 🔑 Essential Sections by Document Type

### Technical Documentation
```
1. Executive Summary
2. Architecture Overview
3. Design Decisions (with rationale)
4. Core Components
5. Data Models
6. Integration Points
7. Deployment Architecture
8. Security Model
9. Troubleshooting
```

### Tutorial
```
- What You'll Learn (objectives)
- Prerequisites
- Time Estimate
- Progressive Sections:
  └─ Concept → Example → Practice → Challenge
- Summary & Next Steps
- Troubleshooting
```

### API Documentation
```
- Base URL & Authentication
- Rate Limiting
- Endpoints (for each):
  └─ Method, URL, Params, Request, Response, Errors, Example
- Webhooks
- SDKs
- Error Codes Reference
```

### ADR (Architecture Decision Record)
```
- Status (Proposed/Accepted/Deprecated/Superseded)
- Context (why decision needed)
- Decision Drivers
- Considered Options (with pros/cons)
- Decision
- Rationale
- Consequences (positive/negative/risks)
- Related Decisions
```

### Implementation Plan
```
Header:
  - Goal (1 sentence)
  - Architecture (2-3 sentences)
  - Tech Stack

For each Task:
  - Files (Create/Modify/Test)
  - Step 1: Write failing test
  - Step 2: Run to verify failure
  - Step 3: Minimal implementation
  - Step 4: Run to verify pass
  - Step 5: Commit
```

### Runbook
```
- Service Overview & Criticality
- Key Metrics (normal/warning/critical)
- Dashboard Links
- Alert Playbooks:
  └─ Trigger → Actions → Diagnosis Tree → Rollback
- Routine Maintenance
- Common Operations
- Escalation Contacts
```

---

## 📋 Quality Checklist (Universal)

```
□ Clear heading hierarchy (H1→H2→H3)
□ Logical flow (overview → details)
□ TOC for docs > 1 page
□ All code examples tested and runnable
□ No TODOs/placeholders/TBD
□ Cross-references linked
□ Version/date included
□ Diagrams render correctly
```

---

## 🔄 Document Generation Triggers

| User Says... | Generate |
|--------------|----------|
| "document this system" | Technical Docs |
| "how do I learn X" | Tutorial |
| "API reference for" | API Docs |
| "all configuration options" | Reference |
| "why did we choose" | ADR |
| "what's new in v2" | Changelog |
| "getting started guide" | README |
| "plan to build X" | Implementation Plan |
| "on-call runbook for" | Runbook |
| "show the architecture" | Diagram |

---

## 📐 Mermaid Diagram Quick Reference

```mermaid
%% Flowchart
flowchart TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Action]
    B -->|No| D[Other]

%% Sequence
sequenceDiagram
    Client->>Server: Request
    Server-->>Client: Response

%% ERD
erDiagram
    USER ||--o{ ORDER : places
    
%% State
stateDiagram-v2
    [*] --> Active
    Active --> Closed
```

---

## 🏷️ Commit Message → Changelog Mapping

| Commit Prefix | Changelog Section | Version Bump |
|---------------|-------------------|--------------|
| `feat:` | Added | MINOR |
| `fix:` | Fixed | PATCH |
| `perf:` | Changed | PATCH |
| `feat!:` | ⚠️ Breaking | MAJOR |
| `BREAKING CHANGE:` | ⚠️ Breaking | MAJOR |

---

## 📞 When to Create What

```
New Feature     → ADR + Tech Docs + Tutorial + README + Changelog
Bug Fix         → Changelog entry only
New API         → API Docs + README update
Major Decision  → ADR
New Team Member → README + Tutorials
Production Issue → Runbook update
Breaking Change → ADR + Migration Guide + Changelog
```
