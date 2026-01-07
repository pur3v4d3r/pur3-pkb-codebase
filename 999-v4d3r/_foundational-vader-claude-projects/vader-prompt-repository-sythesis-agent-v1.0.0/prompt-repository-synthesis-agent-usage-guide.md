# Repository Synthesis Agent: Usage Guide

## Quick Start

This guide explains how to effectively use the **Repository Synthesis Agent v1.0.0** prompt to analyze repository packages and generate master document series.

---

## What This Prompt Does

The Repository Synthesis Agent transforms scattered repository contents into coherent, comprehensive master document series through:

1. **Systematic multi-perspective analysis** (Tree of Thoughts exploration)
2. **Advanced extended thinking** with explicit reasoning
3. **Claim verification** and quality validation
4. **Large file handling** through intelligent chunking
5. **Production-ready document generation** with complete cross-referencing

---

## When to Use This Prompt

✅ **IDEAL USE CASES:**
- Analyzing repo packs containing domain-specific files (e.g., prompt engineering, coding patterns, architectural patterns)
- Consolidating scattered documentation into comprehensive guides
- Creating authoritative reference materials from multiple sources
- Extracting best practices from code examples and documentation
- Building knowledge bases from research papers or technical articles

❌ **NOT SUITABLE FOR:**
- Simple file summarization (use regular summarization)
- Single-file analysis (use targeted analysis prompts)
- Real-time collaboration (this is for static repo analysis)
- Code execution or testing (this is read-only analysis)

---

## Setup & Preparation

### 1. Organize Your Repository

The agent works best when your repository has:
- **Clear file naming**: Descriptive names that indicate content
- **Logical structure**: Related files grouped together
- **Consistent format**: Primarily text-based files (Markdown, code, YAML, JSON)
- **Reasonable size**: 5-100 files optimal (can handle more with sampling)

### 2. Upload Your Repository

**Option A: Upload as Zip**
1. Compress your repository folder
2. Upload the zip file to Claude
3. Mention the zip file name in your request

**Option B: Upload Individual Files**
1. Select key files from repository
2. Upload them to Claude
3. List the files in your request

**Option C: Provide Repository Path**
1. If using Claude Code or similar tool
2. Provide the absolute path to repository
3. Ensure Claude has read access

### 3. Craft Your Initial Request

Your request should include:

```markdown
I have uploaded [prompt-engineering-exemplar] containing files on [prompt-engineering].

Please use the Repository Synthesis Agent protocol to:
1. Analyze the repository structure and contents systematically
2. Identify key patterns and concepts
3. Design and generate a master document series consolidating the best works

Repository context:
- Domain: [e.g., "prompt engineering techniques"]
- File count: [90-100 files]
- Primary file types: [Markdown some Json/YAML]
- Specific focus: [comprehensive guides on advanced techniques]

Please begin with safety validation and repository characterization.
```

---

## Execution Workflow

The agent will execute in **8 sequential phases**. You don't need to guide each phase—the agent follows the protocol autonomously.

### Phase Sequence

**Phase 0: Initialization** (5-10 min)
- Safety validation
- Repository characterization
- Resource planning

**Phase 1: Discovery** (10-15 min)
- Structural analysis
- Content classification
- Domain identification

**Phase 2: Lens Generation** (5-10 min)
- Create analytical perspectives
- Prioritize lenses
- Plan exploration

**Phase 3: Exploration** (20-40 min)
- Apply lenses systematically
- Extract concepts and patterns
- Evaluate productivity

**Phase 4: Integration** (15-25 min)
- Synthesize findings
- Design document architecture
- Plan cross-references

**Phase 5: Detailed Planning** (15-20 min)
- Plan each document structure
- Allocate content to sections
- Define quality standards

**Phase 6: Generation** (30-60 min)
- Generate document content
- Apply formatting
- Insert cross-references

**Phase 7: Verification** (20-30 min)
- Verify claims
- Check consistency
- Validate quality

**Phase 8: Finalization** (10-15 min)
- Apply corrections
- Generate navigation
- Package deliverables

**Total Estimated Time: 2-4 hours** (varies by repository size)

---

## Monitoring Progress

### Green Flags (Good Signs)

✅ Agent creates explicit `<thinking>` blocks showing reasoning
✅ Agent generates multiple analytical lenses (3-4)
✅ Agent cross-validates findings across lenses
✅ Agent cites specific files and line numbers for claims
✅ Agent identifies and resolves inconsistencies
✅ Agent iterates to improve quality (Reflexion loops)

### Red Flags (Intervention Needed)

⚠️ Agent skips directly to document generation without analysis
⚠️ Agent uses only one analytical lens
⚠️ Agent makes claims without source citations
⚠️ Agent bypasses quality validation checkpoints
⚠️ Agent produces shallow documents (< 1000 words)
⚠️ Agent doesn't show thinking process

**If you see red flags:** Stop and redirect:
```markdown
Please go back to [specific phase] and follow the protocol systematically.
I notice you skipped [specific step]. Please execute that step with full thinking blocks before proceeding.
```

---

## Expected Outputs

### 1. Master Document Series

You'll receive **3-7 comprehensive documents**, each:
- **2500-5000+ words** (depending on complexity)
- **Production-ready formatting** (YAML metadata, proper headers, callouts)
- **Comprehensive cross-references** (internal and cross-document links)
- **Source citations** (file names, line numbers for all claims)
- **Code examples** (with explanations and context)
- **Diagrams** (Mermaid charts for complex systems)

### 2. Synthesis Report

Executive summary including:
- Repository overview and domain classification
- Analytical lenses applied and findings
- Pattern library (all patterns identified)
- Concept inventory (all concepts with sources)

### 3. Quality Assurance Documentation

- Verification report (claims verified, confidence scores)
- Consistency validation results  
- Production readiness scorecard
- Reflexion history (iterations, improvements)

### 4. Navigation Package

- Document series navigation guide
- Concept cross-reference map
- Reading path recommendations
- Source file provenance index

---

## Customization Options

### Adjust Analytical Focus

You can guide the lens generation:

```markdown
When generating analytical lenses, please prioritize:
- [Specific aspect, e.g., "practical implementation patterns"]
- [Another aspect, e.g., "theoretical foundations"]

You may de-emphasize:
- [Aspect to skip, e.g., "historical evolution"]
```

### Specify Document Types

```markdown
For the master document series, please focus on:
- 1 comprehensive reference guide
- 2-3 technical implementation guides
- 1 quick reference card

Skip tutorials and beginner content.
```

### Set Quality Thresholds

```markdown
Please target production readiness score of 9.5/10 (excellent) rather than 8.0/10 (good).
Use additional Reflexion cycles if needed to reach this threshold.
```

### Handle Large Repositories

```markdown
This repository has 200+ files. Please:
1. Sample 30-40 most representative files
2. Focus analysis on [specific subdirectory]
3. Use aggressive chunking for files > 500 lines
```

---

## Troubleshooting

### Issue: Agent Processes Too Slowly

**Cause:** Repository too large or files too complex

**Solution:**
```markdown
Please adjust your analysis strategy:
- Focus on [specific subdirectory] only
- Sample 50% of files, prioritizing [criteria]
- Use parallel processing where possible
```

### Issue: Documents Too Shallow

**Cause:** Agent not meeting minimum word counts

**Solution:**
```markdown
Your documents are below the minimum depth requirements. Please:
1. Review the "Minimum Word Count Enforcement" section in the prompt
2. Expand sections that are < 300 words per major concept
3. Add more examples and cross-references
4. Run quality validation and iterate until 9/10
```

### Issue: Inconsistent Terminology

**Cause:** Agent didn't complete consistency validation

**Solution:**
```markdown
Please run the "Cross-Document Consistency Check" from Phase 7.
Identify and resolve all terminology inconsistencies before finalizing.
```

### Issue: Missing Source Citations

**Cause:** Agent synthesized without Chain of Verification

**Solution:**
```markdown
Please apply Chain of Verification to all documents:
1. Extract all factual claims
2. Verify each claim against source files
3. Add citations (file name, line numbers) to every claim
4. Mark any unverifiable claims
```

### Issue: Agent Skipped Phases

**Cause:** Agent took shortcuts or didn't follow protocol

**Solution:**
```markdown
I notice you skipped from Phase [X] to Phase [Y].
Please return to Phase [X] and execute all tasks systematically.
Follow the quality gate checkpoints - do not proceed until gates pass.
```

---

## Advanced Usage

### Multi-Session Analysis

For very large repositories:

**Session 1: Analysis & Planning**
```markdown
Please complete Phases 0-5 (through detailed planning).
Save the architectural plan and concept inventory.
We'll continue with generation in the next session.
```

**Session 2: Generation**
```markdown
Continuing from previous session, please:
1. Review the architectural plan from our last session
2. Execute Phases 6-8 (generation, verification, finalization)
3. Apply quality validation throughout
```

### Iterative Refinement

After receiving initial documents:

```markdown
Thank you for the initial document series. Please now:
1. Run additional Reflexion cycle focusing on [specific aspect]
2. Expand Document [N], Section [X] with more [examples/depth/context]
3. Add cross-references between Documents [A] and [B] for [concepts]
4. Re-verify claims related to [specific topic]
```

### Domain-Specific Customization

For specialized domains:

```markdown
Note: This repository covers [specialized domain].
When analyzing:
- Use technical terminology appropriate for [audience level]
- Emphasize [domain-specific considerations]
- Include [domain-specific validation criteria]
```

---

## Quality Checklist

Before considering output complete, verify:

- [ ] **All documents generated** (as planned)
- [ ] **Minimum word counts met** (2500+ per major document)
- [ ] **All claims cited** (file names, line numbers)
- [ ] **Consistency validated** (terminology, definitions)
- [ ] **Cross-references work** (all links point to valid targets)
- [ ] **Quality score ≥8/10** (production readiness)
- [ ] **Navigation complete** (reading paths, index)
- [ ] **Metadata included** (YAML frontmatter)
- [ ] **Formatting applied** (consistent headers, callouts, code blocks)
- [ ] **Examples provided** (2-3 per major concept)

---

## Tips for Best Results

### ✅ DO:

1. **Provide context** about the repository domain and purpose
2. **Be patient** - comprehensive analysis takes time (2-4 hours)
3. **Trust the protocol** - let agent execute phases systematically
4. **Review thinking blocks** - they show agent's reasoning
5. **Validate outputs** - check quality scores and verification results
6. **Iterate if needed** - request Reflexion cycles for improvement

### ❌ DON'T:

1. **Rush the agent** - each phase needs adequate thinking time
2. **Skip phases** - the sequence is designed to build on previous work
3. **Accept low quality** - insist on scores ≥8/10
4. **Ignore red flags** - intervene if agent shortcuts protocol
5. **Overlook citations** - every claim needs source provenance
6. **Skip validation** - quality assurance is critical

---

## Example Complete Request

```markdown
I have uploaded a repository containing 42 Markdown files on advanced prompt engineering techniques for LLMs. The files include:
- 15 technique descriptions (Chain of Thought, Tree of Thoughts, etc.)
- 12 implementation patterns and code examples
- 8 use case studies
- 7 theoretical framework documents

Please use the Repository Synthesis Agent v1.0.0 protocol to:

1. Systematically analyze the repository using Tree of Thoughts exploration
2. Apply multiple analytical lenses (conceptual, practical, technical)
3. Extract all concepts, patterns, and best practices with source citations
4. Design a master document series consolidating this knowledge
5. Generate production-ready documents (target: 4-5 comprehensive guides)
6. Verify all claims and ensure consistency across documents
7. Achieve production readiness score ≥9/10

Repository context:
- Domain: Advanced prompt engineering for LLM applications
- Target audience: Experienced ML engineers and AI researchers  
- Emphasis: Practical implementation with theoretical grounding
- Quality: Publication-ready reference materials

Please begin with Phase 0: Safety validation and repository characterization.
Show your thinking process explicitly in all phases.
```

---

## Support & Feedback

This prompt is designed to be comprehensive and autonomous. However:

- **If agent deviates from protocol**: Redirect with specific phase reference
- **If quality below expectations**: Request additional Reflexion cycle
- **If outputs don't meet needs**: Provide specific feedback and request revision

The prompt includes extensive self-correction mechanisms through:
- Quality gate checkpoints at each phase
- Chain of Verification for factual accuracy
- Reflexion loops for iterative improvement
- Production readiness validation

Trust these mechanisms and let them run their course for optimal results.

---

## Version Information

**Prompt Version:** Repository Synthesis Agent v1.0.0
**Created:** 2025-01-07
**Architecture:** ToT-CoT-CoVe-Reflexion Enhanced
**Thinking Mode:** Enabled (40% token budget)
**Quality Standard:** Production-ready (≥8/10 score)
**Minimum Output:** 3000+ words per major document

---

**Ready to synthesize your repository? Upload your files and provide the context!**
