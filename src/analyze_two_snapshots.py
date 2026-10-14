# Reproduce the fixed-threshold structural analysis.
# See README.md for environment and interpretation.
from pathlib import Path
import h5py, numpy as np, pandas as pd
from scipy import ndimage
from pyproj import Proj, Transformer

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT/'data'/'raw'
FILES = {1979: RAW/'sic_psn25_197909_n07_v06r00.nc',
         2025: RAW/'sic_psn25_202509_am2_v06r00.nc'}

def load_nc(path):
    with h5py.File(path, 'r') as h:
        raw=h['cdr_seaice_conc_monthly'][0].astype(float)
        sic=np.where(raw<=100,raw*0.01,np.nan)
        surf=h['cdr_supplementary/surface_type_mask'][0]
        sic=np.where(surf==50,sic,np.nan)
        return sic,h['x'][:].astype(float),h['y'][:].astype(float)

data={y:load_nc(p) for y,p in FILES.items()}
x=data[1979][1]; y=data[1979][2]
xx,yy=np.meshgrid(x,y)
tr=Transformer.from_crs('EPSG:3411','EPSG:4326',always_xy=True)
lon,lat=tr.transform(xx,yy)
fac=Proj('EPSG:3411').get_factors(lon,lat)
cell_area=(25000.0**2)/(np.asarray(fac.meridional_scale)**2)

def metrics(sic,q):
    valid=np.isfinite(sic); b=valid&(sic>=q)
    lab,n=ndimage.label(b,structure=ndimage.generate_binary_structure(2,1))
    sizes=np.bincount(lab.ravel(),weights=cell_area.ravel())[1:] if n else np.array([])
    total=float(sizes.sum()) if len(sizes) else 0.0
    largest=float(sizes.max()) if len(sizes) else 0.0
    p=sizes/total if total else np.array([])
    return {'q':q,'n_clusters':int(n),'ice_area_million_km2':total/1e12,
            'largest_cluster_area_million_km2':largest/1e12,
            'p_inf':largest/total if total else 0.0,
            'simpson_fragmentation':float(1-(p**2).sum()) if len(p) else 0.0}

rows=[]
for year,(sic,_,_) in data.items():
    for q in [0.15,0.50,0.80,0.90,0.95,0.98]:
        r=metrics(sic,q); r['year']=year; rows.append(r)
pd.DataFrame(rows).to_csv(ROOT/'data'/'reproduced_structural_metrics.csv',index=False)
print('done')
