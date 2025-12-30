// Script: capture-thought-prompt.js
module.exports = async (params) => {
    const { quickAddApi: qa } = params;
    
    // Prompt for the core idea
    const thought = await qa.inputPrompt("What's the thought?");
    if (!thought) return; // User cancelled
    
    // Generate title from first 40 characters
    const title = thought.length > 40 
        ? thought.substring(0, 40).trim() + "..." 
        : thought;
    
    // Store for file name and content
    qa.variables["thought"] = thought;
    qa.variables["thoughtTitle"] = title;
    qa.variables["timestamp"] = qa.date.now("YYYY-MM-DD HH:mm:ss");
};