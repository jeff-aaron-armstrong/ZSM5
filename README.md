# ZSM5 — TOSCA methanol and 1-propanol adsorption experiment

This repository records the analysis workflow for TOSCA inelastic neutron scattering (INS) measurements of methanol and 1-propanol adsorbed in highly siliceous H-ZSM-5.

The experimental zeolite has a nominal Si/Al ratio of approximately **140**. The aim is to follow how the alcohol vibrational spectrum changes with loading and, later, to compare the experimental spectra with classical molecular dynamics and MLIP simulations.

## Repository status

This is a **working research repository**, not a finalized publication data release. Several quantities — particularly the retained alcohol wt% — are currently provisional and are documented explicitly below.

## Measurements

The experiment contains:

- empty H-ZSM-5, Si/Al ~140
- ZSM-5 + nominal 2 wt% methanol
- ZSM-5 + nominal 4 wt% methanol
- ZSM-5 + high methanol loading, treated as an **8.3 wt% anchor**
- ZSM-5 + nominal 2 wt% 1-propanol
- ZSM-5 + nominal 8 wt% 1-propanol
- a separate pure/bulk methanol spectrum
- an empty small aluminium can for correcting the bulk methanol run

The pure methanol measurement was made in a different can and contains no zeolite, so the empty-ZSM-5 spectrum is **not** subtracted from it.

## Data format

The supplied TOSCA data files contain three columns:

1. X — wavenumber / energy-transfer coordinate
2. Y — TOSCA intensity
3. E — uncertainty

The loaded-ZSM-5 and empty-ZSM-5 files share the same X-grid, allowing direct point-by-point subtraction without interpolation.

## Current processing workflow

### 1. Empty-ZSM-5 smoothing

The empty-ZSM-5 spectrum is smoothed before subtraction.

The current chosen rule is:

- **5-point centered moving average up to 500 cm⁻¹**
- the effective window then increases gradually
- it reaches **8 points at 4500 cm⁻¹**

This was chosen because the TOSCA grid becomes progressively coarser in wavenumber. It preserves sharper low-energy framework structure while averaging the noisier high-energy region more strongly.

### 2. Background subtraction

The smoothed empty-ZSM-5 spectrum is subtracted 1:1 from each alcohol-loaded ZSM-5 spectrum.

No fitted multiplicative background factor is currently used.

The bulk methanol spectrum is treated separately as:

**bulk methanol − empty small Al can**

Uncertainties are propagated in quadrature.

### 3. Relative methanol loading from INS intensity

Hydrogen dominates the INS signal of methanol. For methanol-to-methanol comparisons, the common hydrogen-count / scattering-cross-section factor therefore cancels to first order because every methanol molecule contains the same four H atoms.

To avoid using the low-frequency adsorption/librational region itself to estimate quantity, a working methanol amount proxy is obtained by integrating predominantly internal-mode regions:

- 1000–1800 cm⁻¹
- 2700–3100 cm⁻¹

The relative methanol signal is approximately:

**1 : 5.71 : 15.54**

for the nominal 2%, 4%, and high-loading spectra respectively.

Assuming the highest-loading methanol sample is approximately **8.3 wt%**, and converting through the methanol/zeolite mass ratio rather than scaling wt% linearly, the current working retained loadings are:

| Nominal label | Working retained loading |
|---|---:|
| 2 wt% MeOH | **~0.58 wt%** |
| 4 wt% MeOH | **~3.22 wt%** |
| high-loading MeOH | **8.3 wt% anchor** |

These are **provisional INS-derived estimates**, not independently measured absolute loadings. They should later be cross-checked against the experimental sample/dosing mass records.

### 4. 1-propanol working labels

A provisional analogous treatment currently gives:

| Nominal label | Working retained loading |
|---|---:|
| 2 wt% 1-propanol | **~3.89 wt%** |
| 8 wt% 1-propanol | **8.0 wt% anchor** |

This calibration is less secure than the methanol calibration and should be revisited before being treated quantitatively.

### 5. Shape normalization

For comparing **spectral shapes**, the background-subtracted spectra are normalized to the main low-frequency peak in the **40–200 cm⁻¹** region.

This is deliberately different from the loading/amount normalization above.

The normalized plots therefore answer:

> If the dominant low-frequency peak is assigned a common height, how does the rest of the spectrum change with loading?

The relative amplitude of that normalization peak itself should therefore not be interpreted from the normalized figures.

### 6. Plotting conventions

Current comparison figures use:

- **20–1700 cm⁻¹** as the display range
- thick solid lines
- large axis, tick, and legend text
- constant vertical offsets so traces do not overlap

These offsets are **graphical only** and do not modify the stored spectra.

Current methanol visual offsets:

- nominal 2%: +0.00
- nominal 4%: +0.42
- high-loading / 8.3% anchor: +0.84
- bulk methanol in the bulk-comparison plot: +1.46

The bulk methanol trace was shifted an additional ~0.2 relative to an earlier version to avoid overlap.

Current 1-propanol offsets:

- lower loading: +0.00
- high loading: +0.50

## Bulk methanol comparison

The pure methanol reference is corrected using its own empty small-Al-can measurement and then peak-normalized for shape comparison with the confined methanol spectra.

The bulk and confined low-frequency maxima are **not assumed to be the same physical mode** merely because they have been assigned the same normalized height.

## Important caveats

- Filename wt% values are nominal dosing targets, not necessarily retained loadings.
- The 8.3 wt% methanol value is currently used as a calibration anchor.
- Loading estimates based on integrated INS intensity assume comparable experimental scaling and should be checked against sample masses.
- Background subtraction is currently 1:1 after smoothing; no fitted background multiplier is used.
- Normalization and vertical offsets are plotting operations and must not be confused with raw or background-subtracted intensities.
- Methanol and 1-propanol are treated as **separate analysis series**.

## Next steps

1. cross-check inferred retained loadings against recorded experimental masses
2. assign loading-dependent low-frequency/librational features
3. compare the experimental spectra with classical MD
4. compare the one-methanol case with the MLIP trajectory currently running
5. generate simulated INS spectra for direct TOSCA comparison
