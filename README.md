# RFMIP-rad-irf-intake

This repo a Python intake catalog for data from the [RFMIP](https://doi.org/10.5194/gmd-9-3447-2016) 
"rad-irf" experiements. 

The catalog's structure is shown below. All models provided longwave variables (rlu, rld). All of the 
parameterized models and some of the benchmark models also provided shortwave variables (rsu, rsd). The catalog 
also contains the inputs, i.e. the profiles of temperature, humidity, and gas concentrations used in the radiative 
transfer calculations. 

We have not found remote access to data from the ESGF to be robust so the catalog uses local copies of the 
data. The local data can be populated by invoking the `download_with_pooch.py` script; availablity 
can be confirmed by running `report_availability.py`

```mermaid
graph TD;
    main-->inputs;
    main-->benchmark;
    main-->parameterized;
    benchmark-->LBLRTM;
    benchmark-->ARTS;
    benchmark-->4AOP;
    benchmark-->HadGEM3 (p2, p3);
    parameterized-->CanESM5;
    parameterized-->HadGEM3 (p1);
    parameterized-->GISS-E2-1;
    parameterized-->GISS-E3;
    parameterized-->RTE-RRTMGP;
    parameterized-->RRTMG;
    parameterized-->MIROC6;
```
