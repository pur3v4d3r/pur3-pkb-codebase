---
title: ""
id: ""
type: ""
status: ""
rating: ""
source: ""
url: ""
tags: []
aliases: [] 
link-up: []
link-related: []
date created: 2025-10-10T03:28:11
date modified: 2025-11-06T22:41:32
---

**Tree-of-Thought (ToT)** (Yao et al., 2023b), also known as Tree of Thoughts, (Long, 2023), creates a tree-like search problem by starting with an initial problem then generating multiple possible steps in the form of thoughts (as from a CoT). It evaluates the progress each step makes towards solving the problem (through prompting) and decides which steps to continue with, then keeps creating more thoughts. ToT is particularly effective for tasks that require search and planning.

**Prompt Mining** (Jiang et al., 2020) is the process of discovering optimal "middle words" in prompts through large corpus analysis. These middle words are effectively prompt templates. For example, instead of using the common "Q: A:" format for fewshot prompts, there may exist something similar that occurs more frequently in the corpus. Formats which occur more often in the corpus will likely lead to improved prompt performance.

**Uncertainty-Routed CoT Prompting** (Google, 2023) samples multiple CoT reasoning paths, then selects the majority if it is above a certain threshold (calculated based on validation data). If not, it samples greedily and selects that response. This method demonstrates improvement on the MMLU benchmark for both GPT-4 and Gemini Ultra models

**Complexity-based Prompting** (Fu et al., 2023b) involves two major modifications to CoT. First, it selects complex examples for annotation and inclusion in the prompt, based on factors like question length or reasoning steps required. Second, during inference, it samples multiple reasoning chains (answers) and uses a majority vote among chains exceeding a certain length threshold, under the premise that longer reasoning indicates higher answer quality. This technique has shown improvements on three mathematical reasoning datasets.

**Least-to-Most Prompting** (Zhou et al., 2022a) starts by prompting a LLM to break a given problem into sub-problems without solving them. Then, it solves them sequentially, appending model responses to the prompt each time, until it arrives at a final result. This method has shown significant improvements in tasks involving symbolic , compositional generalization, and mathematical reasoning.

**Decomposed Prompting** (DECOMP) (Khot et al., 2022) Few-Shot prompts a LLM to show it how to use certain functions. These might include things like string splitting or internet searching; these are often implemented as separate LLM calls. Given this, the LLM breaks down its original problem into sub-problems which it sends to different functions. It has shown improved performance over Least-to-Most prompting on some tasks.

**Demonstration Ensembling (DENSE)** (Khalifa et al., 2023) creates multiple few-shot prompts, each containing a distinct subset of exemplars from the training set. Next, it aggregates over their outputs to generate a final response.

**Max Mutual Information Method** (Sorensen et al., 2022) creates multiple prompt templates with 14 varied styles and exemplars, then selects the optimal template as the one that maximizes mutual information between the prompt and the LLM's outputs.

**Ensembling** In GenAI, ensembling is the process of using multiple prompts to solve the same problem, then aggregating these responses into a final output. In many cases, a majority vote—selecting the most frequent response—is used to generate the final output. Ensembling techniques reduce the variance of LLM outputs and often improving accuracy, but come with the cost of increasing the number of model calls needed to reach a final answer.

**Meta-Reasoning over Multiple CoTs** (Yoran et al., 2023) is similar to universal SelfConsistency; it first generates multiple reasoning chains (but not necessarily final answers) for a given problem. Next, it inserts all of these chains in a single prompt template then generates a final answer from them.

**DiVeRSe** (Li et al., 2023i) creates multiple prompts for a given problem then performs SelfConsistency for each, generating multiple reasoning paths. They score reasoning paths based on each step in them then select a final response.

**Consistency-based Self-adaptive Prompting** (COSP) (Wan et al., 2023a) constructs Few-Shot CoT prompts by running Zero-Shot CoT with Self-Consistency on a set of examples then selecting a high agreement subset of the outputs to be included in the final prompt as exemplars. It again performs Self-Consistency with this final prompt.

**Universal Self-Adaptive Prompting (USP)** (Wan et al., 2023b) builds upon the success of COSP, aiming to make it generalizable to all tasks. USP makes use of unlabeled data to generate exemplars and a more complicated scoring function to select them. Additionally, USP does not use Self-Consistency.

**Mixture of Reasoning Experts** (MoRE) (Si et al., 2023d) creates a set of diverse reasoning experts by using different specialized prompts for different reasoning types (such as retrieval augmentation prompts for factual reasoning, Chain-of-Thought reasoning for multi-hop and math reasoning, and generated knowledge prompting for commonsense reasoning). The best answer from all experts is selected based on an agreement score.

**Self-Refine** (Madaan et al., 2023) is an iterative framework where, given an initial answer from the LLM, it prompts the same LLM to provide feedback on the answer, and then prompts the LLM to improve the answer based on the feedback. This iterative process continues until a stopping condition is met (e.g., max number of steps reached). Self-Refine has demonstrated improvement across
a range of reasoning, coding, and generation tasks.

**Self-Consistency** (Wang et al., 2022) is based on the intuition that multiple different reasoning paths can lead to the same answer. This method first prompts the LLM multiple times to perform CoT, crucially with a non-zero temperature to elicit diverse reasoning paths. Next, it uses a majority vote over all generated responses to select a final response. Self-Consistency has shown improvements on arithmetic, commonsense, and symbolic reasoning tasks.

**Universal Self-Consistency** (Chen et al., 2023e) is similar to Self-Consistency except that rather\ than selecting the majority response by programmatically counting how often it occurs, it inserts all outputs into a prompt template that selects the majority answer. This is helpful for free-form text generation and cases where the same answer may be output slightly differently by different prompts

**Automatic Prompt Engineer (APE)** (Zhou et al., 2022b) uses a set of exemplars to generate a ZeroShot instruction prompt. It generates multiple possible prompts, scores them, then creates variations of the best ones (e.g. by using prompt paraphrasing). It iterates on this process until some desiderata are reached.

**Gradientfree Instructional Prompt Search (GrIPS)** (Prasad et al., 2023) is similar to APE, but uses a more complex set of operations including deletion, addition, swapping, and paraphrasing in order to create variations of a starting prompt

**Thread-of-Thought (ThoT)** Prompting (Zhou et al., 2023) consists of an improved thought inducer for CoT reasoning. Instead of "Let's think step by step," it uses "Walk me through this context in manageable parts step by step, summarizing and analyzing as we go." This thought inducer works well in question-answering and retrieval settings, especially when dealing with large, complex contexts.

**Step-Back Prompting** (Zheng et al., 2023c) is a modification of CoT where the LLM is first asked a generic, high-level question about relevant concepts or facts before delving into reasoning. This approach has improved performance significantly on multiple reasoning benchmarks for both PaLM2L and GPT-4.

**Automatic Chain-of-Thought (Auto-CoT)** Prompting (Zhang et al., 2022b) uses Wei et al. (2022b)'s Zero-Shot prompt to automatically generate chains of thought. These are then used to build a Few-Shot CoT prompt for a test sample
