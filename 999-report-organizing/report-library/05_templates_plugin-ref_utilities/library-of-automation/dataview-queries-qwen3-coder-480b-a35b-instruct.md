## Intermediate Queries (DQL)

### 1. Group Notes by Type and Maturity
This query groups all notes by their `type` and then further groups them by `maturity`, showing the count of notes in each subgroup.

```
TABLE rows.file.name as "Notes"
FROM "03-notes" OR "04-library"
GROUP BY type
GROUP BY maturity
```

### 2. Flatten and Filter Tags Across Multiple Folders
This example uses `FLATTEN` to extract individual tags from a list and filters for specific ones, such as those related to cognitive science or PKM.

```
TABLE file.name AS "Note", tag AS "Tag"
FROM "03-notes" OR "07-mocs"
FLATTEN file.tags AS tag
WHERE contains(tag, "#cognitive") OR contains(tag, "#pkb")
```

### 3. Calculate Age of Notes and Filter by Priority
Calculates how many days old each note is based on creation date (`file.cday`) and filters for high-priority items that are more than 30 days old.

```
TABLE date(today) - file.cday AS "Age (Days)", priority
FROM "03-notes"
WHERE priority = "high" AND (date(today) - file.cday) > 30
SORT file.cday ASC
```

### 4. List Notes with Multiple Link-ups (MOCs)
Identifies notes linked to more than one MOC using the `link-up` field, which can be useful for finding highly connected content.

```
TABLE file.name AS "Note", link-up AS "Linked MOCs", length(link-up) AS "# of MOCs"
FROM "03-notes"
WHERE length(link-up) > 1
SORT length(link-up) DESC
```

---

## Advanced Queries (DataviewJS)

### 1. **Dynamic Knowledge Network Mapper**
#### Description:
This script scans through your notes to build a network map of connections between MOCs and other content types. It visualizes how different domains like cognitive science, cosmology, and PKM interconnect through shared notes.

#### Top Use Cases:
- Visualizing interdisciplinary knowledge overlap
- Identifying under-connected MOCs
- Tracking evolution of cross-domain insights

#### Tips for Implementation:
- Place in a dashboard or MOC note for live updates
- Consider limiting scope to avoid performance issues with large vaults
- Add filtering logic for specific time ranges or priorities

#### Customization Options:
- Modify `targetMOCs` to focus on specific domains
- Adjust `minConnectionCount` to filter weak links
- Include additional metadata like `status` or `confidence`

```javascript
const targetMOCs = [
  "artificial-intelligence-moc",
  "cognitive-science-moc",
  "cosmology-moc",
  "pkb-&-pkm-moc"
];

const connections = {};
const allNotes = dv.pages('"03-notes" OR "04-library"');

for (const note of allNotes) {
  if (!note.linkUp || note.linkUp.length < 2) continue;

  const linkedMOCs = note.linkUp
    .filter(moc => targetMOCs.includes(moc.path))
    .map(moc => moc.path);

  if (linkedMOCs.length < 2) continue;

  for (let i = 0; i < linkedMOCs.length; i++) {
    for (let j = i + 1; j < linkedMOCs.length; j++) {
      const pair = [linkedMOCs[i], linkedMOCs[j]].sort().join(" ↔ ");
      connections[pair] = (connections[pair] || 0) + 1;
    }
  }
}

dv.header(3, "Knowledge Network Connections");
dv.list(Object.entries(connections).map(([pair, count]) => 
  `${pair} (${count} shared notes)`
));
```

### 2. **Progress Tracker for Multi-Stage Notes**
#### Description:
Tracks the maturity progression of notes across statuses, calculating average time taken to move from seedling to evergreen. Useful for understanding personal knowledge development velocity.

#### Top Use Cases:
- Measuring PKB growth efficiency
- Identifying bottlenecks in note maturation
- Benchmarking content quality timelines

#### Tips for Implementation:
- Add this to a monthly PKB report template
- Use `file.ctime` and `file.mtime` for creation/modification tracking
- Consider excluding archived or deprecated notes

#### Customization Options:
- Filter by `type` (e.g., only `permanent-note`, `concept`)
- Add confidence-weighted scoring
- Export results to CSV via JS Engine

```javascript
const maturityStages = ["seedling", "developing", "budding", "evergreen"];
const stageDates = {};
const stageCounts = {};

dv.pages('"03-notes"')
  .where(p => p.maturity && maturityStages.includes(p.maturity))
  .forEach(page => {
    const stage = page.maturity;
    const ctime = page.file.ctime.toMillis();
    
    if (!stageDates[stage]) stageDates[stage] = [];
    stageDates[stage].push(ctime);
    
    stageCounts[stage] = (stageCounts[stage] || 0) + 1;
  });

const avgStageTimes = {};
for (let i = 1; i < maturityStages.length; i++) {
  const prevStage = maturityStages[i - 1];
  const currStage = maturityStages[i];
  
  if (stageDates[prevStage] && stageDates[currStage]) {
    const avgPrev = stageDates[prevStage].reduce((a,b) => a + b, 0) / stageDates[prevStage].length;
    const avgCurr = stageDates[currStage].reduce((a,b) => a + b, 0) / stageDates[currStage].length;
    const diffDays = Math.round((avgCurr - avgPrev) / (1000 * 60 * 60 * 24));
    avgStageTimes[`${prevStage} → ${currStage}`] = `${diffDays} days`;
  }
}

dv.header(3, "Average Time Between Maturity Stages");
dv.table(["Transition", "Avg Duration"], 
  Object.entries(avgStageTimes).map(([k, v]) => [k, v])
);
```

---

## Synergy Queries (use Charts or JS Engine)

### 1. **Maturity Distribution Radar Chart**
#### Description:
Generates a radar chart showing distribution of notes across maturity levels. Works with the Charts plugin to visualize content lifecycle balance.

#### Top Use Cases:
- Monitoring PKB health and content diversity
- Balancing effort between new ideas and refined concepts
- Reporting to AI assistants on knowledge base status

#### Tips for Implementation:
- Requires Charts plugin installed and enabled
- Best placed in a dashboard note for real-time monitoring
- Combine with filters for specific domains or authors

#### Customization Options:
- Segment by `type` or `source`
- Overlay with confidence ratings
- Compare distributions over time using date filters

```javascript
const maturityLevels = ["seedling", "developing", "budding", "evergreen", "needs-review"];
const counts = maturityLevels.map(level => 
  dv.pages('"03-notes"').where(p => p.maturity === level).length
);

window.renderChart({
  type: "radar",
  data: {
    labels: maturityLevels,
    datasets: [{
      label: "Note Maturity Distribution",
      data: counts,
      backgroundColor: "rgba(54, 162, 235, 0.2)",
      borderColor: "rgba(54, 162, 235, 1)",
      borderWidth: 2
    }]
  },
  options: {
    scales: { r: { min: 0 } }
  }
});
```

### 2. **AI Source Contribution Analysis**
#### Description:
Analyzes contribution patterns from different AI models, showing volume, average confidence, and most active domains. Integrates with JS Engine for exportable analytics.

#### Top Use Cases:
- Optimizing AI tool usage for research tasks
- Evaluating model reliability across domains
- Automating source attribution in generated reports

#### Tips for Implementation:
- Ensure consistent use of `source` metadata in AI-generated notes
- Combine with task tracking for cost/benefit analysis
- Schedule periodic summaries using templater or periodic notes

#### Customization Options:
- Filter by date range or project tags
- Weight contributions by note length or complexity
- Export to external analytics tools via JS Engine

```javascript
const sources = [
  "claude-opus-4.1",
  "claude-sonnet-4.5",
  "gemini-pro-3.0",
  "gemini-flash-2.5"
];

const results = sources.map(source => {
  const pages = dv.pages('"04-library"').where(p => p.source === source);
  const count = pages.length;
  const avgConfidence = pages
    .where(p => p.confidence)
    .map(p => ["speculative", "provisional", "moderate", "established", "high"]
      .indexOf(p.confidence))
    .average() || 0;
  
  const topTypes = pages
    .groupBy(p => p.type)
    .sort(g => g.rows.length, 'desc')
    .take(3)
    .map(g => g.key);

  return {
    source,
    count,
    avgConfidence: avgConfidence.toFixed(2),
    topTypes: topTypes.join(", ")
  };
});

dv.table(
  ["Source", "Notes Count", "Avg Confidence", "Top Types"],
  results.map(r => [r.source, r.count, r.avgConfidence, r.topTypes])
);

// Optional: Export via JS Engine
// window.exportData("ai_source_analysis", results);
```


## Intermediate Queries (DQL)

### 1. Group Notes by Type and Maturity with Count
This query organizes notes by their type and maturity level, showing how many notes exist in each category combination.

```
TABLE rows.file.name as "Notes", length(rows) as "Count"
FROM "03-notes" OR "04-library"
GROUP BY type
GROUP BY maturity
SORT length(rows) DESC
```

### 2. Flatten and Analyze Tags with Source Filtering
Extracts individual tags from notes generated by specific AI sources and displays them alongside confidence ratings.

```
TABLE file.name AS "Note", tag AS "Tag", confidence, source
FROM "04-library"
WHERE source = "claude-opus-4.1" OR source = "gemini-pro-3.0"
FLATTEN file.tags AS tag
WHERE contains(tag, "#cognitive") OR contains(tag, "#pkb")
SORT file.mtime DESC
```

### 3. Calculate Age and Filter by Multiple Criteria
Computes the age of notes in days and filters for high-priority items that are still in early maturity stages.

```
TABLE date(today) - file.cday AS "Age (Days)", priority, maturity, status
FROM "03-notes"
WHERE (priority = "high" OR priority = "urgent") 
  AND (maturity = "seedling" OR maturity = "developing")
  AND status != "archived"
SORT file.cday ASC
```

### 4. Find Notes with Multiple MOC Connections and High Confidence
Identifies highly connected notes that also have high confidence ratings, useful for finding reliable core knowledge.

```
TABLE file.name AS "Note", 
      link-up AS "Linked MOCs", 
      length(link-up) AS "# of MOCs",
      confidence
FROM "03-notes"
WHERE length(link-up) > 2 
  AND (confidence = "established" OR confidence = "high")
SORT length(link-up) DESC
```

## Advanced Queries (DataviewJS)

### 1. **AI Source Performance Matrix**
#### Description:
This script creates a comprehensive performance matrix comparing different AI sources across multiple dimensions: volume of contributions, average confidence levels, maturity distribution, and domain specialization. It helps identify which AI tools are most effective for specific types of knowledge work.

#### Top Use Cases:
- Optimizing AI tool selection for different research tasks
- Evaluating ROI of various AI services
- Creating automated source attribution reports

#### Tips for Implementation:
- Place in a dashboard note for continuous monitoring
- Consider adding date range filters for periodic analysis
- Combine with task tracking to correlate effort with output quality

#### Customization Options:
- Add filtering by project or domain tags
- Include word count or complexity metrics
- Export results to external analytics via JS Engine

```javascript
const sources = [
  "claude-opus-4.1",
  "claude-sonnet-4.5",
  "gemini-pro-3.0",
  "gemini-flash-2.5"
];

const confidenceMap = {
  "speculative": 1,
  "provisional": 2,
  "moderate": 3,
  "established": 4,
  "high": 5
};

const maturityWeights = {
  "seedling": 1,
  "developing": 2,
  "budding": 3,
  "evergreen": 4,
  "needs-review": 0.5
};

const results = sources.map(source => {
  const pages = dv.pages('"04-library"').where(p => p.source === source);
  
  if (pages.length === 0) return { source, count: 0 };
  
  const count = pages.length;
  
  const avgConfidence = pages
    .where(p => p.confidence)
    .map(p => confidenceMap[p.confidence] || 0)
    .average();
  
  const maturityScore = pages
    .where(p => p.maturity)
    .map(p => maturityWeights[p.maturity] || 0)
    .average();
  
  const domainSpecialization = pages
    .where(p => p.linkUp)
    .flatMap(p => p.linkUp.map(moc => moc.path))
    .groupBy(moc => moc)
    .sort(group => group.rows.length, 'desc')
    .take(3)
    .map(group => `${group.key} (${group.rows.length})`)
    .join(", ");
  
  const recentActivity = pages
    .sort(p => p.file.mtime, 'desc')
    .take(5)
    .map(p => p.file.link)
    .array();

  return {
    source,
    count,
    avgConfidence: avgConfidence ? avgConfidence.toFixed(2) : "N/A",
    maturityScore: maturityScore ? maturityScore.toFixed(2) : "N/A",
    domainSpecialization,
    recentActivity
  };
});

dv.header(3, "AI Source Performance Matrix");
dv.table(
  ["Source", "Notes", "Avg Confidence", "Maturity Score", "Top Domains", "Recent"],
  results.map(r => [
    r.source,
    r.count,
    r.avgConfidence,
    r.maturityScore,
    r.domainSpecialization,
    dv.el('div', r.recentActivity.slice(0, 3).map(link => link.toString()).join(" "))
  ])
);
```

### 2. **Knowledge Maturation Pipeline Tracker**
#### Description:
Tracks the flow of notes through different maturity stages over time, identifying bottlenecks and acceleration points in the knowledge development process. Calculates transition times between stages and highlights notes that are taking longer than average to mature.

#### Top Use Cases:
- Optimizing personal knowledge development workflows
- Identifying notes that need attention or review
- Measuring the effectiveness of knowledge refinement practices

#### Tips for Implementation:
- Add to a monthly PKB dashboard for progress tracking
- Consider excluding archived or deprecated notes from analysis
- Use file metadata history if available for more accurate timing

#### Customization Options:
- Filter by content type or domain tags
- Add confidence-weighted maturation scoring
- Set alerts for notes stuck in particular stages

```javascript
const maturityStages = ["seedling", "developing", "budding", "evergreen"];
const stageThresholds = {
  "seedling->developing": 7,    // days
  "developing->budding": 14,
  "budding->evergreen": 30
};

// Get all relevant notes
const notes = dv.pages('"03-notes" OR "04-library"')
  .where(p => p.maturity && maturityStages.includes(p.maturity));

// Group by maturity stage
const stageGroups = {};
maturityStages.forEach(stage => {
  stageGroups[stage] = notes.where(p => p.maturity === stage);
});

// Calculate stage statistics
const stageStats = maturityStages.map(stage => {
  const group = stageGroups[stage];
  const count = group.length;
  const avgAge = group
    .map(p => Math.floor((Date.now() - p.file.ctime.toMillis()) / (1000 * 60 * 60 * 24)))
    .average();
  
  return {
    stage,
    count,
    avgAge: avgAge ? `${Math.round(avgAge)} days` : "N/A"
  };
});

// Identify slow-maturing notes
const slowNotes = notes
  .where(p => {
    if (!p.maturity) return false;
    const ageDays = Math.floor((Date.now() - p.file.ctime.toMillis()) / (1000 * 60 * 60 * 24));
    const threshold = stageThresholds[`seedling->${p.maturity}`] || 
                     stageThresholds[`developing->${p.maturity}`] || 
                     stageThresholds[`budding->${p.maturity}`] || 30;
    return ageDays > threshold;
  })
  .sort(p => p.file.ctime, 'asc')
  .take(10);

dv.header(3, "Knowledge Maturation Pipeline");
dv.table(
  ["Stage", "Note Count", "Avg Age"],
  stageStats.map(s => [s.stage, s.count, s.avgAge])
);

dv.header(4, "Slow-Maturing Notes (Needs Attention)");
dv.table(
  ["Note", "Maturity", "Age", "Priority"],
  slowNotes.map(p => [
    p.file.link,
    p.maturity,
    `${Math.floor((Date.now() - p.file.ctime.toMillis()) / (1000 * 60 * 60 * 24))} days`,
    p.priority || "N/A"
  ])
);
```

## Synergy Queries (use Charts or JS Engine)

### 1. **Maturity Progression Timeline Visualization**
#### Description:
Creates an interactive timeline chart showing how notes progress through maturity stages over time. Visualizes both the volume of notes at each stage and the transition patterns between stages.

#### Top Use Cases:
- Monitoring PKB growth and development velocity
- Identifying seasonal patterns in knowledge work
- Presenting progress to collaborators or stakeholders

#### Tips for Implementation:
- Requires the Charts plugin to be installed and enabled
- Best placed in a dashboard note for real-time updates
- Consider limiting date range for better performance

#### Customization Options:
- Filter by content type or domain tags
- Add confidence level coloring
- Compare multiple time periods side-by-side

```javascript
// Generate data for the last 90 days
const startDate = dv.date('today').minus({ days: 90 });
const dates = [];
for (let i = 0; i <= 90; i++) {
  dates.push(startDate.plus({ days: i }));
}

const maturityStages = ["seedling", "developing", "budding", "evergreen"];
const stageData = {};

maturityStages.forEach(stage => {
  stageData[stage] = dates.map(date => {
    const count = dv.pages('"03-notes" OR "04-library"')
      .where(p => p.maturity === stage && 
                  p.file.ctime.toISODate() <= date.toISODate())
      .length;
    return count;
  });
});

const chartData = {
  labels: dates.map(d => d.toISODate()),
  datasets: maturityStages.map((stage, index) => {
    const colors = [
      'rgba(255, 99, 132, 1)',
      'rgba(54, 162, 235, 1)',
      'rgba(255, 205, 86, 1)',
      'rgba(75, 192, 192, 1)'
    ];
    
    return {
      label: stage,
      data: stageData[stage],
      borderColor: colors[index],
      backgroundColor: colors[index].replace('1)', '0.2)'),
      fill: true
    };
  })
};

window.renderChart({
  type: 'line',
  data: chartData,
  options: {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Knowledge Maturation Over Time'
      }
    },
    scales: {
      x: {
        type: 'time',
        time: {
          unit: 'day'
        }
      },
      y: {
        beginAtZero: true
      }
    }
  }
});
```

### 2. **AI Source Contribution Network Analysis**
#### Description:
Analyzes the contribution network of different AI sources across knowledge domains, creating a force-directed graph showing relationships between sources, domains, and content types. Integrates with JS Engine for advanced network analysis capabilities.

#### Top Use Cases:
- Understanding cross-domain AI capabilities
- Optimizing AI tool allocation for research projects
- Creating automated knowledge mapping systems

#### Tips for Implementation:
- Requires JS Engine plugin for advanced visualization
- Place in a dedicated analysis dashboard note
- Consider caching results for large vaults

#### Customization Options:
- Add temporal filtering for trend analysis
- Include confidence-weighted connections
- Export network data for external analysis

```javascript
const sources = [
  "claude-opus-4.1",
  "claude-sonnet-4.5",
  "gemini-pro-3.0",
  "gemini-flash-2.5"
];

const targetMOCs = [
  "artificial-intelligence-moc",
  "cognitive-science-moc",
  "cosmology-moc",
  "pkb-&-pkm-moc",
  "prompt-engineering-moc"
];

// Build network data
const nodes = [];
const links = [];

// Add source nodes
sources.forEach(source => {
  nodes.push({
    id: source,
    label: source,
    group: 'source',
    size: 20
  });
});

// Add MOC nodes and build connections
targetMOCs.forEach(moc => {
  nodes.push({
    id: moc,
    label: moc.replace('-moc', '').replace(/-/g, ' '),
    group: 'domain',
    size: 15
  });
  
  const mocPages = dv.pages('"03-notes" OR "04-library"')
    .where(p => p.linkUp && p.linkUp.some(link => link.path === moc));
  
  if (mocPages.length > 0) {
    sources.forEach(source => {
      const sourcePages = mocPages.where(p => p.source === source);
      if (sourcePages.length > 0) {
        links.push({
          source: source,
          target: moc,
          value: sourcePages.length,
          color: 'rgba(100, 100, 100, 0.5)'
        });
      }
    });
  }
});

// Add content type nodes
const contentTypes = ["concept", "permanent-note", "analysis", "framework"];
contentTypes.forEach(type => {
  nodes.push({
    id: type,
    label: type,
    group: 'type',
    size: 12
  });
});

// Connect domains to content types
targetMOCs.forEach(moc => {
  const mocPages = dv.pages('"03-notes" OR "04-library"')
    .where(p => p.linkUp && p.linkUp.some(link => link.path === moc));
  
  contentTypes.forEach(type => {
    const typeCount = mocPages.where(p => p.type === type).length;
    if (typeCount > 0) {
      links.push({
        source: moc,
        target: type,
        value: typeCount,
        color: 'rgba(150, 150, 150, 0.3)'
      });
    }
  });
});

// Export for visualization
window.networkData = {
  nodes: nodes,
  links: links
};

dv.paragraph("Network analysis data prepared. Use JS Engine visualization tools to render the graph.");
dv.paragraph(`Nodes: ${nodes.length}, Links: ${links.length}`);
```

# Dataview Query Inspiration for Cognitive Science & PKB Development

## Intermediate Queries (DQL)

*Here are some intermediate-level DQL queries that demonstrate powerful filtering, grouping, and field manipulation techniques relevant to your cognitive science and PKB theme.*

```
TABLE 
  link-up AS "MOC Links",
  maturity,
  confidence,
  length(file.inlinks) AS "Inbound Links"
FROM "03-notes" 
WHERE type = "concept" AND maturity != "seedling"
SORT length(file.inlinks) DESC
LIMIT 10
```

```
TABLE 
  type,
  status,
  date(today) - file.cday AS "Age (Days)",
  length(file.outlinks) AS "Outbound Links"
FROM "03-notes" OR "04-library"
WHERE contains(tags, "#cognitive-science") OR contains(link-up, "cognitive-science-moc")
GROUP BY type
```

```
FLATTEN link-up as mocLink
TABLE 
  rows.file.link AS "Notes",
  rows.maturity AS "Maturity",
  length(rows.file.inlinks) AS "Inbound Links"
FROM "03-notes"
WHERE contains(link-up, "learning-theory-moc")
GROUP BY mocLink
SORT length(rows.file) DESC
```

```
TABLE 
  source,
  confidence,
  status,
  file.cday AS "Created"
FROM "04-library"
WHERE type = "literature" AND contains(tags, "#cognitive-science")
SORT file.cday DESC
```

## Advanced Queries (DataviewJS)

*These DataviewJS examples showcase sophisticated data processing and relationship mapping capabilities.*

### Interconnected Concepts Network Analyzer

**Description:** This query identifies the most interconnected concepts in your PKB by analyzing both inbound and outbound link relationships, calculating a centrality score to highlight key knowledge nodes.

**Top Use Cases:** 
- Finding the most influential concepts in your knowledge base
- Identifying gaps where concepts lack connections
- Prioritizing which notes to develop further based on their network importance

**Tips for Implementation:**
- Adjust the `MIN_LINKS` constant to filter out less connected notes
- Modify the scoring algorithm to weigh inbound vs outbound links differently
- Consider adding date filters to focus on recently created content

**Customization Options:**
- Change the folder scope to focus on specific domains
- Add metadata filters for maturity or confidence levels
- Include tag-based filtering for specific knowledge areas
- Adjust the display limit to show more or fewer results

```dataviewjs
const notes = dv.pages()
  .where(p => p.type === "report" && p.maturity !== "seedling");

const MIN_LINKS = 0;
const networkData = [];

for (const note of notes) {
  const inbound = note.file.inlinks.length;
  const outbound = note.file.outlinks.length;
  const totalLinks = inbound + outbound;
  
  if (totalLinks >= MIN_LINKS) {
    const centrality = (inbound * 0.6) + (outbound * 0.4); // Weight inbound links more heavily
    networkData.push({
      note: note.file.link,
      inbound: inbound,
      outbound: outbound,
      centrality: centrality,
      maturity: note.maturity || "unspecified"
    });
  }
}

dv.table(
  ["Note", "Inbound", "Outbound", "Centrality Score", "Maturity"],
  networkData
    .sort((a, b) => b.centrality - a.centrality)
    .slice(0, 15)
    .map(item => [
      item.note,
      item.inbound,
      item.outbound,
      item.centrality.toFixed(2),
      item.maturity
    ])
);
```

### Cognitive Science Literature Synthesis Tracker

**Description:** This query aggregates and analyzes your cognitive science literature collection, grouping by source type and calculating reading progress while highlighting gaps in your research coverage.

**Top Use Cases:**
- Tracking completion status of literature reviews
- Identifying under-researched areas or sources
- Planning future reading based on publication dates and relevance

**Tips for Implementation:**
- Regularly update the `status` field in your literature notes
- Use consistent tagging for different cognitive subdomains
- Consider adding a "last-reviewed" field for currency tracking

**Customization Options:**
- Filter by specific MOC links for domain-focused analysis
- Add confidence or priority ratings to prioritize readings
- Include word count or page estimates for progress tracking
- Group by publication year or journal for trend analysis

```dataview
const literature = dv.pages('"04-library"')
  .where(p => p.type === "literature" && 
              contains(p.tags, "#cognitive-science"));

const synthesisData = {};
const statusMapping = {
  "not-read": 0,
  "in-progress": 50,
  "read": 100,
  "complete": 100
};

// Group by source and calculate progress
for (const item of literature) {
  const source = item.source || "unspecified";
  const status = item.status || "not-read";
  const progress = statusMapping[status] || 0;
  
  if (!synthesisData[source]) {
    synthesisData[source] = {
      total: 0,
      completed: 0,
      inProgress: 0,
      progressSum: 0,
      items: []
    };
  }
  
  synthesisData[source].total += 1;
  synthesisData[source].progressSum += progress;
  synthesisData[source].items.push({
    title: item.file.link,
    status: status,
    created: item.file.cday,
    confidence: item.confidence || "provisional"
  });
  
  if (progress === 100) synthesisData[source].completed += 1;
  if (progress > 0 && progress < 100) synthesisData[source].inProgress += 1;
}

// Convert to array and sort by completion
const results = Object.entries(synthesisData)
  .map(([source, data]) => ({
    source: source,
    total: data.total,
    completed: data.completed,
    inProgress: data.inProgress,
    avgProgress: (data.progressSum / data.total).toFixed(1),
    items: data.items
  }))
  .sort((a, b) => b.avgProgress - a.avgProgress);

// Display summary table
dv.table(
  ["Source", "Total", "Completed", "In Progress", "Avg Progress %"],
  results.map(r => [
    r.source,
    r.total,
    r.completed,
    r.inProgress,
    r.avgProgress
  ])
);

// Display detailed breakdown for lowest progress sources
const lowProgressSources = results.filter(r => r.avgProgress < 70);
if (lowProgressSources.length > 0) {
  dv.header(3, "Priority Reading - Low Progress Sources");
  
  for (const source of lowProgressSources) {
    dv.header(4, source.source);
    dv.list(source.items
      .sort((a, b) => b.created - a.created) // Newest first
      .map(item => `${item.title} (${item.status}, ${item.confidence})`)
    );
  }
}
```

The error you're encountering:

```
Expected one of the following: 
Not a comment, TABLE or LIST or TASK or CALENDAR, whitespace
```

…is because **you're trying to write JavaScript code directly in a DataviewJS block**, but you're not wrapping it in the correct syntax. In Obsidian, to execute JavaScript code using Dataview, you need to use a **DataviewJS code block** like this:

````markdown
```dataviewjs
// Your JavaScript code here
```
````

Currently, your code appears to be inside a regular code block (probably without the `dataviewjs` language identifier), which makes Dataview try to parse it as a query instead of executing it as JavaScript. That’s why you’re getting a parsing error at the very first line — `const literature = dv.pages(…)` — which is valid **JavaScript**, not a valid **Dataview query**.

---

### ✅ Fix

Wrap your entire script in a ` ```dataviewjs ` block like this:


```dataviewjs
const literature = dv.pages('""')
  .where(p => p.type === "" && 
              dv.func.contains(p.tags, "#"));

const synthesisData = {};
const statusMapping = {
  "not-read": 0,
  "in-progress": 50,
  "read": 100,
  "complete": 100
};

// Group by source and calculate progress
for (const item of literature) {
  const source = item.source || "unspecified";
  const status = item.status || "not-read";
  const progress = statusMapping[status] || 0;
  
  if (!synthesisData[source]) {
    synthesisData[source] = {
      total: 0,
      completed: 0,
      inProgress: 0,
      progressSum: 0,
      items: []
    };
  }
  
  synthesisData[source].total += 1;
  synthesisData[source].progressSum += progress;
  synthesisData[source].items.push({
    title: item.file.link,
    status: status,
    created: item.file.cday,
    confidence: item.confidence || "provisional"
  });
  
  if (progress === 100) synthesisData[source].completed += 1;
  if (progress > 0 && progress < 100) synthesisData[source].inProgress += 1;
}

// Convert to array and sort by completion
const results = Object.entries(synthesisData)
  .map(([source, data]) => ({
    source: source,
    total: data.total,
    completed: data.completed,
    inProgress: data.inProgress,
    avgProgress: (data.progressSum / data.total).toFixed(1),
    items: data.items
  }))
  .sort((a, b) => b.avgProgress - a.avgProgress);

// Display summary table
dv.table(
  ["Source", "Total", "Completed", "In Progress", "Avg Progress %"],
  results.map(r => [
    r.source,
    r.total,
    r.completed,
    r.inProgress,
    r.avgProgress
  ])
);

// Display detailed breakdown for lowest progress sources
const lowProgressSources = results.filter(r => r.avgProgress < 70);
if (lowProgressSources.length > 0) {
  dv.header(3, "Priority Reading - Low Progress Sources");
  
  for (const source of lowProgressSources) {
    dv.header(4, source.source);
    dv.list(source.items
      .sort((a, b) => b.created - a.created) // Newest first
      .map(item => `${item.title} (${item.status}, ${item.confidence})`)
    );
  }
}
```


---

### 🔍 Additional Notes:

1. **Use `dv.func.contains()`**: You used `contains(p.tags, "#cognitive-science")`, but the correct way to call Dataview functions inside `.where()` is via `dv.func.contains(…)`.
2. **Ensure Tags Are Arrays**: Make sure that the `tags` field on your pages is an array (or list-like). If stored as a string, you might need to convert or check accordingly.
3. **Check File Properties**: Ensure `type`, `source`, `status`, and `confidence` are properly set in your note frontmatter/YAML.

---

Let me know if you'd like help simplifying or visualizing this further!


Here's a modified version that reads more broadly and includes additional cognitive science topics:

```dataviewjs
const literature = dv.pages('""')
  .where(p => p.type === "report" && 
              (p.tags && p.tags.some(tag => tag.includes("cognitive-science")) ||
               p.tags && p.tags.some(tag => tag.includes("psychology")) ||
               p.tags && p.tags.some(tag => tag.includes("neuroscience")) ||
               p.tags && p.tags.some(tag => tag.includes("ai")) ||
               p.tags && p.tags.some(tag => tag.includes("machine-learning")) ||
               p.tags && p.tags.some(tag => tag.includes("consciousness")) ||
               p.tags && p.tags.some(tag => tag.includes("memory")) ||
               p.tags && p.tags.some(tag => tag.includes("learning"))));

const synthesisData = {};
const statusMapping = {
  "not-read": 0,
  "in-progress": 50,
  "read": 100,
  "complete": 100
};

// Group by source and calculate progress
for (const item of literature) {
  const source = item.source || item.author || "unspecified";
  const status = item.status || "not-read";
  const progress = statusMapping[status] || 0;
  
  if (!synthesisData[source]) {
    synthesisData[source] = {
      total: 0,
      completed: 0,
      inProgress: 0,
      progressSum: 0,
      items: []
    };
  }
  
  synthesisData[source].total += 1;
  synthesisData[source].progressSum += progress;
  synthesisData[source].items.push({
    title: item.file.link,
    status: status,
    created: item.file.cday,
    confidence: item.confidence || "provisional",
    tags: item.tags || []
  });
  
  if (progress === 100) synthesisData[source].completed += 1;
  if (progress > 0 && progress < 100) synthesisData[source].inProgress += 1;
}

// Convert to array and sort by completion
const results = Object.entries(synthesisData)
  .map(([source, data]) => ({
    source: source,
    total: data.total,
    completed: data.completed,
    inProgress: data.inProgress,
    avgProgress: data.total > 0 ? (data.progressSum / data.total).toFixed(1) : "0.0",
    items: data.items
  }))
  .sort((a, b) => parseFloat(b.avgProgress) - parseFloat(a.avgProgress));

// Display summary table
dv.table(
  ["Source", "Total", "Completed", "In Progress", "Avg Progress %"],
  results.map(r => [
    r.source,
    r.total,
    r.completed,
    r.inProgress,
    r.avgProgress
  ])
);

// Display detailed breakdown for lowest progress sources
const lowProgressSources = results.filter(r => parseFloat(r.avgProgress) < 70);
if (lowProgressSources.length > 0) {
  dv.header(3, "Priority Reading - Low Progress Sources");
  
  for (const source of lowProgressSources) {
    dv.header(4, source.source);
    dv.list(source.items
      .sort((a, b) => b.created - a.created) // Newest first
      .map(item => `${item.title} (${item.status}, ${item.confidence}) [${item.tags.join(", ")}]`)
    );
  }
}
```

Key changes made:
1. **Broader tag matching**: Now includes psychology, neuroscience, AI, machine learning, consciousness, memory, and learning tags
2. **Better source fallback**: Uses author field if source is not available
3. **Safer array handling**: Checks for tag existence before processing
4. **Improved sorting**: More robust parsing of progress values
5. **Enhanced display**: Shows tags in the item listing
6. **Error prevention**: Added safety checks for division and sorting

The script will now capture literature from a wider range of cognitive science-related topics while maintaining the same progress tracking and prioritization features.












## Synergy Queries (with Charts or JS Engine)

*These examples demonstrate how DataviewJS can integrate with visualization plugins to create powerful analytical dashboards.*

### Knowledge Base Maturity & Growth Dashboard

**Description:** This query creates a comprehensive dashboard showing the maturity distribution of your notes over time, with visual charts to identify growth patterns and areas needing attention.

**Top Use Cases:**
- Monitoring the health and development of your PKB
- Identifying imbalances in content maturity levels
- Tracking growth trends to measure PKB development velocity

**Tips for Implementation:**
- Ensure consistent use of the `maturity` field across all notes
- Run this query on a regular dashboard note for ongoing monitoring
- Consider adding filters for specific knowledge domains or tags

**Customization Options:**
- Add time-based filtering to focus on recent growth
- Include confidence levels as additional dimensions
- Break down by note type or source for more granular analysis
- Add targets or benchmarks for maturity distribution goals

```dataviewjs
// Get all notes with maturity data
const allNotes = dv.pages('"03-notes" OR "04-library"')
  .where(p => p.maturity);

// Prepare data for charts
const maturityCounts = {};
const creationTimeline = {};
const maturityTimeline = {};

// Initialize counters
["seedling", "developing", "budding", "evergreen", "needs-review"].forEach(m => {
  maturityCounts[m] = 0;
});

// Process all notes
for (const note of allNotes) {
  const maturity = note.maturity;
  const created = note.file.cday.toFormat("yyyy-MM");
  
  // Count by maturity level
  if (maturityCounts[maturity] !== undefined) {
    maturityCounts[maturity] += 1;
  }
  
  // Build creation timeline
  if (!creationTimeline[created]) creationTimeline[created] = 0;
  creationTimeline[created] += 1;
  
  // Build maturity timeline
  if (!maturityTimeline[created]) {
    maturityTimeline[created] = {};
    ["seedling", "developing", "budding", "evergreen", "needs-review"].forEach(m => {
      maturityTimeline[created][m] = 0;
    });
  }
  if (maturityTimeline[created][maturity] !== undefined) {
    maturityTimeline[created][maturity] += 1;
  }
}

// Create summary table
dv.header(3, "Current Maturity Distribution");
dv.table(
  ["Maturity Level", "Count", "Percentage"],
  Object.entries(maturityCounts)
    .map(([level, count]) => [
      level,
      count,
      ((count / allNotes.length) * 100).toFixed(1) + "%"
    ])
    .sort((a, b) => b[1] - a[1])
);

// Prepare chart data
const months = Object.keys(creationTimeline).sort();
const maturityLevels = ["seedling", "developing", "budding", "evergreen", "needs-review"];

// Creation timeline chart
const creationData = months.map(month => creationTimeline[month]);
dv.header(3, "Note Creation Over Time");
dv.paragraph(`\`\`\`chart
type: line
labels: [${months.map(m => `"${m}"`).join(", ")}]
series:
  - title: Notes Created
    data: [${creationData.join(", ")}]
tension: 0.2
pointSize: 4
\`\`\``);

// Stacked maturity timeline chart
dv.header(3, "Maturity Evolution Over Time");
let chartYAML = "```chart\n";
chartYAML += "type: bar\n";
chartYAML += "labels: [" + months.map(m => `"${m}"`).join(", ") + "]\n";
chartYAML += "series:\n";

maturityLevels.forEach(level => {
  const levelData = months.map(month => 
    maturityTimeline[month] && maturityTimeline[month][level] 
      ? maturityTimeline[month][level] 
      : 0
  );
  chartYAML += `  - title: ${level}\n`;
  chartYAML += `    data: [${levelData.join(", ")}]\n`;
});

chartYAML += "stacked: true\n";
chartYAML += "```\n";
dv.paragraph(chartYAML);

// Growth rate calculation
if (months.length > 1) {
  const firstMonth = months[0];
  const lastMonth = months[months.length - 1];
  const firstCount = creationTimeline[firstMonth] || 0;
  const lastCount = creationTimeline[lastMonth] || 0;
  
  dv.header(3, "Growth Metrics");
  dv.paragraph(`**Growth Rate**: ${(((lastCount - firstCount) / firstCount) * 100).toFixed(1)}%`);
  dv.paragraph(`**Average Monthly Growth**: ${((allNotes.length / months.length).toFixed(1))} notes/month`);
}
```








The error is caused by the `return` statement outside of a function. Here's the corrected version:

```dataviewjs
// Get all cognitive science literature from the library
const literature = dv.pages('""')
  .where(p => p.type === "literature" && 
        p.tags && p.tags.includes("#cognitive-science") && 
        p.source);

// Check if we have literature to analyze
if (literature.length === 0) {
  dv.paragraph("No cognitive science literature found in the library.");
} else {
  // Track metrics for each source
  const sourceMetrics = {};

  // Process each literature item
  for (const item of literature) {
    const source = item.source;
    const confidence = item.confidence || "provisional";
    const status = item.status || "not-read";
    const dateAdded = item.dateAdded || item.created || "Unknown";
    
    // Initialize tracking for this source if needed
    if (!sourceMetrics[source]) {
      sourceMetrics[source] = {
        count: 0,
        totalConfidence: 0,
        confidences: [],
        statuses: [],
        items: []
      };
    }
    
    // Update our tracking data
    sourceMetrics[source].count += 1;
    sourceMetrics[source].confidences.push(confidence);
    sourceMetrics[source].statuses.push(status);
    sourceMetrics[source].items.push({
      title: item.file.name,
      confidence: confidence,
      status: status,
      date: dateAdded
    });
    
    // Convert confidence levels to numbers (speculative=1, high=5)
    const confidenceValues = {
      "speculative": 1,
      "provisional": 2,
      "moderate": 3,
      "established": 4,
      "high": 5
    };
    sourceMetrics[source].totalConfidence += confidenceValues[confidence] || 2;
  }

  // Prepare data for charts
  const sources = Object.keys(sourceMetrics);
  const sourceCounts = sources.map(s => sourceMetrics[s].count);
  const avgConfidences = sources.map(s => 
    (sourceMetrics[s].totalConfidence / sourceMetrics[s].count).toFixed(2)
  );

  // Count how many items exist at each confidence level
  const confidenceLevels = ["speculative", "provisional", "moderate", "established", "high"];
  const confidenceData = confidenceLevels.map(level => 
    sources.reduce((sum, source) => 
      sum + sourceMetrics[source].confidences.filter(c => c === level).length, 0)
  );

  // Generate Report Header
  dv.header(2, "Cognitive Science Literature Report");
  dv.paragraph(`*Generated on ${dv.date('yyyy-MM-dd')}*`);
  dv.paragraph(`**Total Literature Items:** ${literature.length}`);
  dv.paragraph(`**Sources Analyzed:** ${sources.length}`);

  // Show literature distribution by source
  dv.header(3, "1. Literature Distribution by Source");
  dv.paragraph(`This chart shows how literature is distributed across different sources.`);
  dv.paragraph(`\`\`\`chart
type: pie
labels: [${sources.map(s => `"${s}"`).join(", ")}]
series:
  - data: [${sourceCounts.join(", ")}]
\`\`\``);

  // Show average confidence by source
  dv.header(3, "2. Average Confidence by Source");
  dv.paragraph(`This chart shows the average confidence level for each source (1=speculative, 5=high).`);
  dv.paragraph(`\`\`\`chart
type: bar
labels: [${sources.map(s => `"${s}"`).join(", ")}]
series:
  - data: [${avgConfidences.join(", ")}]
\`\`\``);

  // Show distribution of confidence levels
  dv.header(3, "3. Confidence Level Distribution");
  dv.paragraph(`This chart shows the overall distribution of confidence levels across all literature.`);
  dv.paragraph(`\`\`\`chart
type: doughnut
labels: [${confidenceLevels.map(l => `"${l}"`).join(", ")}]
series:
  - data: [${confidenceData.join(", ")}]
\`\`\``);

  // Detailed analysis of each source
  dv.header(3, "4. Source Quality Analysis");
  dv.paragraph(`Detailed breakdown of each source's performance and content distribution.`);

  const sourceAnalysis = sources.map(source => {
    const metrics = sourceMetrics[source];
    const avgConf = (metrics.totalConfidence / metrics.count).toFixed(2);
    
    // Count how many items have each status
    const statusCounts = {};
    metrics.statuses.forEach(status => {
      statusCounts[status] = (statusCounts[status] || 0) + 1;
    });
    
    return {
      source: source,
      count: metrics.count,
      avgConfidence: avgConf,
      statusDistribution: statusCounts,
      items: metrics.items
    };
  }).sort((a, b) => parseFloat(b.avgConfidence) - parseFloat(a.avgConfidence));

  dv.table(
    ["Source", "Count", "Avg Confidence", "Status Distribution"],
    sourceAnalysis.map(s => [
      s.source,
      s.count,
      s.avgConfidence,
      Object.entries(s.statusDistribution).map(([status, count]) => 
        `${status}: ${count}`).join(", ")
    ])
  );

  // Top performing sources
  dv.header(3, "5. High-Performing Sources");
  const highValueSources = sourceAnalysis.filter(s => parseFloat(s.avgConfidence) >= 4.0);
  if (highValueSources.length > 0) {
    dv.paragraph("These sources consistently provide high-confidence information:");
    dv.list(highValueSources.map(s => `${s.source} (Avg Confidence: ${s.avgConfidence})`));
  } else {
    dv.paragraph("No high-performing sources identified (confidence >= 4.0).");
  }

  // Sources needing review
  dv.header(3, "6. Sources Requiring Review");
  const lowValueSources = sourceAnalysis.filter(s => parseFloat(s.avgConfidence) < 2.5);
  if (lowValueSources.length > 0) {
    dv.paragraph("These sources may need quality evaluation:");
    dv.list(lowValueSources.map(s => `${s.source} (Avg Confidence: ${s.avgConfidence})`));
  } else {
    dv.paragraph("All sources meet minimum quality standards (confidence >= 2.5).");
  }

  // Detailed item listings by source
  dv.header(3, "7. Detailed Source Breakdown");
  dv.paragraph("Individual items organized by source for detailed review.");

  for (const sourceData of sourceAnalysis) {
    dv.header(4, `${sourceData.source} (Items: ${sourceData.count})`);
    
    // Group items by confidence level
    const itemsByConfidence = {};
    sourceData.items.forEach(item => {
      if (!itemsByConfidence[item.confidence]) {
        itemsByConfidence[item.confidence] = [];
      }
      itemsByConfidence[item.confidence].push(item);
    });
    
    // Display items grouped by confidence
    Object.keys(itemsByConfidence).forEach(confidence => {
      dv.header(5, `Confidence: ${confidence}`);
      dv.list(itemsByConfidence[confidence].map(item => 
        `${item.title} (${item.status})`
      ));
    });
  }

  // Summary recommendations
  dv.header(3, "8. Summary Recommendations");
  dv.paragraph("**Key Insights:**");
  dv.list([
    `Total literature items analyzed: ${literature.length}`,
    `Number of sources: ${sources.length}`,
    `Overall average confidence: ${(confidenceData.reduce((sum, count, i) => 
       sum + count * (i + 1), 0) / literature.length).toFixed(2)}`,
    `High-performing sources: ${highValueSources.length}`,
    `Sources needing review: ${lowValueSources.length}`
  ]);

  dv.paragraph("**Action Items:**");
  const recommendations = [];
  if (highValueSources.length > 0) {
    recommendations.push(`Prioritize literature from high-performing sources: ${highValueSources.map(s => s.source).join(", ")}`);
  }
  if (lowValueSources.length > 0) {
    recommendations.push(`Review or replace low-performing sources: ${lowValueSources.map(s => s.source).join(", ")}`);
  }
  recommendations.push("Continue monitoring source quality metrics");
  recommendations.push("Consider diversifying sources if concentration is too high");

  dv.list(recommendations);
}
```

### Key fixes:
1. **Removed the illegal `return` statement** and replaced it with an `else` block
2. **Wrapped all the main logic** in the `else` block so it only runs when there's data
3. **Maintained all the report functionality** while fixing the syntax error

Now the script will work properly in DataviewJS without syntax errors.










## 🚀 Simple Queries (DQL)

```
LIST FROM #project
```

```
TABLE status, priority, due FROM "Projects" SORT due ASC
```

```
TASK FROM "Projects" WHERE contains(text, "client") AND !completed
```

```
LIST file.name WHERE project-status = "active"
```

---

## 🛠️ Intermediate Queries (DQL)

```
TABLE length(filter(file.outlinks, (x) => contains(x, "meeting"))) AS MeetingLinks, priority 
FROM #project 
WHERE status = "in-progress"
```

```
TABLE date(today) - file.cday AS DaysActive, budget-used/budget AS PercentUsed 
FROM "Projects" 
SORT DaysActive DESC
```

```
FLATTEN list(stakeholders, team-members) AS People 
FROM #project 
WHERE contains(People, "john")
```

```
TABLE rows.file.name AS Projects, rows.budget AS Budgets 
FROM #project 
GROUP BY department 
SORT sum(rows.budget) DESC
```

---


You're encountering a **SyntaxError: Invalid or unexpected token** in your DataviewJS script. This error typically indicates an issue with the code syntax that JavaScript cannot parse — often due to invisible characters (like non-breaking spaces), incorrect quotes, or invalid operators.

Let’s go through and **fix the issues** step-by-step:

---

### ✅ Fixed Version of Your Script

```javascript
const { DateTime, Duration } = dv.luxon;

// Get projects with milestones
let projectsWithMilestones = dv.pages("#project")
  .filter(p => p.milestones || p.due)
  .map(p => {
    let milestones = [];
    if (p.milestones && Array.isArray(p.milestones)) {
      milestones = p.milestones.map((m, i) => ({
        name: typeof m === 'object' ? m.name : `Milestone ${i + 1}`,
        date: typeof m === 'object' ? dv.date(m.date) : dv.date(m),
        completed: typeof m === 'object' ? (m.completed || false) : false,
        project: p.file.link
      }));
    }
    // Add due date as final milestone if exists
    if (p.due) {
      milestones.push({
        name: "Project Due",
        date: p.due,
        completed: p.status === "completed",
        project: p.file.link
      });
    }
    return { …p, processedMilestones: milestones };
  });

// Flatten all milestones
let allMilestones = projectsWithMilestones.flatMap(p => p.processedMilestones || [])
  .filter(m => m.date)
  .sort((a, b) => a.date.ts - b.date.ts); // Fixed: compare timestamps directly

// Upcoming milestones (next 30 days)
dv.header(3, "📅 Upcoming Milestones (Next 30 Days)");
let upcoming = allMilestones.filter(m => {
  let daysDiff = Duration.fromMillis(m.date.ts - Date.now()).as('days');
  return daysDiff >= 0 && daysDiff <= 30;
});

if (upcoming.length > 0) {
  dv.table(
    ["Date", "Milestone", "Project", "Status"],
    upcoming.map(m => [
      m.date.toFormat('yyyy-MM-dd'),
      m.name,
      m.project,
      m.completed ? "✅ Completed" : "⏳ Pending"
    ])
  );
} else {
  dv.paragraph("No upcoming milestones in the next 30 days.");
}

// Milestone completion statistics
dv.header(3, "📊 Milestone Completion");
let pastMilestones = allMilestones.filter(m => m.date.ts < Date.now());
if (pastMilestones.length > 0) {
  let completedCount = pastMilestones.filter(m => m.completed).length;
  let completionRate = (completedCount / pastMilestones.length) * 100;

  dv.paragraph(`Overall milestone completion: ${completionRate.toFixed(1)}% (${completedCount}/${pastMilestones.length})`);

  // Group by time periods
  let thisWeek = pastMilestones.filter(m => {
    let weekAgo = DateTime.now().minus({ weeks: 1 });
    return m.date >= weekAgo;
  });
  if (thisWeek.length > 0) {
    let weekRate = (thisWeek.filter(m => m.completed).length / thisWeek.length) * 100;
    dv.paragraph(`This week's completion rate: ${weekRate.toFixed(1)}%`);
  }
}

// Critical path projects (closest to due dates)
dv.header(3, "🚨 Critical Path Projects");
let criticalProjects = projectsWithMilestones
  .filter(p => p.due && !p.completed)
  .map(p => ({
    project: p.file.link,
    daysToDue: Math.floor(Duration.fromMillis(p.due.ts - Date.now()).as('days')),
    priority: p.priority || 'medium'
  }))
  .filter(p => p.daysToDue < 60) // Projects due within 60 days
  .sort((a, b) => a.daysToDue - b.daysToDue); // Fixed: correct sort usage

if (criticalProjects.length > 0) {
  dv.table(
    ["Project", "Days to Due", "Priority"],
    criticalProjects.map(p => [
      p.project,
      p.daysToDue,
      p.priority.charAt(0).toUpperCase() + p.priority.slice(1)
    ])
  );
} else {
  dv.paragraph("No critical projects requiring immediate attention.");
}
```

---

### 🔧 Key Fixes Made

1. **Invalid Spread Operator Syntax:**
   ```js
   return {…p, processedMilestones: milestones};
   ```
   ➜ Changed to valid JS:
   ```js
   return { …p, processedMilestones: milestones };
   ```

2. **Incorrect Sort Usage:**
   ```js
   .sort(p => p.daysToDue, 'asc');
   ```
   ➜ Fixed to:
   ```js
   .sort((a, b) => a.daysToDue - b.daysToDue);
   ```

3. **Typo in Paragraph Output:**
   ```js
   dv.paragraph(`Overall milestone completion: ${completionRate.toFixed(1)}% ($/${pastMilestones.length})`);
   ```
   ➜ Should be:
   ```js
   dv.paragraph(`Overall milestone completion: ${completionRate.toFixed(1)}% (${completedCount}/${pastMilestones.length})`);
   ```

4. **Ensure Consistent Date Comparisons:**
   ```js
   .sort((a, b) => a.date - b.date);
   ```
   ➜ Should use `.ts` for Luxon DateTime comparisons:
   ```js
   .sort((a, b) => a.date.ts - b.date.ts);
   ```

---

### 🛠 Tips to Avoid These Errors in the Future

- Use a proper code editor like VS Code when writing DataviewJS scripts.
- Enable **"Show Invisible Characters"** to catch weird spacing.
- Always test small parts of the script incrementally.
- Use `try/catch` blocks during development to isolate errors.

---

Let me know if you want this converted into a reusable component or need help formatting it for Obsidian!























































