<%*
// 1. Import the cleaning logic
const normalize = tp.user.clipboard_normalizer;
// 2. Safety Check: Ensure we have the script
if (!normalize) {
    new Notice("❌ Error: clipboard_normalizer.js not found!");
} else {
    // 3. Get the Active Editor (The note you are looking at)
    const view = app.workspace.getActiveViewOfType(tp.obsidian.MarkdownView);
    if (!view) {
        new Notice("⚠️ No active Markdown note found to paste into.");
    } else {
        const editor = view.editor;
        // 4. Define Options
        const modes = {
            "Standard (Typography + Markdown + URL Clean)": "standard",
            "Links Only (Strip Tracking Params)": "links_only",
            "Raw (Just Paste)": "raw"
        };
        // 5. Prompt User (Focus momentarily shifts to Suggester)
        const selectedLabel = await tp.system.suggester(
            Object.keys(modes),
            Object.keys(modes)
        );
        // 6. Execute and Paste
        if (selectedLabel) {
            const mode = modes[selectedLabel];
            // Run the cleaning script
            const cleanText = await normalize(tp, mode);
            // DIRECT INSERTION:
            // This replaces your selection (if any) or inserts at cursor.
            // It mimics standard OS paste behavior perfectly.
            editor.replaceSelection(cleanText);
        }
    }
}
%>