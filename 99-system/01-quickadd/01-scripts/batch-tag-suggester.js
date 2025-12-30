/**
 * ENHANCED BATCH TAG SUGGESTER
 * Updated with comprehensive 577-tag taxonomy
 * Based on: _reference-taxonomy-pur3v4d3r-tags-202511190109.md
 */

module.exports = async (params) => {
    const { quickAddApi: qa, app } = params;

    // ========================================
    // COMPREHENSIVE TAG TAXONOMIES
    // ========================================

    const tagTaxonomies = {
        // PKM/PKB DOMAIN
        pkmGeneral: {
            name: "PKM/PKB General",
            description: "Personal Knowledge Management & Knowledge Base",
            domains: [
                '#pkm', '#pkb', '#note-taking', '#knowledge-workflow',
                '#obsidian', '#information-architecture', '#knowledge-graph',
                '#digital-garden', '#productivity', '#knowledge-work'
            ],
            subdomains: [
                // PKM Theory & Methodology
                '#pkm/theory', '#pkm/methodology', '#pkm/workflow', '#pkm/principles', '#pkm/research',
                '#pkm/methodology/zettelkasten', '#pkm/methodology/para', '#pkm/methodology/lyt',
                '#pkm/methodology/evergreen-notes', '#pkm/methodology/digital-garden',
                '#pkm/workflow/capture', '#pkm/workflow/process', '#pkm/workflow/organize',
                '#pkm/workflow/distill', '#pkm/workflow/express', '#pkm/workflow/review',
                // PKB Architecture
                '#pkb/architecture', '#pkb/design', '#pkb/components', '#pkb/metadata',
                '#pkb/maintenance', '#pkb/optimization',
                '#pkb/components/moc', '#pkb/components/hub-notes', '#pkb/components/index-notes',
                // Knowledge Workflows
                '#knowledge-workflow/capture', '#knowledge-workflow/processing', '#knowledge-workflow/synthesis',
                '#knowledge-workflow/output', '#knowledge-workflow/review',
                // Obsidian Specific
                '#obsidian/core-features', '#obsidian/plugins', '#obsidian/customization',
                '#obsidian/plugins/dataview', '#obsidian/plugins/templater', '#obsidian/plugins/quickadd',
                '#obsidian/plugins/tasks', '#obsidian/plugins/meta-bind'
            ],
            types: [
                '#type/fleeting', '#type/literature', '#type/permanent', '#type/moc',
                '#type/reference', '#type/tutorial', '#type/template', '#type/dashboard',
                '#type/guide', '#type/framework', '#type/practice-log', '#type/reflection', '#type/review'
            ],
            status: [
                '#status/seedling', '#status/budding', '#status/evergreen', '#status/review',
                '#status/archived', '#status/in-progress', '#status/complete',
                '#status/read', '#status/not-read'
            ],
            source: [
                '#source/book', '#source/article', '#source/blog', '#source/video',
                '#source/podcast', '#source/course', '#source/documentation',
                '#source/community', '#source/experience', '#source/original', '#source/pur3v4d3r'
            ],
            context: [
                '#context/theoretical', '#context/practical', '#context/tutorial',
                '#context/reference', '#context/meta', '#context/experimental'
            ]
        },

        // COGNITIVE SCIENCE DOMAIN
        cognitivePsychology: {
            name: "Cognitive Science & Psychology",
            description: "Cognitive science, psychology, learning theory",
            domains: [
                '#cognitive-science', '#neuroscience', '#behavioral-science', '#learning-science'
            ],
            subdomains: [
                // Major Subdisciplines
                '#cognitive-psychology', '#cognitive-neuroscience', '#cognitive-linguistics',
                '#cognitive-development', '#educational-psychology', '#instructional-design',
                // Core Cognitive Systems
                '#memory-systems', '#working-memory', '#long-term-memory', '#episodic-memory',
                '#semantic-memory', '#procedural-memory', '#prospective-memory',
                '#attention', '#selective-attention', '#divided-attention', '#sustained-attention',
                '#executive-function', '#inhibitory-control', '#cognitive-flexibility', '#planning',
                '#language-processing', '#reasoning', '#problem-solving', '#creative-thinking',
                '#critical-thinking', '#learning-processes', '#skill-acquisition',
                // Mechanisms
                '#encoding', '#consolidation', '#retrieval', '#reconsolidation',
                '#cognitive-load', '#cognitive-control', '#metacognition', '#self-regulation',
                // Theories
                '#cognitive-load-theory', '#dual-process-theory', '#information-processing-theory',
                '#embodied-cognition', '#distributed-cognition', '#extended-cognition',
                // Applied
                '#applied-cognition', '#cognitive-training', '#cognitive-enhancement'
            ],
            types: [
                '#type/permanent', '#type/literature', '#type/moc', '#type/framework',
                '#type/practice-log', '#type/synthesis', '#type/technique'
            ],
            status: [
                '#status/seedling', '#status/budding', '#status/developing', '#status/evergreen',
                '#status/needs-review', '#status/archived'
            ],
            source: [
                '#source/book', '#source/article', '#source/paper', '#source/course',
                '#source/podcast', '#source/video', '#source/experience', '#source/original'
            ],
            context: [
                '#context/theoretical', '#context/applied', '#context/personal',
                '#context/professional', '#context/research', '#context/teaching'
            ],
            mode: [
                '#mode/analytical', '#mode/synthetic', '#mode/reflective', '#mode/practical'
            ]
        },

        // PROMPT ENGINEERING DOMAIN
        promptEngineering: {
            name: "Prompt Engineering & LLMs",
            description: "AI prompting, LLM capabilities, prompt patterns",
            domains: [
                '#prompt-engineering', '#llm-capability', '#llm-limitation', '#llm-architecture'
            ],
            subdomains: [
                // Fundamentals
                '#prompt-engineering/theory', '#prompt-engineering/principles', '#prompt-engineering/anatomy',
                '#prompt-engineering/evaluation', '#prompt-engineering/optimization',
                // Techniques
                '#prompting-technique', '#prompting-technique/zero-shot', '#prompting-technique/few-shot',
                '#prompting-technique/chain-of-thought', '#prompting-technique/reasoning',
                '#prompting-technique/react', '#prompting-technique/reflection', '#prompting-technique/meta-prompting',
                // Patterns
                '#prompt-pattern', '#prompt-pattern/persona', '#prompt-pattern/template',
                '#prompt-pattern/context-control', '#prompt-pattern/output-format', '#prompt-pattern/error-handling',
                // Advanced
                '#advanced-prompting/agents', '#advanced-prompting/rag', '#advanced-prompting/function-calling',
                '#advanced-prompting/multi-modal', '#advanced-prompting/programming', '#advanced-prompting/chain-systems',
                // LLM Specifics
                '#llm-capability/reasoning', '#llm-capability/knowledge', '#llm-capability/generation',
                '#llm-limitation/hallucination', '#llm-limitation/reasoning-failures',
                '#llm-architecture/transformer', '#llm-architecture/model-family/claude',
                '#llm-architecture/model-family/gpt', '#llm-architecture/model-family/gemini',
                // Context & Safety
                '#context-management', '#context-management/window', '#context-management/memory',
                '#prompt-safety', '#prompt-safety/adversarial', '#prompt-safety/alignment',
                // Workflow
                '#prompt-workflow', '#prompt-workflow/ideation', '#prompt-workflow/prototyping',
                '#prompt-workflow/evaluation', '#prompt-workflow/deployment',
                // Applications
                '#prompt-application/writing', '#prompt-application/analysis', '#prompt-application/coding'
            ],
            types: [
                '#type/technique', '#type/pattern', '#type/template', '#type/experiment',
                '#type/analysis', '#type/literature', '#type/reference', '#type/case-study',
                '#type/tutorial', '#type/comparison', '#type/prompt-library'
            ],
            status: [
                '#status/experimental', '#status/proven', '#status/deprecated',
                '#status/under-revision', '#status/production', '#status/archived'
            ],
            maturity: [
                '#maturity/emerging', '#maturity/established', '#maturity/standard', '#maturity/deprecated'
            ],
            complexity: [
                '#complexity/basic', '#complexity/intermediate', '#complexity/advanced', '#complexity/expert'
            ],
            validation: [
                '#validation/tested', '#validation/reported', '#validation/theoretical', '#validation/failed'
            ],
            model: [
                '#model/claude', '#model/gpt', '#model/gemini', '#model/open-source', '#model/agnostic'
            ]
        },

        // CRITICAL THINKING & SELF-IMPROVEMENT
        criticalThinking: {
            name: "Critical Thinking & Self-Development",
            description: "Analysis, evaluation, self-improvement",
            domains: [
                '#critical-thinking', '#self-regulation', '#self-improvement', '#learning-theory'
            ],
            subdomains: [
                // Critical Thinking
                '#critical-thinking/analysis', '#critical-thinking/logic', '#critical-thinking/evaluation',
                '#critical-thinking/synthesis', '#critical-thinking/problem-solving',
                // Self-Regulation
                '#self-regulation/motivation', '#self-regulation/goal-setting', '#self-regulation/self-control',
                '#self-regulation/emotional', '#self-regulation/behavioral',
                // Learning Theory
                '#learning-theory/andragogy', '#learning-theory/pedagogy', '#learning-theory/heutagogy',
                '#learning-theory/constructivism', '#learning-theory/cognitive-apprenticeship',
                // Self-Improvement
                '#self-improvement/skill-development', '#self-improvement/mental-models',
                '#self-improvement/productivity', '#self-improvement/reflective-practice',
                '#self-improvement/growth-mindset'
            ],
            types: [
                '#type/permanent', '#type/technique', '#type/framework', '#type/practice-log'
            ],
            status: [
                '#status/seedling', '#status/budding', '#status/developing', '#status/evergreen'
            ],
            source: [
                '#source/book', '#source/article', '#source/course', '#source/experience', '#source/original'
            ]
        },

        // CROSS-DOMAIN INTEGRATION
        crossDomain: {
            name: "Cross-Domain Integration",
            description: "Cognitive science + PKM integration",
            domains: [
                '#cognitive-pkm', '#evidence-based-pkm', '#learning-optimization'
            ],
            subdomains: [
                '#memory-systems-design', '#attention-architecture', '#spaced-review-system',
                '#retrieval-practice-pkm', '#encoding-strategies', '#consolidation-workflow',
                '#extraneous-load-reduction', '#germane-load-optimization', '#working-memory-support',
                '#metacognitive-pkm', '#learning-analytics', '#reflection-systems',
                '#instructional-design-pkm', '#expertise-development'
            ],
            types: [
                '#type/permanent', '#type/framework', '#type/synthesis', '#type/moc'
            ],
            status: [
                '#status/developing', '#status/evergreen'
            ]
        },

        // BOOKS & LITERATURE
        books: {
            name: "Books & Literature Notes",
            description: "Book notes and literature summaries",
            domains: [
                '#cognitive-science', '#learning-theory', '#prompt-engineering',
                '#pkm', '#productivity', '#self-improvement'
            ],
            types: [
                '#type/literature', '#type/permanent', '#type/moc', '#type/synthesis'
            ],
            status: [
                '#status/to-read', '#status/reading', '#status/complete',
                '#status/review', '#status/archived', '#status/read', '#status/not-read'
            ],
            source: ['#source/book']
        },

        // OBSIDIAN SYSTEM NOTES
        obsidianSystem: {
            name: "Obsidian System & Meta",
            description: "Technical documentation, templates, system notes",
            domains: [
                '#obsidian', '#information-architecture', '#pkb'
            ],
            subdomains: [
                '#obsidian/plugins/dataview', '#obsidian/plugins/templater', '#obsidian/plugins/quickadd',
                '#obsidian/plugins/tasks', '#obsidian/plugins/meta-bind', '#obsidian/advanced/dataviewjs',
                '#obsidian/advanced/templater-scripts', '#obsidian/advanced/automation'
            ],
            types: [
                '#type/reference', '#type/tutorial', '#type/template', '#type/dashboard',
                '#type/guide', '#type/framework'
            ],
            status: [
                '#status/in-progress', '#status/complete', '#status/review', '#status/archived'
            ],
            context: [
                '#context/meta', '#context/reference', '#context/tutorial'
            ]
        },

        // PROJECTS
        projects: {
            name: "Projects & Tasks",
            description: "Project management and tracking",
            domains: ['#project', '#productivity'],
            types: [
                '#type/project', '#type/moc', '#type/dashboard', '#type/practice-log'
            ],
            status: [
                '#status/planning', '#status/active', '#status/on-hold',
                '#status/complete', '#status/archived'
            ],
            priority: [
                '#priority/high', '#priority/medium', '#priority/low'
            ]
        },

        // RESEARCH NOTES
        research: {
            name: "Research & Academic",
            description: "Research notes, papers, academic content",
            domains: [
                '#cognitive-science', '#learning-theory', '#prompt-engineering'
            ],
            types: [
                '#type/literature', '#type/synthesis', '#type/analysis',
                '#type/framework', '#type/moc'
            ],
            status: [
                '#status/seedling', '#status/budding', '#status/developing',
                '#status/evergreen', '#status/review'
            ],
            source: [
                '#source/paper', '#source/article', '#source/book',
                '#source/conference', '#source/course'
            ],
            context: [
                '#context/research', '#context/theoretical', '#context/applied'
            ]
        },

        // MINIMAL/QUICK CAPTURE
        minimal: {
            name: "Quick Capture & Inbox",
            description: "Unprocessed captures, inbox items",
            types: ['#type/fleeting', '#type/inbox'],
            status: ['#status/unprocessed', '#status/in-progress', '#status/complete'],
            priority: ['#priority/high', '#priority/medium', '#priority/low']
        }
    };

    // ========================================
    // TAXONOMY SELECTION
    // ========================================

    const taxonomyNames = Object.keys(tagTaxonomies);
    const taxonomyChoices = taxonomyNames.map(name => {
        const tax = tagTaxonomies[name];
        return `${tax.name} - ${tax.description}`;
    });

    const selectedTaxonomyLabel = await qa.suggester(
        taxonomyChoices,
        taxonomyChoices,
        "Select tag taxonomy for this folder:"
    );

    if (!selectedTaxonomyLabel) return;

    const selectedTaxonomyName = Object.keys(tagTaxonomies).find(name =>
        tagTaxonomies[name].name === selectedTaxonomyLabel.split(' - ')[0]
    );
    const tagTaxonomy = tagTaxonomies[selectedTaxonomyName];

    // ========================================
    // FOLDER SELECTION
    // ========================================

    const allFolders = app.vault.getAllLoadedFiles()
        .filter(f => f.children !== undefined)
        .map(f => f.path)
        .sort();

    const folderPath = await qa.suggester(
        allFolders,
        allFolders,
        "Select folder to process:"
    );

    if (!folderPath) return;

    // ========================================
    // FILE ANALYSIS
    // ========================================

    const files = app.vault.getMarkdownFiles()
        .filter(f => f.path.startsWith(folderPath));

    const suggestions = [];
    let processedCount = 0;

    for (const file of files) {
        processedCount++;
        if (processedCount % 10 === 0) {
            new Notice(`Processing... ${processedCount}/${files.length}`);
        }

        const content = await app.vault.read(file);
        const cache = app.metadataCache.getFileCache(file);
        const frontmatter = cache?.frontmatter;

        // Get all existing tags
        let existingTags = [];
        if (frontmatter?.tags) {
            if (Array.isArray(frontmatter.tags)) {
                existingTags = frontmatter.tags;
            } else if (typeof frontmatter.tags === 'string') {
                existingTags = frontmatter.tags.split(',').map(t => t.trim());
            }
        }
        // Add inline tags from cache
        if (cache?.tags) {
            existingTags = [...existingTags, ...cache.tags.map(t => t.tag)];
        }
        // Normalize tags (ensure they start with #)
        existingTags = existingTags.map(t => t.startsWith('#') ? t : '#' + t);
        existingTags = [...new Set(existingTags)]; // Remove duplicates

        // Analyze content for missing tags
        const missingTags = [];
        const contentLower = content.toLowerCase();

        // Check domain tags
        if (tagTaxonomy.domains) {
            let hasDomain = existingTags.some(t =>
                tagTaxonomy.domains.includes(t)
            );
            if (!hasDomain) {
                // Suggest based on content keywords
                for (const domain of tagTaxonomy.domains) {
                    const keyword = domain.replace('#', '').replace(/\//g, ' ').replace(/-/g, ' ');
                    if (contentLower.includes(keyword)) {
                        missingTags.push(domain);
                        hasDomain = true;
                        break; // Only suggest one domain
                    }
                }
                if (!hasDomain) {
                    missingTags.push(`#needs-domain-tag (from: ${tagTaxonomy.domains.slice(0,3).join(', ')}...)`);
                }
            }
        }

        // Check subdomain tags (optional but suggested)
        if (tagTaxonomy.subdomains) {
            let hasSubdomain = existingTags.some(t =>
                tagTaxonomy.subdomains.includes(t)
            );
            if (!hasSubdomain) {
                // Suggest based on content keywords
                for (const subdomain of tagTaxonomy.subdomains.slice(0, 20)) {
                    const keyword = subdomain.split('/').pop().replace(/-/g, ' ');
                    if (contentLower.includes(keyword)) {
                        missingTags.push(subdomain);
                        break; // Only suggest one
                    }
                }
            }
        }

        // Check type tags
        if (tagTaxonomy.types && !existingTags.some(t => tagTaxonomy.types.includes(t))) {
            missingTags.push(`#needs-type-tag (options: ${tagTaxonomy.types.slice(0,5).join(', ')}...)`);
        }

        // Check status tags
        if (tagTaxonomy.status && !existingTags.some(t => tagTaxonomy.status.includes(t))) {
            missingTags.push(`#needs-status-tag (options: ${tagTaxonomy.status.slice(0,5).join(', ')}...)`);
        }

        // Check source tags
        if (tagTaxonomy.source && !existingTags.some(t => tagTaxonomy.source.includes(t))) {
            if (contentLower.includes('author:') || contentLower.includes('source:') ||
                contentLower.includes('reference:') || contentLower.includes('from:')) {
                missingTags.push(`#needs-source-tag (options: ${tagTaxonomy.source.join(', ')})`);
            }
        }

        // Check context tags
        if (tagTaxonomy.context && !existingTags.some(t => tagTaxonomy.context.includes(t))) {
            missingTags.push(`#needs-context-tag (options: ${tagTaxonomy.context.join(', ')})`);
        }

        // Check maturity tags
        if (tagTaxonomy.maturity && !existingTags.some(t => tagTaxonomy.maturity.includes(t))) {
            missingTags.push(`#needs-maturity-tag (options: ${tagTaxonomy.maturity.join(', ')})`);
        }

        // Check complexity tags
        if (tagTaxonomy.complexity && !existingTags.some(t => tagTaxonomy.complexity.includes(t))) {
            missingTags.push(`#needs-complexity-tag (options: ${tagTaxonomy.complexity.join(', ')})`);
        }

        // Check model tags (for prompt engineering)
        if (tagTaxonomy.model && !existingTags.some(t => tagTaxonomy.model.includes(t))) {
            if (contentLower.includes('claude') || contentLower.includes('gpt') ||
                contentLower.includes('gemini') || contentLower.includes('llm')) {
                missingTags.push(`#needs-model-tag (options: ${tagTaxonomy.model.join(', ')})`);
            }
        }

        // Check mode tags
        if (tagTaxonomy.mode && !existingTags.some(t => tagTaxonomy.mode.includes(t))) {
            missingTags.push(`#needs-mode-tag (options: ${tagTaxonomy.mode.join(', ')})`);
        }

        if (missingTags.length > 0) {
            suggestions.push({
                file: file.basename,
                path: file.path,
                existing: existingTags,
                missing: missingTags
            });
        }
    }

    // ========================================
    // GENERATE REPORT
    // ========================================

    let report = `# 🔄 Enhanced Tag Suggestion Report\n\n`;
    report += `**Generated**: ${new Date().toISOString().slice(0, 19).replace('T', ' ')}\n`;
    report += `**Taxonomy Used**: ${tagTaxonomy.name}\n`;
    report += `**Description**: ${tagTaxonomy.description}\n`;
    report += `**Folder Analyzed**: \`${folderPath}\`\n`;
    report += `**Files Processed**: ${files.length}\n`;
    report += `**Files with Suggestions**: ${suggestions.length}\n`;
    report += `**Coverage**: ${((files.length - suggestions.length) / files.length * 100).toFixed(1)}% properly tagged\n\n`;
    report += `---\n\n`;

    // Summary statistics
    report += `## 📊 Summary Statistics\n\n`;
    const tagTypes = ['domain', 'type', 'status', 'source', 'context', 'subdomain', 'maturity', 'complexity', 'model', 'mode'];
    tagTypes.forEach(tagType => {
        const needsTag = suggestions.filter(s =>
            s.missing.some(m => m.includes(`needs-${tagType}-tag`))
        ).length;
        if (needsTag > 0) {
            report += `- **Missing ${tagType} tags**: ${needsTag} files\n`;
        }
    });
    report += `\n---\n\n`;

    report += `## 📋 Detailed Suggestions\n\n`;

    suggestions.forEach((s, index) => {
        report += `### ${index + 1}. [[${s.file}]]\n\n`;
        report += `**Path**: \`${s.path}\`\n\n`;

        if (s.existing.length > 0) {
            report += `**Existing Tags**: ${s.existing.join(', ')}\n\n`;
        }

        report += `**Suggested Tags**:\n`;
        s.missing.forEach(tag => {
            report += `- ${tag}\n`;
        });
        report += `\n---\n\n`;
    });

    // Add taxonomy reference
    report += `## 📚 Taxonomy Reference\n\n`;
    report += `**Available in this taxonomy**:\n\n`;

    Object.entries(tagTaxonomy).forEach(([key, value]) => {
        if (Array.isArray(value) && value.length > 0) {
            report += `### ${key.charAt(0).toUpperCase() + key.slice(1)}\n`;
            report += `\`\`\`\n${value.join('\n')}\n\`\`\`\n\n`;
        }
    });

    // ========================================
    // SAVE REPORT
    // ========================================

    const reportFileName = `tag-suggestions_${folderPath.replace(/\//g, '-')}_${new Date().toISOString().slice(0, 10)}.md`;
    const reportPath = `99-system/reports/${reportFileName}`;

    // Ensure directory exists
    try {
        await app.vault.createFolder('99-system');
    } catch (e) { /* ignore */ }
    try {
        await app.vault.createFolder('99-system/reports');
    } catch (e) { /* ignore */ }

    await app.vault.create(reportPath, report);

    // Store for next step
    if (qa.variables) {
        qa.variables.reportPath = reportPath;
    }

    new Notice(`✅ Tag analysis complete! ${suggestions.length}/${files.length} files need attention. Report: ${reportFileName}`);

    // Open the report
    const reportFile = app.vault.getAbstractFileByPath(reportPath);
    if (reportFile) {
        await app.workspace.getLeaf().openFile(reportFile);
    }
};
