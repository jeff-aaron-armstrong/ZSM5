from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/"data"/"raw"
PROC=ROOT/"data"/"processed"

bg=np.genfromtxt(PROC/"ZSM5140_empty_smoothed_5to8_with_error.dat",delimiter=",",names=True)
x0=bg["X_cm1"]; y0=bg["smoothed_Y"]; e0=bg["smoothed_E"]

for fname in ["ZSM5140_m2pc.dat","ZSM5140_m4pc.dat","ZSM5140_m8pc.dat",
              "ZSM5140_p2pc.dat","ZSM5140_p8pc.dat"]:
    a=np.genfromtxt(RAW/fname,delimiter=",",comments="#")
    a=a[~np.isnan(a).any(axis=1)]
    x,y,e=a[:,0],a[:,1],a[:,2]
    if len(x)!=len(x0) or not np.allclose(x,x0,rtol=0,atol=1e-8):
        raise ValueError(f"X grid mismatch: {fname}")
    ys=y-y0
    es=np.sqrt(e**2+e0**2)
    np.savetxt(
        PROC/fname.replace(".dat","_minus_empty.dat"),
        np.column_stack([x,ys,es,y,e,y0,e0]),
        delimiter=",",
        header="X_cm-1,subtracted_Y,subtracted_E,loaded_raw_Y,loaded_raw_E,empty_smoothed_Y,empty_smoothed_E",
        comments=""
    )

# Pure methanol has a separate small aluminium can background.
pure=np.genfromtxt(RAW/"methanol.dat",delimiter=",",comments="#")
can=np.genfromtxt(RAW/"emptysmallAlcan.dat",delimiter=",",comments="#")
pure=pure[~np.isnan(pure).any(axis=1)]
can=can[~np.isnan(can).any(axis=1)]
xp,yp,ep=pure[:,0],pure[:,1],pure[:,2]
xc,yc,ec=can[:,0],can[:,1],can[:,2]
if len(xp)==len(xc) and np.allclose(xp,xc,rtol=0,atol=1e-8):
    yi,ei=yc,ec
else:
    yi=np.interp(xp,xc,yc); ei=np.interp(xp,xc,ec)
ys=yp-yi
es=np.sqrt(ep**2+ei**2)
np.savetxt(
    PROC/"methanol_minus_smallAlcan.dat",
    np.column_stack([xp,ys,es,yp,ep,yi,ei]),
    delimiter=",",
    header="X_cm-1,subtracted_Y,subtracted_E,pureMeOH_raw_Y,pureMeOH_raw_E,emptyAlcan_Y,emptyAlcan_E",
    comments=""
)
