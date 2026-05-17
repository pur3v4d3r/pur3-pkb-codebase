/**
 * Static mapping of Dewey chapters → modern CT framework concepts.
 * Derived from cross-framework-synthesis.json + chapter abstracts.
 * Each tag points to a framework page in the app.
 */

export interface CrosswalkTag {
  framework: string;
  concept: string;
  href: string;
}

export interface ChapterCrosswalk {
  chapter: number;
  tags: CrosswalkTag[];
}

const CROSSWALK: ChapterCrosswalk[] = [
  {
    chapter: 1,
    tags: [
      { framework: 'Paul-Elder', concept: 'Element: Inference', href: '/frameworks/paul-elder' },
      { framework: 'Delphi', concept: 'Skill: Self-Regulation', href: '/frameworks/delphi-consensus' },
      { framework: 'Ennis', concept: 'Disp: Be Reflective', href: '/frameworks/ennis-framework' },
      { framework: 'Metacognition', concept: 'Monitoring cognition', href: '/frameworks/acer-metacognitive' },
    ],
  },
  {
    chapter: 2,
    tags: [
      { framework: 'Paul-Elder', concept: 'Virtue: Fair-mindedness', href: '/frameworks/paul-elder' },
      { framework: 'Paul-Elder', concept: 'Virtue: Intellectual Humility', href: '/frameworks/paul-elder' },
      { framework: 'Ennis', concept: 'Disp: Open-mindedness', href: '/frameworks/ennis-framework' },
      { framework: 'Delphi', concept: 'Disp: Open-mindedness', href: '/frameworks/delphi-consensus' },
    ],
  },
  {
    chapter: 3,
    tags: [
      { framework: 'Delphi', concept: 'Disp: Inquisitiveness', href: '/frameworks/delphi-consensus' },
      { framework: 'Ennis', concept: 'Disp: Truth-seeking', href: '/frameworks/ennis-framework' },
      { framework: 'Paul-Elder', concept: 'Virtue: Intellectual Curiosity', href: '/frameworks/paul-elder' },
      { framework: 'Habits of Mind', concept: 'Questioning & posing problems', href: '/frameworks/habits-of-mind' },
    ],
  },
  {
    chapter: 4,
    tags: [
      { framework: 'Lipman', concept: 'Community of Inquiry', href: '/frameworks/lipman-community-of-inquiry' },
      { framework: 'Brookfield', concept: 'Social dimension of CT', href: '/frameworks/brookfield-critical-thinking' },
      { framework: 'Ennis', concept: 'Disp: Seek interaction', href: '/frameworks/ennis-framework' },
    ],
  },
  {
    chapter: 5,
    tags: [
      { framework: 'Paul-Elder', concept: 'Standards: Logic', href: '/frameworks/paul-elder' },
      { framework: 'Delphi', concept: 'Skill: Analysis', href: '/frameworks/delphi-consensus' },
      { framework: 'Ennis', concept: 'Skill: Analyze arguments', href: '/frameworks/ennis-framework' },
      { framework: 'Toulmin', concept: 'Warrant / Backing', href: '/frameworks/toulmin-argument' },
    ],
  },
  {
    chapter: 6,
    tags: [
      { framework: 'Paul-Elder', concept: 'Standards: Accuracy, Logic', href: '/frameworks/paul-elder' },
      { framework: 'Delphi', concept: 'Skill: Evaluation', href: '/frameworks/delphi-consensus' },
      { framework: 'Ennis', concept: 'Skill: Assess evidential claims', href: '/frameworks/ennis-framework' },
    ],
  },
  {
    chapter: 7,
    tags: [
      { framework: 'Dewey 5-Phase', concept: 'All phases', href: '/frameworks/dewey-five-phases' },
      { framework: 'Paul-Elder', concept: 'All 8 elements', href: '/frameworks/paul-elder' },
      { framework: 'Delphi', concept: 'All 6 core skills', href: '/frameworks/delphi-consensus' },
      { framework: 'Halpern', concept: 'Problem-solving cycle', href: '/frameworks/halpern-critical-thinking' },
    ],
  },
  {
    chapter: 8,
    tags: [
      { framework: 'Paul-Elder', concept: 'Element: Judgments', href: '/frameworks/paul-elder' },
      { framework: 'Delphi', concept: 'Skill: Evaluation', href: '/frameworks/delphi-consensus' },
      { framework: 'Ennis', concept: 'Skill: Judge quality of evidence', href: '/frameworks/ennis-framework' },
      { framework: 'Dual-Process', concept: 'System 2 deliberation', href: '/frameworks/dual-process-theory' },
    ],
  },
  {
    chapter: 9,
    tags: [
      { framework: 'Paul-Elder', concept: 'Element: Concepts', href: '/frameworks/paul-elder' },
      { framework: 'Delphi', concept: 'Skill: Interpretation', href: '/frameworks/delphi-consensus' },
      { framework: "Browne-Keeley", concept: 'Ambiguous language', href: '/frameworks/browne-keeley' },
      { framework: 'Ennis', concept: 'Disp: Seek clarity of thesis', href: '/frameworks/ennis-framework' },
    ],
  },
  {
    chapter: 10,
    tags: [
      { framework: 'Paul-Elder', concept: 'Standards: Clarity, Precision', href: '/frameworks/paul-elder' },
      { framework: 'Delphi', concept: 'Skill: Interpretation', href: '/frameworks/delphi-consensus' },
      { framework: 'Ennis', concept: 'Disp: Seek precise questions', href: '/frameworks/ennis-framework' },
      { framework: 'Bloom', concept: 'Level: Understand (define)', href: '/frameworks/blooms-taxonomy' },
    ],
  },
  {
    chapter: 11,
    tags: [
      { framework: 'Paul-Elder', concept: 'Standards: Accuracy, Evidence', href: '/frameworks/paul-elder' },
      { framework: 'Delphi', concept: 'Skill: Evaluation', href: '/frameworks/delphi-consensus' },
      { framework: 'Ennis', concept: 'Skill: Judge credibility of sources', href: '/frameworks/ennis-framework' },
      { framework: 'Halpern', concept: 'Hypothesis testing', href: '/frameworks/halpern-critical-thinking' },
    ],
  },
  {
    chapter: 12,
    tags: [
      { framework: 'Paul-Elder', concept: 'Standards: Logic, Breadth', href: '/frameworks/paul-elder' },
      { framework: 'Toulmin', concept: 'Warrant, Backing, Rebuttal', href: '/frameworks/toulmin-argument' },
      { framework: 'Ennis', concept: 'Skill: Deductive inference', href: '/frameworks/ennis-framework' },
      { framework: 'Walton', concept: 'Argumentation schemes', href: '/frameworks/walton-argumentation-schemes' },
    ],
  },
  {
    chapter: 13,
    tags: [
      { framework: 'Paul-Elder', concept: 'Standards: Accuracy, Depth', href: '/frameworks/paul-elder' },
      { framework: 'Delphi', concept: 'Skill: Inference + Analysis', href: '/frameworks/delphi-consensus' },
      { framework: 'Bloom', concept: 'Level: Analyze & Evaluate', href: '/frameworks/blooms-taxonomy' },
      { framework: 'Marzano', concept: 'Analysis system', href: '/frameworks/marzano-new-taxonomy' },
    ],
  },
  {
    chapter: 14,
    tags: [
      { framework: 'Bloom', concept: 'Level: Apply', href: '/frameworks/blooms-taxonomy' },
      { framework: 'Habits of Mind', concept: 'Applying past knowledge', href: '/frameworks/habits-of-mind' },
      { framework: 'Delphi', concept: 'Disp: Systematic', href: '/frameworks/delphi-consensus' },
    ],
  },
  {
    chapter: 15,
    tags: [
      { framework: 'Bloom', concept: 'Level: Evaluate & Create', href: '/frameworks/blooms-taxonomy' },
      { framework: 'SOLO Taxonomy', concept: 'Relational → Extended abstract', href: '/frameworks/solo-taxonomy' },
      { framework: 'Marzano', concept: 'Knowledge utilization', href: '/frameworks/marzano-new-taxonomy' },
    ],
  },
  {
    chapter: 16,
    tags: [
      { framework: 'Paul-Elder', concept: 'Standards: Clarity, Precision', href: '/frameworks/paul-elder' },
      { framework: 'Delphi', concept: 'Skill: Interpretation', href: '/frameworks/delphi-consensus' },
      { framework: 'Lipman', concept: 'Language in inquiry', href: '/frameworks/lipman-community-of-inquiry' },
    ],
  },
  {
    chapter: 17,
    tags: [
      { framework: 'Paul-Elder', concept: 'Element: Information', href: '/frameworks/paul-elder' },
      { framework: 'Ennis', concept: 'Skill: Seek credible sources', href: '/frameworks/ennis-framework' },
      { framework: 'Delphi', concept: 'Skill: Evaluation', href: '/frameworks/delphi-consensus' },
    ],
  },
  {
    chapter: 18,
    tags: [
      { framework: 'Socratic Questioning', concept: 'Probing questions', href: '/frameworks/socratic-questioning' },
      { framework: 'Lipman', concept: 'Community of Inquiry', href: '/frameworks/lipman-community-of-inquiry' },
      { framework: 'Brookfield', concept: 'Critical questioning', href: '/frameworks/brookfield-critical-thinking' },
    ],
  },
  {
    chapter: 19,
    tags: [
      { framework: 'Delphi', concept: 'Skill: Self-Regulation', href: '/frameworks/delphi-consensus' },
      { framework: 'Paul-Elder', concept: 'Intellectual virtues (synthesis)', href: '/frameworks/paul-elder' },
      { framework: 'Metacognition', concept: 'Transfer & self-direction', href: '/frameworks/acer-metacognitive' },
    ],
  },
];

const CROSSWALK_MAP = new Map<number, ChapterCrosswalk>(
  CROSSWALK.map((c) => [c.chapter, c]),
);

export function getCrosswalk(chapterNum: number): ChapterCrosswalk | undefined {
  return CROSSWALK_MAP.get(chapterNum);
}
