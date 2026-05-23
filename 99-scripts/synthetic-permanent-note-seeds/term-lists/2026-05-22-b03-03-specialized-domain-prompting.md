---
batch_name: b03-03-specialized-domain-prompting
batch_date: 2026-05-22
default_domain: prompt-engineering
default_confidence: high
notes: |
  Fifteen domain-specific prompting strategies: medical/clinical, legal,
  scientific hypothesis generation, mathematical proof, code generation,
  code review, financial analysis, educational content, creative writing,
  technical documentation, data analysis, ethical reasoning, historical
  reasoning, philosophical argument, and cybersecurity analysis.
---

# Batch: B03-03 Specialized Domain Prompting

## Medical Clinical Prompting

- secondary_domains: [large-language-models, clinical-ai, healthcare-ai, prompt-engineering]
- aliases: [clinical LLM prompting, healthcare AI prompting, medical reasoning prompts]
- broader: [specialized-domain-prompting, clinical-ai, prompt-engineering]
- related: [ethical-reasoning-prompting, hallucination-in-llms, retrieval-augmented-generation, claim-strength-calibration]
- prerequisites: [prompt-engineering, clinical-decision-support, large-language-models]
- confidence: high

**definition**: Medical Clinical Prompting refers to the specialised prompting strategies, safety constraints, and output design patterns used to elicit accurate, safe, and clinically useful responses from large language models in medical and healthcare contexts — including differential diagnosis support, clinical note synthesis, patient communication drafting, medication interaction checking, clinical guideline interpretation, and medical education. Medical clinical prompting must account for the catastrophic-consequence nature of clinical errors, the requirement for rigorous source citation, the need to maintain appropriate scope of practice boundaries, the diversity of clinical audiences (specialists, generalists, patients), and the regulatory constraints on clinical AI use. It incorporates explicit uncertainty quantification, mandatory escalation cues, and strict out-of-scope refusal patterns.

**key_claim**: Medical Clinical Prompting effectiveness is determined primarily by the specificity of clinical context provided in the prompt — prompts that include patient demographics, presenting complaint, relevant history, current medications, and recent investigations produce substantially more clinically relevant differential diagnoses and recommendations than prompts that provide only a chief complaint, because clinical reasoning is inherently patient-specific and LLMs perform as pattern matchers on clinical context features; sparse clinical context produces generic textbook responses that are technically correct but clinically uninformative, while rich clinical context elicits the contextual specificity that makes LLM output clinically actionable.

**warning**: Medical Clinical Prompting must never use LLM outputs as the primary or sole clinical decision basis — LLMs are not certified medical devices, have not been validated on representative clinical populations, do not have access to real-time clinical evidence updates, and produce confident outputs for clinical questions that are outside their reliable knowledge range without reliable self-awareness of these limitations; any medical clinical prompting deployment must include mandatory human clinical oversight, explicit scope limitations communicated to all users, and regular calibration validation against current clinical guidelines.

## Legal Reasoning Prompting

- secondary_domains: [large-language-models, legal-ai, jurisprudence, prompt-engineering]
- aliases: [legal LLM prompting, law application prompting, statutory reasoning prompts]
- broader: [specialized-domain-prompting, legal-ai, prompt-engineering]
- related: [ethical-reasoning-prompting, claim-strength-calibration, logical-entailment-verification, domain-adaptive-pretraining]
- prerequisites: [prompt-engineering, legal-reasoning, large-language-models]
- confidence: high

**definition**: Legal Reasoning Prompting refers to the prompting strategies and output design patterns adapted for legal analysis tasks — including statutory interpretation, case law analysis, contract review, legal argument construction, jurisdiction-specific compliance checking, and legal document drafting. Legal reasoning prompting must account for the jurisdiction-specificity of law (the same legal question may have different answers under different legal systems), the precedent-based nature of common law reasoning (relevant case holdings must be cited and distinguished), the formal requirements for legal documents (specific language, structure, and procedural requirements), and the prohibition on LLMs providing legal advice without appropriate professional oversight. Effective legal reasoning prompts specify the applicable jurisdiction, the specific legal question, the relevant legal framework, the available facts, and the required output format.

**key_claim**: Legal Reasoning Prompting performance degrades dramatically without explicit jurisdiction specification — LLMs trained on legal text from multiple jurisdictions (US federal, US state, UK, EU, Australian, etc.) default to a blend of legal systems that may be inconsistent or inapplicable when a specific jurisdiction's law is required; providing the specific jurisdiction, applicable statute versions, and current case law citations as context anchors substantially improves jurisdictional accuracy and reduces the rate of legal errors caused by cross-jurisdictional contamination.

**warning**: Legal Reasoning Prompting outputs must be treated as legal research assistance, not legal advice — LLMs confidently produce plausible-seeming legal analyses that contain substantive errors including misquoted statutes, incorrectly stated holdings, fabricated citations, and outdated precedents, at rates that would be professionally unacceptable without expert review; all legal reasoning prompting outputs must be reviewed by qualified legal professionals before reliance, and no LLM legal analysis output should be communicated to clients or used in court filings without independent verification by a licensed attorney.

## Scientific Hypothesis Generation

- secondary_domains: [large-language-models, scientific-methodology, research-design, prompt-engineering]
- aliases: [research hypothesis generation, scientific abduction prompting, scientific ideation prompts]
- broader: [specialized-domain-prompting, scientific-ai, prompt-engineering]
- related: [domain-adaptive-pretraining, claim-strength-calibration, counterfactual-data-augmentation, chain-of-thought-prompting]
- prerequisites: [scientific-methodology, prompt-engineering, large-language-models]
- confidence: high

**definition**: Scientific Hypothesis Generation via LLMs refers to the use of large language models to propose testable scientific hypotheses — identifying gaps in existing literature, generating mechanistic explanations for observed phenomena, proposing experimental designs, and synthesising findings across related domains to suggest novel research directions. LLMs bring complementary strengths to hypothesis generation: broad cross-domain knowledge that enables unexpected cross-disciplinary connections, rapid synthesis of large literature bodies, and systematic enumeration of hypothesis spaces. Effective scientific hypothesis generation prompting provides the LLM with background on the target domain, known mechanisms, unresolved questions, and constraints on feasible hypotheses, then elicits structured hypotheses with testability criteria and differentiation from existing explanations.

**key_claim**: Scientific Hypothesis Generation prompting is most valuable for cross-domain hypothesis transfer — LLMs are more effective than domain experts at generating hypotheses that apply mechanisms from one domain to problems in an adjacent domain (e.g., applying computational network theory to neuroscience) because the model's breadth of training allows cross-domain analogical reasoning that is cognitively difficult for specialists with deep but narrow expertise; domain experts using LLMs for hypothesis generation should therefore specifically prompt for cross-domain mechanism transfer rather than within-domain hypothesis extension, where the LLM's advantage over expert intuition is smaller.

**warning**: Scientific Hypothesis Generation by LLMs produces highly plausible-sounding hypotheses that may already be documented in the literature, may be theoretically motivated but empirically refuted, or may be inconsistent with established constraints in the domain — LLMs cannot reliably distinguish novel from already-tested hypotheses because their training data does not include comprehensive negative results and because false negative results are under-represented in published literature; every LLM-generated scientific hypothesis must be systematically checked against existing literature before investing experimental resources.

## Mathematical Proof Prompting

- secondary_domains: [large-language-models, formal-mathematics, theorem-proving, prompt-engineering]
- aliases: [proof generation prompting, formal reasoning in LLMs, mathematical deduction prompts]
- broader: [specialized-domain-prompting, mathematical-ai, prompt-engineering]
- related: [logical-entailment-verification, chain-of-thought-prompting, formal-verification, code-generation-prompting]
- prerequisites: [formal-mathematics, proof-theory, prompt-engineering, large-language-models]
- confidence: high

**definition**: Mathematical Proof Prompting refers to the prompting strategies used to elicit formal mathematical arguments, proofs, and derivations from large language models — guiding the model to construct step-by-step logical arguments that establish mathematical claims from axioms or given premises through valid inference rules. Mathematical proof prompting must account for the strict validity requirements of formal proof (each step must follow from preceding steps by an explicitly identified rule), the diverse proof strategies (direct, contradiction, induction, construction, probabilistic), and the failure modes specific to mathematical LLM output (plausible-looking but invalid reasoning steps, incorrect use of quantifiers, missing case analysis, and circular arguments presented as if valid).

**key_claim**: Mathematical Proof Prompting is most reliable when the model is instructed to produce machine-verifiable formal proofs in a specified proof language (e.g., Lean, Coq, Isabelle) rather than natural language proofs — natural language proofs allow the model to introduce subtly invalid reasoning steps that appear valid due to imprecision in natural language quantification and inference language, while formal proof languages require explicit logical justification at each step that can be mechanically checked; the additional prompting overhead of specifying a formal proof language and syntax is outweighed by the dramatic reduction in undetected reasoning errors that formal verification provides.

**warning**: Mathematical Proof Prompting using natural language produces outputs that are frequently incorrect in ways that are difficult to detect without mathematical expertise — models commonly produce proofs that have the correct high-level structure and individual steps that appear plausible but contain specific steps where the logical validity breaks down in subtle ways (e.g., applying a theorem outside its stated conditions, making an existential claim without providing a witness, or assuming symmetry without proving it); users without strong mathematical expertise should not trust LLM-generated proofs without independent verification by a mathematician or a formal verification tool.

## Code Generation Prompting

- secondary_domains: [large-language-models, software-engineering, prompt-engineering]
- aliases: [code synthesis prompting, program generation prompts, LLM programming assistance]
- broader: [specialized-domain-prompting, code-generation, prompt-engineering]
- related: [code-review-prompting, technical-documentation-prompting, mathematical-proof-prompting, data-analysis-prompting]
- prerequisites: [prompt-engineering, software-engineering, large-language-models]
- confidence: high

**definition**: Code Generation Prompting refers to the specialised prompting strategies for eliciting correct, efficient, secure, and maintainable code from large language models — including function implementation, algorithm design, data structure selection, API usage, testing, refactoring, and debugging. Effective code generation prompting specifies the programming language and version, the precise functional requirements, the performance constraints, the target coding style or framework, example inputs and expected outputs, and the edge cases to handle. Advanced code generation prompting incorporates test-driven development patterns (provide tests before requesting implementation), incremental elaboration (request skeleton then fill in details), and self-verification (request code that includes its own tests or asserts).

**key_claim**: Code Generation Prompting with test-driven prompting (specifying test cases before requesting implementation) produces substantially higher correctness rates than specification-first prompting (describing functionality without test cases) — providing concrete input-output examples forces the model to reason about specific edge cases and boundary conditions rather than generating implementations optimised for the most common case, resulting in code that handles edge cases the model would otherwise miss; providing three to five test cases including at least one boundary case and one error case in the prompt reduces first-generation correctness failures by approximately 40–60% across common programming tasks.

**warning**: Code Generation Prompting produces code that is syntactically correct and passes superficial review at much higher rates than it produces code that is semantically correct under adversarial inputs or correct in edge cases — LLMs generate confident, well-formatted code for inputs similar to training data but produce subtly incorrect implementations for algorithmic requirements that require careful boundary condition analysis, correct error handling for rare failure modes, and secure input validation; all LLM-generated code must be tested against a comprehensive test suite including adversarial and edge-case inputs before deployment, as code review alone is insufficient to catch the category of errors LLMs most commonly make.

## Code Review Prompting

- secondary_domains: [large-language-models, software-engineering, prompt-engineering, security]
- aliases: [LLM code audit prompting, automated code review, AI code inspection prompting]
- broader: [specialized-domain-prompting, code-review, prompt-engineering]
- related: [code-generation-prompting, cybersecurity-analysis-prompting, logical-entailment-verification, data-analysis-prompting]
- prerequisites: [prompt-engineering, software-engineering, security-review, large-language-models]
- confidence: high

**definition**: Code Review Prompting refers to the prompting strategies used to direct large language models to systematically analyse code for correctness, security vulnerabilities, performance inefficiencies, maintainability issues, and style violations — functioning as an automated first-pass code reviewer that identifies issues before human review. Effective code review prompting specifies the review scope (security only, performance only, full review), the target language and framework version, the security threat model, the performance constraints, the team's style guide or coding conventions, and the output format (inline comments, categorised issue list, ranked findings). Advanced code review prompting employs adversarial mindset instruction (asking the model to assume the role of an attacker looking for vulnerabilities) to surface security issues that passive correctness review misses.

**key_claim**: Code Review Prompting with explicit security-focused prompts discovers substantially more security vulnerabilities than correctness-focused prompts on the same code — adversarial security prompts that instruct the model to "identify all possible inputs that could cause security vulnerabilities, including injection attacks, buffer overflows, authentication bypasses, and information disclosure" surface vulnerabilities at rates 2–3x higher than generic "review this code" prompts, because security review requires adversarial reasoning that generic review prompts do not elicit; security-specific code review prompting should be a distinct pipeline stage from correctness review rather than a combined prompt.

**warning**: Code Review Prompting produces false positives (identifying issues that are not real problems) at higher rates than false negatives (missing real issues) for security vulnerabilities — LLMs trained on security literature learn to flag patterns associated with vulnerabilities even when the specific code instance is not exploitable due to surrounding context that the model has not adequately weighted; human security engineers reviewing LLM code review outputs must be prepared for a substantial false positive rate and should treat LLM findings as candidates requiring confirmation rather than confirmed vulnerabilities.

## Financial Analysis Prompting

- secondary_domains: [large-language-models, financial-analysis, prompt-engineering, quantitative-finance]
- aliases: [financial LLM prompting, investment analysis prompting, quantitative finance prompts]
- broader: [specialized-domain-prompting, financial-ai, prompt-engineering]
- related: [data-analysis-prompting, ethical-reasoning-prompting, claim-strength-calibration, risk-communication]
- prerequisites: [prompt-engineering, financial-analysis, large-language-models]
- confidence: high

**definition**: Financial Analysis Prompting refers to the prompting strategies adapted for financial analysis tasks — including financial statement interpretation, ratio analysis, valuation modelling, market trend identification, risk assessment, investment thesis construction, regulatory compliance checking, and financial narrative drafting. Financial analysis prompting must address the temporal sensitivity of financial data (LLM training cutoffs mean financial data may be outdated), the quantitative precision requirements of financial calculations, the regulatory constraints on financial advice communication, and the institutional specificity of financial analysis (different analyst types require different frameworks and output conventions). Effective financial analysis prompting provides current financial data as context (rather than relying on model memory), specifies the analytical framework, and structures quantitative outputs in verifiable formats.

**key_claim**: Financial Analysis Prompting is most reliable when financial data is explicitly provided as structured context rather than requested from the model's parametric memory — LLMs retain financial figures from training data that are outdated by months to years, and when prompted to "analyse company X's financial performance" without current data, produce analyses that mix accurate structural commentary with potentially outdated quantitative figures; providing current financial statements directly in the prompt context reduces quantitative error rates substantially and allows the model's analytical capabilities (ratio interpretation, trend identification, comparative analysis) to operate on accurate data rather than potentially stale memorised figures.

**warning**: Financial Analysis Prompting must include explicit regulatory and scope-of-practice guardrails — many financial analysis outputs that are appropriate for institutional analyst contexts constitute regulated financial advice when provided to retail investors, and LLMs do not reliably distinguish between these contexts without explicit instruction; deployments providing financial analysis prompting outputs to end users must include explicit scope limitations, disclaimers about the absence of personalised advice, and guidance to seek qualified financial advisors for investment decisions.

## Educational Content Prompting

- secondary_domains: [large-language-models, educational-technology, pedagogy, prompt-engineering]
- aliases: [pedagogical prompting, educational AI prompting, learning content generation]
- broader: [specialized-domain-prompting, educational-ai, prompt-engineering]
- related: [abstraction-level-control, register-and-tone-control, specificity-vs-generality-tradeoff, audience-calibration]
- prerequisites: [pedagogy, cognitive-load-theory, prompt-engineering, large-language-models]
- confidence: high

**definition**: Educational Content Prompting refers to the prompting strategies and design patterns used to elicit pedagogically effective educational materials from large language models — including explanations, worked examples, analogies, exercises, assessments, scaffolded progressions, and feedback — calibrated to specific learning objectives, student knowledge levels, and pedagogical frameworks. Educational content prompting incorporates principles from learning science: specifying the student's prior knowledge and zone of proximal development, designing for spaced repetition and retrieval practice, structuring content for cognitive load management, and adapting instructional strategy (direct instruction, guided discovery, problem-based learning) to content type and student level. It is distinguished from general-purpose explanation prompting by its systematic attention to learning outcome achievement rather than information transmission.

**key_claim**: Educational Content Prompting that specifies learning objectives in behavioural terms ("after this explanation, the student will be able to solve X type problem by applying Y procedure") produces substantially more pedagogically effective materials than prompting that specifies topic coverage ("explain X") — behavioural objective specification forces the model to generate content that builds toward demonstrable competence rather than content that describes concepts, producing explanations that include worked examples, practice problems, and explicit competence tests that general-topic explanations omit; this distinction between topic-coverage and competence-building prompting is the primary differentiator between educational content that produces learning and educational content that produces the illusion of learning.

**warning**: Educational Content Prompting can produce pedagogically plausible content that embeds subtle misconceptions at rates higher than expert-authored educational materials — LLMs trained on a mix of correct and partially-correct educational text learn to generate plausible explanations that contain the common misconceptions present in low-quality educational sources; subject-matter expert review is required for all LLM-generated educational content before deployment, with particular attention to procedural explanations and conceptual analogies that are the most common vehicles for embedded misconceptions.

## Creative Writing Prompting

- secondary_domains: [large-language-models, creative-writing, narrative-design, prompt-engineering]
- aliases: [literary generation prompting, fiction writing prompts, creative AI prompting]
- broader: [specialized-domain-prompting, creative-ai, prompt-engineering]
- related: [narrative-consistency-prompting, register-and-tone-control, abstraction-level-control, stance-consistency-across-output]
- prerequisites: [creative-writing-craft, prompt-engineering, large-language-models]
- confidence: high

**definition**: Creative Writing Prompting refers to the prompting strategies and iterative generation techniques used to elicit high-quality literary and narrative content from large language models — including fiction, poetry, screenwriting, lyric writing, interactive narrative, and creative non-fiction. Creative writing prompting encompasses genre specification, narrative structure design, character development, voice and style calibration, tension and pacing management, and the management of creative constraint systems (formal poetry constraints, genre conventions, world-building rules). Unlike task-oriented prompting that specifies outputs precisely, creative writing prompting often involves strategic under-specification to enable creative generation while maintaining narrative coherence, combined with iterative refinement through critique-and-revision cycles that progressively improve output toward the desired quality target.

**key_claim**: Creative Writing Prompting produces highest-quality outputs when the iterative critique-revision cycle is treated as the primary generation mechanism rather than as a correction step for deficient first drafts — LLMs generating creative text produce qualitatively different outputs when explicitly prompted to critique their own work against specific craft criteria (e.g., "evaluate this passage for showing versus telling, pacing, sensory specificity, and character voice authenticity") and then revise based on the critique, compared to outputs from a single high-effort generation pass; the critique step's value lies in activating a different mode of reasoning (evaluative rather than generative) that surfaces improvements the generative mode systematically misses.

**warning**: Creative Writing Prompting exhibits mode collapse tendencies where LLMs systematically gravitate toward prototypical genre structures, common narrative arc templates, and well-represented stylistic patterns from training data — default-prompted creative writing lacks genuine novelty and originality, defaulting to the most statistically central creative patterns the model has learned; achieving genuinely novel creative outputs requires explicit constraint-and-violation prompting (specifying which conventions to subvert) or strong style-transfer anchoring on specific authors or texts rather than generic genre specification, as genre specification alone produces the most statistically average genre exemplar rather than distinctive creative work.

## Technical Documentation Prompting

- secondary_domains: [large-language-models, technical-writing, software-documentation, prompt-engineering]
- aliases: [software docs generation prompting, API documentation prompts, technical writing AI]
- broader: [specialized-domain-prompting, technical-writing, prompt-engineering]
- related: [code-generation-prompting, information-density-optimization, verbosity-control-in-prompts, register-and-tone-control]
- prerequisites: [technical-writing, prompt-engineering, large-language-models]
- confidence: high

**definition**: Technical Documentation Prompting refers to the prompting strategies used to generate high-quality technical documentation from large language models — including API reference documentation, user guides, installation instructions, architecture documentation, developer tutorials, release notes, and troubleshooting guides. Technical documentation prompting must manage the technical accuracy-accessibility tradeoff (documentation that is accurate but inaccessible fails engineers new to the codebase; documentation that is accessible but imprecise fails engineers in edge-case situations), the currency of technical information (documentation must reflect current API behaviour, not training-data-time behaviour), and the audience diversity of technical documentation (beginners, intermediate users, and expert maintainers have different documentation needs from the same system).

**key_claim**: Technical Documentation Prompting achieves highest accuracy when actual code, API signatures, and function implementations are included directly in the prompt as primary context rather than relying on the model's parametric memory of libraries and APIs — LLMs trained on documentation for popular libraries have memorised documentation that may reflect outdated versions, and generating documentation from memory produces version-inconsistent outputs; providing the actual current source code or API signatures as prompt context and instructing the model to document what the code actually does rather than what documentation says it does substantially reduces version inconsistency errors in generated technical documentation.

**warning**: Technical Documentation Prompting for internal proprietary systems cannot rely on LLM parametric knowledge at all — LLMs have no training data for internal, proprietary, or non-public codebases, and prompts that ask models to "document how our authentication system works" without providing the actual code or system architecture will produce generic, plausible-sounding authentication documentation that describes common patterns but not the specific system; technical documentation prompting for non-public systems requires comprehensive code context provision and validation against actual system behaviour.

## Data Analysis Prompting

- secondary_domains: [large-language-models, data-science, statistics, prompt-engineering]
- aliases: [data analysis LLM prompting, statistical analysis prompting, analytics AI prompting]
- broader: [specialized-domain-prompting, data-science, prompt-engineering]
- related: [code-generation-prompting, financial-analysis-prompting, claim-strength-calibration, mathematical-proof-prompting]
- prerequisites: [statistics, data-analysis, prompt-engineering, large-language-models]
- confidence: high

**definition**: Data Analysis Prompting refers to the prompting strategies used to direct large language models to perform statistical analysis, data interpretation, visualisation planning, hypothesis testing, and exploratory data analysis — either directly on provided datasets (for code-execution-enabled LLMs) or by generating analysis code and interpretation frameworks that users execute on their data. Effective data analysis prompting specifies the dataset structure and variable types, the analytical questions to answer, the statistical assumptions and constraints, the output format requirements, and the target audience's statistical sophistication. It incorporates appropriate statistical method selection, assumption checking requirements, effect size reporting standards, and uncertainty quantification practices appropriate to the data type and analytical goal.

**key_claim**: Data Analysis Prompting is most effective when structured as a question-first, method-later workflow — beginning with precise specification of the analytical question ("is there a statistically significant difference in X between groups A and B, accounting for confounders Y and Z?") before specifying analytical methods, because question-first prompting allows the model to select appropriate statistical methods for the analytical question rather than applying a pre-specified method that may be statistically inappropriate; method-first prompting (e.g., "run an ANOVA on this data") frequently produces statistically inappropriate analyses when the data violates method assumptions that the model would have checked if given the analytical question instead.

**warning**: Data Analysis Prompting using LLMs without code execution produces statistical interpretations that cannot be verified against actual calculations — models generate plausible statistical interpretation language that may not correspond to any actual computation on the provided data, producing outputs that look like analysis results but are actually patterns from training data statistics reporting; all quantitative data analysis claims from LLMs must be verified against actual code execution on the actual dataset, and natural-language statistical interpretation from LLMs should be treated as a template for analysis planning rather than as computed results.

## Ethical Reasoning Prompting

- secondary_domains: [large-language-models, applied-ethics, moral-philosophy, prompt-engineering]
- aliases: [moral reasoning prompts, ethical analysis prompting, applied ethics in LLMs]
- broader: [specialized-domain-prompting, ai-ethics, prompt-engineering]
- related: [constitutional-ai-data-pipeline, social-desirability-bias-in-llms, confirmation-bias-in-chain-of-thought, claim-strength-calibration]
- prerequisites: [moral-philosophy, ethical-theory, prompt-engineering, large-language-models]
- confidence: high

**definition**: Ethical Reasoning Prompting refers to the prompting strategies designed to elicit systematic moral analysis from large language models — applying ethical frameworks (consequentialism, deontology, virtue ethics, contractualism, care ethics) to specific moral dilemmas, policy questions, business decisions, and design choices. Ethical reasoning prompting provides the moral context, stakeholder perspectives, relevant constraints, and applicable ethical frameworks, and guides the model through structured ethical analysis rather than soliciting direct moral verdicts. Effective ethical reasoning prompting is multi-framework (applying multiple ethical theories and comparing conclusions), stakeholder-inclusive (explicitly considering all affected parties), and uncertainty-explicit (acknowledging genuine moral disagreement rather than presenting contested conclusions as settled).

**key_claim**: Ethical Reasoning Prompting that requires explicit application of multiple competing ethical frameworks produces more epistemically defensible outputs than single-framework analysis — forcing the model to apply consequentialist, deontological, and virtue-ethical frameworks to the same dilemma and then synthesise across frameworks reveals where ethical frameworks agree (providing stronger grounds for conclusions) and where they diverge (identifying genuine moral uncertainty), producing analysis that appropriately represents moral complexity rather than presenting the single-framework conclusion that reflects the model's RLHF-aligned default framework as if it were a settled ethical verdict.

**warning**: Ethical Reasoning Prompting is subject to the same RLHF-induced biases as all LLM output — models trained on human feedback exhibit systematic tendencies toward the moral positions that human raters found most agreeable, which tends to reflect the social desirability norms and cultural values of the RLHF rater pool rather than carefully reasoned ethical analysis; users should treat LLM ethical reasoning outputs as structured frameworks for human moral deliberation rather than as authoritative ethical verdicts, and should be especially sceptical of LLM ethical conclusions on morally contested questions where the model's output may reflect training-time consensus rather than valid ethical reasoning.

## Historical Reasoning Prompting

- secondary_domains: [large-language-models, historiography, historical-analysis, prompt-engineering]
- aliases: [historical analysis prompting, historical LLM prompting, historiographical reasoning in AI]
- broader: [specialized-domain-prompting, historical-ai, prompt-engineering]
- related: [claim-strength-calibration, hindsight-bias-in-llm-evaluation, nuance-preservation-in-summarization, availability-heuristic-in-llms]
- prerequisites: [historiography, historical-method, prompt-engineering, large-language-models]
- confidence: high

**definition**: Historical Reasoning Prompting refers to the prompting strategies adapted for historical analysis tasks — including historical causation analysis, counterfactual historical reasoning, comparative historical analysis, primary source interpretation, historiographical debate synthesis, and historical context reconstruction. Historical reasoning prompting must address the epistemic challenges specific to historical knowledge: the incompleteness and bias of the historical record, the diversity of historiographical interpretations, the difficulty of causal inference in non-experimental historical settings, the presence of present-day anachronism in historical judgment, and the tendency of training data to over-represent well-documented periods and under-represent poorly documented ones. Effective historical reasoning prompts specify the historical period and geography, the relevant historiographical debates, the evidential basis required, and the distinction between established historical consensus and contested interpretations.

**key_claim**: Historical Reasoning Prompting is most epistemically valuable when explicitly structured around the distinction between primary evidence, secondary interpretation, and historiographical consensus — prompting the model to separately identify what primary sources establish, how secondary historians have interpreted those sources, and what the current historiographical consensus is (and where it is disputed) produces more accurate and more epistemically calibrated historical analysis than prompting for a single integrated historical narrative, which the model will construct by blending evidence, interpretation, and consensus in ways that conceal the evidential basis for each claim.

**warning**: Historical Reasoning Prompting exhibits strong availability bias effects — LLMs have substantially more training data about well-documented historical periods (modern European and North American history, classical Mediterranean antiquity) than about equally important but less textually-documented periods (sub-Saharan African pre-colonial history, Central Asian medieval history, indigenous American pre-contact history), producing systematic gaps in historical knowledge that the model cannot reliably identify; users requesting historical analysis of under-documented periods or cultures should independently verify LLM outputs against specialised historical scholarship rather than treating confident outputs as reflecting equivalent evidentiary bases.

## Philosophical Argument Prompting

- secondary_domains: [large-language-models, philosophy, formal-argumentation, prompt-engineering]
- aliases: [philosophical reasoning prompts, argument analysis prompting, philosophical LLM reasoning]
- broader: [specialized-domain-prompting, philosophical-ai, prompt-engineering]
- related: [ethical-reasoning-prompting, logical-entailment-verification, claim-strength-calibration, chain-of-thought-prompting]
- prerequisites: [formal-logic, philosophical-methodology, prompt-engineering, large-language-models]
- confidence: high

**definition**: Philosophical Argument Prompting refers to the prompting strategies used to elicit rigorous philosophical analysis from large language models — including argument reconstruction, validity assessment, objection generation, counterargument development, thought experiment analysis, conceptual clarification, and philosophical literature synthesis. Philosophical argument prompting must manage the distinction between valid and sound arguments, the distinction between empirical and conceptual claims, the role of intuition in philosophical methodology, and the diversity of philosophical traditions (analytic, continental, pragmatist, Eastern) that the model may draw on. Effective philosophical argument prompting specifies the philosophical tradition and methodology, the target argument or position, the level of technical philosophical sophistication, and the specific analytical task.

**key_claim**: Philosophical Argument Prompting produces its highest-value outputs when used for steelmanning — explicitly prompting the model to construct the strongest possible version of a philosophical argument the user disagrees with — because this application directly leverages LLMs' ability to reconstruct philosophical positions from training data that encompasses the full diversity of philosophical perspectives, providing a systematically stronger adversarial test of a position than the user's own objection formulation; steelmanning prompting produces substantially more intellectually productive engagement with philosophical disagreement than prompting for the model's own position on contested philosophical questions.

**warning**: Philosophical Argument Prompting surfaces a fundamental limitation of LLMs in philosophical discourse — LLMs lack genuine philosophical intuitions, which are a primary evidential source in many philosophical methodologies; when prompted to engage with thought experiments, the model generates responses that reproduce the consensus reactions from training data rather than exercising independent philosophical judgment, making LLM philosophical engagement particularly unreliable for novel thought experiments not covered in training data and for philosophical questions where intuition revision is the primary philosophical contribution.

## Cybersecurity Analysis Prompting

- secondary_domains: [large-language-models, cybersecurity, vulnerability-analysis, prompt-engineering]
- aliases: [security analysis prompting, penetration test planning prompts, threat modelling LLM prompts]
- broader: [specialized-domain-prompting, security-ai, prompt-engineering]
- related: [code-review-prompting, ethical-reasoning-prompting, data-analysis-prompting, logical-entailment-verification]
- prerequisites: [cybersecurity, threat-modelling, prompt-engineering, large-language-models]
- confidence: high

**definition**: Cybersecurity Analysis Prompting refers to the prompting strategies used to direct large language models to perform security-focused analysis — including threat modelling, attack surface analysis, vulnerability identification, security architecture review, incident analysis, security policy evaluation, and defensive control recommendation — within appropriate ethical and legal bounds. Cybersecurity analysis prompting leverages LLMs' broad knowledge of attack patterns, defensive frameworks (MITRE ATT&CK, STRIDE, OWASP), and security best practices, while explicitly constraining outputs to defensive contexts that do not provide operational attack capability. Effective cybersecurity prompting specifies the analysis scope (specific system, infrastructure, code), the threat model (relevant adversary types and capabilities), the defensive objective, and the output format required.

**key_claim**: Cybersecurity Analysis Prompting using structured threat modelling frameworks (STRIDE, PASTA, LINDDUN) as prompt scaffolding produces substantially more comprehensive threat coverage than unstructured security analysis prompts — providing the model with a systematic threat category enumeration forces it to reason across the full threat model rather than focusing on the most salient attack vectors the model has encountered most frequently in training data, reducing the availability bias effect that causes unstructured security prompting to over-represent common attack vectors and under-represent novel or domain-specific threats; structured framework prompting also produces outputs in formats compatible with standard security documentation workflows.

**warning**: Cybersecurity Analysis Prompting must maintain strict offensive/defensive framing boundaries — LLMs trained on security literature contain knowledge of attack techniques that can be elicited by prompts that progressively erode defensive framing constraints; cybersecurity prompting deployments must implement robust output filtering and access controls that prevent prompt injection and jailbreak attempts from eliciting operational attack guidance; additionally, LLM-generated vulnerability reports require expert security review before remediation action because LLMs produce both false positives (flagging non-exploitable patterns as vulnerabilities) and false negatives (missing exploitable vulnerabilities requiring contextual reasoning beyond pattern matching).
