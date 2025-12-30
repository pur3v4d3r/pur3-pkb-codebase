```dataviewjs
// 🧠 SYSTEM: Semantic Bridge Engine
// PURPOSE: Find "Sibling" notes that share the same Outlinks (Contexts)
const current = dv.current();
const myOutlinks = current.file.outlinks.map(l => l.path);

// 1. Filter the Vault
const siblings = dv.pages()
    .where(p => p.file.path !== current.file.path) // Exclude self
    .where(p => !current.file.outlinks.map(l => l.path).includes(p.file.path)) // Exclude existing direct links
    .map(p => {
        // Find overlap between this page's links and the current page's links
        const shared = p.file.outlinks.filter(l => myOutlinks.includes(l.path));
        return { 
            link: p.file.link, 
            sharedCount: shared.length, 
            sharedLinks: shared 
        };
    })
    .where(p => p.sharedCount > 0) // Must share at least 1 connection
    .sort(p => p.sharedCount, "desc") // Sort by strongest connection
    .limit(5); // Only show top 5

// 2. Render the Bridge
if (siblings.length > 0) {
    dv.header(4, "🌉 Semantic Bridges (Missing Connections)");
    dv.table(
        ["Sibling Note", "Strength", "Shared Context"], 
        siblings.map(s => [
            s.link, 
            "🔗 " + s.sharedCount, 
            s.sharedLinks.slice(0, 3).join(", ") + (s.sharedCount > 3 ? "…" : "")
        ])
    );
} else {
    dv.paragraph("*No semantic siblings found. This note is unique in its connections.*");
}
```
