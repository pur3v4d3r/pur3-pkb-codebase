// Generic framework type — covers the diverse JSON schemas in data/frameworks/

export interface Framework {
  id: string;
  name: string;
  shortName?: string;
  description?: string;
  version?: string;
  // Each framework has its own rich structure; keep it open
  [key: string]: unknown;
}

// ---- Template types ----

export type FieldType =
  | 'textarea'
  | 'text'
  | 'select'
  | 'multiselect'
  | 'scale'
  | 'checklist';

export interface TemplateField {
  id: string;
  label: string;
  type: FieldType;
  prompt?: string;
  options?: string[];
  required?: boolean;
  min?: number;
  max?: number;
  placeholder?: string;
}

export interface TemplateSection {
  id: string;
  title: string;
  description?: string;
  fields: TemplateField[];
}

export interface Template {
  id: string;
  name: string;
  description: string;
  framework?: string;
  difficulty?: 'beginner' | 'intermediate' | 'advanced';
  sections: TemplateSection[];
  [key: string]: unknown;
}

// ---- Exercise types ----

export type ExerciseType = 'reflection' | 'argument-analysis' | 'socratic' | 'fallacy-id' | 'scaffold';

export interface Exercise {
  id: string;
  title: string;
  type: ExerciseType;
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  estimatedMinutes: number;
  chapterRef?: number;
  frameworkRef?: string;
  description: string;
  instructions: string[];
}

// ---- Portfolio types ----

export interface PortfolioEntry {
  id: string;
  createdAt: string;
  updatedAt: string;
  type: 'template' | 'exercise' | 'reflection';
  title: string;
  templateId?: string;
  exerciseId?: string;
  chapterRef?: number;
  responses: Record<string, unknown>;
  tags: string[];
}
