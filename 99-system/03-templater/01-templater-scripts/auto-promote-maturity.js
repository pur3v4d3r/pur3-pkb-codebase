/**
 * Auto-Promote Maturity
 *
 * Suggests maturity promotions based on review history and engagement patterns.
 * Promotion criteria:
 * - Seedling → Budding: 3+ reviews
 * - Budding → Developing: 6+ reviews
 * - Developing → Evergreen: 10+ reviews
 * - Needs-review → Budding: 2+ reviews with improvements
 *
 * Can be called from Templater templates using:
 * <% tp.user.auto-promote-maturity(tp) %>
 *
 * @param {object} tp - Templater object
 * @returns {string} Suggested new maturity level (or current if no promotion)
 */

async function autoPromoteMaturity(tp) {
    // Get current frontmatter
    const frontmatter = tp.frontmatter || {};
    const currentMaturity = frontmatter.maturity || "seedling";
    const reviewCount = frontmatter.review?.["review-count"] || frontmatter["review-count"] || 0;

    // Promotion rules
    const promotionRules = {
        "seedling": {minReviews: 3, nextStage: "budding"},
        "budding": {minReviews: 6, nextStage: "developing"},
        "developing": {minReviews: 10, nextStage: "evergreen"},
        "needs-review": {minReviews: 2, nextStage: "budding"},
        "evergreen": {minReviews: Infinity, nextStage: "evergreen"}
    };

    const rule = promotionRules[currentMaturity];

    // Check if eligible for promotion
    if (!rule) {
        return currentMaturity; // Unknown maturity, return as-is
    }

    if (reviewCount >= rule.minReviews) {
        // Eligible for promotion - ask user
        const shouldPromote = await tp.system.prompt(
            `This note has ${reviewCount} reviews. Promote from ${currentMaturity} to ${rule.nextStage}?`,
            null,
            false,
            true // multiline
        );

        // Check for positive response
        if (shouldPromote &&
            (shouldPromote.toLowerCase().includes("yes") ||
             shouldPromote.toLowerCase().includes("y") ||
             shouldPromote.toLowerCase().trim() === "")) {
            return rule.nextStage;
        }
    }

    // Not eligible or user declined
    return currentMaturity;
}

module.exports = autoPromoteMaturity;
