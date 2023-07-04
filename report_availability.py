#! /usr/env/python 
from intake import open_catalog
import warnings
from xarray import SerializationWarning

warnings.simplefilter("ignore", SerializationWarning)

cat = open_catalog("main.yml")

print("Inputs")
try:
  x = cat.inputs.to_dask() 
except: 
    print(f'inputs not available')
    print(cat.inputs.urlpath)

for t in ["benchmark", "parameterized"]: 
    for m in list(cat[t]):
        for v in list(cat[t][m]):
            print ("Model: ", m, " variant: ", v)
            for f in list(cat[t][m][v]): 
                try: 
                    x = cat[t][m][v][f].to_dask()
                except: 
                    print(f'{m} {v} {f} not available ({cat[t][m][v][f].urlpath})')


