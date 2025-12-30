### Vault Activity 90 Days [Searches by Created File Date]

```dataviewjs
/** * 📊 SYSTEM: Vault Pulse Visualizer (Luxon Native Fix)
 * REQUIRES: 'Charts' Plugin
 * * FIX APPLIED: 
 * - Removed Moment.js wrappers around file dates.
 * - Uses Dataview's native .toFormat() method to read real file dates.
 */

// --- CONFIGURATION ---
const daysBack = 90; 
const showTemplates = false; 
const showSystem = false;
// ---------------------

// 1. Gather Data
let pages = dv.pages();
if (!showTemplates) pages = pages.where(p => !p.file.path.includes("Templates"));
if (!showSystem)    pages = pages.where(p => !p.file.path.includes("System"));

// 2. Group Data (Using Native Dataview/Luxon Formatting)
// We use p.file.ctime.toFormat() which reads the actual Dataview date object directly
const noteGroups = pages.groupBy(p => p.file.ctime.toFormat('yyyy-MM-dd'));

// Create dictionary for fast lookups
let dateCounts = {};
for (let group of noteGroups) {
    dateCounts[group.key] = group.rows.length;
}

// 3. Build Timeline (Backwards from today)
let labels = [];
let data = [];
let totalNotes = 0;

// We use Luxon for the timeline loop to match the file format perfectly
for (let i = daysBack; i >= 0; i--) {
    // Calculate the date i days ago
    const dateObj = dv.date("now").minus({ days: i });
    const dateKey = dateObj.toFormat('yyyy-MM-dd');
    const displayLabel = dateObj.toFormat('MMM d'); // e.g. "Oct 23"
    
    const count = dateCounts[dateKey] || 0;
    
    labels.push(displayLabel);
    data.push(count);
    totalNotes += count;
}

// 4. Render Header
dv.header(3, `🌟 Vault Momentum: Last ${daysBack} Days`);
dv.paragraph(`**${totalNotes}** new notes created in this period.`);

// 5. Render Chart
const chartData = {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'New Notes',
            data: data,
            backgroundColor: ['rgba(142, 68, 173, 0.2)'], 
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


### Vault Activity 90 Days [Searches by Modified File Date]

```dataviewjs
/** * 📊 SYSTEM: Vault Activity Visualizer (Modified Date)
 * REQUIRES: 'Charts' Plugin
 * * DATA SOURCE: file.mtime (Last Modified Date)
 * * LOGIC: Uses native Luxon formatting to ensure date accuracy.
 */

// --- CONFIGURATION ---
const daysBack = 90; 
const showTemplates = false; 
const showSystem = false;
// ---------------------

// 1. Gather Data
let pages = dv.pages();
if (!showTemplates) pages = pages.where(p => !p.file.path.includes("Templates"));
if (!showSystem)    pages = pages.where(p => !p.file.path.includes("System"));

// 2. Group Data (Targeting Modification Date)
// We use p.file.mtime instead of ctime to track when you last worked on a file
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
    // Calculate the date i days ago
    const dateObj = dv.date("now").minus({ days: i });
    const dateKey = dateObj.toFormat('yyyy-MM-dd');
    const displayLabel = dateObj.toFormat('MMM d'); 
    
    const count = dateCounts[dateKey] || 0;
    
    labels.push(displayLabel);
    data.push(count);
    totalActivity += count;
}

// 4. Render Header
dv.header(3, `📉 Vault Activity: Last ${daysBack} Days`);
dv.paragraph(`**${totalActivity}** files modified/worked on in this period.`);

// 5. Render Chart
const chartData = {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Files Modified',
            data: data,
            backgroundColor: ['rgba(54, 162, 235, 0.2)'], // Switched to Blue for "Activity"
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