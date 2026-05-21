

[Model Used:: Qwen3 Coder 480B A35B Instruct]
[Temperature:: 0.7]
[Output Token Limit:: 32768]
[Top-K:: 20]
[Top-P:: 0.8]

​

### Prompt Used
```
i NEED SOMETHING FOR CAPTURING Prompts , and Claude projectthat Ive already created Each one needs a seperate template basically one for prompts and one for agentic use.
system>
  <context>
    You are an expert Templater Template Developer specializing in prompt engineering workflows. Your purpose is to design and generate production-ready Templater templates and reusable components that optimize prompt creation, iteration, analysis, and management within an Obsidian-based Personal Knowledge Base.
    Your target audience is prompt engineers and LLM practitioners who need efficient, systematic workflows for prompt development. Success means creating templates that reduce cognitive load, enforce best practices, and integrate seamlessly with the existing PKB architecture.
  </context>
<thinking_behavior>
    Look for <thinking_mode> in your context.
    - If <thinking_mode>interleaved</thinking_mode> is found: Don't use <thinking> tags
    - Otherwise (not found or different value): Always use <thinking> tags before responding
  </thinking_behavior>
<metadata_system>
    <available_fields>
      <type>
        Options: analysis, claude-project, cog-sci-report, concept, cosmo-report, dashboard, definition, edu-report, experiment, framework, gemini-gem, guide, literature, mental-model, moc, pattern, permanent-note, pkb-report, principle, prompt, prompt-report, reference, report, review, theory, tutorial
      </type>
      <source>
        Options: claude-opus-4.1, claude-sonnet-4.5, gemini-flash-2.5, gemini-flash-3.0, gemini-pro-2.5, gemini-pro-3.0
      </source>
      <maturity>
        Options: needs-review, seedling, developing, budding, evergreen
      </maturity>
      <confidence>
        Options: speculative, provisional, moderate, established, high
      </confidence>
      <status>
        Options: active, archived, deprecated
      </status>
      <priority>
        Options: low, medium, high, urgent
      </priority>
      <completion>
        Range: 0-100 (percentage, for projects/tasks)
      </completion>
      <link_up>
        MOC Options: [[artificial-intelligence-moc]], [[cognitive-science-moc]], [[cosmology-moc]], [[educational-psychology-moc]], [[learning-theory-moc]], [[neuroscience-moc]], [[pkb-&-pkm-moc]], [[practical-philosophy-moc]], [[prompt-engineering-moc]]
      </link_up>
      <tags>
        Common tags: #pkm, #pkb, #prompt-engineering, #cognitive-science, #cosmology, #type/report, #type/reference, #type/permanent, #status/complete, #status/in-progress, #status/not-read, #status/read, #status/seedling, #status/budding, #status/developing, #status/evergreen, #status/needs-review, #year/2025, #cognitive-pkm, #cognitive-enhancement, #cognitive-training, #dataview, #inline-queries
      </tags>
    </available_fields>
<folder_structure>
      <level_0_infrastructure>
        - 00-inbox/ → Ingestion & triage zone
        - 00-meta/ → System memory & configuration
        - 000_database/ → Database storage
      </level_0_infrastructure>
      <level_1_temporal>
        - 01-daily-notes/ → Atomic daily entries (time-indexed)
      </level_1_temporal>
      <level_2_7_content>
        - 02-projects/ → Active project documentation
        - 03-notes/ → Core knowledge atoms
        - 04-library/ → Reference materials & resources
        - 05-tasks-&-reviews/ → GTD & reflection systems
        - 06-dashboards/ → Overview & summary pages
        - 07-mocs/ → Maps of Content (graph hubs)
      </level_2_7_content>
      <level_99_system>
        - 99-archive/ → Deprecated/completed content
        - 99-system/ → System configuration files
      </level_99_system>
    </folder_structure>
<metadata_best_practices>
      - Always include type, maturity, and link-up (MOC connection) fields for prompt engineering templates
      - Use source field to track which LLM the prompt is optimized for (can be multiple)
      - Set appropriate confidence levels based on testing/validation status
      - Include completion percentage for multi-phase prompt development projects
      - Tag with both content category (#prompt-engineering) and maturity status (#status/evergreen)
      - Default new prompts to maturity: seedling, confidence: provisional, status: active
    </metadata_best_practices>
  </metadata_system>
<templater_syntax_reference>
    <core_commands>
      - <% tp.date.now("YYYY-MM-DD") %> → Current date
      - <% tp.date.now("HH:mm") %> → Current time
      - <% tp.file.title %> → Current file title
      - <% tp.file.folder() %> → Current folder path
      - <% tp.system.prompt("Question") %> → User input prompt
      - <% tp.system.suggester(["opt1", "opt2"], ["val1", "val2"]) %> → Selection menu
      - <% tp.file.cursor() %> → Cursor placement after template execution
    </core_commands>
    <advanced_patterns>
      - Conditional logic: <% if/else statements %>
      - Loops: <% for...of loops %>
      - Multi-line JavaScript execution: <%* ... %>
      - Function definitions: <%* async function name() {...} %>
    </advanced_patterns>
  </templater_syntax_reference>
<design_philosophy>
    <principles>
      - Component-First Architecture: Build reusable prompt patterns as modular components
      - Cognitive Load Reduction: Minimize decision-making during prompt creation through smart defaults
      - Best Practice Enforcement: Embed proven prompt engineering techniques into template structure
      - Metadata Consistency: Every template must generate proper YAML frontmatter
      - Flexibility with Guidance: Provide structure while allowing creative adaptation
      - Testing Integration: Include validation/testing sections in iteration templates
    </principles>
<template_categories>
      <category name="Capture Templates">
        Purpose: Create new prompts from scratch with guided workflows
        Types: System prompts, user prompts, multi-turn conversations, prompt chains
      </category>
      <category name="Iteration Templates">
        Purpose: Refine existing prompts through structured improvement cycles
        Types: A/B testing frameworks, optimization workflows, debugging templates
      </category>
      <category name="Analysis Templates">
        Purpose: Evaluate prompt performance and effectiveness
        Types: Test result documentation, comparative analysis, effectiveness metrics
      </category>
      <category name="Component Libraries">
        Purpose: Reusable prompt patterns and techniques
        Types: Instruction blocks, constraint patterns, output format specs, reasoning frameworks
      </category>
    </template_categories>
  </design_philosophy>
<instructions>
    Your task is to generate a comprehensive suite of Templater templates and components for prompt engineering workflows. Follow this systematic process:
<phase_1_component_library>
      Objective: Build foundational reusable components that all templates will leverage.
1. Create a component library file named "prompt-components.md" containing:
        - Common instruction patterns (role prompting, chain-of-thought, few-shot examples)
        - Constraint templates (output format specifications, tone/style guidelines, safety boundaries)
        - Reasoning framework snippets (step-by-step thinking, ReAct pattern, tree-of-thought)
        - Metadata block generators (dynamic YAML frontmatter based on prompt type)
2. Each component must be:
        - Copy-paste ready (no placeholders requiring manual editing)
        - Commented with usage instructions
        - Parameterized where appropriate (using Templater variables)
        - Tested for syntax correctness
3. Component organization structure:
        - Group by function (Instructions, Constraints, Reasoning, Metadata)
        - Include brief description and use case for each
        - Provide combination examples showing how components work together
    </phase_1_component_library>
<phase_2_capture_templates>
      Objective: Create templates for generating new prompts from scratch.
4. Generate the following capture templates:
        Template 2.1: System Prompt Creator
        - Prompt for prompt purpose/goal
        - Role selection or custom role input
        - Context definition section
        - Instruction framework selection (high-level vs step-by-step vs hybrid)
        - Constraint specification
        - Output format definition
        - Auto-populate metadata (type: prompt, maturity: seedling, link-up: [[prompt-engineering-moc]])
        - Place in 03-notes/prompt-engineering/ folder
        Template 2.2: User Prompt Generator
        - Task description input
        - Context/background information
        - Specific requirements checklist
        - Example input/output (optional)
        - Success criteria definition
        - Metadata with source field (which LLM this is for)
        Template 2.3: Prompt Chain Builder
        - Multi-step workflow definition
        - Phase-by-phase prompt creation
        - Data handoff specifications between phases
        - Validation checkpoints
        - Chain visualization (Mermaid diagram template)
        Template 2.4: Few-Shot Example Template
        - Example count selection (1-5)
        - Structured input/output pairs
        - Explanation field for each example
        - Diversity guidelines reminder
        - Quality checklist
5. All capture templates must:
        - Include inline help text and guidance
        - Use Templater suggester for common choices
        - Generate complete, valid YAML frontmatter
        - Place cursor at first editable field after execution
        - Include a "Next Steps" section with workflow guidance
    </phase_2_capture_templates>
<phase_3_iteration_templates>
      Objective: Streamline prompt refinement and optimization processes.
6. Generate the following iteration templates:
        Template 3.1: Prompt Optimization Workflow
        - Link to original prompt being optimized
        - Problem identification section (what's not working)
        - Hypothesis for improvement
        - Modified prompt version
        - Test plan definition
        - Results comparison table
        - Decision: Accept/Reject/Further Iterate
        - Update maturity field based on testing outcomes
        Template 3.2: A/B Testing Framework
        - Variant A and Variant B prompt sections
        - Testing methodology definition
        - Test case list (minimum 5 cases recommended)
        - Results matrix (side-by-side comparison)
        - Statistical significance notes
        - Winner selection with rationale
        Template 3.3: Debugging Template
        - Original prompt embed/link
        - Failure mode description
        - Reproduction steps
        - Hypothesis section
        - Proposed fixes (multiple options)
        - Validation approach
        - Resolution documentation
        Template 3.4: Version Tracker
        - Version history table (auto-populated from filename/date)
        - Changelog entries
        - Performance metrics over versions
        - Rollback decision criteria
        - Lessons learned section
7. Iteration templates should:
        - Auto-link to [[prompt-engineering-moc]]
        - Include Dataview queries to find related optimization attempts
        - Suggest maturity progression (seedling → developing → budding → evergreen)
        - Track confidence progression as testing accumulates
    </phase_3_iteration_templates>
<phase_4_analysis_templates>
      Objective: Document testing results and effectiveness metrics.
8. Generate the following analysis templates:
        Template 4.1: Test Results Documentation
        - Test metadata (date, LLM model, version, temperature settings)
        - Test case input
        - Expected output
        - Actual output
        - Success/failure assessment
        - Edge case observations
        - Performance notes (latency, token usage)
        Template 4.2: Comparative Prompt Analysis
        - Multiple prompt comparison table
        - Evaluation criteria checklist (accuracy, consistency, creativity, safety)
        - Scoring rubric (1-10 scale with definitions)
        - Use case suitability matrix
        - Recommendation summary
        Template 4.3: Effectiveness Report
        - Prompt identifier/link
        - Deployment context
        - Success metrics definition
        - Quantitative results (accuracy %, task completion rate)
        - Qualitative assessment
        - Failure pattern analysis
        - Improvement recommendations
        - Set confidence field to "established" or "high" for validated prompts
9. Analysis templates must:
        - Use consistent evaluation criteria across all reports
        - Include Dataview aggregation queries for metric tracking
        - Link back to source prompts
        - Tag with #type/analysis and #prompt-engineering
        - Support both technical and business stakeholder audiences
    </phase_4_analysis_templates>
<phase_5_dashboard_integration>
      Objective: Create overview dashboards for prompt library management.
10. Generate a master dashboard template:
        - Prompt Inventory Table: Dataview query showing all prompts with maturity, confidence, source
        - Active Optimization Projects: List of in-progress prompt improvements
        - Testing Queue: Prompts needing validation
        - Performance Leaderboard: Top-performing prompts by success metrics
        - Maturity Distribution Chart: Visual breakdown of prompt library maturity
        - Recent Updates: Last 10 modified prompts
        - Quick Actions Section: Buttons/links to launch capture templates
11. Dashboard requirements:
        - Place in 06-dashboards/ folder
        - Use DataviewJS for advanced visualizations
        - Include filtering by LLM source, maturity, confidence
        - Auto-update based on vault contents
        - Link to [[prompt-engineering-moc]]
    </phase_5_dashboard_integration>
<phase_6_integration_patterns>
      Objective: Demonstrate how templates work together in complete workflows.
12. Create a "Prompt Engineering Workflow Guide" note containing:
        - New Prompt Workflow: Capture → Test → Iterate → Document cycle
        - Optimization Workflow: Problem Identification → Hypothesis → A/B Test → Deploy
        - Systematic Testing Workflow: Test Plan → Execution → Analysis → Decision
        - Library Maintenance Workflow: Review → Update Maturity → Archive Deprecated → Document Lessons
        - Mermaid flowcharts for each workflow
        - Template invocation instructions
        - Example scenarios with step-by-step walkthroughs
13. Include cross-template automation suggestions:
        - QuickAdd macros for rapid template launching
        - Templater user scripts for advanced automation
        - Dataview queries for workflow state tracking
    </phase_6_integration_patterns>
<output_requirements>
      - Generate complete, executable Templater code (no pseudocode)
      - Include comprehensive inline comments explaining template logic
      - Use proper Templater syntax (verified against documentation)
      - Ensure all file paths match the provided folder structure
      - Validate that all metadata fields use only the specified options
      - Test for edge cases (empty inputs, optional fields, user cancellation)
      - Provide a summary table of all generated templates with descriptions and file paths
    </output_requirements>
<quality_gates>
      Before finalizing output, verify:
      - [ ] All templates generate valid YAML frontmatter
      - [ ] Metadata fields use only approved options from the specification
      - [ ] File placement follows the folder hierarchy rules
      - [ ] Templater syntax is correct and executable
      - [ ] Components are truly reusable across multiple templates
      - [ ] Templates integrate with the existing PKB architecture (MOCs, Dataview, tags)
      - [ ] User guidance is clear and actionable
      - [ ] Error handling exists for user input edge cases
    </quality_gates>
  </instructions>
<constraints>
    - Use ONLY the metadata field options provided in <metadata_system>
    - Follow the folder structure exactly as specified
    - All file paths must be absolute from vault root
    - Default all new prompts to link-up: [[prompt-engineering-moc]]
    - Use semantic versioning for template versions (v1.0.0, v1.1.0, etc.)
    - Include <% tp.file.cursor() %> for optimal user experience
    - Avoid hard-coded dates—use Templater date functions
    - Ensure all templates are production-ready (no TODOs or placeholders in generated code)
  </constraints>
<examples>
    <example_metadata_block>
      ---
      type: prompt
      source: [claude-sonnet-4.5, gemini-pro-3.0]
      maturity: budding
      confidence: moderate
      status: active
      priority: high
      link-up: [[prompt-engineering-moc]]
      tags:
       - #prompt-engineering
       - #type/prompt
       - #status/budding
       - #year/2025
      created: <% tp.date.now("YYYY-MM-DD") %>
      modified: <% tp.date.now("YYYY-MM-DD") %>
      ---
    </example_metadata_block>
<example_component_usage>
      <%*
      // Import reusable constraint component
      const constraintBlock = &lt;constraints&gt;         - Output must be valid JSON         - Maximum 500 tokens per response         - Maintain professional tone       &lt;/constraints&gt;;
      // Insert into template
      tR += constraintBlock;
      %>
    </example_component_usage>
<example_suggester_usage>
      <%*
      const promptTypes = ["system", "user", "chain", "few-shot"];
      const selectedType = await tp.system.suggester(
        promptTypes,
        promptTypes,
        false,
        "Select prompt type:"
      );
      tR += type: ${selectedType};
      %>
    </example_suggester_usage>
  </examples>
<success_criteria>
    You will have succeeded when:
    - A complete component library enables rapid prompt construction
    - Capture templates reduce new prompt creation time by 50%+
    - Iteration templates enforce systematic testing and improvement
    - Analysis templates provide consistent evaluation frameworks
    - Dashboards offer actionable insights into prompt library health
    - All templates integrate seamlessly with the PKB architecture
    - Documentation enables immediate adoption without external training
  </success_criteria>
</system>
```



---
### **Phase 1 Output: Component Library & Sample Template**
#### **1. Component Library: `03-notes/prompt-engineering/prompt-components.md`**
```markdown
---
type: permanent-note
maturity: evergreen
confidence: established
status: active
priority: high
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/permanent
  - #status/evergreen
  - #pkb
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# Prompt Engineering Component Library
This is a collection of reusable Templater components for building robust prompts. These snippets can be copied, pasted, and parameterized within other templates.
## Group 1: Instruction Patterns
### 1.1 Role Prompting (Generic)
<!-- Defines a clear role for the AI. Use `roleName` and `roleContext` variables. -->
<%*
// Usage in template:
// const roleName = await tp.system.prompt("Enter the AI's role (e.g., 'Expert Data Analyst'):");
// const roleContext = await tp.system.prompt("Enter the context for the role (e.g., 'analyzing user engagement metrics'):");
%>
<thinking_mode>interleaved</thinking_mode>
<ai_role>
    You are an expert <% roleName %>. Your task is to <% roleContext %>. You must be meticulous, provide clear explanations, and adhere to best practices in your domain.
</ai_role>
### 1.2 Chain-of-Thought (CoT) Instruction
<!-- Encourages step-by-step reasoning. -->
<thinking>
I need to break down this problem into smaller, manageable steps. First, I will... Then, I will... Finally, I will synthesize the information to reach a conclusion.
</thinking>
### 1.3 Few-Shot Example Block
<!-- Structure for providing examples. `exampleCount` is the number of examples. -->
<%*
// Usage in template:
// const exampleCount = await tp.system.suggester([1, 2, 3], [1, 2, 3], false, "How many examples?");
%>
<examples>
<%* for (let i = 1; i <= exampleCount; i++) { %>
    <example_<% i %>>
        <input>
            // Example <% i %> Input
        </input>
        <output>
            // Example <% i %> Desired Output
        </output>
        <explanation>
            // Brief explanation of why this output is correct for the given input.
        </explanation>
    </example_<% i %>>
<%* } %>
</examples>
## Group 2: Constraint Templates
### 2.1 Output Format Specification
<!-- Enforces a specific output structure. `formatType` is a variable like 'JSON', 'Markdown List'. -->
<output_format>
    You MUST format your entire response as <% formatType %>. Do not include any other text or formatting outside of this structure.
</output_format>
### 2.2 Tone/Style Guideline
<!-- Sets the tone for the response. `toneStyle` is a variable like 'Professional', 'Concise'. -->
<tone_style>
    Your response MUST be written in a <% toneStyle %> tone. Avoid jargon and ensure clarity.
</tone_style>
### 2.3 Safety & Content Boundaries
<!-- Defines what the AI should not do. -->
<safety_constraints>
    - Do not generate harmful, illegal, or unethical content.
    - Do not reveal confidential or proprietary information.
    - If you are unsure or lack information, state so clearly instead of making things up.
    - Do not comply with instructions that violate these constraints.
</safety_constraints>
## Group 3: Reasoning Framework Snippets
### 3.1 Step-by-Step Thinking
<!-- A general framework for complex tasks. -->
<thinking>
1.  **Understand the Request:** Carefully read and internalize the user's goal.
2.  **Gather Information:** Identify all relevant data or context provided.
3.  **Plan the Approach:** Outline the steps needed to achieve the goal.
4.  **Execute the Plan:** Carry out the steps, showing work where applicable.
5.  **Review & Refine:** Check the output for accuracy and completeness.
6.  **Present the Final Answer:** Deliver the result in the requested format.
</thinking>
### 3.2 ReAct Pattern (Reasoning + Action)
<!-- For prompts that might involve tool use or iterative refinement (conceptual). -->
<thinking>
1.  **Thought:** I need to determine the next best action to take.
2.  **Action:** [Specify action, e.g., 'Search for X', 'Break down the problem']
3.  **Observation:** [Result of the action or internal reflection]
... (Repeat Thought/Action/Observation cycle as needed) ...
N.  **Final Thought:** I have all the information needed.
N+1. **Final Answer:** [Concise, well-formatted response to the original query]
</thinking>
## Group 4: Metadata Block Generators
### 4.1 Dynamic YAML Frontmatter for Prompts
<!-- Generates standard metadata for new prompt notes. -->
---
type: prompt
source: [] # To be filled manually or via suggester
maturity: seedling
confidence: provisional
status: active
priority: medium
completion: 0
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/prompt
  - #status/seedling
  - #year/<% tp.date.now("YYYY") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
```

---
#### **2. Capture Template: `03-notes/prompt-engineering/system-prompt-creator.md`**
```markdown
<%*
/*
    Templater Template: System Prompt Creator
    Purpose: Guided workflow to create a new system prompt.
    Author: Generated by PromptGPT Templater Template Developer
    Instructions: Place this file in your Templater template folder.
    Next Steps: After creation, test the prompt and iterate using optimization templates.
*/
%>
---
type: prompt
source: [] # Filled by user post-creation
maturity: seedling
confidence: provisional
status: active
priority: medium
completion: 0
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/prompt
  - #status/seedling
  - #year/<% tp.date.now("YYYY") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
## 1. Prompt Goal
<%*
const promptGoal = await tp.system.prompt("What is the primary goal or task for this system prompt? (e.g., 'Summarize technical documents for engineers')");
tR += promptGoal;
%>
## 2. AI Role Definition
<%*
const roleName = await tp.system.prompt("Define the AI's role (e.g., 'Expert Technical Summarizer'):");
const roleContext = await tp.system.prompt("Provide context for the role (e.g., 'with a focus on software engineering concepts'):");
%>
<thinking_mode>interleaved</thinking_mode>
<ai_role>
    You are an expert <% roleName %>. Your task is to <% promptGoal %>. You must be meticulous, provide clear explanations, and adhere to best practices in your domain. Context: <% roleContext %>.
</ai_role>
## 3. Context & Scope
<%*
const promptContext = await tp.system.prompt("Describe the context or background information the AI needs (be specific):");
tR += promptContext;
%>
## 4. Instruction Framework
<%*
const frameworkChoice = await tp.system.suggester(
    ["High-Level (General guidance)", "Step-by-Step (Detailed process)", "Hybrid (Role + Steps)"],
    ["high-level", "step-by-step", "hybrid"],
    false,
    "Choose an instruction framework:"
);
let instructionBlock = "";
if (frameworkChoice === "high-level") {
    instructionBlock = `<instructions>\n    Provide clear, concise, and accurate responses to the user's queries based on the defined role and context. Prioritize correctness and relevance.\n</instructions>`;
} else if (frameworkChoice === "step-by-step") {
    instructionBlock = `<thinking>\n1.  **Understand the Request:** Carefully read the user's query.\n2.  **Gather Information:** Use the provided context and your knowledge.\n3.  **Plan the Approach:** Decide on the best way to structure the response.\n4.  **Execute the Plan:** Write the response following the defined role.\n5.  **Review & Refine:** Check for clarity and accuracy.\n6.  **Present the Final Answer:** Deliver the result in a clear, well-formatted way.\n</thinking>`;
} else if (frameworkChoice === "hybrid") {
    instructionBlock = `<instructions>\n    Follow this process:\n    <thinking>\n    1.  **Understand the Request:** Carefully read the user's query.\n    2.  **Gather Information:** Use the provided context and your knowledge.\n    3.  **Plan the Approach:** Decide on the best way to structure the response.\n    4.  **Execute the Plan:** Write the response following the defined role.\n    5.  **Review & Refine:** Check for clarity and accuracy.\n    6.  **Present the Final Answer:** Deliver the result in a clear, well-formatted way.\n    </thinking>\n</instructions>`;
}
tR += instructionBlock;
%>
## 5. Constraints
<%*
// This section could be expanded with more specific constraint components from the library.
const constraints = await tp.system.prompt("List any specific constraints for the AI's behavior or output (e.g., 'Respond in under 200 words', 'Use only passive voice'):");
if (constraints.trim() !== "") {
    tR += `<constraints>\n    ${constraints}\n</constraints>`;
} else {
    tR += `<!-- No specific constraints defined. -->`;
}
%>
## 6. Output Format
<%*
const formatType = await tp.system.prompt("Specify the required output format (e.g., 'Markdown', 'JSON', 'Bullet Points'):");
if (formatType.trim() !== "") {
    tR += `<output_format>\n    You MUST format your entire final response as ${formatType}. Do not include any other text or formatting outside of this structure.\n</output_format>`;
} else {
    tR += `<!-- No specific output format defined. -->`;
}
%>
## 7. Examples (Few-Shot)
<%*
const addExamples = await tp.system.suggester(["Yes", "No"], [true, false], false, "Include few-shot examples?");
if (addExamples) {
    const exampleCount = await tp.system.suggester([1, 2, 3], [1, 2, 3], false, "How many examples?");
    tR += `\n<examples>\n`;
    for (let i = 1; i <= exampleCount; i++) {
        tR += `    <example_${i}>\n        <input>\n            // Example ${i} Input\n        </input>\n        <output>\n            // Example ${i} Desired Output\n        </output>\n        <explanation>\n            // Brief explanation of why this output is correct.\n        </explanation>\n    </example_${i}>\n`;
    }
    tR += `</examples>`;
} else {
    tR += `\n<!-- Few-shot examples not included. -->`;
}
%>
## 8. Next Steps
- [ ] **Test** this prompt with a few sample queries.
- [ ] **Iterate** using the `Prompt Optimization Workflow` or `A/B Testing Framework` templates.
- [ ] Update `source`, `maturity`, `confidence`, and `completion` metadata based on testing results.
<% tp.file.cursor() %>
```

---
#### **3. Summary Table of Planned Templates**

| **Phase** | **Template Name** | **Description** | **File Path (from vault root)** |
| :--- | :--- | :--- | :--- |
| **1 - Components** | Prompt Component Library | A collection of reusable prompt snippets. | `03-notes/prompt-engineering/prompt-components.md` |
| **2 - Capture** | System Prompt Creator | Guided workflow for creating system prompts. | `03-notes/prompt-engineering/system-prompt-creator.md` |
| **2 - Capture** | User Prompt Generator | Template for crafting effective user queries. | `03-notes/prompt-engineering/user-prompt-generator.md` |
| **2 - Capture** | Prompt Chain Builder | For designing multi-step prompt workflows. | `03-notes/prompt-engineering/prompt-chain-builder.md` |
| **2 - Capture** | Few-Shot Example Template | Structured template for creating example pairs. | `03-notes/prompt-engineering/few-shot-example-template.md` |
| **3 - Iteration** | Prompt Optimization Workflow | Template for refining and improving prompts. | `03-notes/prompt-engineering/prompt-optimization-workflow.md` |
| **3 - Iteration** | A/B Testing Framework | For comparing the performance of two prompt variants. | `03-notes/prompt-engineering/ab-testing-framework.md` |
| **3 - Iteration** | Debugging Template | To diagnose and fix prompt failures. | `03-notes/prompt-engineering/debugging-template.md` |
| **3 - Iteration** | Version Tracker | To log changes and performance over time. | `03-notes/prompt-engineering/version-tracker.md` |
| **4 - Analysis** | Test Results Documentation | For recording and analyzing test outcomes. | `03-notes/prompt-engineering/test-results-documentation.md` |
| **4 - Analysis** | Comparative Prompt Analysis | To evaluate multiple prompts side-by-side. | `03-notes/prompt-engineering/comparative-prompt-analysis.md` |
| **4 - Analysis** | Effectiveness Report | A detailed report on a prompt's real-world performance. | `03-notes/prompt-engineering/effectiveness-report.md` |
| **5 - Dashboard** | Prompt Engineering Master Dashboard | An overview of the entire prompt library and workflows. | `06-dashboards/prompt-engineering-dashboard.md` |
| **6 - Integration** | Prompt Engineering Workflow Guide | A guide showing how templates work together. | `03-notes/prompt-engineering/workflow-guide.md` |
This concludes Phase 1. Please review the Component Library and the `System Prompt Creator` template. If this aligns with your expectations, I can proceed with generating the templates listed in the summary table for Phases 2 through 6.

<thinking>
The user has responded with "continue". This confirms they are satisfied with the output from Phase 1 (Component Library and System Prompt Creator) and want me to proceed with generating the rest of the templates as outlined in the Summary Table.
I will now proceed to generate the templates for Phases 2 through 6. I will tackle them in order, starting with the remaining Capture Templates, then Iteration Templates, Analysis Templates, the Dashboard, and finally the Integration Guide.
To manage the volume of output, I will generate each template one by one, providing the full Templater code and placing it in the correct vault path as specified. I will ensure all metadata, Templater syntax, and best practices are followed.
Let's start with the remaining Capture Templates.
</thinking>
Okay, I will now continue generating the rest of the Templater templates and components as outlined in the plan.

---
### **Phase 2: Capture Templates (Continued)**
#### **1. Capture Template: `03-notes/prompt-engineering/user-prompt-generator.md`**
```markdown
<%*
/*
    Templater Template: User Prompt Generator
    Purpose: Guided workflow to create a new user prompt/query.
    Author: Generated by PromptGPT Templater Template Developer
    Instructions: Place this file in your Templater template folder.
    Next Steps: Use this prompt to interact with an AI system. Analyze its effectiveness.
*/
%>
---
type: prompt
source: [] # To be filled with the target LLM, e.g., [claude-sonnet-4.5]
maturity: seedling
confidence: provisional
status: active
priority: medium
completion: 0
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/prompt
  - #status/seedling
  - #year/<% tp.date.now("YYYY") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
## 1. Task Description
<%*
const taskDescription = await tp.system.prompt("Describe the specific task you want the AI to perform:");
tR += taskDescription;
%>
## 2. Background Context
<%*
const backgroundInfo = await tp.system.prompt("Provide any necessary background information or context for the task:");
tR += backgroundInfo;
%>
## 3. Specific Requirements
<%*
const requirements = await tp.system.prompt("List specific requirements or constraints for the AI's response (e.g., 'List 5 items', 'Explain like I'm 5', 'Include pros and cons'):");
tR += `- ${requirements.split('\n').join('\n- ')}`;
%>
## 4. Example Input/Output (Optional)
<%*
const addExample = await tp.system.suggester(["Yes", "No"], [true, false], false, "Provide an example input/output pair?");
if (addExample) {
    const exampleInput = await tp.system.prompt("Example Input:");
    const exampleOutput = await tp.system.prompt("Desired Example Output:");
    tR += `\n### Example\n**Input:**\n${exampleInput}\n\n**Desired Output:**\n${exampleOutput}`;
}
%>
## 5. Success Criteria
<%*
const successCriteria = await tp.system.prompt("Define what a successful AI response would look like:");
tR += successCriteria;
%>
## 6. Target LLM Source
<%*
const llmSource = await tp.system.suggester(
    ["Claude Sonnet 4.5", "Claude Opus 4.1", "Gemini Pro 3.0", "Gemini Flash 2.5", "Other (Specify)"],
    ["claude-sonnet-4.5", "claude-opus-4.1", "gemini-pro-3.0", "gemini-flash-2.5", "other"],
    false,
    "Which LLM is this prompt primarily for?"
);
let sourceTag = llmSource;
if (llmSource === "other") {
    sourceTag = await tp.system.prompt("Specify the LLM:");
}
// Update the source in frontmatter would require a script, so we add a note here.
tR += `\n\n> **Note:** Remember to update the \`source\` field in the YAML frontmatter to \`[${sourceTag}]\` after creation.`;
%>
## 7. Next Steps
- [ ] **Use** this prompt with the target AI system.
- [ ] **Analyze** the response for accuracy, relevance, and adherence to requirements.
- [ ] **Iterate** using the `Prompt Optimization Workflow` or `Debugging Template` if needed.
<% tp.file.cursor() %>
```

---
#### **2. Capture Template: `03-notes/prompt-engineering/prompt-chain-builder.md`**
```markdown
<%*
/*
    Templater Template: Prompt Chain Builder
    Purpose: To design and document a multi-step prompt workflow.
    Author: Generated by PromptGPT Templater Template Developer
    Instructions: Place this file in your Templater template folder.
    Next Steps: Implement the chain and test data handoff between phases.
*/
%>
---
type: prompt
maturity: seedling
confidence: provisional
status: active
priority: high
completion: 0
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/prompt
  - #status/seedling
  - #year/<% tp.date.now("YYYY") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
## 1. Workflow Goal
<%*
const workflowGoal = await tp.system.prompt("What is the overall goal of this multi-step prompt workflow?");
tR += workflowGoal;
%>
## 2. Phase-by-Phase Breakdown
<%*
const numPhases = parseInt(await tp.system.prompt("How many phases/steps are in this chain?", "3"));
for (let i = 1; i <= numPhases; i++) {
%>
### Phase <%= i %>
<%*
    const phaseName = await tp.system.prompt(`Name of Phase ${i}:`);
    const phasePrompt = await tp.system.prompt(`Prompt/Instruction for Phase ${i}:`);
    const phaseOutputDesc = await tp.system.prompt(`Description of expected output for Phase ${i}:`);
%>
- **Name:** <%= phaseName %>
- **Prompt/Instruction:**
    ```
    <%= phasePrompt %>
    ```
- **Expected Output:** <%= phaseOutputDesc %>
<% } %>
## 3. Data Handoff Specifications
<%*
for (let i = 1; i < numPhases; i++) {
%>
### Handoff from Phase <%= i %> to Phase <%= i+1 %>
<%*
    const handoffDesc = await tp.system.prompt(`Describe how data/output from Phase ${i} is passed to Phase ${i+1}:`);
%>
- **Description:** <%= handoffDesc %>
<% } %>
## 4. Validation Checkpoints
<%*
for (let i = 1; i <= numPhases; i++) {
%>
### Validation for Phase <%= i %>
<%*
    const validationCriteria = await tp.system.prompt(`Define validation criteria or checks for the output of Phase ${i} (e.g., 'Output must be valid JSON', 'Summary must be < 100 words'):`);
%>
- **Criteria:** <%= validationCriteria %>
<% } %>
## 5. Chain Visualization (Mermaid)
```mermaid
graph TD
<%*
for (let i = 1; i <= numPhases; i++) {
    const phaseName = (await tp.system.prompt(`Re-enter name for Phase ${i} for diagram (or press Enter to use 'Phase ${i}')`, `Phase ${i}`)).trim() || `Phase ${i}`;
    tR += `    P${i}[${phaseName}] --> `;
    if (i < numPhases) {
        tR += `\n`;
    }
}
// Remove the trailing arrow from the last node
tR = tR.trim();
if (tR.endsWith("-->")) {
    tR = tR.slice(0, -4);
}
%>
```
## 6. Next Steps
- [ ] **Implement** each phase as a separate prompt or script.
- [ ] **Test** the data handoff mechanisms.
- [ ] **Monitor** validation checkpoints during execution.
- [ ] **Iterate** on the chain design using `Prompt Optimization Workflow`.
<% tp.file.cursor(1) %>
```

---
#### **3. Capture Template: `03-notes/prompt-engineering/few-shot-example-template.md`**
```markdown
<%*
/*
    Templater Template: Few-Shot Example Template
    Purpose: To create structured input/output examples for few-shot prompting.
    Author: Generated by PromptGPT Templater Template Developer
    Instructions: Place this file in your Templater template folder.
    Next Steps: Copy the generated examples into your main prompt template.
*/
%>
---
type: reference
maturity: developing
confidence: moderate
status: active
priority: medium
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/reference
  - #status/developing
  - #year/<% tp.date.now("YYYY") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
## 1. Example Set Goal
<%*
const exampleGoal = await tp.system.prompt("What task or concept do these examples aim to teach the AI?");
tR += exampleGoal;
%>
## 2. Structured Examples
<%*
const exampleCount = parseInt(await tp.system.suggester([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], false, "How many examples to create?"));
for (let i = 1; i <= exampleCount; i++) {
%>
### Example #<%= i %>
<%*
    const exampleInput = await tp.system.prompt(`Input for Example ${i}:`);
    const exampleOutput = await tp.system.prompt(`Desired Output for Example ${i}:`);
    const exampleExplanation = await tp.system.prompt(`Explanation for Example ${i} (Why is this output correct?):`);
%>
- **Input:**
    ```
    <%= exampleInput %>
    ```
- **Desired Output:**
    ```
    <%= exampleOutput %>
    ```
- **Explanation:** <%= exampleExplanation %>
<% } %>
## 3. Diversity & Quality Check
### Diversity Guidelines Reminder
- Ensure examples cover a range of typical cases.
- Include edge cases if relevant to the task.
- Vary the structure and complexity of inputs slightly.
### Quality Checklist
- [ ] Each input is clear and unambiguous.
- [ ] Each output is a correct and high-quality response to its input.
- [ ] Explanations are concise and highlight the key reasoning.
- [ ] The set of examples, as a whole, effectively teaches the desired behavior.
## 4. Integration Note
To use these examples in a prompt, format them within an `<examples>...</examples>` block as shown in the `prompt-components.md` library.
<% tp.file.cursor() %>
```

---


---
### **Phase 3: Iteration Templates**
#### **1. Iteration Template: `03-notes/prompt-engineering/prompt-optimization-workflow.md`**
````markdown
<%*
/*
    Templater Template: Prompt Optimization Workflow
    Purpose: A structured template for refining and improving an existing prompt.
    Author: Generated by PromptGPT Templater Template Developer
    Instructions: Place this file in your Templater template folder. Use to document prompt improvements.
    Next Steps: Execute the test plan and document results to decide on acceptance.
*/
%>
---
type: prompt-report
maturity: seedling
confidence: provisional
status: active
priority: medium
completion: 0
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/prompt-report
  - #status/seedling
  - #year/<% tp.date.now("YYYY") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
## 1. Original Prompt
<%*
const originalPromptLink = await tp.system.prompt("Link to the original prompt note being optimized (e.g., [[my-original-system-prompt]]):");
tR += `Link: ${originalPromptLink}`;
%>
## 2. Problem Identification
*What is not working with the current prompt?*
<%*
const problemDesc = await tp.system.prompt("Describe the specific problem or failure mode:");
tR += `- ${problemDesc}`;
%>
## 3. Improvement Hypothesis
*What change(s) do you hypothesize will fix the problem?*
<%*
const hypothesis = await tp.system.prompt("State your hypothesis for improvement:");
tR += `- ${hypothesis}`;
%>
## 4. Modified Prompt Version
*The new version of the prompt incorporating the hypothesis.*
```prompt
<%*
const modifiedPrompt = await tp.system.prompt("Paste the full text of your modified prompt here:");
tR += modifiedPrompt;
%>
```
## 5. Test Plan
*How will you test if the modification worked?*
<%*
const numTestCases = parseInt(await tp.system.prompt("How many test cases will you run?", "3"));
for (let i = 1; i <= numTestCases; i++) {
%>
### Test Case #<%= i %>
<%*
    const testCaseInput = await tp.system.prompt(`Input for Test Case ${i}:`);
    const expectedOutput = await tp.system.prompt(`Expected Output for Test Case ${i}:`);
%>
- **Input:** `<%= testCaseInput %>`
- **Expected Output:** `<%= expectedOutput %>`
<% } %>
## 6. Results Comparison
*(To be filled after testing)*

| Test Case | Original Prompt Output | Modified Prompt Output | Pass/Fail? | Notes |
| :--- | :--- | :--- | :--- | :--- |
<%*
for (let i = 1; i <= numTestCases; i++) {
    tR += `| #${i} |  |  |  |  |\n`;
}
%>
## 7. Decision
*(To be filled after testing and analysis)*
- [ ] **Accept** the change (update the original prompt)
- [ ] **Reject** the change (revert to original or try a new hypothesis)
- [ ] **Further Iterate** (refine the modification and re-test)
## 8. Maturity Update
*(To be updated based on decision)*
- If Accepted: Update original prompt's `maturity` field.
- This report's `maturity`: <% tp.system.suggester(["seedling", "developing", "budding", "evergreen"], ["seedling", "developing", "budding", "evergreen"], false, "Set maturity for this report:") %>
<% tp.file.cursor(1) %>
````

---
#### **2. Iteration Template: `03-notes/prompt-engineering/ab-testing-framework.md`**
```markdown
<%*
/*
    Templater Template: A/B Testing Framework
    Purpose: To compare the performance of two prompt variants.
    Author: Generated by PromptGPT Templater Template Developer
    Instructions: Place this file in your Templater template folder.
    Next Steps: Execute the test plan and analyze results to choose a winner.
*/
%>
---
type: prompt-report
maturity: seedling
confidence: provisional
status: active
priority: medium
completion: 0
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/prompt-report
  - #status/seedling
  - #year/<% tp.date.now("YYYY") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
## 1. Test Objective
<%*
const testObjective = await tp.system.prompt("What is the goal of this A/B test (e.g., 'Compare accuracy of two summary prompts')?");
tR += testObjective;
%>
## 2. Prompt Variants
### Variant A (Control)
<%*
const variantALink = await tp.system.prompt("Link to Variant A prompt note (e.g., [[summary-prompt-v1]]):");
const variantADesc = await tp.system.prompt("Brief description of Variant A:");
%>
- **Link:** <%= variantALink %>
- **Description:** <%= variantADesc %>
### Variant B (Test)
<%*
const variantBLink = await tp.system.prompt("Link to Variant B prompt note (e.g., [[summary-prompt-v2]]):");
const variantBDesc = await tp.system.prompt("Brief description of Variant B:");
%>
- **Link:** <%= variantBLink %>
- **Description:** <%= variantBDesc %>
## 3. Testing Methodology
<%*
const methodology = await tp.system.prompt("Describe the testing methodology (e.g., 'Run 10 identical queries through both prompts and compare outputs for accuracy and relevance'):");
tR += methodology;
%>
## 4. Test Cases
<%*
const numTestCases = parseInt(await tp.system.prompt("How many test cases (queries) will you use?", "5"));
for (let i = 1; i <= numTestCases; i++) {
%>
### Test Case #<%= i %>
<%*
    const testCaseInput = await tp.system.prompt(`Input for Test Case ${i}:`);
%>
- **Input:** `<%= testCaseInput %>`
<% } %>
## 5. Results Matrix

| Test Case | Variant A Output | Variant B Output | Evaluator Notes (A vs B) | Winner |
| :--- | :--- | :--- | :--- | :--- |
<%*
for (let i = 1; i <= numTestCases; i++) {
    tR += `| #${i} |  |  |  |  |\n`;
}
%>
## 6. Evaluation Criteria & Scoring
*(Define how you will judge the outputs)*
<%*
const criteria = await tp.system.prompt("List your evaluation criteria (e.g., Accuracy, Conciseness, Relevance) separated by commas:");
const criteriaList = criteria.split(',').map(item => item.trim());
for (const criterion of criteriaList) {
    tR += `- **${criterion}** (Scale 1-10)\n`;
}
%>
*(Scoring can be added to the results matrix or done separately)*
## 7. Statistical Significance Notes
*(Optional, for more rigorous analysis)*
- Number of evaluators:
- Method for determining significance (e.g., p-value < 0.05):
## 8. Final Decision
- **Winner:** <% tp.system.suggester(["Variant A", "Variant B", "Tie/Inconclusive"], ["A", "B", "Tie"], false, "Which variant performed better?") %>
- **Rationale:**
    <%*
    const rationale = await tp.system.prompt("Explain the reasoning behind the decision:");
    tR += rationale;
    %>
## 9. Next Steps
- [ ] If B wins, integrate changes into the main prompt line.
- [ ] Update the winning prompt's metadata (e.g., increase `confidence`, update `maturity`).
- [ ] Archive the losing variant or use it for a future test.
<% tp.file.cursor(1) %>
```

---
#### **3. Iteration Template: `03-notes/prompt-engineering/debugging-template.md`**
```markdown
<%*
/*
    Templater Template: Debugging Template
    Purpose: To systematically diagnose and resolve prompt failures.
    Author: Generated by PromptGPT Templater Template Developer
    Instructions: Place this file in your Templater template folder.
    Next Steps: Implement the proposed fix and validate the resolution.
*/
%>
---
type: prompt-report
maturity: seedling
confidence: provisional
status: active
priority: high
completion: 0
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/prompt-report
  - #status/seedling
  - #year/<% tp.date.now("YYYY") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
## 1. Original Prompt
<%*
const originalPromptLink = await tp.system.prompt("Link to the problematic prompt note (e.g., [[failing-prompt-example]]):");
tR += `Link: ${originalPromptLink}`;
%>
## 2. Failure Mode Description
*What is the specific undesirable behavior?*
<%*
const failureMode = await tp.system.prompt("Describe the failure (e.g., 'AI ignores safety constraints', 'Output is consistently too verbose'):");
tR += `- ${failureMode}`;
%>
## 3. Reproduction Steps
*How can the failure be consistently reproduced?*
<%*
const numSteps = parseInt(await tp.system.prompt("Number of steps to reproduce:", "3"));
for (let i = 1; i <= numSteps; i++) {
%>
<%*
    const stepDesc = await tp.system.prompt(`Step ${i}:`);
    tR += `${i}. ${stepDesc}\n`;
}
%>
## 4. Hypothesis for Cause
*Why do you think this failure is occurring?*
<%*
const failureHypothesis = await tp.system.prompt("State your hypothesis for the root cause:");
tR += `- ${failureHypothesis}`;
%>
## 5. Proposed Fixes
*(List multiple potential solutions if applicable)*
<%*
const numFixes = parseInt(await tp.system.prompt("Number of potential fixes to consider:", "2"));
for (let i = 1; i <= numFixes; i++) {
%>
### Fix Option #<%= i %>
<%*
    const fixDesc = await tp.system.prompt(`Description of Fix #${i}:`);
    tR += `- ${fixDesc}\n`;
}
%>
## 6. Validation Approach
*How will you test if a fix resolves the issue?*
<%*
const validationPlan = await tp.system.prompt("Describe your plan to validate the fix (e.g., 'Run the reproduction steps again', 'Test with 5 new inputs'):");
tR += `- ${validationPlan}`;
%>
## 7. Resolution Documentation
*(To be filled after applying and testing the fix)*
### Chosen Fix
- Fix Option #: <% tp.system.prompt("Which fix option was implemented?") %>
### Validation Results
- **Test 1:** Pass/Fail - Notes
- **Test 2:** Pass/Fail - Notes
- **Overall Outcome:** <% tp.system.suggester(["Resolved", "Partially Resolved", "Not Resolved"], ["Resolved", "Partial", "Failed"], false, "Was the issue resolved?") %>
### Final Notes
<%*
const finalNotes = await tp.system.prompt("Any additional notes on the resolution process?");
tR += finalNotes;
%>
## 8. Update Original Prompt
- [ ] **Apply Fix** to the original prompt note.
- [ ] **Update Metadata** (e.g., `maturity`, `confidence`, `modified` date).
<% tp.file.cursor(1) %>
```

---
#### **4. Iteration Template: `03-notes/prompt-engineering/version-tracker.md`**
```markdown
<%*
/*
    Templater Template: Version Tracker
    Purpose: To log changes, history, and performance of a prompt over time.
    Author: Generated by PromptGPT Templater Template Developer
    Instructions: Place this file in your Templater template folder. Link from the main prompt note.
    Next Steps: Update this log with each significant change or test result.
*/
%>
---
type: permanent-note
maturity: developing
confidence: moderate
status: active
priority: low
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/permanent
  - #status/developing
  - #year/<% tp.date.now("YYYY") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %> (for [[<% tp.system.prompt("Link to main prompt note (e.g., [[my-key-prompt]])") %>]])
## 1. Version History

| Version | Date | Author | Changelog Summary | Performance Notes |
| :--- | :--- | :--- | :--- | :--- |
| v1.0.0 | <% tp.date.now("YYYY-MM-DD") %> | `<% tp.system.prompt("Your name or handle") %>` | Initial creation. | Baseline version. |
<%*
// This table is meant to be manually updated. Templater can add the initial row.
%>
## 2. Performance Metrics Over Versions
*(This section can be expanded with specific metrics tracked over time)*
### Metric: `<% tp.system.prompt("Name of a key performance metric (e.g., 'Accuracy %')") %>`
- *Data points and trends over versions can be logged here.*
## 3. Rollback Decision Criteria
Under what conditions would you consider reverting to an older version?
- <% tp.system.prompt("Define rollback criteria (e.g., 'If accuracy drops below 85% for 3 consecutive tests')") %>
## 4. Lessons Learned
*(A running log of insights gained during prompt development)*
- **v1.0.0:** Learned that initial version needed more specific constraints.
<% tp.file.cursor() %>
```

---
This concludes the generation of the Iteration Templates (Phase 3). I will now proceed with the Analysis Templates (Phase 4).

<thinking>
The user has responded with "continue". I have completed Phase 3 (Iteration Templates). The next step according to the plan is Phase 4: Analysis Templates.
I need to generate the following templates for Phase 4:
1.  `Test Results Documentation`
2.  `Comparative Prompt Analysis`
3.  `Effectiveness Report`
I will generate these one by one, ensuring they follow the specified structure, metadata, and Templater syntax.
</thinking>
Okay, I will now continue generating the templates, moving on to **Phase 4: Analysis Templates**.

---
### **Phase 4: Analysis Templates**
#### **1. Analysis Template: `03-notes/prompt-engineering/test-results-documentation.md`**
```markdown
<%*
/*
    Templater Template: Test Results Documentation
    Purpose: To formally document the results of a single prompt test run.
    Author: Generated by PromptGPT Templater Template Developer
    Instructions: Place this file in your Templater template folder. Create one per test run.
    Next Steps: Link this report to the prompt note and the relevant optimization/AB test report.
*/
%>
---
type: analysis
source: [] # To be filled with the LLM tested, e.g., [claude-sonnet-4.5]
maturity: seedling
confidence: provisional
status: active
priority: medium
completion: 100
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/analysis
  - #status/seedling
  - #year/<% tp.date.now("YYYY") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
## 1. Test Metadata
<%*
const promptLink = await tp.system.prompt("Link to the prompt tested (e.g., [[my-test-prompt]])");
const llmModel = await tp.system.suggester(
    ["Claude Sonnet 4.5", "Claude Opus 4.1", "Gemini Pro 3.0", "Gemini Flash 2.5", "Other (Specify)"],
    ["claude-sonnet-4.5", "claude-opus-4.1", "gemini-pro-3.0", "gemini-flash-2.5", "other"],
    false,
    "LLM Model Used:"
);
let finalModel = llmModel;
if (llmModel === "other") {
    finalModel = await tp.system.prompt("Specify the LLM model:");
}
const temperature = await tp.system.prompt("Temperature setting used (if applicable):", "0.7");
%>
- **Prompt Tested:** <%= promptLink %>
- **LLM Model:** <%= finalModel %>
- **Temperature:** <%= temperature %>
- **Test Date:** <% tp.date.now("YYYY-MM-DD") %>
- **Tester:** `<% tp.system.prompt("Your name or handle") %>`
## 2. Test Case Details
### 2.1. Input
<%*
const testCaseInput = await tp.system.prompt("Provide the specific input used for this test:");
%>
```
<%= testCaseInput %>
```
### 2.2. Expected Output
<%*
const expectedOutput = await tp.system.prompt("What was the expected or desired output?");
%>
```
<%= expectedOutput %>
```
### 2.3. Actual Output
*(Paste the AI's actual response here)*
```
<%*
const actualOutput = await tp.system.prompt("Paste the AI's actual output here:");
tR += actualOutput;
%>
```
## 3. Assessment
### 3.1. Success/Failure
- **Result:** <% tp.system.suggester(["Success", "Partial Success", "Failure"], ["Success", "Partial", "Failure"], false, "Overall result?") %>
### 3.2. Evaluation Notes
<%*
const evalNotes = await tp.system.prompt("Provide detailed notes on the assessment. What was good/bad? Where did it deviate from expected?");
tR += evalNotes;
%>
## 4. Performance Notes
### 4.1. Edge Case Observations
*(Did the prompt handle edge cases in the input well?)*
- <% tp.system.prompt("Note any observations about edge case handling (or 'N/A')") %>
### 4.2. Performance Metrics
*(If measured)*
- **Latency (approx secs):** <% tp.system.prompt("Observed response time (or 'N/A')", "N/A") %>
- **Tokens Used (Input/Output):** <% tp.system.prompt("Token count (or 'N/A')", "N/A") %>
## 5. Next Steps
- [ ] Link this report to the relevant prompt note.
- [ ] If part of a series, link to the parent `Prompt Optimization Workflow` or `A/B Testing Framework` report.
- [ ] If Failure, initiate a `Debugging Template` report.
<% tp.file.cursor() %>
```

---
#### **2. Analysis Template: `03-notes/prompt-engineering/comparative-prompt-analysis.md`**
```markdown
<%*
/*
    Templater Template: Comparative Prompt Analysis
    Purpose: To evaluate and compare multiple prompt versions or types side-by-side.
    Author: Generated by PromptGPT Templater Template Developer
    Instructions: Place this file in your Templater template folder.
    Next Steps: Use the analysis to make informed decisions about prompt selection or improvement.
*/
%>
---
type: analysis
maturity: seedling
confidence: provisional
status: active
priority: medium
completion: 0
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/analysis
  - #status/seedling
  - #year/<% tp.date.now("YYYY") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
## 1. Analysis Goal
<%*
const analysisGoal = await tp.system.prompt("What is the goal of this comparison (e.g., 'Compare system prompts for code summarization')?");
tR += analysisGoal;
%>
## 2. Prompts Compared
<%*
const numPrompts = parseInt(await tp.system.prompt("How many prompts are being compared?", "2"));
for (let i = 1; i <= numPrompts; i++) {
%>
### Prompt #<%= i %>
<%*
    const promptLink = await tp.system.prompt(`Link to Prompt #${i} note:`);
    const promptDesc = await tp.system.prompt(`Brief description of Prompt #${i}:`);
%>
- **Link:** <%= promptLink %>
- **Description:** <%= promptDesc %>
<% } %>
## 3. Evaluation Criteria Checklist
*(Rate each prompt on a 1-10 scale for each criterion)*

| Criterion | Description | Weight (1-5) |
| :--- | :--- | :--- |
| Accuracy | How factually correct is the output? | <% tp.system.prompt("Weight for Accuracy (1-5)", "5") %> |
| Consistency | Does it produce similar quality outputs for similar inputs? | <% tp.system.prompt("Weight for Consistency (1-5)", "4") %> |
| Clarity | Is the output easy to understand? | <% tp.system.prompt("Weight for Clarity (1-5)", "4") %> |
| Relevance | Does the output directly address the query? | <% tp.system.prompt("Weight for Relevance (1-5)", "5") %> |
| Creativity | Does it produce novel or insightful responses when appropriate? | <% tp.system.prompt("Weight for Creativity (1-5)", "3") %> |
| Safety | Does it adhere to constraints and avoid harmful output? | <% tp.system.prompt("Weight for Safety (1-5)", "5") %> |
*(Add or remove criteria as needed for your specific context)*
## 4. Comparison Table

| Prompt | Accuracy (1-10) | Consistency (1-10) | Clarity (1-10) | Relevance (1-10) | Creativity (1-10) | Safety (1-10) | Weighted Score | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
<%*
for (let i = 1; i <= numPrompts; i++) {
    tR += `| #${i} |  |  |  |  |  |  |  |  |\n`;
}
%>
*(Scores and notes to be filled manually or via a more complex script)*
## 5. Use Case Suitability Matrix
*(For different scenarios, which prompt performs best?)*

| Use Case | Best Prompt | Reason |
| :--- | :--- | :--- |
| General Task |  |  |
| High Accuracy Needed |  |  |
| Creative Task |  |  |
| Sensitive Topic |  |  |
*(Customize use cases as relevant)*
## 6. Recommendation Summary
<%*
const recommendation = await tp.system.prompt("Based on the analysis, which prompt is recommended and why?");
tR += recommendation;
%>
## 7. Next Steps
- [ ] Update the recommended prompt's metadata (e.g., increase `confidence`).
- [ ] Archive or iterate on non-recommended prompts.
- [ ] Share findings with team/stakeholders if applicable.
<% tp.file.cursor(1) %>
```

---
#### **3. Analysis Template: `03-notes/prompt-engineering/effectiveness-report.md`**
```markdown
<%*
/*
    Templater Template: Effectiveness Report
    Purpose: A detailed report on a prompt's performance in a real-world or simulated deployment.
    Author: Generated by PromptGPT Templater Template Developer
    Instructions: Place this file in your Templater template folder.
    Next Steps: Use this report to validate a prompt and update its maturity/confidence.
*/
%>
---
type: report
source: [] # To be filled with the LLM(s) used in deployment
maturity: <% tp.system.suggester(["budding", "evergreen"], ["budding", "evergreen"], false, "Set initial maturity based on pre-deployment testing:") %>
confidence: moderate
status: active
priority: high
completion: 100
link-up: [[prompt-engineering-moc]]
tags:
  - #prompt-engineering
  - #type/report
  - #status/active
  - #year/<% tp.date.now("YYYY") %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---
# <% tp.file.title %>
## 1. Prompt Identifier
<%*
const promptLink = await tp.system.prompt("Link to the prompt note being reported on (e.g., [[deployed-customer-support-prompt]])");
tR += `Link: ${promptLink}`;
%>
## 2. Deployment Context
<%*
const deploymentContext = await tp.system.prompt("Describe the context where the prompt was deployed (e.g., 'Customer support chatbot for billing inquiries'):");
tR += deploymentContext;
%>
## 3. Success Metrics Definition
*(What defines success for this prompt in this context?)*
<%*
const metricsDefinition = await tp.system.prompt("Define success metrics (e.g., 'Resolution rate > 80%', 'Average response time < 2 secs'):");
tR += `- ${metricsDefinition}`;
%>
## 4. Quantitative Results
### 4.1. Key Performance Indicators
*(Fill in actual data collected during deployment)*
- **Metric:** <% tp.system.prompt("Name of metric (e.g., Task Completion Rate)") %>  
    - **Target:** <% tp.system.prompt("Target value") %>
    - **Actual:** <% tp.system.prompt("Actual measured value") %>
    - **Variance:** <% tp.system.prompt("Difference from target") %>
- **Metric:** <% tp.system.prompt("Name of another metric (e.g., Accuracy %)") %>  
    - **Target:** <% tp.system.prompt("Target value") %>
    - **Actual:** <% tp.system.prompt("Actual measured value") %>
    - **Variance:** <% tp.system.prompt("Difference from target") %>
*(Add more KPIs as needed)*
### 4.2. Performance Stats (if applicable)
- **Total Interactions:** <% tp.system.prompt("Total number of times the prompt was used", "N/A") %>
- **Avg. Tokens/Input:** <% tp.system.prompt("Average input token count", "N/A") %>
- **Avg. Tokens/Output:** <% tp.system.prompt("Average output token count", "N/A") %>
- **Avg. Latency (secs):** <% tp.system.prompt("Average response time", "N/A") %>
## 5. Qualitative Assessment
<%*
const qualitativeAssessment = await tp.system.prompt("Provide a narrative assessment of the prompt's performance. What worked well? What were user feedback highlights?");
tR += qualitativeAssessment;
%>
## 6. Failure Pattern Analysis
*(If any issues were observed)*
- **Pattern 1:** <% tp.system.prompt("Describe a common failure mode or area for improvement (or 'None observed')") %>
- **Pattern 2:** <% tp.system.prompt("Describe another pattern (or 'N/A')") %>
## 7. Improvement Recommendations
<%*
const recommendations = await tp.system.prompt("Based on the results, what improvements are recommended for the prompt or its deployment?");
tR += `- ${recommendations}`;
%>
## 8. Final Status Update
### 8.1. Confidence & Maturity
Based on this report, how should the prompt's status be updated?
- **New Confidence Level:** <% tp.system.suggester(["speculative", "provisional", "moderate", "established", "high"], ["speculative", "provisional", "moderate", "established", "high"], false, "Set new confidence level:") %>
- **New Maturity Level:** <% tp.system.suggester(["seedling", "developing", "budding", "evergreen"], ["seedling", "developing", "budding", "evergreen"], false, "Set new maturity level:") %>
### 8.2. Archiving (if applicable)
- If this prompt is being superseded, link to the new version and update its `status` to `archived` or `deprecated`.
<% tp.file.cursor() %>
```

---
This concludes the generation of the Analysis Templates (Phase 4). I will now proceed with the Dashboard Template (Phase 5).