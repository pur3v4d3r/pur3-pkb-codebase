/**
 * clipboard_normalizer.js
 * A modular normalization engine for Obsidian Templater.
 * * @param {object} tp - The Templater object (passed from the template)
 * @param {string} mode - The normalization mode ('standard', 'aggressive', 'links_only', 'raw')
 * @returns {Promise<string>} - The normalized text
 */

async function normalize(tp, mode = 'standard') {
    // 1. Ingest Clipboard Content
    let text = await tp.system.clipboard();
    
    // If clipboard is empty, return notification
    if (!text) {
        new Notice("📋 Clipboard is empty.");
        return "";
    }

    console.log(`[Normalizer] Processing ${text.length} chars in mode: ${mode}`);

    // 2. Define Regex Cleaning Modules
    
    // BASIC: Removes invisible cruft and standardizes line endings
    const basicClean = (str) => {
        return str
            .replace(/\r\n/g, "\n")           // Windows to Unix line endings
            .replace(/\r/g, "\n")             // Old Mac to Unix
            .replace(/[\u200B-\u200D\uFEFF]/g, "") // Zero-width spaces
            .replace(/\u00A0/g, " ");         // Non-breaking space to normal space
    };

    // TYPOGRAPHY: Fixes quotes, dashes, and ellipses
    const typographyFix = (str) => {
        return str
            .replace(/[“”]/g, '"')            // Smart double quotes to straight
            .replace(/[‘’]/g, "'")            // Smart single quotes to straight
            .replace(/…/g, "...")             // Ellipsis char to three dots
            .replace(/–/g, "--")              // En-dash to double hyphen (optional preference)
            .replace(/—/g, "---");            // Em-dash to triple hyphen
    };

    // MARKDOWN: Standardizes headers, lists, and spacing
    const markdownStruct = (str) => {
        return str
            // Fix headers: "#Header" -> "# Header"
            .replace(/^(#{1,6})(?=[^\s#])/gm, "$1 ")
            // Fix list spacing: "-Item" -> "- Item"
            .replace(/^(\s*[-*+])(?=[^\s])/gm, "$1 ")
            // Remove multiple empty lines (max 2)
            .replace(/\n{3,}/g, "\n\n")
            // Trim trailing whitespace per line
            .replace(/[ \t]+$/gm, "");
    };

    // URL SANITIZER: Strips UTM and tracking params
    const cleanUrls = (str) => {
        // Regex to find Markdown links and raw URLs
        // Note: This is a robust but safe regex for common tracking params
        return str.replace(/(\?|&)(utm_[^=&]+|fbclid|gclid|mc_eid|oly_enc_id|rb_clickid)=[^&\s)]*/g, "");
    };

    // 3. Execution Pipeline based on Mode
    
    let processed = text;

    // PIPELINE: Always run Basic
    processed = basicClean(processed);

    if (mode === 'links_only') {
        processed = cleanUrls(processed);
        return processed;
    }

    if (mode === 'standard') {
        processed = typographyFix(processed);
        processed = markdownStruct(processed);
        processed = cleanUrls(processed);
    }

    if (mode === 'aggressive') {
        processed = typographyFix(processed);
        processed = markdownStruct(processed);
        processed = cleanUrls(processed);
        // Aggressive: Flatten to single paragraph if it looks like broken PDF paste
        // Warning: destructive for lists
        // processed = processed.replace(/\n(?!\n)/g, " "); 
    }

    // 4. Final Trim
    return processed.trim();
}

module.exports = normalize;