Review all of this information carefully, then plan out and generate the Claude Project System Prompt that can accomplish the goals of this project. The system prompt should be designed to guide the generation of reports using the "Structural Scaffolds" outlined below [Which-you-will-need-toconstruct], ensuring that the output is deeply analytical, richly detailed, and well-connected to existing knowledge in my PKB. The system prompt should also include instructions for the use of callouts, wikilinks, and the YAML Metadata template to ensure consistency and integration within the PKB. The final output should be a comprehensive system prompt that can be used to generate high-quality reports on a variety of academic inquiries.

**NOTE**: You MUST incorporate the use of Self Consistency, Tree of Thoughts, and Chain of Density techniques in the generation process to ensure depth and coherence in the reports. AS WELL AS Thinking Tags at appropriate points in the generation process to guide the reasoning and ensure that the output is well-structured and logically coherent.
Use the REACT so the Claude Project in question integrate tool use and generation in a way that maximizes the quality and depth of the reports.

---

# Claude Project Report Generator Series Idea: Structural Scaffolds for Advanced Academic Reports

I have an idea for a Claude Project that both researches and then generates report using Self Consistency, Tree of Thoughts, and Chain of Density to generate Advanced Reports on Academic inquiries. The idea is to create a series of "Structural Scaffolds" that guide the generation of different types of reports, each with its own unique structure and requirements. That I can tell the Claude Project I am interested in learning about: John Deweys Reflective Thinking in a First Priciples style. The Claude Project looks at the "Structural Scaffold: First Principles Report (Fundamental Analysis)" and generates a report that is deeply analytical, breaking down the topic into its most fundamental components and exploring it from the ground up. With prose that is rich in detail and analysis, supported by callouts that highlight key concepts, arguments, evidence, and connections to other ideas in my PKB. The final output is a comprehensive report that not only explains the topic but also situates it within the broader landscape of knowledge in my PKB, providing insights and connections that I can further explore.

Use of Wikilinks is also mandated to connect the report to existing concepts in my PKB, and the final section includes a YAML Metadata template to ensure consistent documentation and classification across my PKB. The goal is to create a series of reports that are not only informative but also deeply analytical and interconnected, providing a rich resource for learning and exploration.


# List of Report Scaffolds
- Here is a list of scaffolds you can create for this Claude project.
- Each MUST be tailored to a different style of reporting and analysis.

`````markdown
List of Report Scaffolds:
- Structural Scaffold: Foundational Report (Deep Exposition)
- Structural Scaffold: First Principles Report (Fundamental Analysis)
- Structural Scaffold: Analytical Report (Critical Analysis)
- Structural Scaffold: Socratic Report (Question-Driven Exploration)
`````

# Key Notes
- The main goal is always prose with the use of Callouts in supporting the information in the prose before and after it.
- The callouts are not just for formatting; they are a deliberate strategy to structure the information in a way that enhances understanding and retention.
- The connections made in the reports should be explicit and meaningful, demonstrating how the topic fits into the broader landscape of knowledge in my PKB.
- The final output should be meticulously reviewed for coherence, accuracy, and depth, ensuring it meets the highest academic standards.


This is a template for a "Structural Scaffold: Foundational Report (Deep Exposition)" designed to guide the creation of comprehensive, in-depth reports on specific topics. The template is structured into several phases, each with specific requirements and callouts to ensure a thorough exploration of the topic.

Use this to create other scaffolds, such as "Structural Scaffold: Analytical Report (Critical Analysis)" or "Structural Scaffold: Synthesis Report (Integrative Overview)" by modifying the phases and callouts accordingly.

`````Structural_Scaffold_exemplar_Foundational Report_(Deep_Exposition)
**Structural Scaffold: Foundational Report (Deep Exposition)**

 **1. Define Core Parameters:**
    * **[TOPIC]:** {{Specify the central topic, concept, or question}}
    * **[DEPTH_LEVEL]:** {{e.g., "Encyclopedic overview," "In-depth technical analysis," "Historical context"}}
    * **[EXISTING_CONCEPTS]:** {{(Optional) Provide a list of `[[wikilinks]]` from your vault that you want to connect this topic to, e.Example: `[[Concept A]]`, `[[Theory B]]`}}

 **2. Phase 1: Overture & Foundation (The "Why & What")**
    * **Abstract:** Start with a `> [!abstract]` callout. Provide a high-level, 1-2 paragraph summary of the entire topic.
    * **Definition:** Provide a clear, unambiguous `> [!definition]` of the `[TOPIC]`.
    * **Core Principles:** Explain the "big picture." What is the fundamental idea?
      * `> [!the-philosophy]` or `> [!core-principle]`
      * `> What is the central problem this topic addresses or the core phenomenon it describes?`

 **3. Phase 2: Encyclopedic Exposition (The "Deep Dive")**
    * **Deconstruction:** Break the `[TOPIC]` down into its logical, primary sub-headings (e.g., History, Mechanism, Key Figures, Sub-types, Implications).
    * **Detailed Prose (Per Sub-Heading):** For *each* sub-heading, you must write extensive, detailed, and high-quality prose.
    * **Semantic Enrichment:** As you write, you MUST actively use the following callouts to structure the information:
        * `> [!atomic-concept]` (For breaking out a small, singular idea)
        * `> [!key-claim]` (For stating a central assertion)
        * `> [!evidence]` (To provide data, studies, or proof for a claim)
        * `> [!argument]` / `> [!counter-argument]` (To explore debates within the field)
        * `> [!analogy]` / `> [!example]` (To clarify complex points)
        * `> [!equation]` (If the topic is technical/mathematical)
        * `> [NOT-a-callout]` (Use `PC_Style-Quote_Integration` to embed `> [!quote]` and `> [!cite]` callouts where the author's voice is critical.)

 **4. Phase 3: PKB Integration & Exploration (The "New Avenues")**
    * **Goal:** This phase fulfills the "discovery" and "connection" requirements.
    * **Internal Connections:**
      * `> [!connections-and-links]`
      * `> Based on the `[EXISTING_CONCEPTS]` provided, explicitly state how this `[TOPIC]` connects to, expands upon, or challenges `[[Concept A]]` and `[[Theory B]]`."
    * **External Exploration:**
      * `> [!further-exploration]`
      * `> Generate a list of 3-5 *new* topics, concepts, or questions that emerged from this report. These are "new avenues" for me to explore.`
      * For each new avenue, format it as a `> [!topic-idea]` callout with a `[[New Wiki-Link]]`.

 **5. Phase 4: Synthesis & Reflection**
    * **Summary:** Conclude with a `> [!summary]` callout, synthesizing the *most important* insights.
    * **Prompt Reflection:**
      * `> [!ask-yourself-this]`
      * `> Generate 2-3 provocative questions for me (the user) to reflect on, based on this report.`

 **6. Phase 5: Metadata & Constraints**
    * Apply `PC_Format-Enriched_YAML`, `PC_Format-PKB_Linking`, and `PC_Constraint-Demand_Depth_No_SummarIES`

* **Important Notes:**
    * The depth and quality of the prose in Phase 2 are critical. This is where the "deep exposition" happens. Do not skimp on detail or clarity.
    * The use of callouts is not just for formatting; it is a deliberate strategy to structure the information in a way that enhances understanding and retention.
    * The connections made in Phase 3 should be explicit and meaningful, demonstrating how this topic fits into the broader landscape of knowledge in my PKB.  
    * The final output should be meticulously reviewed for coherence, accuracy, and depth, ensuring it meets the highest academic standards.
`````


# PKB Metadata Template
This final section is a YAML Metadata template that should be included at the beginning of each report.
- Ensuring consistent documentation and classification across my PKB.

```yaml
---
# DOCUMENT IDENTIFICATION

doc_id: {{Unique identifier for this document, e.g., "Foundational_Report_001"}}
doc_type: Foundational Report
doc_created: {{Creation date, e.g., "2024-06-01"}}
doc_modified: {{Last modified date, e.g., "2024-06-01"}}
author: {{Author's name, e.g., "ChatGPT"}}

# CLASSIFICATION & DISCOVERY
primary_domain: {{Primary domain of knowledge, e.g., "Cognitive Science"}}
secondary_domains: {{List of secondary domains, e.g., ["Philosophy", "Neuroscience"]}}
related_concepts: {{List of related concepts, e.g., ["[[Concept A]]", "[[Theory B]]"]}}
knowledge_level: {{Level of depth, e.g., "Encyclopedic overview", "In-depth technical analysis", "Historical context"}}
tags: {{List of relevant tags, e.g., ["#cognition", "#philosophy", "#neuroscience"]}}

# QUALITY & STATUS
status: {{Current status of the document, e.g., "evergreen", "draft", "needs review"}}
maturity: {{Maturity level, e.g., "highly developed", "in progress", "conceptual"}}
confidence: {{Confidence level in the content, e.g., "high", "medium", "low"}}

# REASONING ARCHITECTURE
reasoning_tier: {{Tier of reasoning, e.g., "Tier 1: Foundational Understanding", "Tier 2: Analytical Depth", "Tier 3: Synthesis & Innovation"}}
reasoning_methods: {{List of reasoning methods used, e.g., ["Deductive reasoning", "Inductive reasoning", "Analogical reasoning"]}}
reasoning_technique: {{Specific techniques employed, e.g., "Socratic questioning", "Thought experiments", "Comparative analysis"}}

# EPISTEMIC & VALIDATION
epistemic_status: {{Epistemic status, e.g., "well-established", "emerging theory", "speculative"}}
validation_methods: {{Methods used for validation, e.g., "Peer review", "Empirical evidence", "Logical consistency"}}
test_coverage: {{Scope of testing, e.g., "Comprehensive", "Limited", "Theoretical"}}
validation_results: {{Summary of validation results, e.g., "Consistent with existing literature", "Requires further empirical testing", "Contradicted by recent studies"}}
validation_date: {{Date of last validation, e.g., "2024-06-01"}}
factual_verification: {{Status of factual verification, e.g., "Verified", "Partially verified", "Not verified"}}
hallucination_check: {{Status of hallucination check, e.g., "True", "False"}}

# SOURCE & ATTRIBUTION
source: {{Primary source of information, e.g., "Academic journals", "Books", "Expert interviews", "claude-sonnet-4.5"}}
based_on_prompts: {{List of prompts used to generate the content, e.g., ["Prompt 1: Define the core principles of cognitive science", "Prompt 2: Explain the historical development of cognitive science"]}}

# KNOWLEDGE GRAPH INTEGRATION
related_concepts:
  - "[[Concept A]]"
  - "[[Theory B]]"

prerequisites:
  - "[[Prerequisite Concept 1]]"
  - "[[Prerequisite Concept 2]]"

builds_on:
  - "[[Theory X]]"
  - "[[Concept Y]]"

extends:
  - "[[Concept Z]]"
  - "[[Theory W]]"

# ALIASES & LINKING
aliases:
  - "[[Alias 1]]"
  - "[[Alias 2]]"

link_up: "[[Higher-Level Concept]]"
link_down: "[[Lower-Level Concept]]"
link_related:
  - "[[Related Concept 1]]"
  - "[[Related Concept 2]]"

# ADDITIONAL METADATA
summary: {{A brief summary of the document, e.g., "This report provides an in-depth analysis of the core principles of cognitive science, exploring its historical development, key theories, and implications for understanding human cognition."}}
keywords: {{List of keywords, e.g., ["cognition", "neuroscience", "philosophy", "cognitive science"]}}

---
```







# Complete Metadata Template Explanation

This is How the Yaml at the front Must look in order to be consistent with the rest of the PKB and to ensure that it is properly integrated into the knowledge graph. Each field should be filled out with accurate and relevant information to facilitate discovery, classification, and connection within the PKB.

---
# ═══════════════════════════════════════════════════════════════════════════
# CORE IDENTITY
# ═══════════════════════════════════════════════════════════════════════════
title: "Critical Thinking Skills and Metacognitive Self-Regulation"
aliases:
  - Critical Thinking Deployment
  - Metacognitive Self-Regulation in Reasoning
  - Applied Critical Thinking Framework
  - PENCRISAL-MAI Integration
  - CT-MSR Framework
  - Situational Critical Thinking
  - Metacognitive Control of Reasoning
  - Critical Thinking Architecture
type: permanent-note
status: evergreen
confidence: high

# ═══════════════════════════════════════════════════════════════════════════
# CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════════════
tags:
  # Content Type
  - permanent-note
  - academic-synthesis
  - reference-note
  - practical-framework
  
  # Domain (hierarchical)
  - cognitive-psychology/metacognition
  - cognitive-psychology/critical-thinking
  - educational-psychology/learning-strategies
  - cognitive-psychology/self-regulation
  
  # Methodology
  - empirical-research
  - assessment-frameworks
  - systematic-protocols
  - practical-application
  - evidence-based
  
  # Specific Frameworks
  - pencrisal-framework
  - mai-framework
  - epistemic-vigilance
  
  # Core Competencies
  - reasoning-skills
  - error-detection
  - transfer-learning
  - calibration-training
  - deployment-strategies
  
  # Status
  - evergreen
  - comprehensive
  - research-grounded

domain: cognitive-psychology
subdomains:
  - metacognition
  - critical-thinking
  - educational-psychology
  - self-regulated-learning

# ═══════════════════════════════════════════════════════════════════════════
# TEMPORAL
# ═══════════════════════════════════════════════════════════════════════════
created: 2026-02-01
updated: 2026-02-01

# ═══════════════════════════════════════════════════════════════════════════
# ACADEMIC METADATA
# ═══════════════════════════════════════════════════════════════════════════
source-type: academic-synthesis
research-base: empirical-studies
evidence-quality: high
peer-validation: multiple-frameworks

key-frameworks:
  - name: PENCRISAL
    description: "Five-dimensional critical thinking assessment (Deductive Reasoning, Inductive Reasoning, Practical Reasoning, Decision-Making, Problem-Solving)"
    developers: "Rivas & Saiz (2012)"
    validation: "psychometric-validated"
  
  - name: MAI
    description: "Metacognitive Awareness Inventory - 8 subdimensions across Knowledge and Regulation of Cognition"
    developers: "Schraw & Dennison (1994)"
    validation: "widely-validated"
  
  - name: EEVF
    description: "Extended Epistemic Vigilance Framework - 3-dimensional evaluation (Source, Claim, Receiver)"
    developers: "Sperber et al. (2010), Bielik & Krüger (2024)"
    validation: "empirically-supported"
  
  - name: Halpern Transfer Model
    description: "Four-component framework for critical thinking transfer across domains"
    developers: "Halpern (1998)"
    validation: "empirically-validated"

key-researchers:
  - Diane Halpern
  - Gregory Schraw
  - Carlos Saiz
  - Dan Sperber
  - Hugo Mercier
  - Raymond Dennison

# ═══════════════════════════════════════════════════════════════════════════
# CONTENT CHARACTERISTICS
# ═══════════════════════════════════════════════════════════════════════════
word-count: 6200
complexity-level: advanced-practitioner
target-audience: "Intermediate to Advanced learners in cognitive psychology, educators, professionals seeking systematic reasoning improvement"
depth-level: comprehensive
treatment-type: practical-deployment-focused

practical-components:
  - operational-templates
  - decision-protocols
  - calibration-exercises
  - debugging-workflows
  - self-assessment-tools
  - monitoring-checklists

# ═══════════════════════════════════════════════════════════════════════════
# CORE CONCEPTS
# ═══════════════════════════════════════════════════════════════════════════
core-concepts:
  - Metacognitive Self-Regulation as Cognitive Control System
  - PENCRISAL Five-Dimensional Framework
  - Transfer Problem and Domain-Specificity
  - Recognition Patterns for Deployment Triggers
  - Knowledge of Cognition (Declarative, Procedural, Conditional)
  - Regulation of Cognition (Planning, Monitoring, Evaluation, Information Management, Debugging)
  - Epistemic Vigilance Three-Dimensional Model
  - Confidence Calibration Training
  - Structural Encoding for Transfer
  - Systematic Error Debugging Protocols

key-distinctions:
  - "Domain-General vs Domain-Specific Critical Thinking"
  - "Monitoring vs Control in Metacognition"
  - "Knowledge of Cognition vs Regulation of Cognition"
  - "Immersion vs Infusion Instructional Approaches"
  - "System 1 vs System 2 Deployment Triggers"
  - "Overconfidence vs Underconfidence Calibration Errors"

# ═══════════════════════════════════════════════════════════════════════════
# RELATIONSHIPS
# ═══════════════════════════════════════════════════════════════════════════
prerequisites:
  - "[[Introduction-to-Critical-Thinking]]"
  - "[[Metacognition Fundamentals]]"
  - "[[Basic Argument Analysis]]"
  - "[[Logical Reasoning Foundations]]"

related:
  - "[[Metacognition]]"
  - "[[PENCRISAL Assessment Framework]]"
  - "[[Metacognitive-Awareness-Inventory]]"
  - "[[Epistemic-Vigilance]]"
  - "[[Dual-Process-Theory]]"
  - "[[Cognitive-Load-Theory]]"
  - "[[Argument-Analysis]]"
  - "[[Decision Making Under Uncertainty]]"
  - "[[Cognitive Biases and Debiasing]]"
  - "[[Scientific-Reasoning]]"
  - "[[Transfer-of-Learning]]"
  - "[[Self-Regulated-Learning]]"
  - "[[Confirmation-Bias]]"
  - "[[Availability-Heuristic]]"
  - "[[Anchoring Bias]]"

broader:
  - "[[cognitive-psychology]]"
  - "[[Educational-Psychology]]"
  - "[[Applied Epistemology]]"
  - "[[Rationality Studies]]"

narrower:
  - "[[Deductive Reasoning Techniques]]"
  - "[[Inductive Reasoning Strategies]]"
  - "[[Practical Reasoning in Real-World Contexts]]"
  - "[[Metacognitive Monitoring Protocols]]"
  - "[[Calibration Training Methods]]"
  - "[[Debugging Strategies for Reasoning Errors]]"
  - "[[Structural Encoding Techniques]]"

see-also:
  - "[[Working Memory and Executive Function]]"
  - "[[Expertise-Development]]"
  - "[[Reflective-Judgment-Model]]"
  - "[[Intellectual-Humility]]"
  - "[[Bayesian-Reasoning]]"
  - "[[Argument-Mapping]]"
  - "[[Socratic-Questioning]]"
  - "[[Pre-Mortem-Analysis]]"
  - "[[Red-Team-Thinking]]"
  - "[[Cognitive-Forcing-Functions]]"

contrasts-with:
  - "[[Heuristic-Based Decision Making]]"
  - "[[Intuitive Judgment]]"
  - "[[Unconscious Competence]]"

applied-in:
  - "[[Professional Decision Making]]"
  - "[[Academic Research]]"
  - "[[Strategic-Planning]]"
  - "[[Problem Solving in Complex Domains]]"
  - "[[Evidence-Based Practice]]"

# ═══════════════════════════════════════════════════════════════════════════
# LEARNING PATHWAYS
# ═══════════════════════════════════════════════════════════════════════════
builds-on:
  - "[[Foundational-Logic]]"
  - "[[Cognitive-Development-Theory]]"
  - "[[Information-Processing-Models]]"

enables:
  - "[[Advanced Reasoning Techniques]]"
  - "[[Domain-Specific Critical Thinking]]"
  - "[[Debiasing-Interventions]]"
  - "[[Metacognitive Instruction Design]]"
  - "[[Epistemic Virtue Development]]"

expansion-topics:
  - topic: "[[Domain-Specific Critical Thinking Standards]]"
    description: "Field-specific criteria and recognition patterns for professional contexts"
    priority: high
  
  - topic: "[[Metacognitive Intervention Design]]"
    description: "Systematic protocols for targeting specific metacognitive deficiencies"
    priority: high
  
  - topic: "[[Cognitive Bias Mitigation Protocols]]"
    description: "Operational detection and correction algorithms for specific biases"
    priority: medium
  
  - topic: "[[Transfer-Enabling Pedagogical Frameworks]]"
    description: "Instructional design for building transferable competencies"
    priority: medium
  
  - topic: "[[Epistemic Humility and Intellectual Virtue]]"
    description: "Dispositional foundations supporting critical thinking deployment"
    priority: medium

# ═══════════════════════════════════════════════════════════════════════════
# PRACTICAL APPLICATION
# ═══════════════════════════════════════════════════════════════════════════
use-cases:
  - Personal decision-making improvement
  - Professional reasoning enhancement
  - Educational instruction design
  - Research methodology
  - Strategic planning
  - Quality assurance protocols

deployment-contexts:
  - High-stakes decisions
  - Persuasive communication evaluation
  - Complex problem-solving
  - Evidence assessment
  - Strategic planning
  - Learning and skill development

tools-provided:
  - Pre-task planning protocol
  - Monitoring checkpoint template
  - Post-task reflection framework
  - Error debugging workflow
  - Calibration training exercise
  - MAI self-assessment guide
  - Recognition pattern checklist

# ═══════════════════════════════════════════════════════════════════════════
# QUALITY INDICATORS
# ═══════════════════════════════════════════════════════════════════════════
empirical-support:
  - PENCRISAL validation studies (Rivas & Saiz, 2012, 2015)
  - MAI psychometric validation (Schraw & Dennison, 1994)
  - Transfer research (Halpern, 1998; Tiruneh et al., 2017)
  - Epistemic vigilance studies (Sperber et al., 2010)
  - Metacognition-CT relationship studies (Magno, 2010; Ku & Ho, 2010)

validation-evidence:
  - Longitudinal persistence of training effects
  - Cross-cultural replication
  - Convergent validity with multiple instruments
  - Predictive validity for academic performance
  - Structural equation modeling support

limitations-noted:
  - Optimal balance of explicit vs implicit instruction remains debated
  - Domain specificity vs generality tension
  - Limited long-term naturalistic validation
  - Individual difference moderators not fully characterized

# ═══════════════════════════════════════════════════════════════════════════
# DOCUMENT STRUCTURE
# ═══════════════════════════════════════════════════════════════════════════
sections:
  - Abstract and Executive Overview
  - Architectural Foundation (Metacognitive Engine)
  - Deployment Challenge (Recognition Patterns)
  - Critical Thinking Skills (PENCRISAL Framework)
  - Transfer Problem
  - Metacognitive Deployment Protocols
  - Error Detection and Correction
  - Self-Assessment Frameworks
  - Bridging Transfer Gap
  - Synthesis and Integration
  - References and Resources

document-features:
  - callouts: 17
  - wiki-links: 27+
  - empirical-citations: 15+
  - operational-templates: 7
  - framework-integrations: 4
  - practical-examples: 12+

# ═══════════════════════════════════════════════════════════════════════════
# PERSONAL KNOWLEDGE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════
review-frequency: quarterly
mastery-stage: budding
importance: critical
foundational-for-future-learning: true

connection-strength:
  high:
    - Metacognition
    - Critical Thinking
    - Transfer of Learning
  medium:
    - Cognitive Biases
    - Decision Making
    - Self-Regulated Learning
  exploratory:
    - Expertise Development
    - Instructional Design
    - Epistemic Virtue

# ═══════════════════════════════════════════════════════════════════════════
# CUSTOM METADATA
# ═══════════════════════════════════════════════════════════════════════════
pencrisal-dimensions:
  - Deductive Reasoning
  - Inductive Reasoning
  - Practical Reasoning
  - Decision-Making
  - Problem-Solving

mai-dimensions:
  knowledge:
    - Declarative Knowledge
    - Procedural Knowledge
    - Conditional Knowledge
  regulation:
    - Planning
    - Information Management
    - Comprehension Monitoring
    - Debugging Strategies
    - Evaluation

eevf-dimensions:
  - Source Evaluation
  - Claim Evaluation
  - Receiver Self-Evaluation

assessment-instruments:
  - PENCRISAL (35 items, 0-70 scale)
  - MAI (52 items, two-factor structure)
  - Holistic Critical Thinking Scoring Rubric
  - Watson-Glaser Critical Thinking Test (referenced)
  - Cornell Critical Thinking Tests (referenced)

---
