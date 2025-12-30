module.exports = async (params) => {
    const { quickAddApi: QuickAdd } = params;

    // Prompt for concept title
    const title = await QuickAdd.inputPrompt("Enter concept title:");
    if (!title) {
        new Notice("❌ Concept creation cancelled");
        return;
    }

    // Prompt for maturity level
    const maturity = await QuickAdd.suggester(
        ["🌱 Seedling (Just learning)", "🌿 Budding (Growing understanding)", "🌳 Evergreen (Well understood)"],
        ["seedling", "budding", "evergreen"]
    );
    if (!maturity) {
        new Notice("❌ Concept creation cancelled");
        return;
    }

    // Prompt for confidence level
    const confidence = await QuickAdd.suggester(
        ["Low (Uncertain)", "Medium (Somewhat confident)", "High (Very confident)"],
        ["low", "medium", "high"]
    );
    if (!confidence) {
        new Notice("❌ Concept creation cancelled");
        return;
    }

    // Calculate spaced repetition interval based on maturity and confidence
    let intervalDays;
    let intervalText;
    let priority;

    // Determine review interval
    if (maturity === "seedling") {
        if (confidence === "low") {
            intervalDays = 1;
            intervalText = "day";
            priority = "⏫";
        } else if (confidence === "medium") {
            intervalDays = 3;
            intervalText = "3 days";
            priority = "🔼";
        } else {
            intervalDays = 7;
            intervalText = "week";
            priority = "🔼";
        }
    } else if (maturity === "budding") {
        if (confidence === "low") {
            intervalDays = 3;
            intervalText = "3 days";
            priority = "🔼";
        } else if (confidence === "medium") {
            intervalDays = 7;
            intervalText = "week";
            priority = "";
        } else {
            intervalDays = 14;
            intervalText = "2 weeks";
            priority = "";
        }
    } else { // evergreen
        if (confidence === "low") {
            intervalDays = 7;
            intervalText = "week";
            priority = "";
        } else if (confidence === "medium") {
            intervalDays = 30;
            intervalText = "month";
            priority = "🔽";
        } else {
            intervalDays = 90;
            intervalText = "3 months";
            priority = "🔽";
        }
    }

    // Calculate next review date
    const today = new Date();
    const nextReviewDate = new Date(today);
    nextReviewDate.setDate(today.getDate() + intervalDays);
    const nextReview = nextReviewDate.toISOString().split('T')[0];

    // Generate unique ID
    const id = moment().format("YYYYMMDDHHmmss");

    // Set variables for the template
    QuickAdd.variables = {
        title: title,
        maturity: maturity,
        confidence: confidence,
        id: id,
        nextReview: nextReview,
        intervalText: intervalText,
        priority: priority,
        dateNow: moment().format("YYYY-MM-DD")
    };

    new Notice(`✨ Creating concept: "${title}"`);
};
