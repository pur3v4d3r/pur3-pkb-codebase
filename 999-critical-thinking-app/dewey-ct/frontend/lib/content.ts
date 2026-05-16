import type { Chapter, ChapterSummary, CalloutType } from '@/types/chapter';
import type { Template, Framework, WorkedExample, PracticeProblem } from '@/types/framework';
import path from 'path';
import fs from 'fs';

// During SSG/SSR, read files directly from the filesystem.
// Public data lives at <project-root>/public/data/
const DATA_DIR = path.join(process.cwd(), 'public', 'data');

function readJSON<T>(relPath: string): T {
  const full = path.join(DATA_DIR, relPath);
  const raw = fs.readFileSync(full, 'utf-8');
  return JSON.parse(raw) as T;
}

// ---- Chapter loaders ----

export function getChapter(id: number): Chapter {
  const padded = String(id).padStart(2, '0');
  return readJSON<Chapter>(`chapters/chapter-${padded}.json`);
}

export function getAllChapters(): Chapter[] {
  const ids = Array.from({ length: 19 }, (_, i) => i + 1);
  return ids.map((id) => getChapter(id));
}

export function getChapterSummaries(): ChapterSummary[] {
  const chapters = getAllChapters();
  return chapters.map(chapterToSummary);
}

export function chapterToSummary(ch: Chapter): ChapterSummary {
  const calloutCounts = ch.callouts.reduce(
    (acc, c) => {
      acc[c.type as CalloutType] = (acc[c.type as CalloutType] ?? 0) + 1;
      return acc;
    },
    {} as Record<CalloutType, number>,
  );
  return {
    chapter: ch.chapter,
    title: ch.title,
    abstract: ch.abstract,
    conceptCount: ch.concepts.length,
    calloutCounts,
  };
}

// ---- Framework loaders ----

const FRAMEWORK_FILES = [
  'paul-elder',
  'blooms-taxonomy',
  'socratic-questioning',
  'toulmin-argument',
  'mental-models',
  'logical-fallacies',
  'dewey-five-phases',
  'ennis-framework',
  'delphi-consensus',
  'dual-process-theory',
  'habits-of-mind',
  'browne-keeley',
  'paul-elder-enrichments',
  'acer-critical-thinking',
  'acer-metacognitive',
  'developmental-models',
  'cognitive-biases',
  'cross-framework-synthesis',
  'siegel-reasons-conception',
  'halpern-critical-thinking',
  'webbs-depth-of-knowledge',
  'marzano-new-taxonomy',
  'solo-taxonomy',
  'watson-glaser',
  'cctdi',
  'walton-argumentation-schemes',
  'lipman-community-of-inquiry',
  'brookfield-critical-thinking',
  'dikw-pyramid',
  'bailin-reconception',
] as const;

export type FrameworkId = (typeof FRAMEWORK_FILES)[number];

export function getFramework(id: FrameworkId): Framework {
  return readJSON<Framework>(`frameworks/${id}.json`);
}

export function getAllFrameworks(): Framework[] {
  return FRAMEWORK_FILES.map((id) => getFramework(id));
}

// ---- Template loaders ----

const TEMPLATE_FILES = [
  'dewey-reflective-v1',
  'argument-analysis-v1',
  'blooms-scaffold-v1',
  'socratic-questioning-v1',
  'paul-elder-analysis-v1',
  'frisco-quick-analysis-v1',
  'see-i-elaboration-v1',
  'metacognitive-reflection-v1',
  'deliberate-practice-full-v1',
] as const;

export type TemplateId = (typeof TEMPLATE_FILES)[number];

export function getTemplate(id: TemplateId): Template {
  return readJSON<Template>(`templates/${id}.json`);
}

export function getAllTemplates(): Template[] {
  return TEMPLATE_FILES.map((id) => getTemplate(id));
}

// ---- Worked Example loaders ----

const WORKED_EXAMPLE_FILES = ['WE-01', 'WE-02', 'WE-03', 'WE-04', 'WE-05', 'WE-06', 'WE-07', 'WE-08', 'WE-09', 'WE-10', 'WE-11', 'WE-12'] as const;

export type WorkedExampleId = (typeof WORKED_EXAMPLE_FILES)[number];

export function getWorkedExample(id: WorkedExampleId): WorkedExample {
  return readJSON<WorkedExample>(`worked-examples/${id}.json`);
}

export function getAllWorkedExamples(): WorkedExample[] {
  return WORKED_EXAMPLE_FILES.map((id) => getWorkedExample(id));
}

// ---- Practice Problem loaders ----

const PRACTICE_PROBLEM_FILES = [
  'PP-01', 'PP-02', 'PP-03', 'PP-04',
  'PP-05', 'PP-06', 'PP-07', 'PP-08',
  'PP-09', 'PP-10', 'PP-11', 'PP-12',
  'PP-13', 'PP-14', 'PP-15', 'PP-16',
] as const;

export type PracticeProblemId = (typeof PRACTICE_PROBLEM_FILES)[number];

export function getPracticeProblem(id: PracticeProblemId): PracticeProblem {
  return readJSON<PracticeProblem>(`practice-problems/${id}.json`);
}

export function getAllPracticeProblems(): PracticeProblem[] {
  return PRACTICE_PROBLEM_FILES.map((id) => getPracticeProblem(id));
}

