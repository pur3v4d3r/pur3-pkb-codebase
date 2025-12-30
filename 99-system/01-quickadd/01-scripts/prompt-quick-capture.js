/**
 * QuickAdd Macro: Prompt Quick Capture
 * Purpose: Minimal friction idea logging (<10 seconds)
 * Location: 99-system/01-quickadd/01-scripts/prompt-quick-capture.js
 * Version: 1.0.0
 * Created: 2025-12-20
 */

module.exports = async (params) => {
  const { app, quickAddApi } = params;

  // Input: Title
  const title = await quickAddApi.inputPrompt("Prompt title/idea:");
  if (!title) {
    new Notice("❌ Cancelled: No title provided");
    return;
  }

  // Input: Type
  const type = await quickAddApi.suggester(
    ["System Prompt", "User Prompt", "Component", "Chain/Workflow", "Other"],
    ["system", "user", "component", "chain", "other"]
  );
  if (!type) {
    new Notice("❌ Cancelled: No type selected");
    return;
  }

  // Input: Initial notes (optional)
  const notes = await quickAddApi.inputPrompt("Initial notes (optional):", "");

  // Generate unique ID
  const id = window.moment().format("YYYYMMDDHHmmss");

  // Generate filename (sanitize title)
  const sanitizedTitle = title
    .replace(/[\\/:*?"<>|]/g, "-")
    .replace(/\s+/g, "-")
    .toLowerCase();
  const fileName = `idea-${type}-${sanitizedTitle}-${id}.md`;

  // File path
  const folder = "00-inbox/prompt-ideas";
  const filePath = `${folder}/${fileName}`;

  // Create content
  const content = `---
type: "idea"
idea-type: "${type}"
id: "${id}"
status: "captured"
created: "${window.moment().format("YYYY-MM-DD")}"
tags:
  - "year/${window.moment().format("YYYY")}"
  - "prompt-engineering/idea"
  - "idea-type/${type}"
aliases:
  - "${title}"
link-up: "[[prompt-engineering-moc]]"
---

# ${title}

> [!idea] Quick Capture
> **Type**: ${type}
> **Captured**: ${window.moment().format("dddd, MMMM Do, YYYY")}

## 💡 Initial Notes

${notes || "*No notes yet - develop when ready*"}

## 🎯 Intended Use

<!-- What problem does this solve? -->

## 📋 Development Checklist

- [ ] Expand notes with full description
- [ ] Identify reusable components needed
- [ ] Create full prompt from template
- [ ] Test and iterate
- [ ] Document results
- [ ] Promote to production if successful

## 🔗 Related Ideas

<!-- Links to similar ideas or prompts -->

---

*Quick captured idea - Use "Develop Idea" macro to promote to full prompt template*
`;

  // Create file
  try {
    // Ensure folder exists
    const folderPath = folder;
    if (!(await app.vault.adapter.exists(folderPath))) {
      await app.vault.createFolder(folderPath);
    }

    // Create note
    await app.vault.create(filePath, content);

    // Success notification
    new Notice(`✅ Idea captured: ${fileName}`, 5000);

    // Open the new note (optional)
    const file = app.vault.getAbstractFileByPath(filePath);
    if (file) {
      await app.workspace.openLinkText(filePath, '', false);
    }
  } catch (error) {
    new Notice(`❌ Error creating idea: ${error.message}`, 8000);
    console.error("Prompt Quick Capture Error:", error);
  }
};
