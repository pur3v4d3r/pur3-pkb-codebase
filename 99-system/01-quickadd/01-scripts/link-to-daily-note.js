// Script: link-to-daily-note.js
module.exports = async (params) => {
    const { quickAddApi: qa, app } = params;
    
    const dailyNotePath = `01_daily-notes/${qa.date.now("YYYY-MM-DD")}_daily-note.md`;
    const capturedTitle = qa.variables["thoughtTitle"];
    const capturedLink = `- [[${qa.variables["fileName"]}|${capturedTitle}]]`;
    
    // Check if daily note exists
    const dailyNote = app.vault.getAbstractFileByPath(dailyNotePath);
    
    if (dailyNote) {
        // Append to "Captured Thoughts" section
        let content = await app.vault.read(dailyNote);
        
        // Find or create section
        if (content.includes("## 📥 Captured Thoughts")) {
            content = content.replace(
                "## 📥 Captured Thoughts",
                `## 📥 Captured Thoughts\n${capturedLink}`
            );
        } else {
            content += `\n\n## 📥 Captured Thoughts\n${capturedLink}`;
        }
        
        await app.vault.modify(dailyNote, content);
    }
};