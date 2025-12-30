// Script: literature-capture-metadata.js
module.exports = async (params) => {
    const { quickAddApi: qa } = params;
    
    // Source type selection
    const sourceType = await qa.suggester(
        ["📖 Book", "📄 Article", "🎥 Video", "🎙️ Podcast", "🌐 Web"],
        ["book", "article", "video", "podcast", "web"]
    );
    
    // Core metadata
    const title = await qa.inputPrompt("Title:");
    const author = await qa.inputPrompt("Author:");
    const url = await qa.inputPrompt("URL (optional):");
    
    // Generate short title for filename
    const titleShort = title.split(' ').slice(0, 3).join('-').toLowerCase();
    
    // Store all variables
    qa.variables["sourceType"] = sourceType;
    qa.variables["sourceTitle"] = title;
    qa.variables["author"] = author;
    qa.variables["url"] = url || "N/A";
    qa.variables["title-short"] = titleShort;
    
    // Prompt for first highlight
    const highlight = await qa.inputPrompt("Highlight/Quote:");
    qa.variables["firstHighlight"] = highlight;
};