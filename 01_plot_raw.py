from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
FIG = ROOT / "figures"

files = [
    ("ZSM5140_empty.dat", "Empty ZSM-5"),
    ("ZSM5140_m2pc.dat", "MeOH nominal 2%"),
    ("ZSM5140_m4pc.dat", "MeOH nominal 4%"),
    ("ZSM5140_m8pc.dat", "MeOH nominal 8%"),
    ("ZSM5140_p2pc.dat", "1-propanol nominal 2%"),
    ("ZSM5140_p8pc.dat", "1-propanol nominal 8%"),
    ("methanol.dat", "Pure methanol"),
]

fig, ax = plt.subplots(figsize=(13.2, 8))
for fname, label in files:
    a = np.genfromtxt(RAW / fname, delimiter=",", comments="#")
    a = a[~np.isnan(a).any(axis=1)]
    m = (a[:,0] >= 20) & (a[:,0] <= 1700)
    ax.plot(a[m,0], a[m,1], lw=1.7, label=label)

ax.set_xlim(20, 1700)
ax.set_xlabel(r"Wavenumber / cm$^{-1}$", fontsize=24)
ax.set_ylabel("Raw TOSCA intensity", fontsize=24)
ax.set_title("Raw TOSCA spectra", fontsize=21)
ax.tick_params(axis="both", labelsize=19)
ax.grid(alpha=0.10)
ax.legend(fontsize=13)
fig.tight_layout()
fig.savefig(FIG / "01_raw_spectra_20_1700.svg")
