# ✅ Pre-Output Validation Micro-Checklist

## CRITICAL GATES - Must Pass ALL Before Output

### 🏷️ Gate 1: Metadata Compliance (If Note-Type Output)

**Metadata Presence Check:**
- [ ] YAML frontmatter included for permanent notes (Reference, Atomic, MOC, Synthesis)
- [ ] NO metadata for conversational/simple query responses
- [ ] Proper YAML syntax: `---` opening and closing delimiters
- [ ] Correct indentation (no tabs, 2-space indent for nested items)

**Tag Quality Check:**
- [ ] Position 1: Primary domain tag present (e.g., `#cognitive-science`)
- [ ] Position 2: Methodology/framework tag present (e.g., `#zettelkasten`)
- [ ] Position 3: Content type tag present (`#atomic-note`, `#reference-note`, etc.)
- [ ] All tags use lowercase, hyphenated format (`#tag-name`)
- [ ] 3-7 tags total (not too sparse, not excessive)

**Alias Quality Check:**
- [ ] 2-4 aliases included (not 0, not 10+)
- [ ] Includes common abbreviations (e.g., "CoT" for "Chain of Thought")
- [ ] Includes alternative phrasings (e.g., "Distributed Practice" for "Spaced Repetition")
- [ ] Includes related search terms
- [ ] No redundant or trivial aliases

**Status & Certainty Check:**
- [ ] Status field present: `[seedling|budding|evergreen|wilting]`
- [ ] Certainty field present: `[speculative|probable|confident|verified]`
- [ ] Type field matches content type tag
- [ ] Related notes field has 3-5 wiki-links (if applicable)

---

### 🔗 Gate 2: Wiki-Link Density Check

**Count Validation:**

| Note Type | Target Range | Your Count | Pass? |
|-----------|--------------|------------|-------|
| Simple Query | 3-6 links | ___ | ⬜ |
| Atomic Note | 3-8 links | ___ | ⬜ |
| Reference Note | 15-40 links | ___ | ⬜ |
| MOC | 20-50+ links | ___ | ⬜ |
| Synthesis Note | 10-25 links | ___ | ⬜ |

**Quality Checks:**
- [ ] All KEY concepts formatted as `[[Wiki-Links]]` (not plain text)
- [ ] Links are MEANINGFUL (not superficial or forced)
- [ ] First mention of terms linked (not every repetition)
- [ ] Correct syntax: `[[Note Title]]` (no broken brackets)
- [ ] Display text used where appropriate: `[[Target|Display Text]]`

**Coverage Checks:**
- [ ] Theoretical frameworks linked
- [ ] Technical terms linked
- [ ] Related concepts linked
- [ ] Prerequisites linked (for advanced content)
- [ ] Applications/extensions linked

---

### 💬 Gate 3: Callout Usage Check

**Density Validation:**

| Note Type | Target Range | Your Count | Pass? |
|-----------|--------------|------------|-------|
| Simple Query | 2-3 callouts | ___ | ⬜ |
| Atomic Note | 2-4 callouts | ___ | ⬜ |
| Reference Note | 8-15 callouts | ___ | ⬜ |
| Technical Guide | 10-20 callouts | ___ | ⬜ |
| MOC | 3-8 callouts | ___ | ⬜ |
| Synthesis Note | 5-8 callouts | ___ | ⬜ |

**Semantic Appropriateness:**
- [ ] Each callout type MATCHES content semantics:
  - `[!definition]` for definitions
  - `[!warning]` for warnings
  - `[!example]` for examples
  - `[!key-claim]` for main arguments
  - `[!evidence]` for supporting data
  - `[!methodology-and-sources]` for process explanations
  - `[!what-this-does]` for functional descriptions
- [ ] Callouts add value BEYOND plain text (not just decoration)
- [ ] NOT overusing callouts (creating visual clutter)
- [ ] Nesting depth ≤3 levels (if nesting used)

**Syntax Validation:**
- [ ] All callouts use valid syntax: `> [!type]` or `> [!type] Title`
- [ ] Callout types are from approved taxonomy (not invented)
- [ ] Multi-line callouts properly indented with `>` on each line
- [ ] Foldable callouts use correct syntax: `> [!type]-` or `> [!type]+`

---

### 📝 Gate 4: Format Compliance Check

**Prose Structure:**
- [ ] Prose-DOMINANT structure (not bullet-list-only sections)
- [ ] Detailed paragraphs build understanding (not just lists)
- [ ] Lists used SPARINGLY and appropriately
- [ ] Sentences vary in length and structure (not monotonous)
- [ ] Active voice preferred (passive when appropriate)

**Header Hierarchy:**
- [ ] Headers use markdown hierarchy: `#`, `##`, `###` correctly
- [ ] Header levels create LOGICAL outline structure
- [ ] No skipped levels (e.g., `#` to `###` without `##`)
- [ ] Headers are descriptive and scannable (not vague)
- [ ] Hierarchy supports TOC generation

**Code Blocks (If Present):**
- [ ] All code blocks properly fenced with \`\`\`
- [ ] Language identifiers specified: \`\`\`python, \`\`\`javascript, etc.
- [ ] Code is syntactically CORRECT and functional
- [ ] Explanatory prose surrounds code blocks (not orphaned)
- [ ] Error handling included in code examples (if applicable)

**Visual Elements:**
- [ ] Emoji used appropriately as semantic markers: ⚙️, 📚, 💡, 🔗
- [ ] Tables used for structured comparison data (when appropriate)
- [ ] Mermaid diagrams included for complex systems (when beneficial)
- [ ] Visual elements ENHANCE (not distract)

**Production Readiness:**
- [ ] NO placeholder content (no "TODO", "TBD", "Coming soon")
- [ ] NO incomplete syntax (all brackets closed, all tags complete)
- [ ] NO broken references (all links valid or marked as future)
- [ ] Can be pasted directly into Obsidian without modification

---

### 🔗 Gate 5: Expansion Section Check

**Presence Validation:**
- [ ] Expansion section INCLUDED for comprehensive responses
- [ ] Uses standard template structure:
  - Core Extensions (2)
  - Cross-Domain Connections (2)
  - Advanced Deep Dives (optional 2)
- [ ] NOT included for trivial queries or conversational responses

**Topic Quality:**
- [ ] 4-6 related topics suggested (4 minimum, 6 maximum)
- [ ] Each topic has CLEAR connection explanation
- [ ] Depth potential rationale is SUBSTANTIVE (not generic)
- [ ] Knowledge graph role positioning is SPECIFIC
- [ ] Priority levels assigned with CLEAR rationale

**Categorization Check:**
- [ ] Core Extensions (2) are DIRECT elaborations of current content
- [ ] Cross-Domain Connections (2) bridge DIFFERENT knowledge areas
- [ ] Advanced Deep Dives (optional 2) genuinely require prerequisite knowledge
- [ ] Prerequisites explicitly identified where applicable

**Topic Criteria:**
- [ ] Each topic genuinely WARRANTS separate note (not trivial)
- [ ] Topics connect MEANINGFULLY to current content (not tangential)
- [ ] Topics fit COHERENTLY in knowledge graph (not orphaned)
- [ ] Exploration paths are CLEAR (not vague)

---

### 🎯 Gate 6: Content Quality Check

**Depth Assessment:**
- [ ] DEPTH MANDATE satisfied (comprehensive treatment, NOT superficial)
- [ ] Complex concepts explained THOROUGHLY with examples
- [ ] Sufficient detail for IMMEDIATE understanding and application
- [ ] NO placeholder content or "TODO" markers

**Educational Coherence:**
- [ ] Information flows LOGICALLY from foundational to advanced
- [ ] Prerequisites addressed BEFORE dependent concepts
- [ ] Learning science principles applied (scaffolding, examples, elaboration)
- [ ] Terminology DEFINED before use
- [ ] Progressive complexity (Basic → Intermediate → Advanced)

**Accuracy & Evidence:**
- [ ] Claims SUPPORTED with reasoning or attribution
- [ ] NO dubious or unverified assertions
- [ ] Sources CITED when making empirical claims
- [ ] Distinctions and definitions are PRECISE
- [ ] Evidence quality appropriate to certainty level

**Completeness:**
- [ ] ALL aspects of query/topic addressed
- [ ] NO obvious gaps or omissions
- [ ] Edge cases and limitations noted where appropriate
- [ ] Counterarguments considered (for argumentative content)
- [ ] Integration with existing PKB knowledge addressed

---

### 🛠️ Gate 7: Obsidian Optimization Check

**Production Readiness:**
- [ ] Output can be pasted DIRECTLY into Obsidian without modification
- [ ] NO placeholder syntax or incomplete formatting
- [ ] ALL Obsidian-specific features used correctly
- [ ] Compatible with current Obsidian version

**Knowledge Graph Contribution:**
- [ ] Creates MEANINGFUL nodes in knowledge graph
- [ ] Enables discovery through graph visualization
- [ ] Establishes bi-directional linking opportunities
- [ ] Positions topic within broader knowledge architecture
- [ ] NO orphan nodes (always connected to graph)

**Plugin Compatibility:**
- [ ] Dataview inline fields follow correct syntax (if used)
- [ ] Templater variables avoided in static content
- [ ] Meta Bind syntax NOT included unless explicitly requested
- [ ] Content compatible with: graph view, search, linking
- [ ] Advanced PKB markers use correct syntax (if applicable)

---

## 🎯 Final Quality Scoring

**Assign scores (1-10) for each dimension:**

### Format Compliance: ___/10
*Metadata quality, wiki-link density, callout usage, syntax correctness*

### Knowledge Graph Contribution: ___/10
*Link quality, connection density, graph positioning, discoverability*

### Content Quality: ___/10
*Depth, accuracy, educational coherence, completeness, evidence strength*

### Obsidian Optimization: ___/10
*Production readiness, plugin compatibility, immediate usability*

### Overall Quality: ___/10
*Holistic assessment of response value and user utility*

---

## 🚦 Pass/Fail Thresholds

**PASS THRESHOLD:**
- ✅ Each dimension ≥7/10
- ✅ Overall quality ≥8/10

**IF ANY DIMENSION <7 OR OVERALL <8:**
```
STOP ⛔
└─ IDENTIFY specific deficiencies
└─ APPLY targeted corrections
└─ RE-VALIDATE before output
└─ IF still failing after corrections → Consider regeneration
```

**IF ALL ≥7 AND OVERALL ≥8:**
```
PROCEED ✅
└─ OUTPUT approved for delivery
└─ Document any minor improvements for future reference
└─ Move to outputs directory
└─ Present to user
```

---

## 🔄 Common Error Patterns

**Error 1: Missing Metadata Header**
- **Symptom:** Note-type content without YAML frontmatter
- **Fix:** Add complete frontmatter using Scaffold #2
- **Prevention:** Check note type selection before starting

**Error 2: Insufficient Wiki-Links**
- **Symptom:** Link count below target range
- **Fix:** Re-scan content for linkable concepts using Scaffold #3
- **Prevention:** Apply link criteria proactively during writing

**Error 3: Callout Type Mismatch**
- **Symptom:** Using `[!note]` for definition, `[!info]` for warning, etc.
- **Fix:** Replace with semantically correct type using Scaffold #4
- **Prevention:** Use Callout Semantic Selector during enhancement

**Error 4: Placeholder Content**
- **Symptom:** "TODO", "TBD", "[Add example here]" markers
- **Fix:** Complete all sections or remove placeholders
- **Prevention:** Production Fidelity principle - finish before output

**Error 5: Broken Wiki-Link Syntax**
- **Symptom:** `[Note Title]` or `((Note Title))` instead of `[[Note Title]]`
- **Fix:** Correct all link syntax to double-bracket format
- **Prevention:** Auto-validate link syntax before output

**Error 6: Missing Expansion Section**
- **Symptom:** Comprehensive note ends abruptly without related topics
- **Fix:** Add expansion section using Scaffold #6
- **Prevention:** Include expansion in initial structure planning

---

**Token Count:** ~350 tokens
**Use Case:** Run immediately before finalizing any output
**Critical:** Never skip this validation - prevents compound errors
**Next Step:** If validation passes → Present to user | If fails → Fix and re-validate
