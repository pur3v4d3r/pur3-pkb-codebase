---
copilot-command-context-menu-enabled: true
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 10
copilot-command-model-key: ""
copilot-command-last-used: 0
---
Act as a meticulous knowledge management assistant. Your task is to generate a complete and consistent YAML frontmatter block for the note provided below.

Analyze the note's title and content to intelligently fill in the fields.

- For 'title', use the note's title.
- For 'aliases', suggest 2-3 logical alternative names or keywords based on the title.
- For 'tags', analyze the text and suggest 3-5 relevant, hierarchical tags (e.g., subject/topic/sub-topic).
- For 'status', default to 'seedling' as this is a new piece of frontmatter.
	- (with the emoji)
- For 'created', use the 'ctime' from the provided note_context.
- For 'updated', use the 'mtime' from the provided note_context.
- For 'source', insert a placeholder for me to fill in.
- For 'related', leave the field ready for me to add links.

Format the output as a clean YAML code block (`---`).

Note Title: {{note_title}}
Note Content:
{{note_content}}