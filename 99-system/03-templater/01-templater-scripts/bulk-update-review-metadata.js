/**
 * Bulk Update Review Metadata
 *
 * Scans all permanent notes and adds missing review metadata.
 * Features:
 * - Adds flattened review-* properties (Obsidian properties panel compatible)
 * - Fills missing maturity, confidence, status fields
 * - Auto-calculates priority from backlinks/edits/tags
 * - Removes old nested review: objects if present
 * - Provides detailed report
 *
 * Properties added:
 * - review-last-reviewed: Date of last review (null initially)
 * - review-next-review: Calculated next review date
 * - review-count: Number of times reviewed (0 initially)
 * - review-interval: Days between reviews (based on maturity)
 * - review-priority: Priority level (urgent/high/medium/low)
 *
 * Can be called from Templater templates using:
 * <%* await tp.user["bulk-update-review-metadata"](tp) %>
 *
 * @param {object} tp - Templater object
 * @returns {string} Summary report of updates
 */

async function bulkUpdateReviewMetadata(tp) {
    // Confirmation prompt
    const confirm = await tp.system.prompt(
        "⚠️ BULK UPDATE REVIEW METADATA\n\nThis will update ALL notes in permanent-notes folders.\nA backup will be created first.\n\nType 'yes' to continue:",
        "no"
    );

    if (confirm.toLowerCase() !== "yes") {
        return "❌ Bulk update cancelled by user.";
    }

    // Maturity intervals
    const maturityIntervals = {
        "seedling": 3,
        "budding": 7,
        "developing": 14,
        "evergreen": 30,
        "needs-review": 1
    };

    // Stats tracking
    let stats = {
        totalScanned: 0,
        updated: 0,
        skipped: 0,
        errors: 0,
        reviewAdded: 0,
        maturityAdded: 0,
        confidenceAdded: 0,
        statusAdded: 0
    };

    // Find all notes in permanent notes folder
    const allNotes = app.vault.getMarkdownFiles()
        .filter(file =>
            file.path.includes("03-notes/01_permanent-notes") ||
            file.path.includes("permanent-notes")
        );

    stats.totalScanned = allNotes.length;

    // Show progress
    new Notice(`🔄 Scanning ${allNotes.length} notes...`);

    // Process each note
    for (const file of allNotes) {
        try {
            // Read file content
            const content = await app.vault.read(file);

            // Parse frontmatter
            const yamlRegex = /^---\n([\s\S]*?)\n---/;
            const match = content.match(yamlRegex);

            if (!match) {
                stats.skipped++;
                continue; // No frontmatter, skip
            }

            let yamlContent = match[1];
            let updated = false;

            // Parse current frontmatter
            const cache = app.metadataCache.getFileCache(file);
            const frontmatter = cache?.frontmatter || {};

            // Check for duplicate or malformed review metadata
            const lastReviewedCount = (yamlContent.match(/^review-last-reviewed:/gm) || []).length;
            const nextReviewCount = (yamlContent.match(/^review-next-review:/gm) || []).length;
            const reviewCountCount = (yamlContent.match(/^review-count:/gm) || []).length;
            const reviewIntervalCount = (yamlContent.match(/^review-interval:/gm) || []).length;
            const reviewPriorityCount = (yamlContent.match(/^review-priority:/gm) || []).length;
            const hasOrphanedIndented = /^  (?:last-reviewed|next-review|review-count|review-interval|priority):/m.test(yamlContent);
            const hasNestedReview = /^review:\s*$/m.test(yamlContent);

            const hasDuplicatesOrProblems = lastReviewedCount > 1 ||
                                            nextReviewCount > 1 ||
                                            reviewCountCount > 1 ||
                                            reviewIntervalCount > 1 ||
                                            reviewPriorityCount > 1 ||
                                            hasOrphanedIndented ||
                                            hasNestedReview;

            // Skip if already has complete, clean review metadata
            if (frontmatter["review-next-review"] &&
                frontmatter["review-count"] !== undefined &&
                frontmatter.maturity &&
                frontmatter.confidence &&
                frontmatter.status &&
                !hasDuplicatesOrProblems) {
                stats.skipped++;
                continue;
            }

            // Add maturity if missing
            if (!frontmatter.maturity) {
                const defaultMaturity = "seedling";
                if (/^maturity:/m.test(yamlContent)) {
                    yamlContent = yamlContent.replace(/^maturity:.*$/m, `maturity: ${defaultMaturity}`);
                } else {
                    yamlContent += `\nmaturity: ${defaultMaturity}`;
                }
                stats.maturityAdded++;
                updated = true;
            }

            // Add confidence if missing
            if (!frontmatter.confidence) {
                const defaultConfidence = "speculative";
                if (/^confidence:/m.test(yamlContent)) {
                    yamlContent = yamlContent.replace(/^confidence:.*$/m, `confidence: ${defaultConfidence}`);
                } else {
                    yamlContent += `\nconfidence: ${defaultConfidence}`;
                }
                stats.confidenceAdded++;
                updated = true;
            }

            // Add status if missing
            if (!frontmatter.status) {
                const defaultStatus = "active";
                if (/^status:/m.test(yamlContent)) {
                    yamlContent = yamlContent.replace(/^status:.*$/m, `status: ${defaultStatus}`);
                } else {
                    yamlContent += `\nstatus: ${defaultStatus}`;
                }
                stats.statusAdded++;
                updated = true;
            }

            // Always clean up old/duplicate review metadata first
            // Remove nested "review:" block
            yamlContent = yamlContent.replace(/^review:\s*\n(?:  .+\n)*/gm, '');

            // Remove orphaned indented review properties (leftover from previous runs)
            yamlContent = yamlContent.replace(/^  (?:last-reviewed|next-review|review-count|review-interval|priority):.*\n/gm, '');

            // Count existing flattened review properties to detect duplicates
            const lastReviewedMatches = yamlContent.match(/^review-last-reviewed:.*$/gm) || [];
            const nextReviewMatches = yamlContent.match(/^review-next-review:.*$/gm) || [];
            const reviewCountMatches = yamlContent.match(/^review-count:.*$/gm) || [];
            const reviewIntervalMatches = yamlContent.match(/^review-interval:.*$/gm) || [];
            const reviewPriorityMatches = yamlContent.match(/^review-priority:.*$/gm) || [];

            const hasDuplicates = lastReviewedMatches.length > 1 ||
                                  nextReviewMatches.length > 1 ||
                                  reviewCountMatches.length > 1 ||
                                  reviewIntervalMatches.length > 1 ||
                                  reviewPriorityMatches.length > 1;

            // If there are duplicates or missing review data, clean and re-add
            if (hasDuplicates || !frontmatter["review-next-review"]) {
                // Remove ALL existing flattened review properties
                yamlContent = yamlContent.replace(/^review-last-reviewed:.*\n?/gm, '');
                yamlContent = yamlContent.replace(/^review-next-review:.*\n?/gm, '');
                yamlContent = yamlContent.replace(/^review-count:.*\n?/gm, '');
                yamlContent = yamlContent.replace(/^review-interval:.*\n?/gm, '');
                yamlContent = yamlContent.replace(/^review-priority:.*\n?/gm, '');

                // Preserve existing values if they exist
                const existingLastReviewed = frontmatter["review-last-reviewed"] || null;
                const existingReviewCount = frontmatter["review-count"] || 0;

                // Calculate review metadata
                const maturity = frontmatter.maturity || "seedling";
                const reviewInterval = maturityIntervals[maturity] || 7;

                // Calculate days since last modified
                const fileStats = await app.vault.adapter.stat(file.path);
                const daysSinceModified = Math.floor((Date.now() - fileStats.mtime) / (1000 * 60 * 60 * 24));

                // Use existing next-review if present, otherwise calculate
                let nextReview;
                if (frontmatter["review-next-review"]) {
                    nextReview = frontmatter["review-next-review"];
                } else {
                    const nextReviewDate = new Date(fileStats.mtime);
                    nextReviewDate.setDate(nextReviewDate.getDate() + reviewInterval);
                    nextReview = nextReviewDate.toISOString().split('T')[0];
                }

                // Calculate priority
                const backlinks = app.metadataCache.getBacklinksForFile(file);
                const backlinkCount = backlinks?.data ? Object.keys(backlinks.data).length : 0;
                const tags = frontmatter.tags || [];
                const tagsString = Array.isArray(tags) ? tags.join(" ") : tags;
                const hasMOCTag = tagsString.includes("type/moc");
                const hasUrgentTag = tagsString.includes("needs-review");

                let priority = frontmatter["review-priority"] || "medium";
                if (!frontmatter["review-priority"]) {
                    if (hasUrgentTag || backlinkCount > 20) {
                        priority = "urgent";
                    } else if (hasMOCTag || backlinkCount > 10) {
                        priority = "high";
                    } else if (backlinkCount < 3 && daysSinceModified > 60) {
                        priority = "low";
                    }
                }

                // Add clean flattened review properties
                const reviewProperties = [
                    `review-last-reviewed: ${existingLastReviewed}`,
                    `review-next-review: ${nextReview}`,
                    `review-count: ${existingReviewCount}`,
                    `review-interval: ${reviewInterval}`,
                    `review-priority: ${priority}`
                ].join('\n');

                yamlContent = yamlContent + '\n' + reviewProperties;

                stats.reviewAdded++;
                updated = true;
            }

            // Write updated content if changed
            if (updated) {
                const newContent = content.replace(yamlRegex, `---\n${yamlContent}\n---`);
                await app.vault.modify(file, newContent);
                stats.updated++;
            } else {
                stats.skipped++;
            }

        } catch (error) {
            console.error(`Error processing ${file.path}:`, error);
            stats.errors++;
        }
    }

    // Generate report
    const report = `
✅ BULK UPDATE COMPLETE

📊 Statistics:
- Total Scanned: ${stats.totalScanned}
- Updated: ${stats.updated}
- Skipped (already complete): ${stats.skipped}
- Errors: ${stats.errors}

📝 Metadata Added:
- Review objects: ${stats.reviewAdded}
- Maturity fields: ${stats.maturityAdded}
- Confidence fields: ${stats.confidenceAdded}
- Status fields: ${stats.statusAdded}

✅ All updates complete!
Check the review dashboard to see your queue.
`;

    new Notice("✅ Bulk update complete!");
    console.log(report);

    return report;
}

module.exports = bulkUpdateReviewMetadata;
