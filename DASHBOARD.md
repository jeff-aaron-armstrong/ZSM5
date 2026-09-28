# TOSCA ZSM-5 experiment — results dashboard

**RB 2620468 · H-ZSM-5, Si/Al ≈ 140**

These figures are generated directly from the processed TOSCA spectra using the **full measured data** over 20–1700 cm⁻¹. There is no spectral downsampling in the plotted curves; the JPEG files are only rasterized display versions of the full-data plots.

## Processing used here

- Loaded ZSM-5 samples: agreed smoothed empty-ZSM-5 subtraction.
- Empty-ZSM-5 smoothing: 5-point centered average to 500 cm⁻¹, gradually increasing to 8 points by 4500 cm⁻¹.
- Pure methanol: small empty Al-can subtraction.
- Pure 1-propanol: large empty Al-can subtraction currently available.
- Each background-subtracted spectrum is normalized to its first main low-frequency peak in 40–200 cm⁻¹.
- Vertical offsets are display-only.
- Display range: 20–1700 cm⁻¹.

## Methanol

**2.78 wt% · 4.08 wt% · 8.30 wt% · pure MeOH**

![Methanol in ZSM-5 compared with pure methanol](dashboard_methanol_basic_comparison.jpg)

The original 2.13 wt% methanol run is excluded from the primary comparison because the sample was not correctly positioned in the beam. The final 2.78 wt% rerun is used instead.

## 1-propanol

**1.99 wt% · 7.86 wt% (alignment suspect) · pure 1-propanol**

![1-propanol in ZSM-5 compared with pure 1-propanol](dashboard_propanol_basic_comparison.jpg)

The 7.86 wt% 1-propanol run is retained for spectral-shape comparison, but its absolute amplitude is not trusted because a smaller fraction of the sample was in the beam.

## Experimental caveats

- The small Al foil frame can contribute a slightly different amplitude from run to run.
- The old 2.13 wt% MeOH and 7.86 wt% 1-propanol runs had sample-positioning problems.
- No fitted Al or beam-overlap correction is applied on this basic dashboard.
- These normalized plots are intended primarily for **shape comparison**.

## Secondary analysis

More detailed Al-can/framework residual analysis and possible correction of the alignment-suspect 1-propanol run should remain separate from this basic dashboard so that the first view stays transparent and easy to interpret.
