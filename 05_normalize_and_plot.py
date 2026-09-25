from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
PROC=ROOT/"data"/"processed"
FIG=ROOT/"figures"

def read(path):
    return np.genfromtxt(path,delimiter=",",names=True)

def norm_peak(a,lo=40,hi=200):
    x=a["X_cm1"]; y=a["subtracted_Y"]
    m=(x>=lo)&(x<=hi)
    return x,y/y[m].max()

def style(ax,title):
    ax.set_xlim(20,1700)
    ax.set_xlabel(r"Wavenumber / cm$^{-1}$",fontsize=24)
    ax.set_ylabel("Normalized intensity + vertical offset",fontsize=24)
    ax.set_title(title,fontsize=21)
    ax.tick_params(axis="both",labelsize=19)
    ax.grid(alpha=0.10)

# Methanol
mspec={
 "2":read(PROC/"ZSM5140_m2pc_minus_empty.dat"),
 "4":read(PROC/"ZSM5140_m4pc_minus_empty.dat"),
 "8":read(PROC/"ZSM5140_m8pc_minus_empty.dat"),
}
mn={k:norm_peak(a) for k,a in mspec.items()}
labels={
 "2":"MeOH nominal 2%  (~0.58 wt%)",
 "4":"MeOH nominal 4%  (~3.22 wt%)",
 "8":"MeOH nominal 8% / anchored 8.3%  (~8.30 wt%)",
}
offsets={"2":0.0,"4":0.42,"8":0.84}

fig,ax=plt.subplots(figsize=(13.2,8.3))
for k in ("2","4","8"):
    x,y=mn[k]; m=(x>=20)&(x<=1700)
    ax.plot(x[m],y[m]+offsets[k],lw=2.5,label=labels[k])
style(ax,"Methanol-loaded ZSM-5 — low-frequency-peak-normalized comparison")
ax.legend(fontsize=14); fig.tight_layout()
fig.savefig(FIG/"03_methanol_confined_comparison.svg")

# Add bulk methanol with an additional +0.2 separation above the earlier stack.
bulk=read(PROC/"methanol_minus_smallAlcan.dat")
xb,ybn=norm_peak(bulk)
fig,ax=plt.subplots(figsize=(13.2,8.8))
for k in ("2","4","8"):
    x,y=mn[k]; m=(x>=20)&(x<=1700)
    ax.plot(x[m],y[m]+offsets[k],lw=2.5,label=labels[k])
m=(xb>=20)&(xb<=1700)
ax.plot(xb[m],ybn[m]+1.46,lw=2.5,label="Pure MeOH (small Al can subtracted, scaled)")
style(ax,"Methanol-loaded ZSM-5 compared with bulk methanol")
ax.legend(fontsize=14); fig.tight_layout()
fig.savefig(FIG/"04_methanol_with_bulk_comparison.svg")

# 1-propanol
pspec={
 "2":read(PROC/"ZSM5140_p2pc_minus_empty.dat"),
 "8":read(PROC/"ZSM5140_p8pc_minus_empty.dat"),
}
pn={k:norm_peak(a) for k,a in pspec.items()}
plabels={
 "2":"1-propanol nominal 2%  (~3.89 wt%)",
 "8":"1-propanol nominal 8% / anchored 8.0%  (~8.00 wt%)",
}
poff={"2":0.0,"8":0.50}
fig,ax=plt.subplots(figsize=(13.2,8.3))
for k in ("2","8"):
    x,y=pn[k]; m=(x>=20)&(x<=1700)
    ax.plot(x[m],y[m]+poff[k],lw=2.5,label=plabels[k])
style(ax,"1-propanol-loaded ZSM-5 — low-frequency-peak-normalized comparison")
ax.legend(fontsize=14); fig.tight_layout()
fig.savefig(FIG/"05_propanol_confined_comparison.svg")
