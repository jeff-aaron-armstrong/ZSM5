# ZSM5 — TOSCA methanol and 1-propanol adsorption experiment

This repository records the analysis workflow for TOSCA inelastic neutron scattering (INS)
measurements of methanol and 1-propanol adsorbed in highly siliceous H-ZSM-5.

The experimental zeolite has a nominal Si/Al ratio of approximately **140**. The aim is to
follow how the alcohol vibrational spectrum changes with loading and, later, to compare the
experimental spectra with classical molecular dynamics and MLIP simulations.

## Repository status

This is a **working research repository**, not a finalized publication data release.
Several quantities — particularly the retained alcohol wt% — are currently provisional and
are documented explicitly below.

## Directory structure

```text
data/
  raw/          Original TOSCA data exactly as supplied
  processed/    Smoothed backgrounds, subtracted spectra, and working loading tables
figures/        Current comparison figures
scripts/        Reproducible processing and plotting scripts
notes/          Analysis decisions and caveats
```

## Raw measurements

The original files are retained unchanged in `data/raw/`.

### ZSM-5 measurements

| File | Measurement |
|---|---|
| `ZSM5140_empty.dat` | Empty H-ZSM-5, Si/Al ~140 |
| `ZSM5140_m2pc.dat` | ZSM-5 + nominal 2 wt% methanol dosing |
| `ZSM5140_m4pc.dat` | ZSM-5 + nominal 4 wt% methanol dosing |
| `ZSM5140_m8pc.dat` | ZSM-5 + high methanol dosing; experimentally treated as ~8.3 wt% anchor |
| `ZSM5140_p2pc.dat` | ZSM-5 + nominal 2 wt% 1-propanol dosing |
| `ZSM5140_p8pc.dat` | ZSM-5 + nominal 8 wt% 1-propanol dosing |

### Bulk methanol reference

| File | Measurement |
|---|---|
| `methanol.dat` | Pure/bulk methanol reference spectrum |
| `emptysmallAlcan.dat` | Empty small aluminium can used for the bulk methanol measurement |

The pure methanol measurement must **not** have the empty-zeolite spectrum subtracted from it,
because it was measured in a different sample can and contains no zeolite.

## Data format

The supplied `.dat` files contain three columns:

1. `X` — wavenumber / energy-transfer coordinate
2. `Y` — TOSCA intensity
3. `E` — uncertainty

All loaded-ZSM-5 spectra use the same X-grid as the empty-ZSM-5 run, allowing direct
point-by-point subtraction without interpolation.

## Current analysis workflow

### 1. Empty-ZSM-5 smoothing

The empty-ZSM-5 spectrum is smoothed before subtraction.

A simple moving-average scheme was chosen deliberately after comparing several methods:

- **5-point centered average up to 500 cm⁻¹**
- the effective averaging window increases gradually above 500 cm⁻¹
- it reaches **8 points at 4500 cm⁻¹**

The TOSCA grid becomes progressively coarser in wavenumber, so this naturally produces more
averaging in the high-energy/noisier region while preserving the sharper low-energy framework
features.

The final background file is:

`data/processed/ZSM5140_empty_smoothed_5to8_with_error.dat`

The uncertainty of the smoothed background is propagated from the original error column.

### 2. Background subtraction

The smoothed empty-ZSM-5 spectrum is subtracted 1:1 from every alcohol-loaded ZSM-5 spectrum.

No additional scale factor has yet been applied to the empty-zeolite background.

The bulk methanol spectrum is treated separately:

`bulk methanol - empty small Al can`

Uncertainties are propagated in quadrature.

### 3. Relative methanol loading from INS intensity

Hydrogen dominates the INS signal of methanol, so for methanol-to-methanol comparisons the
hydrogen scattering factor cancels to first order: every methanol molecule contains the same
four H atoms.

To avoid using the low-frequency adsorption/librational region itself to estimate quantity,
a working methanol amount proxy is obtained by integrating predominantly internal-mode regions:

- 1000–1800 cm⁻¹
- 2700–3100 cm⁻¹

The relative methanol signal is approximately:

`1 : 5.71 : 15.54`

for the nominal 2%, 4%, and high-loading spectra respectively.

Assuming the high-loading methanol sample is approximately **8.3 wt%**, and converting through
the methanol/zeolite mass ratio rather than simply scaling wt% linearly, the current working
retained loadings are approximately:

| Nominal label | Working retained loading |
|---|---:|
| 2 wt% MeOH | **~0.58 wt%** |
| 4 wt% MeOH | **~3.22 wt%** |
| high-loading MeOH | **8.3 wt% anchor** |

These are **provisional INS-derived estimates**, not independently measured absolute loadings.
They should eventually be cross-checked against the experimental sample/dosing mass records.

### 4. 1-propanol loading labels

The same general intensity-ratio idea was applied provisionally to the two 1-propanol spectra,
with the high-loading sample treated as an 8 wt% anchor.

Current working labels are:

| Nominal label | Working retained loading |
|---|---:|
| 2 wt% 1-propanol | **~3.89 wt%** |
| 8 wt% 1-propanol | **8.0 wt% anchor** |

This result is less secure than the methanol calibration and should be revisited before being
treated quantitatively.

### 5. Shape normalization

For comparing **spectral shapes**, the background-subtracted spectra are normalized to the
main low-frequency peak in the 40–200 cm⁻¹ region.

This is intentionally different from the loading/amount normalization above.

The plotted spectra therefore answer:

> If the dominant low-frequency peak is assigned a common height, how does the rest of the
> spectrum change with loading?

This means the relative amplitude of that normalization peak itself should not be interpreted
from the normalized figures.

### 6. Plot presentation

Current comparison figures:

- use **20–1700 cm⁻¹** as the display range
- use solid, relatively thick lines
- apply constant vertical offsets so traces do not overlap

The offsets are **only graphical** and do not modify the stored processed spectra.

For the current methanol stack the visual offsets are:

- nominal 2%: +0.00
- nominal 4%: +0.42
- high-loading / 8.3% anchor: +0.84
- bulk methanol in the bulk-comparison plot: +1.46

The pure methanol trace was deliberately shifted an additional ~0.2 relative to the earlier
version to avoid overlap.

For the current 1-propanol plot:

- lower loading: +0.00
- high loading: +0.50

## Current figures

- `01_raw_spectra_20_1700.svg` — raw experimental overview
- `02_empty_zsm5_smoothing.svg` — raw vs chosen smoothed empty-ZSM-5 background
- `03_methanol_confined_comparison.svg` — methanol-loaded ZSM-5 spectra
- `04_methanol_with_bulk_comparison.svg` — confined methanol plus corrected bulk methanol
- `05_propanol_confined_comparison.svg` — 1-propanol-loaded ZSM-5 spectra

## Reproducing the workflow

Install the minimal Python dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python scripts/01_plot_raw.py
python scripts/02_smooth_empty.py
python scripts/03_subtract_backgrounds.py
python scripts/04_estimate_relative_loading.py
python scripts/05_normalize_and_plot.py
```

## Planned next steps

The current analysis is intentionally conservative. Likely next steps include:

1. cross-check the inferred retained loadings against recorded experimental masses;
2. examine methanol and 1-propanol separately rather than comparing them directly;
3. assign loading-dependent low-frequency/librational features;
4. compare the experimental spectra with classical MD;
5. compare the one-methanol case with the MLIP trajectory currently being run;
6. generate simulated INS spectra for direct TOSCA comparison.

See `notes/analysis_log.md` for the decision history and important caveats.
