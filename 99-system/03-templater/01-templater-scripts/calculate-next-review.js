/**
 * Calculate Next Review Date
 *
 * Calculates the next review date based on maturity level and review interval.
 * Can be called from Templater templates using:
 * <% tp.user.calculate-next-review(tp, maturity, customInterval) %>
 *
 * @param {object} tp - Templater object
 * @param {string} maturity - Current maturity level (seedling, budding, developing, evergreen, needs-review)
 * @param {number} customInterval - Optional custom interval in days (overrides maturity-based)
 * @returns {string} Next review date in YYYY-MM-DD format
 */

function calculateNextReview(tp, maturity = "seedling", customInterval = null) {
    // Maturity-based interval mapping (in days)
    const maturityIntervals = {
        "seedling": 3,
        "budding": 7,
        "developing": 14,
        "evergreen": 30,
        "needs-review": 1
    };

    // Use custom interval if provided, otherwise use maturity-based interval
    const interval = customInterval !== null
        ? customInterval
        : maturityIntervals[maturity] || 7; // Default to 7 days if unknown maturity

    // Calculate next review date
    const nextReview = tp.date.now("YYYY-MM-DD", interval);

    return nextReview;
}

module.exports = calculateNextReview;
