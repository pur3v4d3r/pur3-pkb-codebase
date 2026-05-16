// Types derived from the _dewey_ch*.json schema

export type CalloutType = 'quote' | 'concept' | 'warning' | 'tip' | 'synthesis';

export interface QuoteCallout {
  type: 'quote';
  line_hint: string;
  quote: string;
  insight: string;
}

export interface ConceptCallout {
  type: 'concept';
  concept_name: string;
  definition: string;
  why_it_matters: string;
  modern_echo: string;
}

export interface WarningCallout {
  type: 'warning';
  misconception: string;
  correction: string;
  still_relevant: string;
}

export interface TipCallout {
  type: 'tip';
  principle: string;
  in_practice: string;
}

export interface SynthesisCallout {
  type: 'synthesis';
  central_argument: string;
  logical_progression: string[];
  bridge_to_next: string;
}

export type Callout =
  | QuoteCallout
  | ConceptCallout
  | WarningCallout
  | TipCallout
  | SynthesisCallout;

export interface ChapterConcept {
  name: string;
  definition: string;
}

export interface ChapterConnectionRef {
  chapter: number | null;
  reason: string;
}

export interface ChapterContrastRef {
  concept: string;
  reason: string;
}

export interface ChapterConnections {
  builds_on: ChapterConnectionRef[];
  anticipates: ChapterConnectionRef[];
  contrasts_with: ChapterContrastRef[];
}

export interface Chapter {
  chapter: number;
  title: string;
  abstract: string;
  overview: string;
  callouts: Callout[];
  concepts: ChapterConcept[];
  connections: ChapterConnections;
}

// Lightweight version for listing/cards (no full callout text)
export interface ChapterSummary {
  chapter: number;
  title: string;
  abstract: string;
  conceptCount: number;
  calloutCounts: Record<CalloutType, number>;
}
