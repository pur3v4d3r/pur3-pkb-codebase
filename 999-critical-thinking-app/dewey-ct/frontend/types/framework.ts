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

// ---- Worked Example types ----

export interface WorkedExampleSection {
  section_label: string;
  content?: string;
  fields?: Array<{ label: string; content: string }>;
}

export interface WorkedExample {
  id: string;
  we_number: string;
  title: string;
  subtitle?: string;
  framework: string;
  framework_label: string;
  object_type: string;
  question_type?: string;
  stakes?: string;
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  duration_minutes: number;
  pre_confidence?: number;
  post_confidence?: number;
  rigor_score?: number;
  mastery_rating?: number;
  tags: string[];
  summary: string;
  how_to_use: string;
  learning_objectives: string[];
  related_template_id?: string;
  related_practice_problems?: string[];
  sections: WorkedExampleSection[];
  [key: string]: unknown;
}

// ---- Practice Problem types ----

export interface PracticeProblemHint {
  id: string;
  title: string;
  content: string;
}

export interface PracticeProblem {
  id: string;
  pp_number: string;
  title: string;
  framework: string;
  framework_label: string;
  object_type: string;
  difficulty: 'easy' | 'medium' | 'hard';
  estimated_minutes: number;
  related_worked_example_id?: string | null;
  related_template_id?: string | null;
  tags: string[];
  object_of_analysis: string;
  context?: string;
  instructions: string;
  workspace_prompts?: Record<string, string>;
  hints: PracticeProblemHint[];
  solution_sketch: {
    key_moves: string[];
    revised_position?: string;
  };
  template_prefill?: {
    template_id: string;
    subject_value?: string;
    context_note: string;
  } | null;
  [key: string]: unknown;
}

