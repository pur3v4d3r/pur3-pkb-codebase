---
tags: #meta #system #structure #analytics
aliases: [Vault Structure, Knowledge Graph Map, PKB Architecture]
status: evergreen
certainty: ^verified
created: 2025-12-16
---

# Vault Map

> [!abstract] Purpose
> Dynamic map of vault structure, growth patterns, and architectural insights. This note serves as a living index of the knowledge graph's topology.

---

## 📊 Directory Architecture

### Level 0: Core Infrastructure
```
00-inbox/          → Ingestion & triage zone
00-meta/           → System memory & configuration
000_databsae/      → [Investigation needed: typo or intentional?]
```

### Level 1: Temporal Organization
```
01-daily-notes/    → Atomic daily entries (time-indexed)
01_daily-notes/    → [Duplicate? Underscore vs hyphen variant ] 
```
Note from Pur3v4d3r: `01_daily-notes/    → [Duplicate? Underscore vs hyphen variant ]` -> this was created from a plugin or something being set up on an older naming convention. Hass been romoved. [[2025-16-12]]

### Level 2-7: Content Layers
```
02-projects/       → Active project documentation
03-notes/          → Core knowledge atoms
04-library/        → Reference materials & resources
05-tasks-&-reviews/ → GTD & reflection systems
06-dashboards/     → Overview & summary pages
07-mocs/           → Maps of Content (graph hubs)
```

### Level 99: System Management
```
99-archive/        → Deprecated/completed content
99-system/         → System configuration files
.claude/           → AI assistant configuration
.obsidian/         → Obsidian app configuration
.trash/            → Soft-deleted content
```

---

## 🔍 Structural Insights

### Naming Conventions
- **Numerical prefixes**: `00-` to `99-` for ordering
- **Separators**: Mix of hyphens and underscores (standardization opportunity)
- **Case style**: lowercase-with-hyphens preferred

### Directory Patterns
| Pattern | Count | Notes |
|---------|-------|-------|
| Core content | 6 | Levels 02-07 |
| System/meta | 4 | 00-meta, 99-system, .claude, .obsidian |
| Temporal | 2 | Daily notes (potential duplicate) |
| Utility | 2 | Archive, trash |

### Potential Issues
- `01-daily-notes/` vs `01_daily-notes/` duplication
- `000_databsae/` naming inconsistency (typo?)

---

## 📈 Growth Metrics

### Current State (2025-12-16 Baseline)
*To be populated with file counts*

```dataview
TABLE length(file.inlinks) as "Inlinks", length(file.outlinks) as "Outlinks"
FROM ""
SORT file.mtime DESC
LIMIT 10
```

### Hub Analysis
*Notes with highest connectivity (MOC candidates)*

```dataview
TABLE length(file.inlinks) + length(file.outlinks) as "Total Links"
FROM ""
WHERE length(file.inlinks) + length(file.outlinks) > 10
SORT (length(file.inlinks) + length(file.outlinks)) DESC
```

---

## 🗺️ MOC Index

### Confirmed MOCs
- `07-mocs/learning-&-memory-moc.md` - Learning systems

### MOC Candidates
*Areas with 5+ loosely connected notes*
- *To be identified through graph analysis*

---

## 🔗 Cross-System Integration

### Git Integration
- Repository root: `d:\10_pur3v4d3r's-vault`
- Branch: `master`
- Status: Multiple staged files (system in active development)

### Obsidian Plugins
- Icon folders detected (`.obsidian/icons/`)
- Dataview available (queries above)
- Custom icons: pur3, catppuccin, academicons themes

---

## 🧹 Maintenance Tasks

### Cleanup Opportunities
- [ ] Resolve daily-notes directory duplication
- [ ] Investigate `000_databsae` naming
- [ ] Standardize separator convention (- vs _)
- [ ] Archive `.trash/` contents if stale

### Graph Health Checks
- [ ] Identify orphan notes (0 inlinks/outlinks)
- [ ] Find over-connected notes (centralization risk)
- [ ] Map ghost links (references to non-existent notes)

---

## 🔗 Related

- [[session-memory]] - Session continuity
- [[user-preferences]] - Workflow patterns
- [[project-tracker]] - Active changes

---

*Last Structure Scan: 2025-12-16 | Next Review: On request*
