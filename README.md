# ZSM5 — TOSCA methanol and 1-propanol adsorption experiment

TOSCA INS analysis for **RB 2620468**, using highly siliceous H-ZSM-5 with nominal **Si/Al ≈ 140**.

## Results dashboard

➡️ **[Open the current results dashboard](DASHBOARD.md)**

The dashboard is intentionally simple: the current methanol and 1-propanol spectra, the exact gravimetric loadings, the background/can treatment used for each series, and the main experimental caveats.

## Current primary data set

### Methanol

| Sample | Loading used in current analysis | Status |
|---|---:|---|
| Low loading | **2.78 wt%** | Final second-attempt run; replaces the misaligned original 2.13 wt% measurement |
| Medium loading | **4.08 wt%** | Main run |
| High loading | **8.30 wt%** | Main run |
| Pure methanol | — | Bulk reference |

The original **2.13 wt% methanol** measurement remains useful for diagnosing the beam-positioning problem, but it is not used as the primary low-loading spectrum.

### 1-propanol

| Sample | Loading used in current analysis | Status |
|---|---:|---|
| Low loading | **1.99 wt%** | Main run |
| High loading | **7.86 wt%** | Alignment suspect; absolute amplitude should not be trusted |
| Pure 1-propanol | — | Bulk reference |

## Basic processing used on the dashboard

1. Loaded ZSM-5 spectra have the **smoothed empty-ZSM-5 spectrum** subtracted.
2. Empty-ZSM-5 smoothing uses a **5-point centered average to 500 cm⁻¹**, increasing gradually to **8 points by 4500 cm⁻¹**.
3. Pure methanol has the **empty small Al can** subtracted.
4. Pure 1-propanol currently has the **empty large Al can reference** subtracted.
5. For shape comparison, spectra are normalized to the first main low-frequency peak in **40–200 cm⁻¹**.
6. Dashboard plots show **20–1700 cm⁻¹** and use vertical offsets only for readability.

No fitted correction for variable Al-frame illumination or sample/beam overlap is applied in this first-pass dashboard.

## Important experimental caveats

The absolute intensity differences are not uniformly trustworthy between all runs.

- The original 2.13 wt% methanol can was not correctly positioned in front of the beam. A final **2.78 wt%** second attempt was measured and is now the preferred low-loading methanol spectrum.
- The **7.86 wt% 1-propanol** run appears to have suffered a similar alignment problem and may not be repeatable.
- A small Al foil frame was made for each packet. Its position in the beam varies slightly between runs, so the Al contribution is not perfectly constant.
- Separate empty Al-can measurements are therefore useful for identifying Al spectral contributions, but their absolute amplitude should not automatically be assumed to match every experimental assembly.

The normalized dashboard figures should consequently be read primarily as **spectral-shape comparisons**.

## Secondary analysis

More detailed analysis can be kept separate from the simple dashboard, including:

- run-to-run Al-can and framework residual similarity;
- old-versus-rerun methanol alignment analysis;
- possible approximate correction of the alignment-suspect propanol spectrum;
- loading-dependent band assignments;
- classical MD and MLIP comparison;
- simulated INS spectra.

This repository is a working research record rather than a finalized publication data release.
