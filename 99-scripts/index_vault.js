/**
 * Title: Direct-to-Vault Emoji Indexer
 * Description: Generates a Markdown tree and saves it directly to a specific file.
 */

const fs = require('fs');
const path = require('path');

// [**Configuration-Block**]
const CONFIG = {
    // 1. Where to scan ('.' means the folder this script is in)
    targetDir: './', 
    
    // 2. WHERE TO SAVE THE FILE
    // We use double quotes and double backslashes for Windows path safety
    outputFile: "D:\\10_pur3v4d3r's-vault\\.claude\\folder-index.md",

    ignore: ['.git', 'node_modules', '.obsidian', '.trash', '.DS_Store', 'Thumbs.db', '.venv'],
    depthLimit: 10,
    includeSummary: true
};

// Global buffer to store the text before writing
let outputBuffer = "";

// Helper to append text instead of printing it
function log(text) {
    outputBuffer += text + "\n";
}

function getFileIcon(filename) {
    const ext = path.extname(filename).toLowerCase();
    const icons = {
        '.jpg': '📷', '.jpeg': '📷', '.png': '🖼️', '.gif': '🎞️',
        '.arw': '📸', '.dng': '📸', // RAW
        '.md': '📝', '.txt': '📄', '.pdf': '📕', 
        '.js': '📜', '.json': '⚙️', '.css': '🎨', 
        '.mp4': '🎬', '.zip': '📦'
    };
    return icons[ext] || '📎';
}

let stats = { files: 0, folders: 0, totalSize: 0 };

function walk(dir, depth = 0) {
    if (depth > CONFIG.depthLimit) return;

    let list;
    try { list = fs.readdirSync(dir); } catch (e) { return; }

    // Sort: Folders first
    list.sort((a, b) => {
        const pathA = path.join(dir, a);
        const pathB = path.join(dir, b);
        try {
            const isDirA = fs.statSync(pathA).isDirectory();
            const isDirB = fs.statSync(pathB).isDirectory();
            if (isDirA === isDirB) return a.toLowerCase().localeCompare(b.toLowerCase());
            return isDirA ? -1 : 1;
        } catch (e) { return 0; }
    });

    list.forEach(file => {
        if (CONFIG.ignore.includes(file)) return;
        // Avoid indexing the output file itself
        if (path.resolve(path.join(dir, file)) === path.resolve(CONFIG.outputFile)) return;

        const fullPath = path.join(dir, file);
        let fileStat;
        try { fileStat = fs.statSync(fullPath); } catch (e) { return; }

        const indent = '  '.repeat(depth);

        if (fileStat.isDirectory()) {
            stats.folders++;
            log(`${indent}- 📂 **${file}**`);
            walk(fullPath, depth + 1);
        } else {
            stats.files++;
            stats.totalSize += fileStat.size;
            const icon = getFileIcon(file);
            
            // Convert to relative path from the Output File location if needed, 
            // or use absolute file:/// links. Here we use Web-Standard absolute paths.
            const webPath = fullPath.split(path.sep).join('/');
            
            log(`${indent}- ${icon} [${file}](${encodeURI(webPath)})`);
        }
    });
}

// --- Execution ---

console.log("⏳ Generating Index...");

// Header
log(`# 🗺️ Index of: ${path.resolve(CONFIG.targetDir)}`);
log(`> [!abstract] Generated on ${new Date().toLocaleString()}\n`);

// Run the walker
walk(CONFIG.targetDir);

// Footer
if (CONFIG.includeSummary) {
    const sizeMB = (stats.totalSize / (1024 * 1024)).toFixed(2);
    log(`\n---\n### 📊 Summary Statistics`);
    log(`- **Total Folders:** ${stats.folders}`);
    log(`- **Total Files:** ${stats.files}`);
    log(`- **Total Volume:** ${sizeMB} MB`);
}

// [**Write-Operation**:: The final step where the accumulated buffer is flushed to the hard drive.]
try {
    // Ensure the directory exists before writing
    const outputDir = path.dirname(CONFIG.outputFile);
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    fs.writeFileSync(CONFIG.outputFile, outputBuffer, 'utf8');
    console.log(`✅ Success! Index saved to: \n${CONFIG.outputFile}`);
} catch (err) {
    console.error("❌ Error writing file:", err.message);
}