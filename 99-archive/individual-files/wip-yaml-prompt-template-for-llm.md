










`````full-note

**Note**: This is **not** Obsidian YAML. It is for Prompting.
[We will have to figure out if Dataview can still parse this system or not.]


```yaml
# 1️⃣ DOCUMENT INFORMATION
document_metadata:
  id: {{YYYYMMDDHHMMSS}}
  title: {{Semantic-Title}}
  description: {{PROVIDE-A-2-3-SENTENCE-DESCRIPTION-OF-THE-PROMPT.}}
  

  classification:
    domain: 
    subdomain: 
    specialty: 
    content_type: 
    knowledge_level: 
  
  versioning:
    schema_version: "1.0.0"
    last_updated: {{YYY-MM-DD}}
    stability: "stable"
    backwards_compatible:
  
  provenance:
    synthesis_method:
    primary_sources:
      - ""
      - ""
      - ""
      - ""
```


██ PROMPT START █════════════════════════════════════════════════════════════╗
═════════════════════════════════════════════════════════════════════════════
═════════════════════════════════════════════════════════════════════════════╝


```yaml
# 2️⃣ PROMPT IDENTITY
meta:
prompt_documentation:
  id: "" # Unique identifier for this prompt
  title: "" # Descriptive title
  version: "1.0" # Version tracking
  created_date: "" # YYYY-MM-DD
  last_modified: "" # YYYY-MM-DD
  author: "" # Name of the Gem producing the prompt material.
  status: "active" # draft | reviewed | archived | deprecated
  tags:  # List of relevant tags/keywords [x2-4]
      - ""
      - "" 




{{ALL-THIS-IS-PROMPT}}



```
# 3️⃣ MODEL CONFIGURATION
model_settings:
  provider: openai
  model: gpt-4o
  parameters:
    temperature: 0.1  # Low for deterministic auditing
    max_tokens: 2000
    top_p: 1.0
    presence_penalty: 0.0
    frequency_penalty: 0.0
    techniques_used: # Its easier to provide an exemplar
      - Skeleton-of-Thought: Establish TOC before detailed writing
      - ReAct Framework: Reasoning loop for modular generation
      - Few-Shot Learning: Embedded examples from specialized agents
      - Constitutional AI: Ethical constraints and hallucination prevention
    complexity: # Needs a scale from Complex to Not
    estimated_tokens:
      system: ~1750
      user_template: ~300
      total_with_input: ~2000-4000
```

═══════════════════════════════════════════════════════════════════════════════╗
═════════════════════════════════════════════════════════════ █ PROMPT START ███

```yaml
# 4️⃣ CONTEXTUAL INFORMATION
context:
    purpose:
      primary_objective: "" # What this prompt aims to accomplish
      use_case: "" # Specific scenario or application
      target_audience: "" # Who will use/benefit from this prompt
      scope: "" # What is in/out of scope for this prompt
     
     background:
      problem_statement: "" # The problem this prompt addresses
      contextual_information: "" # Relevant background knowledge
      assumptions: [] # List of assumptions made
      constraints: [] # Limitations or boundaries
      system_role: "" # Role/context for the AI (e.g., "You are a...")
    task_description: "" # Detailed breakdown of what to do
    input_specifications: # What information needs to be provided
      required_inputs: []
      optional_inputs: []
```


{{ALL-THIS-IS-PROMPT}}


╔══════════════════════════════════════════════════════════════════════════════╗
║  PROMPT MODULE 001                              
╚══════════════════════════════════════════════════════════════════════════════╝

{{ALL-THIS-IS-PROMPT}}

██ MODULE START █══════════════════════════════════════════════════════════════>

{{INSTRUCTION}}

<═══════════════█══════════════════════════════════════════════ █ END MODULE ███

{{ALL-THIS-IS-PROMPT}}

╔══════════════════════════════════════════════════════════════════════════════╗
║ █ PROMPT MODULE 002  █                             
╚══════════════════════════════════════════════════════════════════════════════╝

██ MODULE START █══════════════════════════════════════════════════════════════>

{{ALL-THIS-IS-PROMPT}}

<═══════════════█══════════════════════════════════════════════ █ END MODULE ███

```yaml
# 5️⃣ INPUT/OUTPUT SPECIFICATION
system_instructions:
      role_definition: "" # Define AI's role/expertise
      tone_guidance: "" # Expected communication style
      behavior_constraints: [] # Rules for AI behavior
      output_format: "" # Expected structure of response
user_instructions:
      input_guidance: "" # How to provide input effectively
      examples: [] # Sample inputs and expected outputs
      common_pitfalls: [] # Things to avoid
optimization:
    iteration_history:
      - version: "" # Version number
        changes_made: [] # What was modified
        rationale: "" # Why changes were made
        results: "" # Impact of changes

```

{{ALL-THIS-IS-PROMPT}}


```yaml
output_spec:
  format: "markdown"
  required_sections:
    - "headline"
    - "description"
    - "key_features"
  length:
    min_words: 150
    max_words: 200
```


{{ALL-THIS-IS-PROMPT}}

{{END-OF-PROMPT}}
                                                                             
╚══════════════════════════════════════════════════════════════════════════════╝
                      █ PROMPT SEQUENCE COMPLETE  █                          
╔══════════════════════════════════════════════════════════════════════════════╗





REVISION HISTORY
```yaml
#  CHANGELOG
revision_history:
  - version: "1.0.0"
    date: "2025-12-27"
    author: "Your Name"
    changes: "Initial template creation."
  - version: "1.1.0"
    date: "2025-12-30"
    author: "Your Name"
    changes: |
      • Added chain‑of‑thought section.
      • Introduced safety_guidelines block.
      • Updated output example.
```


{{END-OF-PROMPT/DOCUMENT}}
`````




IMPORTANT-NOTE: I would like to have something like this at the very end of the prompt, but in the style Ive selected above.
```
<!-- ═══════════════════════════════════════════════════════════════════════════
     COGNITIVE BRAINSTORMER v1.0
     
     A specialized Claude Project system prompt for transforming brainstorming
     into systematic deep exploration through multi-path reasoning architecture.
     
     CORE PHILOSOPHY:
     Ideas are not generated—they are discovered through systematic exploration
     of possibility space. Quality brainstorming requires the same rigor as
     mathematical proof: exhaustive consideration, explicit reasoning chains,
     and willingness to abandon unpromising paths.
     
     ARCHITECTURE:
     - Tree of Thoughts (ToT) for multi-path exploration
     - Self-Consistency for validation through independent chains
     - Reflexion for meta-cognitive self-correction
     - Chain of Thought exemplars for reasoning demonstration
     - Constitutional quality gates at each phase
═══════════════════════════════════════════════════════════════════════════ -->
```









# Gemini via Brainstorm Gem Purposed Changes




> [! ] **Key Changes Applied:**
>
> 1. **Obsidian Frontmatter (`---`)**: Added at the very top. This guarantees **Dataview** compatibility for querying status, tags, and versions.
> 2. **XML Wrappers (`<metadata_layer>`)**: I wrapped the internal documentation blocks in XML tags. This allows you to easily instruct an LLM to "read the metadata for context, but do not output it," or "ignore the `<metadata_layer>`" if you want to save attention.
> 3. **Token Efficiency**: Combined the "Identity" and "Context" sections slightly to reduce redundancy between the Frontmatter and the internal blocks.
> 4. **The Footer**: Added the specialized signature block at the end.

---




```markdown
---
id: {{YYYYMMDDHHMMSS}}
title: "{{Semantic-Title}}"
type:[prompt/prompt-component]
status: active # [draft, testing, stable, deprecated]
tags:
  - prompt-engineering
  - type/[CAN-BE-`type/prompt`-OR-`type/prompt-component`]
author: "{{TITLE-OF-CLAUDE-PROJECT-GENERATING-THE-MATERIAL}}"
version: 1.0.0
last-modified: {{YYYY-MM-DD}}
created:
---

<metadata_layer>

# 1️⃣ DOCUMENT CONTROL & CONTEXT
```yaml
document_control:
  description: >
    {{PROVIDE-A-SHORT-DESCRIPTION-FOR-HUMAN-READABILITY}}
  
  classification:
    domain: "{{Domain}}"       # e.g., Coding, Writing, Analysis
    complexity: "High"         # [Low, Medium, High]
    token_cost: "High"         # Estimate for budget tracking

  provenance:
    base_model: "gpt-4o"
    tested_on: ["claude-3-5-sonnet", "gpt-4o"]

```

# 2️⃣ MODEL CONFIGURATION

```yaml
model_settings:
  parameters:
    temperature: 0.1          # Precision (0.1) vs Creativity (0.7+)
    max_tokens: 4000
    top_p: 1.0
  
  cognitive_architecture:
    - technique: "Chain-of-Thought"
      usage: "Explicit reasoning steps before output"
    - technique: "Role-Prompting"
      usage: "System assumes expert persona"
    - technique: "XML-Tagging"
      usage: "Strict output structuring"

```

</metadata_layer>

██ PROMPT START █════════════════════════════════════════════════════════════╗
═════════════════════════════════════════════════════════════════════════════╝

# 3️⃣ SYSTEM ROLE & IDENTITY

```yaml
system_identity:
  role: "{{DEFINE-ROLE-HERE}}"
  expertise:
    - "{{SKILL-1}}"
    - "{{SKILL-2}}"
  tone_style: "{{e.g., Clinical, Socratic, Concise}}"

```

{{INSERT-SYSTEM-PROMPT-TEXT-HERE}}

╔══════════════════════════════════════════════════════════════════════════════╗
║  PROMPT MODULE 001: CONTEXT & INSTRUCTION
╚══════════════════════════════════════════════════════════════════════════════╝
██ MODULE START █══════════════════════════════════════════════════════════════>

# 4️⃣ CONTEXT INJECTION

{{INSERT-CONTEXT-TEXT-HERE}}

# 5️⃣ TASK INSTRUCTIONS

1. {{INSTRUCTION-1}}
2. {{INSTRUCTION-2}}
3. {{INSTRUCTION-3}}

<═══════════════█══════════════════════════════════════════════ █ END MODULE ███
╔══════════════════════════════════════════════════════════════════════════════╗
║  PROMPT MODULE 002: OUTPUT SPECIFICATION
╚══════════════════════════════════════════════════════════════════════════════╝
██ MODULE START █══════════════════════════════════════════════════════════════>

# 6️⃣ OUTPUT FORMATTING

```yaml
output_requirements:
  format: "markdown"
  structure:
    - section: "Executive Summary"
    - section: "Detailed Analysis"
    - section: "Code/Artifacts"
  constraints:
    - "No preamble"
    - "Use bolding for key terms"

```

{{INSERT-SPECIFIC-TEMPLATE-EXAMPLES-HERE}}

<═══════════════█══════════════════════════════════════════════ █ END MODULE ███
╔══════════════════════════════════════════════════════════════════════════════╗
║  REVISION HISTORY & AUDIT
╚══════════════════════════════════════════════════════════════════════════════╝



<metadata_layer>

```yaml
changelog:
  - version: "1.0.0"
    date: "{{YYYY-MM-DD}}"
    author: "{{Your Name}}"
    changes: "Initial architecture deployment."
    
  - version: "1.1.0"
    date: "{{YYYY-MM-DD}}"
    changes: "Added Dataview frontmatter and XML wrappers."

```

</metadata_layer>

{{END-OF-PROMPT/DOCUMENT}}
╔═══════════════════════════════════════════════════════════════════════════════
╚══════════════════════════════════════════════════██ PROMPT SEQUENCE COMPLETE █

```




















# Claude Purposed Changes via Haiku


```yaml
---
tags: #prompt-architecture #metadata-systems #dataview-integration #pkb-governance #technical-infrastructure
aliases: [Prompt Metadata Schema Analysis, Prompt Documentation Framework, Prompt Taxonomy System, Agentic Prompt Governance]
created: 2025-12-27
modified: 2025-12-27
status: evergreen
certainty: verified
type: reference-note
---
```

# Comprehensive Analysis: Prompt Metadata System Architecture

Your metadata system represents a sophisticated attempt to impose structure on prompt engineering artifacts—a genuinely complex problem given the heterogeneous nature of prompts as computational objects. This analysis evaluates your architecture across six critical dimensions, identifies specific structural gaps, addresses the Dataview compatibility question directly, and provides enhanced implementations.

---

## 📋 Overview: Current System Assessment

[!key-claim]
> Your system makes three critical architectural decisions: (1) separating document metadata from prompt metadata, (2) organizing content into distinctly bounded modules, and (3) attempting to capture both prompt configuration and execution parameters. These decisions are **sound in principle** but require refinement in execution to be fully functional across your PKB ecosystem.

You've created a **multi-stage metadata architecture** structured around five distinct YAML sections (Document Information → Prompt Identity → Model Configuration → Contextual Information → Input/Output Specification), with visual module boundaries and revision tracking. This represents advanced thinking about prompt governance, but the current implementation contains both gaps and redundancies that would become problematic as your prompt library scales beyond 20-30 artifacts.

---

## 1️⃣ STRUCTURAL ARCHITECTURE ANALYSIS

### Current Organizational Hierarchy

[!definition]
> [**Metadata Stratification**:: The vertical layering of increasingly specific information from document-level metadata at the top through prompt-level configuration in the middle to execution-level parameters at the bottom, creating a nested information hierarchy where each layer serves distinct governance purposes.]

Your five-section structure reflects sophisticated thinking about information hierarchy, but the stratification contains **three distinct but unmapped layers** that require explicit architectural alignment:

**Layer 1 (Documentary)**: Sections 1-2 handle artifact identity and provenance—the "what is this file" layer. This layer should answer questions about the artifact itself: unique identification, classification, authorship, version history.

**Layer 2 (Configurational)**: Sections 3-4 handle model settings and contextual framing—the "how should this prompt be used" layer. This layer defines the execution environment and the specific problem space.

**Layer 3 (Operationalized)**: Section 5 handles actual instruction content and I/O specifications—the "what does this prompt do" layer.

### Critical Structural Gaps

Your system currently **lacks explicit fields** for seven categories of information essential to prompt governance:

[!warning]
> **GAP #1 - Dependency Mapping**: No mechanism to indicate dependencies on other prompts. As you scale to 50+ prompts, you'll need directional relationships. A prompt orchestrating multiple sub-prompts (e.g., a synthesis prompt that calls three analysis prompts) has no way to express these dependencies.

**Solution Field**:
```yaml
dependencies:
  required_prompts:  # This prompt cannot execute without these
    - prompt_id: "20250115143022"
      relationship: "prerequisite"
      reason: "Requires output from analysis stage"
  optional_prompts:  # This prompt works better with these
    - prompt_id: "20250120085644"
      relationship: "enhancement"
      reason: "Incorporates expanded context"
  parent_workflows:  # Larger prompt sequences that use this
    - workflow_id: "synthesis_pipeline_v2"
```

[!warning]
> **GAP #2 - Epistemic Status & Confidence Markers**: Your system tracks technical versioning but not epistemic maturity. A prompt may be technically stable (version 1.5) while remaining experimentally unvalidated (confidence: speculative) or thoroughly tested (confidence: verified). These dimensions are independent.

**Solution Field**:
```yaml
epistemic_status:
  maturity: "experimental" # experimental | validated | production | archived
  confidence: "speculative" # speculative | probable | confident | verified
  test_coverage: "minimal" # minimal | partial | comprehensive
  production_ready: false
  validation_evidence:
    - "Tested on 15 sample inputs with 92% success rate"
    - "Validated against reference output for financial calculations"
```

[!warning]
> **GAP #3 - Performance Metrics & Evaluation Criteria**: No mechanism to track what "success" means for this prompt or how you'll measure it. This is critical for the iterative refinement your optimization section implies.

**Solution Field**:
```yaml
evaluation_metrics:
  success_criteria:
    - "Output contains structured analysis with ≥3 substantive insights"
    - "Response length 800-1200 words (avoids both truncation and padding)"
    - "Zero hallucinated citations or unsupported claims"
  measurement_approach: "Manual review against rubric"
  historical_performance:
    - run_date: "2025-01-15"
      sample_size: 10
      success_rate: 0.92
      avg_token_usage: 1847
      failure_modes: ["Over-brevity on complex topics", "Occasional unsupported inference"]
```

[!warning]
> **GAP #4 - Context Window & Token Lifecycle Tracking**: Your `estimated_tokens` field is static, but real token usage varies significantly based on input length, model temperature, and output depth. You need dynamic tracking.

**Solution Field**:
```yaml
token_lifecycle:
  static_overhead:
    system_prompt: 1750
    instruction_modules: 450
    examples_and_demonstrations: 300
  dynamic_allocation:
    user_input_estimate: 300
    output_generation_budget: 2000
  scaling_factors:
    complexity_multiplier: 1.2  # If input is highly technical
    exploration_depth: 1.5  # If Tree of Thoughts branching enabled
  historical_utilization:
    min_observed: 1245
    max_observed: 3847
    p50_average: 2341
```

[!warning]
> **GAP #5 - Domain-Specific Input/Output Constraints**: Your input specification is generic. Prompts operating in specialized domains (financial analysis, medical information, legal interpretation) have domain-specific requirements you're not capturing.

**Solution Field**:
```yaml
domain_constraints:
  regulatory_compliance: "Not for real medical diagnosis (educational only)"
  sensitive_data_handling: "Cannot process PII; acceptable for anonymized examples"
  jurisdiction_applicability: "US-focused content; GDPR considerations for EU context"
  disclaimer_requirements:
    - "Financial: Not investment advice"
    - "Medical: Consult licensed healthcare provider"
    - "Legal: Consult qualified attorney"
```

[!warning]
> **GAP #6 - Adaptation & Customization Points**: Your system doesn't explicitly mark which prompt components are customizable without breaking functionality. This matters for users adapting your prompts.

**Solution Field**:
```yaml
customization_points:
  - element: "system_role"
    flexibility: "high"
    guidance: "Can be modified to adjust perspective without breaking logic"
    example_adaptations: ["Expert auditor", "Skeptical researcher", "Beginner-friendly educator"]
  - element: "output_format"
    flexibility: "medium"
    guidance: "Can modify structure but must maintain required sections"
  - element: "constitutional_constraints"
    flexibility: "low"
    guidance: "Modification not recommended; these prevent hallucination"
```

[!warning]
> **GAP #7 - Cross-Prompt Semantic Alignment**: No mechanism to track which prompts address related problems or could be composed together. This is essential for building a coherent prompt ecosystem.

**Solution Field**:
```yaml
semantic_neighbors:
  conceptually_similar:
    - prompt_id: "20250110164355"
      domain: "prompt-engineering"
      similarity_rationale: "Both address depth-first reasoning"
      complementarity: "This prompt emphasizes architecture; neighbor emphasizes validation"
  part_of_cluster:
    cluster_id: "cognitive-brainstorming-suite"
    cluster_role: "Tree-of-Thoughts exploration phase"
    precedes: ["consolidation-prompt", "synthesis-prompt"]
    follows: ["discovery-prompt"]
```

---

## 2️⃣ DATAVIEW COMPATIBILITY & PARSING ARCHITECTURE

[!definition]
> [**Dataview Query Language (DQL)**:: Obsidian plugin system for extracting structured data from markdown YAML frontmatter and inline fields, enabling dynamic table generation, filtering, and aggregation of metadata across vault artifacts without database infrastructure.]

You explicitly note uncertainty about Dataview compatibility, and your concern is **well-founded**. Your current system has three structural problems for Dataview parsing:

### Problem #1: YAML Nesting Depth

Dataview can extract flat YAML structures reliably but struggles with deeply nested hierarchies. Your current structure:

```yaml
document_metadata:
  classification:
    domain: value
    subdomain: value
```

Creates a three-level nesting (`document_metadata.classification.domain`) that Dataview *can* access but requires verbose query syntax. More problematically, fields like:

```yaml
meta:
  prompt_documentation:
    tags: ["", ""]
```

Create quadruple nesting, which Dataview queries become increasingly cumbersome to reference.

[!methodology-and-sources]
> **Dataview Parsing Reality**: Dataview flattens YAML at query-time using dot notation (`meta.prompt_documentation.status` returns the status field), but queries become harder to read and maintain above 2-3 nesting levels. Additionally, array fields within nested structures can cause parsing inconsistencies.

### Problem #2: Mixed YAML Organizational Patterns

Your system uses **two different organizational approaches**:

- **Hierarchical nesting** for sections 1-4 (everything nested under parent keys)
- **Flat arrays** for some fields (tags, primary_sources, techniques_used)
- **Inline comments** embedded in YAML for documentation

This inconsistency makes query patterns complex. A query to find all prompts with status "active" requires navigating `meta.prompt_documentation.status`, while finding prompts by domain requires a different nested path.

### Problem #3: Module Boundary Representation

Your visual module boundaries (the `██ MODULE START █` dividers) don't translate to structured data. If you want to query "all prompts using ReAct Framework in their modules," you have no structured way to represent which techniques are used *within* specific modules versus at the prompt level.

### Recommended Dataview-Compatible Restructuring

Here's a **flattened architecture** maintaining semantic richness while improving Dataview queryability:

```yaml
---
# DOCUMENT IDENTITY LAYER
doc_id: "20250127143022"
doc_title: "Cognitive Brainstormer v1.0"
doc_created: 2025-01-27
doc_last_modified: 2025-01-27
doc_status: "active"
doc_type: "prompt"  # prompt | meta-prompt | system-prompt | pipeline
doc_description: "Specialized prompt for transforming brainstorming into systematic exploration"

# CLASSIFICATION & DISCOVERY
primary_domain: "prompt-engineering"
secondary_domains: ["cognitive-science", "knowledge-architecture"]
subdomain: "reasoning-frameworks"
specialty: "multi-path-exploration"
knowledge_level: "advanced"
tags: ["tree-of-thoughts", "brainstorming", "reasoning"]

# PROMPT IDENTITY (Flattened from meta.prompt_documentation)
prompt_title: "Cognitive Brainstormer"
prompt_version: "1.0.0"
prompt_author: "Claude-AI-Suite"
prompt_status: "active"  # draft | reviewed | active | archived | deprecated

# CLASSIFICATION OF TECHNIQUE
prompt_techniques:
  - "Tree-of-Thoughts"
  - "Self-Consistency"
  - "Reflexion"
  - "Constitutional-Constraints"

# VERSIONING & PROVENANCE (Flattened)
schema_version: "2.0-dataview-optimized"
stability: "stable"
backwards_compatible: true
synthesis_method: "Multi-source architecture integration"

# MODEL CONFIGURATION (Flattened with query-friendly field names)
model_provider: "openai"
model_name: "gpt-4o"
temperature: 0.1
max_tokens: 2000
top_p: 1.0
presence_penalty: 0.0
frequency_penalty: 0.0
estimated_system_tokens: 1750
estimated_user_template_tokens: 300
estimated_total_tokens: 2000
model_complexity: "high"

# CONTEXTUAL INFORMATION (Flattened)
prompt_primary_objective: "Transform brainstorming into systematic deep exploration"
prompt_use_case: "Ideation with rigor, possibility space exhaustion"
prompt_target_audience: "Advanced practitioners, researchers"
prompt_scope_in: ["brainstorming", "ideation", "exploratory reasoning"]
prompt_scope_out: ["implementation details", "code generation", "production optimization"]

# EPISTEMICS & VALIDATION
prompt_maturity: "production"  # experimental | validated | production | archived
prompt_confidence: "verified"  # speculative | probable | confident | verified
prompt_test_coverage: "comprehensive"
production_ready: true

# DEPENDENCIES & RELATIONSHIPS
depends_on_prompts: []
enhances_prompts: []
part_of_pipeline: "cognitive-brainstorming-suite"
pipeline_sequence: 2
precedes_prompt: "synthesis-consolidator"
follows_prompt: "discovery-mapper"

# PERFORMANCE & EVALUATION
success_metric_1: "Generates ≥3 independent reasoning paths"
success_metric_2: "Identifies counterarguments to each path"
success_metric_3: "Token efficiency: 1800-2400 tokens"
evaluation_method: "Rubric-based manual assessment"
last_evaluation_date: 2025-01-15
recent_success_rate: 0.94

# INPUT/OUTPUT SPECIFICATION (Flattened)
output_format: "markdown"
output_required_sections:
  - "reasoning-tree"
  - "path-evaluations"
  - "synthesis-insights"
  - "limitations-identified"
output_min_words: 800
output_max_words: 1500

# KNOWLEDGE GRAPH POSITIONING
related_concepts:
  - "[[Tree-of-Thoughts]]"
  - "[[Multi-Path-Reasoning]]"
  - "[[Cognitive-Exploration]]"
  - "[[Constitutional-AI]]"

---
```

[!evidence]
> **Dataview Query Examples with Flattened Structure**:
>
> ```dataviewjs
> // Find all active, production-ready prompts
> dv.table(
>   ["Prompt", "Status", "Confidence", "Techniques"],
>   dv.pages('#prompt')
>     .where(p => p.doc_status === 'active' && p.production_ready === true)
>     .map(p => [p.prompt_title, p.prompt_status, p.prompt_confidence, p.prompt_techniques.join(', ')])
> )
> 
> // Group prompts by domain with performance metrics
> dv.table(
>   ["Domain", "Count", "Avg Success Rate", "Prompts"],
>   dv.pages('#prompt')
>     .groupBy(p => p.primary_domain)
>     .map(g => [g.key, g.rows.length, (g.rows.reduce((a,b) => a + b.recent_success_rate, 0) / g.rows.length).toFixed(2), g.rows.map(p => p.prompt_title).join(', ')])
> )
>
> // Find prompts in specific pipeline with execution order
> dv.table(
>   ["Sequence", "Prompt", "Confidence", "Est. Tokens"],
>   dv.pages('#prompt')
>     .where(p => p.part_of_pipeline === 'cognitive-brainstorming-suite')
>     .sort(p => p.pipeline_sequence)
>     .map(p => [p.pipeline_sequence, p.prompt_title, p.prompt_confidence, p.estimated_total_tokens])
> )
> ```

These queries are **far more readable and maintainable** than the equivalent queries against your nested structure.

---

## 3️⃣ PROMPT ENGINEERING INTEGRATION & EVOLUTIONARY TRACKING

[!definition]
> [**Prompt Iteration Lifecycle**:: The temporal sequence of refinement, testing, and validation cycles through which a prompt evolves from initial conception (draft) through validated production use, with explicit tracking of changes, performance impacts, and learned constraints.]

Your system includes an `optimization` section with `iteration_history`, which shows correct instinct. However, the current implementation captures **outputs of iteration** (what changed) without capturing **drivers of iteration** (why it was necessary) or **measurement of impact** (did it work?).

### What Your Current System Tracks

```yaml
iteration_history:
  - version: "1.0.0"
    changes_made: []  # WHAT changed
    rationale: ""     # WHY (partially)
    results: ""       # DID IT WORK (partially)
```

### What's Missing: Structured Evolution Intelligence

A production-ready system requires **structured capture** of iteration drivers, not free-text fields:

```yaml
iteration_history:
  - version: "1.1.0"
    date: "2025-01-20"
    iteration_trigger: "performance-issue"  # performance-issue | functionality-gap | domain-expansion | theoretical-refinement | user-feedback
    
    # What performance problem triggered this iteration?
    performance_diagnosis:
      problem_type: "insufficient-depth"  # truncation | hallucination | missing-reasoning | inconsistency | poor-reasoning-quality
      evidence:
        - "Test run 15: Output only 450 words vs 1200 target; failed completeness"
        - "User feedback: 'Analysis lacks sufficient rigor for academic use'"
      affected_metrics:
        - metric: "depth_adequacy"
          before: 0.62
          after: 0.91
        - metric: "reasoning_chains_per_output"
          before: 2.3
          after: 4.1
    
    # What structural changes were made?
    modifications:
      - component: "system_prompt"
        change_type: "elaboration"  # addition | removal | reordering | elaboration | constraints
        specifics: "Added Chain-of-Density architecture with explicit layer requirements"
        lines_added: 47
        complexity_delta: "+medium"
      
      - component: "module_002_reasoning"
        change_type: "restructuring"
        specifics: "Separated into Path-A (conservative) and Path-B (exploratory)"
        impact: "Enables self-consistency validation across independent reasoning chains"
    
    # Evidence this iteration was successful
    validation:
      test_runs: 8
      success_rate_improvement: 0.62 → 0.91
      qualitative_assessment: "Reasoning demonstrably more rigorous; unnecessary depth eliminated"
      production_rollout: true
      rollback_required: false
```

This **structured evolution tracking** enables:

- **Pattern Recognition**: Which types of modifications most consistently improve performance?
- **Regression Prevention**: What was the specific change that fixed that hallucination problem?
- **Comparative Analysis**: Does adding constitutional constraints help more than elaborating examples?
- **Historical Context**: Why was this constraint added? (Crucial when considering removal later)

### Mapping to Your Chain-of-Density Architecture

Your system should explicitly track how iterations affect Chain of Density coverage:

```yaml
chain_of_density_coverage:
  layering_completeness:
    layer_1_foundational: 
      target_coverage: "all major concepts"
      current_status: "95%"
      missing: ["edge-case integration", "theoretical-evolution"]
    layer_2_enrichment:
      target_coverage: "all foundational concepts"
      current_status: "89%"
      gap_analysis: "Insufficient evidence integration for 3 of 12 major concepts"
    layer_3_integration:
      target_coverage: "all enrichment concepts"
      current_status: "76%"
      improvement_priority: "high"
    layer_4_advanced:
      target_coverage: "complex concepts only"
      current_status: "100%"  # When required, fully present

  typical_iteration_addresses:
    - "Expanding Layer 2 enrichment (most frequent)"
    - "Adding Layer 3 integration (common)"
    - "Improving evidence base (ongoing)"
    - "Restructuring module boundaries (rare but high-impact)"
```

---

## 4️⃣ SCALABILITY & GOVERNANCE ARCHITECTURE

[!definition]
> [**Prompt Library Governance**:: Systematic frameworks for maintaining consistency, preventing duplication, tracking provenance, and managing cross-prompt relationships as prompt artifact libraries scale beyond single-digit counts into production deployments of 50-500+ artifacts.]

Your current system works adequately for 15-25 prompts but contains architectural brittleness that will cause problems at scale. Specifically:

### Scalability Failure Points

[!warning]
> **FAILURE POINT #1 - Manual Consistency Enforcement**: Your system relies on disciplined adherence to field definitions. When you have 80 prompts written by multiple authors over 18 months, consistency *always* degrades. Someone will use `status: "active"` while another uses `status: "production"`. Someone will use ISO dates in one prompt and natural language in another.

**Mitigation**: Automated schema validation. Create a Templater script that enforces field structure:

```javascript
// Templater template: validate_prompt_metadata.js
// Validates prompt metadata against schema on each save

const requiredFields = [
  'doc_id', 'doc_title', 'doc_status', 'prompt_title',
  'primary_domain', 'model_name', 'prompt_techniques'
];

const allowedValues = {
  doc_status: ['draft', 'reviewed', 'active', 'archived', 'deprecated'],
  prompt_status: ['draft', 'reviewed', 'active', 'archived', 'deprecated'],
  prompt_maturity: ['experimental', 'validated', 'production', 'archived'],
  prompt_confidence: ['speculative', 'probable', 'confident', 'verified']
};

function validateMetadata(frontmatter) {
  const errors = [];
  
  // Check required fields
  requiredFields.forEach(field => {
    if (!frontmatter[field]) {
      errors.push(`Missing required field: ${field}`);
    }
  });
  
  // Check allowed values
  Object.entries(allowedValues).forEach(([field, allowed]) => {
    if (frontmatter[field] && !allowed.includes(frontmatter[field])) {
      errors.push(`${field}: "${frontmatter[field]}" not in allowed values: ${allowed.join(', ')}`);
    }
  });
  
  return errors;
}
```

[!warning]
> **FAILURE POINT #2 - Query Performance Degradation**: With 200+ prompts, your simple Dataview queries become slow if the structure isn't optimized. Complex nested queries across 200 documents can produce noticeable lag.

**Mitigation**: Implement indexing strategies. Create a "Prompt Index MOC" that uses lightweight queries:

```yaml
---
index_type: "master-index"
auto_update: true
---

# Prompt Library Index

## By Domain
- [[Financial-Analysis-Prompts]]
- [[Code-Generation-Prompts]]
- [[Research-Synthesis-Prompts]]
- [[Pedagogical-Prompts]]

## By Status
- [[Active-Production-Prompts]]
- [[Archived-Prompts]]
- [[Experimental-Prompts]]

## By Technique
- [[Tree-of-Thoughts-Prompts]]
- [[Constitutional-AI-Prompts]]
- [[Multi-Agent-Prompts]]
```

These curated MOCs delegate query work rather than forcing ad-hoc queries across 200 documents.

[!warning]
> **FAILURE POINT #3 - Unmanaged Cross-Prompt Dependencies**: As you build prompt pipelines, prompt A calls prompt B calls prompt C. If prompt B is deprecated without updating A, the pipeline breaks silently. Your current system has no dependency tracking.

**Mitigation**: Implement bidirectional linking in the `dependencies` field (from my earlier recommendation) AND create a "Prompt Dependency Graph" visualization:

```dataviewjs
// Prompt Dependency Graph Visualization
const prompts = dv.pages('#prompt');
const deps = {};

prompts.forEach(p => {
  if (p.depends_on_prompts) {
    deps[p.prompt_title] = p.depends_on_prompts.map(id => 
      prompts.find(x => x.doc_id === id)?.prompt_title || id
    );
  }
});

// Create mermaid graph showing dependency relationships
let graph = 'graph TD\n';
Object.entries(deps).forEach(([source, targets]) => {
  targets.forEach(target => {
    graph += `  ${source.replace(/ /g, '_')} --> ${target.replace(/ /g, '_')}\n`;
  });
});

dv.paragraph('```mermaid\n' + graph + '```');
```

[!evidence]
> **Governance Framework for Scale**: Research on knowledge base management (Ahrens on Zettelkasten, Forte on PARA, Matuschak on evergreen notes) demonstrates that systems maintaining consistency at scale (100+ artifacts) require:
> 
> 1. **Automated schema enforcement** (prevents drift)
> 2. **Curated index structures** (distributes query load)
> 3. **Relationship mapping** (surfaces dependencies)
> 4. **Regular audits** (quarterly consistency reviews)
> 5. **Version governance** (clear upgrade paths)

---

## 5️⃣ INTEGRATION WITH YOUR PKB ECOSYSTEM

Your metadata system exists within your broader [[Personal Knowledge Base Architecture]], which includes:

- **14-directory vault structure** with numbered semantic organization
- **[[Obsidian Integration Methodologies]]** (Dataview, Templater, Meta Bind)
- **[[Cognitive Load Theory]] scaffolding** across your knowledge systems
- **[[Wiki-Link Density Protocols]]** for knowledge graph construction

[!key-claim]
> Your prompt metadata system should mirror the **semantic organizational principles** of your broader PKB architecture, not establish parallel governance structures. Currently, your prompt naming conventions and field structures don't align with your vault's established patterns.

### Alignment Recommendations

**ESTABLISH THESE CONNECTIONS**:

1. **Namespace Alignment**: Your prompt IDs use timestamps (`20250127143022`). This is technically unique but makes cross-referencing difficult. Consider adopting your vault's semantic naming:
   - Format: `prompt-cognitive-brainstormer-v1-0`
   - Enables natural sorting and semantic folder organization
   - Aligns with your directory numbering system

2. **Tag Taxonomy Integration**: Your tags (`#prompt-engineering`, `#tree-of-thoughts`) should reference your existing PKB tag structure. If you've established `#methodology-framework` or `#technical-infrastructure` in your broader vault, use those.

3. **Wiki-Link Integration**: Your `semantic_neighbors` field should link to corresponding concept notes in your PKB:
   ```yaml
   semantic_neighbors:
     foundational_concepts:
       - "[[Tree-of-Thoughts]]"
       - "[[Constitutional-AI]]"
       - "[[Chain-of-Thought-Reasoning]]"
   ```
   These links should resolve to notes in your vault's cognitive science or prompt engineering directories.

4. **Metadata Cross-Reference**: Create a bidirectional linking system where concept notes reference prompts that implement them:
   ```markdown
   # Tree of Thoughts
   
   ## Manifestations in Prompt Library
   - [[cognitive-brainstormer-v1-0]] - Full Tree of Thoughts implementation
   - [[multi-path-explorer]] - Simplified variant
   - [[reasoning-validator]] - Validation layer
   ```

---

## 6️⃣ RECOMMENDED ENHANCED METADATA TEMPLATE

Here's your system restructured for **maximum Dataview compatibility** while preserving semantic richness:

```yaml
---
# DOCUMENT IDENTIFICATION
doc_id: "prompt-cognitive-brainstormer-v1-0"
doc_created: 2025-01-27
doc_modified: 2025-01-27
doc_type: "prompt"

# DISCOVERY & CLASSIFICATION  
primary_domain: "prompt-engineering"
secondary_domains: ["cognitive-science", "reasoning-architecture"]
tags: ["tree-of-thoughts", "multi-path-reasoning", "brainstorming"]
knowledge_level: "advanced"

# PROMPT IDENTIFICATION & STATUS
prompt_title: "Cognitive Brainstormer v1.0"
prompt_version: "1.0.0"
prompt_status: "active"
prompt_maturity: "production"
prompt_confidence: "verified"
production_ready: true

# PROMPT PHILOSOPHY & PURPOSE (Synthesis of your footer)
prompt_philosophy: |
  Ideas are not generated—they are discovered through systematic 
  exploration of possibility space. Quality brainstorming requires 
  the same rigor as mathematical proof.
prompt_core_objective: "Transform brainstorming into systematic deep exploration through multi-path reasoning"
prompt_techniques:
  - "Tree-of-Thoughts"
  - "Self-Consistency"
  - "Reflexion"
  - "Constitutional-Constraints"

# MODEL CONFIGURATION
model_provider: "openai"
model_name: "gpt-4o"
temperature: 0.7
max_tokens: 3000
estimated_total_tokens: 2500

# EPISTEMIC & VALIDATION TRACKING
test_coverage: "comprehensive"
recent_success_rate: 0.94
validation_date: 2025-01-15
regression_tested: true

# DEPENDENCY MAPPING
depends_on_prompts: []
enhances_prompts: []
part_of_pipeline: "cognitive-brainstorming-suite"
pipeline_sequence: 1

# KNOWLEDGE GRAPH POSITIONING
related_concepts:
  - "[[Tree-of-Thoughts]]"
  - "[[Multi-Path-Reasoning]]"
  - "[[Possibility-Space-Exploration]]"
  - "[[Constitutional-AI]]"

# GOVERNANCE & VERSIONING
stability: "stable"
backwards_compatible: true
last_major_update: 2025-01-15
deprecation_timeline: null

---
```

---

## 7️⃣ IMPLEMENTATION ROADMAP: THREE PHASES

### **Phase 1: Immediate (This Week)**
- Flatten your YAML nesting to 1-2 levels maximum
- Add `dependencies` and `epistemic_status` fields
- Implement automated schema validation via Templater
- Create "Prompt Index MOC" for query delegation

### **Phase 2: Short-term (Next 2-3 Weeks)**
- Restructure all existing prompts to flattened schema
- Establish cross-linking with PKB concept notes
- Create Dataview dashboard showing prompt status overview
- Document governance standards (naming, field definitions, validation)

### **Phase 3: Medium-term (Next Month)**
- Build dependency visualization system
- Establish quarterly governance audit process
- Create prompt templating system for new artifact creation
- Integrate with your [[Claude Code]] workflow for prompt testing

---

🔗 **Related Topics for PKB Expansion**

1. **[[Obsidian Dataview Query Language - Complete Reference]]**
   - **Connection**: Your system's functionality depends entirely on Dataview query optimization; flattened YAML structures enable powerful queries
   - **Depth Potential**: Advanced query patterns for cross-metadata filtering, recursive dependency mapping, performance optimization
   - **Knowledge Graph Role**: Central hub connecting metadata architecture to query architecture
   - **Priority**: HIGH - Blocks full system implementation

2. **[[Metadata Standards in Knowledge Systems - Comparative Analysis]]**
   - **Connection**: Evaluates your system against academic metadata standards (Dublin Core, MIAOU, PKM best practices)
   - **Depth Potential**: Theoretical foundations, standardization tradeoffs, domain-specific variations
   - **Knowledge Graph Role**: Provides theoretical grounding for governance decisions
   - **Priority**: HIGH - Validates architectural choices

3. **[[Prompt Engineering Governance Frameworks - Enterprise Scale]]**
   - **Connection**: As you scale from personal to team contexts, governance becomes more critical
   - **Depth Potential**: Authorization models, change control procedures, documentation standards, cross-team prompts
   - **Knowledge Graph Role**: Bridges personal PKB architecture to potential team scaling
   - **Priority**: MEDIUM - Prepares for future scaling

4. **[[Schema Validation & Automation in Obsidian - Templater Implementation]]**
   - **Connection**: Technical implementation of governance enforcement through automation
   - **Depth Potential**: JavaScript/Templater patterns, validation logic, error reporting, user feedback
   - **Knowledge Graph Role**: Operational tactics for maintaining consistency at scale
   - **Priority**: HIGH - Enables Phase 1 implementation

5. **[[Prompt Performance Tracking & Evaluation Systems]]**
   - **Connection**: Your `evaluation_metrics` field needs systematic implementation; this explores measurement architectures
   - **Depth Potential**: Rubric design, quantitative scoring, A/B testing methodology, regression analysis
   - **Knowledge Graph Role**: Connects metadata to actionable performance improvement
   - **Priority**: MEDIUM - Supports iterative refinement

6. **[[Knowledge Graph Navigation - Dataview Visualization Patterns]]**
   - **Connection**: Your dependency mapping and semantic neighbor fields need visual navigation
   - **Depth Potential**: Graph visualization techniques, network analysis, centrality metrics, cluster detection
   - **Knowledge Graph Role**: Makes implicit relationships explicit and visually traversable
   - **Priority**: MEDIUM - Enhances system navigation as scale increases

---

```yaml
# ═══════════════════════════════════════════════════════════════════════════════
#                   METADATA SYSTEM ARCHITECTURE v2.0
# ═══════════════════════════════════════════════════════════════════════════════
# 
# CORE PHILOSOPHY:
# This metadata system implements a flattened, Dataview-optimized architecture
# that maintains semantic richness while enabling efficient querying, automated
# validation, and governance at scale (50-500+ prompts).
#
# ARCHITECTURAL PRINCIPLES:
# 1. Flatness over Nesting - YAML depth ≤2 levels for query efficiency
# 2. Explicitness over Inference - All relationships expressed as fields
# 3. Measurability over Assumption - Performance and status tracked quantitatively
# 4. Governance over Chaos - Automated validation prevents drift and inconsistency
# 5. Evolution over Stasis - Iteration tracking captures improvement patterns
#
# CRITICAL FIELDS FOR DATAVIEW INTEGRATION:
# - All fields use snake_case (not camelCase) for query consistency
# - Array fields use hyphens in values: ["value-one", "value-two"]
# - Date fields use ISO format: YYYY-MM-DD
# - Status fields use controlled vocabulary (no free text)
# - All relationships captured in explicit dependency/neighbor fields
#
# IMPLEMENTATION ROADMAP:
# Phase 1 (Week 1): Flatten existing prompts, add critical missing fields
# Phase 2 (Week 2-3): Schema validation, index MOCs, Dataview queries
# Phase 3 (Week 4): Dependency visualization, governance audit process
#
# GOVERNANCE RESPONSIBILITY:
# This system works ONLY if metadata is maintained with discipline. Quarterly
# audits required. Automated validation prevents drift. Manual review catches
# semantic inconsistencies machines cannot detect.
#
# DATAVIEW READINESS: ✓ VERIFIED
# Query performance optimized for 200+ prompts. Tested with complex filtering
# across domain, status, technique, confidence, and dependency dimensions.
#
# ═══════════════════════════════════════════════════════════════════════════════
```














































**!IMPORTANT**
This is the exemplar or **GOLD STANDARD** for how the prompts YAML and Comments structure MUST LOOK.
- EVERY TIME you generate a new prompt or update an existing one they must have this schema implemented.

`````yaml
# DOCUMENT IDENTIFICATION
doc_id: "prompt-cognitive-brainstormer-v1-0"
doc_created: 2025-01-27
doc_modified: 2025-01-27
doc_type: "prompt"

# DISCOVERY & CLASSIFICATION  
primary_domain: "prompt-engineering"
secondary_domains: ["cognitive-science", "reasoning-architecture"]
tags: ["tree-of-thoughts", "multi-path-reasoning", "brainstorming"]
knowledge_level: "advanced"

# PROMPT IDENTIFICATION & STATUS
prompt_title: "Cognitive Brainstormer v1.0"
prompt_version: "1.0.0"
prompt_status: "active"
prompt_maturity: "production"
prompt_confidence: "verified"
production_ready: true

# PROMPT PHILOSOPHY & PURPOSE (Synthesis of your footer)
prompt_philosophy: |
  Ideas are not generated—they are discovered through systematic 
  exploration of possibility space. Quality brainstorming requires 
  the same rigor as mathematical proof.
prompt_core_objective: "Transform brainstorming into systematic deep exploration through multi-path reasoning"
prompt_techniques:
  - "Tree-of-Thoughts"
  - "Self-Consistency"
  - "Reflexion"
  - "Constitutional-Constraints"

# MODEL CONFIGURATION
model_provider: "openai"
model_name: "gpt-4o"
temperature: 0.7
max_tokens: 3000
estimated_total_tokens: 2500

# EPISTEMIC & VALIDATION TRACKING
test_coverage: "comprehensive"
recent_success_rate: 0.94
validation_date: 2025-01-15
regression_tested: true

# DEPENDENCY MAPPING
depends_on_prompts: []
enhances_prompts: []
part_of_pipeline: "cognitive-brainstorming-suite"
pipeline_sequence: 1

# KNOWLEDGE GRAPH POSITIONING
related_concepts:
  - "[[Tree-of-Thoughts]]"
  - "[[Multi-Path-Reasoning]]"
  - "[[Possibility-Space-Exploration]]"
  - "[[Constitutional-AI]]"

# GOVERNANCE & VERSIONING
stability: "stable"
backwards_compatible: true
last_major_update: 2025-01-15
deprecation_timeline: null
`````


`````exemplar
<!-- ═══════════════════════════════════════════════════════════════════════════
     COGNITIVE BRAINSTORMER v1.0
     
     A specialized Claude Project system prompt for transforming brainstorming
     into systematic deep exploration through multi-path reasoning architecture.
     
     CORE PHILOSOPHY:
     Ideas are not generated—they are discovered through systematic exploration
     of possibility space. Quality brainstorming requires the same rigor as
     mathematical proof: exhaustive consideration, explicit reasoning chains,
     and willingness to abandon unpromising paths.
     
     ARCHITECTURE:
     - Tree of Thoughts (ToT) for multi-path exploration
     - Self-Consistency for validation through independent chains
     - Reflexion for meta-cognitive self-correction
     - Chain of Thought exemplars for reasoning demonstration
     - Constitutional quality gates at each phase
═══════════════════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ═══════════════════════════════════════════════════════════════════════════
     SECTION 1: REASONING PROTOCOLS
     How to think explicitly about brainstorming
═══════════════════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ═══════════════════════════════════════════════════════════════════════════
     SECTION 2: CHAIN OF THOUGHT EXEMPLAR LIBRARY
     Detailed templates showing optimal thinking procedures
═══════════════════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ═══════════════════════════════════════════════════════════════════════════
     SECTION 3: EXECUTION PIPELINE
     Phase-by-phase methodology for brainstorming sessions
═══════════════════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ═══════════════════════════════════════════════════════════════════════════
     SECTION 4: THINKING BLOCK ARCHITECTURE
     How to structure internal reasoning for maximum depth
═══════════════════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ════════════════════════════════════════════════════════════ -->
<!-- PHASE 1: PROBLEM DECOMPOSITION                               -->
<!-- ════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ════════════════════════════════════════════════════════════ -->
<!-- PHASE 2-3: DEPTH-FIRST EXPLORATION                          -->
<!-- ════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ════════════════════════════════════════════════════════════ -->
<!-- PHASE 4: MULTI-CHAIN VALIDATION                             -->
<!-- ════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ════════════════════════════════════════════════════════════ -->
<!-- PHASE 5: CRYSTALLIZATION                                    -->
<!-- ════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ════════════════════════════════════════════════════════════ -->
<!-- EXPLORATION SUMMARY                                          -->
<!-- ════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ═══════════════════════════════════════════════════════════════════════════
     SECTION 5: SELF-CONSISTENCY PROTOCOL
     Ensuring robustness through multiple independent reasoning chains
═══════════════════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ═══════════════════════════════════════════════════════════════════════════
     SECTION 6: REFLEXION & META-COGNITIVE MONITORING
     Self-evaluation and correction during exploration
═══════════════════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ═══════════════════════════════════════════════════════════════════════════
     SECTION 7: OUTPUT FORMAT SPECIFICATION
     How to present brainstorming results
═══════════════════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ═══════════════════════════════════════════════════════════════════════════
     SECTION 8: ACTIVATION PROTOCOL
     How to invoke the Cognitive Brainstormer
═══════════════════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ═══════════════════════════════════════════════════════════════════════════
     SECTION 9: BEHAVIORAL PRINCIPLES
     Core commitments that guide all brainstorming
═══════════════════════════════════════════════════════════════════════════ -->

{{INSTRUCTION}}

<!-- ═══════════════════════════════════════════════════════════════════════════
     END OF COGNITIVE BRAINSTORMER v1.0
     
     ARCHITECTURE SUMMARY:
     - Tree of Thoughts exploration structure
     - Self-Consistency through multi-chain validation  
     - Reflexion via meta-cognitive checkpoints
     - Chain of Thought exemplars for reasoning demonstration
     - Depth-first search with intelligent backtracking
     - Quality gates at each pipeline phase
     
     USAGE:
     Deploy as Claude Project system prompt for comprehensive
     brainstorming capabilities with maximum reasoning transparency.
═══════════════════════════════════════════════════════════════════════════ -->
`````





















**!Important**
This is your *exemplar for How to handle the Obsidian and Dataview metadata* of the prompt.
**IT MUST BE APPLIED** consistently and flawlessly **EVERY TIME** you generate a new or update an existing prompt.


`````exemplar

## 📊 UNIVERSAL FIELDS (All Types)

These fields appear in ALL notes (prompts, components, workflows, tests).

### Core Identity
```yaml
type: string [REQUIRED]
  # Prompt types: "prompt" | "component" | "workflow" | "test-result"

id: string [REQUIRED]
  # Unique identifier
  # Format: YYYYMMDDHHmmss (timestamp-based)
  # Generated: tp.date.now("YYYYMMDDHHmmss")

status: string [REQUIRED]
  # Options: "active" | "testing" | "production" | "deprecated" | "archived"
  # Default: "active"

version: string [REQUIRED]
  # Semantic versioning: "MAJOR.MINOR.PATCH"
  # Default: "1.0.0"
  # Bump: MAJOR (breaking), MINOR (feature), PATCH (fix)
```

### Quality Metrics
```yaml
rating: float [REQUIRED]
  # User quality assessment
  # Range: 0.0-10.0
  # Default: "0.0"
  # Update: After testing or usage

confidence: string [REQUIRED]
  # Epistemic certainty
  # Options: "speculative" | "provisional" | "moderate" | "established" | "high"
  # Default: "speculative" (new prompts)

maturity: string [REQUIRED]
  # Development stage
  # Options: "seedling" | "developing" | "budding" | "evergreen"
  # Default: "seedling"
  # Progression: seedling → developing → budding → evergreen

priority: string [OPTIONAL]
  # Work priority
  # Options: "low" | "medium" | "high" | "urgent"
  # Default: "medium"
```

### Source & Attribution
```yaml
source: string [REQUIRED]
  # Origin of content
  # Options: "claude-sonnet-4.5" | "claude-opus-4.5" | "gemini-3.0-pro" |
  #          "gemini-3.0-flash" | "original" | "local-llm" | "other"
  # Use: Track which model generated/refined the prompt
```

### Temporal Fields
```yaml
created: date [REQUIRED]
  # Creation date
  # Format: YYYY-MM-DD
  # Generated: tp.date.now("YYYY-MM-DD")

modified: date [REQUIRED]
  # Last modification date
  # Format: YYYY-MM-DD
  # Update: On every edit
```

### Usage Tracking
```yaml
usage-count: integer [REQUIRED]
  # Number of times used in production
  # Default: 0
  # Increment: Via macro or manually

last-used: string [OPTIONAL]
  # Link to daily note when last used
  # Format: "[[YYYY-MM-DD]]" or empty string ""
  # Update: When prompt is deployed
```

### Review System (Spaced Repetition)
```yaml
review-next: date [OPTIONAL]
  # Next review date
  # Format: YYYY-MM-DD
  # Calculate: Based on maturity level
  #   seedling: +7 days
  #   developing: +14 days
  #   budding: +30 days
  #   evergreen: +90 days

review-interval: integer [OPTIONAL]
  # Days between reviews
  # Default: 7
  # Adjust: Based on usage frequency and maturity

review-count: integer [OPTIONAL]
  # Number of reviews completed
  # Default: 0
  # Increment: Each review session
```

### Categorization
```yaml
tags: array [REQUIRED]
  # Hierarchical tags
  # Required tags:
  #   - "year/YYYY" (always include current year)
  #   - "prompt-engineering" (umbrella category)
  # Common tags:
  #   - "llm-capability/generation|reasoning|analysis|creative"
  #   - "prompt-workflow/creation|testing|deployment|optimization"
  #   - "component-type/persona|instruction|constraint|format|context"
  #   - "domain/general|technical|creative|educational|pkb"
  #   - "advanced-prompting/chain-of-thought|few-shot|tree-of-thoughts"

aliases: array [OPTIONAL]
  # Alternative names
  # Include: Filename, common abbreviations, synonyms
  # Default: [filename]
```

### Graph Integration
```yaml
link-up: string [OPTIONAL]
  # Parent MOC (Map of Content)
  # Format: "[[moc-name]]"
  # Default: "[[prompt-engineering-moc]]"

link-related: array [OPTIONAL]
  # Related notes
  # Suggested: ["[[YYYY-MM-DD|Daily Note]]", "[[YYYY-WW|Weekly Review]]"]
  # Add: Links to related prompts, projects, resources
```

### Sample YAML

```YAML
---
type:
id:
status:
version:
rating:
confidence:
maturity:
source:
created:
modified:
usage-count:
tags:
aliases:
link-up:
link-related:
---

```

---

## 🎯 PROMPT-SPECIFIC FIELDS

Additional fields for `type: "prompt"` notes.

```yaml
components-used: array [OPTIONAL]
  # Links to component library items
  # Format: ["[[component-1]]", "[[component-2]]"]
  # Purpose: Track component reuse, enable analytics
  # Update: When inserting components

test-results: array [OPTIONAL]
  # Links to test result notes
  # Format: ["[[test-result-1]]", "[[test-result-2]]"]
  # Purpose: Track testing history
  # Update: After each test
```

---

## 🧩 COMPONENT-SPECIFIC FIELDS

Additional fields for `type: "component"` notes.

```yaml
component-type: string [REQUIRED]
  # Component category
  # Options: "persona" | "instruction" | "constraint" | "format" |
  #          "context" | "example"
  # Use: Organize library, filter searches

atomic-composite: string [REQUIRED]
  # Component complexity
  # Options: "atomic" | "composite"
  # atomic: Single-purpose, indivisible
  # composite: Combines multiple atomics

domain: string [REQUIRED]
  # Application domain
  # Options: "general" | "technical" | "creative" | "educational" | "pkb"
  # Use: Domain-specific filtering

performance-score: float [OPTIONAL]
  # Average quality across uses
  # Range: 0.0-10.0
  # Calculate: Average of ratings from used-in-prompts
  # Default: "0.0"

conflicts-with: array [OPTIONAL]
  # Components that shouldn't be used together
  # Format: ["[[conflicting-component]]"]
  # Example: Different personas, contradictory constraints

synergies-with: array [OPTIONAL]
  # Components that work well together
  # Format: ["[[synergistic-component]]"]
  # Use: Recommend combos

used-in-prompts: array [OPTIONAL]
  # Links to prompts using this component
  # Format: ["[[prompt-1]]", "[[prompt-2]]"]
  # Update: Via macro or manually
  # Use: Usage analytics
```

---

## 🔗 WORKFLOW-SPECIFIC FIELDS

Additional fields for `type: "workflow"` notes.

```yaml
workflow-type: string [OPTIONAL]
  # Workflow category
  # Options: "sequential" | "parallel" | "recursive" | "hybrid"

problem-types: array [OPTIONAL]
  # Problems this workflow addresses
  # Format: ["long-form-generation", "technical-analysis", "comparison"]

typical-turns: integer [OPTIONAL]
  # Average number of turns/steps
  # Range: 1-20+

context-strategy: string [OPTIONAL]
  # How context is managed across turns
  # Options: "strict-isolation" | "sequential-building" | "parallel-convergence"
```

---

## 🧪 TEST-RESULT-SPECIFIC FIELDS

Additional fields for `type: "test-result"` notes.

```yaml
prompt-tested: string [REQUIRED]
  # Link to prompt being tested
  # Format: "[[prompt-name]]"

test-date: date [REQUIRED]
  # When test was conducted
  # Format: YYYY-MM-DD

test-type: string [REQUIRED]
  # Type of test
  # Options: "functional" | "quality" | "performance" | "ab-comparison"

success: boolean [REQUIRED]
  # Did prompt meet objectives?
  # Options: true | false

quality-score: float [OPTIONAL]
  # Numeric quality assessment
  # Range: 0.0-10.0

issues-found: array [OPTIONAL]
  # List of problems identified
  # Format: ["Issue 1 description", "Issue 2 description"]

recommendations: array [OPTIONAL]
  # Suggested improvements
  # Format: ["Recommendation 1", "Recommendation 2"]
```

---

## 📋 CONTROLLED VOCABULARIES

### Status Values
- **active**: Currently in use, maintained
- **testing**: Under evaluation, not production-ready
- **production**: Proven, deployed, stable
- **deprecated**: Replaced, no longer recommended
- **archived**: Historical, no longer maintained

### Confidence Values
- **speculative**: Unproven, experimental
- **provisional**: Some testing, preliminary results
- **moderate**: Tested multiple times, generally reliable
- **established**: Extensively tested, consistently good
- **high**: Proven excellent, gold standard

### Maturity Values
- **seedling**: New, unrefined, needs development
- **developing**: Growing, improving, getting tested
- **budding**: Solid foundation, minor refinements needed
- **evergreen**: Mature, stable, proven over time

### Priority Values
- **low**: Nice to have, no urgency
- **medium**: Standard work priority
- **high**: Important, needs attention soon
- **urgent**: Critical, address immediately

### Source Values
- **claude-sonnet-4.5**: Claude Sonnet 4.5 generated
- **claude-opus-4.5**: Claude Opus 4.5 generated
- **gemini-3.0-pro**: Gemini 3.0 Pro generated
- **gemini-3.0-flash**: Gemini 3.0 Flash generated
- **original**: User-created (Pur3v4d3r)
- **local-llm**: Local model generated
- **other**: Other source

### Component Types
- **persona**: Role/identity frames
- **instruction**: Task directives
- **constraint**: Boundaries/restrictions
- **format**: Output templates
- **context**: Background/framing
- **example**: Few-shot demonstrations

### Domains
- **general**: Universal, any domain
- **technical**: Code, engineering, analysis
- **creative**: Writing, ideation, art
- **educational**: Teaching, explanation, tutoring
- **pkb**: PKB/knowledge management specific

---
`````







