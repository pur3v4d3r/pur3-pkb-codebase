/**
 * QuickAdd Person Profile Finder
 * Fetches academic profile information and creates a person profile note
 * 
 * Usage: Add this as a Macro script in QuickAdd settings
 */

module.exports = async (params) => {
    const { quickAddApi: QuickAdd, app } = params;
    
    try {
        // Prompt for person name
        const personName = await QuickAdd.inputPrompt("Enter person name:");
        
        if (!personName) {
            new Notice("No name entered. Cancelled.");
            return;
        }
        
        new Notice(`Searching for ${personName}...`);
        
        // Fetch profile data
        const profile = await fetchPersonProfile(personName);
        
        if (!profile) {
            new Notice(`No profile found for ${personName}. Try a different name.`);
            return;
        }
        
        new Notice(`Found: ${profile.name}`);
        
        // Create the profile note
        const fileName = profile.name.replace(/[\\/:*?"<>|]/g, '_');
        const filePath = `${fileName}.md`;
        
        // Generate the note content
        const content = generateProfileContent(profile);
        
        // Create the file
        await app.vault.create(filePath, content);
        
        new Notice(`✓ Profile created: ${fileName}`);
        
        // Open the new file
        const file = app.vault.getAbstractFileByPath(filePath);
        if (file) {
            await app.workspace.getLeaf().openFile(file);
        }
        
    } catch (error) {
        console.error("Error in Person Profile Finder:", error);
        new Notice(`Error: ${error.message}`);
    }
};

/**
 * Fetch person profile from Semantic Scholar API
 */
async function fetchPersonProfile(name) {
    const baseUrl = "https://api.semanticscholar.org/graph/v1";
    
    try {
        // Search for author
        const searchUrl = `${baseUrl}/author/search?query=${encodeURIComponent(name)}&limit=1`;
        const searchResponse = await fetch(searchUrl);
        
        if (!searchResponse.ok) {
            throw new Error(`Search failed: ${searchResponse.status}`);
        }
        
        const searchData = await searchResponse.json();
        
        if (!searchData.data || searchData.data.length === 0) {
            return null;
        }
        
        const authorId = searchData.data[0].authorId;
        
        // Get detailed author information
        const authorUrl = `${baseUrl}/author/${authorId}?fields=name,aliases,affiliations,homepage,paperCount,citationCount,hIndex,papers,papers.title,papers.year,papers.citationCount,papers.venue,papers.publicationTypes,papers.abstract,papers.url,papers.journal`;
        const authorResponse = await fetch(authorUrl);
        
        if (!authorResponse.ok) {
            throw new Error(`Author fetch failed: ${authorResponse.status}`);
        }
        
        const authorData = await authorResponse.json();
        
        return compileProfile(authorData);
        
    } catch (error) {
        console.error("Error fetching profile:", error);
        throw error;
    }
}

/**
 * Compile profile data from API response
 */
function compileProfile(data) {
    const papers = processPapers(data.papers || []);
    const researchAreas = extractResearchAreas(data.papers || []);
    
    return {
        name: data.name || '',
        aliases: data.aliases || [],
        affiliations: (data.affiliations || []).filter(a => a),
        homepage: data.homepage || '',
        paperCount: data.paperCount || 0,
        citationCount: data.citationCount || 0,
        hIndex: data.hIndex || 0,
        papers: papers,
        researchAreas: researchAreas,
        primaryInstitution: (data.affiliations && data.affiliations.length > 0) ? data.affiliations[0] : ''
    };
}

/**
 * Process and sort papers by citation count
 */
function processPapers(papers) {
    const processed = papers.slice(0, 20).map(paper => {
        const pubTypes = paper.publicationTypes || [];
        const venue = (paper.venue || '').toLowerCase();
        const journal = paper.journal?.name?.toLowerCase() || '';
        
        let type = 'Article';
        if (pubTypes.includes('Book')) {
            type = 'Book';
        } else if (pubTypes.includes('JournalArticle') || journal) {
            type = 'Journal Article';
        } else if (pubTypes.includes('Conference') || venue.includes('proceedings')) {
            type = 'Conference Paper';
        } else if (pubTypes.includes('Review')) {
            type = 'Review';
        }
        
        return {
            title: paper.title || '',
            year: paper.year || '',
            citations: paper.citationCount || 0,
            venue: paper.venue || '',
            url: paper.url || '',
            abstract: paper.abstract || '',
            journal: paper.journal?.name || '',
            type: type
        };
    });
    
    // Sort by citation count
    processed.sort((a, b) => b.citations - a.citations);
    return processed;
}

/**
 * Extract research areas from paper venues
 */
function extractResearchAreas(papers) {
    const areas = new Set();
    
    papers.slice(0, 10).forEach(paper => {
        if (paper.venue) {
            areas.add(paper.venue);
        }
    });
    
    return Array.from(areas).slice(0, 5);
}

/**
 * Generate the profile content in Obsidian markdown format
 */
function generateProfileContent(profile) {
    const today = new Date().toISOString().split('T')[0];
    const topPapers = profile.papers.slice(0, 3);
    const researchArea1 = profile.researchAreas[0] || '';
    const researchArea2 = profile.researchAreas[1] || '';
    const aliasesStr = profile.aliases.length > 0 ? profile.aliases.slice(0, 3).map(a => `"${a}"`).join(', ') : '';
    
    return `---
type: person-profile
tags: #person #academic #researcher #intellectual-influence
person_type: researcher
primary_discipline: "${researchArea1}"
research_areas: 
  - "${researchArea1}"
  - "${researchArea2}"
status: active
institution: "${profile.primaryInstitution}"
website: "${profile.homepage}"
created: ${today}
aliases: [${aliasesStr}]
---

# ${profile.name}

> [!abstract] Academic Overview
> **Primary Role**: researcher
> **Discipline**: ${researchArea1}
> **Institution**: ${profile.primaryInstitution}
> **Research Focus**: ${profile.researchAreas.slice(0, 2).join(", ")}

---

## 👤 Biographical Context

**Education:**
- 
- 

**Career Highlights:**
- 
- 

**Current Position:**
${profile.affiliations[0] || ''}

**Notable Affiliations:**
- ${profile.affiliations.slice(0, 3).join('\n- ')}

**Research Metrics:**
- Total Publications: ${profile.paperCount}
- Total Citations: ${profile.citationCount}
- h-index: ${profile.hIndex}

---

## 🎓 Academic Contributions

### Primary Research Areas

**Area 1**: ${researchArea1}
- Core questions addressed:
- Methodological approach:
- Unique perspective/contribution:

**Area 2**: ${researchArea2}
- Core questions addressed:
- Methodological approach:
- Unique perspective/contribution:

### Key Publications

> [!evidence] Foundational Works

${topPapers.map((paper, i) => `**Publication ${i + 1}:**
- **Title**: ${paper.title}
- **Year**: ${paper.year}
- **Type**: ${paper.type}
- **Significance**: ${paper.citations} citations
- **Link**: ${paper.url}`).join('\n\n')}

### Theoretical Frameworks & Concepts

> [!key-claim] Major Contributions to Field

**Concept/Framework 1**: [[Concept Name]]
- **Description**: 
- **Origin**: [Which work introduced this]
- **Impact**: 
- **Critiques**: 

**Concept/Framework 2**: [[Concept Name]]
- **Description**: 
- **Origin**: 
- **Impact**: 
- **Critiques**: 

---

## 💡 Intellectual Influence

### Why I Admire Their Work

**Core Ideas That Resonate:**
1. 
2. 
3. 

**Methodological Lessons:**


**Conceptual Clarity:**


### How Their Work Informs Mine

> [!thought-experiment] Integration Points

**My Research Areas Influenced:**
- [[My Research Topic 1]]: 
- [[My Research Topic 2]]: 

**Frameworks I've Adopted:**
- 

**Questions They've Inspired Me to Explore:**
- 
- 

---

## 🔗 Intellectual Network

**Frequent Collaborators:**
- [[Collaborator 1]]
- [[Collaborator 2]]

**Intellectual Lineage:**
- **Mentors/Influences**: 
- **Students/Mentees**: 

**Academic Debates/Discourse:**
- **In dialogue with**: 
- **Critical responses to**: 
- **Building on work of**: 

---

## 📚 Reading Notes & Synthesis

### Works I've Read
\`\`\`dataview
TABLE 
  file.link AS "Note",
  author AS "Author",
  year AS "Year",
  type AS "Type"
FROM [[${profile.name}]]
WHERE type = "literature-note" OR contains(file.tags, "literature-note")
SORT year DESC
\`\`\`

### Key Quotes & Concepts

> [!quote] Notable Quote 1
> "Quote text here"
> 
> **Source**: [Publication/Context]
> **Significance**: 

> [!quote] Notable Quote 2
> "Quote text here"
> 
> **Source**: 
> **Significance**: 

---

## 🎯 Further Exploration

**Works I Want to Read:**
- [ ] [Publication title]
- [ ] [Publication title]

**Talks/Lectures to Watch:**
- [ ] [Talk title] - [Link]

**Research Questions to Investigate:**
- 
- 

**Related Scholars to Explore:**
- [[Person Name 1]]
- [[Person Name 2]]

---

## 🔖 External Resources

**Primary Website**: ${profile.homepage}

**Academic Profiles:**
- Google Scholar: 
- ORCID: 
- ResearchGate: 
- Academia.edu: 

**Social/Public Scholarship:**
- Twitter/X: 
- Blog: 
- Podcast Appearances: 

**Institutional Profile**: 

---

## 📝 Personal Notes & Reflections



---

*Profile Created: ${today}*
*Last Updated: ${today}*
`;
}
