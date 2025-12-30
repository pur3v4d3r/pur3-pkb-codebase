

## 🚀 Synthesis: The "Categorical Glossary" Upgrade

To fully harmonize these two files, you need a bridge script. The input file uses prefixes (`Principle-`, `Process-`, `Pitfall-`), but the output file ignores them.

Below is the **missing link**: a [[DataviewJS]] script that detects the prefixes defined in File 1 and groups the output by **Field Type** instead of just A-Z.

### 🛠️ Proposed Solution: The "Taxonomy Engine"

```dataviewj
// CONFIGURATION
const folderPath = dv.current().file.folder; // Or specific path
const pages = dv.pages(`"${folderPath}"`);

// DEFINE TAXONOMY MAPPING (Based on File 1)
const taxonomy = {
    "Principle": "⚖️ Principles & Laws",
    "Definition": "📖 Definitions",
    "Term": "📖 Definitions",
    "Distinction": "🆚 Distinctions",
    "X-vs-Y": "🆚 Distinctions",
    "Claim": "🧪 Empirical Claims",
    "Finding": "🧪 Empirical Claims",
    "Framework": "🏗️ Frameworks & Models",
    "Model": "🏗️ Frameworks & Models",
    "Pitfall": "⚠️ Cautions & Pitfalls",
    "Caution": "⚠️ Cautions & Pitfalls",
    "Process": "⚙️ Processes",
    "Insight": "💡 Key Insights",
    "Example": "🧩 Examples"
};

let allItems = [];

// REGEX: Captures [**Key**:: Value]
// Adapted to be robust for the bolding syntax
const regex = /\[\*\*([^*]+)\*\*::\s*([^\]]+)\]/g;

for (let page of pages) {
    const content = await dv.io.load(page.file.path);
    let match;
    while ((match = regex.exec(content)) !== null) {
        let rawKey = match[1].trim();
        let value = match[2].trim();

        // DETERMINE CATEGORY
        // Logic: Check if key starts with "Principle-", "Process-", etc.
        let category = "📂 General Metadata";
        let cleanKey = rawKey;

        // Check for specific prefixes defined in File 1
        for (let [prefix, label] of Object.entries(taxonomy)) {
            if (rawKey.startsWith(prefix)) {
                category = label;
                // Optional: Remove the prefix for cleaner display?
                // cleanKey = rawKey.replace(prefix + "-", "");
                break;
            }
        }

        allItems.push({
            category: category,
            key: cleanKey,
            value: value,
            link: page.file.link
        });
    }
}

// GROUP AND RENDER
let groups = dv.array(allItems).groupBy(x => x.category);

for (let group of groups) {
    dv.header(3, group.key);
    dv.table(
        ["Concept", "Content", "Source"],
        group.rows.map(k => [`**${k.key}**`, k.value, k.link])
    );
}

```

> [!what-this-does]
> This script bridges your two files. It reads the specific syntax from **File 1**, detects the semantic prefixes (like `Principle-`), and uses the robust regex extraction from **File 2** to display them in a categorized dashboard rather than a simple A-Z list.

## 🔗 Related Topics for PKB Expansion

1. **[[Ontology Engineering]]**
* *Connection:* The Field Type Matrix in File 1 is essentially a lightweight ontology.
* *Depth Potential:* Defining formal relationships between these types (e.g., a *Principle* justifies a *Process*).
* *Knowledge Graph Role:* Elevates the vault from a wiki to a semantic database.

2. **[[Incremental Formalization]]**
* *Connection:* The workflow implies moving from rough notes to strict `Key:: Value` pairs.
* *Depth Potential:* Methodologies for knowing *when* to upgrade text to metadata (the "Density" guidelines touch on this).
* *Knowledge Graph Role:* Process optimization for the PKB lifecycle.

3. **[[Dashboard Design Principles]]**
* *Connection:* File 2 focuses on displaying data. Good dashboard design ensures this data leads to insight.
* *Depth Potential:* Designing specific "View" notes (e.g., a "Principles Dashboard" or "Glossary View") using the scripts.
* *Knowledge Graph Role:* The interface layer between the user and the raw data.

4. **[[Natural Language Processing (NLP)]]**
* *Connection:* You are manually tagging concepts. NLP tools can suggest these tags automatically.
* *Depth Potential:* Using LLMs to scan notes and suggest `[**Key**:: Value]` insertions based on the File 1 taxonomy.
* *Knowledge Graph Role:* Automation of the input protocol.
```dataviewjs
// 🗺️ TAXONOMY BROWSER: Folder Explorer
// Purpose: Browse structured metadata from files in THIS folder only

// 1. SEMANTIC TAXONOMY MAP (Prefix → Display Category)
const taxonomy = {
 "Principle": "⚖️ Principles & Laws",
 "Definition": "📖 Definitions",
 "Term": "📖 Definitions",
 "Distinction": "🆚 Distinctions",
 "Claim": "🧪 Empirical Claims",
 "Finding": "🧪 Empirical Claims",
 "Framework": "🏗️ Frameworks & Models",
 "Model": "🏗️ Frameworks & Models",
 "Pitfall": "⚠️ Cautions & Pitfalls",
 "Process": "⚙️ Processes & Methods",
 "Insight": "💡 Key Insights",
 "Example": "🧩 Examples"
};

// 2. REGEX TO CAPTURE ALL INLINE FIELDS
const globalRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+(?:\][^\]]*)*)\]/g;

// 3. HELPER: CLEAN DISPLAY NAME
function cleanKeyName(rawKey, prefix) {
 let cleaned = rawKey.replace(prefix, "");
 if (cleaned.startsWith("-") || cleaned.startsWith("_")) {
  cleaned = cleaned.substring(1);
 }
 return cleaned.replace(/-/g, " ").trim();
}

// 4. HELPER: TRUNCATE TEXT WITH ELLIPSIS
function truncateText(text, maxLength = 100) {
 if (text.length <= maxLength) return text;
 return text.substring(0, maxLength) + "...";
}

// 5. EXTRACT METADATA FROM CURRENT FOLDER ONLY
let allMetadata = [];
const currentFile = dv.current();
const currentFolderPath = currentFile.file.folder;

// Get all pages in the current folder only
const pages = dv.pages().where(p => p.file.folder === currentFolderPath);

// Process each file in the folder
for (let page of pages) {
 try {
  const content = await dv.io.load(page.file.path);
  let match;
   
  globalRegex.lastIndex = 0; // Reset regex index
  while ((match = globalRegex.exec(content)) !== null) {
   let rawKey = match[1].trim();
   let value = match[2].trim();
   let category = "📂 General Metadata";
   let displayKey = rawKey;

   for (let [prefix, label] of Object.entries(taxonomy)) {
    if (rawKey.startsWith(prefix)) {
     category = label;
     displayKey = cleanKeyName(rawKey, prefix);
     break;
    }
   }

   allMetadata.push({
    cat: category,
    key: displayKey,
    val: value,
    source: page.file.link
   });
  }
 } catch (e) {
  console.warn(`Failed to load ${page.file.path}:`, e.message);
 }
}

// 6. GROUP BY CATEGORY AND RENDER INTERACTIVE OUTPUT
if (allMetadata.length > 0) {
 dv.header(3, "🧭 Folder Taxonomy Browser");

 let groups = dv.array(allMetadata).groupBy(x => x.cat);

 for (let group of groups.sort(g => g.key)) {
  dv.paragraph(`🔽 **${group.key}** (${group.rows.length} items)`);

  let subGroups = group.rows.groupBy(x => x.key);

  for (let sub of subGroups.sort(s => s.key)) {
   // Create collapsible section for each sub-group
   const details = dv.el("details", "");
   const summary = details.createEl("summary", { text: `📘 ${sub.key} (${sub.rows.length})` });
    
   // Create table that will be visible only when expanded
   const table = details.createEl("table");
   const thead = table.createEl("thead");
   const headerRow = thead.createEl("tr");
   headerRow.createEl("th", { text: "Source" });
   headerRow.createEl("th", { text: "Value" });
    
   const tbody = table.createEl("tbody");
   for (let row of sub.rows) {
    const tr = tbody.createEl("tr");
    tr.createEl("td", { text: row.source.toString() });
    
    // Show truncated preview in the summary if content is long
    if (row.val.length > 150 && sub.rows.length === 1) {
     summary.textContent += `: ${truncateText(row.val, 80)}`;
    }
    
    // Full content shown in table (only visible when expanded)
    const td = tr.createEl("td");
    td.createEl("div", { text: row.val });
   }
  }
 }
} else {
 dv.paragraph("> 📭 No structured metadata found in this folder.");
}
```

```dataviewjs
// 🗺️ TAXONOMY BROWSER: Folder Explorer
// Purpose: Browse structured metadata from files in THIS folder only

// 1. SEMANTIC TAXONOMY MAP (Prefix → Display Category)
const taxonomy = {
 "Principle": "⚖️ Principles & Laws",
 "Definition": "📖 Definitions",
 "Term": "📖 Definitions",
 "Distinction": "🆚 Distinctions",
 "Claim": "🧪 Empirical Claims",
 "Finding": "🧪 Empirical Claims",
 "Framework": "🏗️ Frameworks & Models",
 "Model": "🏗️ Frameworks & Models",
 "Pitfall": "⚠️ Cautions & Pitfalls",
 "Process": "⚙️ Processes & Methods",
 "Insight": "💡 Key Insights",
 "Example": "🧩 Examples"
};

// 2. REGEX TO CAPTURE ALL INLINE FIELDS
const globalRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+(?:\][^\]]*)*)\]/g;

// 3. HELPER: CLEAN DISPLAY NAME
function cleanKeyName(rawKey, prefix) {
 let cleaned = rawKey.replace(prefix, "");
 if (cleaned.startsWith("-") || cleaned.startsWith("_")) {
  cleaned = cleaned.substring(1);
 }
 return cleaned.replace(/-/g, " ").trim();
}

// 4. HELPER: TRUNCATE TEXT WITH ELLIPSIS
function truncateText(text, maxLength = 100) {
 if (text.length <= maxLength) return text;
 return text.substring(0, maxLength) + "...";
}

// 5. EXTRACT METADATA FROM CURRENT FOLDER ONLY
let allMetadata = [];
const currentFile = dv.current();
const currentFolderPath = currentFile.file.folder;

// Get all pages in the current folder only
const pages = dv.pages().where(p => p.file.folder === currentFolderPath);

// Process each file in the folder
for (let page of pages) {
 try {
  const content = await dv.io.load(page.file.path);
  let match;
   
  globalRegex.lastIndex = 0; // Reset regex index
  while ((match = globalRegex.exec(content)) !== null) {
   let rawKey = match[1].trim();
   let value = match[2].trim();
   let category = "📂 General Metadata";
   let displayKey = rawKey;

   for (let [prefix, label] of Object.entries(taxonomy)) {
    if (rawKey.startsWith(prefix)) {
     category = label;
     displayKey = cleanKeyName(rawKey, prefix);
     break;
    }
   }

   allMetadata.push({
    cat: category,
    key: displayKey,
    val: value,
    source: page.file.link
   });
  }
 } catch (e) {
  console.warn(`Failed to load ${page.file.path}:`, e.message);
 }
}

// 6. GROUP BY CATEGORY AND RENDER INTERACTIVE OUTPUT
if (allMetadata.length > 0) {
 dv.header(3, "🧭 Folder Taxonomy Browser");

 let groups = dv.array(allMetadata).groupBy(x => x.cat);

 for (let group of groups.sort(g => g.key)) {
  dv.paragraph(`🔽 **${group.key}** (${group.rows.length} items)`);

  let subGroups = group.rows.groupBy(x => x.key);

  for (let sub of subGroups.sort(s => s.key)) {
   // Create collapsible section using dv.el
   const details = dv.el("details", "");
   const summary = details.createEl("summary", { text: `📘 ${sub.key}` });
    
   // Create table for the items in this collapsible section
   const table = details.createEl("table");
   const thead = table.createEl("thead");
   const headerRow = thead.createEl("tr");
   headerRow.createEl("th", { text: "Source" });
   headerRow.createEl("th", { text: "Value" });
    
   const tbody = table.createEl("tbody");
   for (let row of sub.rows) {
    const tr = tbody.createEl("tr");
    tr.createEl("td", { text: row.source.toString() });
    
    // Show truncated preview, full content will be visible when expanded
    const td = tr.createEl("td");
    const preview = truncateText(row.val, 150);
    td.createEl("div", { text: preview });
    
    // If content is long, show "click to expand" indicator
    if (row.val.length > 150) {
     td.createEl("div", { 
      text: "📋 (Click to expand for full content)", 
      attr: { style: "font-size: 0.8em; color: #666; margin-top: 5px;" } 
     });
    }
   }
  }
 }
} else {
 dv.paragraph("> 📭 No structured metadata found in this folder.");
}
```

```dataviewjs
// 🌐 CONCEPT RELATIONSHIP MAPPER
// Purpose: Map semantic relationships between concepts in your PKB
// Output: Text-based relationship visualization and data export

// 1. SEMANTIC TAXONOMY MAP
const taxonomy = {
  "Principle": "⚖️ Principles & Laws",
  "Definition": "📖 Definitions",
  "Term": "📖 Definitions",
  "Distinction": "🆚 Distinctions",
  "Claim": "🧪 Empirical Claims",
  "Finding": "🧪 Empirical Claims",
  "Framework": "🏗️ Frameworks & Models",
  "Model": "🏗️ Frameworks & Models",
  "Pitfall": "⚠️ Cautions & Pitfalls",
  "Process": "⚙️ Processes & Methods",
  "Insight": "💡 Key Insights",
  "Example": "🧩 Examples"
};

// 2. REGEX FOR EXTRACTION
const globalRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+(?:\][^\]]*)*)\]/g;

// 3. HELPER: CLEAN DISPLAY NAME
function cleanKeyName(rawKey, prefix) {
  let cleaned = rawKey.replace(prefix, "");
  if (cleaned.startsWith("-") || cleaned.startsWith("_")) cleaned = cleaned.substring(1);
  return cleaned.replace(/-/g, " ").trim();
}

// 4. EXTRACT ALL CONCEPTS AND RELATIONSHIPS
let conceptRegistry = new Map(); // concept -> {category, sources[], related: Map(concept -> count)}
const pages = dv.pages();

for (let page of pages) {
  const content = await dv.io.load(page.file.path);
  let pageConcepts = [];
  let match;
  
  // Extract all concepts from this page
  while ((match = globalRegex.exec(content)) !== null) {
    let rawKey = match[1].trim();
    let value = match[2].trim();
    
    let category = "📂 General Metadata";
    let displayKey = rawKey;
    
    for (let [prefix, label] of Object.entries(taxonomy)) {
      if (rawKey.startsWith(prefix)) {
        category = label;
        displayKey = cleanKeyName(rawKey, prefix);
        break;
      }
    }
    
    pageConcepts.push({
      name: displayKey,
      rawKey: rawKey,
      category: category,
      source: page.file.name,
      link: page.file.link
    });
    
    // Register concept
    if (!conceptRegistry.has(displayKey)) {
      conceptRegistry.set(displayKey, {
        name: displayKey,
        category: category,
        sources: [],
        related: new Map()
      });
    }
    
    let conceptObj = conceptRegistry.get(displayKey);
    if (!conceptObj.sources.some(s => s.name === page.file.name)) {
      conceptObj.sources.push({
        name: page.file.name,
        link: page.file.link
      });
    }
  }
  
  // Create relationships (co-occurrence in same note)
  for (let i = 0; i < pageConcepts.length; i++) {
    for (let j = i + 1; j < pageConcepts.length; j++) {
      let conceptA = pageConcepts[i].name;
      let conceptB = pageConcepts[j].name;
      
      if (conceptA !== conceptB) {
        let conceptObjA = conceptRegistry.get(conceptA);
        let conceptObjB = conceptRegistry.get(conceptB);
        
        // Add bidirectional relationships
        if (!conceptObjA.related.has(conceptB)) {
          conceptObjA.related.set(conceptB, 0);
        }
        conceptObjA.related.set(conceptB, conceptObjA.related.get(conceptB) + 1);
        
        if (!conceptObjB.related.has(conceptA)) {
          conceptObjB.related.set(conceptA, 0);
        }
        conceptObjB.related.set(conceptA, conceptObjB.related.get(conceptA) + 1);
      }
    }
  }
}

// 5. RENDER CONCEPT NETWORK ANALYSIS
if (conceptRegistry.size > 0) {
  dv.header(3, "🌐 Concept Relationship Analysis");
  
  // Summary statistics
  dv.paragraph(`**📊 Network Summary:**`);
  dv.paragraph(`- Total Concepts: ${conceptRegistry.size}`);
  dv.paragraph(`- Total Concept Relationships: ${Array.from(conceptRegistry.values()).reduce((sum, c) => sum + c.related.size, 0)}`);
  
  // Most connected concepts
  let sortedByConnections = Array.from(conceptRegistry.entries())
    .sort((a, b) => b[1].related.size - a[1].related.size)
    .slice(0, 10);
  
  dv.paragraph(`**🔗 Most Connected Concepts:**`);
  dv.list(sortedByConnections.map(([name, concept]) => 
    `**${name}** (${concept.category}) - ${concept.related.size} connections`
  ));
  
  // Concepts by category
  dv.header(4, "🏷️ Concepts by Category");
  let categoryGroups = Array.from(conceptRegistry.values()).reduce((acc, concept) => {
    if (!acc[concept.category]) acc[concept.category] = [];
    acc[concept.category].push(concept);
    return acc;
  }, {});
  
  for (let [category, concepts] of Object.entries(categoryGroups)) {
    dv.paragraph(`**${category}** (${concepts.length} concepts)`);
    dv.list(concepts.map(c => c.name));
  }
  
  // Detailed relationship map for top concepts
  dv.header(4, "🕸️ Detailed Relationship Map (Top 5 Most Connected)");
  
  for (let [name, concept] of sortedByConnections.slice(0, 5)) {
    dv.paragraph(`**${name}** (${concept.category})`);
    
    // Show sources
    dv.paragraph(`_Found in: ${concept.sources.map(s => s.link).join(", ")}_`);
    
    // Show relationships
    if (concept.related.size > 0) {
      let sortedRelated = Array.from(concept.related.entries())
        .sort((a, b) => b[1] - a[1])
        .slice(0, 8);
      
      dv.table(
        ["Related Concept", "Connection Strength", "Related Category"],
        sortedRelated.map(([relatedName, strength]) => {
          let relatedConcept = conceptRegistry.get(relatedName);
          return [
            relatedName,
            "🔗".repeat(strength), // Visual strength indicator
            relatedConcept ? relatedConcept.category : "Unknown"
          ];
        })
      );
    }
    dv.paragraph("---");
  }
  
  // Data export preparation
  dv.header(4, "💾 Data Export Ready");
  dv.paragraph("> The relationship data is structured and ready for export to visualization tools.");
  
  // Prepare export data (hidden by default)
  const exportData = {
    nodes: Array.from(conceptRegistry.entries()).map(([name, concept]) => ({
      id: name,
      label: name,
      category: concept.category,
      sourceCount: concept.sources.length
    })),
    edges: Array.from(conceptRegistry.entries()).flatMap(([sourceName, concept]) => 
      Array.from(concept.related.entries()).map(([targetName, weight]) => ({
        from: sourceName,
        to: targetName,
        weight: weight
      }))
    )
  };
  
  // This would be the JSON for external tools
  dv.paragraph(`_Export format prepared for tools like Gephi, Cytoscape, or custom D3 visualizations._`);
  
} else {
  dv.paragraph("> 📭 No structured concepts found for relationship mapping.");
}
```

```dataviewjs
// 📊 CHARTS.JS CONFIGURATION GENERATOR
// Purpose: Generate ready-to-use Charts.js configurations for your semantic knowledge
// Output: Complete chart configs for immediate use

// 1. SEMANTIC TAXONOMY MAP
const taxonomy = {
  "Principle": "⚖️ Principles & Laws",
  "Definition": "📖 Definitions",
  "Term": "📖 Definitions",
  "Distinction": "🆚 Distinctions",
  "Claim": "🧪 Empirical Claims",
  "Finding": "🧪 Empirical Claims",
  "Framework": "🏗️ Frameworks & Models",
  "Model": "🏗️ Frameworks & Models",
  "Pitfall": "⚠️ Cautions & Pitfalls",
  "Process": "⚙️ Processes & Methods",
  "Insight": "💡 Key Insights",
  "Example": "🧩 Examples"
};

// 2. REGEX FOR EXTRACTION
const globalRegex = /\[\*\*([^*]+)\*\*::\s*([^\]]+(?:\][^\]]*)*)\]/g;

// 3. HELPER: CLEAN DISPLAY NAME
function cleanKeyName(rawKey, prefix) {
  let cleaned = rawKey.replace(prefix, "");
  if (cleaned.startsWith("-") || cleaned.startsWith("_")) cleaned = cleaned.substring(1);
  return cleaned.replace(/-/g, " ").trim();
}

// 4. EXTRACT ALL CONCEPTS
let conceptRegistry = new Map();
const pages = dv.pages();

dv.paragraph("> 📡 Processing knowledge base...");

for (let page of pages) {
  try {
    const content = await dv.io.load(page.file.path);
    let match;

    // Extract all concepts
    while ((match = globalRegex.exec(content)) !== null) {
      let rawKey = match[1].trim();
      let value = match[2].trim();

      let category = "📂 General Metadata";
      let displayKey = rawKey;

      for (let [prefix, label] of Object.entries(taxonomy)) {
        if (rawKey.startsWith(prefix)) {
          category = label;
          displayKey = cleanKeyName(rawKey, prefix);
          break;
        }
      }

      // Register concept
      if (!conceptRegistry.has(displayKey)) {
        conceptRegistry.set(displayKey, {
          name: displayKey,
          category: category,
          sourceCount: 0,
          sources: new Set()
        });
      }

      let conceptObj = conceptRegistry.get(displayKey);
      const sourceName = page.file?.link?.text || page.file?.name || "Unknown Source";

      // Only increment if this file hasn't contributed yet
      if (!conceptObj.sources.has(sourceName)) {
        conceptObj.sourceCount++;
      }
      conceptObj.sources.add(sourceName);
    }
  } catch (e) {
    continue;
  }
}

// 5. GENERATE CHARTS.JS CONFIGURATIONS
if (conceptRegistry.size > 0) {
  dv.header(3, "📊 Ready-to-Use Charts.js Configurations");

  // === CATEGORY DISTRIBUTION CHART ===
  dv.header(4, "1. Category Distribution");

  const categoryCounts = {};
  for (let [name, concept] of conceptRegistry) {
    categoryCounts[concept.category] = (categoryCounts[concept.category] || 0) + 1;
  }

  const categoryChartConfig = {
    type: 'doughnut',
    data: {
      labels: Object.keys(categoryCounts),
      datasets: [{
        label: 'Concepts by Category',
        data: Object.values(categoryCounts),
        backgroundColor: [
          '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4',
          '#FFEAA7', '#DDA0DD', '#98D8C8', '#F7DC6F',
          '#BB8FCE', '#D5D8DC'
        ],
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Knowledge Base by Semantic Category'
        },
        legend: {
          position: 'bottom'
        }
      }
    }
  };

  dv.paragraph("**Category Distribution Chart:**");
  dv.paragraph("```json\n" + JSON.stringify(categoryChartConfig, null, 2) + "\n```");

  // === TOP CONCEPTS BY SOURCE COUNT ===
  dv.header(4, "2. Most Referenced Concepts");

  const topConcepts = Array.from(conceptRegistry.entries())
    .sort((a, b) => b[1].sourceCount - a[1].sourceCount)
    .slice(0, 10);

  const topConceptsChartConfig = {
    type: 'bar',
    data: {
      labels: topConcepts.map(([name]) => name),
      datasets: [{
        label: 'Number of References',
        data: topConcepts.map(([, concept]) => concept.sourceCount),
        backgroundColor: 'rgba(54, 162, 235, 0.7)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Top 10 Most Referenced Concepts'
        }
      },
      scales: {
        x: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Number of References'
          }
        }
      }
    }
  };

  dv.paragraph("**Top Concepts Chart:**");
  dv.paragraph("```json\n" + JSON.stringify(topConceptsChartConfig, null, 2) + "\n```");

  // === CATEGORY SIZE COMPARISON ===
  dv.header(4, "3. Category Size Comparison");

  const sortedCategories = Object.entries(categoryCounts)
    .sort((a, b) => b[1] - a[1]);

  const categorySizeChartConfig = {
    type: 'polarArea',
    data: {
      labels: sortedCategories.map(([category]) => category),
      datasets: [{
        label: 'Concepts per Category',
        data: sortedCategories.map(([, count]) => count),
        backgroundColor: [
          'rgba(255, 99, 132, 0.7)',
          'rgba(54, 162, 235, 0.7)',
          'rgba(255, 205, 86, 0.7)',
          'rgba(75, 192, 192, 0.7)',
          'rgba(153, 102, 255, 0.7)',
          'rgba(255, 159, 64, 0.7)',
          'rgba(199, 199, 199, 0.7)',
          'rgba(83, 175, 100, 0.7)',
          'rgba(255, 99, 240, 0.7)',
          'rgba(0, 128, 128, 0.7)'
        ]
      }]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Concept Distribution by Category'
        }
      }
    }
  };

  dv.paragraph("**Category Size Chart:**");
  dv.paragraph("```json\n" + JSON.stringify(categorySizeChartConfig, null, 2) + "\n```");

  // === SUMMARY DATA ===
  dv.header(4, "4. Knowledge Base Summary");

  const summaryData = {
    totalConcepts: conceptRegistry.size,
    totalCategories: Object.keys(categoryCounts).length,
    avgReferences: (Array.from(conceptRegistry.values())
      .reduce((sum, c) => sum + c.sourceCount, 0) / conceptRegistry.size).toFixed(1),
    largestCategory: sortedCategories[0] ? sortedCategories[0][0] : "None"
  };

  const summaryChartConfig = {
    type: 'radar',
    data: {
      labels: ['Total Concepts', 'Categories', 'Avg References', 'Diversity'],
      datasets: [{
        label: 'Knowledge Base Metrics',
        data: [
          Math.min(summaryData.totalConcepts / 2, 100),
          Math.min(summaryData.totalCategories * 10, 100),
          Math.min(summaryData.avgReferences * 5, 100),
          (summaryData.totalCategories / Math.max(summaryData.totalConcepts, 1)) * 100
        ],
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        pointBackgroundColor: 'rgba(255, 99, 132, 1)'
      }]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Knowledge Base Health Metrics'
        }
      }
    }
  };

  dv.paragraph("**Summary Metrics Chart:**");
  dv.paragraph("```json\n" + JSON.stringify(summaryChartConfig, null, 2) + "\n```");

  dv.paragraph("> 📋 Copy any configuration above and use directly with Charts.js");

} else {
  dv.paragraph("> 📭 No structured concepts found for chart generation.");
}

// Add styling for code blocks
dv.el("style", `
  pre {
    background: var(--background-primary-alt);
    padding: 1em;
    border-radius: 4px;
    max-height: 300px;
    overflow: auto;
    font-size: 0.85em;
    margin: 1em 0;
  }
`);
```




