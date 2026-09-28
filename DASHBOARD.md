# TOSCA ZSM-5 experiment — results dashboard

**RB 2620468 · H-ZSM-5, Si/Al ≈ 140**

This page is the deliberately simple first-pass view of the experiment. It compares the alcohol-loaded ZSM-5 spectra with the corresponding pure alcohol after the relevant background/can treatment.

## Current sample set

| Series | Loading used on dashboard | Status |
|---|---:|---|
| Methanol | 2.78 wt% | Final second-attempt low-loading run; replaces the misaligned original 2.13 wt% run |
| Methanol | 4.08 wt% | Main run |
| Methanol | 8.30 wt% | Main run |
| Methanol | Pure | Bulk reference |
| 1-propanol | 1.99 wt% | Main run |
| 1-propanol | 7.86 wt% | **Alignment suspect** — absolute amplitude should not be interpreted |
| 1-propanol | Pure | Bulk reference |

## Basic processing

- **Loaded ZSM-5 samples:** subtract the smoothed empty-ZSM-5 measurement.
- Empty-ZSM-5 smoothing: 5-point centered average to 500 cm⁻¹, gradually increasing to 8 points by 4500 cm⁻¹.
- **Pure methanol:** subtract the matching small empty Al can.
- **Pure 1-propanol:** subtract the large empty Al can reference currently available.
- For the plots below, each background-subtracted spectrum is normalized to its first main low-frequency peak in **40–200 cm⁻¹**.
- Vertical offsets are only for display.
- Display range: **20–1700 cm⁻¹**.

## Methanol

Line order from bottom to top:

1. 2.78 wt% MeOH
2. 4.08 wt% MeOH
3. 8.30 wt% MeOH
4. Pure MeOH

```mermaid
xychart-beta
    title "Methanol in ZSM-5 vs pure methanol"
    x-axis "Wavenumber / cm-1" [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050, 1080, 1110, 1140, 1170, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1470, 1500, 1530, 1560, 1590, 1620, 1650, 1680]
    y-axis "Normalized intensity + offset" 0 --> 2.5
    line [0.499, 0.742, 0.984, 0.694, 0.464, 0.343, 0.280, 0.217, 0.212, 0.133, 0.184, 0.174, 0.163, 0.142, 0.126, 0.092, 0.095, 0.109, 0.110, 0.120, 0.123, 0.137, 0.146, 0.131, 0.133, 0.132, 0.131, 0.102, 0.108, 0.097, 0.083, 0.076, 0.072, 0.074, 0.076, 0.131, 0.210, 0.185, 0.226, 0.192, 0.185, 0.171, 0.180, 0.172, 0.160, 0.193, 0.230, 0.282, 0.316, 0.285, 0.267, 0.270, 0.274, 0.281, 0.262, 0.244]
    line [0.910, 1.141, 1.407, 1.157, 0.917, 0.788, 0.723, 0.658, 0.640, 0.563, 0.609, 0.603, 0.588, 0.570, 0.545, 0.515, 0.514, 0.527, 0.526, 0.534, 0.548, 0.565, 0.562, 0.560, 0.554, 0.551, 0.543, 0.529, 0.520, 0.514, 0.502, 0.491, 0.483, 0.500, 0.500, 0.567, 0.617, 0.595, 0.642, 0.604, 0.616, 0.596, 0.595, 0.583, 0.584, 0.613, 0.635, 0.704, 0.710, 0.678, 0.659, 0.670, 0.691, 0.680, 0.665, 0.665]
    line [1.345, 1.553, 1.814, 1.709, 1.651, 1.479, 1.249, 1.205, 1.184, 1.163, 1.120, 1.078, 1.058, 1.035, 1.013, 0.994, 0.983, 0.984, 0.979, 0.986, 1.014, 1.043, 1.043, 1.056, 1.029, 1.032, 1.009, 0.987, 0.973, 0.956, 0.944, 0.939, 0.936, 0.936, 0.931, 0.967, 1.107, 1.050, 1.074, 1.054, 1.068, 1.073, 1.071, 1.064, 1.063, 1.088, 1.117, 1.236, 1.218, 1.170, 1.163, 1.172, 1.177, 1.168, 1.149, 1.139]
    line [1.448, 1.813, 1.752, 2.142, 1.828, 1.862, 1.682, 1.668, 1.618, 1.598, 1.579, 1.539, 1.509, 1.498, 1.473, 1.454, 1.437, 1.417, 1.410, 1.407, 1.396, 1.388, 1.440, 1.457, 1.443, 1.481, 1.424, 1.411, 1.401, 1.387, 1.381, 1.359, 1.354, 1.365, 1.353, 1.351, 1.393, 1.428, 1.421, 1.392, 1.386, 1.402, 1.396, 1.383, 1.378, 1.409, 1.435, 1.490, 1.493, 1.479, 1.476, 1.483, 1.476, 1.469, 1.457, 1.455]
```

The old 2.13 wt% methanol measurement is excluded from the main dashboard because the can was not correctly positioned in the beam. The final 2.78 wt% second attempt is used instead.

## 1-propanol

Line order from bottom to top:

1. 1.99 wt% 1-propanol
2. 7.86 wt% 1-propanol — alignment suspect
3. Pure 1-propanol

```mermaid
xychart-beta
    title "1-propanol in ZSM-5 vs pure 1-propanol"
    x-axis "Wavenumber / cm-1" [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050, 1080, 1110, 1140, 1170, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1470, 1500, 1530, 1560, 1590, 1620, 1650, 1680]
    y-axis "Normalized intensity + offset" 0 --> 2.1
    line [0.716, 0.902, 0.702, 0.317, 0.022, -0.011, 0.216, 0.120, 0.206, 0.074, 0.248, 0.211, 0.211, 0.220, 0.212, 0.219, 0.173, 0.176, 0.150, 0.139, 0.131, 0.126, 0.122, 0.123, 0.278, 0.222, 0.218, 0.184, 0.242, 0.366, 0.274, 0.253, 0.237, 0.201, 0.223, 0.294, 0.291, 0.285, 0.261, 0.243, 0.286, 0.267, 0.333, 0.339, 0.362, 0.404, 0.385, 0.403, 0.502, 0.370, 0.371, 0.334, 0.321, 0.299, 0.284, 0.275]
    line [1.127, 1.400, 1.147, 0.806, 0.794, 0.692, 0.824, 0.823, 0.766, 0.818, 0.730, 0.670, 0.658, 0.657, 0.659, 0.701, 0.650, 0.635, 0.628, 0.639, 0.644, 0.649, 0.627, 0.626, 0.791, 0.672, 0.688, 0.692, 0.734, 0.815, 0.712, 0.720, 0.677, 0.692, 0.708, 0.705, 0.744, 0.723, 0.723, 0.705, 0.770, 0.753, 0.816, 0.788, 0.826, 0.835, 0.816, 0.859, 0.869, 0.821, 0.799, 0.805, 0.781, 0.765, 0.747, 0.745]
    line [1.700, 1.899, 1.979, 1.826, 1.728, 1.654, 1.618, 1.978, 1.640, 1.605, 1.690, 1.509, 1.451, 1.416, 1.424, 1.533, 1.393, 1.367, 1.341, 1.312, 1.298, 1.332, 1.371, 1.378, 1.570, 1.452, 1.407, 1.387, 1.460, 1.564, 1.423, 1.449, 1.403, 1.407, 1.408, 1.399, 1.476, 1.455, 1.393, 1.390, 1.470, 1.474, 1.559, 1.491, 1.596, 1.641, 1.590, 1.698, 1.735, 1.665, 1.637, 1.596, 1.577, 1.552, 1.534, 1.528]
```

The 7.86 wt% run is retained for **shape comparison**, but its absolute intensity is not trusted because a smaller fraction of the sample was in the beam.

## Interpretation status

This first dashboard intentionally makes **no fitted correction for run-to-run Al-frame amplitude or beam-overlap effects**. Those issues are being analysed separately. The main dashboard should remain a transparent view of the processed experimental spectra rather than a heavily corrected reconstruction.

### Known experimental caveats

- The original 2.13 wt% methanol run was misaligned and has been replaced in the primary comparison by the final 2.78 wt% rerun.
- The 7.86 wt% 1-propanol run is also alignment-suspect and may not be repeatable.
- The small Al foil frame varies slightly from run to run, so the Al contribution is not perfectly identical between sample measurements.
- Absolute amplitudes should therefore be interpreted cautiously; the normalized plots above are primarily **shape comparisons**.

## Next analysis layer

Secondary analysis can cover:

1. Al-can / framework residual similarity;
2. comparison of the original and rerun low-loading methanol measurements;
3. possible approximate correction of the alignment-suspect 1-propanol run;
4. band assignments and loading-dependent spectral changes;
5. comparison with classical MD and MLIP simulations.