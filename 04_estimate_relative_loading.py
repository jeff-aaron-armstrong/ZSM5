from pathlib import Path
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
PROC=ROOT/"data"/"processed"

def read(path):
    return np.genfromtxt(path,delimiter=",",names=True)

def area(a,lo,hi):
    x=a["X_cm1"]; y=a["subtracted_Y"]
    m=(x>=lo)&(x<=hi)
    return np.trapezoid(y[m],x[m])

def infer_wt(proxy, anchor_key, anchor_wt):
    wa=anchor_wt/100.0
    qa=wa/(1-wa)
    ra=proxy[anchor_key]
    out={}
    for k,v in proxy.items():
        q=qa*(v/ra)
        out[k]=100*q/(1+q)
    return out

# Methanol: H-dominated INS amount proxy from internal-mode regions.
m={
 "2":read(PROC/"ZSM5140_m2pc_minus_empty.dat"),
 "4":read(PROC/"ZSM5140_m4pc_minus_empty.dat"),
 "8.3":read(PROC/"ZSM5140_m8pc_minus_empty.dat"),
}
proxy={k:area(a,1000,1800)+area(a,2700,3100) for k,a in m.items()}
wt=infer_wt(proxy,"8.3",8.3)

pd.DataFrame({
    "sample":["nominal 2%","nominal 4%","8.3% anchor"],
    "internal_mode_proxy":[proxy["2"],proxy["4"],proxy["8.3"]],
    "relative_to_low_sample":[1.0,proxy["4"]/proxy["2"],proxy["8.3"]/proxy["2"]],
    "approx_retained_wt_percent":[wt["2"],wt["4"],wt["8.3"]],
}).to_csv(PROC/"methanol_relative_loading_internal_mode_proxy.csv",index=False)

print("Working methanol loadings:")
for k in ("2","4","8.3"):
    print(k, wt[k])
