---
license: mit
language:
- en
size_categories:
- 1K<n<10K
pretty_name: "PromptReport"
tags:
- prompt engineering
- dataset
- papers
- academic papers
- arxiv
- semantic scholar
- acl anthology
---
# Prompt Report Dataset
This repository contains the dataset from the Prompt Report []() paper. 
Use huggingface hub or git lfs to download this, and use the instructions in our code [repository](https://github.com/trigaten/Prompt_Systematic_Review) to run the experiments.
We also have a [paper](https://arxiv.org/pdf/2406.06608) and [website](https://trigaten.github.io/Prompt_Survey_Site/) that detail our findings.
## master_papers.csv
The master papers file is a master record of all the papers in the final dataset 

## arxiv_papers_for_human_review.csv
This csv contains the original group of papers reviewed by humans

## blacklist.csv
This csv contains papers that were determined to be irrelevant / shouldn't be present in the final dataset. 

## papers/
This folder contains all the final set of papers, after scraping, deduplication, and review. 