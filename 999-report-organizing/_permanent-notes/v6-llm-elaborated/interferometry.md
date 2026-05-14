---
title: "Interferometry"
aliases:
  - "Interferometry"
  - "astronomical interferometry"
  - "aperture synthesis"
type: permanent-note
status: enriched
confidence: high

tags:
  - permanent-note
  - v6-llm-elaborated
  - astronomy

domain: astronomy
subdomains:
  - observational-techniques

created: 2026-05-14
updated: 2026-05-14

source-type: report-extraction
source-reports:
  - "interferometry-synthetic-seed-2026-05-14"
evidence-quality: high
extraction-method: "pkb-extractor-v1 → pipeline-v6-elaborator (two-pass)"

complexity-level: advanced-practitioner
depth-level: elaborated

parent-concept: "Observational Techniques in Astronomy"

related:
  - "[[Adaptive Optics]]"
  - "[[Radio Astronomy]]"
  - "[[Event Horizon Telescope]]"
prerequisites:
  - "[[]]"
specializes:
  - "[[]]"
broader:
  - "[[]]"
see-also:
  - "[[Adaptive Optics]]"
contrasts-with:
  - "[[]]"
contradicts:
  - "[[]]"
applies-to:
  - "[[Radio Astronomy]]"
formalizes:
  - "[[]]"
instance-of:
  - "[[Event Horizon Telescope]]"
supports:
  - "[[]]"
refines:
  - "[[]]"

review-frequency: quarterly
mastery-stage: budding
importance: medium

provenance:
  pipeline-version: "v6.0.0"
  outline-contract: "v6-outline-v1"
  elaborate-contract: "v6-elaborate-v1"
  passes: 2
---

# Interferometry

> [!definition] **Interferometry**
> Interferometry is a technique that combines electromagnetic signals from spatially separated apertures to synthesize an effective aperture equal to the array's longest baseline, achieving angular resolutions far beyond those of any individual telescope. This method excludes single-aperture imaging techniques and should not be confused with other observational methods like spectroscopy or photometry. It falls under observational techniques in astronomy.

> [!attention] **Boundary**
> This concept excludes single-aperture imaging techniques and should not be confused with other observational methods like spectroscopy or photometry.

## Core Explanation

Interferometry operates on the principle that by combining signals from multiple apertures, it can synthesize an effective aperture equivalent to the longest baseline between any two points in the array. This technique is pivotal for achieving high angular resolution and sensitivity in astronomical observations, particularly in radio astronomy where single-aperture telescopes are limited by their physical size.

In practice, interferometry arrays like the Very Large Array (VLA) or the Atacama Large Millimeter/submillimeter Array (ALMA) use this principle to capture detailed images of celestial objects. The signals from each aperture are correlated with those from others in the array, allowing for the synthesis of an image that would otherwise require a single telescope as large as the entire baseline.

The theoretical underpinnings of interferometry lie in Fourier optics and signal processing, where the spatial frequency information captured by different apertures is combined to reconstruct the full image. This process requires sophisticated algorithms to handle incomplete sampling of the Fourier plane (uv-plane) and systematic uncertainties introduced during image reconstruction.

## Practical Implications

> [!example] **Application 1 — Radio Astronomy**
> In radio astronomy, interferometry enables high-resolution imaging by combining signals from multiple telescopes spread over large distances. For instance, the Very Large Array (VLA) in New Mexico uses this technique to capture detailed images of distant galaxies and quasars that would be impossible with a single telescope due to its limited resolution.

> [!example] **Application 2 — Optical/Infrared Facilities**
> Interferometry is increasingly used in optical and infrared astronomy, where facilities like the Event Horizon Telescope (EHT) combine signals from telescopes around the world to image black holes. This technique allows for unprecedented detail in imaging distant objects that are too small or faint to be resolved by single-aperture instruments.

> [!example] **Application 3 — Gravitational-Wave Detection**
> In gravitational-wave detection, interferometers like LIGO and Virgo use the principle of combining signals from multiple detectors to pinpoint the source of gravitational waves. This application demonstrates how interferometry can be adapted beyond traditional astronomy to detect ripples in spacetime caused by cosmic events.

## Key Distinctions

> [!key-distinction] **Interferometry vs Single-Aperture Imaging**
> While single-aperture imaging relies on a single telescope for capturing images, interferometry combines signals from multiple telescopes to synthesize an effective aperture. This distinction is crucial as it allows interferometry to achieve much higher angular resolutions and sensitivities than would be possible with any individual telescope.

## Open Questions

> [!open-question] **Question**
> How can the incomplete sampling of the Fourier plane be addressed to improve image reconstruction accuracy?
>
> *What would resolve it:* Developing new algorithms or methods that better sample the uv-plane could reduce systematic uncertainties and enhance the accuracy of reconstructed images.

> [!open-question] **Question**
> What new algorithms or methods could reduce systematic uncertainties introduced by current image reconstruction techniques?
>
> *What would resolve it:* Advancements in computational imaging and machine learning may offer novel approaches to improve the fidelity of interferometric images, addressing current limitations in image reconstruction.

## Synthesis

Interferometry is crucial for achieving high-resolution imaging in modern astronomy due to its ability to synthesize large effective apertures from multiple telescopes. Despite challenges such as incomplete sampling and systematic uncertainties, it remains an indispensable technique for observing the cosmos at unprecedented detail.

## Evidence

The key claim about interferometry highlights its enabling role in high-resolution imaging across various astronomical disciplines. Through arrays like ALMA and LIGO, interferometry provides angular resolutions and sensitivities that are completely inaccessible to single-aperture instruments, underscoring its importance for advancing our understanding of the universe.

## Connections & Context

**Falls under:** [[Observational Techniques in Astronomy]]

**Sibling concepts:** [[Adaptive Optics]]

**Applies to:** [[Radio Astronomy]]

**Instance of:** [[Event Horizon Telescope]]

**Source:** [[interferometry-synthetic-seed-2026-05-14]]
