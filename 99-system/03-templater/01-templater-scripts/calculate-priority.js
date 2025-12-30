/**
 * Calculate Priority
 *
 * Auto-calculates review priority based on:
 * - Backlink count (high connectivity = higher priority)
 * - Days since last modified (recent edits = higher priority)
 * - Tag importance (MOCs, domain tags = higher priority)
 * - Explicit review tags
 *
 * Can be called from Templater templates using:
 * <% tp.user.calculate-priority(tp, file) %>
 *
 * @param {object} tp - Templater object
 * @param {object} file - File object (tp.file or specific file)
 * @returns {string} Priority level: urgent, high, medium, or low
 */

async function calculatePriority(tp, file = null) {
    // Use current file if none specified
    if (!file) {
        file = tp.file;
    }

    // Get file path
    const filePath = file.path || tp.file.path(true);

    // Get file metadata from cache
    const cache = app.metadataCache.getFileCache(app.vault.getAbstractFileByPath(filePath));
    const frontmatter = cache?.frontmatter || {};

    // Get tags
    const tags = frontmatter.tags || [];
    const tagsString = Array.isArray(tags) ? tags.join(" ") : tags;

    // Check for urgent tags
    const hasUrgentTag = tagsString.includes("needs-review") ||
                        tagsString.includes("urgent") ||
                        tagsString.includes("critical");

    if (hasUrgentTag) {
        return "urgent";
    }

    // Get backlinks
    const fileObj = app.vault.getAbstractFileByPath(filePath);
    const backlinks = app.metadataCache.getBacklinksForFile(fileObj);
    const backlinkCount = backlinks?.data ? Object.keys(backlinks.data).length : 0;

    // Check for MOC or high-importance tags
    const hasMOCTag = tagsString.includes("type/moc");
    const hasDomainTag = tagsString.includes("cognitive-science") ||
                        tagsString.includes("pkm") ||
                        tagsString.includes("pkb") ||
                        tagsString.includes("philosophy");

    // Days since last modified
    const fileStats = await app.vault.adapter.stat(filePath);
    const lastModified = fileStats?.mtime || Date.now();
    const daysSinceModified = Math.floor((Date.now() - lastModified) / (1000 * 60 * 60 * 24));

    // Priority scoring logic
    let score = 0;

    // Backlink score (0-3 points)
    if (backlinkCount > 20) score += 3;
    else if (backlinkCount > 10) score += 2;
    else if (backlinkCount > 5) score += 1;

    // Tag importance score (0-2 points)
    if (hasMOCTag) score += 2;
    else if (hasDomainTag) score += 1;

    // Recency score (0-2 points)
    if (daysSinceModified <= 7) score += 2;
    else if (daysSinceModified <= 30) score += 1;

    // Determine priority based on score
    if (score >= 6) {
        return "high";
    } else if (score >= 3) {
        return "medium";
    } else {
        return "low";
    }
}

module.exports = calculatePriority;
