/**
 * ═══════════════════════════════════════════════════════════════════════════
 * PERMANENT NOTE AUDIT SCRIPT (QuickAdd Macro)
 * Validates imported permanent notes against PKB quality standards
 * 
 * SETUP:
 *   1. Place this file in your vault (NOT in .obsidian/ or hidden folders)
 *      Recommended: 99-scripts/quickadd/validate-permanent-note.js
 *   2. In QuickAdd settings, create a new Macro Choice
 *   3. Add this script as a User Script command in the macro
 *   4. Optionally assign a hotkey to the macro
 * 
 * USAGE: Open a permanent note, then trigger this macro. It will audit
 *        the note's metadata, connections, and structure, outputting a
 *        report to the console and optionally appending a validation
 *        callout to the note itself.
 * 
 * REQUIREMENTS: QuickAdd plugin (by chhoumann), Dataview plugin
 * ═══════════════════════════════════════════════════════════════════════════
 */

module.exports = {
  entry: start,
  settings: {
    name: "Permanent Note Validator",
    author: "PKB System",
    options: {
      "Append report to note": {
        type: "toggle",
        defaultValue: false,
        description: "If enabled, appends a validation callout at the bottom of the note"
      },
      "Minimum wiki-links": {
        type: "text",
        defaultValue: "8",
        description: "Minimum number of wiki-links expected"
      },
      "Permanent notes folder": {
        type: "text",
        defaultValue: "03-notes/01_permanent-notes",
        description: "Folder path for permanent notes"
      }
    }
  }
};

async function start(params, settings) {
  const { app, quickAddApi } = params;
  
  // Get current file
  const activeFile = app.workspace.getActiveFile();
  if (!activeFile) {
    new Notice("No active file. Open a permanent note first.");
    return;
  }
  
  // Read frontmatter
  const metadata = app.metadataCache.getFileCache(activeFile);
  const frontmatter = metadata?.frontmatter;
  
  if (!frontmatter) {
    new Notice("No frontmatter found in this file.");
    return;
  }
  
  // Initialize scoring
  const issues = [];
  const passes = [];
  let score = 0;
  const maxScore = 10;
  
  // ─── CHECK 1: Core Identity Fields ───
  const coreFields = ["title", "type", "status", "confidence"];
  let coreComplete = true;
  for (const field of coreFields) {
    if (!frontmatter[field]) {
      issues.push(`Missing required field: \`${field}\``);
      coreComplete = false;
    }
  }
  if (coreComplete) {
    passes.push("All core identity fields present");
    score += 1.5;
  }
  
  // ─── CHECK 2: Type and Status ───
  if (frontmatter.type === "permanent-note") {
    passes.push("Correct note type: permanent-note");
    score += 0.5;
  } else {
    issues.push(`Note type is '${frontmatter.type}', expected 'permanent-note'`);
  }
  
  if (frontmatter.status === "evergreen") {
    passes.push("Status is evergreen");
    score += 0.5;
  } else {
    issues.push(`Status is '${frontmatter.status}', expected 'evergreen'`);
  }
  
  // ─── CHECK 3: Aliases ───
  const aliases = frontmatter.aliases;
  if (aliases && Array.isArray(aliases) && aliases.length >= 2) {
    passes.push(`${aliases.length} aliases defined`);
    score += 0.5;
  } else {
    issues.push(`Only ${aliases?.length || 0} alias(es). Minimum 2 recommended.`);
  }
  
  // ─── CHECK 4: Tags ───
  const tags = frontmatter.tags;
  if (tags && Array.isArray(tags)) {
    const hasPermanentNote = tags.includes("permanent-note");
    const hasEvergreen = tags.includes("evergreen");
    if (hasPermanentNote && hasEvergreen) {
      passes.push("Required tags present (permanent-note, evergreen)");
      score += 0.5;
    } else {
      if (!hasPermanentNote) issues.push("Missing tag: permanent-note");
      if (!hasEvergreen) issues.push("Missing tag: evergreen");
    }
  } else {
    issues.push("No tags defined");
  }
  
  // ─── CHECK 5: Domain Classification ───
  if (frontmatter.domain) {
    passes.push(`Domain: ${frontmatter.domain}`);
    score += 0.5;
  } else {
    issues.push("No domain specified");
  }
  
  // ─── CHECK 6: Temporal Fields ───
  if (frontmatter.created && frontmatter.updated) {
    passes.push("Created and updated dates present");
    score += 0.5;
  } else {
    issues.push("Missing created or updated date");
  }
  
  // ─── CHECK 7: Relationships ───
  const relationships = ["prerequisites", "related", "broader", "narrower"];
  let relCount = 0;
  for (const rel of relationships) {
    const val = frontmatter[rel];
    if (val && Array.isArray(val) && val.length > 0) {
      const nonEmpty = val.filter(v => v && v !== "[[]]" && v.length > 4);
      if (nonEmpty.length > 0) relCount++;
    }
  }
  
  if (relCount >= 3) {
    passes.push(`${relCount}/4 relationship categories populated`);
    score += 1.5;
  } else if (relCount >= 1) {
    issues.push(`Only ${relCount}/4 relationship categories populated. Need at least 3.`);
    score += 0.5;
  } else {
    issues.push("No relationships defined. Notes need connections!");
  }
  
  // ─── CHECK 8: Wiki-Link Density ───
  const content = await app.vault.read(activeFile);
  const wikiLinkRegex = /\[\[([^\]]+)\]\]/g;
  const wikiLinks = content.match(wikiLinkRegex) || [];
  const minLinks = parseInt(settings["Minimum wiki-links"]) || 8;
  
  if (wikiLinks.length >= minLinks) {
    passes.push(`${wikiLinks.length} wiki-links (target: ≥${minLinks})`);
    score += 1.5;
  } else if (wikiLinks.length >= Math.floor(minLinks / 2)) {
    issues.push(`${wikiLinks.length} wiki-links, below target of ${minLinks}`);
    score += 0.5;
  } else {
    issues.push(`Only ${wikiLinks.length} wiki-links. Target: ≥${minLinks}`);
  }
  
  // ─── CHECK 9: Content Length ───
  // Strip frontmatter for word count
  const bodyContent = content.replace(/^---[\s\S]*?---/, "").trim();
  const wordCount = bodyContent.split(/\s+/).filter(w => w.length > 0).length;
  
  if (wordCount >= 400) {
    passes.push(`Word count: ~${wordCount} (target: ≥400)`);
    score += 1;
  } else if (wordCount >= 200) {
    issues.push(`Word count: ~${wordCount}. Target is ≥400 for permanent notes.`);
    score += 0.5;
  } else {
    issues.push(`Word count: ~${wordCount}. Substantially below 400 minimum.`);
  }
  
  // ─── CHECK 10: Naming Convention ───
  const fileName = activeFile.basename;
  const title = frontmatter.title;
  if (title && fileName === title) {
    passes.push("Filename matches title (wiki-link compatible)");
    score += 1;
  } else if (title) {
    issues.push(`Filename '${fileName}' does not match title '${title}'`);
  } else {
    issues.push("No title in frontmatter to verify naming");
  }
  
  // ─── CHECK 11: Callouts ───
  const calloutRegex = />\s*\[!(definition|key-claim|example|warning|connection|info|tip|summary)\]/g;
  const callouts = content.match(calloutRegex) || [];
  
  if (callouts.length >= 3) {
    passes.push(`${callouts.length} callouts found`);
    score += 0.5;
  } else {
    issues.push(`Only ${callouts.length} callout(s). Target: ≥3`);
  }
  
  // ─── FINAL SCORE ───
  const finalScore = Math.min(score, maxScore);
  const grade = finalScore >= 8.0 ? "PASS" : finalScore >= 6.0 ? "NEEDS WORK" : "FAIL";
  
  // Build report
  const report = [
    `## Validation Report: ${fileName}`,
    `**Score: ${finalScore.toFixed(1)}/${maxScore} — ${grade}**`,
    `**Date:** ${window.moment().format("YYYY-MM-DD HH:mm")}`,
    `**Word count:** ~${wordCount}`,
    `**Wiki-links:** ${wikiLinks.length}`,
    `**Callouts:** ${callouts.length}`,
    "",
    "### Passes",
    ...passes.map(p => `- ✅ ${p}`),
    "",
    "### Issues",
    ...(issues.length > 0 
      ? issues.map(i => `- ⚠️ ${i}`) 
      : ["- *No issues found!*"]),
  ].join("\n");
  
  // Display results
  console.log(report);
  
  // Show notice with score
  new Notice(`Validation: ${finalScore.toFixed(1)}/10 — ${grade}\n${issues.length} issue(s) found`, 5000);
  
  // Optionally append to note
  if (settings["Append report to note"]) {
    const confirmed = await quickAddApi.yesNoPrompt(
      `Append validation report to "${fileName}"?`,
      `Score: ${finalScore.toFixed(1)}/10 — ${grade}`
    );
    
    if (confirmed) {
      const calloutReport = [
        "",
        "---",
        "",
        `> [!info] **Validation Report — ${window.moment().format("YYYY-MM-DD")}**`,
        `> Score: ${finalScore.toFixed(1)}/${maxScore} — **${grade}**`,
        `> Wiki-links: ${wikiLinks.length} | Callouts: ${callouts.length} | Words: ~${wordCount}`,
        issues.length > 0 
          ? `> Issues: ${issues.join("; ")}` 
          : "> No issues found.",
      ].join("\n");
      
      await app.vault.append(activeFile, calloutReport);
      new Notice("Validation report appended to note.");
    }
  }
}
