---
batch_name: custom-15-advanced-cognitive-science
batch_date: 2026-04-26
default_domain: cognitive-science
default_confidence: high
notes: |
  Custom seeding batch 15: advanced cognitive-science frameworks spanning
  computational, dynamical, predictive-processing, and consciousness theories.
---

# Batch: Advanced Cognitive Science

## Active Inference

- domain: cognitive-science
- secondary_domains: [computational-neuroscience, predictive-processing]
- aliases: [Friston active inference, action-as-inference]
- broader: [predictive-processing]
- related: [free-energy-principle, predictive-coding, bayesian-brain, embodied-cognition]
- prerequisites: [free-energy-principle, predictive-processing]
- confidence: medium

**definition**: Active Inference is a corollary of the Free Energy Principle developed by Karl Friston in which action and perception are unified under a single imperative: the organism minimizes long-term variational free energy by either updating its internal generative model to match sensory input (perception) or by acting on the world to make sensory input match the model (action).

**key_claim**: Active Inference's most striking theoretical move is to dissolve the distinction between control and inference: motor commands are reframed as proprioceptive predictions whose prediction errors are minimized by the spinal reflex arc moving the limb, so action becomes the resolution of self-fulfilling predictions rather than the output of a separate motor controller.

**warning**: Active Inference is mathematically elegant but empirically underdetermined; the same Active Inference equations can be made consistent with almost any observed behavior by adjusting the prior preferences of the generative model, and critics have argued the framework risks unfalsifiability unless its priors are independently constrained.

## Computational Theory of Mind

- domain: cognitive-science
- secondary_domains: [philosophy-of-mind, artificial-intelligence]
- aliases: [CTM, computationalism, mind-as-computer]
- broader: [philosophy-of-mind]
- related: [language-of-thought, symbol-grounding-problem, multiple-realizability, functionalism]
- prerequisites: [functionalism]
- confidence: high

**definition**: The Computational Theory of Mind is the thesis that mental states are computational states and mental processes are computational operations defined over internal representations, most influentially developed by Jerry Fodor as the conjunction of computationalism with a Language of Thought hypothesis postulating syntactically structured mental symbols.

**key_claim**: The Computational Theory of Mind's distinctive explanatory power lies in its account of productivity and systematicity: if thoughts are syntactically structured representations manipulated by formal rules, then the unbounded generativity of thought and its systematic patterns (anyone who can think aRb can think bRa) follow as predictions rather than as anomalies requiring separate explanation.

**warning**: The Computational Theory of Mind faces unresolved challenges from the symbol-grounding problem (how do internal symbols come to represent anything outside the system?), from connectionist and dynamical-systems alternatives that deny the explanatory necessity of structured symbols, and from embodied-cognition arguments that locate cognitive content in sensorimotor coupling rather than in internal computation.

## Dynamic Systems Theory of Cognition

- domain: cognitive-science
- secondary_domains: [embodied-cognition, developmental-psychology]
- aliases: [dynamicism, dynamical cognitive science]
- broader: [cognitive-science]
- related: [embodied-cognition, ecological-psychology, attractor-dynamics, computational-theory-of-mind]
- prerequisites: [cognitive-science]
- confidence: medium

**definition**: The Dynamic Systems Theory of Cognition is a research program — associated with Esther Thelen, Tim van Gelder, and Linda Smith — that models cognitive processes as the time-evolution of coupled state variables described by differential equations, emphasizing continuous change, multistability, and self-organization over discrete symbol manipulation.

**key_claim**: The Dynamic Systems Theory of Cognition reframes classical cognitive phenomena that appeared to demand internal representation as products of body-environment coupling: Thelen's account of infant locomotion development, for instance, replaces the maturation of a central walking program with a dynamical reassembly of leg, postural, and gravitational variables, showing that apparently stage-like cognitive transitions can emerge from continuous parameter change.

**warning**: The Dynamic Systems Theory of Cognition has been criticized for trading explanatory specificity for descriptive elegance: writing down a system of differential equations that fits a cognitive trajectory does not by itself explain the underlying mechanism, and the framework has had limited success accounting for the structured, compositional aspects of higher cognition that classical computational accounts were designed to handle.

## Free Energy Principle

- domain: cognitive-science
- secondary_domains: [computational-neuroscience, theoretical-biology]
- aliases: [FEP, Friston free energy principle, variational free energy]
- broader: [predictive-processing]
- related: [active-inference, predictive-coding, bayesian-brain, markov-blankets]
- prerequisites: [predictive-processing, bayesian-inference]
- confidence: medium

**definition**: The Free Energy Principle, formulated by Karl Friston, is the claim that any self-organizing system at non-equilibrium steady state with its environment must, by mathematical necessity, act so as to minimize a quantity called variational free energy — an information-theoretic upper bound on the surprise of its sensory observations under its internal generative model.

**key_claim**: The Free Energy Principle attempts to derive the existence of perception, action, and learning from a single principle: in this framing, the brain does not minimize free energy as one objective among others, but is the kind of thing that exists at all only because it minimizes free energy, making the principle a candidate for a unified theory of biological self-organization rather than merely of neural function.

**warning**: The Free Energy Principle is contested both mathematically and methodologically; critics including Andy Clark, Jakob Hohwy, and others have argued that the principle is either trivially true (because variational free energy can be defined post-hoc to fit any system) or substantively false (because real brains do not implement the assumed Markov-blanket structure), and the literature is still working out which interpretation of the Free Energy Principle, if any, makes empirically testable predictions.

## Global Workspace Theory

- domain: cognitive-science
- secondary_domains: [consciousness-studies, cognitive-neuroscience]
- aliases: [GWT, Baars global workspace, Dehaene global neuronal workspace]
- broader: [theories-of-consciousness]
- related: [integrated-information-theory, attention, working-memory, neural-correlates-of-consciousness]
- prerequisites: [consciousness-studies]
- confidence: medium

**definition**: Global Workspace Theory, originally proposed by Bernard Baars and developed neurally by Stanislas Dehaene as Global Neuronal Workspace Theory, models conscious access as the broadcast of selected information from local specialist processors to a brain-wide workspace, where it becomes available to working memory, report, and flexible behavior.

**key_claim**: Global Workspace Theory predicts a specific neural signature of conscious access — the "ignition" of large-scale, late, recurrent activity in fronto-parietal networks distinct from the early local processing of unconscious stimuli — and substantial evidence from masking and attentional-blink paradigms supports a sharp ignition threshold, providing one of the strongest empirical bridges between a theoretical framework and the neural correlates of consciousness.

**warning**: Global Workspace Theory is a theory of conscious access (what makes information reportable and globally available) rather than of phenomenal experience (what makes there be something it is like to undergo a state), and conflating the two is the most persistent error in its reception; competing theories such as Integrated Information Theory explicitly target phenomenal consciousness, and any apparent direct competition between Global Workspace Theory and IIT first requires settling which explanandum is in question.

## Integrated Information Theory

- domain: cognitive-science
- secondary_domains: [consciousness-studies, philosophy-of-mind]
- aliases: [IIT, Tononi IIT, phi theory of consciousness]
- broader: [theories-of-consciousness]
- related: [global-workspace-theory, panpsychism, neural-correlates-of-consciousness, computational-theory-of-mind]
- prerequisites: [consciousness-studies]
- confidence: medium

**definition**: Integrated Information Theory, developed by Giulio Tononi, identifies consciousness with the quantity and structure of integrated information (denoted phi) generated by a physical system — information that is irreducible to the information in the system's parts taken independently — and proposes that any system with non-zero phi has some degree of phenomenal experience.

**key_claim**: Integrated Information Theory inverts the standard explanatory order of consciousness science: rather than starting from neural mechanisms and asking which produce consciousness, it begins from axioms about the intrinsic properties of experience and derives the physical substrate that must instantiate them, leading to the controversial prediction that simple feed-forward networks (including most current AI systems) have zero phi and therefore no experience regardless of their behavioral sophistication.

**warning**: Integrated Information Theory's commitments lead it into territory many cognitive scientists treat as a reductio: it implies a graded panpsychism in which simple physical systems possess minimal experience, it has been formally shown to be in principle incomputable for systems of realistic size, and a 2023 open letter from over a hundred scientists labeled it "pseudoscience" — a charge that itself remains contested but illustrates the depth of methodological disagreement Integrated Information Theory provokes.
