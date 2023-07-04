#! /usr/env/python 
from intake import open_catalog
from xarray import SerializationWarning
import warnings
import sys

# xarray throws many SerializationWarning due to slightly different missing values
warnings.simplefilter("ignore", SerializationWarning)


failed = False
cat = open_catalog("main.yml")

print("Inputs")
try:
  x = cat.inputs.to_dask() 
except: 
    failed = True
    print(f'inputs not available ({at.inputs.urlpath})')

for t in ["benchmark", "parameterized"]: 
    for m in list(cat[t]):
        for v in list(cat[t][m]):
            print ("Model: ", m, " variant: ", v)
            for f in list(cat[t][m][v]): 
                try: 
                    x = cat[t][m][v][f].to_dask()
                except: 
                    failed = True
                    print(f'{m} {v} {f} not available ({cat[t][m][v][f].urlpath})')

sys.exit(1) if failed else sys.exit(0)
