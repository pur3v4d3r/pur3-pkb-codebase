/**
 * ═══════════════════════════════════════════════════════════════════════════
 * BATCH AUDIT ALL PERMANENT NOTES (QuickAdd Macro)
 * Scans the entire permanent notes folder and generates an audit report
 * 
 * SETUP:
 *   1. Place in vault: 99-scripts/quickadd/batch-audit-notes.js
 *   2. Create a QuickAdd Macro Choice with this as a User Script
 *   3. Requires: QuickAdd, Dataview plugins
 * 
 * WHAT IT DOES:
 *   - Scans all permanent notes for metadata completeness
 *   - Checks wiki-link density, word count, naming conventions
 *   - Identifies orphaned notes (no backlinks)
 *   - Creates a full audit report as a new note
 * 
 * REQUIREMENTS: QuickAdd plugin, Dataview plugin
 * ═══════════════════════════════════════════════════════════════════════════
 */

module.exports = {
  entry: start,
  settings: {
    name: "Batch Audit Permanent Notes",
    author: "PKB System",
    options: {
      "Notes folder": {
        type: "text",
        defaultValue: "03-notes/01_permanent-notes",
        description: "Folder containing permanent notes"
      },
      "Report folder": {
        type: "text",
        defaultValue: "999-report-orginizing",
        description: "Where to save the audit report"
      }
    }
  }
};

async function start(params, settings) {
  const { app, quickAddApi } = params;
  const moment = window.moment;
  const dv = app.plugins.plugins.dataview?.api;
  
  if (!dv) {
    new Notice("Dataview plugin is required for batch audit.");
    return;
  }
  
  const confirmed = await quickAddApi.yesNoPrompt(
    "Run Batch Audit?",
    "This will scan all permanent notes and generate an audit report."
  );
  if (!confirmed) return;
  
  new Notice("Running batch audit...");
  
  const notesFolder = settings["Notes folder"];
  const reportFolder = settings["Report folder"];
  
  // Get all permanent notes via Dataview
  const pages = dv.pages(`"${notesFolder}"`)
    .where(p => p.type === "permanent-note")
    .array();
  
  if (pages.length === 0) {
    new Notice("No permanent notes found in the specified folder.");
    return;
  }
  
  // Audit each note
  const results = [];
  let totalScore = 0;
  
  for (const page of pages) {
    const file = app.vault.getAbstractFileByPath(page.file.path);
    if (!file) continue;
    
    const content = await app.vault.read(file);
    const fm = page;
    const issues = [];
    let noteScore = 0;
    
    // Check 1: Core fields
    const coreFields = ["title", "type", "status", "confidence", "domain"];
    const missingCore = coreFields.filter(f => !fm[f]);
    if (missingCore.length === 0) noteScore += 2;
    else issues.push(`Missing: ${missingCore.join(", ")}`);
    
    // Check 2: Aliases
    const aliasCount = fm.aliases ? (Array.isArray(fm.aliases) ? fm.aliases.length : 1) : 0;
    if (aliasCount >= 2) noteScore += 1;
    else issues.push(`${aliasCount} alias(es), need ≥2`);
    
    // Check 3: Relationships
    const rels = ["prerequisites", "related", "broader", "narrower"];
    const populatedRels = rels.filter(r => {
      const val = fm[r];
      if (!val) return false;
      if (Array.isArray(val)) return val.some(v => v && v.length > 4);
      return val.length > 4;
    }).length;
    if (populatedRels >= 3) noteScore += 2;
    else if (populatedRels >= 1) { noteScore += 1; issues.push(`${populatedRels}/4 relationships`); }
    else issues.push("No relationships defined");
    
    // Check 4: Wiki-links
    const wikiLinks = (content.match(/\[\[([^\]]+)\]\]/g) || []).length;
    if (wikiLinks >= 8) noteScore += 2;
    else if (wikiLinks >= 4) { noteScore += 1; issues.push(`${wikiLinks} wiki-links, need ≥8`); }
    else issues.push(`Only ${wikiLinks} wiki-links`);
    
    // Check 5: Word count
    const body = content.replace(/^---[\s\S]*?---/, "").trim();
    const wordCount = body.split(/\s+/).filter(w => w.length > 0).length;
    if (wordCount >= 400) noteScore += 1.5;
    else issues.push(`~${wordCount} words, need ≥400`);
    
    // Check 6: Naming
    const nameMatch = file.basename === fm.title;
    if (nameMatch) noteScore += 1;
    else issues.push("Filename ≠ title");
    
    // Check 7: Backlinks (orphan check)
    const backlinks = page.file.inlinks?.length || 0;
    if (backlinks === 0) issues.push("ORPHAN: no backlinks");
    if (backlinks >= 1) noteScore += 0.5;
    
    const finalScore = Math.min(noteScore, 10);
    totalScore += finalScore;
    
    results.push({
      name: file.basename,
      score: finalScore,
      grade: finalScore >= 8 ? "PASS" : finalScore >= 6 ? "NEEDS WORK" : "FAIL",
      wordCount,
      wikiLinks,
      backlinks,
      issues,
      domain: fm.domain || "—",
      mastery: fm["mastery-stage"] || "—"
    });
  }
  
  // Sort by score ascending (worst first)
  results.sort((a, b) => a.score - b.score);
  
  const avgScore = totalScore / results.length;
  const passing = results.filter(r => r.grade === "PASS").length;
  const needsWork = results.filter(r => r.grade === "NEEDS WORK").length;
  const failing = results.filter(r => r.grade === "FAIL").length;
  const orphans = results.filter(r => r.issues.some(i => i.startsWith("ORPHAN"))).length;
  
  // Build report
  const today = moment().format("YYYY-MM-DD");
  const timestamp = moment().format("YYYY-MM-DD-HHmmss");
  
  let report = `---
title: "PKB Batch Audit — ${today}"
type: audit-report
created: ${today}
tags:
  - audit
  - meta
  - quality-assurance
---

# PKB Batch Audit Report

**Generated:** ${moment().format("YYYY-MM-DD HH:mm:ss")}
**Notes scanned:** ${results.length}
**Average score:** ${avgScore.toFixed(1)}/10

## Summary

| Metric | Value |
|--------|-------|
| Total notes | ${results.length} |
| Passing (≥8/10) | ${passing} (${Math.round(passing/results.length*100)}%) |
| Needs work (6-8) | ${needsWork} (${Math.round(needsWork/results.length*100)}%) |
| Failing (<6) | ${failing} (${Math.round(failing/results.length*100)}%) |
| Orphan notes | ${orphans} |
| Average score | ${avgScore.toFixed(1)}/10 |

## Domain Coverage

`;

  // Domain breakdown
  const domains = {};
  for (const r of results) {
    domains[r.domain] = (domains[r.domain] || 0) + 1;
  }
  report += "| Domain | Count |\n|--------|-------|\n";
  for (const [d, c] of Object.entries(domains).sort((a, b) => b[1] - a[1])) {
    report += `| ${d} | ${c} |\n`;
  }

  // Detailed results
  report += `\n## All Notes (Sorted by Score)\n\n`;
  report += "| Note | Score | Grade | Words | Links | Backlinks | Issues |\n";
  report += "|------|-------|-------|-------|-------|-----------|--------|\n";
  
  for (const r of results) {
    const issueText = r.issues.length > 0 ? r.issues.join("; ") : "—";
    report += `| [[${r.name}]] | ${r.score.toFixed(1)} | ${r.grade} | ${r.wordCount} | ${r.wikiLinks} | ${r.backlinks} | ${issueText} |\n`;
  }

  // Failing notes detail
  if (failing > 0) {
    report += `\n## Notes Requiring Attention\n\n`;
    for (const r of results.filter(r => r.grade === "FAIL")) {
      report += `### [[${r.name}]] — ${r.score.toFixed(1)}/10\n`;
      for (const issue of r.issues) {
        report += `- ⚠️ ${issue}\n`;
      }
      report += "\n";
    }
  }

  // Orphan notes
  if (orphans > 0) {
    report += `\n## Orphan Notes (No Backlinks)\n\n`;
    report += "These notes are not linked to from anywhere else. Consider adding connections:\n\n";
    for (const r of results.filter(r => r.issues.some(i => i.startsWith("ORPHAN")))) {
      report += `- [[${r.name}]] (${r.domain})\n`;
    }
  }

  report += `\n---\n*Audit generated by PKB Batch Audit Script v1.0*\n`;

  // Save report
  const reportPath = `${reportFolder}/audit-${timestamp}.md`;
  await app.vault.create(reportPath, report);
  
  // Open the report
  await app.workspace.openLinkText(reportPath, "");
  
  new Notice(
    `Audit complete: ${results.length} notes scanned.\n` +
    `Average: ${avgScore.toFixed(1)}/10 | Passing: ${passing} | Failing: ${failing}`,
    8000
  );
}
