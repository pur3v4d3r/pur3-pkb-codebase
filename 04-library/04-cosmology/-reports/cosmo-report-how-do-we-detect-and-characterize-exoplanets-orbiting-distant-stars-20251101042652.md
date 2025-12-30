---
title: cosmo-report-cosmo-report-how-do-we-detect-and-characterize-exoplanets-orbiting-distant-stars-20251101042652-20251120094837
id: "20251120094837"
type: cosmo/report
status: not-read
source: Problem-Based-Learning
year: "[[2025]]"
tags:
  - cosmology
  - project/pur3v4d3r
  - year/2025
  - self-improvement
  - pkb/metadata/frontmatter
  - pkb/maintenance/refactoring
  - pkb/maintenance/cleanup
aliases:
  - academic/reports,report,Exoplanetary Systems,General Relativity,Albert Einstein
link-up:
  - "[[project-pur3v4d3r-moc]]"
link-related:
  - "[[2025-11-20|Daily-Note]]"
---

***

> [!thought-experiment]
> Imagine you are standing in Los Angeles, looking towards a single, blindingly powerful stadium searchlight in New York City. Now, imagine you have to find a single, non-illuminated *firefly* that is hovering one foot away from that searchlight. Your task is to not only prove the firefly exists, but to determine its size, mass, and what it had for dinner, all without leaving Los Angeles. This scenario is not an exaggeration; it is a direct and accurate analogy for the monumental challenge of finding and characterizing [[exoplanets]], or planets orbiting other stars.

---

> [!abstract]
> This investigation tackles the central observational problem in modern astronomy: the detection and characterization of [[exoplanetary systems]]. The core challenge is one of an almost unimaginable contrast and separation. Planets are vanishingly faint, reflecting only a tiny fraction of their host star's light, and are separated by an angular distance so small that they are completely lost in the star's glare. An Earth-like planet, for example, is about ten billion times ($10^{-10}$) fainter than its Sun-like star in visible light.
>
> To solve this "impossible" problem, astronomers have developed a toolkit of ingenious *indirect* methods. This report will systematically deconstruct the four primary solutions. We will explore the [[Transit Method]], which watches for the subtle *dimming* of a star as a planet passes in front of it. We will analyze the [[Radial Velocity Method]], which measures the tiny gravitational "wobble" a planet induces in its host star. We will also investigate the technologically demanding [[Direct Imaging]] method, which uses advanced optics to *block* the starlight and capture a direct photon from the planet itself. Finally, we will examine the [[Gravitational Microlensing]] technique, which uses [[Albert Einstein]]'s theory of [[General Relativity]] to detect planets by how their gravity magnifies a distant background star.
>
> The final outcome of this analysis will demonstrate that no single method is sufficient. The "solved state" of exoplanetology is achieved only through the *synergy* of these methods. By combining the [[radius]] data from transits with the [[mass]] data from radial velocity, we can calculate a planet's [[density]] and begin to characterize it. By applying [[spectroscopy]] during a transit, we can even "read" the chemical composition of its atmosphere, moving us from a simple census of planets to the profound search for [[life]] elsewhere in the cosmos.

# 1.0  DIAGNOSTICS: Deconstructing the Problem

> [!the-purpose]
> The purpose of this section is to move from the "fuzzy" problem of "finding other planets" to a "clear" problem by defining the specific, quantifiable physical challenges that make this task so difficult. We must first diagnose the illness before we can prescribe the cure. The problem is not one, but a trio of fundamental constraints.

> [!pre-read-questions]
> - *What are the* **known symptoms** *or components of this problem?*
>     - The primary symptom is a failure of direct observation. The problem is defined by three core challenges:
>     1.  **The Brightness Ratio Problem:** This is the "firefly and searchlight" issue. A star is a thermonuclear furnace, while a planet merely shines in reflected light (or faint intrinsic heat). The contrast ratio between a Sun-like star and an Earth-like planet is as extreme as one-to-ten-billion ($1:10^{-10}$). For a larger [[gas giant]] like Jupiter, the ratio is still one-to-one-billion ($1:10^{-9}$) in reflected light. Any telescope pointed at the system is simply saturated by the star's light, and the planet's photons are lost in the noise.
>     2.  **The Angular Separation Problem:** From our perspective on Earth, even planets in wide orbits are incredibly close to their parent stars on the sky. The [[angular resolution]] required to separate the two points of light is immense. This small separation means the planet's faint light is not just *fainter* than the star, but it is *physically located* deep within the star's "glare," a region of bright, diffracted light called a "speckle pattern".
>     3.  **The Time Scale Problem:** Planetary orbits are slow. A planet analogous to Jupiter, with a 12-year orbit, would require *decades* of patient observation to confirm its motion. A planet with a 2,000-year orbit, like Fomalhaut b, is impossible to track for a full revolution. This demands long-term stability in instrumentation and generational dedication from astronomers.
> - *What are the* **key constraints** *(e.g., time, tools, budget, physics) we must work within?*
>     - The primary constraints are the fundamental laws of [[optics]] and the Earth's atmosphere. [[Diffraction]] is a physical limit on how small a point of light a telescope can resolve. Furthermore, observing from the ground means we must look through our own turbulent [[atmosphere]], which blurs starlight and makes the speckle problem far worse. This necessitates either space-based observatories or the development of complex [[Adaptive Optics]] (ExAO) systems.
> - *What would a* **"successful solution"** *look like? What are the acceptance criteria?*
>     - A "successful solution" is not a single photograph. It is a multi-stage process of *confirmation* and *characterization*.
>     1.  **Detection:** A reliable, repeatable signal that indicates the presence of an object.
>     2.  **Confirmation:** Proof that the object is planetary in nature (i.e., has a mass below the deuterium-burning limit, ~$13$ [[Jupiter (mass)|Jupiter masses]]) and is gravitationally bound to the star, not a background object or a smaller companion star.
>     3.  **Characterization:** The ultimate goal. This means measuring the planet's key parameters: its [[orbital period]], its [[radius]], its [[mass]], and from those, its [[density]] (which tells us if it's rocky, gaseous, or "puffy"). The "holy grail" is [[atmospheric composition]].

> [!plan]
> **Our Learning Quest:**
> - Given these challenges, direct observation is a near-impossibility for most planets. Our quest must therefore be to understand the *indirect* methods that cleverly bypass these problems. We will acquire a toolkit of four solutions, each designed to exploit a different physical principle:
>     1.  **Toolkit Item 1:** The [[Transit Method]], which solves the brightness problem by *ignoring* the planet's light and focusing on the *shadow* it casts.
>     2.  **Toolkit Item 2:** The [[Radial Velocity Method]], which solves the problem by ignoring the planet's light entirely and measuring the *gravitational influence* it has on its star.
>     3.  **Toolkit Item 3:** The [[Direct Imaging]] method, which *directly confronts* the brightness problem using high-contrast optical tools like [[coronagraphy]].
>     4.  **Toolkit Item 4:** The [[Gravitational Microlensing]] method, which uses the planet's gravity as a *magnifying glass* for a more distant star.

# 2.0 🛠️ TOOLKIT ACQUISITION: Targeted Principles

This section provides a deep dive into the foundational principles of the four key detection methods. This is the "just-in-time" learning required to build our solution.

> [!principle-point]
> - **Required Concept 1:** [[Transit Method (Photometry)]]
>     - The [[Transit Method]] is currently the most successful exoplanet detection technique, responsible for the vast majority of known planets, largely thanks to space missions like the [[Kepler Space Telescope]] and [[TESS (Transiting Exoplanet Survey Satellite)]]. The principle is elegantly simple: if a planet's orbit happens to be aligned *edge-on* from our line of sight, it will periodically pass, or "transit," in front of its host star. This passage blocks a tiny fraction of the star's light, causing a small, temporary, and periodic *dip* in the star's observed brightness. This method completely bypasses the planet's faintness; it only cares about the *shadow* it casts. Astronomers monitor the brightness of thousands of stars simultaneously, looking for these tell-tale signals. The data is plotted on a [[Light Curve]], which is a graph of brightness versus time. A transit appears as a characteristic U-shaped dip in this graph.
>     - This method is incredibly powerful for characterization. The *depth* of the dip (how much the light dims) is proportional to the ratio of the planet's area to the star's area. If we know the star's size, we can calculate the planet's **radius**. The *frequency* of the dips (how often they repeat) tells us the planet's **orbital period**. Its main limitation is geometric: it only works for the small fraction of planetary systems that happen to be aligned perfectly with our line of sight.

> [!definition]
> - **Key Term:** [[Light Curve]]
>     - A [[light curve]] is a fundamental tool in astronomy. It is a graph that plots the measured brightness (or [[photometric]] flux) of a celestial object over a period of time. For transit-hunters, this graph is their primary data. A flat line indicates a stable star, while a repeating, U-shaped dip is the "smoking gun" signature of a transiting planet. The precise shape of this dip, including its "ingress" (start) and "egress" (end), can even provide clues about the planet's atmosphere or the presence of rings or moons.

> [!analogy]
> - **To understand** the [[Transit Method]] **imagine** a single, distant streetlight in a fog. You are trying to find a moth flying around it. You cannot see the moth itself, but you can precisely measure the brightness of the streetlight. Every time the moth's flight path brings it between you and the bulb, the light dims by a tiny, almost imperceptible amount. If you see this *exact same dimming* happen with a regular, repeating pattern (e.g., every 5 minutes), you can confidently deduce the moth's existence, its orbital period, and even its size based on how much light it blocked.

> [!principle-point]
> - **Required Concept 2:** [[Radial Velocity Method (Doppler Spectroscopy)]]
>     - This was the first successful exoplanet detection method and is also known as "Doppler Spectroscopy" or the "wobble method". It relies on a key principle of [[Newtonian mechanics]]: a planet does not orbit its star. Rather, the planet and star *orbit each other* around their common center of mass, or [[barycenter]]. Because the star is vastly more massive, the barycenter is usually located *inside* the star, but not at its exact center. This means the star executes its own tiny "wobble" orbit in response to the planet's gravitational tug.
>     - We detect this wobble using the [[Doppler effect]]. As the star moves *towards* Earth in its tiny orbit, its light waves are compressed, and its spectrum shifts to shorter, bluer wavelengths (a [[blueshift]]). As it moves *away* from Earth, its light waves are stretched, shifting to longer, redder wavelengths (a [[redshift]]). By taking high-resolution spectra of the star over time, astronomers can measure this periodic shift in its spectral absorption lines and plot a [[radial velocity]] curve. The *period* of this curve is the planet's orbital period. The *amplitude* of the velocity change reveals the star's speed, which is directly related to the planet's mass. This method is best for finding massive planets (like "hot Jupiters") in close-in orbits, as they produce the largest, fastest, and most easily detectable wobbles.

> [!definition]
> - **Key Term:** [[Minimum Mass (m sin i)]]
>     - The [[Radial Velocity Method]] has a key ambiguity. It can only measure the star's motion *along our line of sight* (its "radial" velocity). It cannot detect motion perpendicular to us. This means we don't know the *inclination* (denoted $i$) of the planet's orbit. If the system is "face-on" (inclination $i=0^\circ$), the star wobbles "side-to-side" and we detect no radial velocity at all. If it's "edge-on" ($i=90^\circ$), we measure the full velocity. Because we usually don't know $i$, the mass we calculate is not the true mass, but the **minimum mass**, or $m \sin i$. This is a crucial distinction. However, if a planet is *also* seen to transit, we know its inclination must be very close to $90^\circ$, allowing us to solve for $i$ and determine the planet's *true mass*.

> [!principle-point]
> - **Required Concept 3:** [[Direct Imaging]]
>     - This is the "brute force" solution to the "firefly and searchlight" problem. It is the only method that captures actual photons—typically in the [[infrared]] spectrum—that are coming from the planet itself. At infrared wavelengths, the contrast problem is *slightly* better: a young, hot, Jupiter-sized planet can be "only" a million times fainter than its star, rather than a billion. To succeed, direct imaging requires two cutting-edge technologies.
>     - First is **[[Adaptive Optics (ExAO)]]**, a system on ground-based telescopes that corrects for the blurring effect of Earth's atmosphere. It uses a high-speed deformable mirror that changes its shape hundreds of times per second to counteract atmospheric turbulence, producing an image as sharp as if the telescope were in space.
>     - Second is **[[Coronagraphy]]**. A coronagraph is an instrument *inside* the telescope that uses a system of masks to physically block the light from the star, creating an artificial eclipse and revealing the faint objects orbiting nearby. An even more advanced concept is a [[starshade]], a separate, precisely flown spacecraft that would position itself many kilometers away from a space telescope to block starlight *before* it even enters the instrument. This method is heavily biased towards finding very large, young (and thus hot and self-luminous) planets in *very wide orbits*, far from their star's glare.

> [!principle-point]
> - **Required Concept 4:** [[Gravitational Microlensing]]
>     - This method is perhaps the most exotic, as it relies on [[Einstein's General Relativity]]. Einstein predicted that a massive object's gravity can bend the path of light, acting like a lens. In [[gravitational microlensing]], the "lens" is a foreground star (with its planet) that, by pure chance, drifts *exactly* in front of a much more distant background "source" star from our point of view. The foreground star's gravity bends and magnifies the light from the background star, causing it to brighten and fade in a characteristic way over several weeks.
>     - If the "lens" star also hosts a planet, that planet's own gravity will act as a *secondary* "mini-lens." This creates a brief, sharp *extra* spike of magnification during the main event, betraying the planet's presence. This method is unique for several reasons. It is a *one-time event* based on a chance alignment, so it cannot be repeated. It is the only method that can detect planets at immense distances (e.g., in the [[Galactic Bulge]], thousands of light-years away). It is also uniquely sensitive to "cold" planets in wide orbits (like Jupiter-analogs) and is the *only* method capable of finding [[free-floating planets]]—"rogue" worlds that orbit no star at all.

# 3.0 🔬 THE WORKSHOP: Building the Solution

This section moves from theory to application. We will now synthesize the "Toolkit" concepts from Section 2.0 to detail the step-by-step workflow astronomers use to find and, crucially, *characterize* a new world.

> [!your-new-workflow]
> The modern exoplanet-hunting workflow is a multi-stage process that functions like a funnel. It starts with a wide, shallow survey to find thousands of *candidates*, then moves to a focused, deep follow-up campaign to *confirm* and *characterize* the most promising ones. The solution is not one method, but a carefully choreographed dance between them.

### 3.1 ⚙️ Phase One: The Survey (Finding the Candidate)

> [!phase-one]
> The first step is a large-scale survey designed to sift through millions of stars for promising "candidates." For the [[Transit Method]], this is the job of space-based observatories. The [[TESS (Transiting Exoplanet Survey Satellite)]] mission, for example, divides the sky into sectors and stares at each one for ~27 days, capturing the brightness of millions of stars. This data is fed into a sophisticated "pipeline," a software system that automatically scans every single [[light curve]] for periodic, transit-like dips. This process generates a massive list of "TESS Objects of Interest" (TOIs). A similar survey strategy is used for [[Gravitational Microlensing]], where ground-based survey telescopes monitor the crowded fields of the [[Galactic Bulge]], looking for the unique brightening events that signal a lensing alignment. This phase is all about statistics and finding the "needle in the haystack."

> [!example]
> - A TESS pipeline flags a star designated `TIC 4201` as a TOI. The data shows a 0.8% dip in brightness that repeats with a precise period of $P = 6.2$ days. The data is clear and unambiguous. However, this is *only a candidate*. This dip *could* be caused by an [[eclipsing binary]] star system or other stellar phenomena. It now moves to Phase Two for confirmation.

### 3.2 ⚙️ Phase Two: The Confirmation (Is it a Planet?)

> [!phase-two]
> This is where the synergy of methods begins. The transit from Phase One gave us two key parameters: the orbital period ($P = 6.2$ days) and the planet's radius (a 0.8% dip from a Sun-like star suggests a "sub-Neptune" size). But we don't know its *mass*. Is it a planet, or a tiny, dim star? To answer this, we turn to the [[Radial Velocity Method]].
>
> Astronomers at a ground-based observatory will point a high-resolution spectrograph at `TIC 4201`. They will observe the star over several weeks, measuring its [[Doppler shift]]. Because they *already know* the period from the transit, they know exactly what to look for: a "wobble" signal that repeats every 6.2 days. If they find this signal, they have achieved two things:
> 1.  **Confirmation:** The signal is real and co-planar with the transit, confirming the object's existence.
> 2.  **Mass Measurement:** The *amplitude* of the wobble tells them the star's velocity, which allows them to calculate the planet's [[Minimum Mass (m sin i)]]. Since the planet *transits*, we know the inclination $i$ is near $90^\circ$, so this minimum mass is effectively the *true mass*.
>
> The object is now a *confirmed planet*, with both a known radius and a known mass.

> [!helpful-tip]
> - A primary challenge in this phase is "stellar jitter." Stars are not perfectly stable; they have spots (like sunspots) and flares that can rotate in and out of view, creating their *own* Doppler signals that can mimic or obscure a planet's signal. A key part of the "workshop" is using advanced statistical analysis to filter out this stellar noise and isolate the true, periodic wobble caused by the planet's gravity.

### 3.3 ⚙️ Phase Three: The Characterization (What is it *like*?)

> [!phase-three]
> This is the final and most exciting phase, where detection becomes astrophysics. We now have the two most important numbers for our planet:
> * **Radius ($R$):** From the transit depth.
> * **Mass ($M$):** From the RV amplitude.
>
> With these two values, we can perform our first act of characterization: calculating the planet's **bulk density** (Density $\rho = M / V$, where Volume $V = \frac{4}{3}\pi R^3$). This single value is transformative. Is the density low (like $0.7 \text{ g/cm}^3$, similar to Saturn), indicating a "puffy" [[gas giant]]? Is it high (like $5.5 \text{ g/cm}^3$, like Earth), indicating a rocky [[terrestrial planet]]? Or is it somewhere in between, suggesting a "water world" or an "ice giant" like Neptune?
>
> But we can go even further. We can now perform **[[Transmission Spectroscopy]]**. The next time `TIC 4201 b` transits its star, we will observe it with a powerful spectrograph, like the one on the [[James Webb Space Telescope (JWST)]]. As the starlight passes *through* the planet's upper atmosphere on its way to us, molecules in that atmosphere will absorb specific wavelengths of light. Water ($H_2O$) absorbs in the infrared. So does [[methane]] ($CH_4$) and [[carbon dioxide]] ($CO_2$). By taking a spectrum of the star *during* the transit and subtracting a spectrum taken *out of* transit, astronomers are left with the *absorption spectrum of the atmosphere itself*. This reveals a chemical "bar code," allowing us to identify the molecules present in the air of a world light-years away.

# 4.0 🏁 POST-MORTEM: Analysis of the Outcome

This section analyzes the "solved" state. We have successfully moved from a single, ambiguous "dip" in a light curve to a fully characterized exoplanet, bypassing the seemingly impossible observational challenges outlined in Section 1.0.

> [!outcome]
> The final result is a *character*. The "after" state is no longer a "candidate" but a *known world*. Our `TIC 4201 b` is now in the exoplanet catalog as a confirmed "sub-Neptune" with a radius of 2.7 Earth-radii, a mass of 8.3 Earth-masses, and a bulk density of $2.4 \text{ g/cm}^3$. This density suggests it is not a rocky planet, but a "water world" or a planet with a substantial hydrogen-helium envelope. Furthermore, our [[Transmission Spectroscopy]] in Phase Three (Section 3.3) provided a "flat" spectrum, suggesting the planet is enshrouded in high-altitude clouds or haze, which is itself a critical piece of information. The initial problems of brightness and separation were rendered moot; we succeeded by *never trying* to see the planet's reflected light, but instead by forensically analyzing its *effects* on its parent star.

> [!key-claim]
> - *Based on this workflow, a* **key claim** *is that:*
>     - The power of exoplanet science lies in **synergy**. No single detection method provides a complete picture. The [[Transit Method]] is a powerful "discovery machine" that finds planets and measures their *size*. But it is *mass-blind*. The [[Radial Velocity Method]] is a powerful "confirmation machine" that measures *mass*. But it is *size-blind*. Only by combining them do we unlock the key to composition: **density**. This synergistic approach (Transit + RV) is the "gold standard" for characterizing the thousands of small planets that missions like TESS and Kepler have discovered.

> [!counter-argument]
> - **An important alternative solution or trade-off is:**
>     - The entire Transit + RV workflow has a massive **observational bias**. Because short-period transits are more likely to be observed, and close-in, massive planets produce the largest RV signals, this workflow is *exceptionally* good at finding planets in *close-in, fast orbits*. It is almost completely *blind* to planets with orbits similar to our own Jupiter or Saturn.
> - **This is important because:**
>     - It highlights the critical, complementary role of [[Direct Imaging]] and [[Gravitational Microlensing]]. [[Direct Imaging]] is biased in the *exact opposite way*: it is best suited for finding massive planets in *wide, distant orbits*. [[Gravitational Microlensing]] is also sensitive to planets in wide, "cold" orbits that are analogues to our own gas giants. Therefore, to build a complete census of an exoplanetary system—to understand both its "inner" and "outer" architecture—astronomers *must* employ this full, complementary suite of tools.

# 5.0 🌐 GENERALIZATION: Transferring the Knowledge

This section "zooms out" to explore the wider implications of this problem-solving methodology. Now that we have solved the *specific* problem of detection, how can the *principles* and *workflow* be applied to even bigger questions?

> [!insight]
> - **The core insight from this exercise is:**
>     - We have learned that the greatest challenges in [[astrophysics]] are often solved *indirectly*. The problem of seeing a planet's light was not solved by building a telescope big enough to see it. It was solved by reframing the question. Instead of asking, "How can we see the planet?", astronomers asked, "What *measurable effect* does a planet have on its environment?" The answer was its shadow (Transit), its gravity (RV, Microlensing), and its heat (Direct Imaging). This is a *forensic* approach to science. We are not "seeing" the world; we are analyzing the evidence it leaves behind on its star.

> [!connection-ideas]
> - *The workflow used here* **can also be applied to the field of:**
>     - [[Astrobiology]] and the search for [[Biosignatures]].
> - **The reason:**
>     - The [[Transmission Spectroscopy]] workflow from Section 3.3 is *exactly* the method that will be used in the search for life. The "characterization" problem is the direct precursor to the "astrobiology" problem. Instead of just looking for common molecules like water and methane, the next generation of this workflow will be tuned to search for **[[biosignatures]]**: gases that are out of chemical equilibrium and could only be produced by a living [[biosphere]]. Examples include the simultaneous presence of [[oxygen]] ($O_2$) and [[methane]] ($CH_4$). On Earth, these two gases rapidly destroy each other, and their co-existence is a powerful sign that life is constantly replenishing the supply. This transfers our "planet-hunting" toolkit into a "life-hunting" one.

---

# 6.0 🧠 Key Questions (Metacognition)

> [!ask-yourself-this]
> - *How would* **I explain** *the* *solution to this problem* *to a colleague*? (**The Colleague Test**)
>     - We find planets by *ignoring* them and *watching their star* instead. The two main ways are by looking for "flickers" or "wobbles." We use space telescopes like TESS to find the "flicker"—a tiny, periodic dimming of starlight caused by the planet *transiting* in front of it. This gives us the planet's **size**.
>     - Then, we use ground-based spectrographs to find the "wobble"—a tiny, periodic Doppler shift in the star's spectrum caused by the planet's gravity *tugging* on it. This gives us the planet's **mass**. Once we have both size and mass, we can calculate its **density** and know if it's a rock or a gas ball. For the really big planets that are far from their star, we can just block the starlight with a [[coronagraph]] and take a direct picture.
> - *What was the* **single biggest "blocker"** *to solving this problem initially?* **Why**?
>     - The single biggest blocker was the **signal-to-noise ratio**. The "signal" is the planet's light, and the "noise" is the star's light, which is a billion times brighter. All the "smart" methods (Transit, RV) are clever ways to *change the problem*. Instead of trying to detect a faint signal *buried in* noise, they *modulate* the noise itself. The transit modulates the star's *brightness*. The RV method observes the modulation of the star's *wavelength*. They found a way to make the "noise" *become* the signal.
> - *What* **new questions** *does this solution raise?*
>     - This solution has raised a new, more profound set of questions. We've gone from "Are there other planets?" to:
>         1.  **Why are they so weird?** Our toolkit has revealed "[[Hot Jupiters]]" (gas giants orbiting in days), "Super-Earths," and "Mini-Neptunes"—planet types that *do not exist* in our solar system. This has broken our theories of [[planet formation]].
>         2.  **Are any of them habitable?** Now that we can find Earth-sized planets and probe their atmospheres, the new quest is defining and searching for the [[Habitable Zone]] and identifying true [[Earth 2.0]] candidates.
>         3.  **Are we missing a population?** Our methods are biased. How many Earth-sized planets in Earth-like (1-year) orbits are we *not* seeing?

> [!tasks]
> - **Next Actions:**
>     - Investigate the [[planet formation]] theories that attempt to explain the "hot Jupiter" phenomenon, such as [[planetary migration]].
>     - Research the capabilities of the [[James Webb Space Telescope (JWST)]] for transmission spectroscopy and compare its sensitivity to the [[Hubble Space Telescope]].
>     - Explore the "Phase Curve" method, an advanced technique that measures the changing brightness of a planet as it goes through its own "phases" (like our Moon).

# 7.0 📚 Reference/Appendix

> [!cite]
> - [MODEL&CO: exoplanet detection in angular differential imaging by learning across multiple observations | Monthly Notices of the Royal Astronomical Society | Oxford Academic](https://academic.oup.com/mnras/article/534/2/1569/7762210) [1.1]
> - [Methods of detecting exoplanets - Wikipedia](https://en.wikipedia.org/wiki/Methods_of_detecting_exoplanets) [1.2]
> - [Roadmap for Exoplanet High-Contrast Imaging: Nulling Interferometry, Coronagraph, and Extreme Adaptive Optics - MDPI](https://www.mdpi.com/2304-6732/12/10/1030) [1.3]
> - [What's a transit? - NASA Science](https://science.nasa.gov/exoplanets/whats-a-transit/) [2.1]
> - [Transit method | Exoplanetary Science Class Notes - Fiveable](https://fiveable.me/exoplanetary-science/unit-1/transit-method/study-guide/EWiCTGx1hN8DqYzG) [2.2]
> - [Explained: Transiting exoplanets | MIT News | Massachusetts Institute of Technology](https://news.mit.edu/2011/exp-transits-0127) [2.3]
> - [Color-Shifting Stars: The Radial-Velocity Method - The Planetary Society](https://www.planetary.org/articles/color-shifting-stars-the-radial-velocity-method) [3.1]
> - [Radial Velocity Method - Las Cumbres Observatory](https://lco.global/spacebook/exoplanets/radial-velocity-method/) [3.2]
> - [Doppler spectroscopy - Wikipedia](https://en.wikipedia.org/wiki/Doppler_spectroscopy) [3.3]
> - [Direct Imaging - Las Cumbres Observatory](https://lco.global/spacebook/exoplanets/direct-imaging/) [4.1]
> - [What is the Direct Imaging Method? - Universe Today](https://www.universetoday.com/articles/what-is-direct-imaging) [4.2]
> - [Fireflies Next to Spotlights: The Direct Imaging Method - The Planetary Society](https://www.planetary.org/articles/fireflies-next-to-spotlights-the-direct-imaging-method) [4.3]
> - [Gravitational Microlensing - Las Cumbres Observatory](https://lco.global/spacebook/exoplanets/gravitational-microlensing/) [5.1]
> - [Microlensing Searches for Exoplanets - MDPI](https://www.mdpi.com/2076-3263/8/10/365) [5.2]
> - [Detecting exoplanets through microlensing - ESO Supernova](https://supernova.eso.org/exhibition/videos/eso50microlensingexo/) [5.3]
> - [Rapid characterization of exoplanet atmospheres with the Exoplanet Transmission Spectroscopy Imager - SPIE Digital Library](https://www.spiedigitallibrary.org/journals/Journal-of-Astronomical-Telescopes-Instruments-and-Systems/volume-10/issue-4/045005/Rapid-characterization-of-exoplanet-atmospheres-with-the-Exoplanet-Transmission-Spectroscopy/10.1117/1.JATIS.10.4.045005.full) [6.3]
> - [Exoplanet Detection Methods - Penn State Research Database](https://pure.psu.edu/en/publications/exoplanet-detection-methods) [7.1]
> - [Analysis of Extra-Planets Searching and Detection Approaches: Radial Velocity, Transition and Gravitational Microlensing - SciTePress](https://www.scitepress.org/Papers/2025/138158/138158.pdf) [7.2]

> [!related-topics-to-consider]
> - [[Exoplanet]]
> - [[Transit Method]]
> - [[Radial Velocity Method]]
> - [[Direct Imaging]]
> - [[Gravitational Microlensing]]
> - [[Adaptive Optics]]
> - [[Coronagraphy]]
> - [[Doppler Spectroscopy]]
> - [[Light Curve]]
> - [[Transmission Spectroscopy]]
> - [[Habitable Zone]]
> - [[Biosignatures]]
> - [[James Webb Space Telescope (JWST)]]
> - [[Kepler Space Telescope]]
> - [[TESS (Transiting Exoplanet Survey Satellite)]]
> - [[Planet Formation]]