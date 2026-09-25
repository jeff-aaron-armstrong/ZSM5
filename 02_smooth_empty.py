from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"

a = np.genfromtxt(RAW/"ZSM5140_empty.dat", delimiter=",", comments="#")
a = a[~np.isnan(a).any(axis=1)]
x, y, e = a[:,0], a[:,1], a[:,2]

def centered_average_and_error(y, e, n):
    ys = np.empty_like(y)
    es = np.empty_like(e)
    left = (n-1)//2
    right = n//2
    for i in range(len(y)):
        lo=max(0,i-left); hi=min(len(y),i+right+1)
        N=hi-lo
        ys[i]=np.mean(y[lo:hi])
        es[i]=np.sqrt(np.sum(e[lo:hi]**2))/N
    return ys, es

smooth={n:centered_average_and_error(y,e,n) for n in (5,6,7,8)}
n_eff=np.where(x<=500,5.0,np.where(x>=4500,8.0,5.0+3.0*(x-500.0)/4000.0))

ys=np.empty_like(y); es=np.empty_like(e)
for i,ne in enumerate(n_eff):
    if ne<=5:
        ys[i],es[i]=smooth[5][0][i],smooth[5][1][i]
    elif ne>=8:
        ys[i],es[i]=smooth[8][0][i],smooth[8][1][i]
    else:
        lo=int(np.floor(ne)); hi=int(np.ceil(ne)); w=ne-lo
        ys[i]=(1-w)*smooth[lo][0][i]+w*smooth[hi][0][i]
        es[i]=np.sqrt(((1-w)*smooth[lo][1][i])**2+(w*smooth[hi][1][i])**2)

np.savetxt(
    PROC/"ZSM5140_empty_smoothed_5to8_with_error.dat",
    np.column_stack([x,y,e,ys,es,n_eff]),
    delimiter=",",
    header="X_cm-1,raw_Y,raw_E,smoothed_Y,smoothed_E,effective_window_points",
    comments=""
)
