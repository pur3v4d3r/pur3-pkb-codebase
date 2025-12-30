// Modular Tag Taxonomy Library for Different Content Types
// Use these in your batch-tag-suggester.js or other scripts

const tagTaxonomies = {
    
    // 1. PKM/PKB General Notes (most comprehensive)
    pkmGeneral: {
        domains: [
            '#pkm', '#pkb', '#note-taking', '#knowledge-workflow', 
            '#obsidian', '#information-architecture', '#knowledge-graph',
            '#digital-garden', '#productivity'
        ],
        types: [
            '#type/fleeting', '#type/literature', '#type/permanent', 
            '#type/moc', '#type/reference', '#type/tutorial', 
            '#type/template', '#type/dashboard', '#type/framework'
        ],
        status: [
            '#status/seedling', '#status/budding', '#status/evergreen',
            '#status/review', '#status/archived', '#status/in-progress', '#status/complete'
        ],
        source: [
            '#source/book', '#source/article', '#source/blog', '#source/video',
            '#source/podcast', '#source/course', '#source/documentation',
            '#source/community', '#source/experience', '#source/original'
        ],
        context: [
            '#context/theoretical', '#context/practical', '#context/tutorial',
            '#context/reference', '#context/meta', '#context/experimental'
        ]
    },

    // 2. Psychology/Cognitive Science Notes
    psychologyCognitive: {
        domains: [
            '#cognitive-science', '#critical-thinking', '#self-regulation',
            '#learning-theory', '#self-improvement'
        ],
        types: [
            '#type/fleeting', '#type/literature', '#type/permanent',
            '#type/moc', '#type/practice-log', '#type/synthesis',
            '#type/technique', '#type/framework'
        ],
        status: [
            '#status/seedling', '#status/budding', '#status/evergreen',
            '#status/review', '#status/archived'
        ],
        source: [
            '#source/book', '#source/article', '#source/paper',
            '#source/course', '#source/podcast', '#source/video',
            '#source/experience', '#source/original'
        ],
        context: [
            '#context/theoretical', '#context/applied', '#context/personal',
            '#context/professional', '#context/teaching', '#context/research'
        ],
        mode: [
            '#mode/analytical', '#mode/synthetic', '#mode/reflective', '#mode/practical'
        ]
    },

    // 3. Prompt Engineering
    promptEngineering: {
        domains: [
            '#prompt-engineering', '#prompting-technique', '#prompt-pattern',
            '#llm-capability', '#llm-limitation', '#advanced-prompting',
            '#prompt-safety', '#context-management'
        ],
        types: [
            '#type/technique', '#type/pattern', '#type/template',
            '#type/experiment', '#type/analysis', '#type/literature',
            '#type/reference', '#type/case-study', '#type/tutorial',
            '#type/comparison', '#type/prompt-library'
        ],
        status: [
            '#status/experimental', '#status/proven', '#status/deprecated',
            '#status/under-revision', '#status/production', '#status/archived'
        ],
        maturity: [
            '#maturity/emerging', '#maturity/established',
            '#maturity/standard', '#maturity/deprecated'
        ],
        model: [
            '#model/claude', '#model/gpt', '#model/gemini',
            '#model/open-source', '#model/agnostic'
        ],
        complexity: [
            '#complexity/basic', '#complexity/intermediate',
            '#complexity/advanced', '#complexity/expert'
        ],
        validation: [
            '#validation/tested', '#validation/reported',
            '#validation/theoretical', '#validation/failed'
        ]
    },

    // 4. Books (Literature Notes)
    books: {
        domains: [
            '#cognitive-science', '#learning-theory', '#prompt-engineering',
            '#pkm', '#productivity', '#self-improvement'
        ],
        types: [
            '#type/literature', '#type/permanent', '#type/moc', '#type/synthesis'
        ],
        status: [
            '#status/to-read', '#status/reading', '#status/complete',
            '#status/review', '#status/archived'
        ],
        source: [
            '#source/book'
        ],
        readingStatus: [
            '#reading/to-read', '#reading/in-progress', '#reading/finished',
            '#reading/reference', '#reading/abandoned'
        ]
    },

    // 5. Obsidian System/Technical
    obsidianSystem: {
        domains: [
            '#obsidian', '#information-architecture', '#pkb'
        ],
        types: [
            '#type/reference', '#type/tutorial', '#type/template',
            '#type/dashboard', '#type/guide', '#type/framework'
        ],
        status: [
            '#status/in-progress', '#status/complete', '#status/review', '#status/archived'
        ],
        context: [
            '#context/meta', '#context/practical', '#context/tutorial', '#context/reference'
        ],
        component: [
            '#component/plugin', '#component/script', '#component/template',
            '#component/css', '#component/workflow', '#component/automation'
        ]
    },

    // 6. Projects
    projects: {
        domains: [
            '#project', '#productivity'
        ],
        types: [
            '#type/project', '#type/moc', '#type/dashboard', '#type/practice-log'
        ],
        status: [
            '#status/planning', '#status/active', '#status/on-hold',
            '#status/complete', '#status/archived'
        ],
        priority: [
            '#priority/high', '#priority/medium', '#priority/low'
        ],
        phase: [
            '#phase/ideation', '#phase/planning', '#phase/execution',
            '#phase/review', '#phase/maintenance'
        ]
    },

    // 7. Daily/Periodic Notes
    periodicNotes: {
        types: [
            '#type/daily', '#type/weekly', '#type/monthly',
            '#type/quarterly', '#type/yearly', '#type/reflection'
        ],
        context: [
            '#context/personal', '#context/professional', '#context/meta'
        ],
        mode: [
            '#mode/reflective', '#mode/planning', '#mode/review'
        ]
    },

    // 8. Research/Academic
    research: {
        domains: [
            '#cognitive-science', '#learning-theory', '#prompt-engineering'
        ],
        types: [
            '#type/literature', '#type/synthesis', '#type/analysis',
            '#type/framework', '#type/moc'
        ],
        status: [
            '#status/seedling', '#status/budding', '#status/evergreen',
            '#status/review'
        ],
        source: [
            '#source/paper', '#source/article', '#source/book',
            '#source/conference', '#source/course'
        ],
        context: [
            '#context/research', '#context/theoretical', '#context/applied'
        ],
        maturity: [
            '#maturity/beginner', '#maturity/intermediate',
            '#maturity/advanced', '#maturity/expert'
        ]
    },

    // 9. Learning/Education
    learning: {
        domains: [
            '#learning-theory', '#cognitive-science', '#self-improvement'
        ],
        types: [
            '#type/tutorial', '#type/guide', '#type/practice-log',
            '#type/technique', '#type/framework'
        ],
        status: [
            '#status/learning', '#status/practicing', '#status/mastered', '#status/review'
        ],
        source: [
            '#source/course', '#source/book', '#source/video',
            '#source/tutorial', '#source/practice'
        ],
        maturity: [
            '#maturity/beginner', '#maturity/intermediate', '#maturity/advanced'
        ],
        mode: [
            '#mode/learning', '#mode/practicing', '#mode/teaching'
        ]
    },

    // 10. Minimal (for quick captures/inbox)
    minimal: {
        types: [
            '#type/fleeting', '#type/inbox'
        ],
        status: [
            '#status/unprocessed', '#status/in-progress', '#status/complete'
        ],
        priority: [
            '#priority/high', '#priority/medium', '#priority/low'
        ]
    }
};

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = tagTaxonomies;
}
