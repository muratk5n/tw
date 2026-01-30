# Experiment to Test Elastic Solid / Aether Theory

### Experiment 1

Double-slit, same field, different detector microstructure

* Illuminate a double-slit with a highly stable monochromatic beam
  (laser) attenuated so detection events are rare (so pattern builds
  up dot-by-dot).

* Use two detector types in identical geometry and flux:

  1. A continuous absorber / imaging plane (thick photochemical
  emulsion or CCD with many atoms per pixel).
  
  2. A sparse, strongly discrete detector: e.g., an array of
  individually addressable trapped atoms/ions or well-spaced quantum
  dots (where inter-absorber spacing is comparable to or larger than
  atomic dimensions).
  
* Keep everything else identical (wavelength, slit separation, exposure time).

Why

* The paper argues the interference/dot accumulation arises because a
  continuous EM field excites discrete atoms according to a local
  excitation probability (Monte-Carlo model shown in the doc). The
  detection statistics should therefore depend on the *microscopic*
  characteristics of the detector (atomic spacing, excitation
  cross-section, lifetime, exposure time) used in the accumulation
  model.

Predictions

* Classical-field + discrete-matter theory: The fine-grained
  (single-event) accumulation pattern — e.g., variance of counts per
  fringe, correlation of inter-dot spacing — will vary with detector
  discreteness (sparser detectors show different shot patterns even
  when normalized by average intensity). Timing dependence
  (exposure/τ) affects the per-atom excitation probability and
  therefore dot statistics.

* Standard QED (photons): When flux and detector quantum efficiency
  are the same, the statistical distribution of detection events
  across the interference pattern (after normalization) should be
  independent of the detector microstructure (aside from overall
  efficiency, added noise, and spatial resolution). That is, the same
  interference probability density.

How to read results

* If normalized, high-resolution statistical features (e.g.,
  second-order spatial correlations, pixel-to-pixel variance beyond
  Poisson expectations) change systematically when swapping detector
  microstructure (beyond resolution/efficiency effects), that supports
  the document’s detector-driven mechanism. If nothing changes apart
  from trivial scaling/noise, that disfavors the classical-detector
  explanation.

Suggested parameters/apparatus

* Wavelength: 600–800 nm (easy lasers and detectors).

* Slit spacing: choose D/λ ≈ 10–50 to get multiple clear fringes.

* Detectors: scientific CCD/EMCCD (many-atom pixel) vs sparse
  quantum-dot arrays or trapped-atom fluorescence imaging. Keep
  geometric PSF equalized.

### Experiment 2

This idea disagrees with the previous idea mentioning that "real QED
already account for detector quantum efficiency variations,
atomic-level detection probabilities and material properties affecting
absorption cross-sections. 

Hence a better idea would be instead of comparing different detectors,
use one detector and testing the time-dependence prediction:

1. Fixed setup: Double-slit, single detector type, constant weak flux

2. Vary exposure time τ from very short to very long

3. Measure: Fringe visibility V as function of accumulated counts

Rashkovskiy predicts: V should decrease as V ∝ [1 - exp(-τb)]⁻¹ for  longer τ

Standard QED predicts: V constant (when normalized by total counts),
limited only by Poisson statistics

This would be a cleaner test because it isolates the claimed
τ-dependence without confounding variables from different detector
materials.

### Experiment 3

Vary exposure time / intensity at low flux; test the Born-rule/τ
dependence

* Reproduce the Monte-Carlo excitation idea: hold geometry fixed, vary
  the exposure time τ (or equivalently, the time window before reset
  of detectors) while keeping mean intensity low.

* Measure detection probability vs local field intensity at many
  positions across fringe maxima/minima.

The paper shows excitation probability P_exc = 1-exp(−I·τ) (their
`exctprop` function) and argues Born’s rule emerges for small τ
(linear regime) .

Predictions

* Classical-field + discrete-matter: Detection probability vs
  intensity will show deterministic deviations from linear (Born)
  scaling as τ increases: specifically saturation effects (P->1) in
  high-intensity/long-exposure, and nonlinear mapping that depends on
  τ.

* QED / standard Born rule: The Born rule gives detection probability
  proportional to intensity (for single-photon/low-intensity
  regimes). Saturation due to detector physics is recognized, but the
  dependence on exposure time (as an intrinsic mapping from classical
  intensity to detection clicks) beyond known detector saturation
  would be evidence for the alternative view.

Reading the results

* Demonstrate whether the observed I -> P mapping at low intensity
  deviates from the linear Born expectation in a way explained only by
  detector saturation (known detector models) or requires a new
  τ-dependent fundamental model.

Intensities down to single-photon equivalent rates; variable exposure
windows 10 ns to seconds; use detectors with well-known dead-time and
dynamic range.

