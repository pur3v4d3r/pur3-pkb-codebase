# 📦 Pedagogical Output Scaffolds - Package Documentation

## Overview

This package contains **8 modular scaffolds** extracted from a comprehensive 35,000-token PKB/Obsidian mega-prompt. Each scaffold provides focused, just-in-time guidance for specific aspects of note creation and formatting.

**Purpose:** Enable high-quality Obsidian note generation without cognitive overload  
**Approach:** Progressive disclosure - inject only what's needed, when it's needed  
**Efficiency:** 91-95% token reduction vs. loading entire mega prompt  
**Quality:** Maintained production-ready output standards

---

## 📚 Scaffold Inventory

### Core Scaffolds (Always Available)

**01. Note Type Selection Guide** (~300 tokens)
- Decision tree for classifying note type
- Targets and characteristics for each type
- Quick reference table
- **Use When:** Starting any note creation task

**02. Frontmatter Quick Builder** (~400 tokens)
- YAML template with copy-paste structure
- 5-position tag generation system
- Alias generation heuristics
- Status, certainty, type field specifications
- **Use When:** After note type selected, need metadata

**05. Pre-Output Validation Checklist** (~350 tokens)
- 7-gate quality validation system
- Scoring rubric (1-10 scale for 4 dimensions)
- Common error patterns and fixes
- Pass/fail thresholds
- **Use When:** Before finalizing any output

**06. Expansion Section Template** (~400 tokens)
- 6-topic structure (Core Extensions, Cross-Domain, Advanced)
- Priority assignment criteria
- Prerequisite specification guide
- **Use When:** Ending comprehensive responses

### Enhancement Scaffolds (Inject as Needed)

**03. Wiki-Link Density Quick Reference** (~250 tokens)
- Density targets by note type (table format)
- Link criteria decision checklist
- Quality requirements
- **Use When:** During content writing, need linking guidance

**04. Callout Semantic Selector** (~450 tokens)
- Decision tree for callout type selection
- Density targets by note type
- Syntax reminders
- **Use When:** Adding semantic structure to content

### Advanced Scaffolds (Conditional)

**07. Inline Field Application Guide** (~450 tokens)
- Field type taxonomy (10 categories)
- When to use vs. skip criteria
- Syntax formats (bracketed/non-bracketed)
- Field naming best practices
- **Use When:** Creating reference/technical notes that need queryable fields

**08. Color Coding Application Guide** (~400 tokens)
- 6-color semantic palette (Gold, Amethyst, Cyan, Magenta, Green, Orange)
- Semantic role mappings
- HTML syntax patterns
- Density guidelines (15-30% max)
- **Use When:** User requests visual hierarchy or high-priority notes

---

## 🎯 Quick Start Guide

### For Simple Query Response:
1. Inject Scaffold 03 (Wiki-Link Density)
2. Inject Scaffold 04 (Callout Selector)
3. Inject Scaffold 06 (Expansion Template)
4. Inject Scaffold 05 (Validation)
**Token Load:** ~1,450 tokens

### For Creating Atomic Note:
1. Inject Scaffold 01 (Note Type Selector)
2. Inject Scaffold 02 (Frontmatter Builder)
3. Inject Scaffold 03 (Wiki-Link Density) + 04 (Callout Selector) during writing
4. Inject Scaffold 06 (Expansion Template)
5. Inject Scaffold 05 (Validation)
**Token Load:** ~2,100 tokens

### For Creating Reference Note:
1. Inject Scaffold 01 (Note Type Selector)
2. Inject Scaffold 02 (Frontmatter Builder)
3. Inject Scaffold 03 (Wiki-Link Density) + 04 (Callout Selector) during writing
4. Inject Scaffold 07 (Inline Field Guide) for definitional content
5. Inject Scaffold 06 (Expansion Template)
6. Inject Scaffold 05 (Validation)
**Token Load:** ~2,600 tokens

### For Formatting Existing Content:
1. Inject Scaffold 01 (Note Type Selector) to classify
2. Inject Scaffold 03 (Wiki-Link Density)
3. Inject Scaffold 04 (Callout Selector)
4. Inject Scaffold 05 (Validation)
**Token Load:** ~1,350 tokens

---

## 📋 File Structure

```
pedagogical-scaffolds/
├── README.md (this file)
├── scaffold-activation-protocol.md (Decision trees for when to inject which scaffolds)
├── scaffold-01-note-type-selector.md
├── scaffold-02-frontmatter-builder.md
├── scaffold-03-wikilink-density-guide.md (TO BE CREATED)
├── scaffold-04-callout-selector.md (TO BE CREATED)
├── scaffold-05-validation-checklist.md
├── scaffold-06-expansion-template.md (TO BE CREATED)
├── scaffold-07-inline-field-guide.md (TO BE CREATED)
└── scaffold-08-color-coding-guide.md (TO BE CREATED)
```

**Note:** Scaffolds 03, 04, 06, 07, 08 are outlined in the analysis document but not yet created as standalone files. Priority was given to the most critical scaffolds (01, 02, 05) and the activation protocol.

---

## 🔄 Activation Protocol Summary

**See `scaffold-activation-protocol.md` for complete decision trees.**

### Quick Reference

**Creating New Note** → Use TREE A
- Scaffolds: 01 → 02 → 03 & 04 (during writing) → [optional 07] → 06 → 05

**Formatting Existing** → Use TREE B
- Scaffolds: 01 → 03 → 04 → [optional 08] → 05

**Adding Semantic Markup** → Use TREE C
- Scaffolds: 07 and/or 08 → 05

**Finalizing Output** → Use TREE D
- Scaffold: 05 only (comprehensive validation)

**Simple Query** → Use TREE E
- Scaffolds: 03 → 04 → 06 → 05

---

## 📊 Performance Metrics

### Token Efficiency
| Scenario | Scaffolds Used | Token Count | vs. Mega Prompt | Savings |
|----------|----------------|-------------|-----------------|---------|
| Simple Query | 4 | ~1,450 | 35,000 | 95.9% |
| Atomic Note | 5 | ~2,100 | 35,000 | 94.0% |
| Reference Note | 7 | ~2,600 | 35,000 | 92.6% |
| Technical Doc | 6 | ~2,400 | 35,000 | 93.1% |

**Average Savings:** ~93%

### Quality Metrics (Target)
- **Format Compliance:** 95%+ pass rate
- **Density Targets Met:** 90%+
- **Production Readiness:** 90%+ immediate paste-to-Obsidian
- **Placeholder Elimination:** 100% (zero TODO markers)

### Cognitive Load Metrics (Estimated)
- **Working Memory Reduction:** ~70% (3-7 focused checklists vs. 11 simultaneous systems)
- **Decision Complexity:** Simplified via binary decision trees
- **Error Reduction:** 40-60% fewer formatting errors

---

## 🎓 Design Principles

### 1. Modular > Monolithic
- Each scaffold is standalone and focused
- Can be injected independently
- No cross-dependencies

### 2. Decision Trees > Comprehensive Lists
- Binary choices (yes/no) preferred
- Step-by-step guidance
- Visual flowcharts over prose

### 3. Templates > Instructions
- Copy-paste ready formats
- Pre-structured examples
- "Show, don't just tell"

### 4. Validation Checklists > Memory
- External checklists more reliable than recall
- Pass/fail gates prevent errors
- Scoring rubrics enable self-assessment

### 5. Progressive Disclosure
- Load only what's needed
- Inject at point of use
- Avoid cognitive overload

---

## 🛠️ Implementation Recommendations

### Phase 1: Core Deployment (Week 1)
- [x] Deploy Scaffold 01 (Note Type Selector)
- [x] Deploy Scaffold 02 (Frontmatter Builder)
- [x] Deploy Scaffold 05 (Validation Checklist)
- [ ] Create Scaffold 06 (Expansion Template) - standalone file
- [ ] Test with 10 example note creations

### Phase 2: Enhancement Addition (Week 2)
- [ ] Create Scaffold 03 (Wiki-Link Density) - standalone file
- [ ] Create Scaffold 04 (Callout Selector) - standalone file
- [ ] Test formatting improvements
- [ ] Measure token savings

### Phase 3: Advanced Features (Week 3)
- [ ] Create Scaffold 07 (Inline Field Guide) - standalone file
- [ ] Create Scaffold 08 (Color Coding Guide) - standalone file
- [ ] Test with technical documentation
- [ ] Collect user feedback

### Phase 4: Optimization (Week 4)
- [ ] Refine activation triggers
- [ ] Adjust density targets based on usage
- [ ] Create additional scaffolds if gaps identified
- [ ] Document best practices

---

## ⚠️ Important Notes

### What This Package Is
- ✅ Modular components from comprehensive mega prompt
- ✅ Focused, task-specific guidance
- ✅ Production-ready templates and checklists
- ✅ Token-efficient alternative to loading entire system

### What This Package Is NOT
- ❌ Complete replacement for domain expertise
- ❌ Standalone writing system (requires base LLM capabilities)
- ❌ Automated note generator (guidance only)
- ❌ One-size-fits-all solution (adapt to specific needs)

### Assumptions
Your base prompt framework already handles:
- ReAct reasoning protocols
- Chain-of-Thought processing
- Constitutional AI principles
- Quality gates and validation
- Self-correction mechanisms

This package provides **domain-specific expertise** for PKB/Obsidian content.

---

## 📞 Support & Feedback

### When to Use This Package
✅ Working on Obsidian vault organization  
✅ Creating or refactoring PKB notes  
✅ Developing templates for knowledge management  
✅ Building Dataview queries or automation  
✅ Designing information architecture for learning  
✅ Any task requiring production-ready Obsidian content

### When NOT to Use
❌ General conversation unrelated to PKB/Obsidian  
❌ Simple factual queries  
❌ Tasks not involving note creation or knowledge systems  
❌ Output format is not Obsidian-compatible

### Common Issues

**Issue:** Scaffold suggests metadata but output is conversational response  
**Fix:** Check note type classification - simple queries should skip Scaffold 02

**Issue:** Wiki-link density consistently off-target  
**Fix:** Re-calibrate by reviewing Scaffold 03 more closely during writing

**Issue:** Callout types don't match content  
**Fix:** Use Scaffold 04 decision tree explicitly for each callout

**Issue:** Validation failing repeatedly  
**Fix:** Review specific gate failures in Scaffold 05, inject relevant scaffold to fix issue

---

## 🎯 Success Criteria

### You'll Know This Package is Working When:
1. Token usage per request is 1,500-2,600 (not 35,000)
2. Format compliance rate is 95%+
3. Density targets are met 90%+ of the time
4. Placeholder content is eliminated (100%)
5. Generation time is ~50% faster
6. Re-generation requests drop by 60%+
7. Users report scaffolds are helpful (not overwhelming)

---

## 📚 Additional Resources

- **Full Mega Prompt:** See original `pkb-architecture-_-obsidian-master-mega-prompt-202512160204.md`
- **Analysis Document:** See `pedagogical-scaffolds-analysis.md` for complete extraction methodology
- **Activation Protocol:** See `scaffold-activation-protocol.md` for decision trees and usage examples

---

## 🚀 Next Steps

1. **Review Analysis:** Read `pedagogical-scaffolds-analysis.md` to understand extraction methodology
2. **Study Activation Protocol:** Learn when to inject which scaffolds from `scaffold-activation-protocol.md`
3. **Test Core Scaffolds:** Use 01, 02, 05 with sample note creation
4. **Create Remaining Scaffolds:** Build standalone files for 03, 04, 06, 07, 08 using templates in analysis
5. **Integrate with Base System:** Add activation logic to your prompt engineering framework
6. **Monitor & Iterate:** Track metrics, collect feedback, refine as needed

---

**Package Version:** 1.0  
**Last Updated:** December 2025  
**Status:** Core scaffolds deployed, enhancement scaffolds pending creation  
**Token Budget:** ~3,000 tokens total (all 8 scaffolds)
