Hugging Face's logo
Hugging Face
Models
Datasets
Spaces
Community
Docs
Enterprise
Pricing


Back to Articles
Understanding and Implementing the Tree of Thoughts Paradigm
Community Article
Published March 26, 2025
Sambit Mukherjee's avatar
Sambit Mukherjee
sadhaklal

Follow
Motivation
The Tree of Thoughts (ToT) paper (Yao et al.) demonstrates how to couple the reasoning capabilities of LLMs with a heuristic-guided tree search framework. But before diving into its implementation, let's set the context.

LLMs are designed for autoregressive text generation. This makes them confined to token-level, left-to-right decision-making processes during inference. According to the authors of the ToT paper, this is reminiscent of:

The "System 1" (fast, automatic, unconscious) mode of thinking in humans.
The associative "model-free" paradigm in reinforcement learning.
Given the right type of prompt, this autoregressive mechanism elicits chain of thought (CoT) reasoning (Wei et al.), allowing LLMs to tackle a wide range of tasks requiring mathematical, symbolic, commonsense, and knowledge reasoning.

However, generating a reasoning trace in a left-to-right manner falls short for tasks that need exploration, strategic lookahead, or where initial decisions play an important role (because future decisions depend on them).

In the ToT paper, the authors suggest that left-to-right CoT reasoning might benefit from augmentation by a heuristic-guided tree search framework. This is reminiscent of:

The "System 2" (slow, deliberate, conscious) mode of thinking in humans.
The paradigm of deliberate "model-based" planning in reinforcement learning.
According to the authors, such a system is characterized by two key features:

The ability to maintain and explore diverse alternatives for current, i.e., local (node-level) decisions.
The ability to evaluate each node, and actively look ahead or backtrack to make global decisions.
Such a system would be able to consider multiple different reasoning paths, self-evaluate choices to decide the next course of action, as well as look ahead or backtrack when necessary to make global choices.

Below is a comparison of the ToT paradigm with three other popular reasoning paradigms.



Our objectives in this blog post are the following:

Understand the Tree of Thoughts (ToT) paradigm.
Implement a reusable TreeOfThoughts class.
To achieve these, we shall examine two tasks sequentially: Creative Writing and Game of 24. By understanding how to apply ToT on these tasks (one at a time), we shall build up to our reusable class.

Note: The ToT paper also covers three additional tasks: Mini Crosswords, GSM8k and StrategyQA. For the sake of brevity, we won't be covering those in this blog post.

Setup
We'll need the following imports:

from openai import OpenAI
from huggingface_hub import InferenceClient
from google.colab import userdata # Only if you're using Colab.
from typing import Union, Optional, List
from collections.abc import Callable
import re
from collections import deque
from IPython.display import display, HTML

We'll try to make our TreeOfThoughts class compatible with both OpenAI's Chat Completions API and the Hugging Face's Serverless Inference API.

If you want to use OpenAI, you can create your client as follows:

client = OpenAI(api_key=userdata.get('OPENAI_API_KEY'))

The ToT paper uses GPT-4 for all experiments. If you want to reproduce the paper's results, stick with the OpenAI option.

However, if you prefer to use Hugging Face, you can create your client as follows:

# client = InferenceClient(provider="hf-inference", api_key=userdata.get('HF_TOKEN'), headers={'x-use-cache': "false"})

Note: You must turn off caching by passing the following argument: headers={"x-use-cache": "false"}. Otherwise, you'll not be able to generate n i.i.d. (independent and identically distributed) responses. (As we shall see, generating n i.i.d. responses is required for the Creative Writing task.)

Now, let's create a bare-bones Preliminary class with a chat_completions method.

class Preliminary:
    def __init__(self, client: Union[OpenAI, InferenceClient], model: str = "gpt-4"):
        self.client = client
        self.model = model

    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/models.py
    def chat_completions(
            self,
            prompt: str,
            temperature: float = 0.7,
            max_tokens: int = 1000,
            n: int = 1,
            stop: Optional[List[str]] = None,
            **kwargs
    ) -> List[str]:
        outputs = []
        messages = [{'role': "user", 'content': prompt}]
        if isinstance(self.client, OpenAI):
            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=temperature,
                max_tokens=max_tokens,
                n=n, # The `n` responses are i.i.d.
                stop=stop,
                **kwargs
            )
            outputs.extend([choice.message.content for choice in response.choices])
        else: # `self.client` is an instance of `InferenceClient`.
            # The Hugging Face API doesn't support the `n` argument. Hence, we need to use a loop to generate `n` i.i.d. responses.
            for _ in range(n):
                response = self.client.chat.completions.create(
                    messages=messages,
                    model=self.model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    stop=stop,
                    **kwargs
                )
                outputs.append(response.choices[0].message.content)
        return outputs

Descriptions of the n and stop parameters (from the OpenAI API documentation):





Let's test out the method.

prelim = Preliminary(client, model="gpt-4")
# prelim = Preliminary(client, model="meta-llama/Meta-Llama-3.1-8B-Instruct")
responses = prelim.chat_completions("Write a haiku about delicious food.", n=2)
for response in responses: # The two responses are i.i.d.
    print(response)
    print("---")

Savoring each bite,
Flavors dance on eager tongues,
Feast of joy and light.
---
Savory delight,
Flavors dance upon my tongue,
Feast in every bite.
---

Creative Writing
In the Creative Writing task, the LLM is provided an input sequence comprising four random sentences. The task entails writing a coherent passage with four paragraphs that end with the four random sentences, respectively.



Note: "#ToT steps" in the above table refers to the number of intermediate steps. As we shall see, for the Creative Writing task, there is only one intermediate step: generating a writing plan.

The following is an example of an input sequence:

# Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/data/text/data_100_random_text.txt
input_seq = """1. It isn't difficult to do a handstand if you just stand on your hands.
2. It caught him off guard that space smelled of seared steak.
3. When she didn’t like a guy who was trying to pick her up, she started using sign language.
4. Each person who knows you has a different perception of who you are."""

Before diving into ToT, let's see how we might use a zero-shot chain of thought (CoT) approach to solve this problem.

# Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/prompts/text.py
zero_shot_cot_prompt = f"""Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be:

{input_seq}

Make a plan then write. Your output should be of the following format:

Plan:
Your plan here.

Passage:
Your passage here.
"""
print(zero_shot_cot_prompt)

Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be:

1. It isn't difficult to do a handstand if you just stand on your hands.
2. It caught him off guard that space smelled of seared steak.
3. When she didn’t like a guy who was trying to pick her up, she started using sign language.
4. Each person who knows you has a different perception of who you are.

Make a plan then write. Your output should be of the following format:

Plan:
Your plan here.

Passage:
Your passage here.

Note: You might be wondering how the above is a zero-shot CoT prompt. After all, the famous sentence "Let's think step by step." (Kojima et al.) is missing in the above prompt. Well, the answer is that the sentence "Make a plan then write." elicits chain of thought reasoning, i.e., the intermediate step of generating a plan.

responses = prelim.chat_completions(zero_shot_cot_prompt, n=1) # Since we're passing `n=1`, we'll get back only one response.
print(responses[0])

Plan:
My plan is to create a narrative that revolves around an astronaut's experience in space. The first paragraph will include the astronaut's training before the mission, focusing on physical fitness and particularly handstands. In the second paragraph, the astronaut will finally be in space and be surprised by the smell. The third paragraph will introduce a flashback of the astronaut's unique way of dealing with unwanted attention before the mission. The last paragraph will reflect on how these experiences shape different people's perceptions of the astronaut.

Passage:
As a child, John always had a knack for gymnastics. He was more comfortable in the world upside down, doing handstands and cartwheels, than others were walking on their two feet. His skills would later prove to be beneficial in his career as an astronaut, where physical fitness was a top priority. As he trained for his first mission, he found comfort in the old familiarity of handstands, an exercise that was part of their zero-gravity training. He would often tell his colleagues, "It isn't difficult to do a handstand if you just stand on your hands."

When John finally made it to space, it was nothing like he expected. The zero-gravity, the silence, and the view were all breathtaking. But what caught his attention the most was the smell. After removing his helmet inside the spacecraft, a strong, strange aroma filled his nostrils. It was almost like... seared steak. It caught him off guard that space smelled of seared steak.

Back on Earth, John was a quiet and reserved man. He disliked the attention he got from being an astronaut, especially from women who were more interested in his status than him. He found a clever way to deal with unwanted advances. He remembered a friend who was deaf and communicated through sign language. When she didn’t like a guy who was trying to pick her up, she started using sign language.

To his colleagues, John was a strong and capable astronaut. To the women he rebuffed, he was a strange man who suddenly became mute. To his old gymnastics coach, he was a talented gymnast who could've won medals. Each person had a different story about John, a different perception. Each person who knows you has a different perception of who you are.

The LLM generated a plan, followed by a passage.

Next, let's see what the stop argument does.

responses = []
stop_string = 'Passage:'
for step in range(1, 3):
    if step == 1:
        response = prelim.chat_completions(zero_shot_cot_prompt, n=1, stop=[stop_string])[0]
    else:
        response = prelim.chat_completions(zero_shot_cot_prompt, n=1)[0]
    responses.append(response)
    print(f"Step {step} output:\n---")
    print(response)
    print("---\n~~~")

Step 1 output:
---
Plan:
1. Introduce the main character, a gymnast, and describe their training routine.
2. Transition to the main character's dream of being an astronaut, introducing the unexpected aspects of that experience.
3. Introduce a secondary character and their attempts to flirt with the main character, and the main character's unique way of avoiding it.
4. Discuss the overall theme of individual perception and how it applies to the main character.


---
~~~
Step 2 output:
---
Plan:
1. Discuss the simplicity in achieving a seemingly complex task.
2. Introduce a character who is an astronaut and describe his surprising experience in space.
3. Introduce a female character with an unconventional approach to warding off unwanted attention.
4. Conclude with a philosophical reflection on identity and perception.

Passage:
In life, many tasks may seem daunting at first, but upon closer inspection, they are often much simpler than they first appear. A common example of this is a handstand. To many, the idea of balancing one's entire body weight on their hands seems nearly impossible. But when you break it down, it's all about finding your center of gravity and pushing off with the right amount of force. It isn't difficult to do a handstand if you just stand on your hands.

A similar principle can be applied to Robert, an astronaut who had trained for years to venture into the unknown of space. He had prepared for every possible scenario, or so he thought. There was one aspect of space that he hadn't expected. He was aware of the silence, the darkness, and the weightlessness, but he hadn't predicted the smell. It caught him off guard that space smelled of seared steak.

Meanwhile, back on Earth, a woman named Sarah was dealing with her own set of unique circumstances. Sarah had a knack for attracting attention, especially from men she had no interest in. Over the years, she developed a unique way of dissuading these unwanted suitors. Instead of simply telling them she wasn't interested, she would start communicating only in sign language. When she didn’t like a guy who was trying to pick her up, she started using sign language.

These three stories may seem disconnected, but they all highlight the individuality and unique perception inherent in every person. Each person's experiences and actions shape how others perceive them, and no two perceptions are exactly alike. Just as Sarah used sign language to express her disinterest, Robert was surprised by the smell of space, and you may find handstands easy once you try, people's perceptions of you are shaped by their own unique experiences and interpretations. Each person who knows you has a different perception of who you are.
---
~~~

Here's what happened:

In step 1, we passed the stop string 'Passage:'. As soon as the LLM generated this stop string, text generation stopped. Passing this stop string allowed us to generate ONLY the plan.
In step 2, we didn't pass any stop string. As a result, the LLM generated a plan AND a passage.
But notice that the plan in step 2 is generated from scratch. But when using ToT, that's not what we want. Rather, we want step 2 to utilize the plan generated in step 1. How do we do this?

Well, we need to maintain the state. But what is a state?

A state is simply an accumulation of the thoughts generated so far. For all practical purposes, it's a concatenation of all the thoughts so far (separated by '\n').

We need to create a callable that dynamically generates a prompt by appending the state to the base prompt.

def get_thought_gen_prompt(input_seq: str, state: str) -> str:
    """Get thought generation prompt.

    Keyword arguments:
    input_seq -- the input sequence
    state -- concatenation of all the thoughts so far (separated by '\n')
    """
    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/prompts/text.py
    base_prompt = f"""Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be:

{input_seq}

Make a plan then write. Your output should be of the following format:

Plan:
Your plan here.

Passage:
Your passage here.
"""
    if state == '': # Root node; no thoughts have been generated yet.
        return base_prompt
    else:
        return base_prompt + '\n' + state

Now, let's simulate generating a plan (in step 1) followed by a passage (in step 2), where the prompt for step 2 utilizes the state of step 1.

states = ['']
thoughts = ['']
n_steps = 2 # 1 intermediate step + 1 output generation step.
for step in range(1, n_steps + 1):
    prompt = get_thought_gen_prompt(input_seq, states[-1])
    print(f"Step {step} prompt:\n---")
    print(f"{prompt}\n---")
    if step == 1:
        thought = prelim.chat_completions(prompt, n=1, stop=[stop_string])[0]
    else:
        thought = prelim.chat_completions(prompt, n=1)[0]
    thoughts.append(thought)
    if states[-1] == '':
        updated_state = thought
    else:
        updated_state = states[-1] + '\n' + thought
    states.append(updated_state)
    print(f"Step {step} updated state:\n---")
    print(states[-1])
    print("---\n~~~")

Step 1 prompt:
---
Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be:

1. It isn't difficult to do a handstand if you just stand on your hands.
2. It caught him off guard that space smelled of seared steak.
3. When she didn’t like a guy who was trying to pick her up, she started using sign language.
4. Each person who knows you has a different perception of who you are.

Make a plan then write. Your output should be of the following format:

Plan:
Your plan here.

Passage:
Your passage here.

---
Step 1 updated state:
---
Plan:
In the first paragraph, I'll introduce a character who is a gymnast. The second paragraph will shift to this character's dream of being an astronaut, and the surprising revelation he has while in space. The third paragraph will introduce a new character, a woman who cleverly avoids unwanted attention. The final paragraph will tie the two characters together, exploring their perspectives of each other.


---
~~~
Step 2 prompt:
---
Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be:

1. It isn't difficult to do a handstand if you just stand on your hands.
2. It caught him off guard that space smelled of seared steak.
3. When she didn’t like a guy who was trying to pick her up, she started using sign language.
4. Each person who knows you has a different perception of who you are.

Make a plan then write. Your output should be of the following format:

Plan:
Your plan here.

Passage:
Your passage here.

Plan:
In the first paragraph, I'll introduce a character who is a gymnast. The second paragraph will shift to this character's dream of being an astronaut, and the surprising revelation he has while in space. The third paragraph will introduce a new character, a woman who cleverly avoids unwanted attention. The final paragraph will tie the two characters together, exploring their perspectives of each other.


---
Step 2 updated state:
---
Plan:
In the first paragraph, I'll introduce a character who is a gymnast. The second paragraph will shift to this character's dream of being an astronaut, and the surprising revelation he has while in space. The third paragraph will introduce a new character, a woman who cleverly avoids unwanted attention. The final paragraph will tie the two characters together, exploring their perspectives of each other.


Passage:
Matthew had always been nimble, even as a boy. He had a knack for gymnastics, and his specialty was doing handstands. He would often say to his friends who marveled at his skill, "It's all about balance and strength. It isn't difficult to do a handstand if you just stand on your hands."

As Matthew grew older, his passion for gymnastics remained, but his dreams reached for the stars. He wanted to become an astronaut. He trained relentlessly, and finally, he found himself floating in the weightlessness of space. The first time he took off his helmet inside the spaceship, he was taken aback. It caught him off guard that space smelled of seared steak.

Back on earth, there was a woman named Emily. She was vibrant and witty, but often found herself the target of unwanted attention. Whenever a man tried to harass her or make her uncomfortable, she had a trick up her sleeve. When she didn’t like a guy who was trying to pick her up, she started using sign language.

Emily and Matthew were friends. They had met at a mutual friend's party and hit it off. Emily saw Matthew as a dreamer, always reaching for the stars, while Matthew saw Emily as a quick-witted, independent woman. They had different perceptions of each other, but that wasn't strange. After all, each person who knows you has a different perception of who you are.
---
~~~

It works!

Now, let's dive into ToT. A node is defined as follows:

class TreeNode:
    def __init__(self, state: str, thought: str, value: float = None):
        self.state = state
        self.thought = thought
        self.value = value
        self.children = []

We shall implement ToT with a multi-way tree data structure. In other words, each node is allowed to have more than two children. Hence, the children attribute is a list. (Note: Although using an explicit data structure isn't strictly required for ToT, it makes it easier to understand the algorithm and visualize the tree.)

But what exactly is a thought? From the paper:

While CoT samples thoughts coherently without explicit decomposition, ToT leverages problem properties to design and decompose intermediate thought steps.

In other words, we need to precisely define what an intermediate thought is, and what an output is. In the Creative Writing task, an intermediate thought is a writing plan. And an output is a passage...

As noted previously, a state is simply a concatenation of all the thoughts so far (separated by '\n').

A value is a heuristic assigned to a particular state. Values are used to prune nodes which aren't promising.

For the Creative Writing task, a customized version of the Breadth-First Search (BFS) algorithm is used. Here's how it works:

Execution starts at the root node. Here, the thought is an empty string, and so is the state (since no thoughts have been generated yet). The root node can be considered level 0 of the tree.
Now, it's time for step 1. A thought generator is used to generate n_candidates i.i.d. intermediate thoughts (plans). Each of these thoughts is a child of the root node. These nodes together form level 1 of the tree. (For the Creative Writing task, the authors have chosen to set n_candidates to 5.)
A state evaluator is used to vote n_evals times on the plans. (For the Creative Writing task, the authors have chosen to set n_evals to 5).
A heuristic calculator is used to collate these votes, and assign a heuristic to each plan. (The heuristic is simply the total number of votes received by a plan.)
Time to prune. The parameter breadth_limit refers to the number of most promising states to retain (after pruning) - at each level of the tree. (For the Creative Writing task, the authors have chosen to set breadth_limit to 1. As a result, only the best plan is retained.)
Now, it's time for step 2. In this step, execution proceeds exactly like in points 2, 3, 4, and 5 above. In other words, the thought generator generates 5 outputs (passages). These nodes together form level 2 of the tree. The state evaluator votes 5 times on them. The heuristic calculator collates the votes, and assigns a value to each node. Pruning is used to retain the winning passage.
The following is a pictorial summary of the above:



For the Creative Writing task, the thought generation strategy used is 'sample'. This means that n_candidates thoughts are sampled in an i.i.d. manner. From the paper:

This strategy works better when the thought space is rich (e.g., each thought is a paragraph), and i.i.d. samples lead to diversity.

(We shall see that for the Game of 24 task, a different thought generation strategy is used: 'propose'. More on this later...)

For the Creative Writing task, the state evaluation strategy used is 'vote'. From the paper:

When problem success is harder to directly value (e.g., passage coherency), it is natural to instead compare different partial solutions and vote for the most promising one.

(We shall see that for the Game of 24 task, a different state evaluation strategy is used: 'value'. More on this later...)

It turns out that the state evaluator is the LLM itself. However, it (obviously) needs a different prompt than the thought generator. The state evaluation prompt is given by the following callable:

def get_state_eval_prompt(input_seq: str, states: List[str]) -> str:
    """Get state evaluation prompt.

    Keyword arguments:
    input_seq -- the input sequence
    states -- the states to vote on
    """
    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/prompts/text.py
    vote_prompt = '''Given an instruction and several choices, decide which choice is most promising. Analyze each choice in detail, then conclude in the last line "The best choice is {s}", where s the integer id of the choice.'''
    instruction = f"""Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be:

{input_seq}

Make a plan then write. Your output should be of the following format:

Plan:
Your plan here.

Passage:
Your passage here.
"""
    prompt = vote_prompt + '\n\nInstruction:\n' + instruction + '\n'
    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/tasks/text.py
    for i, state in enumerate(states, start=1):
        prompt += f'Choice {i}:\n{state}\n'
    return prompt

Don't worry if the above function seems unclear. We shall properly inspect the state evaluation prompt below.

For the Creative Writing task, the heuristic calculator is given by the following callable:

# Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/tasks/text.py
def heuristic_calculator(states: List[str], state_evals: List[str]) -> List[int]:
    n_candidates = len(states)
    vote_results = [0] * n_candidates
    for j in range(len(state_evals)):
        pattern = r".*best choice is .*(\d+).*"
        match = re.match(pattern, state_evals[j], re.DOTALL)
        if match:
            vote = int(match.groups()[0]) - 1
            if vote in range(n_candidates):
                vote_results[vote] += 1
        else:
            print(f'Warning! Did not get a regex match for the following state evaluation:\n{state_evals[j]}')
    return vote_results

Once again, don't worry if the above function seems cryptic. We shall examine it in detail below.

For the moment, let's proceed to write the TreeOfThoughts class for the Creative Writing Task. It contains the following methods:

__init__
chat_completions
thought_generator
state_evaluator
bfs
generate_html_tree (a utility to generate an HTML representation of the tree)
render_html_tree (a utility to plot an HTML representation of the tree)
class TreeOfThoughts:
    def __init__(
            self,
            client: Union[OpenAI, InferenceClient],
            model: str,
            input_seq: str,
            get_thought_gen_prompt: Callable,
            get_state_eval_prompt: Callable,
            heuristic_calculator: Callable
    ):
        self.client = client
        self.model = model # e.g., "gpt-4" if using `OpenAI` and "meta-llama/Meta-Llama-3.1-8B-Instruct" if using `InferenceClient`.
        self.input_seq = input_seq # Note: `input_seq` contains the input sequence ("x" in the ToT paper), before wrapping it with a prompt.
        self.root = TreeNode(state='', thought='')
        self.n_steps = 2 # 1 intermediate step + 1 output generation step.
        # Note: The tree height is equal to `n_steps + 1`. That is, we include the root node when calculating the tree height.
        self.thought_gen_strategy = 'sample'
        self.get_thought_gen_prompt = get_thought_gen_prompt
        self.n_candidates = 5 # The number of candidates (thoughts) to generate from a particular node. Also referred to as "size limit" and "k" in the ToT paper.
        self.stop_string = 'Passage:'
        self.state_eval_strategy = 'vote'
        self.get_state_eval_prompt = get_state_eval_prompt
        self.n_evals = 5 # The number of times to vote on the states.
        self.heuristic_calculator = heuristic_calculator
        self.breadth_limit = 1 # The number of most promising states to retain (after pruning) - at each level of the tree.

    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/models.py
    def chat_completions(
            self,
            prompt: str,
            temperature: float = 0.7,
            max_tokens: int = 1000,
            n: int = 1,
            stop: Optional[List[str]] = None,
            **kwargs
    ) -> List[str]:
        outputs = []
        messages = [{'role': "user", 'content': prompt}]
        if isinstance(self.client, OpenAI):
            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=temperature,
                max_tokens=max_tokens,
                n=n, # The `n` responses are i.i.d.
                stop=stop,
                **kwargs
            )
            outputs.extend([choice.message.content for choice in response.choices])
        else: # `self.client` is an instance of `InferenceClient`.
            # The Hugging Face API doesn't support the `n` argument. Hence, we need to use a loop to generate `n` i.i.d. responses.
            for _ in range(n):
                response = self.client.chat.completions.create(
                    messages=messages,
                    model=self.model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    stop=stop,
                    **kwargs
                )
                outputs.append(response.choices[0].message.content)
        return outputs

    def thought_generator(self, state: str, stop_string: Optional[List[str]] = None) -> List[str]:
        if self.thought_gen_strategy == 'sample':
            prompt = self.get_thought_gen_prompt(self.input_seq, state)
            thoughts = self.chat_completions(prompt, n=self.n_candidates, stop=stop_string)
            return thoughts
        else: # `self.thought_gen_strategy` is equal to 'propose'.
            pass

    def state_evaluator(self, states: List[str]) -> List[float]:
        if self.state_eval_strategy == 'vote':
            prompt = self.get_state_eval_prompt(self.input_seq, states)
            state_evals = self.chat_completions(prompt, n=self.n_evals)
            vote_results = self.heuristic_calculator(states, state_evals)
            return vote_results
        else: # `self.state_eval_strategy` is equal to 'value'.
            pass

    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/methods/bfs.py
    def bfs(self, verbose: bool = True) -> str:
        queue = deque()
        queue.append(self.root)

        for step in range(1, self.n_steps + 1):
            if verbose:
                print(f"Step {step} (corresponding to level {step} of the tree):-\n---")
            for i in range(len(queue)):
                node = queue.popleft()
                if verbose:
                    print(f"Node {i + 1} in level {step}:-")
                    if node.state != "":
                        print(f"State of current node:-\n{node.state}\n---")
                    else:
                        print("State of current node:-\n<EMPTY STRING> (root node; no thoughts generated yet)\n---")

                if step == 1:
                    thoughts = self.thought_generator(state=node.state, stop_string=[self.stop_string])
                else:
                    thoughts = self.thought_generator(state=node.state)
                if node.state == '':
                    updated_states = thoughts
                else:
                    updated_states = [node.state + '\n' + thought for thought in thoughts]
                for j in range(len(thoughts)):
                    if verbose:
                        print(f"Thought candidate {j + 1}:-\n{thoughts[j]}\n---")
                    child = TreeNode(state=updated_states[j], thought=thoughts[j])
                    node.children.append(child)
                    queue.append(child)
                if verbose:
                    print("Each of the above thought candidates has been added as a child of the current node.\n---")

            if verbose:
                print("Using the state evaluator to obtain values...\n---")
            states = [node.state for node in queue]
            values = self.state_evaluator(states=states)
            for i in range(len(queue)):
                queue[i].value = values[i]
                if verbose:
                    print(f"Element {i + 1} in queue:-\n")
                    print(f"Value: {queue[i].value}\n---")

            if verbose:
                print("Initiating pruning (using the values obtained from the state evaluator).")
                print(f"Number of elements in queue: {len(queue)}")
            sorted_nodes = sorted(queue, key=lambda node: node.value, reverse=True)
            if step == self.n_steps:
                if verbose:
                    print("Since this is the last step, setting the breadth limit to 1.")
                    print("In other words, retaining only the highest value element (in this last step).\n---")
                top_b_nodes = sorted_nodes[:1]
            else:
                if verbose:
                    print(f"Since this isn't the last step, leaving the breadth limit {self.breadth_limit} unchanged.\n---")
                top_b_nodes = sorted_nodes[:self.breadth_limit]
            top_b_states = [node.state for node in top_b_nodes]
            for i in range(len(queue)):
                node = queue.popleft()
                if verbose:
                    print(f"Element {i + 1} in queue:-\n")
                if node.state in top_b_states:
                    if verbose:
                        print(f"Retaining this element as it's in the top {len(top_b_states)} elements.\n---")
                    queue.append(node)
                else:
                    if verbose:
                        print(f"Dropping this element as it's not in the top {len(top_b_states)} elements.\n---")

            if verbose:
                print("~~~")

        # Return the thought of the highest value node (from the last step):
        node = queue.popleft()
        return node.thought

    def generate_html_tree(self, node: TreeNode) -> str:
        if node is None:
            return ""
        else:
            html = f"""<div class='node'>
<p>State:<br>{node.state}</p>
<hr>
<p>Thought:<br>{node.thought}</p>
<hr>
<p>Value:<br>{node.value}</p>"""
            for child in node.children:
                html += f"""<div class='child'>{self.generate_html_tree(child)}</div>"""
            html += """</div>"""
            return html

    def render_html_tree(self):
        html_tree = self.generate_html_tree(self.root)
        wrapped_html = f"""<!DOCTYPE html>
<html>
<head>
    <style>
        .node {{
            display: inline-block;
            border: 1px solid blue;
            padding: 10px;
            margin: 5px;
            text-align: center;
        }}
        .child {{
            display: flex;
        }}
    </style>
</head>
<body>
    {html_tree}
</body>
</html>"""
        display(HTML(wrapped_html))

Let's instantiate our class.

tot = TreeOfThoughts(client, "gpt-4", input_seq, get_thought_gen_prompt, get_state_eval_prompt, heuristic_calculator)

But before we run the BFS algorithm, let's slow down a bit, and simulate thought generation in step 1.

state = tot.root.state
thoughts = tot.thought_generator(state=state, stop_string=[tot.stop_string])
if state == '':
    updated_states = thoughts
else:
    updated_states = [state + '\n' + thought for thought in thoughts]
len(updated_states)

5

5 thoughts have been generated. Let's take a look at them.

for j in range(len(thoughts)):
    print(f"Thought candidate {j + 1}:-")
    print(thoughts[j])
    print("---\n")

Thought candidate 1:-
Plan:
1. Introduce a young boy learning acrobats and his ease in performing handstands.
2. Transition to a different character, an astronaut who experiences the strange smell of space.
3. Shift the narrative to a woman in a bar who uses sign language to ward off unwanted attention.
4. Conclude with a reflection on the varying perceptions of these characters by the people in their lives.


---

Thought candidate 2:-
Plan:
1. The first paragraph will detail the narrator's attempt at learning how to do a handstand. 
2. The second paragraph will transition to the narrator's dream of becoming an astronaut and his experiences in a simulated environment.
3. The third paragraph will delve into a romantic situation involving a woman who uses sign language as a way to deflect unwanted attention.
4. The fourth paragraph will reflect on the different perceptions people have of the narrator, in light of his experiences and actions.


---

Thought candidate 3:-
Plan:
1. Begin with a discussion on a gymnastics class, focusing on the instructor teaching how to do a handstand.
2. Transition to a character's first experience in space, with an unexpected sensory experience.
3. Introduce a new character who has a unique way of dealing with unwanted attention.
4. Conclude with a reflection on the nature of personal identity and perception.


---

Thought candidate 4:-
Plan:
In this passage, I will begin by talking about a gymnastics class where the instructor is teaching how to do a handstand. Then, the passage will transition to a man who is experiencing space for the first time and is surprised by what he senses. The third paragraph will introduce a woman who has a unique way of dealing with unwanted attention. Lastly, I will conclude with a commentary on how everyone has their own unique perception of us.


---

Thought candidate 5:-
Plan:
1. Introduce a character who is trying to learn a handstand.
2. Transition to the character's dream of becoming an astronaut, leading to a surprising fact about space.
3. Introduce another character, a woman, who has developed an interesting strategy to avoid unwanted advances.
4. Conclude with a reflection on the nature of perception and identity.


---

Next, as promised, let's properly inspect the state evaluation prompt.

prompt = tot.get_state_eval_prompt(tot.input_seq, updated_states)
print(prompt)

Given an instruction and several choices, decide which choice is most promising. Analyze each choice in detail, then conclude in the last line "The best choice is {s}", where s the integer id of the choice.

Instruction:
Write a coherent passage of 4 short paragraphs. The end sentence of each paragraph must be:

1. It isn't difficult to do a handstand if you just stand on your hands.
2. It caught him off guard that space smelled of seared steak.
3. When she didn’t like a guy who was trying to pick her up, she started using sign language.
4. Each person who knows you has a different perception of who you are.

Make a plan then write. Your output should be of the following format:

Plan:
Your plan here.

Passage:
Your passage here.

Choice 1:
Plan:
1. Introduce a young boy learning acrobats and his ease in performing handstands.
2. Transition to a different character, an astronaut who experiences the strange smell of space.
3. Shift the narrative to a woman in a bar who uses sign language to ward off unwanted attention.
4. Conclude with a reflection on the varying perceptions of these characters by the people in their lives.


Choice 2:
Plan:
1. The first paragraph will detail the narrator's attempt at learning how to do a handstand. 
2. The second paragraph will transition to the narrator's dream of becoming an astronaut and his experiences in a simulated environment.
3. The third paragraph will delve into a romantic situation involving a woman who uses sign language as a way to deflect unwanted attention.
4. The fourth paragraph will reflect on the different perceptions people have of the narrator, in light of his experiences and actions.


Choice 3:
Plan:
1. Begin with a discussion on a gymnastics class, focusing on the instructor teaching how to do a handstand.
2. Transition to a character's first experience in space, with an unexpected sensory experience.
3. Introduce a new character who has a unique way of dealing with unwanted attention.
4. Conclude with a reflection on the nature of personal identity and perception.


Choice 4:
Plan:
In this passage, I will begin by talking about a gymnastics class where the instructor is teaching how to do a handstand. Then, the passage will transition to a man who is experiencing space for the first time and is surprised by what he senses. The third paragraph will introduce a woman who has a unique way of dealing with unwanted attention. Lastly, I will conclude with a commentary on how everyone has their own unique perception of us.


Choice 5:
Plan:
1. Introduce a character who is trying to learn a handstand.
2. Transition to the character's dream of becoming an astronaut, leading to a surprising fact about space.
3. Introduce another character, a woman, who has developed an interesting strategy to avoid unwanted advances.
4. Conclude with a reflection on the nature of perception and identity.

Armed with this prompt, we can simulate state evaluation in step 1.

state_evals = tot.chat_completions(prompt, n=tot.n_evals)
for i, eval in enumerate(state_evals, start=1):
    print(f"Vote {i}:")
    print("---")
    print(eval)
    print("---\n~~~")

Vote 1:
---
Analysis:

Choice 1: This plan provides a clear and logical structure that will allow for smooth transitions between each paragraph and incorporates all the given sentences. It does not, however, maintain a single point of view or theme between the paragraphs, which may lead to a disjointed narrative.

Choice 2: This plan maintains a consistent narrative perspective, focusing on the experiences of a single narrator. This will likely result in a more coherent narrative, but it may be challenging to convincingly incorporate the given sentences into this narrative.

Choice 3: Like choice 1, this plan provides a clear and logical structure but does not maintain a single point of view or theme between the paragraphs. This may lead to a disjointed narrative.

Choice 4: This plan is similar to choices 1 and 3, but it provides a slightly more detailed outline of what each paragraph will discuss. This may help in ensuring a smooth transition between each paragraph.

Choice 5: This plan introduces two characters and maintains a consistent theme of perception and identity throughout. This may result in a more coherent narrative than choices 1, 3, and 4, but the transition between the first two paragraphs may be challenging.

The best choice is 2.
---
~~~
Vote 2:
---
Analyzing each choice:

Choice 1: The plan is well-structured and clearly addresses the sentence prompts. Using different characters for each paragraph can make the passage a bit disjointed, but it does offer a diverse range of scenarios.

Choice 2: This plan effectively integrates the sentence prompts into a single narrative. The transitions between the paragraphs are smooth and the passage maintains a coherent focus on the narrator.

Choice 3: Similar to Choice 1, this plan uses different characters for each paragraph. While it addresses the sentence prompts, the transitions between the paragraphs may be abrupt.

Choice 4: This plan is similar to Choice 3 but lacks the specificity and clear transitions that make a passage coherent and engaging.

Choice 5: This plan also integrates the sentence prompts into a single narrative. However, the transitions between paragraphs are not as smoothly outlined as in Choice 2, which may affect the coherence of the passage.

The best choice is 2.
---
~~~
Vote 3:
---
Analysis:

Choice 1: This plan seems well-structured and the transitions between paragraphs seem logical. However, it might be challenging to tie all these characters together coherently in just four paragraphs.

Choice 2: This plan follows the narrator through different stages of his life, which can make the passage more coherent and relatable. However, it might be hard to smoothly transition from a gymnastics class to space simulation.

Choice 3: This plan also introduces too many characters and it might be difficult to tie them all in a coherent story. However, it does follow the instructions closely.

Choice 4: This plan is similar to choice 3, but it lacks the detail that might make the passage engaging and interesting. It does follow the instructions closely.

Choice 5: This plan seems to introduce less characters and might be easier to execute in a coherent, engaging passage. It also follows the instructions closely.

The best choice is 5.
---
~~~
Vote 4:
---
Analyzing each choice:

Choice 1:
This plan offers a clear transition between the different characters and their experiences. It does not simply focus on one character, but rather tells the stories of several characters, providing a more diverse and interesting narrative. The conclusion brings all the narratives together, reflecting on the varying perceptions of these characters.

Choice 2:
This plan focuses on one character, the narrator, who experiences all the situations mentioned in the end sentences. This could provide a more in-depth exploration of a single character, but it may also limit the variety of experiences and perspectives.

Choice 3:
This plan offers a variety of experiences and perspectives, similar to Choice 1. However, it doesn't clearly specify how it will connect these different experiences and perspectives in the conclusion, which might lead to a less coherent narrative.

Choice 4:
This plan is very similar to Choice 3, but it does offer a clear conclusion that ties everything together. It also specifies that it will introduce a commentary on personal perception, which may provide a deeper exploration of the theme.

Choice 5:
This plan also offers a variety of experiences and characters, similar to Choice 1 and 3. However, it doesn't clearly specify how it will connect these different experiences and perspectives in the conclusion, which might lead to a less coherent narrative.

The best choice is 1. It provides a coherent plan for introducing multiple characters and experiences, while ensuring that these are tied together in the conclusion. It also offers the opportunity to explore a variety of perspectives, which may lead to a richer narrative.
---
~~~
Vote 5:
---
Analyzing each choice:

Choice 1: This plan is good as it gives a clear layout of the story. However, it may lack coherence as it jumps between three different characters. The transition between these characters might be difficult to make smoothly.

Choice 2: This plan maintains the same character throughout the passage, ensuring better coherence. It provides a clear transition between each paragraph and maintains a consistent narrative voice.

Choice 3: This plan is similar to Choice 1, with its use of different characters, which could potentially disrupt the coherence of the passage. It also doesn't clearly explain how the story will transition between characters.

Choice 4: This plan is also similar to Choice 1, but it lacks the explicit detail of how the story will transition between characters. It may also disrupt the coherence due to the abrupt shifts between characters.

Choice 5: This plan is also similar to Choice 1, and it suffers from the same potential issues. It does not clearly explain how the story will transition between characters.

The best choice is 2.
---
~~~

Next, as promised, we shall examine the heuristic calculator in detail.

An array containing all zeros is initialized as follows:

n_candidates = len(updated_states)
vote_results = [0] * n_candidates
vote_results

[0, 0, 0, 0, 0]

Then, the votes are counted using the following loop. At each iteration, a regular expression is used to find which choice the LLM voted for.

for j in range(len(state_evals)):
    pattern = r".*best choice is .*(\d+).*"
    match = re.match(pattern, state_evals[j], re.DOTALL)
    if match:
        vote = int(match.groups()[0]) - 1
        if vote in range(n_candidates):
            vote_results[vote] += 1
    else:
        print(f'Warning! Did not get a regex match for the following state evaluation:\n\n{state_evals[j]}')
vote_results

[1, 3, 0, 0, 1]

How about pruning? How does that work?

Well, we've implemented the BFS algorithm with a queue. Let's suppose that our queue contains the following objects (each representing a node).

queue = deque()
queue.append({'state': "q", 'value': 1})
queue.append({'state': "t", 'value': 5})
queue.append({'state': "w", 'value': 2})
queue.append({'state': "r", 'value': 4})
queue.append({'state': "e", 'value': 3})

Imagine our chosen breadth_limit is 3. In other words, we want to retain the nodes with the 3 highest values.

breadth_limit = 3
top_b_nodes = sorted(queue, key=lambda node: node['value'], reverse=True)[:breadth_limit]
top_b_nodes

[{'state': 't', 'value': 5},
 {'state': 'r', 'value': 4},
 {'state': 'e', 'value': 3}]

From the above, we can create a list containing the top 3 states.

top_b_states = [node['state'] for node in top_b_nodes]
top_b_states

['t', 'r', 'e']

Now, we'll use a loop to dequeue (popleft) each node. If the state of the node is in top_b_states, we'll enqueue (append) it back.

for i in range(len(queue)):
    node = queue.popleft()
    if node['state'] in top_b_states:
        queue.append(node)

for node in queue:
    print(node)

{'state': 't', 'value': 5}
{'state': 'r', 'value': 4}
{'state': 'e', 'value': 3}

Pruning simulated! (The above pruning logic is part of the bfs method.)

Finally, let's actually call the bfs method. By passing verbose=True, we can watch the BFS algorithm in action.

output = tot.bfs(verbose=True)
print(output)

Step 1 (corresponding to level 1 of the tree):-
---
Node 1 in level 1:-
State of current node:-
<EMPTY STRING> (root node; no thoughts generated yet)
---
Thought candidate 1:-
Plan:
1. Introduce a character who likes to do handstands in his spare time and how he has mastered this skill.
2. The same character gets the opportunity to go to space and his surprising discovery there.
3. Introduce a female character who has her own unique way of dealing with unwanted attention.
4. Discuss how every individual has their own perception of a person based on their interactions and experiences with them.


---
Thought candidate 2:-
Plan:
In the first paragraph, introduce a gymnastics class where a trainer is teaching learners how to do a handstand. In the second paragraph, shift to the story of an astronaut on his first space mission. In the third paragraph, introduce a woman with a unique strategy to avoid unwanted attention in a bar. Finally, in the fourth paragraph, discuss how different people have different perceptions of the same person, reflecting on the earlier characters.


---
Thought candidate 3:-
Plan:
1. Introduce the protagonist's experience with gymnastics and how he found the handstand easy.
2. Shift to the protagonist's experience as an astronaut and his surprise at the smell of space.
3. Introduce a female character and her clever tactic to deal with unwanted attention.
4. Discuss the idea of perceptions and how it varies from person to person.


---
Thought candidate 4:-
Plan:
The first paragraph will establish the context of a gymnastics class where the protagonist is learning to do a handstand. The second paragraph will transition to a discussion about the protagonist's interests, specifically his fascination with space travel. The third paragraph will introduce a new character, who is a friend of the protagonist and has a unique way of deflecting unwanted attention. The last paragraph will elaborate on the protagonist's reflections about individual perceptions and how they shape our identity.


---
Thought candidate 5:-
Plan:
In this passage, we will start by introducing an adventurous protagonist who is always up for a challenge and loves to learn, using the example of a handstand as a metaphor for his approach to life. We will then move into the protagonist's journey into becoming an astronaut, where he experiences the unexpected smell of space. In the third paragraph, we will introduce a love interest who has a unique way of warding off unwanted suitors. The final paragraph will delve into the protagonist's introspective revelation about the nature of identity and perception.


---
Each of the above thought candidates has been added as a child of the current node.
---
Using the state evaluator to obtain values...
---
Element 1 in queue:-

Value: 0
---
Element 2 in queue:-

Value: 0
---
Element 3 in queue:-

Value: 0
---
Element 4 in queue:-

Value: 1
---
Element 5 in queue:-

Value: 4
---
Initiating pruning (using the values obtained from the state evaluator).
Number of elements in queue: 5
Since this isn't the last step, leaving the breadth limit 1 unchanged.
---
Element 1 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 2 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 3 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 4 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 5 in queue:-

Retaining this element as it's in the top 1 elements.
---
~~~
Step 2 (corresponding to level 2 of the tree):-
---
Node 1 in level 2:-
State of current node:-
Plan:
In this passage, we will start by introducing an adventurous protagonist who is always up for a challenge and loves to learn, using the example of a handstand as a metaphor for his approach to life. We will then move into the protagonist's journey into becoming an astronaut, where he experiences the unexpected smell of space. In the third paragraph, we will introduce a love interest who has a unique way of warding off unwanted suitors. The final paragraph will delve into the protagonist's introspective revelation about the nature of identity and perception.


---
Thought candidate 1:-
Passage:
The protagonist was always up for a challenge; he thrived on overcoming obstacles and learning new things. He was the kind of person who would see the world from a different angle, literally and metaphorically. One day, he watched a group of people doing handstands, and they made it look so easy. He decided to give it a try, and after a few failed attempts, he finally managed to stay upright. He laughed to himself as he thought, it isn't difficult to do a handstand if you just stand on your hands.

His adventurous spirit eventually led him into the field of space exploration. After years of rigorous training, he found himself floating in the vast expanse of space, looking at Earth from a completely different perspective. He took off his helmet inside the spaceship and was taken aback by the smell. It was not the sterile smell of the spaceship interior that he expected, but a rich, almost comforting aroma. It caught him off guard that space smelled of seared steak.

Back on Earth, he met a woman who was as unique and intriguing as the cosmos he had explored. She was not easily impressed and had her own ways of dealing with unwanted attention. Once, in a crowded bar, he saw her being approached by a man who was clearly not taking no for an answer. Instead of responding verbally, she started communicating with him in sign language. When she didn’t like a guy who was trying to pick her up, she started using sign language.

As he got to know her better, he started reflecting on his own life and how people perceived him. He realized that everyone he met saw a different version of him based on their interactions. His family saw him as a dreamer, his colleagues as a daredevil, and she saw him as a kindred spirit. Each person who knows you has a different perception of who you are.
---
Thought candidate 2:-
Passage:
Tom was a man of adventure, always seeking new challenges and experiences. He reveled in the thrill of uncertainty, the rush of adrenaline, and the pure joy that came with accomplishment. His friends often marveled at his fearlessness, to which Tom would laugh and say, "fear is simply a matter of perspective." He believed that the key to overcoming any obstacle was to approach it head on, and with a bit of creativity. After all, he would often quip, it isn't difficult to do a handstand if you just stand on your hands.

This adventurous spirit led Tom to pursue a career as an astronaut. The idea of exploring the unknown, of venturing into a place few have ever been, was tantalizing. When he finally made it into space, he was awed by the beauty of the cosmos. But one thing he hadn't expected was the smell. As he removed his helmet inside the space station, he was met with a scent that was unmistakably familiar yet oddly out of place. It caught him off guard that space smelled of seared steak.

Back on Earth, Tom met a woman named Maya, who was as intriguing as she was beautiful. She had a passion for learning, just like Tom, and had even picked up sign language as a hobby. Maya had a unique approach to dealing with unwanted advances. Instead of giving the usual excuses or ignoring the person, she would simply switch to sign language. When she didn’t like a guy who was trying to pick her up, she started using sign language.

As Tom got to know Maya, he began to reflect on the nature of identity and perception. He realized that while he saw himself as an adventurous astronaut, others might see him as a daredevil, a risk-taker, or even a reckless thrill-seeker. Maya, on the other hand, saw him as a man of curiosity, courage, and resilience. This led him to an important realization: each person who knows you has a different perception of who you are.
---
Thought candidate 3:-
Passage:
The protagonist, a young man of distinct courage and curiosity, had always been one for challenges. From a young age, he had a knack for trying new things, no matter how daunting they seemed. He had a way of simplifying complex tasks, breaking them down into manageable steps, and thereby making the impossible seem possible. When asked how he had mastered the art of doing a handstand, he'd always reply with a smirk, "It isn't difficult to do a handstand if you just stand on your hands."

As he grew older, his thirst for adventure and knowledge led him to pursue a career that was not only challenging but also out of this world, literally. He became an astronaut, a profession that took him to the stars and beyond. His first journey into space was nothing short of extraordinary. One experience, in particular, was unexpected. As he took off his helmet inside the spaceship, he was surprised by a distinct smell. It caught him off guard that space smelled of seared steak.

Back on earth, he met an intriguing woman who was as unique as she was beautiful. She had a whimsical sense of humor and a knack for dealing with unwanted attention. Whenever a man approached her with an intention she didn't appreciate, she had a unique way of warding them off. When she didn’t like a guy who was trying to pick her up, she started using sign language.

Throughout these experiences, he realized something profound about the nature of identity. He understood that the way he saw himself, the adventurous child, the daring astronaut, and the man smitten by love, was unique to him. Similarly, each person in his life, from his parents to his colleagues, and the woman he loved, saw a different version of him based on their interactions and experiences. Each person who knows you has a different perception of who you are.
---
Thought candidate 4:-
Passage:
Our protagonist has always been an adventurous soul, always up to conquer the impossible. Whether it's climbing the highest mountain or diving deep into the sea, he loves to challenge himself. He takes on every challenge as if it were as simple as standing on your hands. As he often says, "It isn't difficult to do a handstand if you just stand on your hands."

Having conquered most challenges on Earth, he set his eyes on the final frontier - space. Training to become an astronaut, he learned and experienced things beyond his wildest dreams. His first journey into space brought an unexpected surprise. As he floated in the vacuum of space, he opened his helmet visor and was hit with a smell that was strange yet oddly familiar. It caught him off guard that space smelled of seared steak.

Back on earth, amid all his adventures and achievements, he met a woman who was as unique and intriguing as space itself. She was not easily impressed, and she had a unique way of dealing with men she wasn't interested in. Once, when a rather persistent suitor tried his luck, she simply switched to sign language. When she didn’t like a guy who was trying to pick her up, she started using sign language.

As our protagonist navigated through these diverse experiences, he began to realize a profound truth about identity and perception. He was a different person to each individual he met - an adventurer to some, a reckless risk-taker to others, a hero to many, and a mystery to the woman he loved. He understood that each person who knows you has a different perception of who you are.
---
Thought candidate 5:-
Passage:
Our protagonist, John, was an adventurous spirit, always eager to take on new challenges. He had a knack for making the seemingly demanding tasks seem simple, much like his unique perspective on handstands. To John, handstands weren't about balance or strength, but a simple reorientation of perspective. After all, he'd say with a smirk, "It isn't difficult to do a handstand if you just stand on your hands."

His thirst for adventure eventually led John to become an astronaut. The training was rigorous, and the anticipation of the unknown was exhilarating. However, nothing prepared him for his first spacewalk. As he popped open his suit's visor, an unexpected smell wafted into his nostrils. It was a surreal moment, heightened by the realization that space smelled of seared steak. It caught him off guard.

Back on Earth, John met Lily, a vibrant woman with a sparkling wit and an unusual strategy for dealing with unwanted advances. Lily was deaf, but she didn't let that define her; instead, she used it to her advantage. When she didn’t like a guy who was trying to pick her up, she started using sign language, a tactic that left most suitors confused and quickly deterred.

John's travels and encounters with people like Lily made him realize that everyone he met had a different perception of him. Some saw him as the daring astronaut, others as the curious man who saw handstands in an unusual light, and to Lily, he was a patient man who took the time to learn sign language. It was a profound realization: each person who knows you has a different perception of who you are.
---
Each of the above thought candidates has been added as a child of the current node.
---
Using the state evaluator to obtain values...
---
Element 1 in queue:-

Value: 3
---
Element 2 in queue:-

Value: 0
---
Element 3 in queue:-

Value: 0
---
Element 4 in queue:-

Value: 0
---
Element 5 in queue:-

Value: 2
---
Initiating pruning (using the values obtained from the state evaluator).
Number of elements in queue: 5
Since this is the last step, setting the breadth limit to 1.
In other words, retaining only the highest value element (in this last step).
---
Element 1 in queue:-

Retaining this element as it's in the top 1 elements.
---
Element 2 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 3 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 4 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 5 in queue:-

Dropping this element as it's not in the top 1 elements.
---
~~~
Passage:
The protagonist was always up for a challenge; he thrived on overcoming obstacles and learning new things. He was the kind of person who would see the world from a different angle, literally and metaphorically. One day, he watched a group of people doing handstands, and they made it look so easy. He decided to give it a try, and after a few failed attempts, he finally managed to stay upright. He laughed to himself as he thought, it isn't difficult to do a handstand if you just stand on your hands.

His adventurous spirit eventually led him into the field of space exploration. After years of rigorous training, he found himself floating in the vast expanse of space, looking at Earth from a completely different perspective. He took off his helmet inside the spaceship and was taken aback by the smell. It was not the sterile smell of the spaceship interior that he expected, but a rich, almost comforting aroma. It caught him off guard that space smelled of seared steak.

Back on Earth, he met a woman who was as unique and intriguing as the cosmos he had explored. She was not easily impressed and had her own ways of dealing with unwanted attention. Once, in a crowded bar, he saw her being approached by a man who was clearly not taking no for an answer. Instead of responding verbally, she started communicating with him in sign language. When she didn’t like a guy who was trying to pick her up, she started using sign language.

As he got to know her better, he started reflecting on his own life and how people perceived him. He realized that everyone he met saw a different version of him based on their interactions. His family saw him as a dreamer, his colleagues as a daredevil, and she saw him as a kindred spirit. Each person who knows you has a different perception of who you are.

Ok. Time to visualize the tree.

tot.render_html_tree()

Note: The HTML tree isn't rendering properly within this blog post. (However, it renders perfectly within Colab/Jupyter.) Hence, I've saved the tree as an HTML file, which you can view here. Below is a screenshot of the same:



In the above visualization, each box represents a node. Nested boxes represent descendants. (Due to pruning, not all nodes have children.)

Hope you've enjoyed the blog post so far! The next section on the Game of 24 task is a bit long and nuanced. So now might be a good time for a coffee/tea break if you need one :)

Game of 24
In the Game of 24 task, the LLM is provided an input sequence comprising four numbers. The task entails generating an equation (using only the +, -, * and / operators) that combines the four numbers to reach 24. (Each of the four numbers can be used only once in the equation.)

For example, if the input sequence is "4 9 10 13", then a valid output is the equation "(13 - 9) * (10 - 4) = 24".



Note: "#ToT steps" in the above table refers to the number of intermediate steps. For the Game of 24 task, there are three intermediate steps: each intermediate step is an intermediate equation (as shown in the table above).

Before diving into ToT, let's see how we might use a few-shot chain of thought (CoT) approach to solve this problem.

Let's consider the following example:

# Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/data/24/24.csv
input_seq = '1 1 1 8'

# Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/prompts/game24.py
five_shot_cot_prompt = f'''Use numbers and basic arithmetic operations (+ - * /) to obtain 24. Each step, you are only allowed to choose two of the remaining numbers to obtain a new number.
Input: 4 4 6 8
Steps:
4 + 8 = 12 (left: 4 6 12)
6 - 4 = 2 (left: 2 12)
2 * 12 = 24 (left: 24)
Answer: (6 - 4) * (4 + 8) = 24
Input: 2 9 10 12
Steps:
12 * 2 = 24 (left: 9 10 24)
10 - 9 = 1 (left: 1 24)
24 * 1 = 24 (left: 24)
Answer: (12 * 2) * (10 - 9) = 24
Input: 4 9 10 13
Steps:
13 - 10 = 3 (left: 3 4 9)
9 - 3 = 6 (left: 4 6)
4 * 6 = 24 (left: 24)
Answer: 4 * (9 - (13 - 10)) = 24
Input: 1 4 8 8
Steps:
8 / 4 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
Answer: (1 + 8 / 4) * 8 = 24
Input: 5 5 5 9
Steps:
5 + 5 = 10 (left: 5 9 10)
10 + 5 = 15 (left: 9 15)
15 + 9 = 24 (left: 24)
Answer: ((5 + 5) + 5) + 9 = 24
Input: {input_seq}
'''
print(five_shot_cot_prompt)

Use numbers and basic arithmetic operations (+ - * /) to obtain 24. Each step, you are only allowed to choose two of the remaining numbers to obtain a new number.
Input: 4 4 6 8
Steps:
4 + 8 = 12 (left: 4 6 12)
6 - 4 = 2 (left: 2 12)
2 * 12 = 24 (left: 24)
Answer: (6 - 4) * (4 + 8) = 24
Input: 2 9 10 12
Steps:
12 * 2 = 24 (left: 9 10 24)
10 - 9 = 1 (left: 1 24)
24 * 1 = 24 (left: 24)
Answer: (12 * 2) * (10 - 9) = 24
Input: 4 9 10 13
Steps:
13 - 10 = 3 (left: 3 4 9)
9 - 3 = 6 (left: 4 6)
4 * 6 = 24 (left: 24)
Answer: 4 * (9 - (13 - 10)) = 24
Input: 1 4 8 8
Steps:
8 / 4 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
Answer: (1 + 8 / 4) * 8 = 24
Input: 5 5 5 9
Steps:
5 + 5 = 10 (left: 5 9 10)
10 + 5 = 15 (left: 9 15)
15 + 9 = 24 (left: 24)
Answer: ((5 + 5) + 5) + 9 = 24
Input: 1 1 1 8

In the above prompt, five examples of "Input", "Steps" and "Answer" are provided, followed by the new "Input". The hope is that the LLM can perform in-context learning to generate the appropriate "Steps" and "Answer" for the new "Input". Let's try it out.

responses = prelim.chat_completions(five_shot_cot_prompt, n=1)
print(responses[0])

Steps:
1 + 1 = 2 (left: 1 2 8)
2 * 8 = 16 (left: 1 16)
16 + 8 = 24 (left: 24)
Answer: ((1 + 1) * 8) + 1 = 24

Few-shot CoT fails on this occassion! Can ToT do better? Let's find out.

The first thing we'll need is an appropriate thought generation strategy.

Recall that in the Creative Writing task, we used the 'sample' thought generation strategy (which involved generating n_candidates thoughts in an i.i.d. manner). However, when each thought is very short (e.g., just a word or a line), an i.i.d. strategy leads to a lot of duplicate thoughts being generated.

To avoid this problem, the authors have adopted a different thought generation strategy for the Game of 24 task: 'propose'. The 'propose' strategy entails generating thoughts sequentially using a propose prompt. (The generated thoughts are separated by a delimiter such as '\n'). From the paper:

This strategy works better when the thought space is more constrained (e.g., each thought is just a word or a line), so proposing different thoughts in the same context avoids duplication.

Let's consider an example to make the idea concrete. The following is the propose prompt for intermediate steps:

# Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/prompts/game24.py
remaining_numbers = input_seq
one_shot_propose_prompt = f'''Input: 2 8 8 14
Possible next steps:
2 + 8 = 10 (left: 8 10 14)
8 / 2 = 4 (left: 4 8 14)
14 + 2 = 16 (left: 8 8 16)
2 * 8 = 16 (left: 8 14 16)
8 - 2 = 6 (left: 6 8 14)
14 - 8 = 6 (left: 2 6 8)
14 /  2 = 7 (left: 7 8 8)
14 - 2 = 12 (left: 8 8 12)
Input: {remaining_numbers}
Possible next steps:
'''
print(one_shot_propose_prompt)

Input: 2 8 8 14
Possible next steps:
2 + 8 = 10 (left: 8 10 14)
8 / 2 = 4 (left: 4 8 14)
14 + 2 = 16 (left: 8 8 16)
2 * 8 = 16 (left: 8 14 16)
8 - 2 = 6 (left: 6 8 14)
14 - 8 = 6 (left: 2 6 8)
14 /  2 = 7 (left: 7 8 8)
14 - 2 = 12 (left: 8 8 12)
Input: 1 1 1 8
Possible next steps:

It's a one-shot prompt containing a single example of "Input" and "Possible next steps". The hope is that the LLM can perform in-context learning to generate a variety of "Possible next steps" for the new "Input" (the remaining numbers). (What's interesting is that the above prompt doesn't contain a task-specific instruction, i.e., it doesn't tell the LLM anything about the Game of 24 task.)

Let's see what thoughts the LLM generates.

responses = prelim.chat_completions(one_shot_propose_prompt, n=1)
thoughts = responses[0].split('\n')
thoughts

['1 + 1 = 2 (left: 1 2 8)',
 '1 * 1 = 1 (left: 1 1 8)',
 '8 / 1 = 8 (left: 1 1 8)',
 '8 - 1 = 7 (left: 1 1 7)',
 '8 * 1 = 8 (left: 1 1 8)',
 '1 * 8 = 8 (left: 1 1 8)',
 '8 + 1 = 9 (left: 1 1 9)']

Note: Recall that with the 'sample' strategy, we specified n_candidates - the numbers of thoughts to generate at each thought generation step. With the 'propose' strategy, we don't specify n_candidates; rather we leave it as a decision for the LLM.

For the next thought generation step, we need to work with the remaining numbers (e.g., "1 2 8"). Therefore, let's write a function that extracts the remaining numbers from a thought.

# Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/tasks/game24.py
def get_remaining_numbers(thought: str) -> str:
    return thought.split('left: ')[-1].split(')')[0]

Let's try it out on one of the above thoughts.

print(thoughts[0])
remaining_numbers = get_remaining_numbers(thoughts[0])
remaining_numbers

1 + 1 = 2 (left: 1 2 8)
'1 2 8'

Using the above remaining numbers, our one-shot propose prompt is now the following:

one_shot_propose_prompt = f'''Input: 2 8 8 14
Possible next steps:
2 + 8 = 10 (left: 8 10 14)
8 / 2 = 4 (left: 4 8 14)
14 + 2 = 16 (left: 8 8 16)
2 * 8 = 16 (left: 8 14 16)
8 - 2 = 6 (left: 6 8 14)
14 - 8 = 6 (left: 2 6 8)
14 /  2 = 7 (left: 7 8 8)
14 - 2 = 12 (left: 8 8 12)
Input: {remaining_numbers}
Possible next steps:
'''
print(one_shot_propose_prompt)

Input: 2 8 8 14
Possible next steps:
2 + 8 = 10 (left: 8 10 14)
8 / 2 = 4 (left: 4 8 14)
14 + 2 = 16 (left: 8 8 16)
2 * 8 = 16 (left: 8 14 16)
8 - 2 = 6 (left: 6 8 14)
14 - 8 = 6 (left: 2 6 8)
14 /  2 = 7 (left: 7 8 8)
14 - 2 = 12 (left: 8 8 12)
Input: 1 2 8
Possible next steps:

Let's see what thoughts the LLM generates.

responses = prelim.chat_completions(one_shot_propose_prompt, n=1)
thoughts = responses[0].split('\n')
thoughts

['1 + 2 = 3 (left: 3 8)',
 '8 - 1 = 7 (left: 2 7)',
 '8 - 2 = 6 (left: 1 6)',
 '2 * 1 = 2 (left: 2 8)',
 '8 / 2 = 4 (left: 1 4)',
 '8 / 1 = 8 (left: 2 8)']

Let's extract the remaining numbers from one of the above thoughts.

print(thoughts[0])
remaining_numbers = get_remaining_numbers(thoughts[0])
remaining_numbers

1 + 2 = 3 (left: 3 8)
'3 8'

Using the above remaining numbers, our one-shot propose prompt is now the following:

one_shot_propose_prompt = f'''Input: 2 8 8 14
Possible next steps:
2 + 8 = 10 (left: 8 10 14)
8 / 2 = 4 (left: 4 8 14)
14 + 2 = 16 (left: 8 8 16)
2 * 8 = 16 (left: 8 14 16)
8 - 2 = 6 (left: 6 8 14)
14 - 8 = 6 (left: 2 6 8)
14 /  2 = 7 (left: 7 8 8)
14 - 2 = 12 (left: 8 8 12)
Input: {remaining_numbers}
Possible next steps:
'''
print(one_shot_propose_prompt)

Input: 2 8 8 14
Possible next steps:
2 + 8 = 10 (left: 8 10 14)
8 / 2 = 4 (left: 4 8 14)
14 + 2 = 16 (left: 8 8 16)
2 * 8 = 16 (left: 8 14 16)
8 - 2 = 6 (left: 6 8 14)
14 - 8 = 6 (left: 2 6 8)
14 /  2 = 7 (left: 7 8 8)
14 - 2 = 12 (left: 8 8 12)
Input: 3 8
Possible next steps:

Let's see what thoughts the LLM generates.

responses = prelim.chat_completions(one_shot_propose_prompt, n=1)
thoughts = responses[0].split('\n')
thoughts

['3 + 8 = 11 (left: 11)',
 '8 - 3 = 5 (left: 5)',
 '3 * 8 = 24 (left: 24)',
 '8 / 3 = 2.67 (left: 2.67)']

We see that one of the thoughts is "3 * 8 = 24 (left: 24)". In other words, across thought generation steps 1, 2 and 3, at least one successful search path exists (that can reach 24).

Now that we have generated intermediate thoughts, we need to generate the output. (This can be considered thought generation step 4.)

For example, let's assume that the state of a particular node is the following:

thoughts = ['1 + 1 = 2 (left: 1 2 8)', '1 + 2 = 3 (left: 3 8)', '3 * 8 = 24 (left: 24)']
state =  '\n'.join(thoughts)
print(state)

1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)

The above state has all the correct intermediate thoughts to be able to generate the output "Answer: (1 + (1 + 1)) * 8 = 24". Since this output generation task is very different from the earlier task of generating intermediate thoughts, the prompt for it will also look very different. Here it is:

# Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/prompts/game24.py
five_shot_cot_prompt = f'''Use numbers and basic arithmetic operations (+ - * /) to obtain 24. Each step, you are only allowed to choose two of the remaining numbers to obtain a new number.
Input: 4 4 6 8
Steps:
4 + 8 = 12 (left: 4 6 12)
6 - 4 = 2 (left: 2 12)
2 * 12 = 24 (left: 24)
Answer: (6 - 4) * (4 + 8) = 24
Input: 2 9 10 12
Steps:
12 * 2 = 24 (left: 9 10 24)
10 - 9 = 1 (left: 1 24)
24 * 1 = 24 (left: 24)
Answer: (12 * 2) * (10 - 9) = 24
Input: 4 9 10 13
Steps:
13 - 10 = 3 (left: 3 4 9)
9 - 3 = 6 (left: 4 6)
4 * 6 = 24 (left: 24)
Answer: 4 * (9 - (13 - 10)) = 24
Input: 1 4 8 8
Steps:
8 / 4 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
Answer: (1 + 8 / 4) * 8 = 24
Input: 5 5 5 9
Steps:
5 + 5 = 10 (left: 5 9 10)
10 + 5 = 15 (left: 9 15)
15 + 9 = 24 (left: 24)
Answer: ((5 + 5) + 5) + 9 = 24
Input: {input_seq}
Steps:
{state}
'''
print(five_shot_cot_prompt)

Use numbers and basic arithmetic operations (+ - * /) to obtain 24. Each step, you are only allowed to choose two of the remaining numbers to obtain a new number.
Input: 4 4 6 8
Steps:
4 + 8 = 12 (left: 4 6 12)
6 - 4 = 2 (left: 2 12)
2 * 12 = 24 (left: 24)
Answer: (6 - 4) * (4 + 8) = 24
Input: 2 9 10 12
Steps:
12 * 2 = 24 (left: 9 10 24)
10 - 9 = 1 (left: 1 24)
24 * 1 = 24 (left: 24)
Answer: (12 * 2) * (10 - 9) = 24
Input: 4 9 10 13
Steps:
13 - 10 = 3 (left: 3 4 9)
9 - 3 = 6 (left: 4 6)
4 * 6 = 24 (left: 24)
Answer: 4 * (9 - (13 - 10)) = 24
Input: 1 4 8 8
Steps:
8 / 4 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
Answer: (1 + 8 / 4) * 8 = 24
Input: 5 5 5 9
Steps:
5 + 5 = 10 (left: 5 9 10)
10 + 5 = 15 (left: 9 15)
15 + 9 = 24 (left: 24)
Answer: ((5 + 5) + 5) + 9 = 24
Input: 1 1 1 8
Steps:
1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)

You may have noticed that it's exactly the earlier five-shot CoT prompt, except that we've also injected the intermediate steps. Will the LLM be able to generate the correct output this time?

responses = prelim.chat_completions(five_shot_cot_prompt, n=1)
thoughts = responses[0].split('\n')
thoughts

['Answer: (1 + 1 + 1) * 8 = 24']

Yes it is able to!

Now, the above workflow raises a minor concern. There are two seperate prompts (one for generating the intermediate thoughts, and one for generating the final answer). Moreover, we are using an external function get_remaining_numbers to extract the remaining numbers from intermediate thoughts. But we need to pass a single callable get_thought_gen_prompt to our TreeOfThoughts class (that returns the correct prompt). How do we do this?

The following callable does the job:

def get_thought_gen_prompt(input_seq: str, state: str) -> str:
    """Get thought generation prompt.

    Keyword arguments:
    input_seq -- the input sequence (comprising four numbers, e.g., '1 1 1 8')
    state -- concatenation of all the thoughts so far (separated by '\n')
    """

    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/tasks/game24.py
    def get_remaining_numbers(thought: str) -> str:
        return thought.split('left: ')[-1].split(')')[0]

    if state == '': # Root node; no thoughts have been generated yet.
        remaining_numbers = input_seq
    else:
        last_thought = state.strip().split('\n')[-1]
        remaining_numbers = get_remaining_numbers(last_thought)

    if remaining_numbers != '24': # Intermediate step.
        # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/prompts/game24.py
        prompt = f'''Input: 2 8 8 14
Possible next steps:
2 + 8 = 10 (left: 8 10 14)
8 / 2 = 4 (left: 4 8 14)
14 + 2 = 16 (left: 8 8 16)
2 * 8 = 16 (left: 8 14 16)
8 - 2 = 6 (left: 6 8 14)
14 - 8 = 6 (left: 2 6 8)
14 /  2 = 7 (left: 7 8 8)
14 - 2 = 12 (left: 8 8 12)
Input: {remaining_numbers}
Possible next steps:
'''
    else: # Last (output generation) step.
        # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/prompts/game24.py
        prompt = f'''Use numbers and basic arithmetic operations (+ - * /) to obtain 24. Each step, you are only allowed to choose two of the remaining numbers to obtain a new number.
Input: 4 4 6 8
Steps:
4 + 8 = 12 (left: 4 6 12)
6 - 4 = 2 (left: 2 12)
2 * 12 = 24 (left: 24)
Answer: (6 - 4) * (4 + 8) = 24
Input: 2 9 10 12
Steps:
12 * 2 = 24 (left: 9 10 24)
10 - 9 = 1 (left: 1 24)
24 * 1 = 24 (left: 24)
Answer: (12 * 2) * (10 - 9) = 24
Input: 4 9 10 13
Steps:
13 - 10 = 3 (left: 3 4 9)
9 - 3 = 6 (left: 4 6)
4 * 6 = 24 (left: 24)
Answer: 4 * (9 - (13 - 10)) = 24
Input: 1 4 8 8
Steps:
8 / 4 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
Answer: (1 + 8 / 4) * 8 = 24
Input: 5 5 5 9
Steps:
5 + 5 = 10 (left: 5 9 10)
10 + 5 = 15 (left: 9 15)
15 + 9 = 24 (left: 24)
Answer: ((5 + 5) + 5) + 9 = 24
Input: {input_seq}
Steps:
{state}
'''
    return prompt

We have been able to package everything into a single callable by adopting the following strategies:

get_remaining_numbers is now a nested function.
The last thought is being extracted from the state by splitting on the '\n' character. (This works because every thought appears on a new line.)
remaining_numbers is extracted from the last thought using get_remaining_numbers.
If remaining_numbers is not equal to '24', we return the prompt for generating intermediate thoughts. Otherwise, we return the prompt for generating the final answer.
Now, the BFS algorithm for Game of 24 looks very similar to the BFS algorithm for Creative Writing, with the following differences:

n_steps is equal to 4 (3 intermediate steps + 1 output generation step).
The authors have chosen to set n_evals to 3.
The authors have chosen to set breadth_limit to 5.


For the Game of 24 task, the state evaluation strategy adopted is 'value' (not 'vote'). From the paper:

Value each state independently ... a value prompt reasons about the state $s$ to generate a scalar value $v$ (e.g. 1-10) or a classification (e.g. sure/likely/impossible) that could be heuristically turned into a value... Such valuations do not need to be perfect, and only need to be approximately helpful for decision making.

In other words, instead of voting on the states, the 'value' strategy values each state independently.

It turns out that the state evaluator is the LLM itself. However, it (obviously) needs a different prompt than the thought generator. Let's take a look.

Recall that the LLM's thoughts have two distinct types: (i) intermediate thoughts, and (ii) final answer. Therefore, we'll need two separate prompts for state evaluation: (1) one prompt to evaluate states which contain only intermediate thoughts, and (2) another prompt to evaluate states which contain both intermediate thoughts and the final answer.

Let's start with the former. Suppose two intermediate thoughts have been generated so far.

thoughts = ['1 + 1 = 2 (left: 1 2 8)', '1 + 2 = 3 (left: 3 8)']
state =  '\n'.join(thoughts)
print(state)

1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)

We can extract the last thought from the state by splitting on the '\n' character.

last_thought = state.strip().split('\n')[-1]
last_thought

'1 + 2 = 3 (left: 3 8)'

And then extract the remaining numbers by using our familiar get_remaining_numbers function.

remaining_numbers = get_remaining_numbers(last_thought)
remaining_numbers

'3 8'

The following eight-shot value prompt is used to evaluate whether the remaining numbers can reach 24.

# Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/prompts/game24.py
eight_shot_value_prompt = f'''Evaluate if given numbers can reach 24 (sure/likely/impossible)
10 14
10 + 14 = 24
sure
11 12
11 + 12 = 23
12 - 11 = 1
11 * 12 = 132
11 / 12 = 0.91
impossible
4 4 10
4 + 4 + 10 = 8 + 10 = 18
4 * 10 - 4 = 40 - 4 = 36
(10 - 4) * 4 = 6 * 4 = 24
sure
4 9 11
9 + 11 + 4 = 20 + 4 = 24
sure
5 7 8
5 + 7 + 8 = 12 + 8 = 20
(8 - 5) * 7 = 3 * 7 = 21
I cannot obtain 24 now, but numbers are within a reasonable range
likely
5 6 6
5 + 6 + 6 = 17
(6 - 5) * 6 = 1 * 6 = 6
I cannot obtain 24 now, but numbers are within a reasonable range
likely
10 10 11
10 + 10 + 11 = 31
(11 - 10) * 10 = 10
10 10 11 are all too big
impossible
1 3 3
1 * 3 * 3 = 9
(1 + 3) * 3 = 12
1 3 3 are all too small
impossible
{remaining_numbers}
'''
print(eight_shot_value_prompt)

Evaluate if given numbers can reach 24 (sure/likely/impossible)
10 14
10 + 14 = 24
sure
11 12
11 + 12 = 23
12 - 11 = 1
11 * 12 = 132
11 / 12 = 0.91
impossible
4 4 10
4 + 4 + 10 = 8 + 10 = 18
4 * 10 - 4 = 40 - 4 = 36
(10 - 4) * 4 = 6 * 4 = 24
sure
4 9 11
9 + 11 + 4 = 20 + 4 = 24
sure
5 7 8
5 + 7 + 8 = 12 + 8 = 20
(8 - 5) * 7 = 3 * 7 = 21
I cannot obtain 24 now, but numbers are within a reasonable range
likely
5 6 6
5 + 6 + 6 = 17
(6 - 5) * 6 = 1 * 6 = 6
I cannot obtain 24 now, but numbers are within a reasonable range
likely
10 10 11
10 + 10 + 11 = 31
(11 - 10) * 10 = 10
10 10 11 are all too big
impossible
1 3 3
1 * 3 * 3 = 9
(1 + 3) * 3 = 12
1 3 3 are all too small
impossible
3 8

Let's see the LLM's response.

responses = prelim.chat_completions(eight_shot_value_prompt, n=1)
print(responses[0])

3 + 8 = 11
3 * 8 = 24
sure

Now, let's consider a state which contains the final answer.

thoughts = ['1 + 1 = 2 (left: 1 2 8)', '1 + 2 = 3 (left: 3 8)', '3 * 8 = 24 (left: 24)', 'Answer: ((1 + 1) + 1) * 8 = 24']
state =  '\n'.join(thoughts)
print(state)

1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
Answer: ((1 + 1) + 1) * 8 = 24

First, the last line is extracted.

last_line = state.strip().split('\n')[-1]
last_line

'Answer: ((1 + 1) + 1) * 8 = 24'

If the string 'left': is NOT a substring of last_line, then we know that we have the final answer. In that case, we extract the equation as follows:

if 'left: ' not in last_line:
    ans = last_line.lower().replace('answer: ', '')
ans

'((1 + 1) + 1) * 8 = 24'

The following six-shot value prompt is used to evaluate whether the extracted equation is correct:

# Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/prompts/game24.py
six_shot_value_last_step_prompt = f'''Use numbers and basic arithmetic operations (+ - * /) to obtain 24. Given an input and an answer, give a judgement (sure/impossible) if the answer is correct, i.e. it uses each input exactly once and no other numbers, and reach 24.
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) = 24
Judge:
sure
Input: 2 9 10 12
Answer: 2 * 12 * (10 - 9) = 24
Judge:
sure
Input: 4 9 10 13
Answer: (13 - 9) * (10 - 4) = 24
Judge:
sure
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) + 1 = 25
Judge:
impossible
Input: 2 9 10 12
Answer: 2 * (12 - 10) = 24
Judge:
impossible
Input: 4 9 10 13
Answer: (13 - 4) * (10 - 9) = 24
Judge:
impossible
Input: {input_seq}
Answer: {ans}
Judge:'''
print(six_shot_value_last_step_prompt)

Use numbers and basic arithmetic operations (+ - * /) to obtain 24. Given an input and an answer, give a judgement (sure/impossible) if the answer is correct, i.e. it uses each input exactly once and no other numbers, and reach 24.
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) = 24
Judge:
sure
Input: 2 9 10 12
Answer: 2 * 12 * (10 - 9) = 24
Judge:
sure
Input: 4 9 10 13
Answer: (13 - 9) * (10 - 4) = 24
Judge:
sure
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) + 1 = 25
Judge:
impossible
Input: 2 9 10 12
Answer: 2 * (12 - 10) = 24
Judge:
impossible
Input: 4 9 10 13
Answer: (13 - 4) * (10 - 9) = 24
Judge:
impossible
Input: 1 1 1 8
Answer: ((1 + 1) + 1) * 8 = 24
Judge:

That's some sophisticated prompting!

Let's see the LLM's response.

responses = prelim.chat_completions(six_shot_value_last_step_prompt, n=1)
print(responses[0])

sure

Once again, the above workflow raises a minor concern. There are two seperate prompts. But we need to pass a single callable get_state_eval_prompt to our TreeOfThoughts class (that returns the correct prompt). How do we do this?

The following callable does the job:

def get_state_eval_prompt(input_seq: str, state: str) -> str:
    """Get state evaluation prompt.

    Keyword arguments:
    input_seq -- the input sequence (comprising four numbers, e.g., '1 1 1 8')
    state -- concatenation of all the thoughts so far (separated by '\n')
    """

    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/tasks/game24.py
    def get_remaining_numbers(thought: str) -> str:
        return thought.split('left: ')[-1].split(')')[0]

    last_line = state.strip().split('\n')[-1]

    if 'left: ' not in last_line: # Last (output generation) step.
        ans = last_line.lower().replace('answer: ', '')
        # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/prompts/game24.py
        prompt = f'''Use numbers and basic arithmetic operations (+ - * /) to obtain 24. Given an input and an answer, give a judgement (sure/impossible) if the answer is correct, i.e. it uses each input exactly once and no other numbers, and reach 24.
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) = 24
Judge:
sure
Input: 2 9 10 12
Answer: 2 * 12 * (10 - 9) = 24
Judge:
sure
Input: 4 9 10 13
Answer: (13 - 9) * (10 - 4) = 24
Judge:
sure
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) + 1 = 25
Judge:
impossible
Input: 2 9 10 12
Answer: 2 * (12 - 10) = 24
Judge:
impossible
Input: 4 9 10 13
Answer: (13 - 4) * (10 - 9) = 24
Judge:
impossible
Input: {input_seq}
Answer: {ans}
Judge:'''
    else: # Intermediate step.
        remaining_numbers = get_remaining_numbers(last_line)
        # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/prompts/game24.py
        prompt = f'''Evaluate if given numbers can reach 24 (sure/likely/impossible)
10 14
10 + 14 = 24
sure
11 12
11 + 12 = 23
12 - 11 = 1
11 * 12 = 132
11 / 12 = 0.91
impossible
4 4 10
4 + 4 + 10 = 8 + 10 = 18
4 * 10 - 4 = 40 - 4 = 36
(10 - 4) * 4 = 6 * 4 = 24
sure
4 9 11
9 + 11 + 4 = 20 + 4 = 24
sure
5 7 8
5 + 7 + 8 = 12 + 8 = 20
(8 - 5) * 7 = 3 * 7 = 21
I cannot obtain 24 now, but numbers are within a reasonable range
likely
5 6 6
5 + 6 + 6 = 17
(6 - 5) * 6 = 1 * 6 = 6
I cannot obtain 24 now, but numbers are within a reasonable range
likely
10 10 11
10 + 10 + 11 = 31
(11 - 10) * 10 = 10
10 10 11 are all too big
impossible
1 3 3
1 * 3 * 3 = 9
(1 + 3) * 3 = 12
1 3 3 are all too small
impossible
{remaining_numbers}
'''
    return prompt

The final callable we need is the heuristic calculator. The job of the heuristic calculator is to collate multiple evaluations of each state into a single heuristic score. (Each evaluation is 'sure'/'likely'/'impossible'.) Let's take a look.

Suppose we're at a node with the following state:

# Say:
thoughts = ['1 + 1 = 2 (left: 1 2 8)', '1 + 2 = 3 (left: 3 8)']
state =  '\n'.join(thoughts)
print(state)

1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)

As noted before, the authors have chosen to set n_evals to 3.

n_evals = 3

Let's get the 3 state evaluations.

prompt = get_state_eval_prompt(input_seq, state)
state_evals = prelim.chat_completions(prompt, n=n_evals)
for eval in state_evals:
    print(eval)
    print("---")

3 + 8 = 11
3 * 8 = 24
sure
---
3 + 8 = 11
8 - 3 = 5
3 * 8 = 24
sure
---
3 + 8 = 11
3 * 8 = 24
sure
---

The following callable collates the three evaluations into a single heuristic score.

# Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/tasks/game24.py
def heuristic_calculator(state: str, state_evals: List[str]) -> float:
    if len(state.strip().split('\n')) == 4 and 'answer' not in state.lower(): # Such a state is undesirable.
        return 0
    value_names = [_.split('\n')[-1].lower() for _ in state_evals] # A list containing 'impossible' / 'likely' / 'sure' values.
    value_map = {'impossible': 0.001, 'likely': 1, 'sure': 20} # Ad hoc.
    value = sum(value * value_names.count(name) for name, value in value_map.items())
    return value

A brief explanation:

If a particular state contains 4 lines, and doesn't contain the final answer, then a value of 0 is assigned to the state (since such a state is undesirable).
Otherwise, the last lines are extracted from the 3 state evaluations. This gives a list containing 'impossible'/'likely'/'sure' values.
The weighted sum of the above values is returned, where the (ad hoc) weights are {'impossible': 0.001, 'likely': 1, 'sure': 20}.
Let's try it out on the above state evaluations.

heuristic_calculator(state, state_evals)

60.0

This is the highest possible value, since all the 3 state evaluations were 'sure'.

Now, let's try a state which doesn't have any hope of reaching 24.

# Say:
thoughts = ['1 + 1 = 2 (left: 1 2 8)', '8 - 1 = 7 (left: 2 7)']
state =  '\n'.join(thoughts)
print(state)

1 + 1 = 2 (left: 1 2 8)
8 - 1 = 7 (left: 2 7)

prompt = get_state_eval_prompt(input_seq, state)
state_evals = prelim.chat_completions(prompt, n=n_evals)
for eval in state_evals:
    print(eval)
    print("---")

2 + 7 = 9
2 * 7 = 14
2 / 7 = 0.28
7 - 2 = 5
impossible
---
2 + 7 = 9
2 * 7 = 14
2 / 7 = 0.28
7 - 2 = 5
impossible
---
2 + 7 = 9
2 * 7 = 14
7 - 2 = 5
7 / 2 = 3.5
impossible
---

heuristic_calculator(state, state_evals)

0.003

A very low value is assigned. Excellent.

Next, let's consider a state which contains a correct final answer.

# Say:
thoughts = ['1 + 1 = 2 (left: 1 2 8)', '1 + 2 = 3 (left: 3 8)', '3 * 8 = 24 (left: 24)', 'Answer: ((1 + 1) + 1) * 8 = 24']
state =  '\n'.join(thoughts)
print(state)

1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
Answer: ((1 + 1) + 1) * 8 = 24

prompt = get_state_eval_prompt(input_seq, state)
state_evals = prelim.chat_completions(prompt, n=n_evals)
for eval in state_evals:
    print(eval)
    print("---")

sure
---
sure
---
sure
---

heuristic_calculator(state, state_evals)

60.0

Perfect.

Finally, let's consider a state which contains an incorrect final answer.

# Say:
thoughts = ['1 + 1 = 2 (left: 1 2 8)', '1 + 2 = 3 (left: 3 8)', '3 * 8 = 24 (left: 24)', 'Answer: ((1 + 1) + 1) - 8 = 24']
state =  '\n'.join(thoughts)
print(state)

1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
Answer: ((1 + 1) + 1) - 8 = 24

prompt = get_state_eval_prompt(input_seq, state)
state_evals = prelim.chat_completions(prompt, n=n_evals)
for eval in state_evals:
    print(eval)
    print("---")

impossible
---
impossible
---
impossible
---

heuristic_calculator(state, state_evals)

0.003

Superb.

Hopefully, you now have a good intuition about the heuristic calculator.

Finally, we're ready to write the TreeOfThoughts class for the Game of 24 task.

Note: In addition to the bfs method, we've also added in the dfs (Depth-First Search) method - which is another search algorithm from the ToT paper. Don't worry about it for now. The dfs method will be explained in detail below.

class TreeOfThoughts:
    def __init__(
            self,
            client: Union[OpenAI, InferenceClient],
            model: str,
            input_seq: str,
            get_thought_gen_prompt: Callable,
            get_state_eval_prompt: Callable,
            heuristic_calculator: Callable,
            max_per_state: Optional[int] = None
    ):
        self.client = client
        self.model = model # e.g., "gpt-4" if using `OpenAI` and "meta-llama/Meta-Llama-3.1-8B-Instruct" if using `InferenceClient`.
        self.input_seq = input_seq
        self.root = TreeNode(state='', thought='')
        self.n_steps = 4 # 3 intermediate steps + 1 output generation step.
        self.thought_gen_strategy = 'propose'
        self.get_thought_gen_prompt = get_thought_gen_prompt
        self.state_eval_strategy = 'value'
        self.get_state_eval_prompt = get_state_eval_prompt
        self.n_evals = 3 # The number of times to sample values for each state.
        self.heuristic_calculator = heuristic_calculator
        self.breadth_limit = 5 # Relevant only for the BFS search algorithm.
        self.heuristic_threshold = 3.0 # Relevant only for the DFS search algorithm; will be explained below.
        self.max_per_state = max_per_state # Relevant only for the DFS search algorithm; will be explained below.

    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/models.py
    def chat_completions(
            self,
            prompt: str,
            temperature: float = 0.7,
            max_tokens: int = 1000,
            n: int = 1,
            stop: Optional[List[str]] = None,
            **kwargs
    ) -> List[str]:
        outputs = []
        messages = [{'role': "user", 'content': prompt}]
        if isinstance(self.client, OpenAI):
            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=temperature,
                max_tokens=max_tokens,
                n=n, # The `n` responses are i.i.d.
                stop=stop,
                **kwargs
            )
            outputs.extend([choice.message.content for choice in response.choices])
        else: # `self.client` is an instance of `InferenceClient`.
            # The Hugging Face API doesn't support the `n` argument. Hence, we need to use a loop to generate `n` i.i.d. responses.
            for _ in range(n):
                response = self.client.chat.completions.create(
                    messages=messages,
                    model=self.model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    stop=stop,
                    **kwargs
                )
                outputs.append(response.choices[0].message.content)
        return outputs

    def thought_generator(self, state: str) -> List[str]:
        if self.thought_gen_strategy == 'sample':
            pass
        else: # `self.thought_gen_strategy` is equal to 'propose'.
            prompt = self.get_thought_gen_prompt(self.input_seq, state)
            responses = self.chat_completions(prompt, n=1)
            thoughts = responses[0].split('\n')
            return thoughts

    def state_evaluator(self, state: str) -> float:
        if self.state_eval_strategy == 'vote':
            pass
        else: # `self.state_eval_strategy` is equal to 'value'.
            prompt = self.get_state_eval_prompt(self.input_seq, state)
            state_evals = self.chat_completions(prompt, n=self.n_evals)
            value = self.heuristic_calculator(state, state_evals)
            return value

    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/methods/bfs.py
    def bfs(self, verbose: bool = True) -> str:
        queue = deque()
        queue.append(self.root)

        for step in range(1, self.n_steps + 1):
            if verbose:
                print(f"Step {step} (corresponding to level {step} of the tree):-\n---")
            for i in range(len(queue)):
                node = queue.popleft()
                if verbose:
                    print(f"Node {i + 1} in level {step}:-")
                    if node.state != "":
                        print(f"State of current node:-\n{node.state}\n---")
                    else:
                        print("State of current node:-\n<EMPTY STRING> (root node; no thoughts generated yet)\n---")

                thoughts = self.thought_generator(state=node.state)
                if node.state == '':
                    updated_states = thoughts
                else:
                    updated_states = [node.state + '\n' + thought for thought in thoughts]
                for j in range(len(thoughts)):
                    if verbose:
                        print(f"Thought candidate {j + 1}:-\n{thoughts[j]}\n---")
                    child = TreeNode(state=updated_states[j], thought=thoughts[j])
                    node.children.append(child)
                    queue.append(child)
                if verbose:
                    print("Each of the above thought candidates has been added as a child of the current node.\n---")

            if verbose:
                print("Using the state evaluator to obtain values...\n---")
            for i in range(len(queue)):
                queue[i].value = self.state_evaluator(state=queue[i].state)
                if verbose:
                    print(f"Element {i + 1} in queue:-\n")
                    print(f"Value: {queue[i].value}\n---")

            if verbose:
                print("Initiating pruning (using the values obtained from the state evaluator).")
                print(f"Number of elements in queue: {len(queue)}")
            sorted_nodes = sorted(queue, key=lambda node: node.value, reverse=True)
            if step == self.n_steps:
                if verbose:
                    print("Since this is the last step, setting the breadth limit to 1.")
                    print("In other words, retaining only the highest value element (in this last step).\n---")
                top_b_nodes = sorted_nodes[:1]
            else:
                if verbose:
                    print(f"Since this isn't the last step, leaving the breadth limit {self.breadth_limit} unchanged.\n---")
                top_b_nodes = sorted_nodes[:self.breadth_limit]
            top_b_states = [node.state for node in top_b_nodes]
            for i in range(len(queue)):
                node = queue.popleft()
                if verbose:
                    print(f"Element {i + 1} in queue:-\n")
                if node.state in top_b_states:
                    if verbose:
                        print(f"Retaining this element as it's in the top {len(top_b_states)} elements.\n---")
                    queue.append(node)
                else:
                    if verbose:
                        print(f"Dropping this element as it's not in the top {len(top_b_states)} elements.\n---")

            if verbose:
                print("~~~")

        # Return the thought of the highest value node (from the last step):
        node = queue.popleft()
        return node.thought

    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/scripts/crosswords/search_crosswords-dfs.ipynb
    def dfs(self, verbose: bool = True) -> str:
        dfs_output = None

        def dfs_func(node: TreeNode, step: int) -> bool:
            nonlocal dfs_output

            if step > self.n_steps: # Base case: successful search.
                dfs_output = node.state # Record the last (output generation) step's output in the nonlocal variable `dfs_output`.
                return True

            if verbose:
                print(f"Step: {step}\n---")
                if node.state != "":
                    print(f"State of current node:-\n{node.state}\n---")
                else:
                    print("State of current node:-\n<EMPTY STRING> (root node; no thoughts generated yet)\n---")

            thoughts = self.thought_generator(state=node.state)
            if len(thoughts) == 0:
                if verbose:
                    print("No thoughts were generated. It's a dead end. Backtracking to the parent node.\n~~~")
                return False
            if node.state == '':
                updated_states = thoughts
            else:
                updated_states = [node.state + '\n' + thought for thought in thoughts]
            for j in range(len(thoughts)):
                if verbose:
                    print(f"Thought candidate {j + 1}:-\n{thoughts[j]}\n---")
                child = TreeNode(state=updated_states[j], thought=thoughts[j])
                node.children.append(child)
            if verbose:
                print("Each of the above thought candidates has been added as a child of the current node.\n---")

            cnt_per_state = 0
            for child in node.children:
                if verbose:
                    print("Reminder:-")
                    if node.state != "":
                        print(f"State of current node:-\n{node.state}\n---")
                    else:
                        print("State of current node:-\n<EMPTY STRING> (root node; no thoughts generated yet)\n---")
                    print(f"Currently traversing child number: {cnt_per_state + 1}\n")
                    print(f"State of current child:-\n{child.state}\n")
                    print("Using the state evaluator to obtain value...\n")
                child.value = self.state_evaluator(state=child.state)
                if verbose:
                    print(f"Value of current child: {child.value}\n---")
                if child.value >= self.heuristic_threshold:
                # Note: If this `if` condition isn't met, the child node is pruned, i.e., a subtree of the child isn't grown.
                    if verbose:
                        print("Value exceeds heuristic threshold. Searching subtree.\n---\n~~~")
                    end_search = dfs_func(child, step + 1)
                    if end_search:
                        if verbose:
                            print(f"Searching the subtree was successful! Backtracking all the way up.\n~~~")
                        return True
                    else:
                        if verbose:
                            print(f"Back at step {step}. Searching the subtree was unsuccessful! Trying the next child.\n---")
                cnt_per_state += 1
                if cnt_per_state >= self.max_per_state:
                    if verbose:
                        print(f"{self.max_per_state} children already searched for this node. Breaking the loop.\n---")
                    break
            if verbose:
                print(f"None of the child nodes led to success. Seems like a dead end. Backtracking to the parent node.\n~~~")
            return False

        dfs_func(node=self.root, step=1)
        return dfs_output

    def generate_html_tree(self, node: TreeNode) -> str:
        if node is None:
            return ""
        else:
            html = f"""<div class='node'>
<p>State:<br>{node.state}</p>
<hr>
<p>Thought:<br>{node.thought}</p>
<hr>
<p>Value:<br>{node.value}</p>"""
            for child in node.children:
                html += f"""<div class='child'>{self.generate_html_tree(child)}</div>"""
            html += """</div>"""
            return html

    def render_html_tree(self):
        html_tree = self.generate_html_tree(self.root)
        wrapped_html = f"""<!DOCTYPE html>
<html>
<head>
    <style>
        .node {{
            display: inline-block;
            border: 1px solid blue;
            padding: 10px;
            margin: 5px;
            text-align: center;
        }}
        .child {{
            display: flex;
        }}
    </style>
</head>
<body>
    {html_tree}
</body>
</html>"""
        display(HTML(wrapped_html))

Let's instantiate our class, and run the BFS algorithm.

tot = TreeOfThoughts(client, "gpt-4", input_seq, get_thought_gen_prompt, get_state_eval_prompt, heuristic_calculator)
output = tot.bfs(verbose=True)
print(output)

Step 1 (corresponding to level 1 of the tree):-
---
Node 1 in level 1:-
State of current node:-
<EMPTY STRING> (root node; no thoughts generated yet)
---
Thought candidate 1:-
1 + 1 = 2 (left: 1 2 8)
---
Thought candidate 2:-
1 * 1 = 1 (left: 1 1 8)
---
Thought candidate 3:-
8 - 1 = 7 (left: 1 1 7)
---
Thought candidate 4:-
8 / 1 = 8 (left: 1 1 8)
---
Thought candidate 5:-
1 + 1 + 1 = 3 (left: 3 8)
---
Thought candidate 6:-
8 - 1 - 1 = 6 (left: 1 6)
---
Thought candidate 7:-
8 / 1 / 1 = 8 (left: 1 8)
---
Each of the above thought candidates has been added as a child of the current node.
---
Using the state evaluator to obtain values...
---
Element 1 in queue:-

Value: 21.001
---
Element 2 in queue:-

Value: 0.003
---
Element 3 in queue:-

Value: 0.003
---
Element 4 in queue:-

Value: 0.003
---
Element 5 in queue:-

Value: 60.0
---
Element 6 in queue:-

Value: 0.003
---
Element 7 in queue:-

Value: 0.003
---
Initiating pruning (using the values obtained from the state evaluator).
Number of elements in queue: 7
Since this isn't the last step, leaving the breadth limit 5 unchanged.
---
Element 1 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 2 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 3 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 4 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 5 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 6 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 7 in queue:-

Dropping this element as it's not in the top 5 elements.
---
~~~
Step 2 (corresponding to level 2 of the tree):-
---
Node 1 in level 2:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
---
Thought candidate 1:-
1 + 2 = 3 (left: 3 8)
---
Thought candidate 2:-
2 * 1 = 2 (left: 2 8)
---
Thought candidate 3:-
8 - 1 = 7 (left: 2 7)
---
Thought candidate 4:-
8 - 2 = 6 (left: 1 6)
---
Thought candidate 5:-
8 / 1 = 8 (left: 2 8)
---
Thought candidate 6:-
2 * 8 = 16 (left: 1 16)
---
Thought candidate 7:-
8 / 2 = 4 (left: 1 4)
---
Each of the above thought candidates has been added as a child of the current node.
---
Node 2 in level 2:-
State of current node:-
1 * 1 = 1 (left: 1 1 8)
---
Thought candidate 1:-
1 + 1 = 2 (left: 2 8)
---
Thought candidate 2:-
1 * 1 = 1 (left: 1 8)
---
Thought candidate 3:-
8 - 1 = 7 (left: 1 7)
---
Thought candidate 4:-
8 / 1 = 8 (left: 1 8)
---
Each of the above thought candidates has been added as a child of the current node.
---
Node 3 in level 2:-
State of current node:-
8 - 1 = 7 (left: 1 1 7)
---
Thought candidate 1:-
1 + 1 = 2 (left: 2 7)
---
Thought candidate 2:-
7 - 1 = 6 (left: 1 6)
---
Thought candidate 3:-
7 / 1 = 7 (left: 1 7)
---
Thought candidate 4:-
1 * 1 = 1 (left: 1 7)
---
Each of the above thought candidates has been added as a child of the current node.
---
Node 4 in level 2:-
State of current node:-
8 / 1 = 8 (left: 1 1 8)
---
Thought candidate 1:-
1 + 1 = 2 (left: 2 8)
---
Thought candidate 2:-
1 * 1 = 1 (left: 1 8)
---
Thought candidate 3:-
8 - 1 = 7 (left: 1 7)
---
Thought candidate 4:-
8 / 1 = 8 (left: 1 8)
---
Each of the above thought candidates has been added as a child of the current node.
---
Node 5 in level 2:-
State of current node:-
1 + 1 + 1 = 3 (left: 3 8)
---
Thought candidate 1:-
3 + 8 = 11 (left: 11)
---
Thought candidate 2:-
8 / 3 = 2.67 (left: 2.67)
---
Thought candidate 3:-
8 - 3 = 5 (left: 5)
---
Thought candidate 4:-
3 * 8 = 24 (left: 24)
---
Each of the above thought candidates has been added as a child of the current node.
---
Using the state evaluator to obtain values...
---
Element 1 in queue:-

Value: 60.0
---
Element 2 in queue:-

Value: 0.003
---
Element 3 in queue:-

Value: 0.003
---
Element 4 in queue:-

Value: 0.003
---
Element 5 in queue:-

Value: 0.003
---
Element 6 in queue:-

Value: 0.003
---
Element 7 in queue:-

Value: 0.003
---
Element 8 in queue:-

Value: 0.003
---
Element 9 in queue:-

Value: 0.003
---
Element 10 in queue:-

Value: 0.003
---
Element 11 in queue:-

Value: 0.003
---
Element 12 in queue:-

Value: 0.003
---
Element 13 in queue:-

Value: 0.003
---
Element 14 in queue:-

Value: 0.003
---
Element 15 in queue:-

Value: 0.003
---
Element 16 in queue:-

Value: 0.003
---
Element 17 in queue:-

Value: 0.003
---
Element 18 in queue:-

Value: 0.003
---
Element 19 in queue:-

Value: 0.003
---
Element 20 in queue:-

Value: 0.003
---
Element 21 in queue:-

Value: 0.002
---
Element 22 in queue:-

Value: 0.003
---
Element 23 in queue:-

Value: 60.0
---
Initiating pruning (using the values obtained from the state evaluator).
Number of elements in queue: 23
Since this isn't the last step, leaving the breadth limit 5 unchanged.
---
Element 1 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 2 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 3 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 4 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 5 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 6 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 7 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 8 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 9 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 10 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 11 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 12 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 13 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 14 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 15 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 16 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 17 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 18 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 19 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 20 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 21 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 22 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 23 in queue:-

Retaining this element as it's in the top 5 elements.
---
~~~
Step 3 (corresponding to level 3 of the tree):-
---
Node 1 in level 3:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
---
Thought candidate 1:-
3 + 8 = 11 (left: 11)
---
Thought candidate 2:-
8 - 3 = 5 (left: 5)
---
Thought candidate 3:-
3 * 8 = 24 (left: 24)
---
Thought candidate 4:-
8 / 3 = 2.67 (left: 2.67)
---
Each of the above thought candidates has been added as a child of the current node.
---
Node 2 in level 3:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
2 * 1 = 2 (left: 2 8)
---
Thought candidate 1:-
2 + 8 = 10 (left: 10)
---
Thought candidate 2:-
2 * 8 = 16 (left: 16)
---
Thought candidate 3:-
8 - 2 = 6 (left: 6)
---
Thought candidate 4:-
8 / 2 = 4 (left: 4)
---
Each of the above thought candidates has been added as a child of the current node.
---
Node 3 in level 3:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
8 - 1 = 7 (left: 2 7)
---
Thought candidate 1:-
2 + 7 = 9 (left: 9)
---
Thought candidate 2:-
7 - 2 = 5 (left: 5)
---
Thought candidate 3:-
2 * 7 = 14 (left: 14)
---
Thought candidate 4:-
7 / 2 = 3.5 (left: 3.5)
---
Each of the above thought candidates has been added as a child of the current node.
---
Node 4 in level 3:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
8 - 2 = 6 (left: 1 6)
---
Thought candidate 1:-
1 + 6 = 7 (left: 7)
---
Thought candidate 2:-
6 - 1 = 5 (left: 5)
---
Thought candidate 3:-
1 * 6 = 6 (left: 6)
---
Thought candidate 4:-
6 / 1 = 6 (left: 6)
---
Each of the above thought candidates has been added as a child of the current node.
---
Node 5 in level 3:-
State of current node:-
1 + 1 + 1 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
---
Thought candidate 1:-
Answer: (1 + 1 + 1) * 8 = 24
---
Each of the above thought candidates has been added as a child of the current node.
---
Using the state evaluator to obtain values...
---
Element 1 in queue:-

Value: 0.003
---
Element 2 in queue:-

Value: 0.003
---
Element 3 in queue:-

Value: 60.0
---
Element 4 in queue:-

Value: 0.003
---
Element 5 in queue:-

Value: 0.003
---
Element 6 in queue:-

Value: 0.003
---
Element 7 in queue:-

Value: 20.002
---
Element 8 in queue:-

Value: 0.001
---
Element 9 in queue:-

Value: 0.003
---
Element 10 in queue:-

Value: 0.003
---
Element 11 in queue:-

Value: 0.003
---
Element 12 in queue:-

Value: 0.003
---
Element 13 in queue:-

Value: 0.001
---
Element 14 in queue:-

Value: 0.003
---
Element 15 in queue:-

Value: 0.003
---
Element 16 in queue:-

Value: 40.001
---
Element 17 in queue:-

Value: 60.0
---
Initiating pruning (using the values obtained from the state evaluator).
Number of elements in queue: 17
Since this isn't the last step, leaving the breadth limit 5 unchanged.
---
Element 1 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 2 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 3 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 4 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 5 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 6 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 7 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 8 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 9 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 10 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 11 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 12 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 13 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 14 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 15 in queue:-

Dropping this element as it's not in the top 5 elements.
---
Element 16 in queue:-

Retaining this element as it's in the top 5 elements.
---
Element 17 in queue:-

Retaining this element as it's in the top 5 elements.
---
~~~
Step 4 (corresponding to level 4 of the tree):-
---
Node 1 in level 4:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 + 8 = 11 (left: 11)
---
Thought candidate 1:-
There is no possible operation as there is only one number.
---
Each of the above thought candidates has been added as a child of the current node.
---
Node 2 in level 4:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
---
Thought candidate 1:-
Answer: ((1 + 1) + 1) * 8 = 24
---
Each of the above thought candidates has been added as a child of the current node.
---
Node 3 in level 4:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
2 * 1 = 2 (left: 2 8)
8 - 2 = 6 (left: 6)
---
Thought candidate 1:-
8 + 6 = 14 (left: 8 14 14)
---
Thought candidate 2:-
8 - 6 = 2 (left: 2 8 14)
---
Thought candidate 3:-
14 - 6 = 8 (left: 8 8 8)
---
Thought candidate 4:-
14 + 6 = 20 (left: 8 8 20)
---
Thought candidate 5:-
2 * 6 = 12 (left: 8 12 14)
---
Thought candidate 6:-
14 / 6 = ~2.33 (left: ~2.33 8 8) (not a valid step, as we are only considering integer solutions)
---
Thought candidate 7:-
8 / 6 = ~1.33 (left: ~1.33 8 14) (not a valid step, as we are only considering integer solutions)
---
Thought candidate 8:-
6 * 8 = 48 (left: 8 14 48)
---
Each of the above thought candidates has been added as a child of the current node.
---
Node 4 in level 4:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
8 - 2 = 6 (left: 1 6)
6 / 1 = 6 (left: 6)
---
Thought candidate 1:-
6 + 10 = 16 (left: 8 14 16)
---
Thought candidate 2:-
6 + 4 = 10 (left: 8 10 14)
---
Thought candidate 3:-
16 - 6 = 10 (left: 8 10 14)
---
Thought candidate 4:-
16 / 6 = 2.67 (left: 2.67 8 14)
---
Thought candidate 5:-
6 - 2 = 4 (left: 4 8 14)
---
Thought candidate 6:-
6 / 2 = 3 (left: 3 8 14)
---
Thought candidate 7:-
7 + 6 = 13 (left: 8 8 13)
---
Thought candidate 8:-
12 - 6 = 6 (left: 6 8 8)
---
Each of the above thought candidates has been added as a child of the current node.
---
Node 5 in level 4:-
State of current node:-
1 + 1 + 1 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
Answer: (1 + 1 + 1) * 8 = 24
---
Thought candidate 1:-
1 + 1 = 2 (left: 1 2)
---
Thought candidate 2:-
1 - 1 = 0 (left: 0 1)
---
Thought candidate 3:-
1 * 1 = 1 (left: 1 1)
---
Thought candidate 4:-
This input is incomplete, it is not possible to define the next steps without knowing the remaining part of the expression.
---
Each of the above thought candidates has been added as a child of the current node.
---
Using the state evaluator to obtain values...
---
Element 1 in queue:-

Value: 0
---
Element 2 in queue:-

Value: 60.0
---
Element 3 in queue:-

Value: 0
---
Element 4 in queue:-

Value: 0
---
Element 5 in queue:-

Value: 0
---
Element 6 in queue:-

Value: 0
---
Element 7 in queue:-

Value: 0
---
Element 8 in queue:-

Value: 0
---
Element 9 in queue:-

Value: 0
---
Element 10 in queue:-

Value: 0
---
Element 11 in queue:-

Value: 0
---
Element 12 in queue:-

Value: 0
---
Element 13 in queue:-

Value: 0
---
Element 14 in queue:-

Value: 0
---
Element 15 in queue:-

Value: 0
---
Element 16 in queue:-

Value: 0
---
Element 17 in queue:-

Value: 0
---
Element 18 in queue:-

Value: 0
---
Element 19 in queue:-

Value: 0.003
---
Element 20 in queue:-

Value: 0.003
---
Element 21 in queue:-

Value: 0.003
---
Element 22 in queue:-

Value: 0.003
---
Initiating pruning (using the values obtained from the state evaluator).
Number of elements in queue: 22
Since this is the last step, setting the breadth limit to 1.
In other words, retaining only the highest value element (in this last step).
---
Element 1 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 2 in queue:-

Retaining this element as it's in the top 1 elements.
---
Element 3 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 4 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 5 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 6 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 7 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 8 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 9 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 10 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 11 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 12 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 13 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 14 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 15 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 16 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 17 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 18 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 19 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 20 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 21 in queue:-

Dropping this element as it's not in the top 1 elements.
---
Element 22 in queue:-

Dropping this element as it's not in the top 1 elements.
---
~~~
Answer: ((1 + 1) + 1) * 8 = 24

Time to visualize the tree.

tot.render_html_tree()

To circumvent the HTML rendering issue, I've saved the tree as an HTML file, which you can view here. Below is a screenshot of the same:



Ok. It's time to take a look at the dfs method.

Note: The ToT paper didn't demonstrate DFS on the Creative Writing task. (It only demonstrated BFS.) But we shall demonstrate it nonetheless.

The dfs method is a customized version of the Depth-First Search (DFS) algorithm. Here's how it works:

Inside the dfs method, there is a variable called dfs_output (with an initial value of None). In case of a successful search, the output of the search will be recorded in this variable. In case of an unsuccessful search, the value of this variable will remain None.
DFS is best executed using recursion. Hence, we've utilized a nested recursive function - dfs_func - inside the dfs method. This nested function returns a Boolean: True if the search is successful, and False otherwise.
The base case is the following: if step > self.n_steps. But why? Well, it is assumed that if the current step has exceeded the number of steps required to solve the problem, then the search is successful. For example, in the Game of 24 task, self.n_steps is always equal to 4 (3 intermediate steps + 1 output generation step). Hence, if the current step exceeds 4, we record the output in the nonlocal variable dfs_output, and then backtrack all the way up by returning True.
In the recursive case, we generate thought candidates from the current node. Each of these thought candidates is added as a child of the current node.
Now, it's time to loop through the children. For each child, we obtain a value from the state evaluator.
We use a heuristic threshold to decide whether to grow a subtree (starting at this child) or prune it. After a bit of experimentation, we found that a heuristic threshold of 3.0 works well for this task.
If the value of a child fails to exceed the heuristic threshold, then the child node is pruned, i.e., a subtree of the child isn't grown.
Otherwise, we grow and search the subtree using the following recursive call: end_search = dfs_func(child, step + 1).
If end_search happens to be True, it means that the search was successful. In that case, we backtrack all the way up by returning True.
If end_search happens to be False, we don't return anything. Rather, we move on to the next child.
To provide more control over the search, an additional hyperparameter max_per_state is used. This hyperparameter specifies the maximum number of children to explore for a particular node. If the number of children explored touches max_per_state, we break the loop.
If looping through the children didn't lead to a successful search, then the current node seems like a dead end. In that case, we backtrack to the parent node. The search will continue...
All right, let's actually call the dfs method. By passing verbose=True, we can watch the DFS algorithm in action.

To get a feel for the algorithm, let's initially set max_per_state to an unreasonably low value: 2. (Since we're not allowing enough children to be explored at each node, the search will fail. This is deliberate. We want to see the backtracking in action in the search trace.)

tot = TreeOfThoughts(client, "gpt-4", input_seq, get_thought_gen_prompt, get_state_eval_prompt, heuristic_calculator, max_per_state=2)
output = tot.dfs(verbose=True)
print("None" if output is None else output)

Step: 1
---
State of current node:-
<EMPTY STRING> (root node; no thoughts generated yet)
---
Thought candidate 1:-
1 + 1 = 2 (left: 1 2 8)
---
Thought candidate 2:-
1 * 1 = 1 (left: 1 1 8)
---
Thought candidate 3:-
8 - 1 = 7 (left: 1 1 7)
---
Thought candidate 4:-
8 / 1 = 8 (left: 1 1 8)
---
Thought candidate 5:-
1 * 8 = 8 (left: 1 1 8)
---
Thought candidate 6:-
8 - 1 = 7 (left: 1 7 1)
---
Thought candidate 7:-
8 / 1 = 8 (left: 1 8 1)
---
Each of the above thought candidates has been added as a child of the current node.
---
Reminder:-
State of current node:-
<EMPTY STRING> (root node; no thoughts generated yet)
---
Currently traversing child number: 1

State of current child:-
1 + 1 = 2 (left: 1 2 8)

Using the state evaluator to obtain value...

Value of current child: 22.0
---
Value exceeds heuristic threshold. Searching subtree.
---
~~~
Step: 2
---
State of current node:-
1 + 1 = 2 (left: 1 2 8)
---
Thought candidate 1:-
1 + 2 = 3 (left: 3 8)
---
Thought candidate 2:-
2 * 1 = 2 (left: 2 8)
---
Thought candidate 3:-
8 - 1 = 7 (left: 2 7)
---
Thought candidate 4:-
8 / 1 = 8 (left: 2 8)
---
Thought candidate 5:-
8 - 2 = 6 (left: 1 6)
---
Thought candidate 6:-
2 * 8 = 16 (left: 1 16)
---
Thought candidate 7:-
1 * 2 = 2 (left: 2 8)
---
Each of the above thought candidates has been added as a child of the current node.
---
Reminder:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
---
Currently traversing child number: 1

State of current child:-
1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)

Using the state evaluator to obtain value...

Value of current child: 60.0
---
Value exceeds heuristic threshold. Searching subtree.
---
~~~
Step: 3
---
State of current node:-
1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
---
Thought candidate 1:-
3 + 8 = 11 (left: 11)
---
Thought candidate 2:-
8 - 3 = 5 (left: 5)
---
Thought candidate 3:-
8 / 3 = 2.67 (left: 2.67)
---
Thought candidate 4:-
3 * 8 = 24 (left: 24)
---
Each of the above thought candidates has been added as a child of the current node.
---
Reminder:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
---
Currently traversing child number: 1

State of current child:-
1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 + 8 = 11 (left: 11)

Using the state evaluator to obtain value...

Value of current child: 0.003
---
Reminder:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
---
Currently traversing child number: 2

State of current child:-
1 + 1 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
8 - 3 = 5 (left: 5)

Using the state evaluator to obtain value...

Value of current child: 0.003
---
2 children already searched for this node. Breaking the loop.
---
None of the child nodes led to success. Seems like a dead end. Backtracking to the parent node.
~~~
Back at step 2. Searching the subtree was unsuccessful! Trying the next child.
---
Reminder:-
State of current node:-
1 + 1 = 2 (left: 1 2 8)
---
Currently traversing child number: 2

State of current child:-
1 + 1 = 2 (left: 1 2 8)
2 * 1 = 2 (left: 2 8)

Using the state evaluator to obtain value...

Value of current child: 0.003
---
2 children already searched for this node. Breaking the loop.
---
None of the child nodes led to success. Seems like a dead end. Backtracking to the parent node.
~~~
Back at step 1. Searching the subtree was unsuccessful! Trying the next child.
---
Reminder:-
State of current node:-
<EMPTY STRING> (root node; no thoughts generated yet)
---
Currently traversing child number: 2

State of current child:-
1 * 1 = 1 (left: 1 1 8)

Using the state evaluator to obtain value...

Value of current child: 0.003
---
2 children already searched for this node. Breaking the loop.
---
None of the child nodes led to success. Seems like a dead end. Backtracking to the parent node.
~~~
None

Next, let's increase max_per_state to 10 (to increase the probability of a successful search), and see what happens.

tot = TreeOfThoughts(client, "gpt-4", input_seq, get_thought_gen_prompt, get_state_eval_prompt, heuristic_calculator, max_per_state=10)
output = tot.dfs(verbose=True)
print("None" if output is None else output)

Step: 1
---
State of current node:-
<EMPTY STRING> (root node; no thoughts generated yet)
---
Thought candidate 1:-
1 + 1 = 2 (left: 1 2 8)
---
Thought candidate 2:-
1 * 1 = 1 (left: 1 1 8)
---
Thought candidate 3:-
8 - 1 = 7 (left: 1 1 7)
---
Thought candidate 4:-
8 / 1 = 8 (left: 1 1 8)
---
Thought candidate 5:-
8 - 1 = 7 (left: 1 7 1)
---
Thought candidate 6:-
1 + 1 = 2 (left: 2 1 8)
---
Thought candidate 7:-
8 / 1 = 8 (left: 1 8 1)
---
Thought candidate 8:-
1 * 1 = 1 (left: 1 8 1)
---
Each of the above thought candidates has been added as a child of the current node.
---
Reminder:-
State of current node:-
<EMPTY STRING> (root node; no thoughts generated yet)
---
Currently traversing child number: 1

State of current child:-
1 + 1 = 2 (left: 1 2 8)

Using the state evaluator to obtain value...

Value of current child: 2.001
---
Reminder:-
State of current node:-
<EMPTY STRING> (root node; no thoughts generated yet)
---
Currently traversing child number: 2

State of current child:-
1 * 1 = 1 (left: 1 1 8)

Using the state evaluator to obtain value...

Value of current child: 0.003
---
Reminder:-
State of current node:-
<EMPTY STRING> (root node; no thoughts generated yet)
---
Currently traversing child number: 3

State of current child:-
8 - 1 = 7 (left: 1 1 7)

Using the state evaluator to obtain value...

Value of current child: 0.003
---
Reminder:-
State of current node:-
<EMPTY STRING> (root node; no thoughts generated yet)
---
Currently traversing child number: 4

State of current child:-
8 / 1 = 8 (left: 1 1 8)

Using the state evaluator to obtain value...

Value of current child: 0.003
---
Reminder:-
State of current node:-
<EMPTY STRING> (root node; no thoughts generated yet)
---
Currently traversing child number: 5

State of current child:-
8 - 1 = 7 (left: 1 7 1)

Using the state evaluator to obtain value...

Value of current child: 0.003
---
Reminder:-
State of current node:-
<EMPTY STRING> (root node; no thoughts generated yet)
---
Currently traversing child number: 6

State of current child:-
1 + 1 = 2 (left: 2 1 8)

Using the state evaluator to obtain value...

Value of current child: 21.001
---
Value exceeds heuristic threshold. Searching subtree.
---
~~~
Step: 2
---
State of current node:-
1 + 1 = 2 (left: 2 1 8)
---
Thought candidate 1:-
2 + 1 = 3 (left: 3 8)
---
Thought candidate 2:-
2 * 1 = 2 (left: 2 8)
---
Thought candidate 3:-
8 - 2 = 6 (left: 1 6)
---
Thought candidate 4:-
8 - 1 = 7 (left: 2 7)
---
Thought candidate 5:-
8 / 2 = 4 (left: 1 4)
---
Thought candidate 6:-
8 / 1 = 8 (left: 2 8)
---
Thought candidate 7:-
2 * 8 = 16 (left: 1 16)
---
Thought candidate 8:-
1 * 8 = 8 (left: 2 8)
---
Each of the above thought candidates has been added as a child of the current node.
---
Reminder:-
State of current node:-
1 + 1 = 2 (left: 2 1 8)
---
Currently traversing child number: 1

State of current child:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)

Using the state evaluator to obtain value...

Value of current child: 60.0
---
Value exceeds heuristic threshold. Searching subtree.
---
~~~
Step: 3
---
State of current node:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
---
Thought candidate 1:-
3 + 8 = 11 (left: 11)
---
Thought candidate 2:-
8 - 3 = 5 (left: 5)
---
Thought candidate 3:-
8 / 3 = 2.666667 (left: 2.666667)
---
Thought candidate 4:-
8 * 3 = 24 (left: 24)
---
Thought candidate 5:-
3 - 8 = -5 (left: -5)
---
Each of the above thought candidates has been added as a child of the current node.
---
Reminder:-
State of current node:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
---
Currently traversing child number: 1

State of current child:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
3 + 8 = 11 (left: 11)

Using the state evaluator to obtain value...

Value of current child: 0.002
---
Reminder:-
State of current node:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
---
Currently traversing child number: 2

State of current child:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
8 - 3 = 5 (left: 5)

Using the state evaluator to obtain value...

Value of current child: 0.002
---
Reminder:-
State of current node:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
---
Currently traversing child number: 3

State of current child:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
8 / 3 = 2.666667 (left: 2.666667)

Using the state evaluator to obtain value...

Value of current child: 0.002
---
Reminder:-
State of current node:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
---
Currently traversing child number: 4

State of current child:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
8 * 3 = 24 (left: 24)

Using the state evaluator to obtain value...

Value of current child: 60.0
---
Value exceeds heuristic threshold. Searching subtree.
---
~~~
Step: 4
---
State of current node:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
8 * 3 = 24 (left: 24)
---
Thought candidate 1:-
Answer: (1 + 1 + 1) * 8 = 24
---
Each of the above thought candidates has been added as a child of the current node.
---
Reminder:-
State of current node:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
8 * 3 = 24 (left: 24)
---
Currently traversing child number: 1

State of current child:-
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
8 * 3 = 24 (left: 24)
Answer: (1 + 1 + 1) * 8 = 24

Using the state evaluator to obtain value...

Value of current child: 60.0
---
Value exceeds heuristic threshold. Searching subtree.
---
~~~
Searching the subtree was successful! Backtracking all the way up.
~~~
Searching the subtree was successful! Backtracking all the way up.
~~~
Searching the subtree was successful! Backtracking all the way up.
~~~
Searching the subtree was successful! Backtracking all the way up.
~~~
1 + 1 = 2 (left: 2 1 8)
2 + 1 = 3 (left: 3 8)
8 * 3 = 24 (left: 24)
Answer: (1 + 1 + 1) * 8 = 24

The search was successful! The above search trace is awesome, right?

Ok. Let's visualize the tree.

tot.render_html_tree()

To circumvent the HTML rendering issue, I've saved the tree as an HTML file, which you can view here. Below is a screenshot of the same:



A Reusable TreeOfThoughts Class
In the above sections, the hyperparameters of ToT were hardcoded (mirroring the values used in the paper for Creative Writing and Game of 24, respectively). However, to make the class reusable, we need to accept the hyperparameters as arguments in the constructor.

Here's a reusable TreeOfThoughts class:

class TreeOfThoughts:
    def __init__(
            self,
            client: Union[OpenAI, InferenceClient],
            model: str,
            input_seq: str,
            n_steps: int,
            thought_gen_strategy: str,
            get_thought_gen_prompt: Callable,
            state_eval_strategy: str,
            get_state_eval_prompt: Callable,
            n_evals: int,
            heuristic_calculator: Callable,
            n_candidates: Optional[int] = None,
            stop_string: Optional[str] = None,
            breadth_limit: Optional[int] = None,
            heuristic_threshold: Optional[float] = None,
            max_per_state: Optional[int] = None
    ):
        self.client = client
        self.model = model # e.g., "gpt-4" if using `OpenAI` and "meta-llama/Meta-Llama-3.1-8B-Instruct" if using `InferenceClient`.
        self.input_seq = input_seq
        self.root = TreeNode(state='', thought='')
        self.n_steps = n_steps # Equal to the number of intermediate steps + 1 output generation step.
        # Note: The tree height is equal to `n_steps + 1`. That is, we include the root node when calculating the tree height.
        if thought_gen_strategy in ['sample', 'propose']:
            self.thought_gen_strategy = thought_gen_strategy
        else:
            raise ValueError(f"The `thought_gen_strategy` argument must be either 'sample' or 'propose'. Couldn't recognize the following: '{thought_gen_strategy}'")
        self.get_thought_gen_prompt = get_thought_gen_prompt
        if state_eval_strategy in ['vote', 'value']:
            self.state_eval_strategy = state_eval_strategy
        else:
            raise ValueError(f"The `state_eval_strategy` argument must be either 'vote' or 'value'. Couldn't recognize the following: '{state_eval_strategy}'")
        self.get_state_eval_prompt = get_state_eval_prompt
        self.n_evals = n_evals # The number of times to either (i) vote on the states, or (ii) sample values for each state (depending on `state_eval_strategy`).
        self.heuristic_calculator = heuristic_calculator
        self.n_candidates = n_candidates # The number of thoughts to generate from a particular node. Relevant only for the 'sample' thought generation strategy.
        self.stop_string = stop_string # Relevant only for the 'sample' thought generation strategy.
        if self.thought_gen_strategy == 'sample':
            assert self.stop_string is not None, "For the 'sample' thought generation strategy, `stop_string` can't be `None` (due to the zero-shot CoT prompt template)."
            assert self.n_steps == 2, "For the 'sample' thought generation strategy, `n_steps` must be equal to 2 (due to the zero-shot CoT prompt template)."
        self.breadth_limit = breadth_limit # The number of most promising states to retain (after pruning) - at each level of the tree. Relevant only for BFS.
        self.heuristic_threshold = heuristic_threshold # Used to decide whether to grow/prune a subtree (starting at a particular child). Relevant only for DFS.
        self.max_per_state = max_per_state # The maximum number of children to explore for a particular node. Relevant only for DFS.

    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/models.py
    def chat_completions(
            self,
            prompt: str,
            temperature: float = 0.7,
            max_tokens: int = 1000,
            n: int = 1,
            stop: Optional[List[str]] = None,
            **kwargs
    ) -> List[str]:
        outputs = []
        messages = [{'role': "user", 'content': prompt}]
        if isinstance(self.client, OpenAI):
            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=temperature,
                max_tokens=max_tokens,
                n=n, # The `n` responses are i.i.d.
                stop=stop,
                **kwargs
            )
            outputs.extend([choice.message.content for choice in response.choices])
        else: # `self.client` is an instance of `InferenceClient`.
            # The Hugging Face API doesn't support the `n` argument. Hence, we need to use a loop to generate `n` i.i.d. responses.
            for _ in range(n):
                response = self.client.chat.completions.create(
                    messages=messages,
                    model=self.model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    stop=stop,
                    **kwargs
                )
                outputs.append(response.choices[0].message.content)
        return outputs

    def thought_generator(self, state: str, stop_string: Optional[List[str]] = None) -> List[str]:
        prompt = self.get_thought_gen_prompt(self.input_seq, state)
        if self.thought_gen_strategy == 'sample':
            thoughts = self.chat_completions(prompt, n=self.n_candidates, stop=stop_string)
            return thoughts
        else: # `self.thought_gen_strategy` is equal to 'propose'.
            responses = self.chat_completions(prompt, n=1)
            thoughts = responses[0].split('\n')
            return thoughts

    def state_evaluator(self, states: Optional[List[str]] = None, state: Optional[str] = None) -> Union[List[float], float]:
        if self.state_eval_strategy == 'vote':
            assert states is not None, "For the 'vote' state evaluation strategy, `states` can't be `None`."
            prompt = self.get_state_eval_prompt(self.input_seq, states)
            state_evals = self.chat_completions(prompt, n=self.n_evals)
            vote_results = self.heuristic_calculator(states, state_evals)
            return vote_results
        else: # `self.state_eval_strategy` is equal to 'value'.
            assert state is not None, "For the 'value' state evaluation strategy, `state` can't be `None`."
            prompt = self.get_state_eval_prompt(self.input_seq, state)
            state_evals = self.chat_completions(prompt, n=self.n_evals)
            value = self.heuristic_calculator(state, state_evals)
            return value

    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/src/tot/methods/bfs.py
    def bfs(self, verbose: bool = True) -> str:
        assert self.breadth_limit is not None, "For the BFS search algorithm, `breadth_limit` can't be `None`."

        queue = deque()
        queue.append(self.root)

        for step in range(1, self.n_steps + 1):
            if verbose:
                print(f"Step {step} (corresponding to level {step} of the tree):-\n---")
            for i in range(len(queue)):
                node = queue.popleft()
                if verbose:
                    print(f"Node {i + 1} in level {step}:-")
                    if node.state != "":
                        print(f"State of current node:-\n{node.state}\n---")
                    else:
                        print("State of current node:-\n<EMPTY STRING> (root node; no thoughts generated yet)\n---")

                if self.thought_gen_strategy == 'sample' and step == 1:
                    thoughts = self.thought_generator(state=node.state, stop_string=[self.stop_string])
                else:
                    thoughts = self.thought_generator(state=node.state)
                if node.state == '':
                    updated_states = thoughts
                else:
                    updated_states = [node.state + '\n' + thought for thought in thoughts]
                for j in range(len(thoughts)):
                    if verbose:
                        print(f"Thought candidate {j + 1}:-\n{thoughts[j]}\n---")
                    child = TreeNode(state=updated_states[j], thought=thoughts[j])
                    node.children.append(child)
                    queue.append(child)

            if verbose:
                print("Using the state evaluator to obtain values...\n---")
            if self.state_eval_strategy == 'vote':
                states = [node.state for node in queue]
                values = self.state_evaluator(states=states)
            for i in range(len(queue)):
                if self.state_eval_strategy == 'vote':
                    queue[i].value = values[i]
                else: # `self.state_eval_strategy` is equal to 'value'.
                    queue[i].value = self.state_evaluator(state=queue[i].state)
                if verbose:
                    print(f"Element {i + 1} in queue:-\n")
                    print(f"Value: {queue[i].value}\n---")

            if verbose:
                print("Initiating pruning (using the values obtained from the state evaluator).")
                print(f"Number of elements in queue: {len(queue)}")
            sorted_nodes = sorted(queue, key=lambda node: node.value, reverse=True)
            if step == self.n_steps:
                if verbose:
                    print("Since this is the last step, setting the breadth limit to 1.")
                    print("In other words, retaining only the highest value element (in this last step).\n---")
                top_b_nodes = sorted_nodes[:1]
            else:
                if verbose:
                    print(f"Since this isn't the last step, leaving the breadth limit {self.breadth_limit} unchanged.\n---")
                top_b_nodes = sorted_nodes[:self.breadth_limit]
            top_b_states = [node.state for node in top_b_nodes]
            for i in range(len(queue)):
                node = queue.popleft()
                if verbose:
                    print(f"Element {i + 1} in queue:-\n")
                if node.state in top_b_states:
                    if verbose:
                        print(f"Retaining this element as it's in the top {len(top_b_states)} elements.\n---")
                    queue.append(node)
                else:
                    if verbose:
                        print(f"Dropping this element as it's not in the top {len(top_b_states)} elements.\n---")

            if verbose:
                print("~~~")

        # Return the thought of the highest value node (from the last step):
        node = queue.popleft()
        return node.thought

    # Reference: https://github.com/princeton-nlp/tree-of-thought-llm/blob/master/scripts/crosswords/search_crosswords-dfs.ipynb
    def dfs(self, verbose: bool = True) -> str:
        assert self.heuristic_threshold is not None and self.max_per_state is not None, "For the DFS search algorithm, `heuristic_threshold` and `max_per_state` can't be `None`."

        dfs_output = None

        def dfs_func(node: TreeNode, step: int) -> bool:
            nonlocal dfs_output

            if step > self.n_steps: # Base case: successful search.
                dfs_output = node.state # Record the last (output generation) step's output in the nonlocal variable `dfs_output`.
                return True

            if verbose:
                print(f"Step: {step}\n---")
                if node.state != "":
                    print(f"State of current node:-\n{node.state}\n---")
                else:
                    print("State of current node:-\n<EMPTY STRING> (root node; no thoughts generated yet)\n---")

            thoughts = self.thought_generator(state=node.state)
            if len(thoughts) == 0:
                if verbose:
                    print("No thoughts were generated. It's a dead end. Backtracking to the parent node.\n~~~")
                return False
            if node.state == '':
                updated_states = thoughts
            else:
                updated_states = [node.state + '\n' + thought for thought in thoughts]
            for j in range(len(thoughts)):
                if verbose:
                    print(f"Thought candidate {j + 1}:-\n{thoughts[j]}\n---")
                child = TreeNode(state=updated_states[j], thought=thoughts[j])
                node.children.append(child)
            if verbose:
                print("Each of the above thought candidates has been added as a child of the current node.\n---")

            cnt_per_state = 0
            for child in node.children:
                if verbose:
                    print("Reminder:-")
                    if node.state != "":
                        print(f"State of current node:-\n{node.state}\n---")
                    else:
                        print("State of current node:-\n<EMPTY STRING> (root node; no thoughts generated yet)\n---")
                    print(f"Currently traversing child number: {cnt_per_state + 1}\n")
                    print(f"State of current child:-\n{child.state}\n")
                    print("Using the state evaluator to obtain value...\n")
                child.value = self.state_evaluator(state=child.state)
                if verbose:
                    print(f"Value of current child: {child.value}\n---")
                if child.value >= self.heuristic_threshold:
                # Note: If this `if` condition isn't met, the child node is pruned, i.e., a subtree of the child isn't grown.
                    if verbose:
                        print("Value exceeds heuristic threshold. Searching subtree.\n---\n~~~")
                    end_search = dfs_func(child, step + 1)
                    if end_search:
                        if verbose:
                            print(f"Searching the subtree was successful! Backtracking all the way up.\n~~~")
                        return True
                    else:
                        if verbose:
                            print(f"Back at step {step}. Searching the subtree was unsuccessful! Trying the next child.\n---")
                cnt_per_state += 1
                if cnt_per_state >= self.max_per_state:
                    if verbose:
                        print(f"{self.max_per_state} children already searched for this node. Breaking the loop.\n---")
                    break
            if verbose:
                print(f"None of the child nodes led to success. Seems like a dead end. Backtracking to the parent node.\n~~~")
            return False

        dfs_func(node=self.root, step=1)
        return dfs_output

    def generate_html_tree(self, node: TreeNode) -> str:
        if node is None:
            return ""
        else:
            html = f"""<div class='node'>
<p>State:<br>{node.state}</p>
<hr>
<p>Thought:<br>{node.thought}</p>
<hr>
<p>Value:<br>{node.value}</p>"""
            for child in node.children:
                html += f"""<div class='child'>{self.generate_html_tree(child)}</div>"""
            html += """</div>"""
            return html

    def render_html_tree(self):
        html_tree = self.generate_html_tree(self.root)
        wrapped_html = f"""<!DOCTYPE html>
<html>
<head>
    <style>
        .node {{
            display: inline-block;
            border: 1px solid blue;
            padding: 10px;
            margin: 5px;
            text-align: center;
        }}
        .child {{
            display: flex;
        }}
    </style>
</head>
<body>
    {html_tree}
</body>
</html>"""
        display(HTML(wrapped_html))

To use the above class on a new task, we need to write three custom callables that work well for that task:

get_thought_gen_prompt
get_state_eval_prompt
heuristic_calculator
Custom callables provide the flexibility needed to adapt the ToT framework for a new task.

Additionally, we need to set hyperparameters that are suitable for that task. (In particular, the hyperparameters need to strike a balance between (i) how exhaustive the searches are, and (ii) the time taken, on average.) We should be able to set suitable hyperparameters using a combination of (1) our human knowledge/intuition about the task and (2) a bit of experimentation.

Armed with the above, we should be able to apply the ToT paradigm on a new task.

Conclusion
The ToT paper draws inspiration from the seminal work on artificial intelligence by Newell, Shaw & Simon from the 1950s. Newell et al. characterized problem solving as search through a combinatorial problem space, represented as a tree. But what's a combinatorial problem space? From the ToT paper:

Research on human problem-solving suggests that people search through a combinatorial problem space – a tree where the nodes represent partial solutions, and the branches correspond to operators that modify them. Which branch to take is determined by heuristics that help to navigate the problem-space and guide the problem-solver towards a solution.

In other words, humans perform heuristic-guided tree search to solve many of their day-to-day problems (without realizing it).

From Newell et al.:

A genuine problem-solving process involves the repeated use of available information to initiate exploration, which discloses, in turn, more information until a way to attain the solution is finally discovered.

The ToT paper takes inspiration from the above, and demonstrates the power of combining the chain of thought (CoT) reasoning capabilities of LLMs with a heuristic-guided tree search framework.

How do the results of ToT compare with CoT?

On the Creative Writing task, two types of evaluation are performed: (i) using a GPT-4 zero-shot prompt to provide a 1-10 scalar score (LLM-as-a-judge), and (ii) using human judgments to compare pairs of outputs from different methods.

On (i): ToT (7.56) was deemed to generate more coherent passages than CoT (6.93) on average.
On (ii): It was found that humans prefer ToT over CoT in 41 out of 100 passage pairs, whereas humans prefer CoT over ToT in 21 of 100 passage pairs.The other 38 pairs were found to be 'similarly coherent'.
On the Game of 24 task, while GPT-4 with CoT prompting only solved 4% of tasks, ToT achieved a success rate of 74%. That's a huge difference!

Hopefully this blog post made it a bit easier for you to understand and use the ToT paradigm. If you have any thoughts, please feel free to drop a comment!

GitHub repo: https://github.com/sambitmukherjee/reasoning-paradigms

Acknowledgement: I would like to thank my colleagues Rishav Dash, Sandeep Dey and Rahim Khan for their valuable feedback on the Python code, and on an earlier draft of this blog post.

References
J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi, Q. Le, and D. Zhou. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. arXiv preprint arXiv:2201.11903, 2022.
T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, Y. Iwasawa. Large Language Models are Zero-Shot Reasoners. arXiv preprint arXiv:2205.11916, 2022.
S. Yao, D. Yu, J. Zhao, I. Shafran, T. L. Griffiths, Y. Cao, K. Narasimhan. Tree of Thoughts: Deliberate Problem Solving with Large Language Models. arXiv preprint arXiv:2305.10601, 2023.
The Tree of Thoughts GitHub repo: https://github.com/princeton-nlp/tree-of-thought-llm
A. Newell, J. C. Shaw, and H. A. Simon. Report on a General Problem Solving Program. In IFIP congress, volume 256, page 64. Pittsburgh, PA, 1959.
Community
Upload images, audio, and videos by dragging in the text input, pasting, or clicking here.












System theme
TOS
Privacy
About
Careers
Models
Datasets
Spaces
Pricing
Docs