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