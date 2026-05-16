import type { Chapter, ChapterSummary, CalloutType } from '@/types/chapter';
import type { Template, Framework } from '@/types/framework';
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
] as const;

export type TemplateId = (typeof TEMPLATE_FILES)[number];

export function getTemplate(id: TemplateId): Template {
  return readJSON<Template>(`templates/${id}.json`);
}

export function getAllTemplates(): Template[] {
  return TEMPLATE_FILES.map((id) => getTemplate(id));
}
