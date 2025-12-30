The "Content Taxonomy" (Doughnut Chart)

**The Question:** *"What am I actually writing about?"*
**The Logic:** This scans your tags. It ignores nested tags (like `#type/note`) and groups by the **Root Tag** (e.g., `#type`) to show you the high-level distribution of your knowledge base.

```dataviewjs
/** * 📊 SYSTEM: Content Taxonomy Visualizer
 * REQUIRES: 'Charts' Plugin
 * * LOGIC: Flattens all tags, extracts the ROOT tag (before the first slash),
 * * and visualizes the distribution.
 */

// --- CONFIGURATION ---
const ignoreTags = ["#excalidraw", "#todo"]; // Tags to hide
// ---------------------

// 1. Gather and Process Tags
const pages = dv.pages("");
let tagCounts = {};

pages.forEach(p => {
    if (p.file.tags) {
        p.file.tags.forEach(t => {
            // Filter ignored tags
            if (ignoreTags.includes(t)) return;
            
            // Extract Root Tag (e.g., "#journal/daily" -> "#journal")
            // If no slash, keeps the whole tag.
            let root = t.split("/")[0];
            
            if (tagCounts[root]) {
                tagCounts[root]++;
            } else {
                tagCounts[root] = 1;
            }
        });
    }
});

// 2. Sort Data (Largest slices first)
const sortedTags = Object.entries(tagCounts)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10); // Limit to Top 10 to prevent clutter

const labels = sortedTags.map(t => t[0]);
const data = sortedTags.map(t => t[1]);

// 3. Render Chart
const chartData = {
    type: 'doughnut',
    data: {
        labels: labels,
        datasets: [{
            data: data,
            backgroundColor: [
                'rgba(255, 99, 132, 0.6)',
                'rgba(54, 162, 235, 0.6)',
                'rgba(255, 206, 86, 0.6)',
                'rgba(75, 192, 192, 0.6)',
                'rgba(153, 102, 255, 0.6)',
                'rgba(255, 159, 64, 0.6)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        plugins: {
            legend: { position: 'right' },
            title: { display: true, text: 'Top 10 Knowledge Categories' }
        }
    }
};

window.renderChart(chartData, this.container);
```

