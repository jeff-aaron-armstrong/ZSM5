# Analysis log

## 25 September 2026 — initial TOSCA analysis milestone

### Scope

TOSCA measurements were performed for methanol and 1-propanol loaded into highly siliceous
H-ZSM-5 (nominal Si/Al ~140), together with an empty-zeolite background. A separate bulk
methanol reference was measured in a small aluminium can, for which an empty-can spectrum is
also available.

Methanol and 1-propanol are treated as **separate analysis series** from this point onward.

### Raw-data check

All experimental files were first plotted without normalization or subtraction to confirm that
they had been read correctly.

The loaded-ZSM-5 and empty-ZSM-5 files share the same X-grid.

### Empty-zeolite smoothing decision

Several smoothing approaches were explored. The adopted working background is a simple
variable-window moving average:

- 5 points through 500 cm⁻¹;
- gradually increasing thereafter;
- 8 points by 4500 cm⁻¹.

Reasoning: low-energy TOSCA points are finely sampled and contain genuine sharp framework
structure, whereas the high-energy grid is coarser and benefits from stronger averaging.

### Background subtraction

The smoothed empty zeolite is subtracted directly from:

- methanol nominal 2%
- methanol nominal 4%
- methanol high loading
- 1-propanol nominal 2%
- 1-propanol nominal 8%

The pure methanol spectrum is corrected instead using `emptysmallAlcan.dat`.

No arbitrary multiplicative background scale factor has yet been introduced.

### Methanol relative quantity estimate

Because the INS response is overwhelmingly hydrogen-sensitive, relative methanol amount can be
estimated from hydrogen-dominated integrated intensity. For methanol-to-methanol comparison,
the molecular H-count/cross-section factor is common and cancels.

A working amount proxy was calculated from internal-mode intensity in:

- 1000–1800 cm⁻¹
- 2700–3100 cm⁻¹

Relative amount:

- nominal 2%: 1.00
- nominal 4%: ~5.71
- high loading: ~15.54

Anchoring the highest methanol sample at 8.3 wt% gives provisional retained loadings:

- nominal 2% -> ~0.58 wt%
- nominal 4% -> ~3.22 wt%
- high loading -> 8.3 wt%

These numbers remain provisional until checked against the actual dosing/sample masses.

### 1-propanol quantity estimate

A provisional analogous treatment currently gives approximately:

- nominal 2% -> ~3.89 wt%
- nominal 8% -> 8.0 wt% anchor

This should be treated more cautiously and revisited.

### Shape normalization decision

For visual comparison of spectral shapes, each subtracted spectrum is divided by the height
of the main low-frequency peak found within 40–200 cm⁻¹.

This normalization is **not** the same thing as the inferred loading correction.

### Figure conventions

The current preferred plotting style is:

- x-range: 20–1700 cm⁻¹
- thicker solid lines
- large axis/tick/legend text
- constant vertical offsets to prevent overlap

Current methanol visual offsets:

- low loading: 0.00
- middle loading: 0.42
- high loading: 0.84
- pure bulk methanol: 1.46

Current propanol offsets:

- low loading: 0.00
- high loading: 0.50

These offsets have no physical meaning and are not applied to stored processed data.

### Bulk methanol

The bulk methanol reference is corrected using its own empty small-Al-can measurement.
It is then peak-normalized for shape comparison with the confined methanol spectra.

The bulk and confined low-frequency maxima are not assumed to be the same physical mode simply
because they have been assigned the same normalized height.

### Important caveats

- Filename wt% values are nominal dosing targets, not necessarily retained loadings.
- The 8.3 wt% methanol value is currently used as a calibration anchor.
- Loading estimates based on INS integrated intensity assume comparable experimental scaling and
  should be cross-checked against sample masses.
- Background subtraction is currently 1:1 after smoothing; no fitted background factor is used.
- Normalization and vertical offsets are plotting operations and must not be confused with the
  raw or background-subtracted intensities.
