# 📝 Note Type Selection Guide

## Quick Decision Tree

**START HERE** ↓

**Is this a SINGLE concept needing thorough explanation?**
├─ ✅ YES → **ATOMIC NOTE**
│  └─ **Targets:** 300-800 words | 3-8 wiki-links | 2-4 callouts
│  └─ **Purpose:** Building block for knowledge graph, one concept fully explained
└─ ❌ NO → Continue ↓

**Is this COMPREHENSIVE coverage of a topic?**
├─ ✅ YES → **REFERENCE NOTE**
│  └─ **Targets:** 1,500-10,000+ words | 15-40 wiki-links | 8-15 callouts
│  └─ **Purpose:** Exhaustive resource, permanent knowledge artifact
└─ ❌ NO → Continue ↓

**Is this a NAVIGATION hub for a domain?**
├─ ✅ YES → **MOC (Map of Content)**
│  └─ **Targets:** Variable length | 20-50+ wiki-links | 3-8 callouts
│  └─ **Purpose:** Curated navigation, domain overview, connection hub
└─ ❌ NO → Continue ↓

**Does this INTEGRATE multiple concepts from different domains?**
├─ ✅ YES → **SYNTHESIS NOTE**
│  └─ **Targets:** 800-1,500 words | 10-25 wiki-links | 5-8 callouts
│  └─ **Purpose:** Cross-domain analysis, emergent insights, integration
└─ ❌ NO → Continue ↓

**Is this for PROJECT MANAGEMENT?**
└─ ✅ YES → **PROJECT HUB**
   └─ **Targets:** Variable | Resource-dependent links | 3-6 callouts
   └─ **Purpose:** Task coordination, timeline, decisions, outcomes

---

## Frontmatter Requirements by Type

| Note Type | Metadata Tags | Content Type Tag | Additional Fields |
|-----------|---------------|------------------|-------------------|
| **Atomic** | tags, aliases, status, certainty, type | `#atomic-note` | related (optional) |
| **Reference** | tags, aliases, status, certainty, type | `#reference-note` | related, source (if applicable) |
| **MOC** | tags, aliases, status, type | `#moc` | related (multiple connections) |
| **Synthesis** | tags, aliases, status, certainty, type | `#synthesis-note` | related (cross-domain links) |
| **Project Hub** | tags, aliases, status, type | `#project-hub` | start date, target date, owner |

---

## Quick Characteristics Table

| Feature | Atomic | Reference | MOC | Synthesis | Project |
|---------|--------|-----------|-----|-----------|---------|
| **Focus** | Single concept | Comprehensive topic | Navigation | Integration | Management |
| **Depth** | Thorough | Exhaustive | Organizational | Analytical | Operational |
| **Length** | 300-800 words | 1,500-10,000+ | Variable | 800-1,500 | Variable |
| **Links** | 3-8 | 15-40 | 20-50+ | 10-25 | Variable |
| **Callouts** | 2-4 | 8-15 | 3-8 | 5-8 | 3-6 |
| **Prose Style** | Explanatory | Scholarly | Curated lists | Integrative | Structured |
| **Examples** | Few key examples | Multiple examples | Link descriptions | Cross-domain cases | Milestones, tasks |

---

## Common Selection Mistakes

**❌ Choosing Atomic when should be Reference:**
- Topic is too complex for 800 words
- Multiple sub-concepts require separate sections
- Comprehensive treatment needed

**❌ Choosing Reference when should be Atomic:**
- Only one concept to explain
- Content would be 90% about single idea
- No need for exhaustive coverage

**❌ Choosing MOC when should be Synthesis:**
- Actually analyzing connections, not just listing
- Creating new insights from integration
- Original thought vs. curation

**❌ Choosing Synthesis when should be MOC:**
- Just organizing existing notes
- No new analysis or integration
- Pure navigation vs. analytical work

---

## Next Steps After Selection

1. **Apply Frontmatter Builder** to generate correct YAML header
2. **Check Density Targets** for wiki-links and callouts
3. **Use Appropriate Template** for note structure
4. **Validate Before Output** using pre-output checklist

---

**Token Count:** ~300 tokens
**Use Case:** Inject at start of note creation task
**Next Scaffold:** Frontmatter Quick Builder
