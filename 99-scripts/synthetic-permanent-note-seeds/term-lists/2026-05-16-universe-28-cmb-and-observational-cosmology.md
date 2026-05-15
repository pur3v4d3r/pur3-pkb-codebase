---
batch_name: universe-28-cmb-and-observational-cosmology
batch_date: 2026-05-16
default_domain: observational-cosmology
default_confidence: high
notes: |
  Cosmological perturbation theory, CMB physics phenomena, polarization
  observables, and major past/present/future observational missions.
---

# Batch: Universe 28 — CMB & Observational Cosmology

## Cosmological Perturbation Theory

- secondary_domains: [structure-formation, theoretical-cosmology]
- aliases: [cosmological perturbations, linear perturbation theory]
- broader: [structure-formation theory]
- related: [cmb-temperature-anisotropies, scalar-spectral-index, gauge-invariance, friedmann-equations, inflation]
- prerequisites: [general-relativity, friedmann-equations]

**definition**: Cosmological Perturbation Theory is the formalism for treating small inhomogeneities of metric, matter, and radiation fields on top of a homogeneous Friedmann-Lemaître-Robertson-Walker background, organising the perturbations into scalar, vector, and tensor modes whose evolution decouples at linear order and determining the linear evolution of large-scale structure.

**key_claim**: Cosmological Perturbation Theory is the theoretical machinery that translates inflationary initial conditions into all observable CMB anisotropies and large-scale-structure statistics; without it, the empirical match between inflation, ΛCDM parameters, and the observed power spectra cannot be computed.

**warning**: Cosmological Perturbation Theory at linear order breaks down on small scales where δρ/ρ approaches unity, requiring non-linear treatments (effective field theory of LSS, N-body simulations); treating linear perturbation theory as accurate on all scales overstates its validity in the regime where most galaxy-survey data live.

## Sachs-Wolfe Effect

- secondary_domains: [cmb-physics, gravitation]
- aliases: [Sachs–Wolfe effect, SW effect]
- broader: [CMB temperature anisotropy mechanisms]
- related: [integrated-sachs-wolfe-effect, cmb-temperature-anisotropies, gravitational-redshift, cosmological-perturbation-theory, last-scattering-surface]
- prerequisites: [general-relativity, cmb-temperature-anisotropies]

**definition**: The Sachs-Wolfe Effect is the gravitational redshift imprinted on CMB photons as they climb out of (or fall into) the gravitational potential wells of large-scale density perturbations on the last-scattering surface; on large angular scales (low multipoles ℓ < 30), the Sachs-Wolfe effect dominates the CMB temperature anisotropy spectrum.

**key_claim**: The Sachs-Wolfe Effect provides the most direct cosmological window onto the gravitational potential at recombination and is the primary mechanism by which inflationary scalar perturbations imprint themselves on the largest CMB scales; the COBE detection of CMB anisotropy was almost entirely Sachs-Wolfe in origin.

**warning**: The Sachs-Wolfe Effect on the largest scales is cosmic-variance limited because there are only ~2ℓ + 1 modes available at each multipole; treating any apparent low-multipole anomaly as physically significant must contend with the irreducible statistical uncertainty inherent to the small number of independent samples.

## Integrated Sachs-Wolfe Effect

- secondary_domains: [cmb-physics, dark-energy]
- aliases: [Integrated Sachs–Wolfe effect, ISW effect]
- broader: [CMB temperature anisotropy mechanisms]
- related: [sachs-wolfe-effect, dark-energy, cmb-temperature-anisotropies, cross-correlation, large-scale-structure]
- prerequisites: [sachs-wolfe-effect, dark-energy]

**definition**: The Integrated Sachs-Wolfe Effect is the additional CMB temperature shift accumulated by photons traversing time-evolving gravitational potentials between last scattering and the observer; in matter-dominated cosmologies the linear potentials are constant and the ISW vanishes, but in dark-energy-dominated cosmologies (like ours) potentials decay and produce a positive late-time ISW signal at large scales.

**key_claim**: The Integrated Sachs-Wolfe Effect provides an independent confirmation of dark energy through cross-correlation between CMB temperature and large-scale-structure tracers (galaxy surveys, weak-lensing maps); detection of a positive cross-correlation at the predicted amplitude is a direct empirical signature of cosmic acceleration.

**warning**: The Integrated Sachs-Wolfe Effect signal is weak and easily contaminated by systematics in the galaxy catalogues used for cross-correlation; treating ISW detections as gold-standard dark-energy evidence overstates the modest statistical significance of the cross-correlation measurements compared with type Ia supernova or BAO tests.

## Silk Damping

- secondary_domains: [cmb-physics, recombination]
- aliases: [diffusion damping, photon diffusion damping]
- broader: [CMB damping mechanisms]
- related: [acoustic-peaks, cmb-temperature-anisotropies, last-scattering-surface, recombination, baryon-acoustic-oscillations]
- prerequisites: [cmb-temperature-anisotropies, recombination]

**definition**: Silk Damping is the diffusion-driven exponential suppression of CMB temperature anisotropies on small angular scales (high multipoles ℓ ≳ 1500), arising because photons free-stream over a finite distance during recombination and wash out small-scale structure in the photon-baryon fluid; predicted by Joseph Silk in 1968 before the anisotropies themselves were detected.

**key_claim**: Silk Damping sets the small-scale cutoff of the CMB acoustic peak structure and provides a direct probe of the recombination history; the damping scale measured in the CMB power spectrum constrains the helium abundance and the number of relativistic degrees of freedom Neff at recombination.

**warning**: Silk Damping computations assume a standard recombination history; non-standard recombination scenarios (delayed or accelerated) modify the damping scale and can mimic shifts in Neff; treating the high-ℓ damping tail as a clean Neff probe without checking recombination assumptions can produce misleading inferences.

## Acoustic Peaks

- secondary_domains: [cmb-physics, baryon-acoustic-oscillations]
- aliases: [CMB acoustic peaks, Doppler peaks]
- broader: [CMB power spectrum features]
- related: [baryon-acoustic-oscillations, silk-damping, cmb-temperature-anisotropies, sound-horizon, last-scattering-surface]
- prerequisites: [cmb-temperature-anisotropies, baryon-acoustic-oscillations]

**definition**: The Acoustic Peaks are the series of harmonic peaks in the CMB temperature angular power spectrum centred near multipoles ℓ ≈ 220, 540, 810, …, arising from acoustic oscillations of the tightly coupled photon-baryon fluid frozen at recombination; the peak positions encode the angular size of the sound horizon at last scattering and hence the spatial geometry of the universe.

**key_claim**: The Acoustic Peaks' positions, heights, and ratios are the single most powerful cosmological dataset, simultaneously constraining the spatial curvature of the universe (first peak), the baryon density (peak height ratios), the matter density (peak height envelope), and the dark-energy density (overall scale).

**warning**: The Acoustic Peaks measurement is degenerate among multiple cosmological parameters and requires combination with low-redshift probes (BAO, supernovae, lensing) to break degeneracies; treating the CMB power spectrum alone as a complete cosmological measurement misrepresents the multi-probe nature of modern cosmological inference.

## CMB Polarization

- secondary_domains: [cmb-physics, recombination]
- aliases: [CMB polarisation]
- broader: [CMB observables]
- related: [b-mode-polarization, e-mode-polarization, cmb-temperature-anisotropies, primordial-gravitational-waves, reionization]
- prerequisites: [cmb-temperature-anisotropies]

**definition**: CMB Polarization is the linear polarisation pattern imprinted on the cosmic microwave background by Thomson scattering off free electrons in the presence of a quadrupolar temperature anisotropy at recombination and during reionization; it carries independent information about the optical depth, the recombination history, and primordial gravitational waves.

**key_claim**: CMB Polarization decomposes into curl-free E-modes (sourced by both scalar and tensor perturbations) and divergence-free B-modes (sourced primarily by tensor perturbations and lensing); the E-mode spectrum has been measured precisely by Planck and is consistent with ΛCDM, while the B-mode spectrum offers the cleanest probe of inflationary gravitational waves.

**warning**: CMB Polarization measurements are exquisitely sensitive to foregrounds (galactic dust and synchrotron emission) and instrumental systematics; treating polarisation maps as clean primordial signals without rigorous foreground removal has historically produced spurious detections (notably BICEP2's 2014 claim).

## B-mode Polarization

- secondary_domains: [cmb-physics, inflation]
- aliases: [B-modes, CMB B-mode polarisation]
- broader: [CMB polarization decomposition]
- related: [cmb-polarization, e-mode-polarization, primordial-gravitational-waves, tensor-to-scalar-ratio, bicep2-experiment]
- prerequisites: [cmb-polarization]

**definition**: B-mode Polarization is the divergence-free (curl-like) component of the CMB polarisation field, distinguished from E-modes by its parity-odd character; primordial B-modes can only be sourced by tensor perturbations (gravitational waves) at large angular scales, while at smaller scales B-modes arise from gravitational lensing of E-modes by intervening matter.

**key_claim**: B-mode Polarization at degree angular scales is the cleanest cosmological probe of primordial gravitational waves from inflation; a confirmed primordial B-mode detection would directly measure the energy scale of inflation and provide the long-sought "smoking gun" for the inflationary paradigm.

**warning**: B-mode Polarization detection is currently dominated by lensing B-modes at small scales; at large scales the signal is buried in galactic-dust contamination, and BICEP2's 2014 claim of a primordial detection was retracted after Planck showed the signal was almost entirely dust — treating any low-significance B-mode signal as primordial without delensing and foreground removal is empirically unreliable.

## E-mode Polarization

- secondary_domains: [cmb-physics, reionization]
- aliases: [E-modes, CMB E-mode polarisation]
- broader: [CMB polarization decomposition]
- related: [cmb-polarization, b-mode-polarization, cmb-temperature-anisotropies, reionization, optical-depth]
- prerequisites: [cmb-polarization]

**definition**: E-mode Polarization is the curl-free (gradient-like) component of the CMB polarisation field, parity-even and sourced primarily by scalar density perturbations at recombination; the E-mode angular power spectrum is correlated with the temperature spectrum and provides one of the principal cosmological probes after temperature.

**key_claim**: E-mode Polarization measurements at low multipoles directly constrain the optical depth to reionization τ, breaking the As–τ degeneracy that limits temperature-only CMB analyses; Planck's E-mode polarisation measurements have refined τ to ~0.054, anchoring the inflationary scalar amplitude.

**warning**: E-mode Polarization at the largest scales is dominated by reionization signal that is sensitive to foreground removal and large-area galactic-plane masking; treating low-ℓ polarisation measurements as systematics-free has historically led to substantial revisions in τ (the Planck 2013 vs. 2018 τ shift is a cautionary example).

## Tensor-to-Scalar Ratio

- secondary_domains: [inflation, cmb-physics]
- aliases: [r, tensor-scalar ratio]
- broader: [inflationary observables]
- related: [primordial-gravitational-waves, b-mode-polarization, scalar-spectral-index, inflation, energy-scale-of-inflation]
- prerequisites: [inflation, cmb-polarization]

**definition**: The Tensor-to-Scalar Ratio r = Pt/Ps is the ratio of the primordial tensor (gravitational-wave) power spectrum to the primordial scalar (density-perturbation) power spectrum at a fiducial pivot scale; in single-field slow-roll inflation r is directly proportional to the inflationary energy scale via r ≈ V/(1.8×10¹⁶ GeV)⁴.

**key_claim**: The Tensor-to-Scalar Ratio is the single most informative inflationary observable: a confirmed measurement would directly determine the energy scale of inflation, distinguish among competing inflaton potentials, and rule out broad classes of low-energy inflationary models.

**warning**: The Tensor-to-Scalar Ratio is currently bounded only from above (r < 0.036 at 95% CL from BICEP/Keck + Planck); claims of any specific positive value require either a future detection or extraordinary control over polarisation foregrounds, and treating r as a measured quantity rather than an upper bound misrepresents its empirical status.

## Primordial Gravitational Waves

- secondary_domains: [inflation, gravitational-waves]
- aliases: [primordial GWs, inflationary gravitational waves]
- broader: [stochastic gravitational-wave backgrounds]
- related: [b-mode-polarization, tensor-to-scalar-ratio, inflation, gravitational-wave, energy-scale-of-inflation]
- prerequisites: [inflation, gravitational-wave]

**definition**: Primordial Gravitational Waves are the stochastic background of tensor metric perturbations generated quantum-mechanically during inflation by the de Sitter-like vacuum fluctuations of the metric; they propagate freely from inflation to the present and imprint a characteristic B-mode polarisation pattern on the CMB at degree angular scales.

**key_claim**: Primordial Gravitational Waves are uniquely diagnostic of the inflationary energy scale and would, if detected, provide the only known direct empirical access to physics at scales of 10¹⁵ to 10¹⁶ GeV — far above any laboratory accelerator's reach.

**warning**: Primordial Gravitational Waves have not been detected to date, and the upper bound on their amplitude (r < 0.036) already excludes some of the simplest large-field inflationary models; treating PGWs as a confirmed prediction rather than as a falsifiable target overstates inflation's empirical status.

## Non-Gaussianity

- secondary_domains: [inflation, cmb-physics]
- aliases: [primordial non-Gaussianity, fNL]
- broader: [statistical properties of primordial perturbations]
- related: [inflation, cmb-temperature-anisotropies, bispectrum, single-field-inflation, multi-field-inflation]
- prerequisites: [cosmological-perturbation-theory, inflation]

**definition**: Non-Gaussianity is any departure of the statistical distribution of primordial cosmological perturbations from a pure Gaussian random field, characterised by higher-order n-point correlation functions (bispectrum, trispectrum) parametrised by amplitudes such as fNL; single-field slow-roll inflation predicts fNL ≪ 1, while alternative scenarios (multi-field, ekpyrotic) predict potentially larger fNL.

**key_claim**: Non-Gaussianity measurements from the CMB bispectrum (Planck) constrain the principal templates fNL^local, fNL^equilateral, and fNL^orthogonal to be consistent with zero at the |fNL| < 5–10 level, dramatically restricting the space of viable inflationary scenarios and disfavouring strongly non-Gaussian alternatives.

**warning**: Non-Gaussianity tests are highly template-dependent; current constraints assume specific functional forms of the bispectrum, and exotic scenarios with unusual squeezed-limit behaviour can evade these constraints — treating fNL bounds as a generic constraint on all inflation alternatives overstates their model-independence.

## BICEP2 Experiment

- secondary_domains: [cmb-experiment, observational-history]
- aliases: [BICEP2 telescope]
- broader: [CMB polarization experiments]
- related: [b-mode-polarization, tensor-to-scalar-ratio, primordial-gravitational-waves, planck-satellite, foreground-contamination]
- prerequisites: [cmb-polarization]

**definition**: The BICEP2 Experiment was a small-aperture CMB polarisation telescope operated at the South Pole that announced in March 2014 the detection of B-mode polarisation at degree angular scales attributed to primordial gravitational waves with r ≈ 0.20; the claim was retracted after joint analysis with Planck showed the signal was dominated by polarised galactic dust emission.

**key_claim**: The BICEP2 Experiment episode is the canonical modern cautionary tale in CMB cosmology about the dangers of foreground contamination: a confidently announced primordial detection turned into a foreground confusion within months, prompting the polarisation community to adopt much stricter multi-frequency cross-checks before declaring future detections.

**warning**: The BICEP2 Experiment story is sometimes told as evidence that CMB polarisation cosmology cannot deliver primordial GW measurements; the lesson is more nuanced — multi-frequency, multi-experiment cross-checks (BICEP/Keck + Planck + future SO/CMB-S4) are now standard practice, and the field has substantially matured rather than regressed.

## COBE Satellite

- secondary_domains: [cmb-experiment, observational-history]
- aliases: [Cosmic Background Explorer]
- broader: [CMB satellite missions]
- related: [cmb-temperature-anisotropies, cmb-blackbody-spectrum, planck-satellite, wmap, sachs-wolfe-effect]
- prerequisites: [cmb-temperature-anisotropies]

**definition**: The COBE Satellite (Cosmic Background Explorer, NASA, launched 1989) was the first satellite mission dedicated to characterising the cosmic microwave background, carrying three instruments (FIRAS, DMR, DIRBE) that respectively measured the CMB blackbody spectrum to extraordinary precision, detected CMB temperature anisotropies for the first time, and mapped diffuse infrared emission.

**key_claim**: The COBE Satellite produced two of the most cosmologically transformative results of the late twentieth century: FIRAS measured the CMB to be a near-perfect blackbody at T = 2.725 K (the most precise blackbody spectrum ever measured), and DMR detected ΔT/T ~ 10⁻⁵ anisotropies (Mather and Smoot, Nobel Prize 2006).

**warning**: The COBE Satellite's DMR anisotropies were detected only at large angular scales (≥ 7°) and could not resolve the acoustic peaks; treating COBE as having measured the CMB power spectrum overstates what was technologically possible at the time, and the full power-spectrum era required WMAP (2001) and Planck (2009).

## Simons Observatory

- secondary_domains: [cmb-experiment, future-observations]
- aliases: [SO]
- broader: [CMB ground-based experiments]
- related: [cmb-polarization, b-mode-polarization, cmb-stage-4, atacama-cosmology-telescope, advanced-actpol]
- prerequisites: [cmb-polarization]

**definition**: The Simons Observatory is a ground-based CMB experiment under construction at Cerro Toco in the Atacama Desert (5,200 m elevation), comprising one large- and three small-aperture telescopes designed to map ~40% of the sky in temperature and polarisation across six frequency bands; first light was achieved in 2024 with full operations ramping toward 2026.

**key_claim**: The Simons Observatory's design tensor-to-scalar sensitivity σ(r) ≈ 0.003 represents an order-of-magnitude improvement over current bounds and will, within its first few years, decisively test single-field large-field inflationary models such as natural inflation and certain Starobinsky variants.

**warning**: The Simons Observatory's r sensitivity assumes successful foreground separation; the real-world sensitivity will depend on how well dust and synchrotron foregrounds can be modelled at degree scales, and extrapolating design specifications to delivered constraints without that caveat overstates likely results.

## CMB Stage 4

- secondary_domains: [cmb-experiment, future-observations]
- aliases: [CMB-S4]
- broader: [CMB ground-based experiments]
- related: [simons-observatory, b-mode-polarization, primordial-gravitational-waves, tensor-to-scalar-ratio, neff]
- prerequisites: [cmb-polarization]

**definition**: CMB Stage 4 (CMB-S4) is the planned next-generation US-led ground-based CMB experiment, intended to deploy ~500,000 detectors across multiple telescope sites (Atacama and South Pole) to map the CMB with unprecedented sensitivity, targeting σ(r) ≈ 0.001 and constraints on the effective number of relativistic species Neff at the 10⁻³ level.

**key_claim**: CMB Stage 4 is designed to either detect or definitively rule out primordial gravitational waves at the energy scale of natural large-field inflation; combined with measurements of light relic species, it will provide the most stringent CMB-based constraints on inflation and on light beyond-Standard-Model physics through the 2030s.

**warning**: CMB Stage 4 funding, schedule, and final scope have undergone several revisions and remain subject to Department of Energy and National Science Foundation budget processes; treating the experiment as on a fixed schedule overstates the certainty around when (or whether at full scope) the project will deploy.

## LiteBIRD Mission

- secondary_domains: [cmb-experiment, satellite-missions]
- aliases: [LiteBIRD satellite]
- broader: [CMB satellite missions]
- related: [b-mode-polarization, primordial-gravitational-waves, cmb-stage-4, simons-observatory, planck-satellite]
- prerequisites: [cmb-polarization]

**definition**: The LiteBIRD Mission is a JAXA-led satellite project (with international partners) targeting full-sky CMB polarisation measurements across 15 frequency bands from 40 to 400 GHz, designed specifically to measure the primordial B-mode signal at large angular scales with sensitivity σ(r) ≈ 0.001; planned launch in the early 2030s.

**key_claim**: The LiteBIRD Mission's full-sky coverage from L2 makes it complementary to ground-based experiments (Simons Observatory, CMB-S4), which can only reach the degree-scale B-mode reionization peak from the ground at limited sky fractions; LiteBIRD will measure both the recombination and reionization B-mode bumps, providing a uniquely robust probe of primordial gravitational waves.

**warning**: The LiteBIRD Mission's schedule and scope, like all space missions, are subject to substantial uncertainty; treating LiteBIRD's design sensitivity as a guaranteed near-future deliverable overstates the expected timeline and the inherent risks of complex satellite hardware.

## Sunyaev-Zel'dovich Effect

- secondary_domains: [cluster-cosmology, cmb-physics]
- aliases: [SZ effect, Sunyaev–Zel'dovich effect, tSZ effect, kSZ effect]
- broader: [CMB secondary anisotropies]
- related: [cluster-cosmology, cmb-temperature-anisotropies, hot-intracluster-medium, planck-satellite, atacama-cosmology-telescope]
- prerequisites: [cmb-temperature-anisotropies]

**definition**: The Sunyaev-Zel'dovich Effect is the spectral distortion of the CMB caused by inverse Compton scattering of CMB photons off hot electrons in galaxy-cluster intracluster medium; the thermal SZ effect produces a frequency-dependent temperature decrement below 217 GHz and increment above, and the kinematic SZ effect produces a Doppler shift proportional to cluster bulk velocity.

**key_claim**: The Sunyaev-Zel'dovich Effect provides a redshift-independent cluster detection technique because the SZ surface brightness does not dim with distance like optical surface brightness; SZ-selected cluster catalogues (Planck SZ catalogue, ACT, SPT) have produced cluster cosmology constraints competitive with X-ray and optical surveys.

**warning**: The Sunyaev-Zel'dovich Effect cluster cosmology depends critically on the mass-observable relation calibration, and discrepancies between SZ-derived cluster mass and weak-lensing mass have been a persistent source of tension with primary CMB cosmology; treating SZ cluster counts as direct mass measurements without addressing this calibration overstates their reliability.

## Lyman-Alpha Forest

- secondary_domains: [intergalactic-medium, large-scale-structure]
- aliases: [Lyα forest]
- broader: [intergalactic-medium probes]
- related: [intergalactic-medium, baryon-acoustic-oscillations, neutral-hydrogen, quasar, reionization]
- prerequisites: [neutral-hydrogen, intergalactic-medium]

**definition**: The Lyman-Alpha Forest is the dense series of absorption features blueward of a quasar's Lyα emission line, produced by neutral hydrogen clouds along the line of sight at progressively higher redshifts; each absorber's redshift maps to a specific intergalactic-medium location, and the forest collectively traces the matter distribution from the quasar to the observer.

**key_claim**: The Lyman-Alpha Forest is the only cosmological probe that traces matter directly at scales ~0.1–10 Mpc and at high redshifts z ~ 2–5, providing constraints on the matter power spectrum, neutrino masses, and warm-dark-matter free-streaming scales that no other observable can match in this combined regime.

**warning**: The Lyman-Alpha Forest interpretation requires hydrodynamical simulations to model the non-linear relationship between absorber properties and the underlying matter density; treating Lyα forest constraints as model-independent overstates their robustness, and tensions between Lyα and CMB-inferred σ8 values may reflect simulation systematics rather than new physics.

## 21-cm Cosmology

- secondary_domains: [reionization, observational-cosmology]
- aliases: [21 cm cosmology, neutral hydrogen 21-cm line cosmology]
- broader: [intergalactic-medium probes]
- related: [reionization, square-kilometre-array, dark-ages, cosmic-dawn, neutral-hydrogen]
- prerequisites: [neutral-hydrogen, recombination]

**definition**: 21-cm Cosmology uses the hyperfine transition of neutral hydrogen at rest-frame wavelength 21 cm (frequency 1420 MHz) as a probe of the cosmological matter distribution from the dark ages (z ~ 200) through cosmic dawn (z ~ 30) to reionization (z ~ 6–10); the redshifted signal appears in radio bands from MHz to GHz and is targeted by interferometers such as HERA, MWA, and SKA.

**key_claim**: 21-cm Cosmology is the only known way to access the dark ages and cosmic dawn observationally; if successfully measured at the high precision targeted by SKA-Low, it would provide constraints on the matter power spectrum down to scales inaccessible to the CMB or galaxy surveys, and could detect signatures of exotic dark matter, primordial black holes, or non-standard reionization scenarios.

**warning**: 21-cm Cosmology faces extraordinarily challenging foreground subtraction (galactic synchrotron emission is ~10⁵ times brighter than the cosmological signal) and instrumental systematics; the EDGES claimed detection in 2018 of an anomalous absorption feature at z ~ 17 has not been confirmed by independent experiments and remains contested — treating any claimed 21-cm cosmological signal as established overstates the empirical situation.
