## Intermediate Queries (DQL) 
### 1. Learning Progress Dashboard with Age Metrics
Shows your cognitive science notes with maturity stages, confidence levels, and how long they've been incubating in your system.
```datavie
TABLE 
  maturity AS "Growth Stage",
  confidence AS "Confidence",
  link-up AS "Connected MOCs",
  date(today) - file.cday AS "Age (days)"
FROM "03-notes" OR "07-mocs"
WHERE contains(type, "cog-sci") OR contains(link-up, "[[learning-theory-moc]]")
SORT maturity desc, confidence desc
```
### Concept Network Analysis via MOC Connections
FLATTENs all MOC connections to reveal which concepts bridge multiple knowledge domains, then groups and counts the intersections.
```datavie
TABLE 
  length(rows.file.link) AS "Linked Notes",
  join(map(rows.confidence, (c) => upper(substring(c, 0, 1))), " | ") AS "Confidence Levels"
FROM "03-notes"
FLATTEN link-up
WHERE type = "concept" AND link-up
GROUP BY link-up AS "MOC Hub"
SORT length(rows.file.link) DESC
```

### Priority Review Queue for Cognitive Enhancement
Creates a filtered task-like view of notes needing review, sorted by priority and enriched with contextual metadata.
```datavie
LIST 
  "**Priority:** " + priority + " | **Maturity:** " + maturity + " | **Confidence:** " + confidence + 
  "  \n**MOCs:** " + join(link-up, ", ") + "  \n**Age:** " + (date(today) - file.cday).days + " days"
FROM "03-notes"
WHERE maturity = "needs-review" OR maturity = "seedling"
WHERE contains(link-up, "[[cognitive-science-moc]]") OR contains(link-up, "[[educational-psychology-moc]]")
SORT priority asc, confidence desc
LIMIT 25
```

---

### Cognitive Load Distribution Heatmap
**Description:** This query analyzes your note-taking patterns across time and maturity stages, creating a temporal view of your cognitive load. It buckets notes by creation week and maturity level, helping you identify periods of high knowledge acquisition vs. consolidation phases.
**Top Use Cases:**
- Detecting burnout patterns when "seedling" notes spike without maturation
- Optimizing review schedules based on your natural learning rhythms
- Balancing intake (new notes) vs. processing (maturing notes)
- Quarterly PKB health assessments
**Tips for Implementation:**
- Best placed in a periodic review template (weekly/monthly)
- Run at the start of review sessions to gauge recent activity
- Combine with daily notes metadata for richer insights
- Export data to CSV for external visualization tools
**Customization Options:**
- Change `timeBucket` to "day", "month", or "quarter"
- Modify `maturityOrder` to match your personal growth taxonomy
- Add `confidence` dimension as a third axis
- Filter by specific MOCs to focus on single domains
```dataviewj
// Cognitive Load Distribution Heatmap
const timeBucket = "week"; // "day", "week", "month"
const maturityOrder = ["seedling", "developing", "budding", "evergreen", "needs-review"];
// Get date bucket function
function getDateBucket(fileCday) {
  const date = dv.date(fileCday);
  if (timeBucket === "week") {
    return date.toFormat("yyyy-WW");
  } else if (timeBucket === "month") {
    return date.toFormat("yyyy-MM");
  }
  return date.toFormat("yyyy-MM-dd");
}
// Collect data
const pages = dv.pages('"03-notes" or "02-projects"')
  .where(p => p.maturity && p.type && 
    (p.type.includes("cog-sci") || p.type.includes("experiment") || p.type.includes("mental-model")));
const buckets = {};
pages.forEach(page => {
  const bucket = getDateBucket(page.file.cday);
  if (!buckets[bucket]) {
    buckets[bucket] = {};
    maturityOrder.forEach(m => buckets[bucket][m] = 0);
  }
  if (buckets[bucket][page.maturity] !== undefined) {
    buckets[bucket][page.maturity]++;
  }
});
// Render table
const headers = ["Time Period", ...maturityOrder.map(m => m.charAt(0).toUpperCase() + m.slice(1))];
const rows = Object.keys(buckets).sort().reverse().slice(0, 12).map(bucket => {
  const row = [bucket];
  maturityOrder.forEach(m => row.push(buckets[bucket][m]));
  return row;
});
dv.table(headers, rows);
```

---
## Synergy Queries (use Charts or JS Engine)
### Learning Velocity & Maturity Flow Chart
**Description:** This query integrates DataviewJS with the Charts plugin to visualize the lifecycle of your cognitive science notes. It shows creation velocity (new notes per week) alongside maturity transitions, creating a Sankey-like flow diagram of knowledge evolution from seedling to evergreen.
**Top Use Cases:**
- Presenting PKB growth in visual form for annual reviews
- Identifying bottlenecks where notes stagnate in "developing" stage
- Demonstrating ROI of your note-taking system to yourself
- Planning focused review sprints based on maturity distribution
**Tips for Implementation:**
- Requires the Charts plugin (`obsidian://show-plugin?id=obsidian-charts`)
- Place in a high-level dashboard like `06-dashboards/learning-analytics.md`
- Use `chart` code block (not `dataviewjs`) after data preparation
- Set chart type to "line" for velocity and "bar" for distribution
**Customization Options:**
- Change `weeksBack` to adjust the historical window (4-52 weeks)
- Modify `maturityStages` colors in the chart config
- Add secondary axis for confidence levels
- Filter by specific MOCs to create domain-specific views
```dataviewj
// Prepare data for Learning Velocity Chart
const weeksBack = 12;
const maturityStages = ["seedling", "developing", "budding", "evergreen"];
const colors = ["#ff9999", "#ffcc99", "#99ccff", "#99ff99"];
// Get weekly data
const weeklyData = {};
for (let i = weeksBack; i >= 0; i--) {
  const date = dv.date('today').minus(dv.duration(`${i} weeks`));
  const weekKey = date.toFormat("yyyy-WW");
  weeklyData[weekKey] = {
    week: date.toFormat("WW"),
    total: 0,
    ...Object.fromEntries(maturityStages.map(m => [m, 0]))
  };
}
// Populate counts
dv.pages('"03-notes"')
  .where(p => p.maturity && p.file.cday >= dv.date('today').minus(dv.duration(`${weeksBack} weeks`)))
  .forEach(p => {
    const weekKey = p.file.cday.toFormat("yyyy-WW");
    if (weeklyData[weekKey]) {
      weeklyData[weekKey].total++;
      if (weeklyData[weekKey][p.maturity] !== undefined) {
        weeklyData[weekKey][p.maturity]++;
      }
    }
  });
// Output data for Charts plugin
const chartData = {
  type: 'bar',
  data: {
    labels: Object.values(weeklyData).map(d => `W${d.week}`),
    datasets: maturityStages.map((stage, i) => ({
      label: stage.charAt(0).toUpperCase() + stage.slice(1),
      data: Object.values(weeklyData).map(d => d[stage]),
      backgroundColor: colors[i] + "80",
      borderColor: colors[i],
      borderWidth: 1
    }))
  },
  options: {
    responsive: true,
    scales: {
      x: { stacked: true },
      y: { stacked: true, beginAtZero: true }
    },
    plugins: {
      title: { display: true, text: "Weekly Note Creation by Maturity Stage" }
    }
  }
};
// Render chart container
dv.paragraph("```chart\n" + JSON.stringify(chartData, null, 2) + "\n```");
```

### Confidence Distribution Sunburst with Maturity Layers
**Description:** Creates a multi-level sunburst chart using Charts plugin that segments your cognitive science notes first by maturity stage (inner ring), then by confidence level (outer ring), providing a hierarchical view of knowledge quality and growth stage distribution.
**Top Use Cases:**
- Quick visual assessment of PKB health during monthly reviews
- Identifying weak spots (e.g., many "seedling" + "speculative" notes)
- Tracking progression toward "evergreen" + "high" confidence over time
- Communicating PKB maturity to collaborators or mentors
**Tips for Implementation:**
- Use `chart` code block type with `type: 'sunburst'`
- Place in `06-dashboards/pkb-health-dashboard.md`
- Update weekly via template automation
- Combine with `WHERE file.mtime >= date(today) - dur(1 week)` for change detection
**Customization Options:**
- Modify `innerRing` and `outerRing` fields to create different hierarchies
- Change `colorScheme` to match your Obsidian theme
- Add third ring for `source` to analyze AI tool effectiveness
- Filter by specific MOCs to create domain-specific sunbursts
```dataviewj
// Confidence Distribution Sunburst Data Generator
const maturityStages = ["seedling", "developing", "budding", "evergreen", "needs-review"];
const confidenceLevels = ["speculative", "provisional", "moderate", "established", "high"];
// Build hierarchical data
const hierarchy = {
  name: "Knowledge Base",
  children: maturityStages.map(maturity => {
    const maturityNotes = dv.pages('"03-notes"')
      .where(p => p.maturity === maturity && 
        (p.type === "cog-sci-report" || p.type === "mental-model" || p.type === "concept"));
    return {
      name: maturity.charAt(0).toUpperCase() + maturity.slice(1),
      children: confidenceLevels.map(confidence => {
        const count = maturityNotes.filter(p => p.confidence === confidence).length;
        return {
          name: confidence.charAt(0).toUpperCase() + confidence.slice(1),
          value: count,
          itemStyle: {
            color: {
              "speculative": "#8b5cf6",
              "provisional": "#ef4444",
              "moderate": "#f59e0b",
              "established": "#3b82f6",
              "high": "#10b981"
            }[confidence]
          }
        };
      }).filter(c => c.value > 0)
    };
  }).filter(m => m.children.length > 0)
};
// Render sunburst chart
const chartConfig = {
  type: 'sunburst',
  data: hierarchy,
  options: {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Knowledge Distribution: Maturity × Confidence',
        font: { size: 16 }
      },
      legend: { display: false }
    }
  }
};
dv.paragraph("```chart\n" + JSON.stringify(chartConfig, null, 2) + "\n```");
// Summary stats
const totalNotes = dv.pages('"03-notes"')
  .where(p => maturityStages.includes(p.maturity) && confidenceLevels.includes(p.confidence)).length;
const evergreenHigh = dv.pages('"03-notes"')
  .where(p => p.maturity === "evergreen" && p.confidence === "high").length;
dv.paragraph(`**Total Notes:** ${totalNotes} | **Evergreen + High Confidence:** ${evergreenHigh} (${Math.round(evergreenHigh/totalNotes*100)}%)`);
```


# Dataview Query Examples for a PKB Centered Around **Cognitive Science & Learning Theories**

---
## Intermediate Queries (DQL)
### 1. **Flattened List of All Notes Linked to Cognitive Science MOC with Their Maturity Status**
This query flattens all links in the `link-up` field and filters for those connected to `[[cognitive-science-moc]]`, then displays their maturity and file name.
```
TABLE maturity AS "Maturity"
FROM #cognitive-science
WHERE contains(link-up, [[cognitive-science-moc]])
FLATTEN file.name AS "Note"
```

---
### 2. **Grouped Count of Note Types by Maturity Level**
This groups notes tagged with `#cognitive-science` by both `type` and `maturity`, showing how many notes exist in each combination.
```
TABLE rows.file.name AS "Notes"
FROM #cognitive-science
GROUP BY type
GROUP BY maturity
```

---
### 3. **Notes Created in the Last 7 Days Sorted by Priority**
This calculates the age of each note and filters for those created within the last week, sorting them by priority.
```
TABLE date(today) - file.cday AS "Age (Days)", priority AS "Priority"
FROM #cognitive-science OR #learning-theory
WHERE file.cday >= date(today) - dur(7 days)
SORT priority DESC
```

---
### 4. **List of Permanent Notes with More Than 3 Backlinks**
This filters for permanent notes and uses `length()` to count backlinks, displaying only those with more than three.
```
TABLE length(file.inlinks) AS "Backlinks"
FROM #type/permanent
WHERE length(file.inlinks) > 3
SORT file.inlinks DESC
```

---
## Advanced Queries (DataviewJS)
### 1. **Dynamic Maturity Heatmap by Type and Confidence**
#### Description:
Generates a heatmap-style table showing the distribution of notes across combinations of `type` and `confidence`. Useful for identifying underdeveloped areas.
#### Top Use Cases:
- Prioritizing content development
- Tracking knowledge base balance
- Identifying gaps in coverage or confidence levels
#### Tips for Implementation:
- Ensure consistent use of `type` and `confidence` metadata.
- Consider filtering by tag or folder for more focused insights.
#### Customization Options:
- Filter by specific tags like `#cognitive-science`
- Add color-coding via CSS snippets or external tools
- Export to markdown tables or integrate with Charts plugin
```dataviewjs

const pages = dv.pages("#cognitive-science").array();
let heatmap = {};
pages.forEach(p => {
  const t = p.type || "unknown";
  const c = p.confidence || "unknown";
  if (!heatmap[t]) heatmap[t] = {};
  heatmap[t][c] = (heatmap[t][c] || 0) + 1;
});
dv.table(
  ["Type", "Speculative", "Provisional", "Moderate", "Established", "High"],
  Object.entries(heatmap).map(([type, confs]) => [
    type,
    confs["speculative"] || 0,
    confs["provisional"] || 0,
    confs["moderate"] || 0,
    confs["established"] || 0,
    confs["high"] || 0
  ])
);
```

---
### 2. **Backlink Growth Over Time Using File Creation Dates**
#### Description:
Calculates cumulative backlink growth over time based on file creation dates. Helps visualize how interconnected your PKB becomes over time.
#### Top Use Cases:
- Measuring PKB maturity
- Tracking engagement with core concepts
- Visualizing network effects in knowledge work
#### Tips for Implementation:
- Ensure backlinks are tracked via `file.inlinks`
- Consider limiting scope to avoid performance issues
#### Customization Options:
- Group by tag or folder
- Add moving averages or trend lines
- Export data for visualization in Charts or JS Engine
```dataviewj

const pages = dv.pages("#cognitive-science").array();
let data = pages.map(p => ({
  date: p.file.cday.toFormat("yyyy-MM-dd"),
  backlinks: p.file.inlinks.length
})).sort((a, b) => a.date.localeCompare(b.date));
let cumulative = 0;
data = data.map(d => {
  cumulative += d.backlinks;
  return [d.date, cumulative];
});
dv.paragraph("### Cumulative Backlinks Over Time");
dv.table(["Date", "Cumulative Backlinks"], data);
```

---

# Dataview Queries for Finding Connections Between Notes
## Intermediate Queries (DQL)

### 2. Cross-Reference Notes by MOC Links
This query shows which notes are connected to multiple Maps of Content, revealing interdisciplinary connections.
```dataview
TABLE WITHOUT ID
  file.link AS Note,
  link-up AS Connected_MOCs,
  length(link-up) AS Connection_Count
FROM "03-notes" OR "07-mocs"
WHERE length(link-up) > 1
SORT Connection_Count DESC
```
### 3. Discover Concept Networks by Type Relationships
This query maps how different note types connect to each other, showing knowledge flow patterns.
```dataview
TABLE WITHOUT ID
  file.link AS Source_Note,
  type AS Note_Type,
  outlinks.file.link AS Connected_Notes,
  outlinks.type AS Connected_Types
FROM "03-notes"
WHERE type = "concept" OR type = "mental-model"
FLATTEN outlinks WHERE contains(outlinks.type, "permanent-note") OR contains(outlinks.type, "framework")
```
### 4. Age-Based Connection Analysis
This query finds older notes that might benefit from connections to newer insights.
```dataview
TABLE WITHOUT ID
  file.link AS Note,
  type,
  date(today) - file.cday AS Age_Days,
  file.outlinks AS Outlinks,
  length(file.outlinks) AS Link_Count
FROM "03-notes"
WHERE (date(today) - file.cday) > dur(180 days) AND length(file.outlinks) < 3
SORT Age_Days DESC
```

### 2. Knowledge Gap Analyzer
This query identifies areas in your PKB with sparse connections and suggests where new content might be needed.
**Description:** Analyzes the link density of your notes to find isolated knowledge islands and over-connected hubs that might need restructuring.
**Top Use Cases:**
- Finding orphaned notes that need integration
- Identifying over-centralized knowledge that could be decentralized
- Discovering thematic areas lacking sufficient connections
**Tips for Implementation:**
- Run this on your main content folders (03-notes, 04-library)
- Adjust the thresholds for "isolated" and "overconnected" based on your PKB size
- Combine with manual review for best results
**Customization Options:**
- Filter by specific MOCs to analyze particular knowledge domains
- Weight inbound vs outbound links differently
- Include file creation dates to prioritize older isolated notes
```dataviewj
const allNotes = dv.pages('"03-notes" OR "04-library"')
  .filter(p => p.type && p.type !== "moc");
const connectionData = allNotes.map(note => {
  const outlinks = note.file.outlinks ? note.file.outlinks.length : 0;
  const inlinks = dv.pages('"03-notes" OR "04-library"')
    .filter(p => p.file.outlinks && p.file.outlinks.some(link => link.path === note.file.path))
    .length;
  return {
    note: note.file.link,
    type: note.type || 'N/A',
    outlinks: outlinks,
    inlinks: inlinks,
    totalConnections: outlinks + inlinks,
    maturity: note.maturity || 'N/A'
  };
});
// Find isolated notes (low connections)
const isolatedNotes = connectionData
  .filter(note => note.totalConnections < 2)
  .sort((a, b) => a.totalConnections - b.totalConnections);
// Find over-connected notes (potential hubs)
const hubNotes = connectionData
  .filter(note => note.totalConnections > 10)
  .sort((a, b) => b.totalConnections - a.totalConnections);
// Find notes with imbalanced connections
const imbalancedNotes = connectionData
  .filter(note => note.outlinks > 0 && note.inlinks > 0)
  .map(note => ({
    ...note,
    ratio: note.outlinks / note.inlinks
  }))
  .filter(note => note.ratio > 5 || note.ratio < 0.2)
  .sort((a, b) => b.ratio - a.ratio);
dv.header(3, "Isolated Notes (Need More Connections)");
dv.table(
  ["Note", "Type", "Total Links", "Maturity"],
  isolatedNotes.slice(0, 10).map(note => [note.note, note.type, note.totalConnections, note.maturity])
);
dv.header(3, "Knowledge Hubs (Potential Over-centralization)");
dv.table(
  ["Note", "Type", "Outbound", "Inbound", "Total"],
  hubNotes.slice(0, 10).map(note => [note.note, note.type, note.outlinks, note.inlinks, note.totalConnections])
);
dv.header(3, "Imbalanced Connection Ratios");
dv.table(
  ["Note", "Type", "Outbound", "Inbound", "Ratio"],
  imbalancedNotes.slice(0, 10).map(note => [note.note, note.type, note.outlinks, note.inlinks, note.ratio.toFixed(2)])
);
```


## Basic Queries (DQL)
These queries form the foundation of Dataview usage, perfect for beginners learning how to extract and organize data from their PKB.

---
### List all notes tagged with #cognitive-science
This query retrieves all files tagged with `#cognitive-science`, displaying them as a simple list.
```
LIST
WHERE contains(file.tags, "#cognitive-science")
```

---
### Table of all reports with metadata
This query creates a table showing key metadata for all notes of type `report`, including creation date and maturity level.
```
TABLE type, maturity, file.cday AS "Created"
FROM #type/report
```

---
### List of recent permanent notes sorted by modification time
This query lists all notes tagged as permanent (`#type/permanent`) and sorts them by most recently modified.
```
LIST
WHERE contains(file.tags, "#type/permanent")
SORT file.mtime DESC
```

---
### Notes created in the last 7 days
This query filters notes created within the past week using date arithmetic.
```
LIST
WHERE file.cday >= date(today) - dur(7 days)
```

---
## Intermediate Queries (DQL)
These queries introduce more advanced features like flattening arrays, grouping data, and performing calculations.

---
### Flatten and count tags per note in cognitive science
This query expands the tags array for each cognitive science note and counts how many tags each has.
```
TABLE flat(file.tags) AS Tags, length(file.tags) AS "Tag Count"
WHERE contains(file.tags, "#cognitive-science")
FLATTEN file.tags
```

---
### Group notes by maturity and show count
This query groups all notes by their `maturity` field and shows how many notes exist in each maturity level.
```
TABLE rows.file.name AS "Notes"
WHERE maturity
GROUP BY maturity
```

---
### List of high-priority notes with regex filtering
This query finds all notes with `priority` set to `high` or `urgent` and whose title contains "PKB" or "system".
```
LIST
WHERE (priority = "high" OR priority = "urgent")
AND regexmatch("PKB|system", file.name)
```

---
### Calculate age of notes in days
This query calculates how many days old each note is by subtracting its creation date from today.
```
TABLE date(today) - file.cday AS "Age (Days)"
WHERE file.cday
SORT file.cday DESC
```

---
## Advanced Queries (DataviewJS)
These DataviewJS queries demonstrate powerful data transformations, custom rendering, and integration with Luxon for date manipulation.

---
### Maturity Distribution Dashboard with Custom Rendering
**Description:** This query aggregates all notes by their `maturity` level and renders a custom dashboard showing counts and percentages with color-coded badges.
**Top Use Cases:**
- Monitoring knowledge base growth and maturity
- Identifying areas needing attention or review
- Creating executive summaries for PKB health
**Implementation Tips:**
- Uses `groupBy` to aggregate data efficiently
- Handles missing maturity values gracefully
- Renders with semantic HTML for clean Obsidian styling
**Customization Options:**
- Change color scheme by modifying CSS classes
- Add filtering by tag or folder
- Include links to filtered views of each maturity group
```dataviewj
// Group all pages by maturity and render a summary dashboard
const pages = dv.pages().where(p => p.maturity);
const maturityGroups = pages.groupBy(p => p.maturity);
const totalCount = pages.length;
dv.header(3, "📘 PKB Maturity Overview");
dv.paragraph(`Total Notes: ${totalCount}`);
const container = dv.el("div", "", {cls: "maturity-dashboard"});
maturityGroups.forEach(group => {
    const count = group.rows.length;
    const percentage = ((count / totalCount) * 100).toFixed(1);
    // Color coding based on maturity level
    let colorClass = "";
    switch(group.key) {
        case 'seedling': colorClass = "seedling"; break;
        case 'developing': colorClass = "developing"; break;
        case 'budding': colorClass = "budding"; break;
        case 'evergreen': colorClass = "evergreen"; break;
        default: colorClass = "default";
    }
    dv.el("div", 
        `<span class="maturity-badge ${colorClass}">${group.key}</span>
         <span class="count">${count}</span>
         <span class="percentage">(${percentage}%)</span>`, 
        {cls: "maturity-item", container});
});
// Add CSS styling
dv.el("style", `
.maturity-dashboard { 
    display: flex; 
    flex-direction: column; 
    gap: 10px; 
    margin: 1em 0;
}
.maturity-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 12px;
    border-radius: 6px;
    background: var(--background-secondary);
}
.maturity-badge {
    padding: 4px 12px;
    border-radius: 20px;
    font-weight: bold;
    text-transform: uppercase;
    font-size: 0.8em;
}
.seedling { background: #e0f7fa; color: #006064; }
.developing { background: #fff3e0; color: #e65100; }
.budding { background: #f3e5f5; color: #4a148c; }
.evergreen { background: #e8f5e9; color: #1b5e20; }
.count {
    font-weight: bold;
    min-width: 30px;
    text-align: center;
}
.percentage {
    color: var(--text-muted);
    font-size: 0.9em;
}
`);
```

---
### Temporal Knowledge Evolution Analysis
**Description:** This query analyzes how your PKB has evolved over time by grouping notes by creation month and showing type distribution with Luxon-powered date formatting.
**Top Use Cases:**
- Understanding knowledge creation patterns
- Identifying periods of high productivity
- Tracking shifts in content focus over time
**Implementation Tips:**
- Uses Luxon for robust date manipulation
- Handles missing dates gracefully
- Efficiently processes large datasets with map/reduce
**Customization Options:**
- Change grouping granularity (week, quarter, year)
- Add filtering by specific tags or folders
- Include modification dates for activity analysis
```dataviewj
// Analyze PKB growth over time with type distribution
const pages = dv.pages().where(p => p.file.cday);
const dateFormat = "yyyy-MM";
// Group by creation month and type
const monthlyData = pages
    .map(p => ({
        date: p.file.cday.toFormat(dateFormat),
        type: p.type || "untyped",
        page: p
    }))
    .groupBy(p => p.date)
    .map(group => ({
        month: group.key,
        total: group.rows.length,
        types: group.rows.groupBy(r => r.type)
    }))
    .sort((a, b) => a.month.localeCompare(b.month));
// Render timeline
dv.header(3, "📅 Knowledge Evolution Timeline");
const headers = ["Month", "Total", "Type Distribution"];
const values = monthlyData.map(m => [
    m.month,
    m.total,
    m.types.map(t => `${t.key}(${t.rows.length})`).join(", ")
]);
dv.table(headers, values);
```


---
### Multi-Dimensional Content Quality Matrix
**Description:** This query evaluates content quality across multiple dimensions (maturity, confidence, status) and renders a comprehensive quality matrix with visual indicators.
**Top Use Cases:**
- Prioritizing content for review or development
- Identifying high-value content for publication
- Tracking quality improvement over time
**Implementation Tips:**
- Uses multi-dimensional grouping for complex analysis
- Implements custom scoring algorithms
- Handles missing data with default values
**Customization Options:**
- Add additional quality metrics (completeness, citations)
- Implement different scoring systems
- Export data for external analysis
```dataviewj
// Multi-dimensional content quality analysis
const qualityPages = dv.pages().where(p => p.type && p.maturity);
const qualityMatrix = qualityPages
    .groupBy(p => p.maturity)
    .map(maturityGroup => ({
        maturity: maturityGroup.key,
        confidenceGroups: maturityGroup.rows
            .groupBy(p => p.confidence || "unknown")
            .map(confidenceGroup => ({
                confidence: confidenceGroup.key,
                statusGroups: confidenceGroup.rows
                    .groupBy(p => p.status || "unknown")
                    .map(statusGroup => ({
                        status: statusGroup.key,
                        count: statusGroup.rows.length,
                        pages: statusGroup.rows
                    }))
            }))
    }));
// Render quality matrix
dv.header(3, "⭐ Content Quality Matrix");
qualityMatrix.forEach(maturityGroup => {
    dv.header(4, `🌱 ${maturityGroup.maturity}`);
    const tableData = [];
    maturityGroup.confidenceGroups.forEach(confidenceGroup => {
        confidenceGroup.statusGroups.forEach(statusGroup => {
            tableData.push([
                confidenceGroup.confidence,
                statusGroup.status,
                statusGroup.count,
                statusGroup.pages.map(p => p.file.link).join(", ")
            ]);
        });
    });
    dv.table(["Confidence", "Status", "Count", "Notes"], tableData);
});
```

---

---
### Interactive Task Prioritization Matrix with Buttons
**Description:** This query integrates with the Buttons plugin to create an interactive Eisenhower Matrix for task prioritization, allowing users to update task status directly from the dashboard.
**Top Use Cases:**
- Daily task planning and prioritization
- Team task management and delegation
- Project milestone tracking and progress monitoring
**Implementation Tips:**
- Requires Buttons plugin v0.5+ installed
- Uses YAML frontmatter for task metadata
- Implements error handling for missing fields
**Customization Options:**
- Add filtering by project or context tags
- Include due date warnings and overdue indicators
- Export prioritized tasks to daily notes
```dataviewj
// Interactive Eisenhower Matrix with Buttons
const tasks = dv.pages("#type/task")
    .where(t => t.priority && t.urgency)
    .sort(t => t.priority, 'desc');
// Categorize tasks
const quadrants = {
    "Do First": tasks.filter(t => t.urgency === "high" && t.importance === "high"),
    "Schedule": tasks.filter(t => t.urgency === "low" && t.importance === "high"),
    "Delegate": tasks.filter(t => t.urgency === "high" && t.importance === "low"),
    "Eliminate": tasks.filter(t => t.urgency === "low" && t.importance === "low")
};
// Render matrix
dv.header(3, "🎯 Eisenhower Task Matrix");
for (const [quadrant, taskList] of Object.entries(quadrants)) {
    dv.header(4, quadrant);
    const container = dv.el("div", "", {cls: "quadrant-container"});
    taskList.forEach(task => {
        const taskDiv = dv.el("div", "", {cls: "task-item", container});
        dv.el("div", task.file.link, {cls: "task-title", container: taskDiv});
        dv.el("div", `Priority: ${task.priority}`, {cls: "task-priority", container: taskDiv});
        // Add action buttons
        dv.paragraph("```button\n" +
            "name: Complete\n" +
            "type: command\n" +
            "action: Tasks: Complete Task\n" +
            "color: green\n" +
            "```", {container: taskDiv});
        dv.paragraph("```button\n" +
            "name: Snooze\n" +
            "type: command\n" +
            "action: Tasks: Postpone Task\n" +
            "color: orange\n" +
            "```", {container: taskDiv});
    });
    dv.el("hr", "", {container});
}
// Add CSS styling
dv.el("style", `
.quadrant-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 15px;
    margin: 1em 0;
}
.task-item {
    border: 1px solid var(--background-modifier-border);
    border-radius: 8px;
    padding: 12px;
    background: var(--background-primary-alt);
}
.task-title {
    font-weight: bold;
    margin-bottom: 8px;
}
.task-priority {
    font-size: 0.9em;
    color: var(--text-muted);
}
`);
```












