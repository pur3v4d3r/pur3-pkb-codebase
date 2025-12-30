/**
 * QuickAdd Macro: Component Search & Insert
 * Purpose: Find and embed library components at cursor
 * Location: 99-system/01-quickadd/01-scripts/component-search-insert.js
 * Version: 1.0.0
 * Created: 2025-12-20
 */

module.exports = async (params) => {
  const { app, quickAddApi } = params;

  // Get keyword for search
  const keyword = await quickAddApi.inputPrompt("Search components (keyword):");
  if (!keyword) {
    new Notice("❌ Cancelled: No keyword provided");
    return;
  }

  try {
    // Search for components in library
    const componentFolder = "02-projects/_spes-sequential-prompt-engineering-system/02-component-library";

    // Get all files in component library
    const allFiles = app.vault.getMarkdownFiles();
    const componentFiles = allFiles.filter(file =>
      file.path.startsWith(componentFolder) &&
      file.path.includes(keyword.toLowerCase())
    );

    if (componentFiles.length === 0) {
      new Notice(`❌ No components found matching "${keyword}"`, 5000);
      return;
    }

    // Create suggester options
    const displayNames = componentFiles.map(file => {
      // Extract component name from path
      const name = file.basename;
      // Try to get component type from path
      let type = "unknown";
      if (file.path.includes("/atomic/personas")) type = "Persona";
      else if (file.path.includes("/atomic/instructions")) type = "Instruction";
      else if (file.path.includes("/atomic/constraints")) type = "Constraint";
      else if (file.path.includes("/atomic/output-formats")) type = "Format";
      else if (file.path.includes("/atomic/context-framers")) type = "Context";
      else if (file.path.includes("/composite/")) type = "Composite";
      else if (file.path.includes("/specialized/")) type = "Specialized";

      return `[${type}] ${name}`;
    });

    // Let user select
    const selectedIndex = displayNames.indexOf(
      await quickAddApi.suggester(displayNames, displayNames)
    );

    if (selectedIndex === -1) {
      new Notice("❌ Cancelled: No component selected");
      return;
    }

    const selectedFile = componentFiles[selectedIndex];

    // Read component content
    const content = await app.vault.read(selectedFile);

    // Extract component text (between ```prompt blocks)
    const promptRegex = /```prompt\s*([\s\S]*?)```/;
    const match = content.match(promptRegex);

    let textToInsert;
    if (match && match[1]) {
      // Found prompt block, use it
      textToInsert = match[1].trim();
    } else {
      // No prompt block, offer full embed
      const useEmbed = await quickAddApi.yesNoPrompt(
        "No explicit prompt block found. Embed full component?",
        "Yes"
      );

      if (useEmbed) {
        textToInsert = `![[${selectedFile.basename}]]`;
      } else {
        new Notice("❌ Cancelled: No component text to insert");
        return;
      }
    }

    // Get active editor
    const activeView = app.workspace.getActiveViewOfType(require("obsidian").MarkdownView);
    if (!activeView) {
      new Notice("❌ No active editor found");
      return;
    }

    const editor = activeView.editor;

    // Insert at cursor
    const cursor = editor.getCursor();
    editor.replaceRange(textToInsert, cursor);

    // Update component usage count (async, don't wait)
    updateComponentUsage(app, selectedFile);

    // Success
    new Notice(`✅ Inserted: ${selectedFile.basename}`, 4000);

  } catch (error) {
    new Notice(`❌ Error: ${error.message}`, 8000);
    console.error("Component Search & Insert Error:", error);
  }
};

/**
 * Update component usage metadata (fire and forget)
 */
async function updateComponentUsage(app, componentFile) {
  try {
    const content = await app.vault.read(componentFile);

    // Parse frontmatter to get usage-count
    const frontmatterRegex = /^---\s*\n([\s\S]*?)\n---/;
    const match = content.match(frontmatterRegex);

    if (!match) return; // No frontmatter, skip

    const frontmatter = match[1];
    const usageRegex = /usage-count:\s*(\d+)/;
    const usageMatch = frontmatter.match(usageRegex);

    if (usageMatch) {
      const currentCount = parseInt(usageMatch[1], 10);
      const newCount = currentCount + 1;

      // Replace usage-count
      const newFrontmatter = frontmatter.replace(
        usageRegex,
        `usage-count: ${newCount}`
      );

      // Replace modified date
      const today = window.moment().format("YYYY-MM-DD");
      const modifiedRegex = /modified:\s*"[^"]*"/;
      const updatedFrontmatter = newFrontmatter.replace(
        modifiedRegex,
        `modified: "${today}"`
      );

      // Replace in full content
      const newContent = content.replace(frontmatterRegex, `---\n${updatedFrontmatter}\n---`);

      // Write back
      await app.vault.modify(componentFile, newContent);
    }
  } catch (error) {
    console.error("Failed to update component usage:", error);
    // Silent fail - don't interrupt user workflow
  }
}
