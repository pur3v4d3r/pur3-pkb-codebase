
# PKM Templates / Scaffolds

## Idea for a Claude Project System Prompt

I have an idea for a Claude Project System Prompt that can:

1. Research and gather information for generating cognitively aligned templates and scaffolds for PKM (Personal Knowledge Management) systems, that will be filled out by the user.
2. Generate templates and scaffolds that are cognitively aligned and tailored to specific PKM needs, based on the gathered information.
3. Provide recommendations for implementing and using the generated templates effectively in a PKM system.
4. Provide recommendations for customizing and adapting the generated templates to fit individual preferences and workflows in a PKM system.
5. Provide recommendations for new templates and scaffolds that can be developed to further enhance PKM systems based on emerging trends and user feedback.
6. Review filled templates and scaffolds to provide feedback and suggestions for improvement based on cognitive principles and best practices in PKM.
7. Use any methods or techniques that can enhance the quality and effectiveness of the generated templates and scaffolds, such as user-centered design, iterative development, and evidence-based practices in PKM.
8. Use any relevant information from the PKB to inform the generation of templates and scaffolds, ensuring that they are well-integrated into the overall knowledge management system.
   1. Meaing the use of varios plugins and tools to access and utilize the information in the PKB effectively for template generation.

    These can include the use of:
    - Templater
    - Dataview
    - Any other relevant plugins or tools that can enhance the template generation process and ensure that the generated templates are well-aligned with the user's PKM system and needs.

## Template & Scaffold MUST-HAVE Features:

- Clear and concise instructions for using the template effectively in a PKM system.
- Cognitive alignment with principles of learning and memory.
- Engaging design that enhances usability and engagement.
- Integration with Obsidian.
- Any other features that enhance the functionality and usability of the template in a PKM system.
- Any other useful information that can help the user engage with and effectively use the templates in their PKM system.

## Types of Templates and Scaffolds:

- Project Planning Templates
- Task Planning Templates
- Metacognition Templates
- Reflection Templates
- Self-Assessment Templates
- Problem-Solving Templates
- Decision-Making Templates
- Critical Thinking Templates
- Creative Thinking Templates
- Socratic Questioning Templates
- Mind Mapping Templates
- Concept Mapping Templates
- Note-Taking Templates

## Metadata for Each Template and Scaffold:

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







# Metadata Template Example

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
  - "[[Decision-Making-Under-Uncertainty]]"
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
  - "[[Evidence-Based-Practice]]"

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
