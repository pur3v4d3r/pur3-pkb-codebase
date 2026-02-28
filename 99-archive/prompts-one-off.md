# prompts-one-off






# Starter Prompt for the Prompt Repository synthesis Agent, designed to explore and analyze a repo pack package containing various files related to a specific field, and to create a master series of documents consolidating the best works on the topic.ic.


`````xml
<prompt>
<task>
<exploration_phase type="decomposition">
<thinking>
1. Review these files I'm uploading.
2. We need to design and build a prompt for thoroughly exploring a repo pack package that contains a variety of files related to a particular field.
3. The prompt should instruct the model to carefully analyze the folder structure and its file contents, then to employ high quality reasoning on how to best create a master series of documents that consolidate the best works on the topic.
4. We will do this by creating a detailed step-by-step plan for executing this task effectively.
   - Use file "task planning and decomposition as reference.
</thinking>
</exploration_phase>
<thinking>
<constraints>
  - The prompt should instruct the model to carefully analyze the folder structure and its contents, and then to employ in depth reasoning on how to best create a master series of documents that consolidate the best works on the topic.
    - The model will do this by creating a detailed step-by-step plan for executing this task effectively.
    - You must show the model how to do this by using file "task planning and decomposition as reference.
  - The prompt must guide the model to inspect the folder structure and its contents carefully, reason through how to create a comprehensive master series of documents that consolidate the best works on the topic.
  - The prompt must emphasize the importance of detail, reasoning, and thorough planning, and should instruct the model to outline each step in detail, provide additional suggestions for improving the quality of the final documents, and ensure that no steps are skipped.
  - The prompt must instruct the model to use any relevant files provided as primary knowledge for planning the creation of the master series of documents.
  - The prompt must also include constraints such as a minimum word count and the necessity of taking the task step by step without rushing.
  - The prompt must be structured to facilitate a clear understanding of the task and encourage comprehensive responses from the model.
  - You need to plan out how the model will handle the larger than normal file size, and ensure it can process all the relevant information effectively. 
    - Meaning the model may need to break down the files into smaller chunks or focus on specific sections at a time.
  - The prompt should specify the desired output format, such as a structured plan for the files uploaded on with clear headings and subheadings, to enhance readability and organization.
  - Finally, the prompt should outline an execution strategy for the model to follow, ensuring that it can effectively manage the task from start to finish while maintaining high-quality output.
  - The prompt should also include instructions for the model to provide additional suggestions that may help improve the quality of the final documents.
  - You will need to incorporate the XML thinking methodologies found in the uploaded file name: `prompt-report-claudes-advanced-tag-and-reasonings-v1-0-0.md` to ensure the model can reason through this task with the highest amount of reasoning possible.
</constraints>
<exploration_phase type="path-generation">
<thinking>
<context-of-files>
**Files being uploaded with this message**:
1. prompt-codebase-archaeologist-agent-v2-0-0.md -> This will be useful for extracting how the model can work through the large files.
2. task-planning-and-decomposition.md -> This will be useful for structuring the step by step plan.
3. clean-architecture-expert.md -> This will be useful for understanding how to structure the documents effectively.
4. python-data-scientist.md -> This will be useful for understanding how to analyze and extract relevant information from the files.
5. document generation-master-prompt.md -> This will be useful for understanding how to generate high-quality documents.
6. prompt-report-claudes-advanced-tag-and-reasonings-v1-0-0.md -> This is to be used for the included advanced reasoning techniques using XML Tag.
</context-of-files>
</thinking>
</exploration_phase>
<prompt>
`````














# Prompt for Comprehensive Brainstorm/Reasoning System v2.0.0



`````xml
<starter_prompt>
<goal>
A production ready newly revamped Brainstorming prompt, that has been optimized rigorously for performance and high quality Thinking and reasoning
</goal>
<thinking type="Analysis">
I need you to inspect the file that I am uploading with this chat message called: `brainstorm-codebase-pack.md`. 
**CAREFULLY** and with **SCRUTINY**,  you must inspect this codebase pack. **The goal**, is for you to *completely understand the way these systems work*, **inside and out**. So that, in turn, you can *create a new, updated version* that *implements all of our hard won prompt engineering best practices*. The new prompt **MUST** take full advantage of the core mechanisms from the `brainstorming-codebase-pack.md` because we know that it is a winner when it comes to *performance and ROI for prompting output*.
</thinking>
<thinking type="Decomposition">
- To achieve this, you will need to break down the existing prompt into its core components and functions. This will allow you to identify areas for improvement and optimization.
    - You **MUST** *fully plan out* the purposed prompt before starting any work on generation. 
        - It will need to be **meticulously mapped out before hand** so that the **cognitive scaffolding** and **architecture** can shine with its full force, allowing the LLM to fully reason during the "brainstorm"/inference.
        - This will involve creating a detailed outline of the prompt structure, including the various sections and their intended purposes.
        - You will also need to identify any potential bottlenecks or inefficiencies in the existing prompt that could be improved upon.
- **ALWAYS** use the `Exploration Phase` XML block to help you with this process.
- **ALWAYS** remember to **think step by step** and use **advanced reasoning frameworks** to help you with this process.
- **ALWAYS** remember to **strategically use the exemplar files** that are loaded into your Claude Project Knowledge to help you with this process.
- **ALWAYS** remember to **document your thought process** in the various `thinking` XML blocks.
    - This is for future reference so we can understand the true logic and reasoning behind this session. Don't worry about making it look pretty just make sure its clear and easy to follow.
</thinking>
<thinking type="Reconstruction">
Once you have a thorough understanding of the existing prompt, you will need to reconstruct it from the ground up. This will involve rethinking the structure, flow, and content of the prompt to ensure that it is fully optimized for performance and ROI.
</thinking>
<thinking type="Synthesis">
The final step will be to synthesize all of your insights and improvements into a new, cohesive prompt. This new prompt should be a significant upgrade over the original, incorporating all of the best practices and techniques that we have developed.
</thinking>
<thinking type="Implementation">
**!IMPORTANT**: You **MUST** use the *exemplars loaded into your Claude Project Knowledge*.
  - These are to help you implement the various advanced reasoning frameworks needed for this with masterful skill and precision.
    - These are individual files that have **clear semantic filenames** for you to *strategically use the exemplar that would provide the most performance increase*.
</thinking>
<thinking type="Finalization">
- Once the new prompt is complete, you will need to finalize it by testing and refining it to ensure that it meets our high standards for performance and ROI.
</thinking>
- **IMPORTANT**:
- **Make sure** you use the files marked `Gold standard` [there are x2] and  `YAML Master Reference`, in the final prompt.
<output>
- You must output a new prompt file called: `brainstorm-codebase-pack-v2.0.0.md`.
  - This new prompt file **MUST** be a *production ready prompt* that is *fully optimized* for *performance* and *ROI*.
  - The new prompt file **MUST** have a complete *YAML frontmatter* section for Obsidian, and also implement *YAML* in the prompt for various metadata, *while also* following the *comment blocks from the second* `Gold Standard Exemplar`
</output>
</starter_prompt>
`````