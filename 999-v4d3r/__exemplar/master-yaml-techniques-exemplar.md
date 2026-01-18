





`````yaml
# ═══════════════════════════════════════════════════════════════════════════════
# PROMPT ENGINEERING MASTER REFERENCE ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════════
# A comprehensive YAML schema covering all dimensions of prompt engineering
# best practices for LLM interaction design and optimization.
#
# Version: 1.0.0
# Created: 2025-12-27
# Status: Production Reference
# Schema: PKB-Compatible Dataview Structure
# ═══════════════════════════════════════════════════════════════════════════════

---
# ┌─────────────────────────────────────────────────────────────────────────────┐
# │                     SECTION 1: DOCUMENT METADATA                             │
# └─────────────────────────────────────────────────────────────────────────────┘

document_metadata:
  title: "Prompt Engineering Master Reference Architecture"
  description: >-
    Exhaustive compilation of prompt engineering principles, techniques,
    patterns, and best practices for designing effective LLM interactions.
    Structured for PKB integration with Dataview-compatible inline fields
    and wiki-link ready terminology.
  
  classification:
    domain: "Artificial Intelligence"
    subdomain: "Language Model Engineering"
    specialty: "Prompt Design & Optimization"
    content_type: "Reference Schema"
    knowledge_level: "Advanced Practitioner"
  
  versioning:
    schema_version: "1.0.0"
    last_updated: "2025-12-27"
    stability: "stable"
    backwards_compatible: true
  
  provenance:
    primary_sources:
      - "Anthropic Claude Documentation"
      - "OpenAI Prompt Engineering Guide"
      - "DAIR.AI Prompt Engineering Guide"
      - "Academic Research Literature"
    synthesis_method: "Cross-Source Integration"
    validation_status: "Peer-Reviewed Synthesis"

---
# ┌─────────────────────────────────────────────────────────────────────────────┐
# │                SECTION 2: FOUNDATIONAL PRINCIPLES                            │
# └─────────────────────────────────────────────────────────────────────────────┘

foundational_principles:
  
  # ═══════════════════════════════════════════════════════════════════════════
  # 2.1 CORE AXIOMS
  # ═══════════════════════════════════════════════════════════════════════════
  
  core_axioms:
    description: >-
      Fundamental truths that underpin all effective prompt engineering.
      These axioms should inform every design decision.
    
    axioms:
      
      - id: "AX-001"
        name: "Explicitness Axiom"
        statement: "Models cannot reliably infer intent - state requirements explicitly"
        rationale: >-
          LLMs process text probabilistically; implicit expectations produce
          inconsistent outputs. Explicit instruction reduces ambiguity and
          improves reproducibility.
        implementation_guidance:
          - "Specify exact output format, not just topic"
          - "State constraints directly rather than hoping they're inferred"
          - "Include edge case handling instructions proactively"
        anti_patterns:
          - "Assuming the model 'knows what you mean'"
          - "Relying on implicit context from prior messages"
          - "Vague instructions like 'make it good'"
        related_concepts:
          - "[[Instruction Clarity]]"
          - "[[Specification Completeness]]"
          - "[[Disambiguation Strategies]]"
      
      - id: "AX-002"
        name: "Context Primacy Axiom"
        statement: "Context quality determines output quality more than instruction complexity"
        rationale: >-
          Models generate outputs conditioned on provided context. Rich,
          relevant context enables more accurate and nuanced responses
          than sophisticated instruction alone.
        implementation_guidance:
          - "Provide comprehensive background before posing questions"
          - "Include domain-specific terminology definitions when relevant"
          - "Supply examples of desired outputs within context"
        anti_patterns:
          - "Minimal context with complex instructions"
          - "Assuming shared knowledge exists"
          - "Omitting relevant constraints or requirements"
        related_concepts:
          - "[[Context Engineering]]"
          - "[[Information Density]]"
          - "[[Retrieval Augmented Generation]]"
      
      - id: "AX-003"
        name: "Decomposition Axiom"
        statement: "Complex tasks succeed through systematic decomposition into subtasks"
        rationale: >-
          Single-prompt complexity has diminishing returns. Breaking complex
          workflows into discrete, focused steps improves accuracy, enables
          validation, and allows targeted optimization.
        implementation_guidance:
          - "Identify natural task boundaries before prompting"
          - "Create validation checkpoints between stages"
          - "Design prompts that do one thing excellently"
        anti_patterns:
          - "Cramming multiple objectives into single prompts"
          - "Expecting complex multi-step reasoning in one pass"
          - "Skipping intermediate validation steps"
        related_concepts:
          - "[[Prompt Chaining]]"
          - "[[Task Decomposition]]"
          - "[[Agentic Workflows]]"
      
      - id: "AX-004"
        name: "Iteration Axiom"
        statement: "Optimal prompts emerge through systematic iteration, not initial design"
        rationale: >-
          First-draft prompts rarely achieve optimal performance. Systematic
          testing, failure analysis, and refinement produce production-ready
          prompts. Expect 5-20 iterations for complex use cases.
        implementation_guidance:
          - "Establish baseline metrics before optimization"
          - "Change one variable at a time during testing"
          - "Document successful patterns and failure modes"
        anti_patterns:
          - "Assuming first attempt is sufficient"
          - "Random modification without systematic testing"
          - "Abandoning approaches too quickly"
        related_concepts:
          - "[[Prompt Optimization]]"
          - "[[A/B Testing]]"
          - "[[Evaluation Frameworks]]"
      
      - id: "AX-005"
        name: "Positive Instruction Axiom"
        statement: "Specify desired behaviors rather than prohibited behaviors"
        rationale: >-
          Research demonstrates LLMs process affirmative instructions more
          reliably than negations. "Do X" outperforms "Don't do Y" across
          model families and task types.
        implementation_guidance:
          - "Reframe prohibitions as positive requirements"
          - "Describe desired output characteristics directly"
          - "Use 'instead of X, do Y' constructions when necessary"
        anti_patterns:
          - "Lists of 'don't do' instructions"
          - "Negative constraint cascades"
          - "Prohibition-heavy system prompts"
        related_concepts:
          - "[[Affirmative Framing]]"
          - "[[Constraint Specification]]"
          - "[[Behavioral Guidance]]"
      
      - id: "AX-006"
        name: "Model Calibration Axiom"
        statement: "Different models require different prompting strategies"
        rationale: >-
          Model architectures, training data, and RLHF procedures create
          distinct behavioral profiles. Prompt strategies must be calibrated
          to specific model characteristics for optimal results.
        implementation_guidance:
          - "Test prompts across target models before deployment"
          - "Maintain model-specific prompt variants when necessary"
          - "Document model-specific optimization findings"
        anti_patterns:
          - "Assuming universal prompt transferability"
          - "Ignoring model-specific documentation"
          - "One-size-fits-all deployment strategies"
        related_concepts:
          - "[[Model-Specific Optimization]]"
          - "[[Cross-Model Testing]]"
          - "[[Model Behavior Profiles]]"

  # ═══════════════════════════════════════════════════════════════════════════
  # 2.2 DESIGN PRINCIPLES
  # ═══════════════════════════════════════════════════════════════════════════
  
  design_principles:
    description: >-
      Actionable principles that translate axioms into prompt design decisions.
      Apply these principles consistently across prompt development workflows.
    
    principles:
      
      - id: "DP-001"
        name: "Clarity Over Cleverness"
        category: "Communication"
        priority: "Critical"
        statement: >-
          Clear, direct language outperforms sophisticated phrasing.
          Optimize for unambiguous interpretation, not linguistic elegance.
        implementation:
          do:
            - "Use simple sentence structures"
            - "Define technical terms when first introduced"
            - "Prefer concrete nouns over abstract references"
            - "Use consistent terminology throughout"
          avoid:
            - "Nested conditional instructions"
            - "Ambiguous pronoun references"
            - "Domain jargon without definition"
            - "Synonym variation for style"
        metrics:
          - "Instruction parse accuracy"
          - "Output consistency rate"
          - "Error rate under ambiguity"
      
      - id: "DP-002"
        name: "Structured Over Freeform"
        category: "Organization"
        priority: "High"
        statement: >-
          Structural markers improve instruction processing. Use XML tags,
          delimiters, headers, and explicit section boundaries to organize
          complex prompts.
        implementation:
          do:
            - "Use XML tags for distinct content sections"
            - "Apply consistent delimiter patterns"
            - "Create hierarchical instruction organization"
            - "Separate context, instructions, and examples"
          avoid:
            - "Unstructured prose for complex instructions"
            - "Mixing content types without markers"
            - "Implicit section boundaries"
        recommended_patterns:
          xml_tags:
            - "<context></context>"
            - "<instructions></instructions>"
            - "<examples></examples>"
            - "<constraints></constraints>"
            - "<output_format></output_format>"
          delimiters:
            - "Triple quotes: '''"
            - "Triple backticks: ```"
            - "Section markers: ---"
            - "Bullet hierarchies"
      
      - id: "DP-003"
        name: "Examples Over Descriptions"
        category: "Demonstration"
        priority: "High"
        statement: >-
          Concrete examples communicate requirements more reliably than
          abstract descriptions. When possible, show rather than tell.
        implementation:
          do:
            - "Provide input-output pairs for format specification"
            - "Include edge case examples"
            - "Demonstrate reasoning patterns explicitly"
            - "Show both correct and incorrect examples when helpful"
          avoid:
            - "Purely abstract format descriptions"
            - "Assuming format inference from description"
            - "Examples that don't cover edge cases"
        example_quality_criteria:
          - "Representative of target distribution"
          - "Clear input-output mapping"
          - "Includes reasoning when relevant"
          - "Covers boundary conditions"
      
      - id: "DP-004"
        name: "Graduated Complexity"
        category: "Architecture"
        priority: "Medium"
        statement: >-
          Build prompt complexity incrementally. Start with minimal viable
          prompts, add complexity only as demonstrated necessary.
        implementation:
          do:
            - "Begin with zero-shot baseline"
            - "Add few-shot examples if zero-shot fails"
            - "Introduce CoT only if reasoning quality insufficient"
            - "Add constraints incrementally"
          avoid:
            - "Over-engineering initial prompts"
            - "Premature optimization"
            - "Unnecessary complexity overhead"
        complexity_progression:
          level_1: "Zero-shot with clear instruction"
          level_2: "Zero-shot with format specification"
          level_3: "Few-shot with 1-3 examples"
          level_4: "Few-shot with CoT reasoning"
          level_5: "Chained prompts with validation"
          level_6: "Agentic workflows with tool use"
      
      - id: "DP-005"
        name: "Output Anchoring"
        category: "Control"
        priority: "High"
        statement: >-
          Constrain output space through explicit format specification,
          prefilling, and structural templates. Reduce degrees of freedom
          to improve consistency.
        implementation:
          do:
            - "Specify exact output format (JSON, XML, Markdown, etc.)"
            - "Use prefilling to begin response in desired format"
            - "Provide template structures for complex outputs"
            - "Request specific field presence/absence"
          avoid:
            - "Open-ended format requests"
            - "Implicit format expectations"
            - "Allowing model to choose output structure"
        prefilling_patterns:
          json_output: |
            Assistant: {
              "result":
          markdown_output: |
            Assistant: # Analysis Results
            
            ## Summary
          code_output: |
            Assistant: ```python
            def
      
      - id: "DP-006"
        name: "Uncertainty Acknowledgment"
        category: "Reliability"
        priority: "Medium"
        statement: >-
          Explicitly permit and encourage uncertainty expression. Calibrated
          confidence improves output reliability and trustworthiness.
        implementation:
          do:
            - "Include 'if uncertain, say so' instructions"
            - "Request confidence levels with assertions"
            - "Allow 'I don't know' responses"
            - "Ask for evidence citations when factual"
          avoid:
            - "Forcing definitive answers always"
            - "Penalizing uncertainty expression"
            - "Implicit expectation of omniscience"
        uncertainty_prompts:
          calibration: "Rate your confidence in this answer from 1-5"
          acknowledgment: "If you're unsure, say so rather than guessing"
          evidence: "Cite the basis for your conclusions"
          limitations: "Note any limitations in your analysis"

---
# ┌─────────────────────────────────────────────────────────────────────────────┐
# │                   SECTION 3: PROMPTING TECHNIQUES                            │
# └─────────────────────────────────────────────────────────────────────────────┘

prompting_techniques:
  
  # ═══════════════════════════════════════════════════════════════════════════
  # 3.1 FOUNDATIONAL TECHNIQUES
  # ═══════════════════════════════════════════════════════════════════════════
  
  foundational_techniques:
    description: >-
      Core prompting patterns that form the basis of LLM interaction.
      Master these before proceeding to advanced techniques.
    
    techniques:
      
      # ─────────────────────────────────────────────────────────────────────────
      # ZERO-SHOT PROMPTING
      # ─────────────────────────────────────────────────────────────────────────
      
      - id: "FT-001"
        name: "Zero-Shot Prompting"
        aliases:
          - "Direct Prompting"
          - "Instruction-Only Prompting"
        
        definition: >-
          Providing task instructions without any demonstration examples,
          relying solely on the model's pre-trained knowledge and instruction-
          following capabilities to generate appropriate outputs.
        
        theoretical_basis:
          mechanism: >-
            Leverages knowledge encoded during pre-training and instruction
            tuning. The model maps novel instructions to learned behavioral
            patterns without task-specific examples.
          cognitive_analog: >-
            Analogous to human ability to follow novel instructions based
            on general language understanding and world knowledge.
          key_research:
            - paper: "Language Models are Zero-Shot Learners"
              authors: "Brown et al."
              year: 2020
              finding: "GPT-3 demonstrates strong zero-shot capabilities"
            - paper: "FLAN: Finetuned Language Models are Zero-Shot Learners"
              authors: "Wei et al."
              year: 2022
              finding: "Instruction tuning dramatically improves zero-shot performance"
        
        when_to_use:
          optimal_conditions:
            - "Well-defined, common tasks (summarization, translation, QA)"
            - "Tasks with clear success criteria"
            - "When speed/simplicity outweighs marginal accuracy gains"
            - "Initial baseline establishment before optimization"
          suboptimal_conditions:
            - "Tasks requiring specific output formats"
            - "Domain-specific terminology or conventions"
            - "Complex multi-step reasoning"
            - "Rare or unusual task types"
        
        implementation_patterns:
          basic_structure:
            template: |
              [Task Description]
              
              [Input Data]
              
              [Output Specification]
            components:
              task_description:
                purpose: "Define what the model should do"
                requirements:
                  - "Clear action verb"
                  - "Specific scope definition"
                  - "Quality criteria when relevant"
              input_data:
                purpose: "Provide material to process"
                requirements:
                  - "Clear delimiters"
                  - "Consistent formatting"
                  - "Relevant context included"
              output_specification:
                purpose: "Constrain response format"
                requirements:
                  - "Explicit format type"
                  - "Length guidance"
                  - "Structure requirements"
          
          enhanced_patterns:
            
            with_role_context:
              template: |
                You are a [role with relevant expertise].
                
                Task: [specific instruction]
                
                Input: [data to process]
                
                Provide your response in [format specification].
              rationale: "Role context activates relevant knowledge"
            
            with_constraints:
              template: |
                [Task instruction]
                
                Requirements:
                - [Constraint 1]
                - [Constraint 2]
                - [Constraint 3]
                
                Input: [data]
                
                Output:
              rationale: "Explicit constraints reduce output variance"
            
            with_quality_anchors:
              template: |
                [Task instruction]
                
                Quality criteria:
                - [Criterion 1]: [specific measure]
                - [Criterion 2]: [specific measure]
                
                Input: [data]
                
                Generate a high-quality response that meets all criteria.
              rationale: "Quality anchors guide output optimization"
        
        optimization_strategies:
          instruction_refinement:
            - "Use precise, unambiguous verbs"
            - "Specify scope boundaries explicitly"
            - "Include success criteria in instruction"
          format_control:
            - "Request specific output structure"
            - "Use prefilling for format enforcement"
            - "Provide output templates"
          context_enhancement:
            - "Add domain-relevant context"
            - "Include constraint specifications"
            - "Provide goal/purpose clarification"
        
        evaluation_metrics:
          accuracy:
            description: "Correctness of output relative to ground truth"
            measurement: "Task-specific accuracy scoring"
          consistency:
            description: "Output variance across multiple runs"
            measurement: "Standard deviation of quality scores"
          format_compliance:
            description: "Adherence to specified output format"
            measurement: "Structural validation pass rate"
        
        common_failure_modes:
          - failure: "Format deviation"
            cause: "Insufficient format specification"
            mitigation: "Add explicit format examples or prefilling"
          - failure: "Scope creep"
            cause: "Ambiguous task boundaries"
            mitigation: "Define explicit scope constraints"
          - failure: "Quality inconsistency"
            cause: "Underspecified quality criteria"
            mitigation: "Add specific quality anchors"
        
        related_concepts:
          - "[[Few-Shot Prompting]]"
          - "[[Instruction Tuning]]"
          - "[[In-Context Learning]]"
      
      # ─────────────────────────────────────────────────────────────────────────
      # FEW-SHOT PROMPTING
      # ─────────────────────────────────────────────────────────────────────────
      
      - id: "FT-002"
        name: "Few-Shot Prompting"
        aliases:
          - "In-Context Learning"
          - "Demonstration-Based Prompting"
          - "Example-Guided Prompting"
        
        definition: >-
          Providing the model with a small number (typically 1-10) of
          input-output demonstration examples before the target input,
          enabling task learning from examples without weight updates.
        
        theoretical_basis:
          mechanism: >-
            Models identify patterns from demonstrations and apply learned
            mappings to novel inputs. This leverages in-context learning
            capabilities that emerge from pre-training on diverse text.
          cognitive_analog: >-
            Similar to human learning by analogy - understanding a task
            through concrete examples rather than abstract descriptions.
          key_research:
            - paper: "Language Models are Few-Shot Learners"
              authors: "Brown et al."
              year: 2020
              finding: "Few-shot significantly outperforms zero-shot for most tasks"
            - paper: "Rethinking the Role of Demonstrations"
              authors: "Min et al."
              year: 2022
              finding: "Label space and input format matter more than label correctness"
        
        when_to_use:
          optimal_conditions:
            - "Tasks requiring specific output format/structure"
            - "Domain-specific conventions or terminology"
            - "Pattern-based transformations"
            - "When zero-shot accuracy is insufficient"
          suboptimal_conditions:
            - "Context window limitations"
            - "Highly diverse output requirements"
            - "Tasks with rare edge cases"
        
        example_selection_criteria:
          diversity:
            description: "Examples should cover the input distribution"
            implementation:
              - "Include edge cases alongside typical cases"
              - "Vary input characteristics (length, complexity, domain)"
              - "Represent different output patterns when applicable"
          relevance:
            description: "Examples should be similar to target inputs"
            implementation:
              - "Match input domain and format"
              - "Use semantically similar examples for best transfer"
              - "Consider dynamic example selection based on input"
          quality:
            description: "Examples must demonstrate correct behavior"
            implementation:
              - "Verify output correctness rigorously"
              - "Ensure examples meet all quality criteria"
              - "Include reasoning when demonstrating complex tasks"
          ordering:
            description: "Example order affects model behavior"
            implementation:
              - "Place most relevant examples closer to target input"
              - "Consider recency bias - recent examples have stronger effect"
              - "Use consistent ordering for reproducibility"
        
        implementation_patterns:
          
          standard_few_shot:
            template: |
              [Task description]
              
              Example 1:
              Input: [example input 1]
              Output: [example output 1]
              
              Example 2:
              Input: [example input 2]
              Output: [example output 2]
              
              Example 3:
              Input: [example input 3]
              Output: [example output 3]
              
              Now apply the same pattern:
              Input: [target input]
              Output:
            optimal_example_count: "3-5 for most tasks"
          
          with_explanations:
            template: |
              [Task description]
              
              Example 1:
              Input: [example input 1]
              Reasoning: [explanation of approach]
              Output: [example output 1]
              
              Example 2:
              Input: [example input 2]
              Reasoning: [explanation of approach]
              Output: [example output 2]
              
              Now apply the same approach:
              Input: [target input]
              Reasoning:
            rationale: "Explanations improve reasoning transfer"
          
          structured_examples:
            template: |
              <task_description>
              [Clear task specification]
              </task_description>
              
              <examples>
              <example id="1">
              <input>[example input]</input>
              <output>[example output]</output>
              </example>
              
              <example id="2">
              <input>[example input]</input>
              <output>[example output]</output>
              </example>
              </examples>
              
              <target>
              <input>[target input]</input>
              <output>
            rationale: "XML structure improves parsing reliability"
        
        optimization_strategies:
          example_count_tuning:
            guidance:
              - "Start with 3 examples as baseline"
              - "Add examples if output quality insufficient"
              - "Reduce if approaching context limits"
              - "Monitor diminishing returns (typically 5-8 examples)"
          dynamic_selection:
            guidance:
              - "Select examples most similar to target input"
              - "Use embedding similarity for selection"
              - "Consider task-specific relevance metrics"
          example_engineering:
            guidance:
              - "Craft examples that highlight key patterns"
              - "Include challenging edge cases"
              - "Ensure examples don't introduce bias"
        
        common_failure_modes:
          - failure: "Pattern overfitting"
            cause: "Examples too similar to each other"
            mitigation: "Increase example diversity"
          - failure: "Context exhaustion"
            cause: "Too many examples consume context window"
            mitigation: "Reduce example count or length"
          - failure: "Conflicting examples"
            cause: "Examples demonstrate inconsistent patterns"
            mitigation: "Audit examples for consistency"
          - failure: "Label leakage"
            cause: "Examples give away target answer"
            mitigation: "Ensure examples don't overlap with targets"
        
        related_concepts:
          - "[[Zero-Shot Prompting]]"
          - "[[Chain-of-Thought Prompting]]"
          - "[[In-Context Learning]]"
          - "[[Dynamic Example Selection]]"
      
      # ─────────────────────────────────────────────────────────────────────────
      # ROLE/PERSONA PROMPTING
      # ─────────────────────────────────────────────────────────────────────────
      
      - id: "FT-003"
        name: "Role/Persona Prompting"
        aliases:
          - "Character Prompting"
          - "Expert Persona"
          - "Role Assignment"
        
        definition: >-
          Assigning the model a specific role, character, or expertise profile
          that shapes response characteristics including knowledge focus,
          communication style, and reasoning approach.
        
        theoretical_basis:
          mechanism: >-
            Role assignment activates relevant knowledge clusters and behavioral
            patterns learned during pre-training. Personas condition the model's
            response distribution toward role-appropriate outputs.
          cognitive_analog: >-
            Similar to human role-taking behavior where adopting a professional
            identity influences communication patterns and knowledge access.
        
        when_to_use:
          optimal_conditions:
            - "Tasks requiring domain expertise"
            - "Desired communication style differs from default"
            - "Consistent persona needed across interactions"
            - "Specialized vocabulary or conventions required"
          suboptimal_conditions:
            - "Tasks requiring pure factual accuracy"
            - "When persona might introduce unwanted bias"
            - "Simple tasks without style requirements"
        
        persona_design_dimensions:
          expertise:
            description: "Domain knowledge and skill level"
            examples:
              - "Senior software engineer with 15 years experience"
              - "Board-certified physician specializing in cardiology"
              - "Tenured professor of cognitive psychology"
          communication_style:
            description: "How the persona communicates"
            examples:
              - "Technical and precise"
              - "Accessible and educational"
              - "Socratic and questioning"
          perspective:
            description: "Viewpoint and approach to problems"
            examples:
              - "Risk-averse and thorough"
              - "Innovative and experimental"
              - "Pragmatic and results-oriented"
          constraints:
            description: "Limitations and boundaries of the role"
            examples:
              - "Within ethical guidelines of profession"
              - "Acknowledges limitations of expertise"
              - "Defers to specialists when appropriate"
        
        implementation_patterns:
          
          minimal_role:
            template: |
              You are a [role].
              
              [Task instruction]
            use_case: "Simple expertise activation"
          
          detailed_persona:
            template: |
              You are [Name], a [role] with [experience/credentials].
              
              Your approach is characterized by:
              - [Key characteristic 1]
              - [Key characteristic 2]
              - [Key characteristic 3]
              
              Communication style: [style description]
              
              [Task instruction]
            use_case: "Consistent persona across complex tasks"
          
          multi_perspective:
            template: |
              Consider this problem from multiple expert perspectives:
              
              As a [Role 1], you would focus on: [perspective]
              As a [Role 2], you would emphasize: [perspective]
              As a [Role 3], you would consider: [perspective]
              
              Now synthesize these perspectives:
              [Task instruction]
            use_case: "Multi-faceted analysis"
        
        optimization_strategies:
          role_specificity:
            guidance:
              - "More specific roles activate more relevant knowledge"
              - "Include credentials/experience for expertise depth"
              - "Specify industry or domain context"
          behavioral_anchoring:
            guidance:
              - "Describe how the persona approaches problems"
              - "Include communication style preferences"
              - "Specify reasoning methodology"
          consistency_maintenance:
            guidance:
              - "Use consistent persona across prompt chain"
              - "Reinforce key persona traits in complex prompts"
              - "Include persona reminders in long conversations"
        
        common_failure_modes:
          - failure: "Persona breaking"
            cause: "Instructions conflict with assigned role"
            mitigation: "Align instructions with persona capabilities"
          - failure: "Expertise hallucination"
            cause: "Role implies knowledge model doesn't have"
            mitigation: "Scope expertise claims appropriately"
          - failure: "Style inconsistency"
            cause: "Insufficient persona specification"
            mitigation: "Add detailed communication style guidance"
        
        related_concepts:
          - "[[System Prompts]]"
          - "[[Character Design]]"
          - "[[Expert Systems]]"

  # ═══════════════════════════════════════════════════════════════════════════
  # 3.2 REASONING TECHNIQUES
  # ═══════════════════════════════════════════════════════════════════════════
  
  reasoning_techniques:
    description: >-
      Prompting patterns designed to improve complex reasoning, multi-step
      problem solving, and logical inference capabilities.
    
    techniques:
      
      # ─────────────────────────────────────────────────────────────────────────
      # CHAIN-OF-THOUGHT (CoT)
      # ─────────────────────────────────────────────────────────────────────────
      
      - id: "RT-001"
        name: "Chain-of-Thought Prompting"
        aliases:
          - "CoT"
          - "Step-by-Step Reasoning"
          - "Reasoning Traces"
        
        definition: >-
          Eliciting intermediate reasoning steps before the final answer,
          making the model's reasoning process explicit and improving
          accuracy on complex tasks requiring multi-step inference.
        
        theoretical_basis:
          mechanism: >-
            By generating intermediate steps, the model allocates compute
            to reasoning rather than attempting direct answer prediction.
            This decomposes complex problems into manageable substeps.
          cognitive_analog: >-
            Mirrors human "thinking aloud" - externalizing reasoning
            improves problem-solving by making implicit steps explicit.
          key_research:
            - paper: "Chain-of-Thought Prompting Elicits Reasoning"
              authors: "Wei et al."
              year: 2022
              finding: "CoT dramatically improves math and reasoning accuracy"
            - paper: "Large Language Models are Zero-Shot Reasoners"
              authors: "Kojima et al."
              year: 2022
              finding: "'Let's think step by step' enables zero-shot CoT"
        
        when_to_use:
          optimal_conditions:
            - "Multi-step mathematical problems"
            - "Logical reasoning and deduction"
            - "Complex analysis requiring structured thinking"
            - "Tasks where reasoning transparency matters"
          suboptimal_conditions:
            - "Simple factual retrieval"
            - "Tasks where speed critical"
            - "Very simple, single-step problems"
        
        variants:
          
          zero_shot_cot:
            description: "Trigger CoT without examples"
            trigger_phrases:
              - "Let's think step by step."
              - "Let's work through this systematically."
              - "Let's break this down:"
              - "Think carefully about each step."
              - "Take a deep breath and work through this step by step."
            template: |
              [Problem statement]
              
              Let's think step by step:
            effectiveness: "Significant improvement over direct answering"
          
          few_shot_cot:
            description: "Demonstrate CoT reasoning in examples"
            template: |
              [Problem 1]
              
              Reasoning:
              Step 1: [first reasoning step]
              Step 2: [second reasoning step]
              Step 3: [third reasoning step]
              Therefore, the answer is [answer].
              
              [Problem 2]
              
              Reasoning:
              Step 1: [first reasoning step]
              Step 2: [second reasoning step]
              Therefore, the answer is [answer].
              
              [Target problem]
              
              Reasoning:
            effectiveness: "Highest accuracy for complex reasoning"
          
          structured_cot:
            description: "Enforce specific reasoning structure"
            template: |
              [Problem statement]
              
              Analyze this systematically:
              
              1. UNDERSTAND: What is the problem asking?
              2. IDENTIFY: What information is given?
              3. PLAN: What approach will solve this?
              4. EXECUTE: Work through the solution
              5. VERIFY: Check the answer makes sense
              
              Begin analysis:
            effectiveness: "Improved consistency and coverage"
        
        implementation_patterns:
          
          mathematical_reasoning:
            template: |
              Problem: [math problem]
              
              Solution:
              
              Given information:
              - [fact 1]
              - [fact 2]
              
              Step 1: [calculation/reasoning]
              Result: [intermediate result]
              
              Step 2: [calculation/reasoning]
              Result: [intermediate result]
              
              Final answer: [answer]
              
              Verification: [check calculation]
          
          logical_analysis:
            template: |
              Scenario: [scenario description]
              
              Question: [question]
              
              Analysis:
              
              1. Premises:
                 - [premise 1]
                 - [premise 2]
              
              2. Logical implications:
                 - If [premise], then [implication]
                 - This means [consequence]
              
              3. Conclusion:
                 Based on the above reasoning, [conclusion]
              
              4. Confidence: [high/medium/low] because [justification]
          
          decision_analysis:
            template: |
              Decision: [decision to analyze]
              
              Structured analysis:
              
              1. Options available:
                 - Option A: [description]
                 - Option B: [description]
                 - Option C: [description]
              
              2. Criteria for evaluation:
                 - [criterion 1]: weight [importance]
                 - [criterion 2]: weight [importance]
              
              3. Analysis of each option:
                 Option A:
                   - [criterion 1]: [evaluation]
                   - [criterion 2]: [evaluation]
                 [continue for each option]
              
              4. Recommendation: [recommendation with reasoning]
        
        optimization_strategies:
          reasoning_depth:
            guidance:
              - "More steps for more complex problems"
              - "Avoid skipping intermediate calculations"
              - "Include verification steps for critical accuracy"
          reasoning_structure:
            guidance:
              - "Use consistent step numbering"
              - "Separate reasoning from conclusions"
              - "Include explicit intermediate results"
          error_reduction:
            guidance:
              - "Add self-verification instructions"
              - "Request alternative approaches"
              - "Include sanity check prompts"
        
        common_failure_modes:
          - failure: "Reasoning shortcut"
            cause: "Model skips to answer without full reasoning"
            mitigation: "Explicit instruction to show all steps"
          - failure: "Reasoning error propagation"
            cause: "Early step error cascades through chain"
            mitigation: "Add intermediate verification prompts"
          - failure: "Verbose irrelevant reasoning"
            cause: "Model generates unnecessary tangential thoughts"
            mitigation: "Structure reasoning with specific steps"
        
        related_concepts:
          - "[[Tree of Thoughts]]"
          - "[[Self-Consistency]]"
          - "[[Program-Aided Language Models]]"
      
      # ─────────────────────────────────────────────────────────────────────────
      # TREE OF THOUGHTS (ToT)
      # ─────────────────────────────────────────────────────────────────────────
      
      - id: "RT-002"
        name: "Tree of Thoughts"
        aliases:
          - "ToT"
          - "Branching Reasoning"
          - "Deliberate Exploration"
        
        definition: >-
          A reasoning framework that explores multiple reasoning paths
          simultaneously, evaluates intermediate states, and backtracks
          when necessary, enabling more deliberate problem-solving.
        
        theoretical_basis:
          mechanism: >-
            Extends chain-of-thought by maintaining multiple reasoning
            trajectories, evaluating their promise, and pursuing the most
            promising paths while pruning unpromising ones.
          cognitive_analog: >-
            Models deliberate human problem-solving where we consider
            alternatives, evaluate approaches, and backtrack from dead ends.
          key_research:
            - paper: "Tree of Thoughts: Deliberate Problem Solving"
              authors: "Yao et al."
              year: 2023
              finding: "ToT significantly outperforms CoT on planning tasks"
        
        when_to_use:
          optimal_conditions:
            - "Problems with multiple valid solution paths"
            - "Tasks requiring exploration and backtracking"
            - "Creative problem-solving with evaluation criteria"
            - "Complex planning with uncertain outcomes"
          suboptimal_conditions:
            - "Simple, single-solution problems"
            - "When computational cost is constrained"
            - "Real-time response requirements"
        
        implementation_patterns:
          
          exploration_and_evaluation:
            template: |
              Problem: [problem description]
              
              Step 1: Generate multiple approaches
              
              Approach A: [brief description]
              Approach B: [brief description]
              Approach C: [brief description]
              
              Step 2: Evaluate each approach
              
              Approach A evaluation:
              - Feasibility: [assessment]
              - Likelihood of success: [assessment]
              - Potential issues: [assessment]
              Score: [1-10]
              
              [Repeat for B and C]
              
              Step 3: Pursue most promising approach
              
              Selected: Approach [X] because [reasoning]
              
              Detailed execution:
              [Step-by-step solution using selected approach]
              
              Step 4: Verify and potentially backtrack
              
              Result assessment: [evaluation]
              If unsuccessful, try: [alternative approach]
          
          breadth_first_exploration:
            template: |
              Problem: [problem description]
              
              Level 1 - Initial options:
              1.1: [option]
              1.2: [option]
              1.3: [option]
              
              Evaluation: [1.1: score] [1.2: score] [1.3: score]
              Continue with: [top 2 options]
              
              Level 2 - Develop selected paths:
              From 1.X:
                2.1: [next step option]
                2.2: [next step option]
              From 1.Y:
                2.3: [next step option]
                2.4: [next step option]
              
              Evaluation: [scores for each]
              Continue with: [top options]
              
              [Continue until solution found]
          
          self_evaluation_tot:
            template: |
              Problem: [problem]
              
              I'll explore this systematically:
              
              <thought_branch id="1">
              Initial approach: [description]
              
              First step: [step]
              Self-evaluation: Is this promising? [yes/no + reasoning]
              
              If promising, next step: [step]
              Self-evaluation: [assessment]
              
              [Continue or abandon based on evaluation]
              </thought_branch>
              
              <thought_branch id="2">
              Alternative approach: [description]
              [Same pattern]
              </thought_branch>
              
              <synthesis>
              Most promising path: [branch X]
              Final solution: [detailed solution]
              Confidence: [level + justification]
              </synthesis>
        
        optimization_strategies:
          branching_factor:
            guidance:
              - "2-4 branches per decision point typically optimal"
              - "More branches for high-uncertainty problems"
              - "Fewer branches for well-understood domains"
          evaluation_criteria:
            guidance:
              - "Define explicit evaluation metrics upfront"
              - "Use consistent scoring across branches"
              - "Consider both feasibility and optimality"
          pruning_strategy:
            guidance:
              - "Aggressive pruning for computational efficiency"
              - "Keep at least 2 paths until resolution"
              - "Allow backtracking when top paths fail"
        
        related_concepts:
          - "[[Chain-of-Thought Prompting]]"
          - "[[Self-Consistency]]"
          - "[[Monte Carlo Tree Search]]"
          - "[[Deliberate Practice]]"
      
      # ─────────────────────────────────────────────────────────────────────────
      # SELF-CONSISTENCY
      # ─────────────────────────────────────────────────────────────────────────
      
      - id: "RT-003"
        name: "Self-Consistency"
        aliases:
          - "Ensemble Reasoning"
          - "Majority Voting"
          - "Multi-Path Sampling"
        
        definition: >-
          Sampling multiple reasoning paths for the same problem and
          selecting the most consistent answer across samples, improving
          reliability through ensemble effects.
        
        theoretical_basis:
          mechanism: >-
            Different sampling temperatures or random seeds produce
            varied reasoning paths. Agreement across paths indicates
            robust conclusions while disagreement reveals uncertainty.
          cognitive_analog: >-
            Similar to seeking multiple opinions or working a problem
            multiple times independently to verify conclusions.
          key_research:
            - paper: "Self-Consistency Improves Chain of Thought Reasoning"
              authors: "Wang et al."
              year: 2023
              finding: "Majority voting over CoT paths improves accuracy 5-20%"
        
        when_to_use:
          optimal_conditions:
            - "Tasks where correctness critical"
            - "Problems with single correct answer"
            - "When API cost not primary constraint"
            - "Evaluation/testing scenarios"
          suboptimal_conditions:
            - "Real-time applications"
            - "Tasks with multiple valid answers"
            - "Cost-constrained deployments"
        
        implementation_patterns:
          
          basic_self_consistency:
            process:
              - step: "Generate multiple responses"
                details: "Sample 3-10 CoT responses with temperature > 0"
              - step: "Extract final answers"
                details: "Parse the conclusion from each reasoning path"
              - step: "Apply voting"
                details: "Select most frequent answer"
              - step: "Assess confidence"
                details: "Agreement rate indicates confidence"
            
            prompt_template: |
              [Problem statement]
              
              Let's think step by step:
              
              [Run this prompt multiple times with temperature 0.7-1.0]
              [Extract final answers and apply majority vote]
          
          weighted_self_consistency:
            process:
              - step: "Generate responses with confidence"
                details: "Request confidence score with each answer"
              - step: "Weight votes by confidence"
                details: "Higher confidence answers count more"
              - step: "Select weighted majority"
                details: "Choose answer with highest weighted support"
        
        optimization_strategies:
          sample_count:
            guidance:
              - "3 samples minimum for basic voting"
              - "5-7 samples for production reliability"
              - "10+ samples for high-stakes decisions"
          temperature_setting:
            guidance:
              - "Temperature 0.7-1.0 for diverse samples"
              - "Lower temperature if answers too varied"
              - "Higher temperature if answers too similar"
          agreement_thresholds:
            guidance:
              - ">80% agreement: high confidence"
              - "50-80% agreement: moderate confidence"
              - "<50% agreement: flag for review"
        
        related_concepts:
          - "[[Chain-of-Thought Prompting]]"
          - "[[Ensemble Methods]]"
          - "[[Uncertainty Quantification]]"

  # ═══════════════════════════════════════════════════════════════════════════
  # 3.3 ADVANCED TECHNIQUES
  # ═══════════════════════════════════════════════════════════════════════════
  
  advanced_techniques:
    description: >-
      Sophisticated prompting patterns for complex applications, production
      systems, and cutting-edge use cases.
    
    techniques:
      
      # ─────────────────────────────────────────────────────────────────────────
      # META-PROMPTING
      # ─────────────────────────────────────────────────────────────────────────
      
      - id: "AT-001"
        name: "Meta-Prompting"
        aliases:
          - "Prompt Generation"
          - "Self-Prompting"
          - "Prompt Optimization"
        
        definition: >-
          Using an LLM to generate, refine, or optimize prompts for itself
          or other models, leveraging meta-cognitive capabilities for
          prompt engineering automation.
        
        when_to_use:
          optimal_conditions:
            - "Scaling prompt development across many tasks"
            - "Optimizing prompts for specific objectives"
            - "Exploring prompt space systematically"
            - "When human prompt engineering time constrained"
        
        implementation_patterns:
          
          prompt_generation:
            template: |
              I need a prompt that will make an LLM perform this task effectively:
              
              Task: [task description]
              Input type: [input format]
              Desired output: [output specification]
              Quality criteria: [success metrics]
              
              Generate an optimized prompt that:
              1. Clearly defines the task
              2. Specifies output format precisely
              3. Includes appropriate examples if helpful
              4. Anticipates edge cases
              
              Generated prompt:
          
          prompt_refinement:
            template: |
              Current prompt:
              ```
              [existing prompt]
              ```
              
              This prompt is producing these issues:
              - [Issue 1]
              - [Issue 2]
              
              Improve the prompt to address these issues while maintaining
              its core functionality. Explain your changes.
              
              Improved prompt:
          
          automatic_prompt_engineer:
            process:
              - step: "Generate prompt candidates"
                details: "Create multiple prompt variations"
              - step: "Evaluate on test set"
                details: "Score each prompt on held-out examples"
              - step: "Select top performers"
                details: "Keep highest-scoring prompts"
              - step: "Iterate and refine"
                details: "Use winners to generate new variations"
        
        related_concepts:
          - "[[Automatic Prompt Engineer]]"
          - "[[Prompt Optimization]]"
          - "[[Self-Improvement]]"
      
      # ─────────────────────────────────────────────────────────────────────────
      # PROMPT CHAINING
      # ─────────────────────────────────────────────────────────────────────────
      
      - id: "AT-002"
        name: "Prompt Chaining"
        aliases:
          - "Sequential Prompting"
          - "Pipeline Prompting"
          - "Multi-Stage Prompting"
        
        definition: >-
          Decomposing complex tasks into a sequence of simpler prompts,
          where each prompt's output becomes input or context for the
          next prompt in the chain.
        
        theoretical_basis:
          mechanism: >-
            Each prompt focuses on a single, well-defined subtask. This
            reduces complexity per prompt, enables validation between
            stages, and allows targeted optimization of each step.
        
        when_to_use:
          optimal_conditions:
            - "Complex tasks exceeding single-prompt capability"
            - "Tasks with natural stage decomposition"
            - "When intermediate validation needed"
            - "Error-sensitive applications requiring checkpoints"
          suboptimal_conditions:
            - "Simple, atomic tasks"
            - "Latency-critical applications"
            - "Tasks without clear stage boundaries"
        
        chain_architectures:
          
          linear_chain:
            description: "Sequential stages where each builds on previous"
            pattern: "A → B → C → D → Output"
            use_cases:
              - "Document processing pipelines"
              - "Multi-step analysis workflows"
              - "Sequential transformation tasks"
            example:
              stage_1:
                name: "Extract"
                prompt: "Extract key information from: [document]"
                output: "Extracted facts and entities"
              stage_2:
                name: "Analyze"
                prompt: "Analyze these facts: [stage_1_output]"
                output: "Analysis and insights"
              stage_3:
                name: "Synthesize"
                prompt: "Create summary from: [stage_2_output]"
                output: "Final synthesis"
          
          branching_chain:
            description: "Parallel processing with merge"
            pattern: |
              A → B₁ ⟍
                       → D → Output
              A → B₂ ⟋
            use_cases:
              - "Multi-perspective analysis"
              - "Parallel feature extraction"
              - "Ensemble reasoning"
          
          conditional_chain:
            description: "Routing based on intermediate results"
            pattern: "A → [if X: B₁ → C₁; else: B₂ → C₂] → Output"
            use_cases:
              - "Adaptive processing pipelines"
              - "Error handling workflows"
              - "Classification-based routing"
          
          iterative_chain:
            description: "Repeated refinement until criteria met"
            pattern: "A → B → [if not satisfied: → B] → Output"
            use_cases:
              - "Quality refinement loops"
              - "Iterative improvement"
              - "Convergence-based processing"
        
        implementation_patterns:
          
          extraction_analysis_synthesis:
            stages:
              - id: "extract"
                prompt: |
                  Document: [input_document]
                  
                  Extract the following information:
                  - Key facts and claims
                  - Named entities (people, organizations, dates)
                  - Main arguments or themes
                  
                  Format as structured JSON.
                output_format: "JSON with extracted elements"
              
              - id: "analyze"
                prompt: |
                  Extracted information:
                  [extract_output]
                  
                  Analyze this information:
                  1. Identify relationships between entities
                  2. Evaluate strength of arguments
                  3. Note any inconsistencies or gaps
                  4. Assess credibility of claims
                  
                  Provide structured analysis.
                output_format: "Structured analysis report"
              
              - id: "synthesize"
                prompt: |
                  Original document context: [brief_context]
                  Analysis results: [analyze_output]
                  
                  Synthesize a [output_type] that:
                  - Highlights key insights
                  - Presents balanced conclusions
                  - Notes limitations and uncertainties
                output_format: "Final deliverable"
          
          with_validation_gates:
            stages:
              - id: "process"
                prompt: "[processing instruction]"
              - id: "validate"
                prompt: |
                  Review this output for:
                  - Factual accuracy
                  - Format compliance
                  - Completeness
                  
                  Output: [previous_stage_output]
                  
                  Validation result (PASS/FAIL):
                  Issues found:
                  Corrections needed:
              - id: "correct_or_proceed"
                logic: "If FAIL: return to process with corrections; If PASS: continue"
        
        optimization_strategies:
          stage_design:
            guidance:
              - "Each stage should have single clear objective"
              - "Define explicit input/output contracts"
              - "Include validation criteria per stage"
          context_management:
            guidance:
              - "Pass only necessary context between stages"
              - "Summarize long outputs before passing"
              - "Maintain critical information throughout chain"
          error_handling:
            guidance:
              - "Implement validation gates between stages"
              - "Design fallback paths for failures"
              - "Log intermediate outputs for debugging"
        
        related_concepts:
          - "[[Agentic Workflows]]"
          - "[[Task Decomposition]]"
          - "[[Pipeline Architecture]]"
      
      # ─────────────────────────────────────────────────────────────────────────
      # RETRIEVAL AUGMENTED GENERATION (RAG)
      # ─────────────────────────────────────────────────────────────────────────
      
      - id: "AT-003"
        name: "Retrieval Augmented Generation"
        aliases:
          - "RAG"
          - "Grounded Generation"
          - "Knowledge-Augmented Prompting"
        
        definition: >-
          Augmenting prompts with relevant information retrieved from
          external knowledge sources, combining parametric knowledge
          (model weights) with non-parametric knowledge (retrieved documents).
        
        theoretical_basis:
          mechanism: >-
            Retrieved passages provide factual grounding and domain-specific
            context that may not exist in model weights or may be outdated.
            The model synthesizes retrieved information with its capabilities.
          key_research:
            - paper: "Retrieval-Augmented Generation for Knowledge-Intensive NLP"
              authors: "Lewis et al."
              year: 2020
              finding: "RAG significantly improves factual accuracy"
        
        when_to_use:
          optimal_conditions:
            - "Questions requiring current/specific facts"
            - "Domain-specific knowledge needs"
            - "Reducing hallucination critical"
            - "Working with proprietary knowledge bases"
          suboptimal_conditions:
            - "General reasoning without factual grounding"
            - "Creative tasks not requiring accuracy"
            - "When retrieval latency unacceptable"
        
        rag_architecture_patterns:
          
          basic_rag:
            components:
              query_processing: "Convert user query to retrieval query"
              retrieval: "Search knowledge base for relevant documents"
              context_assembly: "Format retrieved docs with user query"
              generation: "Generate response using augmented context"
            prompt_template: |
              Use the following context to answer the question.
              If the answer is not in the context, say so.
              
              Context:
              [retrieved_document_1]
              ---
              [retrieved_document_2]
              ---
              [retrieved_document_3]
              
              Question: [user_question]
              
              Answer:
          
          advanced_rag:
            enhancements:
              query_expansion:
                description: "Generate multiple query variations"
                benefit: "Improved recall for complex queries"
              reranking:
                description: "Score and reorder retrieved documents"
                benefit: "Higher precision in context"
              citation_tracking:
                description: "Track which sources support which claims"
                benefit: "Verifiability and attribution"
              self_reflection:
                description: "Evaluate if retrieved context sufficient"
                benefit: "Know when to retrieve more or acknowledge gaps"
            prompt_template: |
              <context>
              <document id="1" source="[source_1]">
              [content_1]
              </document>
              <document id="2" source="[source_2]">
              [content_2]
              </document>
              </context>
              
              <instructions>
              Answer the question using ONLY the provided context.
              - Cite sources using [doc_id] notation
              - If information not in context, explicitly state this
              - Distinguish between stated facts and inferences
              </instructions>
              
              <question>[user_question]</question>
              
              <answer>
          
          agentic_rag:
            description: "RAG with iterative retrieval and reasoning"
            components:
              initial_retrieval: "First-pass document fetch"
              gap_analysis: "Identify what information is missing"
              targeted_retrieval: "Fetch additional docs for gaps"
              synthesis: "Combine all retrieved information"
            process:
              - "Retrieve initial documents"
              - "Assess: Is this sufficient to answer?"
              - "If no: Identify gaps and retrieve more"
              - "Repeat until sufficient or retrieval exhausted"
              - "Generate final response with citations"
        
        optimization_strategies:
          retrieval_quality:
            guidance:
              - "Use semantic search for concept matching"
              - "Implement hybrid search (semantic + keyword)"
              - "Tune chunk size for optimal context density"
          context_formatting:
            guidance:
              - "Structure retrieved docs with clear boundaries"
              - "Include source metadata for citation"
              - "Prioritize most relevant content at context edges"
          prompt_design:
            guidance:
              - "Explicit instruction to use only provided context"
              - "Encourage citation and source attribution"
              - "Include fallback behavior for missing information"
        
        related_concepts:
          - "[[Vector Databases]]"
          - "[[Semantic Search]]"
          - "[[Knowledge Graphs]]"
          - "[[Context Engineering]]"
      
      # ─────────────────────────────────────────────────────────────────────────
      # ReAct (REASONING + ACTING)
      # ─────────────────────────────────────────────────────────────────────────
      
      - id: "AT-004"
        name: "ReAct"
        aliases:
          - "Reason + Act"
          - "Reasoning and Acting"
          - "Interleaved Reasoning"
        
        definition: >-
          A prompting paradigm that interleaves reasoning traces with
          action execution, allowing models to plan, act, observe results,
          and adjust reasoning based on observations.
        
        theoretical_basis:
          mechanism: >-
            Combines chain-of-thought reasoning with action-taking in an
            interleaved loop. Observations from actions inform subsequent
            reasoning, creating a dynamic problem-solving cycle.
          key_research:
            - paper: "ReAct: Synergizing Reasoning and Acting in Language Models"
              authors: "Yao et al."
              year: 2023
              finding: "ReAct outperforms CoT and Act-only on knowledge tasks"
        
        when_to_use:
          optimal_conditions:
            - "Tasks requiring external tool use"
            - "Problems needing information gathering"
            - "Dynamic environments with feedback"
            - "Multi-step tasks with uncertain requirements"
        
        react_loop_structure:
          components:
            thought: "Reasoning about current state and next steps"
            action: "Executing a tool or taking an action"
            observation: "Processing results of the action"
          loop: "Thought → Action → Observation → Thought → ..."
        
        implementation_patterns:
          
          standard_react:
            template: |
              You have access to the following tools:
              - search[query]: Search for information
              - lookup[term]: Look up a specific term
              - calculate[expression]: Perform calculation
              - finish[answer]: Submit final answer
              
              Question: [user_question]
              
              Thought 1: I need to find information about [topic].
              Action 1: search[topic query]
              Observation 1: [search results]
              
              Thought 2: Based on this, I should look up [specific term].
              Action 2: lookup[term]
              Observation 2: [lookup results]
              
              Thought 3: Now I can calculate [expression].
              Action 3: calculate[expression]
              Observation 3: [calculation result]
              
              Thought 4: I have enough information to answer.
              Action 4: finish[final answer]
          
          with_reflection:
            template: |
              [Standard ReAct loop]
              
              After each observation, also assess:
              - Did this action provide useful information?
              - Am I making progress toward the goal?
              - Should I try a different approach?
              
              [Continue with adjusted strategy if needed]
        
        optimization_strategies:
          tool_design:
            guidance:
              - "Clear tool descriptions with usage examples"
              - "Consistent input/output formats"
              - "Informative error messages"
          thought_quality:
            guidance:
              - "Encourage explicit reasoning before actions"
              - "Include goal-tracking in thoughts"
              - "Prompt for strategy adjustment when stuck"
          loop_termination:
            guidance:
              - "Define clear completion criteria"
              - "Implement maximum iteration limits"
              - "Include fallback behavior"
        
        related_concepts:
          - "[[Agentic Systems]]"
          - "[[Tool Use]]"
          - "[[Planning]]"
      
      # ─────────────────────────────────────────────────────────────────────────
      # REFLEXION
      # ─────────────────────────────────────────────────────────────────────────
      
      - id: "AT-005"
        name: "Reflexion"
        aliases:
          - "Self-Reflection"
          - "Iterative Refinement"
          - "Learning from Mistakes"
        
        definition: >-
          A technique where the model reflects on its outputs, identifies
          errors or improvements, and refines its response through
          iterative self-critique and correction.
        
        theoretical_basis:
          mechanism: >-
            Leverages the model's ability to evaluate its own outputs
            against criteria, identify shortcomings, and generate improved
            versions. Creates a feedback loop without external signals.
          key_research:
            - paper: "Reflexion: Language Agents with Verbal Reinforcement Learning"
              authors: "Shinn et al."
              year: 2023
              finding: "Verbal self-reflection improves task success rates"
        
        when_to_use:
          optimal_conditions:
            - "Tasks with clear evaluation criteria"
            - "Quality-critical applications"
            - "When first-pass accuracy insufficient"
            - "Complex outputs requiring refinement"
        
        implementation_patterns:
          
          generate_critique_refine:
            stages:
              generate:
                prompt: |
                  [Task instruction]
                  
                  Generate your best response:
              critique:
                prompt: |
                  Review this response against the criteria:
                  
                  Response: [generated_response]
                  
                  Criteria:
                  - [criterion 1]
                  - [criterion 2]
                  - [criterion 3]
                  
                  Critique:
                  - What's done well:
                  - What could be improved:
                  - Specific suggestions:
              refine:
                prompt: |
                  Original response: [generated_response]
                  
                  Critique and suggestions:
                  [critique_output]
                  
                  Generate an improved response that addresses the critique:
          
          iterative_reflexion:
            process:
              - "Generate initial response"
              - "Evaluate against criteria"
              - "If criteria met: finish"
              - "If not: generate reflection on gaps"
              - "Use reflection to guide improved attempt"
              - "Repeat until criteria met or max iterations"
            max_iterations: "3-5 typically sufficient"
          
          self_consistency_reflexion:
            process:
              - "Generate multiple candidate responses"
              - "Compare candidates against each other"
              - "Identify best elements from each"
              - "Synthesize optimal response from best elements"
        
        optimization_strategies:
          critique_quality:
            guidance:
              - "Provide explicit evaluation criteria"
              - "Request specific, actionable feedback"
              - "Include both positive and negative observations"
          refinement_guidance:
            guidance:
              - "Direct attention to specific improvement areas"
              - "Preserve successful elements"
              - "Avoid over-correction"
          termination_criteria:
            guidance:
              - "Define explicit quality thresholds"
              - "Set maximum iteration limits"
              - "Track improvement delta between iterations"
        
        related_concepts:
          - "[[Self-Consistency]]"
          - "[[Constitutional AI]]"
          - "[[Iterative Refinement]]"

---
# ┌─────────────────────────────────────────────────────────────────────────────┐
# │              SECTION 4: STRUCTURAL COMPONENTS                                │
# └─────────────────────────────────────────────────────────────────────────────┘

structural_components:
  
  # ═══════════════════════════════════════════════════════════════════════════
  # 4.1 SYSTEM PROMPTS
  # ═══════════════════════════════════════════════════════════════════════════
  
  system_prompts:
    description: >-
      Persistent instructions that define model behavior, capabilities,
      and constraints across an interaction session.
    
    purpose:
      - "Establish consistent behavioral baseline"
      - "Define role and expertise domain"
      - "Set output constraints and formatting"
      - "Implement safety guardrails"
    
    design_components:
      
      identity_block:
        purpose: "Define who/what the assistant is"
        elements:
          - "Name or identifier (optional)"
          - "Role or expertise description"
          - "Capabilities summary"
          - "Limitations acknowledgment"
        template: |
          You are [name/role], a [expertise description].
          
          Your capabilities include:
          - [capability 1]
          - [capability 2]
          
          You are particularly skilled at:
          - [strength 1]
          - [strength 2]
          
          Note: You cannot [limitation 1] or [limitation 2].
      
      behavioral_block:
        purpose: "Define how the assistant should behave"
        elements:
          - "Communication style"
          - "Response structure preferences"
          - "Interaction patterns"
          - "Personality traits"
        template: |
          Behavioral guidelines:
          
          Communication style:
          - [style directive 1]
          - [style directive 2]
          
          Response approach:
          - [approach directive 1]
          - [approach directive 2]
          
          Interaction principles:
          - [principle 1]
          - [principle 2]
      
      constraint_block:
        purpose: "Define boundaries and limitations"
        elements:
          - "Topics to avoid"
          - "Output restrictions"
          - "Safety constraints"
          - "Compliance requirements"
        template: |
          Constraints:
          
          You must:
          - [requirement 1]
          - [requirement 2]
          
          You must not:
          - [prohibition 1]
          - [prohibition 2]
          
          When uncertain:
          - [uncertainty handling directive]
      
      context_block:
        purpose: "Provide persistent knowledge or context"
        elements:
          - "Domain knowledge"
          - "User information"
          - "Session context"
          - "Reference data"
        template: |
          Context information:
          
          Domain: [domain description]
          User profile: [relevant user info]
          Current context: [session context]
          
          Reference data:
          [key reference information]
      
      instruction_block:
        purpose: "Define task-specific instructions"
        elements:
          - "Primary task definition"
          - "Output format specification"
          - "Quality criteria"
          - "Edge case handling"
        template: |
          Task instructions:
          
          Primary objective: [main task]
          
          Output format:
          [format specification]
          
          Quality criteria:
          - [criterion 1]
          - [criterion 2]
          
          Edge cases:
          - If [condition 1]: [handling]
          - If [condition 2]: [handling]
    
    system_prompt_patterns:
      
      minimal_effective:
        description: "Bare minimum for effective interaction"
        template: |
          You are a helpful assistant specializing in [domain].
          Provide clear, accurate responses.
          If uncertain, acknowledge it.
        use_case: "Simple, general-purpose applications"
      
      comprehensive_production:
        description: "Full-featured production system prompt"
        template: |
          <system_identity>
          You are [Name], an AI assistant created by [Organization].
          Your purpose is to [primary purpose].
          </system_identity>
          
          <capabilities>
          - [Capability 1 with scope]
          - [Capability 2 with scope]
          - [Capability 3 with scope]
          </capabilities>
          
          <behavioral_guidelines>
          Communication:
          - [Guideline 1]
          - [Guideline 2]
          
          Response format:
          - [Format guideline 1]
          - [Format guideline 2]
          </behavioral_guidelines>
          
          <constraints>
          Safety:
          - [Safety constraint 1]
          - [Safety constraint 2]
          
          Compliance:
          - [Compliance requirement 1]
          - [Compliance requirement 2]
          </constraints>
          
          <context>
          [Persistent context information]
          </context>
          
          <instructions>
          [Task-specific instructions]
          </instructions>
        use_case: "Production deployments requiring consistency"
      
      agentic_system:
        description: "System prompt for tool-using agents"
        template: |
          <agent_identity>
          You are an AI agent capable of using tools to accomplish tasks.
          </agent_identity>
          
          <available_tools>
          [Tool definitions with parameters and usage]
          </available_tools>
          
          <tool_usage_guidelines>
          - Plan before acting
          - Use tools only when necessary
          - Verify results before proceeding
          - Handle errors gracefully
          </tool_usage_guidelines>
          
          <reasoning_approach>
          For each task:
          1. Understand the objective
          2. Plan the approach
          3. Execute using tools as needed
          4. Verify results
          5. Report outcome
          </reasoning_approach>
          
          <constraints>
          [Safety and operational constraints]
          </constraints>
        use_case: "Agentic applications with tool use"
    
    optimization_strategies:
      structure:
        - "Use XML tags for clear section separation"
        - "Order sections by importance/frequency of reference"
        - "Keep related instructions grouped together"
      clarity:
        - "Use specific, unambiguous language"
        - "Provide examples for complex requirements"
        - "Define terms that might be ambiguous"
      maintenance:
        - "Version control system prompts"
        - "Document changes and rationale"
        - "Test changes before deployment"

  # ═══════════════════════════════════════════════════════════════════════════
  # 4.2 OUTPUT FORMATTING
  # ═══════════════════════════════════════════════════════════════════════════
  
  output_formatting:
    description: >-
      Techniques for controlling and constraining model output format,
      structure, and presentation.
    
    format_types:
      
      json_output:
        description: "Structured JSON responses"
        use_cases:
          - "API integrations"
          - "Data extraction"
          - "Structured information capture"
        implementation:
          basic:
            prompt: |
              Extract the following information as JSON:
              
              Required fields:
              - name: string
              - age: number
              - occupation: string
              
              Input: [text]
              
              JSON output:
          with_schema:
            prompt: |
              Output your response as valid JSON matching this schema:
              
              {
                "summary": "string - brief summary of content",
                "key_points": ["string - array of main points"],
                "sentiment": "positive | negative | neutral",
                "confidence": "number between 0 and 1"
              }
              
              Input: [text]
          with_prefilling:
            prompt: |
              [Instructions]
              
              Input: [text]
              
              Assistant: {
                "
            notes: "Prefilling forces JSON format start"
      
      markdown_output:
        description: "Formatted markdown responses"
        use_cases:
          - "Documentation generation"
          - "Report creation"
          - "Readable structured content"
        implementation:
          with_structure:
            prompt: |
              Create a report using this markdown structure:
              
              # [Title]
              
              ## Summary
              [Brief overview]
              
              ## Key Findings
              - [Finding 1]
              - [Finding 2]
              
              ## Details
              [Detailed analysis]
              
              ## Recommendations
              1. [Recommendation 1]
              2. [Recommendation 2]
      
      xml_output:
        description: "Structured XML responses"
        use_cases:
          - "Machine-parseable structured output"
          - "Complex nested data"
          - "Integration with XML-based systems"
        implementation:
          basic:
            prompt: |
              Output your analysis as XML with this structure:
              
              <analysis>
                <summary>[summary text]</summary>
                <findings>
                  <finding priority="high|medium|low">[finding]</finding>
                </findings>
                <recommendations>
                  <recommendation>[recommendation]</recommendation>
                </recommendations>
              </analysis>
      
      tabular_output:
        description: "Table-formatted responses"
        use_cases:
          - "Comparisons"
          - "Data summaries"
          - "Structured lists"
        implementation:
          markdown_table:
            prompt: |
              Present the comparison as a markdown table:
              
              | Feature | Option A | Option B | Option C |
              |---------|----------|----------|----------|
              | [Feature 1] | ... | ... | ... |
      
      code_output:
        description: "Programming code responses"
        use_cases:
          - "Code generation"
          - "Script creation"
          - "Technical solutions"
        implementation:
          with_context:
            prompt: |
              Write a [language] function that [description].
              
              Requirements:
              - [Requirement 1]
              - [Requirement 2]
              
              Include:
              - Clear comments
              - Error handling
              - Usage example
              
              ```[language]
              # Your code here
    
    format_control_techniques:
      
      explicit_specification:
        description: "Directly state required format"
        approach: |
          Respond in exactly this format:
          
          [Format specification with placeholders]
      
      example_based:
        description: "Show format through examples"
        approach: |
          Example input: [example]
          Example output: [formatted example output]
          
          Now process: [actual input]
      
      prefilling:
        description: "Begin response in desired format"
        approach: |
          [Instructions]
          
          Assistant: [Start of desired format
        benefit: "Forces model to continue in specified format"
      
      constraint_emphasis:
        description: "Emphasize format requirements"
        approach: |
          IMPORTANT: Your response must be valid JSON.
          Do not include any text outside the JSON structure.
          Do not use markdown code blocks.
          
          Response:

---
# ┌─────────────────────────────────────────────────────────────────────────────┐
# │              SECTION 5: CONTEXT ENGINEERING                                  │
# └─────────────────────────────────────────────────────────────────────────────┘

context_engineering:
  description: >-
    Strategies for managing, optimizing, and structuring context provided
    to LLMs to maximize relevance and minimize noise.
  
  # ═══════════════════════════════════════════════════════════════════════════
  # 5.1 CONTEXT WINDOW MANAGEMENT
  # ═══════════════════════════════════════════════════════════════════════════
  
  context_window_management:
    
    principles:
      relevance_maximization:
        description: "Include only contextually relevant information"
        strategies:
          - "Filter context to task requirements"
          - "Remove redundant information"
          - "Prioritize high-value content"
      
      information_density:
        description: "Maximize information per token"
        strategies:
          - "Compress verbose content"
          - "Use efficient representations"
          - "Eliminate filler content"
      
      structural_clarity:
        description: "Organize context for easy processing"
        strategies:
          - "Use clear section boundaries"
          - "Apply consistent formatting"
          - "Order by relevance or logical flow"
    
    context_position_effects:
      primacy_effect:
        description: "Information at beginning receives strong attention"
        implication: "Place critical instructions and context early"
      
      recency_effect:
        description: "Information near end also receives strong attention"
        implication: "Place immediate task/query near end"
      
      middle_attention:
        description: "Middle content may receive less attention in very long contexts"
        implication: "Avoid burying critical information in middle"
        mitigation: "Use structural markers to highlight important middle content"
    
    context_optimization_patterns:
      
      summarize_then_detail:
        description: "Provide summary upfront, details as needed"
        template: |
          Summary: [High-level overview]
          
          Detailed context:
          [Expanded information as needed]
          
          Task: [Specific task]
      
      hierarchical_context:
        description: "Nest context by relevance/specificity"
        template: |
          Global context:
          [Broad, persistent context]
          
          Session context:
          [Current session relevant information]
          
          Task context:
          [Immediate task requirements]
      
      progressive_disclosure:
        description: "Reveal context as needed through interaction"
        approach: |
          Initial prompt: Minimal necessary context
          Follow-up: Add context based on model questions
          Refinement: Provide specific details as needed

  # ═══════════════════════════════════════════════════════════════════════════
  # 5.2 CONTEXT TYPES AND MANAGEMENT
  # ═══════════════════════════════════════════════════════════════════════════
  
  context_types:
    
    instructional_context:
      description: "Context defining how to perform the task"
      components:
        - "Task definition"
        - "Methodology specifications"
        - "Quality criteria"
        - "Output requirements"
      best_practices:
        - "Place early in prompt"
        - "Use clear, imperative language"
        - "Include examples when helpful"
    
    informational_context:
      description: "Context providing knowledge needed for task"
      components:
        - "Domain knowledge"
        - "Reference materials"
        - "Facts and data"
        - "External content"
      best_practices:
        - "Mark clearly as reference material"
        - "Structure for easy scanning"
        - "Include source attribution"
    
    conversational_context:
      description: "Context from prior conversation turns"
      components:
        - "User messages"
        - "Assistant responses"
        - "Clarifications"
        - "State updates"
      best_practices:
        - "Summarize long conversation history"
        - "Preserve critical decisions and requirements"
        - "Remove redundant exchanges"
    
    environmental_context:
      description: "Context about current state and environment"
      components:
        - "Date/time information"
        - "User profile/preferences"
        - "System state"
        - "Available capabilities"
      best_practices:
        - "Include only when relevant"
        - "Update for accuracy"
        - "Format consistently"

---
# ┌─────────────────────────────────────────────────────────────────────────────┐
# │              SECTION 6: AGENTIC PATTERNS                                     │
# └─────────────────────────────────────────────────────────────────────────────┘

agentic_patterns:
  description: >-
    Prompt patterns for autonomous agent behavior, tool use,
    and multi-step task execution.
  
  # ═══════════════════════════════════════════════════════════════════════════
  # 6.1 TOOL USE PATTERNS
  # ═══════════════════════════════════════════════════════════════════════════
  
  tool_use:
    
    tool_definition_format:
      standard_structure:
        name: "Tool identifier"
        description: "What the tool does and when to use it"
        parameters:
          - name: "Parameter name"
            type: "Data type"
            description: "What this parameter does"
            required: "boolean"
        returns: "Description of return value"
        examples: "Usage examples"
      
      template: |
        <tool name="[tool_name]">
        <description>[Clear description of purpose and use cases]</description>
        <parameters>
          <param name="[param1]" type="[type]" required="[true/false]">
            [Parameter description]
          </param>
        </parameters>
        <returns>[Return value description]</returns>
        <example>
          Input: [example input]
          Output: [example output]
        </example>
        </tool>
    
    tool_selection_guidance:
      prompting_for_selection:
        template: |
          You have access to these tools:
          [tool definitions]
          
          To use a tool, respond with:
          <tool_call>
          <name>[tool_name]</name>
          <parameters>
          [parameter values]
          </parameters>
          </tool_call>
          
          Guidelines:
          - Use tools only when necessary
          - Verify tool is appropriate before calling
          - Handle tool errors gracefully
      
      decision_framework:
        questions:
          - "Is external information needed?"
          - "Can the task be done without tools?"
          - "Which tool best fits the need?"
          - "What are the expected results?"
    
    tool_result_handling:
      patterns:
        direct_incorporation:
          description: "Directly use tool results in response"
          approach: "Synthesize tool output into answer"
        
        validation_first:
          description: "Validate tool results before use"
          approach: |
            1. Receive tool result
            2. Check for errors or unexpected output
            3. Validate against expectations
            4. Incorporate if valid, retry or report if not
        
        iterative_refinement:
          description: "Use multiple tool calls to refine results"
          approach: |
            1. Initial tool call
            2. Assess result completeness
            3. Additional calls as needed
            4. Synthesize all results

  # ═══════════════════════════════════════════════════════════════════════════
  # 6.2 PLANNING PATTERNS
  # ═══════════════════════════════════════════════════════════════════════════
  
  planning:
    
    plan_then_execute:
      description: "Generate plan before taking actions"
      template: |
        Task: [complex task]
        
        First, create a plan:
        
        1. Analyze the task requirements
        2. Identify necessary steps
        3. Determine dependencies between steps
        4. Estimate resources/tools needed
        5. Outline execution order
        
        Plan:
        [generate plan]
        
        Now execute the plan step by step:
        [execute with reasoning]
    
    hierarchical_planning:
      description: "Create high-level plan with detailed sub-plans"
      template: |
        Task: [complex task]
        
        High-level plan:
        1. [Phase 1]
        2. [Phase 2]
        3. [Phase 3]
        
        Detailed plan for Phase 1:
        1.1 [Substep]
        1.2 [Substep]
        
        [Continue expanding as needed]
    
    adaptive_planning:
      description: "Adjust plan based on execution results"
      template: |
        Initial plan: [plan]
        
        After each step:
        - Assess: Did the step succeed?
        - Evaluate: Are we on track?
        - Adapt: Should the plan change?
        
        Current status: [status]
        Adjusted plan: [updated plan if needed]

  # ═══════════════════════════════════════════════════════════════════════════
  # 6.3 MULTI-AGENT PATTERNS
  # ═══════════════════════════════════════════════════════════════════════════
  
  multi_agent:
    
    specialist_delegation:
      description: "Different prompts/personas for different subtasks"
      pattern:
        coordinator:
          role: "Orchestrate task and delegate"
          prompt: |
            You are a coordinator. Break this task into subtasks
            and delegate to specialists:
            - Researcher: For information gathering
            - Analyst: For data analysis
            - Writer: For content creation
        specialists:
          researcher:
            prompt: "You are a research specialist. Find and verify information."
          analyst:
            prompt: "You are an analysis specialist. Evaluate and synthesize data."
          writer:
            prompt: "You are a writing specialist. Create clear, engaging content."
    
    debate_and_synthesis:
      description: "Multiple perspectives that debate and reach consensus"
      template: |
        Topic: [topic]
        
        Perspective A argues: [viewpoint]
        Perspective B argues: [counter-viewpoint]
        
        Synthesis: Considering both perspectives, [balanced conclusion]
    
    review_chain:
      description: "Sequential review by different personas"
      pattern:
        generator: "Create initial output"
        reviewer_1: "Review for accuracy"
        reviewer_2: "Review for completeness"
        editor: "Final refinement"

---
# ┌─────────────────────────────────────────────────────────────────────────────┐
# │              SECTION 7: SAFETY AND ALIGNMENT                                 │
# └─────────────────────────────────────────────────────────────────────────────┘

safety_and_alignment:
  description: >-
    Patterns and practices for ensuring safe, aligned, and reliable
    LLM behavior through prompt design.
  
  # ═══════════════════════════════════════════════════════════════════════════
  # 7.1 SAFETY PATTERNS
  # ═══════════════════════════════════════════════════════════════════════════
  
  safety_patterns:
    
    output_validation:
      description: "Verify output meets safety criteria"
      implementation:
        pre_generation:
          prompt_addition: |
            Before responding, verify that your response:
            - Does not contain harmful content
            - Does not provide dangerous instructions
            - Does not violate privacy
            - Is factually grounded
        
        post_generation:
          approach: "Use separate validation prompt or classifier"
          template: |
            Review this response for safety issues:
            
            Response: [generated_response]
            
            Check for:
            - Harmful advice
            - Misinformation
            - Privacy violations
            - Bias or discrimination
            
            Safety assessment:
    
    refusal_patterns:
      description: "Graceful handling of problematic requests"
      implementation:
        explicit_refusal:
          template: |
            If asked to [problematic category]:
            - Acknowledge the request
            - Explain why you cannot comply
            - Offer alternative assistance if possible
        
        redirect:
          template: |
            I can't help with [specific request] because [reason].
            
            However, I can help you with [alternative approach].
            Would that be useful?
    
    uncertainty_expression:
      description: "Honest communication of limitations"
      patterns:
        calibrated_confidence:
          template: |
            When uncertain, express confidence levels:
            - High confidence: "Based on [evidence], ..."
            - Medium confidence: "It appears that..., though..."
            - Low confidence: "I'm not certain, but..."
            - Unknown: "I don't have reliable information about..."
        
        source_acknowledgment:
          template: |
            For factual claims:
            - Cite sources when available
            - Distinguish facts from inferences
            - Note when information might be outdated

  # ═══════════════════════════════════════════════════════════════════════════
  # 7.2 ALIGNMENT PATTERNS
  # ═══════════════════════════════════════════════════════════════════════════
  
  alignment_patterns:
    
    value_alignment:
      description: "Ensuring responses align with intended values"
      implementation:
        explicit_values:
          template: |
            Core values to uphold:
            - Helpfulness: Provide genuinely useful assistance
            - Honesty: Be truthful and transparent
            - Harmlessness: Avoid causing harm
            
            When values conflict, prioritize in this order:
            1. Safety and harmlessness
            2. Honesty and accuracy
            3. Helpfulness and utility
    
    constitutional_principles:
      description: "Self-critique against defined principles"
      implementation:
        critique_revision:
          template: |
            Response: [initial_response]
            
            Critique against principles:
            - Is this helpful? [assessment]
            - Is this honest? [assessment]
            - Is this harmless? [assessment]
            
            Revised response if needed:
            [improved_response]
    
    consistency_maintenance:
      description: "Ensuring consistent behavior across contexts"
      strategies:
        - "Use consistent system prompts"
        - "Define explicit decision rules"
        - "Test edge cases systematically"
        - "Monitor for behavior drift"

---
# ┌─────────────────────────────────────────────────────────────────────────────┐
# │              SECTION 8: EVALUATION AND TESTING                               │
# └─────────────────────────────────────────────────────────────────────────────┘

evaluation_and_testing:
  description: >-
    Methodologies for evaluating prompt effectiveness and
    ensuring quality in production deployments.
  
  # ═══════════════════════════════════════════════════════════════════════════
  # 8.1 EVALUATION METRICS
  # ═══════════════════════════════════════════════════════════════════════════
  
  evaluation_metrics:
    
    task_specific_metrics:
      accuracy:
        description: "Correctness of output vs ground truth"
        measurement: "Percentage of correct responses"
        applicable_to: "Classification, QA, factual tasks"
      
      relevance:
        description: "How well output addresses the query"
        measurement: "Human rating or automated scoring"
        applicable_to: "Open-ended generation, search"
      
      completeness:
        description: "Coverage of required information"
        measurement: "Checklist completion rate"
        applicable_to: "Analysis, summarization, extraction"
      
      coherence:
        description: "Logical flow and consistency"
        measurement: "Human rating or automated metrics"
        applicable_to: "Long-form generation"
    
    operational_metrics:
      latency:
        description: "Time to generate response"
        measurement: "Milliseconds or seconds"
        considerations: "Balance with quality requirements"
      
      token_efficiency:
        description: "Output quality per token used"
        measurement: "Quality score / token count"
        considerations: "Cost optimization"
      
      consistency:
        description: "Variance across multiple runs"
        measurement: "Standard deviation of quality scores"
        considerations: "Production reliability"
    
    safety_metrics:
      refusal_rate:
        description: "Appropriate refusals for harmful requests"
        target: "High for harmful, low for benign"
      
      hallucination_rate:
        description: "Frequency of factually incorrect claims"
        measurement: "Fact-checking against sources"
      
      bias_score:
        description: "Presence of unwanted bias"
        measurement: "Fairness metrics across demographics"

  # ═══════════════════════════════════════════════════════════════════════════
  # 8.2 TESTING METHODOLOGIES
  # ═══════════════════════════════════════════════════════════════════════════
  
  testing_methodologies:
    
    unit_testing:
      description: "Testing individual prompt components"
      approach:
        - "Test each prompt in isolation"
        - "Verify expected output format"
        - "Check edge case handling"
        - "Validate constraint adherence"
      test_case_structure:
        input: "Test input"
        expected_behavior: "What should happen"
        actual_output: "What did happen"
        pass_criteria: "Conditions for passing"
    
    integration_testing:
      description: "Testing prompt chains and workflows"
      approach:
        - "Test complete prompt chains"
        - "Verify data flow between stages"
        - "Check error propagation handling"
        - "Validate end-to-end quality"
    
    regression_testing:
      description: "Ensuring changes don't break existing behavior"
      approach:
        - "Maintain test suite of key scenarios"
        - "Run before and after changes"
        - "Compare quality metrics"
        - "Flag regressions for review"
    
    adversarial_testing:
      description: "Testing against edge cases and attacks"
      categories:
        edge_cases:
          - "Empty inputs"
          - "Very long inputs"
          - "Unusual formats"
          - "Multiple languages"
        adversarial_inputs:
          - "Prompt injection attempts"
          - "Jailbreak attempts"
          - "Confusing instructions"
          - "Contradictory requirements"
    
    ab_testing:
      description: "Comparing prompt variants in production"
      approach:
        - "Define clear hypothesis"
        - "Split traffic between variants"
        - "Collect metrics on both"
        - "Statistical significance testing"
        - "Roll out winner"

  # ═══════════════════════════════════════════════════════════════════════════
  # 8.3 EVALUATION FRAMEWORKS
  # ═══════════════════════════════════════════════════════════════════════════
  
  evaluation_frameworks:
    
    llm_as_judge:
      description: "Using LLMs to evaluate LLM outputs"
      implementation:
        single_evaluation:
          template: |
            Evaluate this response on a scale of 1-5:
            
            Response: [response]
            
            Criteria:
            - Accuracy: [1-5]
            - Relevance: [1-5]
            - Clarity: [1-5]
            
            Overall score: [1-5]
            Justification: [reasoning]
        
        pairwise_comparison:
          template: |
            Compare these two responses:
            
            Response A: [response_a]
            Response B: [response_b]
            
            Which is better for [criteria]?
            Winner: [A/B/Tie]
            Reasoning: [explanation]
      
      best_practices:
        - "Use clear, specific criteria"
        - "Request justification for scores"
        - "Use multiple evaluator runs"
        - "Validate against human judgment"
    
    human_evaluation:
      description: "Human raters assess quality"
      design_considerations:
        - "Clear evaluation criteria"
        - "Rating scale definition"
        - "Evaluator training"
        - "Inter-rater reliability measurement"
      
      approaches:
        absolute_rating:
          description: "Rate each response independently"
          scale: "1-5 or 1-7 Likert scale"
        
        comparative_rating:
          description: "Compare responses to each other"
          method: "Pairwise comparison or ranking"
        
        binary_judgment:
          description: "Pass/fail against criteria"
          use_case: "Safety evaluation, format compliance"

---
# ┌─────────────────────────────────────────────────────────────────────────────┐
# │              SECTION 9: MODEL-SPECIFIC OPTIMIZATION                          │
# └─────────────────────────────────────────────────────────────────────────────┘

model_specific_optimization:
  description: >-
    Guidance for optimizing prompts for specific model families,
    leveraging their unique characteristics and capabilities.
  
  # ═══════════════════════════════════════════════════════════════════════════
  # 9.1 CLAUDE (ANTHROPIC)
  # ═══════════════════════════════════════════════════════════════════════════
  
  claude:
    model_family: "Anthropic Claude"
    versions:
      - "Claude 3.5 Sonnet"
      - "Claude 3 Opus"
      - "Claude 4 (Opus 4.5, Sonnet 4.5, Haiku 4.5)"
    
    characteristics:
      strengths:
        - "Strong instruction following"
        - "Nuanced reasoning"
        - "Code generation"
        - "Long context handling"
        - "Constitutional AI training"
      considerations:
        - "Tends toward verbose responses by default"
        - "Strong safety guardrails"
        - "Excellent at structured outputs"
    
    optimization_strategies:
      
      xml_tag_usage:
        description: "Claude excels with XML-structured prompts"
        recommendation: "Use XML tags for complex prompt organization"
        example: |
          <context>
          [Background information]
          </context>
          
          <instructions>
          [Task instructions]
          </instructions>
          
          <examples>
          [Demonstration examples]
          </examples>
      
      thinking_tags:
        description: "Extended thinking for complex reasoning"
        recommendation: "Use <thinking> tags for step-by-step reasoning"
        note: "Claude 4 models have native extended thinking"
      
      prefilling:
        description: "Control response format by starting the response"
        recommendation: "Use assistant prefill for format control"
        example:
          prompt: "[Instructions]\n\nAssistant: {"
          effect: "Forces JSON output format"
      
      system_prompt_structure:
        recommendation: "Use hierarchical XML structure for system prompts"
        key_sections:
          - "<identity>"
          - "<capabilities>"
          - "<guidelines>"
          - "<constraints>"
      
      conciseness_control:
        description: "Claude tends verbose - explicit brevity instructions help"
        techniques:
          - "Be concise. Skip preambles."
          - "Respond in under [X] words."
          - "Skip explanations unless asked."

  # ═══════════════════════════════════════════════════════════════════════════
  # 9.2 GPT (OPENAI)
  # ═══════════════════════════════════════════════════════════════════════════
  
  gpt:
    model_family: "OpenAI GPT"
    versions:
      - "GPT-4"
      - "GPT-4 Turbo"
      - "GPT-4o"
      - "o1 / o1-mini (reasoning models)"
    
    characteristics:
      strengths:
        - "Broad knowledge base"
        - "Strong creative writing"
        - "Good at following complex instructions"
        - "Multimodal capabilities (GPT-4V)"
      considerations:
        - "JSON mode available for structured output"
        - "Function calling for tool use"
        - "o1 models have built-in reasoning"
    
    optimization_strategies:
      
      json_mode:
        description: "Native JSON output mode"
        recommendation: "Use response_format: json_object for structured output"
        prompt_requirement: "Prompt must mention 'JSON' when using JSON mode"
      
      function_calling:
        description: "Native tool use capability"
        recommendation: "Use function definitions for tool-based tasks"
        structure:
          type: "function"
          function:
            name: "tool_name"
            description: "tool description"
            parameters: "JSON schema"
      
      o1_reasoning:
        description: "o1 models have internal reasoning"
        recommendations:
          - "Don't include step-by-step instructions"
          - "Don't use CoT prompting - it's built in"
          - "Focus on clear problem statement"
          - "Simpler prompts often better"

  # ═══════════════════════════════════════════════════════════════════════════
  # 9.3 GEMINI (GOOGLE)
  # ═══════════════════════════════════════════════════════════════════════════
  
  gemini:
    model_family: "Google Gemini"
    versions:
      - "Gemini Pro"
      - "Gemini Ultra"
      - "Gemini 1.5 Pro"
      - "Gemini 2.0"
    
    characteristics:
      strengths:
        - "Very long context windows (1M+ tokens)"
        - "Strong multimodal capabilities"
        - "Good at reasoning tasks"
        - "Native code execution"
      considerations:
        - "Different safety thresholds"
        - "Strong at handling long documents"
    
    optimization_strategies:
      
      long_context:
        description: "Leverage extended context capabilities"
        recommendations:
          - "Can process entire documents/codebases"
          - "Use for document QA over long texts"
          - "Consider context position effects"
      
      multimodal:
        description: "Native image and video understanding"
        recommendations:
          - "Interleave images with text naturally"
          - "Reference images by position in prompt"
          - "Leverage video understanding for Gemini 2.0"

  # ═══════════════════════════════════════════════════════════════════════════
  # 9.4 OPEN SOURCE MODELS
  # ═══════════════════════════════════════════════════════════════════════════
  
  open_source:
    model_families:
      llama:
        name: "Meta Llama"
        versions: ["Llama 2", "Llama 3", "Llama 3.1", "Llama 4"]
        optimization:
          - "Benefits strongly from role prompting"
          - "System prompts in specific format"
          - "Good with few-shot examples"
      
      mistral:
        name: "Mistral AI"
        versions: ["Mistral 7B", "Mixtral 8x7B", "Mistral Large"]
        optimization:
          - "Strong instruction following"
          - "Efficient at reasoning tasks"
          - "Good few-shot learner"
      
      deepseek:
        name: "DeepSeek"
        versions: ["DeepSeek-V2", "DeepSeek-R1"]
        optimization:
          - "R1 has built-in reasoning like o1"
          - "Strong at code and math"
          - "Efficient architectures"
    
    general_recommendations:
      - "Test prompts specifically on target model"
      - "Open source models vary more in behavior"
      - "May need more explicit instructions"
      - "Consider fine-tuning for specific use cases"

---
# ┌─────────────────────────────────────────────────────────────────────────────┐
# │              SECTION 10: PRODUCTION OPERATIONS                               │
# └─────────────────────────────────────────────────────────────────────────────┘

production_operations:
  description: >-
    Best practices for deploying and maintaining prompts in production
    environments at scale.
  
  # ═══════════════════════════════════════════════════════════════════════════
  # 10.1 PROMPT MANAGEMENT
  # ═══════════════════════════════════════════════════════════════════════════
  
  prompt_management:
    
    version_control:
      practices:
        - "Store prompts in version control (git)"
        - "Use semantic versioning for changes"
        - "Document changes in commit messages"
        - "Maintain changelog for major prompts"
      
      versioning_schema:
        major: "Breaking changes to input/output contract"
        minor: "New capabilities, backward compatible"
        patch: "Bug fixes, minor improvements"
    
    prompt_registry:
      description: "Centralized management of production prompts"
      features:
        - "Unique identifiers for each prompt"
        - "Version history and rollback"
        - "Deployment status tracking"
        - "Performance metrics association"
      
      metadata_schema:
        prompt_id: "Unique identifier"
        version: "Semantic version"
        name: "Human-readable name"
        description: "Purpose and usage"
        owner: "Responsible team/person"
        created_at: "Creation timestamp"
        updated_at: "Last update timestamp"
        status: "draft | testing | production | deprecated"
        model_compatibility: "Tested model versions"
        performance_baseline: "Expected metrics"
    
    environment_management:
      environments:
        development:
          purpose: "Experimentation and initial testing"
          constraints: "None - free exploration"
        staging:
          purpose: "Pre-production testing"
          constraints: "Mirrors production, uses test data"
        production:
          purpose: "Live deployment"
          constraints: "Strict change control"
      
      promotion_process:
        - "Development testing complete"
        - "Peer review of changes"
        - "Staging deployment and testing"
        - "Performance validation"
        - "Approval for production"
        - "Gradual rollout with monitoring"

  # ═══════════════════════════════════════════════════════════════════════════
  # 10.2 MONITORING AND OBSERVABILITY
  # ═══════════════════════════════════════════════════════════════════════════
  
  monitoring:
    
    key_metrics:
      performance:
        - "Response latency (p50, p95, p99)"
        - "Token usage (input, output)"
        - "Error rates"
        - "Timeout rates"
      
      quality:
        - "User satisfaction scores"
        - "Task completion rates"
        - "Accuracy metrics (if measurable)"
        - "Hallucination rates"
      
      safety:
        - "Refusal rates"
        - "Content policy violations"
        - "Prompt injection attempts"
        - "Jailbreak attempts"
    
    alerting:
      conditions:
        - "Error rate exceeds threshold"
        - "Latency exceeds SLA"
        - "Quality metrics drop significantly"
        - "Unusual usage patterns"
      
      response_playbooks:
        - "Identify affected prompts/users"
        - "Assess severity and impact"
        - "Implement mitigation (rollback if needed)"
        - "Root cause analysis"
        - "Preventive measures"
    
    logging:
      what_to_log:
        - "Prompt version used"
        - "Input/output (with PII handling)"
        - "Latency and token counts"
        - "Error messages"
        - "Model version"
      
      retention_considerations:
        - "Compliance requirements"
        - "Debugging needs"
        - "Cost constraints"
        - "Privacy implications"

  # ═══════════════════════════════════════════════════════════════════════════
  # 10.3 COST OPTIMIZATION
  # ═══════════════════════════════════════════════════════════════════════════
  
  cost_optimization:
    
    strategies:
      prompt_efficiency:
        description: "Minimize tokens while maintaining quality"
        techniques:
          - "Remove unnecessary verbosity"
          - "Use efficient delimiters"
          - "Compress context where possible"
          - "Use smaller prompts for simpler tasks"
      
      model_selection:
        description: "Match model capability to task requirements"
        approach:
          - "Use smaller models for simple tasks"
          - "Reserve larger models for complex tasks"
          - "Consider fine-tuned smaller models"
      
      caching:
        description: "Avoid redundant API calls"
        techniques:
          - "Cache common query responses"
          - "Use prompt caching (where available)"
          - "Implement semantic caching for similar queries"
      
      batching:
        description: "Combine requests for efficiency"
        considerations:
          - "Batch similar requests"
          - "Balance latency vs cost"
          - "Consider async processing"

---
# ┌─────────────────────────────────────────────────────────────────────────────┐
# │              SECTION 11: REFERENCE APPENDICES                                │
# └─────────────────────────────────────────────────────────────────────────────┘

appendices:
  
  # ═══════════════════════════════════════════════════════════════════════════
  # A: PROMPT TEMPLATE LIBRARY
  # ═══════════════════════════════════════════════════════════════════════════
  
  template_library:
    description: "Ready-to-use prompt templates for common tasks"
    
    classification:
      template: |
        Classify the following text into one of these categories:
        [category_1, category_2, category_3, ...]
        
        Text: {input_text}
        
        Respond with only the category name.
    
    summarization:
      template: |
        Summarize the following text in {length} words or less.
        Focus on: {focus_areas}
        
        Text:
        {input_text}
        
        Summary:
    
    extraction:
      template: |
        Extract the following information from the text:
        {fields_to_extract}
        
        Text:
        {input_text}
        
        Respond in JSON format:
        {
          "field_1": "value",
          "field_2": "value"
        }
    
    analysis:
      template: |
        Analyze the following {content_type} and provide:
        1. Summary of main points
        2. Key insights
        3. Potential concerns or issues
        4. Recommendations
        
        Content:
        {input_content}
        
        Analysis:
    
    code_generation:
      template: |
        Write {language} code that {task_description}.
        
        Requirements:
        {requirements_list}
        
        Include:
        - Clear comments
        - Error handling
        - Example usage
        
        ```{language}
        
    
    creative_writing:
      template: |
        Write a {content_type} about {topic}.
        
        Style: {style_description}
        Tone: {tone}
        Length: approximately {word_count} words
        
        Additional requirements:
        {additional_requirements}

  # ═══════════════════════════════════════════════════════════════════════════
  # B: COMMON PITFALLS AND SOLUTIONS
  # ═══════════════════════════════════════════════════════════════════════════
  
  common_pitfalls:
    
    - pitfall: "Prompt is too vague"
      symptoms:
        - "Inconsistent output quality"
        - "Model interprets task incorrectly"
        - "High variance between runs"
      solutions:
        - "Add specific requirements"
        - "Include examples"
        - "Define success criteria explicitly"
    
    - pitfall: "Output format inconsistent"
      symptoms:
        - "Sometimes JSON, sometimes prose"
        - "Missing required fields"
        - "Extra unwanted content"
      solutions:
        - "Use prefilling"
        - "Add explicit format specification"
        - "Include format examples"
        - "Use JSON mode where available"
    
    - pitfall: "Model refuses appropriate requests"
      symptoms:
        - "Excessive safety refusals"
        - "Won't complete benign tasks"
        - "Overly cautious responses"
      solutions:
        - "Clarify legitimate context"
        - "Reframe request constructively"
        - "Add appropriate context"
    
    - pitfall: "Hallucinations in output"
      symptoms:
        - "Fabricated facts"
        - "Non-existent citations"
        - "Incorrect information"
      solutions:
        - "Add uncertainty acknowledgment instructions"
        - "Use RAG for factual grounding"
        - "Request source citations"
        - "Add verification prompts"
    
    - pitfall: "Context window exceeded"
      symptoms:
        - "API errors"
        - "Truncated context"
        - "Missing information in response"
      solutions:
        - "Summarize long context"
        - "Use chunking strategies"
        - "Prioritize most relevant content"
        - "Consider larger context models"
    
    - pitfall: "Reasoning errors in complex tasks"
      symptoms:
        - "Incorrect conclusions"
        - "Skipped reasoning steps"
        - "Logical inconsistencies"
      solutions:
        - "Add chain-of-thought prompting"
        - "Break into smaller steps"
        - "Add verification prompts"
        - "Use self-consistency"

  # ═══════════════════════════════════════════════════════════════════════════
  # C: GLOSSARY
  # ═══════════════════════════════════════════════════════════════════════════
  
  glossary:
    
    chain_of_thought:
      term: "Chain-of-Thought (CoT)"
      definition: >-
        A prompting technique that elicits step-by-step reasoning
        before the final answer, improving performance on complex tasks.
    
    context_window:
      term: "Context Window"
      definition: >-
        The maximum number of tokens a model can process in a single
        request, including both input prompt and generated output.
    
    few_shot:
      term: "Few-Shot Learning"
      definition: >-
        Providing a small number of examples in the prompt to demonstrate
        the desired task, enabling in-context learning without fine-tuning.
    
    hallucination:
      term: "Hallucination"
      definition: >-
        When a model generates plausible-sounding but factually incorrect
        or fabricated information.
    
    in_context_learning:
      term: "In-Context Learning"
      definition: >-
        The ability of language models to learn tasks from examples
        provided in the prompt without updating model weights.
    
    prefilling:
      term: "Prefilling"
      definition: >-
        Technique of pre-populating the beginning of the model's response
        to guide output format and content direction.
    
    prompt_injection:
      term: "Prompt Injection"
      definition: >-
        A security vulnerability where user input is crafted to override
        or manipulate the system prompt instructions.
    
    rag:
      term: "Retrieval-Augmented Generation (RAG)"
      definition: >-
        A technique that retrieves relevant documents from a knowledge
        base and includes them as context for generation.
    
    system_prompt:
      term: "System Prompt"
      definition: >-
        Persistent instructions that define model behavior, typically
        set at the beginning of a conversation or API call.
    
    temperature:
      term: "Temperature"
      definition: >-
        A parameter controlling randomness in model outputs. Lower values
        (0-0.3) produce more deterministic responses; higher values
        (0.7-1.0) produce more diverse/creative outputs.
    
    token:
      term: "Token"
      definition: >-
        The basic unit of text processing for LLMs. Roughly 0.75 words
        per token for English text, though varies by language and content.
    
    zero_shot:
      term: "Zero-Shot"
      definition: >-
        Performing a task without any demonstration examples, relying
        solely on task instructions and model pre-training.

  # ═══════════════════════════════════════════════════════════════════════════
  # D: FURTHER READING
  # ═══════════════════════════════════════════════════════════════════════════
  
  further_reading:
    
    documentation:
      - title: "Anthropic Prompt Engineering Guide"
        url: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"
        focus: "Claude-specific techniques"
      
      - title: "OpenAI Prompt Engineering Guide"
        url: "https://platform.openai.com/docs/guides/prompt-engineering"
        focus: "GPT-specific techniques"
      
      - title: "DAIR.AI Prompt Engineering Guide"
        url: "https://www.promptingguide.ai/"
        focus: "Comprehensive technique coverage"
    
    research_papers:
      - title: "Chain-of-Thought Prompting"
        authors: "Wei et al., 2022"
        focus: "Foundational CoT paper"
      
      - title: "Tree of Thoughts"
        authors: "Yao et al., 2023"
        focus: "Deliberate problem-solving"
      
      - title: "ReAct: Reasoning and Acting"
        authors: "Yao et al., 2023"
        focus: "Interleaved reasoning and action"
      
      - title: "Self-Consistency"
        authors: "Wang et al., 2023"
        focus: "Ensemble reasoning"
      
      - title: "RAG: Retrieval-Augmented Generation"
        authors: "Lewis et al., 2020"
        focus: "Knowledge-augmented generation"
    
    tools:
      - name: "LangChain"
        description: "Framework for LLM application development"
        url: "https://langchain.com"
      
      - name: "LlamaIndex"
        description: "Data framework for LLM applications"
        url: "https://llamaindex.ai"
      
      - name: "PromptHub"
        description: "Prompt management and optimization"
        url: "https://prompthub.us"

---
# ═══════════════════════════════════════════════════════════════════════════════
# END OF PROMPT ENGINEERING MASTER REFERENCE ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════════
#
# This document provides a comprehensive reference for prompt engineering
# best practices. For PKB integration:
#
# 1. Use wiki-links: Convert [[bracketed terms]] to Obsidian links
# 2. Create atomic notes: Extract individual techniques as separate notes
# 3. Build MOCs: Create Maps of Content for major sections
# 4. Add examples: Expand template library with your own examples
# 5. Track evolution: Update as the field advances
#
# Version History:
# - 1.0.0 (2025-12-27): Initial comprehensive release
#
# ═══════════════════════════════════════════════════════════════════════════════
`````
