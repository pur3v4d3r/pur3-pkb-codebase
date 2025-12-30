/**
 * Cleanup Duplicate Review Properties
 *
 * One-time script to remove duplicate review-* properties.
 * Keeps only the FIRST occurrence of each property.
 *
 * Usage: Run once via Templater
 * <%* await tp.user["cleanup-duplicate-review-properties"](tp) %>
 */

async function cleanupDuplicateReviewProperties(tp) {
    const confirm = await tp.system.prompt(
        "⚠️ CLEANUP DUPLICATE REVIEW PROPERTIES\n\nThis will remove duplicate review-* properties, keeping only the first occurrence.\n\nType 'yes' to continue:",
        "no"
    );

    if (confirm.toLowerCase() !== "yes") {
        return "❌ Cleanup cancelled.";
    }

    let stats = {
        totalScanned: 0,
        cleaned: 0,
        skipped: 0
    };

    // Find all notes in permanent notes folder
    const allNotes = app.vault.getMarkdownFiles()
        .filter(file =>
            file.path.includes("03-notes/01_permanent-notes") ||
            file.path.includes("permanent-notes")
        );

    stats.totalScanned = allNotes.length;
    new Notice(`🔄 Scanning ${allNotes.length} notes...`);

    for (const file of allNotes) {
        try {
            const content = await app.vault.read(file);
            const yamlRegex = /^---\n([\s\S]*?)\n---/;
            const match = content.match(yamlRegex);

            if (!match) {
                stats.skipped++;
                continue;
            }

            let yamlContent = match[1];
            let cleaned = false;

            // For each review property, keep only the first occurrence
            const reviewProps = [
                'review-last-reviewed',
                'review-next-review',
                'review-count',
                'review-interval',
                'review-priority'
            ];

            for (const prop of reviewProps) {
                const regex = new RegExp(`^${prop}:.*$`, 'gm');
                const matches = yamlContent.match(regex);

                if (matches && matches.length > 1) {
                    // Found duplicates - keep first, remove rest
                    const firstMatch = matches[0];
                    yamlContent = yamlContent.replace(regex, ''); // Remove all
                    yamlContent = yamlContent + '\n' + firstMatch; // Add back first one
                    cleaned = true;
                }
            }

            if (cleaned) {
                const newContent = content.replace(yamlRegex, `---\n${yamlContent}\n---`);
                await app.vault.modify(file, newContent);
                stats.cleaned++;
            } else {
                stats.skipped++;
            }

        } catch (error) {
            console.error(`Error processing ${file.path}:`, error);
        }
    }

    const report = `
✅ CLEANUP COMPLETE

📊 Statistics:
- Total Scanned: ${stats.totalScanned}
- Files Cleaned: ${stats.cleaned}
- Files Skipped: ${stats.skipped}

✅ Duplicate properties removed!
`;

    new Notice("✅ Cleanup complete!");
    console.log(report);
    return report;
}

module.exports = cleanupDuplicateReviewProperties;
