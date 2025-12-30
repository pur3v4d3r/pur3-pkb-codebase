module.exports = async (params) => {
  const { quickAddApi: qa, app } = params;
  
  try {
    // Get all concept notes
    const conceptFiles = app.vault.getMarkdownFiles()
      .filter(f => {
        const cache = app.metadataCache.getFileCache(f);
        return cache?.frontmatter?.["concept-type"];
      });
    
    const conceptNames = conceptFiles.map(f => f.basename);
    
    // Let user select concept
    const selected = await qa.suggester(conceptNames, conceptFiles);
    
    if (!selected) return;
    
    // Get current file
    const activeFile = app.workspace.getActiveFile();
    if (!activeFile) {
      new Notice("No active file");
      return;
    }
    
    // Read frontmatter
    await app.fileManager.processFrontMatter(activeFile, (fm) => {
      if (!fm.concepts) fm.concepts = [];
      
      const link = `[[${selected.basename}]]`;
      if (!fm.concepts.includes(link)) {
        fm.concepts.push(link);
      }
    });
    
    new Notice(`Added concept: ${selected.basename}`);
    
  } catch (error) {
    new Notice("Error: " + error.message);
    console.error(error);
  }
};