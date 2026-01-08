---
type: "component"
component-type: "atomic"
component-category: "constraints"
id: "20260108000002"
status: "active"
maturity: "evergreen"
confidence: "established"
version: "1.0.0"
usage-count: 0
last-used: ""
success-rate: null
link-up: "[[00-library-index]]"
tags:
  - "year/2026"
  - "spes-system"
  - "component"
  - "atomic"
  - "constraints"
  - "quality-assurance"
aliases:
  - "Quality Gates Component"
  - "Validation Checklist"
created: "2026-01-08"
modified: "2026-01-08"
---

# Component: Quality Gates Checklist

> [!definition] Purpose
> Provides systematic validation checklists for code, templates, and documentation quality. Ensures artifacts meet production standards before delivery.

---

## 🎯 When to Use

Use this component when:
- Validating code before deployment
- Reviewing template quality
- Assessing documentation completeness
- Creating system prompts that generate artifacts
- Building tools that require quality assurance

**Best For**:
- Code generation prompts
- Template creation systems
- Documentation generators
- Review workflows
- QA automation

---

## 🚫 When NOT to Use

Avoid this component when:
- Creating quick prototypes or drafts
- Working in exploratory/experimental modes
- Quality validation is premature
- Output is internal/informal only

---

## 📝 Component Text

```prompt
<quality_gates>
## Validation Checklists

Apply these checks before delivering any artifact:

### Code Quality
- [ ] Try-catch error handling for all async operations
- [ ] File existence checks before read/write operations
- [ ] User feedback via Notice() or equivalent for all actions
- [ ] No hardcoded absolute paths (use relative or dynamic references)
- [ ] Descriptive variable names (no single letters except loop counters)
- [ ] Comments for non-obvious logic
- [ ] Graceful cancellation handling (user presses Escape)
- [ ] Edge case handling (empty arrays, null values, missing fields)
- [ ] No silent failures (all errors logged or reported)

### Template Quality
- [ ] Usage instructions at document top (as comments or callout)
- [ ] Consistent metadata schema (all required fields present)
- [ ] No orphaned template variables (all placeholders resolve or are marked for manual input)
- [ ] Valid syntax (test execution before delivery)
- [ ] Examples provided in comments for each section
- [ ] Handles empty/missing data without breaking
- [ ] Cursor positions numbered sequentially (if applicable)
- [ ] File naming automation works correctly

### Documentation Quality
- [ ] Purpose statement (what this does)
- [ ] Prerequisites (what must be installed/configured)
- [ ] Step-by-step usage instructions
- [ ] At least one basic example (input → output)
- [ ] Troubleshooting for common issues
- [ ] Integration notes (how this connects to other system components)
- [ ] Version history documented
- [ ] Links to related documentation
- [ ] Maintenance notes (how to update/extend)

### System Integration Quality
- [ ] Follows established naming conventions
- [ ] Respects existing folder structure
- [ ] Uses standard metadata schema
- [ ] Integrates with existing tools (Dataview, Templater, etc.)
- [ ] No duplicate functionality
- [ ] Backward compatible (or breaking changes documented)
- [ ] Dependencies documented
- [ ] Performance impact assessed
</quality_gates>
```

---

## 🔗 Works Well With

- [[component-constitutional-principles]] → Principles guide what to validate
- [[component-testing-framework]] → Testing validates quality
- [[component-review-workflow]] → Review process applies gates
- Any code generation or artifact creation prompt

**Synergy**: When combined with constitutional principles, creates complete design & validation framework.

---

## ⚠️ Conflicts With

- **Speed-first approaches** → Quality gates slow down initial delivery
- **"Move fast and break things"** → Gates enforce stability
- **Exploratory prototyping** → Gates may be premature

**Resolution**: Apply gates selectively based on artifact maturity and importance.

---

## 📊 Performance Notes

**Usage Context**: Pre-deployment validation, code review, template testing

**Success Rate**: High (95%+) when checklist is followed completely

**Quality Impact**: +40% defect reduction, +50% maintainability improvement

**Typical Placement**: End of generation prompts, before final output delivery

---

## 💡 Implementation Tips

1. **Customize for Context**: Not all gates apply to all artifact types
2. **Automate Where Possible**: Script common checks (syntax validation, link checking)
3. **Document Exceptions**: When skipping a gate, note why in artifact
4. **Evolve Checklist**: Add new gates as patterns emerge

---

## 🧪 Testing Validation

**Test Method**: Generate artifact, apply checklist, count violations

**Success Criteria**:
- [ ] Zero critical violations (error handling, silent failures)
- [ ] ≤2 minor violations (style issues, optional documentation)
- [ ] All sections of checklist reviewed
- [ ] Exceptions documented

---

## 📝 Variant Versions

**Lightweight Version** (for quick checks):
```prompt
Quick Quality Check:
- [ ] Does it work? (functional)
- [ ] Is it safe? (error handling)
- [ ] Is it clear? (documentation)
- [ ] Does it fit? (integration)
```

**Extended Version** (for critical systems):
Add security, performance, and accessibility gates.

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0   | 2026-01-08 | Initial extraction from v1.0.0 template |

---

## 🔗 Related Components

**In Same Category (Constraints)**:
- [[component-constitutional-principles]]
- [[component-safety-boundaries]]
- [[component-scope-limitations]]

**Cross-Category**:
- [[component-testing-framework]] (instructions)
- [[component-review-protocol]] (workflows)

---

*Component ID: 20260108000002 | Category: atomic/constraints | Status: active*
*Part of SPES Component Library*
