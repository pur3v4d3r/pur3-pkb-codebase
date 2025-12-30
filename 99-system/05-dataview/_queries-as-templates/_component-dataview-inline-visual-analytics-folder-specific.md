### Vault Activity 90 Days [Searches by Created File Date]

```dataviewjs
/** * 📊 SYSTEM: Folder Activity Visualizer (03-notes)
 * REQUIRES: 'Charts' Plugin
 * * SCOPE: Only files inside the target folder.
 * * DATA: file.mtime (Last Modified Date)
 */

// --- CONFIGURATION ---
// ⚠️ UPDATE this to match your folder path exactly
const targetFolder = '"03-notes"'; 

const daysBack = 90; 
// ---------------------

// 1. Gather Data (Restricted Scope)
// We pass the folder path directly into dv.pages()
let pages = dv.pages(targetFolder);

// 2. Group Data (Targeting Modification Date)
// Uses native Luxon formatting to prevent date errors
const noteGroups = pages.groupBy(p => p.file.mtime.toFormat('yyyy-MM-dd'));

// Create dictionary for fast lookups
let dateCounts = {};
for (let group of noteGroups) {
    dateCounts[group.key] = group.rows.length;
}

// 3. Build Timeline (Backwards from today)
let labels = [];
let data = [];
let totalActivity = 0;

for (let i = daysBack; i >= 0; i--) {
    const dateObj = dv.date("now").minus({ days: i });
    const dateKey = dateObj.toFormat('yyyy-MM-dd');
    const displayLabel = dateObj.toFormat('MMM d'); 
    
    const count = dateCounts[dateKey] || 0;
    
    labels.push(displayLabel);
    data.push(count);
    totalActivity += count;
}

// 4. Render Header
// We strip quotes from the folder name for a cleaner title
const cleanFolderName = targetFolder.replace(/"/g, '');
dv.header(3, `📂 Activity in ${cleanFolderName}: Last ${daysBack} Days`);
dv.paragraph(`**${totalActivity}** files worked on in this folder.`);

// 5. Render Chart
const chartData = {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: `${cleanFolderName} Activity`,
            data: data,
            backgroundColor: ['rgba(54, 162, 235, 0.2)'], // Blue
            borderColor: ['rgba(54, 162, 235, 1)'],
            borderWidth: 2,
            pointRadius: 1,
            tension: 0.4,
            fill: true
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: { 
                beginAtZero: true, 
                ticks: { stepSize: 1 } 
            },
            x: { 
                ticks: { maxTicksLimit: 15 } 
            }
        }
    }
};

window.renderChart(chartData, this.container);
```

```dataviewjs
/** * 📊 SYSTEM: Folder Growth Visualizer (03-notes)
 * REQUIRES: 'Charts' Plugin
 * * SCOPE: Only files inside the target folder.
 * * DATA: file.ctime (Creation Date)
 * * VISUAL: Purple (to distinguish from Blue Activity chart)
 */

// --- CONFIGURATION ---
const targetFolder = '"03-notes"'; 
const daysBack = 90; 
// ---------------------

// 1. Gather Data (Restricted Scope)
let pages = dv.pages(targetFolder);

// 2. Group Data (Targeting Creation Date)
// We use the robust Luxon fix: p.file.ctime
const noteGroups = pages.groupBy(p => p.file.ctime.toFormat('yyyy-MM-dd'));

// Create dictionary
let dateCounts = {};
for (let group of noteGroups) {
    dateCounts[group.key] = group.rows.length;
}

// 3. Build Timeline
let labels = [];
let data = [];
let totalNew = 0;

for (let i = daysBack; i >= 0; i--) {
    const dateObj = dv.date("now").minus({ days: i });
    const dateKey = dateObj.toFormat('yyyy-MM-dd');
    const displayLabel = dateObj.toFormat('MMM d'); 
    
    const count = dateCounts[dateKey] || 0;
    
    labels.push(displayLabel);
    data.push(count);
    totalNew += count;
}

// 4. Render Header
const cleanFolderName = targetFolder.replace(/"/g, '');
dv.header(3, `🌱 New Growth in ${cleanFolderName}: Last ${daysBack} Days`);
dv.paragraph(`**${totalNew}** new notes created in this folder.`);

// 5. Render Chart
const chartData = {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: `${cleanFolderName} Growth`,
            data: data,
            backgroundColor: ['rgba(142, 68, 173, 0.2)'], // Purple for "Creation"
            borderColor: ['rgba(142, 68, 173, 1)'],
            borderWidth: 2,
            pointRadius: 1,
            tension: 0.4,
            fill: true
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: { 
                beginAtZero: true, 
                ticks: { stepSize: 1 } 
            },
            x: { 
                ticks: { maxTicksLimit: 15 } 
            }
        }
    }
};

window.renderChart(chartData, this.container);
```