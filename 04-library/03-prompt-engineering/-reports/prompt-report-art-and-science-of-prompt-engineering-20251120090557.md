---
title: "prompt-report-comprehensive-guide-to-the-art-and-science-of-prompt-engineering-20251120090557"
id: "20251120090557"
type: "prompt/report"
status: not-read
source: "[Gemini-Deep-Research]"
year: "[[2025]]"
tags:
  - prompt-engineering
  - project/pur3v4d3r
  - year/2025
  - self-improvement
  - pkb/maintenance/refactoring
  - pkb/maintenance/cleanup
aliases:
  - "A COMPREHENSIVE GUIDE TO THE ART AND SCIENCE OF PROMPT ENGINEERING,LLM Instruction Design,Mastering AI Communication,Prompt Engineering Guide"
link-up:
  - "[[project-pur3v4d3r-moc]]"
link-related:
  - "[[2025-11-20|Daily-Note]]"
---

# A COMPREHENSIVE GUIDE TO THE ART AND SCIENCE OF PROMPT ENGINEERING

## INTRODUCTION: COMMUNICATING WITH ARTIFICIAL INTELLIGENCE

### DEFINING PROMPT ENGINEERING

Prompt engineering is the art and science of designing, structuring, and optimizing inputs—known as prompts—to guide generative artificial intelligence (AI) models toward producing desired, high-quality outputs.1 It is a systematic process that extends beyond simply asking questions; it involves the careful selection of words, phrases, formats, and symbols to communicate intent with precision.4 While modern generative AI, particularly Large Language Models (LLMs), is designed to mimic human conversation, it lacks genuine understanding and requires explicit, detailed instructions to unlock its full potential and generate relevant, accurate results.1

### THE CRITICAL ROLE OF PROMPTING

Effective prompting is the crucial link between a user's intent and an AI model's performance. It serves as a roadmap for the AI, steering it toward a specific outcome and unlocking its latent capabilities.2 The practice of prompt engineering offers several significant benefits. It provides developers with greater control over AI interactions, ensuring that the model's output is concise, properly formatted, and aligned with the application's purpose.4 For end-users, it improves the experience by reducing the trial-and-error often associated with obtaining useful responses.4 Furthermore, thoughtful prompting can help mitigate inherent biases present in the model's training data and enhance the flexibility of AI tools, allowing them to be applied to a wider range of tasks.4 The growing importance of this discipline has led to the emergence of specialized roles, such as the prompt engineer, dedicated to mastering this human-AI interface.4

### REPORT STRUCTURE AND LEARNING PATHWAY

This report provides a comprehensive exploration of prompt engineering, designed to guide readers from foundational concepts to advanced, domain-specific applications. The structure is as follows:

* **Section I** deconstructs the essential components and core principles that form the anatomy of any effective prompt.
* **Section II** introduces foundational prompting techniques, including zero-shot, one-shot, and few-shot prompting, which form the basis of in-context learning.
* **Section III** delves into advanced frameworks that enable complex reasoning, problem decomposition, and the integration of external knowledge.
* **Section IV** offers guidance on tailoring prompts for specific domains, such as text manipulation, code generation, and text-to-image synthesis.
* Section V outlines the practical, iterative lifecycle of prompt development, including common pitfalls to avoid.
    This structured pathway provides a clear and systematic roadmap for mastering the craft of prompt engineering.

## SECTION I: THE ANATOMY OF AN EFFECTIVE PROMPT

A well-engineered prompt is not a monolithic block of text but a carefully assembled structure of distinct components. Understanding these building blocks is the first step toward crafting inputs that consistently yield desired outputs. The structure of a prompt is not merely for the AI's benefit; it also serves as a cognitive tool for the user. The process of breaking down a request into these components forces the user to move from a vague goal to a precise, actionable set of instructions. For example, a user may start with the general idea of needing a marketing email. A novice might simply ask the AI to "write a marketing email," resulting in a generic and unhelpful draft. However, a structured approach compels the user to define the key elements: Who should the AI be? (the **Role**), What is the exact task? (the **Instruction**), What information is necessary? (the **Context**), and What should the final output look like? (the **Output Format**). This pre-prompting clarification of intent is a meta-skill that prompt engineering cultivates, making it a discipline that refines human thought as much as it directs machine computation.

### CORE COMPONENTS OF A PROMPT

An effective prompt can be deconstructed into several key elements that work in concert to guide the AI model.7

* **Role/Persona**: This component assigns a specific identity or expertise to the AI, such as "Act as a senior software engineer" or "You are a world-renowned historian".9 Assigning a role frames the AI's response, influencing its tone, style, vocabulary, and the knowledge it draws upon.11
* **Instruction/Task**: This is the primary directive—a clear and direct command that specifies what the AI should accomplish.13 It often begins with an action verb like "Summarize," "Translate," "Generate," or "Classify".14
* **Context**: This provides the necessary background information, external data, or situational details that the AI needs to generate a relevant and accurate response.6 Without sufficient context, the model is forced to make assumptions, which often leads to generic or incorrect outputs.16
* **Input Data**: This is the specific content that the instruction will be applied to.13 It could be a block of text for summarization, a question to be answered, or a topic for creative writing.
* **Output Format/Indicator**: This element provides explicit instructions on the desired structure of the output.8 Specifying a format, such as JSON, a bulleted list, a markdown table, or a specific number of paragraphs, ensures the response is consistent and easy to parse, both for humans and for downstream programmatic use.5

### FUNDAMENTAL PRINCIPLES OF PROMPT DESIGN

Beyond the structural components, several universal principles govern the effectiveness of a prompt. Adhering to these principles can dramatically improve the quality and reliability of AI-generated responses.

* **Clarity and Specificity**: This is the most critical principle in prompt engineering.6 Vague prompts lead to ambiguous and often useless outputs.11 The prompt should be as descriptive and detailed as possible regarding the desired outcome, context, length, and style. For instance, a less effective prompt like "Write a poem about OpenAI" can be significantly improved by adding specificity: "Write a short inspiring poem about OpenAI, focusing on the recent DALL-E product launch (DALL-E is a text-to-image ML model) in the style of a {famous poet}".18
* **Providing Rich and Relevant Context**: Context grounds the model's response in reality and reduces ambiguity.15 A well-crafted prompt should contain all the information necessary for the AI to complete the task without making assumptions.17 This might include background details, key terms, or relevant data points.9
* **The Power of Affirmative Directives**: Research and best practices indicate that it is more effective to instruct the model on what to _do_ rather than what _not to do_.18 Negative instructions can be confusing for the model. For example, instead of a negative command like "DO NOT ASK FOR USERNAME OR PASSWORD," a more effective, affirmative prompt would be: "The agent will attempt to diagnose the problem and suggest a solution, whilst refraining from asking any questions related to PII. Instead of asking for PII... refer the user to the help article
    [www.samplewebsite.com/help/faq](https://www.samplewebsite.com/help/faq)".18
* **Structuring for Success**: The physical layout of the prompt can impact how the model interprets it. Placing the primary instruction at the beginning of the prompt is a recommended best practice.18 Additionally, using clear separators or delimiters, such as triple quotes (
    """), XML tags, or hash marks (###), to distinguish between instructions, context, and input data can significantly improve the model's comprehension and the quality of its output.14

## SECTION II: FOUNDATIONAL PROMPTING TECHNIQUES

At the core of prompt engineering are several foundational techniques that leverage a model's ability to learn from information provided directly within the prompt. These methods, known as in-context learning, range from giving the model no examples to providing several, each suited for different types of tasks.

### ZERO-SHOT PROMPTING

Zero-shot prompting is the most direct form of interaction, where the model is given an instruction to perform a task without any prior examples.25 This technique relies entirely on the vast knowledge and patterns the model acquired during its pre-training phase.27

* **Example (Sentiment Analysis):**
    Classify the following product review as "Positive", "Negative", or "Neutral".

    Review: "The setup was straightforward, but the battery life is disappointing."

    Sentiment:

    In this case, the model uses its pre-existing understanding of language to infer that the review has mixed elements and should likely be classified as "Neutral" or "Negative".29

* **Use Cases:** Zero-shot prompting is best suited for simple, well-defined tasks that the model has likely encountered in its training data, such as basic text summarization, straightforward translation, or sentiment analysis of common phrases.30

### ONE-SHOT AND FEW-SHOT PROMPTING (IN-CONTEXT LEARNING)

This technique enhances a model's performance by providing it with one (one-shot) or a few (few-shot) examples of the desired input-output pattern directly within the prompt.30 This process, also known as in-context learning, does not update the model's parameters but guides its response for the current query by demonstrating the expected format, style, and logic.34

* **Example (One-Shot Translation):**
    Translate the English word to its French equivalent.
    Example: English: "cat" -> French: "chat"

    English: "cheese" -> French:

    The single example clarifies the task and the desired output format, making the response more reliable.30

* **Example (Few-Shot Classification):**
    Classify the customer support ticket into one of the categories: "Technical Issue," "Billing Inquiry," or "General Inquiry."

    Ticket: "I can't log in to my account. The system keeps giving me an error message."

    Category: Technical Issue

    Ticket: "What are the hours of operation for your customer support team?"

    Category: General Inquiry

    Ticket: "Can you explain why my latest bill is higher than usual?"

    Category:

    By providing multiple examples, the model can better discern the nuances between categories, leading to a more accurate classification of "Billing Inquiry".37

* **Best Practices:** The quality and diversity of examples are crucial. They should be consistently formatted and accurately represent the task.34 The optimal number of examples varies with task complexity; too many can lead the model to overfit to the specific examples provided, while too few may not provide sufficient guidance.34

### THE PERSONA PATTERN (ROLE PROMPTING)

The persona pattern, or role prompting, involves assigning a specific role or character to the AI to shape its response.9 This technique influences the model's tone, style, level of expertise, and perspective by instructing it to "act as" a particular entity.41

* **Example:**
    You are an expert financial analyst with 20 years of experience in the tech sector. Summarize the key takeaways from the following quarterly earnings report for a non-technical executive audience. Focus on revenue growth, profit margins, and future outlook.

    This prompt encourages the model to adopt a professional tone and prioritize information relevant to a financial expert communicating with a business leader.20

* **Benefits:** Role prompting can significantly improve the relevance and quality of responses by activating the specific domains of knowledge the model associates with that persona.40
* **Limitations:** The effectiveness of a persona depends heavily on how well that role is represented in the model's training data. Furthermore, this technique can inadvertently reinforce stereotypes if not crafted with care.40

| Technique | Definition | No. of Examples | Best Use Cases | Pros | Cons |
| --- | --- | --- | --- | --- | --- |
| Zero-Shot Prompting | The model performs a task based on instructions alone, without any examples. | 0 | Simple, common tasks (e.g., basic summarization, general Q&A). | Fast, simple, requires minimal prompt design. | Can be unreliable for complex or nuanced tasks; highly dependent on model's pre-training. |
| One-Shot Prompting | The model is provided with a single example to guide its response. | 1 | Tasks requiring a specific format or when ambiguity needs to be reduced (e.g., specific translation style). | Better than zero-shot for clarity; helps specify output format. | A single example may not be sufficient to capture the full complexity or variability of a task. |
| Few-Shot Prompting | The model is given multiple examples to demonstrate the desired input-output pattern. | 2+ | Complex tasks requiring pattern recognition, specific formatting, or nuanced classification. | High accuracy and consistency; effective for custom formats and specialized tasks. | Requires more effort to create good examples; can consume more context window space; risk of overfitting to examples. |

Table 1: A comparative overview of foundational "shot-based" prompting techniques.25

## SECTION III: ADVANCED REASONING AND DECOMPOSITION FRAMEWORKS

For tasks that require multi-step logic, planning, or access to external information, foundational techniques are often insufficient. Advanced frameworks have been developed to enhance the reasoning and problem-solving capabilities of LLMs. The development of these frameworks illustrates a clear progression in AI problem-solving. Standard prompting treated the model as a black box, hoping for a correct answer in one step. Chain-of-Thought (CoT) was a significant leap forward, forcing the model to externalize its reasoning into a linear, step-by-step process, much like a student showing their work on a math problem.48 However, this single path could still be flawed. This limitation led directly to the development of Self-Consistency, which introduces diversity by asking, "What if we think about this problem in a few different ways and see which answer is most common?".49 This is akin to getting a second and third opinion before making a decision. The next logical step was to move beyond simply generating multiple independent paths to actively managing the exploration process. Tree of Thoughts (ToT) achieves this by allowing the model to not only explore different paths but also to evaluate them as it goes, pruning unpromising ideas and expanding on promising ones—effectively managing a structured brainstorming session.50 While these techniques address the model's internal reasoning process, Retrieval-Augmented Generation (RAG) tackles a different fundamental limitation: the static nature of the model's internal knowledge.51

### CHAIN-OF-THOUGHT (COT) PROMPTING

Chain-of-Thought (CoT) prompting is a technique that encourages an LLM to break down a complex problem into a sequence of intermediate, logical steps before arriving at a final answer.4 This method significantly improves performance on tasks that demand arithmetic, commonsense, or symbolic reasoning, as it mimics a more deliberate human thought process.3

* **Zero-Shot CoT:** This is the simplest form, achieved by appending a simple instruction like "Let's think step by step" to the end of a question.24 This triggers the model's inherent reasoning capabilities without needing explicit examples.
* **Few-Shot CoT:** This more robust method involves providing one or more examples in the prompt that explicitly demonstrate the step-by-step reasoning process.48
* **Example (Few-Shot CoT for an arithmetic problem):**
    Q: A juggler can juggle 16 balls. Half of the balls are golf balls, and half of the golf balls are blue. How many blue golf balls are there?
    A: The juggler has 16 balls in total. Half of the balls are golf balls, so there are 16 / 2 = 8 golf balls. Half of the golf balls are blue, so there are 8 / 2 = 4 blue golf balls. The answer is 4.

    Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

    A:

    The model would then generate the reasoning: Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74 - 35 = 39. The answer is 39..56

### SELF-CONSISTENCY

Self-consistency is an advanced technique that enhances CoT prompting by replacing naive greedy decoding (i.e., picking the single most likely next word at each step) with a more robust sampling method.57 The core idea is to generate multiple, diverse reasoning paths for the same problem and then select the most consistent answer through a majority vote.49 This approach is based on the intuition that a complex problem may have several valid solution paths, but they should all converge on the same correct answer.49

* **Example:** For the question, "When I was 6 my sister was half my age. Now I'm 70 how old is my sister?", the model might generate three different reasoning paths:
    1. When I was 6 my sister was 3. The age difference is 3 years. Now I'm 70, so she is 70 - 3 = 67. The answer is 67.
    2. The age difference between me and my sister is 3 years. So when I am 70, my sister is 70 - 3 = 67. The answer is 67.
    3. When I was 6, my sister was 3. Now I am 70, so she is 70 / 2 = 35. The answer is 35.
        By taking a majority vote, the final answer selected would be 67, correcting the error in the third path.57

### TREE OF THOUGHTS (TOT)

The Tree of Thoughts (ToT) framework generalizes CoT by enabling the model to explore multiple reasoning paths concurrently in a tree-like structure.17 Unlike the linear progression of CoT, ToT allows the model to perform deliberate problem-solving by generating multiple intermediate "thoughts" at each step, evaluating their viability, and deciding whether to expand upon them, backtrack, or explore alternatives.50

* **Process:** ToT typically involves a thought generator (proposer) and an evaluator. At each node of the tree, the model proposes several potential next steps. An evaluation mechanism (e.g., a "value prompt" or heuristic) then scores these thoughts, and a search algorithm (like breadth-first search or depth-first search) determines which paths to explore further.50 This allows the model to look ahead and self-correct, making it highly effective for complex planning and search problems.62

### RETRIEVAL-AUGMENTED GENERATION (RAG)

Retrieval-Augmented Generation (RAG) is a framework that addresses the inherent limitation of LLMs: their knowledge is static and confined to their training data.3 RAG enhances an LLM by connecting it to an external, authoritative knowledge base, allowing it to retrieve relevant, up-to-date, or proprietary information before generating a response.51

* **Process:** The RAG workflow involves several stages:
    1. **Indexing:** External documents (e.g., company policies, technical manuals) are converted into numerical representations (embeddings) and stored in a vector database.51
    2. **Retrieval:** When a user submits a query, the system converts the query into an embedding and searches the vector database to find the most relevant chunks of information.51
    3. **Augmentation & Generation:** The retrieved information is then added to the original prompt as context, and this augmented prompt is fed to the LLM to generate a grounded, fact-based response.51
* **Benefits:** RAG is highly effective at reducing "hallucinations" (fabricated information), providing users with source citations, and enabling the LLM to answer questions about topics beyond its training data.3

| Framework | Core Idea | Best For (Problem Type) | Key Benefit | Primary Limitation |
| --- | --- | --- | --- | --- |
| Chain-of-Thought (CoT) | Generate a single, linear sequence of intermediate reasoning steps. | Multi-step reasoning tasks (math, logic, commonsense). | Improves accuracy on complex problems by breaking them down. | A single reasoning error can derail the entire process; can be unreliable. |
| Self-Consistency | Generate multiple reasoning paths and select the most frequent answer. | Tasks with a discrete, verifiable answer (e.g., arithmetic, multiple-choice). | Increases robustness and accuracy over standard CoT by mitigating random errors. | Computationally more expensive; less effective for open-ended generation tasks. |
| Tree of Thoughts (ToT) | Explore and evaluate multiple reasoning paths in a tree structure, with backtracking. | Complex planning, search, and strategic problems where exploration is key. | Enables deliberate problem-solving and self-correction, tackling problems beyond CoT's reach. | Very resource-intensive; requires complex prompt structures and search algorithms. |
| Retrieval-Augmented Generation (RAG) | Retrieve relevant information from an external knowledge base to augment the prompt. | Knowledge-intensive tasks requiring up-to-date, proprietary, or verifiable information. | Reduces hallucinations, provides current information, and allows for source citation. | Depends on the quality of the external knowledge base and retrieval system. |

Table 2: A comparative overview of advanced reasoning and decomposition frameworks.50

## SECTION IV: DOMAIN-SPECIFIC PROMPT ENGINEERING

While the fundamental principles of prompting are universal, their application often needs to be tailored to the specific domain and AI model being used. Different tasks, such as generating creative text, writing code, or creating images, require distinct prompting strategies.

### PROMPTING FOR TEXT GENERATION AND MANIPULATION

This domain covers a wide range of common Natural Language Processing (NLP) tasks, each benefiting from specific prompting approaches.

* **Summarization:** Effective summarization prompts must clearly define the desired output's constraints. This includes specifying the length (e.g., "in one paragraph," "in exactly 50 words"), the target audience (e.g., "for an executive," "for a high school student"), and the desired format (e.g., "as a bulleted list," "in a single paragraph").68 Assigning a role, such as "Act as a project manager," combined with instruction-heavy prompts that detail what to include or exclude, is a highly effective strategy.68
* **Translation:** While modern LLMs have strong baseline translation capabilities, few-shot prompting is particularly useful for controlling the style, tone, and format of the translation.28 Providing a few examples can guide the model to produce a formal business translation versus a casual, conversational one.36
* **Creative Writing:** To elicit creative and engaging narratives, prompts should focus on establishing a rich context. Key elements to include are the setting (e.g., "a dystopian city in the year 2242"), character details (e.g., "a cynical detective haunted by their past"), mood (e.g., "a sense of impending doom"), and desired style (e.g., "in the style of a classic film noir").2 Role-playing ("Act as a seasoned fantasy author") and providing a short story excerpt as an example can further refine the output.

### PROMPTING FOR CODE GENERATION

Code generation models like GitHub Copilot are powerful tools, but their effectiveness is highly dependent on the context provided by the developer.

* **Provide Clear Context:** These models are context-aware, using the contents of currently open files and the overall project structure to inform their suggestions.23 To get relevant code, it is best practice to have related files open while closing irrelevant ones, ensuring the model has a clear picture of the existing codebase.72
* **Use Descriptive Comments and Names:** Well-written code serves as a prompt. Using meaningful and descriptive function and variable names (e.g., calculate\_user\_age instead of calc) provides strong signals to the model about the code's intent.23 Furthermore, writing a clear, top-level comment that explains the overall goal of a file or function before writing any code can guide the model to generate a more accurate and complete implementation.23
* **Break Down Complex Tasks:** Instead of asking the model to generate an entire application in one go, a more effective approach is to decompose the problem into smaller, self-contained functions.72 Prompting for one function at a time—for example, first a function to initialize a database, then a function to add a user—yields more reliable and modular code.74
* **Provide Examples (Few-Shot Learning):** Just as with text generation, providing examples is a powerful technique for code generation. This can be done by writing a function signature and a docstring, or even by writing a set of unit tests first and then asking the model to generate the code that passes those tests.72

### PROMPTING FOR IMAGE GENERATION (DALL-E, MIDJOURNEY)

Crafting effective text-to-image prompts is a distinct skill that blends descriptive language with technical specifications. The goal is to paint a vivid picture for the AI to interpret.

* **Core Components:** A successful image prompt typically specifies several key elements:
    * **Subject:** The main focus of the image (e.g., "an astronaut riding a horse").3
    * **Medium:** The artistic form (e.g., "photograph," "oil painting," "3D render," "pencil sketch").75
    * **Style:** The artistic movement or aesthetic (e.g., "impressionist," "cyberpunk," "hyper-realistic," "cubism").2
    * **Composition:** The framing and perspective (e.g., "close-up," "wide shot," "aerial view," "portrait").77
    * **Lighting:** The mood and time of day (e.g., "cinematic lighting," "soft natural light," "golden hour," "neon").75
    * **Color:** The desired color palette (e.g., "vibrant," "monochromatic," "muted orange warm tones").75
* **Model-Specific Syntax:** Different models have unique ways of interpreting prompts. DALL-E 3, for instance, responds well to long, descriptive sentences that read like natural language.79 Midjourney, on the other hand, utilizes specific parameters at the end of the prompt, such as
    \--ar 16:9 to set the aspect ratio or --no trees to exclude an element (a form of negative prompting).75
* Example (Detailed Image Prompt):
    A hyper-realistic, cinematic photograph of a rugged cowboy riding a robotic horse on a dusty alien planet, double suns setting behind him. The lighting is dramatic golden hour, shot on a 35mm lens with a shallow depth of field. The style is a space western..76

## SECTION V: THE ITERATIVE PROMPT DEVELOPMENT LIFECYCLE

Effective prompt engineering is rarely a single-shot success. It is an iterative process of design, testing, analysis, and refinement, much like the development cycle in software engineering or machine learning.6 Achieving a prompt that consistently produces high-quality outputs requires a systematic approach and an understanding of common pitfalls.

### THE WORKFLOW OF A PROMPT ENGINEER

The development of a robust prompt follows a cyclical workflow designed to incrementally improve performance.

1. **Step 1: Initial Prompt Creation:** The process begins with crafting an initial prompt based on established best practices. This first draft should be clear, specific, and include as much relevant context as possible.14 The goal is to create a solid baseline for testing.
2. **Step 2: Testing and Response Analysis:** The prompt is then executed, and the AI's output is critically evaluated.86 This analysis should focus on several key dimensions: accuracy (is the information correct?), relevance (does it address the prompt's intent?), tone (does it match the desired style?), and format (is it structured correctly?).87
3. **Step 3: Prompt Refinement:** Based on the analysis of the response, the prompt is modified. This is the core of the iterative loop. If the output was too vague, the prompt might be refined by adding more specific details or constraints. If the format was incorrect, providing few-shot examples can help. If the tone was off, adjusting the persona is a common solution.83
4. **Step 4: Repeat:** The refined prompt is tested again, and the cycle of analysis and modification continues until the prompt consistently produces the desired results across a variety of inputs and edge cases.84

### COMMON PITFALLS AND ANTI-PATTERNS

In the process of prompt development, beginners and even experienced users can fall into common traps that lead to suboptimal results. Understanding these anti-patterns is crucial for effective debugging and refinement.

* **Vagueness:** Being too open-ended or imprecise is the most common mistake.92 A prompt like "Write about marketing" forces the AI to guess the user's intent, leading to generic content. A better prompt specifies the topic, audience, length, and format.94
* **Overloading the Prompt:** Asking the model to perform multiple, distinct tasks within a single prompt can confuse it and lead to incomplete or disjointed outputs.92 It is more effective to break down complex workflows into a series of focused, single-task prompts.93
* **Ignoring Context:** Assuming the model has access to specific, private, or real-time information is a frequent error.93 The prompt must provide all necessary context for the task, as the model only knows what is in its training data and the current prompt.94
* **Using Negative Language:** Instructing the model on what _not_ to do (e.g., "Don't use jargon") is generally less effective than providing a positive, affirmative directive (e.g., "Explain this in simple terms that a beginner can understand").18
* **Ignoring Model Limitations:** Expecting perfect factual accuracy without grounding the model with external data (using RAG) or asking for real-time information (like today's stock prices) fails to respect the inherent limitations of LLMs.92 This can lead to confident-sounding but incorrect "hallucinations".93

| Pitfall / Anti-Pattern | Description | Example of Bad Prompt | Solution / Best Practice | Example of Good Prompt |
| --- | --- | --- | --- | --- |
| Vague Instructions | The prompt lacks sufficient detail, forcing the AI to make assumptions. | Write an email. | Be specific about the task, audience, tone, and desired length. | Write a formal email to our new client, ABC Corp, welcoming them. Keep it under 150 words and maintain a professional yet friendly tone. |
| Overloaded Prompt | A single prompt contains multiple, unrelated tasks. | Summarize the attached report, translate the summary into German, and then create a 5-slide presentation outline from it. | Break the workflow into a sequence of single-task prompts. | Prompt 1: Summarize the attached report in 3 key bullet points. Prompt 2: Translate the following text into German: [insert summary] |
| Missing Context | The prompt assumes the AI has knowledge it doesn't possess. | Is our new marketing campaign compliant with internal policy #2.3.1? | Provide all necessary external information directly in the prompt (or use RAG). | Given our internal marketing policy #2.3.1 below, is the following campaign description compliant? Policy: [text of policy] Campaign: [text of campaign] |
| Negative Directives | The prompt focuses on what to avoid rather than what to do. | Don't write a boring product description. Don't make it too long. | Use affirmative instructions that clearly state the desired action and style. | Write an exciting and concise product description (around 50 words) that highlights the top 3 features. |
| Factual Hallucination | The prompt asks for information that the model is likely to invent due to knowledge gaps. | What were the key findings of the research paper published yesterday by Dr. Smith? | Ground the model with retrieved data using RAG or provide the content directly. | Based on the following abstract from Dr. Smith's paper, what are the key findings? Abstract: [paste abstract here] |

Table 3: A troubleshooting guide for common prompting pitfalls and their solutions.92

## CONCLUSION: THE FUTURE OF HUMAN-AI COMMUNICATION

### RECAP OF KEY PRINCIPLES

Prompt engineering is a discipline founded on a set of core principles that transform communication with AI from a guessing game into a systematic process. The most critical of these is the pursuit of **clarity and specificity**, ensuring that instructions are unambiguous and detailed. This is supported by providing **rich context**, which grounds the model and reduces its reliance on assumptions. Structuring prompts with clear **roles, tasks, and output formats** further refines the AI's output, while employing **affirmative directives** proves more effective than negative constraints. The journey from foundational techniques like **few-shot learning** to advanced frameworks such as **Chain-of-Thought** and **Retrieval-Augmented Generation** demonstrates a clear trajectory toward enabling more complex reasoning and knowledge-intensive tasks. Ultimately, success in prompt engineering is achieved through a continuous **iterative lifecycle** of crafting, testing, analyzing, and refining.

### THE EVOLVING LANDSCAPE

The field of prompt engineering is rapidly evolving. While manual crafting of prompts remains a vital skill, the frontier is shifting towards more automated and agentic systems. Emerging research explores techniques where AI models generate and refine their own prompts to solve problems, a concept known as Automatic Prompt Engineering.3 Frameworks like Plan-and-Solve Prompting allow models to devise a multi-step plan before execution 97, while others like ReAct (Reason + Act) enable models to interact with external tools to gather information and perform actions.98

This evolution suggests a future where the focus of human-AI interaction may move from crafting individual, perfect prompts to designing high-level goals, systems, and ethical guardrails for autonomous AI agents. The role of the prompt engineer is therefore not diminishing but transforming—from a precise instructor to a strategic architect of complex, AI-driven workflows. As AI models become more capable, the principles of clear communication, contextual grounding, and logical decomposition pioneered by prompt engineering will remain the bedrock of effective human-AI collaboration.

## APPENDICES

### APPENDIX A: PROMPT PATTERN CATALOG

This is a quick-reference guide to common and reusable prompt structures, or "patterns," that can be adapted for various tasks.98

* **Persona Pattern:** Assigns a role to the AI to guide its tone and expertise.
    * _Template:_ Act as a..
    * _Example:_ Act as an expert copywriter. Write three headlines for a new brand of coffee.
* **Template Pattern:** Provides a strict format for the AI to fill in.
    * _Template:_ Use the following template:. Fill in the placeholders based on this information:.
    * _Example:_ Template: "Dear \[Name\], Your order #\[Number\] has shipped. Expected delivery:." Information: Name=John Doe, Number=123, Date=Oct 28.
* **Question Refinement Pattern:** Asks the AI to improve the user's question before answering.
    * _Template:_ From now on, whenever I ask a question, suggest a better version of the question to use instead.
* **Flipped Interaction Pattern:** The user takes on a role, and the AI asks questions to elicit information.
    * _Template:_ I am a student struggling with calculus. You are a tutor. Ask me questions to figure out where I'm stuck.
* **Cognitive Verifier Pattern:** Instructs the AI to break down a problem and verify its steps.
    * _Template:_ \[Problem\]. First, identify the key components of the problem. Second, outline the steps to solve it. Third, solve it step-by-step. Finally, provide the answer.

### APPENDIX B: CURATED LIST OF INFLUENTIAL RESEARCH PAPERS

For those interested in a deeper exploration of the concepts discussed in this report, the following seminal research papers are highly recommended.

1. **"Language Models are Few-Shot Learners"** (Brown, T. et al., 2020). This paper from OpenAI introduced the GPT-3 model and demonstrated the power of in-context learning (few-shot prompting) in large language models.
2. **"Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing"** (Liu, P. et al., 2021). An early and comprehensive survey that systematized the emerging field of prompting.101
3. **"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"** (Wei, J. et al., 2022). The groundbreaking paper that introduced Chain-of-Thought (CoT) prompting, showing that it significantly improves reasoning in LLMs.48 (arXiv:2201.11903)
4. **"Self-Consistency Improves Chain of Thought Reasoning in Language Models"** (Wang, X. et al., 2022). This paper introduced the Self-Consistency method as a powerful enhancement to CoT, improving robustness by sampling multiple reasoning paths.49 (arXiv:2203.11171)
5. **"Tree of Thoughts: Deliberate Problem Solving with Large Language Models"** (Yao, S. et al., 2023). This paper proposed the Tree of Thoughts (ToT) framework, generalizing CoT to allow for systematic exploration and backtracking.102
6. **"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"** (Lewis, P. et al., 2020). The foundational paper on Retrieval-Augmented Generation (RAG), detailing a method to connect LLMs with external knowledge sources.
7. **"A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT"** (White, J. et al., 2023). A practical and influential catalog of prompt patterns designed to solve common problems when interacting with LLMs.103

#### WORKS CITED

1. aws.amazon.com, accessed September 19, 2025, [https://aws.amazon.com/what-is/prompt-engineering/#:~:text=Prompt%20engineering%20is%20the%20process,high%2Dquality%20and%20relevant%20output.](https://aws.amazon.com/what-is/prompt-engineering/#:~:text=Prompt%20engineering%20is%20the%20process,high%2Dquality%20and%20relevant%20output.)
2. Prompt Engineering for AI Guide | Google Cloud, accessed September 19, 2025, [https://cloud.google.com/discover/what-is-prompt-engineering](https://cloud.google.com/discover/what-is-prompt-engineering)
3. Prompt engineering - Wikipedia, accessed September 19, 2025, [https://en.wikipedia.org/wiki/Prompt\_engineering](https://en.wikipedia.org/wiki/Prompt_engineering)
4. What is Prompt Engineering? - AI Prompt Engineering Explained ..., accessed September 19, 2025, [https://aws.amazon.com/what-is/prompt-engineering/](https://aws.amazon.com/what-is/prompt-engineering/)
5. 5 Timeless Prompt Engineering Principles for Reliable AI Outputs - General Assembly, accessed September 19, 2025, [https://generalassemb.ly/blog/timeless-prompt-engineering-principles-improve-ai-output-reliability/](https://generalassemb.ly/blog/timeless-prompt-engineering-principles-improve-ai-output-reliability/)
6. AI Demystified: What is Prompt Engineering? | University IT, accessed September 19, 2025, [https://uit.stanford.edu/service/techtraining/ai-demystified/prompt-engineering](https://uit.stanford.edu/service/techtraining/ai-demystified/prompt-engineering)
7. The Structure of a Good Prompt – Are You AI Ready? Investigating ..., accessed September 19, 2025, [https://ucddublin.pressbooks.pub/StudentResourcev1\_od/chapter/the-structure-of-a-good-prompt/](https://ucddublin.pressbooks.pub/StudentResourcev1_od/chapter/the-structure-of-a-good-prompt/)
8. Overview of prompting strategies | Generative AI on Vertex AI ..., accessed September 19, 2025, [https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies)
9. What is ChatGPT Prompt Engineering Principles - GeeksforGeeks, accessed September 19, 2025, [https://www.geeksforgeeks.org/blogs/chatgpt-prompt-engineering-principles/](https://www.geeksforgeeks.org/blogs/chatgpt-prompt-engineering-principles/)
10. Understanding Prompt Structure: Key Parts of a Prompt, accessed September 19, 2025, [https://learnprompting.org/docs/basics/prompt\_structure](https://learnprompting.org/docs/basics/prompt_structure)
11. AI Helpful Tips: Creating Effective Prompts - Office of OneIT - UNC Charlotte, accessed September 19, 2025, [https://oneit.charlotte.edu/2024/09/19/ai-helpful-tips-creating-effective-prompts/](https://oneit.charlotte.edu/2024/09/19/ai-helpful-tips-creating-effective-prompts/)
12. The ultimate guide to writing effective AI prompts - Work Life by Atlassian, accessed September 19, 2025, [https://www.atlassian.com/blog/artificial-intelligence/ultimate-guide-writing-ai-prompts](https://www.atlassian.com/blog/artificial-intelligence/ultimate-guide-writing-ai-prompts)
13. Elements of a Prompt - Prompt Engineering Guide, accessed September 19, 2025, [https://www.promptingguide.ai/introduction/elements](https://www.promptingguide.ai/introduction/elements)
14. General Tips for Designing Prompts | Prompt Engineering Guide, accessed September 19, 2025, [https://www.promptingguide.ai/introduction/tips](https://www.promptingguide.ai/introduction/tips)
15. the principles and practices of prompt engineering, accessed September 19, 2025, [https://www.prompts.ai/en/blog/the-principles-and-practices-of-prompt-engineering](https://www.prompts.ai/en/blog/the-principles-and-practices-of-prompt-engineering)
16. What is Context in Prompt Engineering? Here's Everything You ..., accessed September 19, 2025, [https://www.godofprompt.ai/blog/what-is-context-in-prompt-engineering](https://www.godofprompt.ai/blog/what-is-context-in-prompt-engineering)
17. The Ultimate Fucking Guide to Prompt Engineering : r/PromptEngineering - Reddit, accessed September 19, 2025, [https://www.reddit.com/r/PromptEngineering/comments/1j8m0rs/the\_ultimate\_fucking\_guide\_to\_prompt\_engineering/](https://www.reddit.com/r/PromptEngineering/comments/1j8m0rs/the_ultimate_fucking_guide_to_prompt_engineering/)
18. Best practices for prompt engineering with the OpenAI API, accessed September 19, 2025, [https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
19. Define GPT output formats in JSON with prompt builder - Microsoft Learn, accessed September 19, 2025, [https://learn.microsoft.com/en-us/power-platform/release-plan/2024wave2/ai-builder/define-specific-output-formats-prompt-builder](https://learn.microsoft.com/en-us/power-platform/release-plan/2024wave2/ai-builder/define-specific-output-formats-prompt-builder)
20. A Beginner's Guide to Engineering Prompts in ChatGPT (and Other AI Tools) - Medium, accessed September 19, 2025, [https://medium.com/@matthew.edgar.ritchie/a-beginners-guide-to-engineering-prompts-in-chatgpt-and-other-ai-tools-f8dbec88a309](https://medium.com/@matthew.edgar.ritchie/a-beginners-guide-to-engineering-prompts-in-chatgpt-and-other-ai-tools-f8dbec88a309)
21. Prompt engineering best practices for ChatGPT - OpenAI Help Center, accessed September 19, 2025, [https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt](https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt)
22. Understanding the Anatomy of a Prompt: Context + Instructions + Format, accessed September 19, 2025, [https://www.paradisosolutions.com/blog/how-to-structure-an-ai-prompt/](https://www.paradisosolutions.com/blog/how-to-structure-an-ai-prompt/)
23. Using GitHub Copilot in your IDE: Tips, tricks, and best practices, accessed September 19, 2025, [https://github.blog/developer-skills/github/how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/](https://github.blog/developer-skills/github/how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/)
24. 26 Prompt Engineering Principles for 2024 | by Dan Clearly - Medium, accessed September 19, 2025, [https://medium.com/@dan\_43009/26-prompt-engineering-principles-for-2024-775099ddfe94](https://medium.com/@dan_43009/26-prompt-engineering-principles-for-2024-775099ddfe94)
25. Zero-Shot Prompting - GeeksforGeeks, accessed September 19, 2025, [https://www.geeksforgeeks.org/nlp/zero-shot-prompting/](https://www.geeksforgeeks.org/nlp/zero-shot-prompting/)
26. What Are Zero-Shot Prompting and Few-Shot Prompting - MachineLearningMastery.com, accessed September 19, 2025, [https://machinelearningmastery.com/what-are-zero-shot-prompting-and-few-shot-prompting/](https://machinelearningmastery.com/what-are-zero-shot-prompting-and-few-shot-prompting/)
27. Zero-Shot Prompting: Examples, Theory, Use Cases | DataCamp, accessed September 19, 2025, [https://www.datacamp.com/tutorial/zero-shot-prompting](https://www.datacamp.com/tutorial/zero-shot-prompting)
28. Zero-Shot vs. Few-Shot Prompting: Key Differences - Shelf.io, accessed September 19, 2025, [https://shelf.io/blog/zero-shot-and-few-shot-prompting/](https://shelf.io/blog/zero-shot-and-few-shot-prompting/)
29. What is Zero-Shot Prompting? Examples & Applications - Digital Adoption, accessed September 19, 2025, [https://www.digital-adoption.com/zero-shot-prompting/](https://www.digital-adoption.com/zero-shot-prompting/)
30. Shot-Based Prompting: Zero-Shot, One-Shot, and Few-Shot Prompting, accessed September 19, 2025, [https://learnprompting.org/docs/basics/few\_shot](https://learnprompting.org/docs/basics/few_shot)
31. What is zero-shot prompting? - IBM, accessed September 19, 2025, [https://www.ibm.com/think/topics/zero-shot-prompting](https://www.ibm.com/think/topics/zero-shot-prompting)
32. Prompt Engineering 101: Understanding Zero-Shot, One-Shot, and Few-Shot | Codecademy, accessed September 19, 2025, [https://www.codecademy.com/article/prompt-engineering-101-understanding-zero-shot-one-shot-and-few-shot](https://www.codecademy.com/article/prompt-engineering-101-understanding-zero-shot-one-shot-and-few-shot)
33. Zero shot , One shot and Few shot learning with examples | by RAHULRAJ P V - Medium, accessed September 19, 2025, [https://rahulrajpvr7d.medium.com/zero-shot-one-shot-and-few-shot-learning-with-examples-8a3efdcbb158](https://rahulrajpvr7d.medium.com/zero-shot-one-shot-and-few-shot-learning-with-examples-8a3efdcbb158)
34. Include few-shot examples | Generative AI on Vertex AI | Google Cloud, accessed September 19, 2025, [https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/few-shot-examples](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/few-shot-examples)
35. The Few Shot Prompting Guide - PromptHub, accessed September 19, 2025, [https://www.prompthub.us/blog/the-few-shot-prompting-guide](https://www.prompthub.us/blog/the-few-shot-prompting-guide)
36. Do you know when to use 0-shot, 1-shot, or multi-shot prompts (e.g. give it 1 or more examples)? | SSW.Rules, accessed September 19, 2025, [https://www.ssw.com.au/rules/shot-prompts/](https://www.ssw.com.au/rules/shot-prompts/)
37. Provide examples (few-shot prompting) - Amazon Nova - AWS Documentation, accessed September 19, 2025, [https://docs.aws.amazon.com/nova/latest/userguide/prompting-examples.html](https://docs.aws.amazon.com/nova/latest/userguide/prompting-examples.html)
38. How to use few shot examples - Python LangChain, accessed September 19, 2025, [https://python.langchain.com/docs/how\_to/few\_shot\_examples/](https://python.langchain.com/docs/how_to/few_shot_examples/)
39. Few-Shot Prompting: Examples, Theory, Use Cases | DataCamp, accessed September 19, 2025, [https://www.datacamp.com/tutorial/few-shot-prompting](https://www.datacamp.com/tutorial/few-shot-prompting)
40. What is Role prompting? | PromptLayer, accessed September 19, 2025, [https://www.promptlayer.com/glossary/role-prompting](https://www.promptlayer.com/glossary/role-prompting)
41. Assigning Roles to Chatbots - Learn Prompting, accessed September 19, 2025, [https://learnprompting.org/docs/basics/roles](https://learnprompting.org/docs/basics/roles)
42. How to Prompt and Role Set for AI - Michigan Creative, accessed September 19, 2025, [https://michigancreative.com/how-to-prompt-and-role-set-for-ai/](https://michigancreative.com/how-to-prompt-and-role-set-for-ai/)
43. Role-Prompting: Does Adding Personas to Your Prompts Really Make a Difference?, accessed September 19, 2025, [https://www.prompthub.us/blog/role-prompting-does-adding-personas-to-your-prompts-really-make-a-difference](https://www.prompthub.us/blog/role-prompting-does-adding-personas-to-your-prompts-really-make-a-difference)
44. Why I don't like role prompts. : r/PromptEngineering - Reddit, accessed September 19, 2025, [https://www.reddit.com/r/PromptEngineering/comments/1koxgss/why\_i\_dont\_like\_role\_prompts/](https://www.reddit.com/r/PromptEngineering/comments/1koxgss/why_i_dont_like_role_prompts/)
45. Role Prompting: Guide LLMs with Persona-Based Tasks - Learn Prompting, accessed September 19, 2025, [https://learnprompting.org/docs/advanced/zero\_shot/role\_prompting](https://learnprompting.org/docs/advanced/zero_shot/role_prompting)
46. Zero-shot and few-shot learning - .NET | Microsoft Learn, accessed September 19, 2025, [https://learn.microsoft.com/en-us/dotnet/ai/conceptual/zero-shot-learning](https://learn.microsoft.com/en-us/dotnet/ai/conceptual/zero-shot-learning)
47. Zero-Shot vs Few-Shot prompting: A Guide with Examples - Vellum AI, accessed September 19, 2025, [https://www.vellum.ai/blog/zero-shot-vs-few-shot-prompting-a-guide-with-examples](https://www.vellum.ai/blog/zero-shot-vs-few-shot-prompting-a-guide-with-examples)
48. Chain-of-Thought Prompting Elicits Reasoning in Large ... - arXiv, accessed September 19, 2025, [https://arxiv.org/pdf/2201.11903](https://arxiv.org/pdf/2201.11903)
49. Self-Consistency Improves Chain of Thought Reasoning in ..., accessed September 19, 2025, [https://arxiv.org/pdf/2203.11171](https://arxiv.org/pdf/2203.11171)
50. Tree of Thoughts (ToT): Enhancing Problem-Solving in LLMs, accessed September 19, 2025, [https://learnprompting.org/docs/advanced/decomposition/tree\_of\_thoughts](https://learnprompting.org/docs/advanced/decomposition/tree_of_thoughts)
51. What is RAG? - Retrieval-Augmented Generation AI Explained ..., accessed September 19, 2025, [https://aws.amazon.com/what-is/retrieval-augmented-generation/](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
52. What is Chain-of-Thought Prompting? - Iguazio, accessed September 19, 2025, [https://www.iguazio.com/glossary/chain-of-thought-prompting/](https://www.iguazio.com/glossary/chain-of-thought-prompting/)
53. Chain of Thought Prompting Explained (with examples) - Codecademy, accessed September 19, 2025, [https://www.codecademy.com/article/chain-of-thought-cot-prompting](https://www.codecademy.com/article/chain-of-thought-cot-prompting)
54. How Chain of Thought (CoT) Prompting Helps LLMs Reason More Like Humans | Splunk, accessed September 19, 2025, [https://www.splunk.com/en\_us/blog/learn/chain-of-thought-cot-prompting.html](https://www.splunk.com/en_us/blog/learn/chain-of-thought-cot-prompting.html)
55. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models - arXiv, accessed September 19, 2025, [https://arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903)
56. Chain of Thought Prompting Guide - PromptHub, accessed September 19, 2025, [https://www.prompthub.us/blog/chain-of-thought-prompting-guide](https://www.prompthub.us/blog/chain-of-thought-prompting-guide)
57. Self-Consistency | Prompt Engineering Guide, accessed September 19, 2025, [https://www.promptingguide.ai/techniques/consistency](https://www.promptingguide.ai/techniques/consistency)
58. Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview, accessed September 19, 2025, [https://openreview.net/forum?id=1PL1NIMMrw](https://openreview.net/forum?id=1PL1NIMMrw)
59. Self-Consistency and Universal Self-Consistency Prompting, accessed September 19, 2025, [https://www.prompthub.us/blog/self-consistency-and-universal-self-consistency-prompting](https://www.prompthub.us/blog/self-consistency-and-universal-self-consistency-prompting)
60. What is Tree Of Thoughts Prompting? - IBM, accessed September 19, 2025, [https://www.ibm.com/think/topics/tree-of-thoughts](https://www.ibm.com/think/topics/tree-of-thoughts)
61. Beginner's Guide To Tree Of Thoughts Prompting (With Examples ..., accessed September 19, 2025, [https://zerotomastery.io/blog/tree-of-thought-prompting/](https://zerotomastery.io/blog/tree-of-thought-prompting/)
62. Tree of Thought Prompting: What It Is and How to Use It, accessed September 19, 2025, [https://www.vellum.ai/blog/tree-of-thought-prompting-framework-examples](https://www.vellum.ai/blog/tree-of-thought-prompting-framework-examples)
63. Tree of Thoughts Prompting (ToT) - Humanloop, accessed September 19, 2025, [https://humanloop.com/blog/tree-of-thoughts-prompting](https://humanloop.com/blog/tree-of-thoughts-prompting)
64. RAG Tutorial: A Beginner's Guide to Retrieval Augmented Generation, accessed September 19, 2025, [https://www.singlestore.com/blog/a-guide-to-retrieval-augmented-generation-rag/](https://www.singlestore.com/blog/a-guide-to-retrieval-augmented-generation-rag/)
65. What is Retrieval Augmented Generation (RAG)? - DataCamp, accessed September 19, 2025, [https://www.datacamp.com/blog/what-is-retrieval-augmented-generation-rag](https://www.datacamp.com/blog/what-is-retrieval-augmented-generation-rag)
66. Retrieval-Augmented Generation (RAG) from basics to advanced | by Tejpal Kumawat, accessed September 19, 2025, [https://medium.com/@tejpal.abhyuday/retrieval-augmented-generation-rag-from-basics-to-advanced-a2b068fd576c](https://medium.com/@tejpal.abhyuday/retrieval-augmented-generation-rag-from-basics-to-advanced-a2b068fd576c)
67. Retrieval-Augmented Generation (RAG) Tutorial, Examples & Best Practices | Nexla, accessed September 19, 2025, [https://nexla.com/ai-infrastructure/retrieval-augmented-generation/](https://nexla.com/ai-infrastructure/retrieval-augmented-generation/)
68. Best Prompts for Text Summarization: Enhance AI Summaries, accessed September 19, 2025, [https://blog.promptlayer.com/best-prompts-for-text-summarization-guide-to-ai-summaries/](https://blog.promptlayer.com/best-prompts-for-text-summarization-guide-to-ai-summaries/)
69. Prompt Engineering Guide: The Ultimate Guide to Generative AI - Learn Prompting, accessed September 19, 2025, [https://learnprompting.org/docs/introduction](https://learnprompting.org/docs/introduction)
70. How to Create Effective AI Prompts (With Examples) | Grammarly, accessed September 19, 2025, [https://www.grammarly.com/blog/ai/generative-ai-prompts/](https://www.grammarly.com/blog/ai/generative-ai-prompts/)
71. Prompt engineering for Copilot Chat - Visual Studio Code, accessed September 19, 2025, [https://code.visualstudio.com/docs/copilot/chat/prompt-crafting](https://code.visualstudio.com/docs/copilot/chat/prompt-crafting)
72. Prompt engineering for GitHub Copilot Chat - GitHub Docs, accessed September 19, 2025, [https://docs.github.com/en/copilot/concepts/prompt-engineering](https://docs.github.com/en/copilot/concepts/prompt-engineering)
73. Prompt Engineering Tips with GitHub Copilot - GeeksforGeeks, accessed September 19, 2025, [https://www.geeksforgeeks.org/git/prompt-engineering-tips-with-github-copilot/](https://www.geeksforgeeks.org/git/prompt-engineering-tips-with-github-copilot/)
74. 15 Prompting Techniques Every Developer Should Know for Code Generation, accessed September 19, 2025, [https://dev.to/nagasuresh\_dondapati\_d5df/15-prompting-techniques-every-developer-should-know-for-code-generation-1go2](https://dev.to/nagasuresh_dondapati_d5df/15-prompting-techniques-every-developer-should-know-for-code-generation-1go2)
75. Prompt Basics – Midjourney, accessed September 19, 2025, [https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics](https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics)
76. 30+ DALL·E 3 Prompts to Create Stunning Visuals - ClickUp, accessed September 19, 2025, [https://clickup.com/blog/dall-e-3-prompts/](https://clickup.com/blog/dall-e-3-prompts/)
77. Prompt and image attribute guide | Generative AI on Vertex AI ..., accessed September 19, 2025, [https://cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide](https://cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide)
78. How to Master Midjourney Prompts (Best Prompts in 2025) - Superside, accessed September 19, 2025, [https://www.superside.com/blog/midjourney-prompts](https://www.superside.com/blog/midjourney-prompts)
79. How to Use DALL-E 3: Tips, Examples, and Features | DataCamp, accessed September 19, 2025, [https://www.datacamp.com/tutorial/an-introduction-to-dalle3](https://www.datacamp.com/tutorial/an-introduction-to-dalle3)
80. DALLE3 and gpt-image-1 Prompt Tips and Tricks Thread - OpenAI Developer Community, accessed September 19, 2025, [https://community.openai.com/t/dalle3-and-gpt-image-1-prompt-tips-and-tricks-thread/498040](https://community.openai.com/t/dalle3-and-gpt-image-1-prompt-tips-and-tricks-thread/498040)
81. Midjourney Prompts 101 (With V6 Examples for 2025) - Printify, accessed September 19, 2025, [https://printify.com/blog/midjourney-prompts/](https://printify.com/blog/midjourney-prompts/)
82. Free Gemini AI prompts for realistic and professional-quality photos: A step-by-step process, accessed September 19, 2025, [https://timesofindia.indiatimes.com/technology/tech-tips/free-gemini-ai-prompts-for-realistic-and-professional-quality-photos-a-step-by-step-process/articleshow/123849888.cms](https://timesofindia.indiatimes.com/technology/tech-tips/free-gemini-ai-prompts-for-realistic-and-professional-quality-photos-a-step-by-step-process/articleshow/123849888.cms)
83. Quick Guide for Researchers using Generative AI Tools — Indeemo, accessed September 19, 2025, [https://indeemo.com/blog/iterative-prompting-generative-ai](https://indeemo.com/blog/iterative-prompting-generative-ai)
84. Iterative Prompt Development. Any prompt to the LLM(Large ..., accessed September 19, 2025, [https://medium.com/@aanshsavla2453/iterative-prompt-development-14252e0597f5](https://medium.com/@aanshsavla2453/iterative-prompt-development-14252e0597f5)
85. Iterative Prompt Development - Kaggle, accessed September 19, 2025, [https://www.kaggle.com/code/youssef19/iterative-prompt-development](https://www.kaggle.com/code/youssef19/iterative-prompt-development)
86. Iterative Prompt Refinement: Step-by-Step Guide - Ghost, accessed September 19, 2025, [https://latitude-blog.ghost.io/blog/iterative-prompt-refinement-step-by-step-guide/](https://latitude-blog.ghost.io/blog/iterative-prompt-refinement-step-by-step-guide/)
87. AI Prompt Analysis: How its Elevating the Creative Process in a Very Real Way, accessed September 19, 2025, [https://www.assemblestudio.com/blog/introducing-ai-prompt-analysis-how-its-elevating-the-creative-process-in-a-very-real-way](https://www.assemblestudio.com/blog/introducing-ai-prompt-analysis-how-its-elevating-the-creative-process-in-a-very-real-way)
88. Intelligent prompt analysis: Accelerate the performance of your GenAI apps - Outshift - Cisco, accessed September 19, 2025, [https://outshift.cisco.com/blog/prompt-intelligence-GenAI-app-accelerator](https://outshift.cisco.com/blog/prompt-intelligence-GenAI-app-accelerator)
89. What is Prompt iteration? | PromptLayer, accessed September 19, 2025, [https://www.promptlayer.com/glossary/prompt-iteration](https://www.promptlayer.com/glossary/prompt-iteration)
90. clearimpact.com, accessed September 19, 2025, [https://clearimpact.com/effective-ai-prompts/#:~:text=Instead%20of%20settling%20for%20an,useful%20the%20response%20will%20become.](https://clearimpact.com/effective-ai-prompts/#:~:text=Instead%20of%20settling%20for%20an,useful%20the%20response%20will%20become.)
91. Guide to Refining Prompts & AI Prompts Terms - Whole Whale, accessed September 19, 2025, [https://www.wholewhale.com/tips/guide-to-refining-prompts-ai-prompts-terms/](https://www.wholewhale.com/tips/guide-to-refining-prompts-ai-prompts-terms/)
92. 5 Common Prompt Engineering Mistakes Beginners Make, accessed September 19, 2025, [https://www.mygreatlearning.com/blog/prompt-engineering-beginners-mistakes/](https://www.mygreatlearning.com/blog/prompt-engineering-beginners-mistakes/)
93. 7 Prompt Engineering Mistakes Beginners Must Avoid (and How to ..., accessed September 19, 2025, [https://promptjesus.com/blog/7-prompt-engineering-mistakes-beginners-must-avoid](https://promptjesus.com/blog/7-prompt-engineering-mistakes-beginners-must-avoid)
94. Top Prompt Engineering Pitfalls & Mistakes to Avoid - Treyworks LLC, accessed September 19, 2025, [https://treyworks.com/common-prompt-engineering-mistakes-to-avoid/](https://treyworks.com/common-prompt-engineering-mistakes-to-avoid/)
95. Prompt Engineering Debugging: The 10 Most Common Issues We ..., accessed September 19, 2025, [https://www.reddit.com/r/PromptEngineering/comments/1mai2a1/prompt\_engineering\_debugging\_the\_10\_most\_common/](https://www.reddit.com/r/PromptEngineering/comments/1mai2a1/prompt_engineering_debugging_the_10_most_common/)
96. Prompt Engineering: Pitfalls to Avoid and Best Practices to Embrace ..., accessed September 19, 2025, [https://medium.com/@v4sooraj/prompt-engineering-pitfalls-to-avoid-and-best-practices-to-embrace-096ad737c9d0](https://medium.com/@v4sooraj/prompt-engineering-pitfalls-to-avoid-and-best-practices-to-embrace-096ad737c9d0)
97. \[2305.04091\] Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models - arXiv, accessed September 19, 2025, [https://arxiv.org/abs/2305.04091](https://arxiv.org/abs/2305.04091)
98. Prompt Engineering for ChatGPT by Vanderbilt - Coursera, accessed September 19, 2025, [https://www.coursera.org/learn/prompt-engineering](https://www.coursera.org/learn/prompt-engineering)
99. 16 prompt patterns and templates : r/ChatGPTPromptGenius - Reddit, accessed September 19, 2025, [https://www.reddit.com/r/ChatGPTPromptGenius/comments/1d3ocjb/16\_prompt\_patterns\_and\_templates/](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1d3ocjb/16_prompt_patterns_and_templates/)
100. Prompt Patterns | Generative AI | Vanderbilt University, accessed September 19, 2025, [https://www.vanderbilt.edu/generative-ai/prompt-patterns/](https://www.vanderbilt.edu/generative-ai/prompt-patterns/)
101. thunlp/PromptPapers: Must-read papers on prompt-based ... - GitHub, accessed September 19, 2025, [https://github.com/thunlp/PromptPapers](https://github.com/thunlp/PromptPapers)
102. Papers | Prompt Engineering Guide, accessed September 19, 2025, [https://www.promptingguide.ai/papers](https://www.promptingguide.ai/papers)
103. Top Research Papers on Prompt Engineering - Paperguide, accessed September 19, 2025, [https://paperguide.ai/papers/top/research-papers-prompt-engineering/](https://paperguide.ai/papers/top/research-papers-prompt-engineering/)
