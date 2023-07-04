#! /usr/env/python 

urls = [
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/AER/LBLRTM-12-8/rad-irf/r1i1p1f1/Efx/rld/gn/v20190514/rld_Efx_LBLRTM-12-8_rad-irf_r1i1p1f1_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/AER/LBLRTM-12-8/rad-irf/r1i1p1f1/Efx/rlu/gn/v20190514/rlu_Efx_LBLRTM-12-8_rad-irf_r1i1p1f1_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/AER/LBLRTM-12-8/rad-irf/r1i1p1f1/Efx/rsd/gn/v20190514/rsd_Efx_LBLRTM-12-8_rad-irf_r1i1p1f1_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/AER/LBLRTM-12-8/rad-irf/r1i1p1f1/Efx/rsu/gn/v20190514/rsu_Efx_LBLRTM-12-8_rad-irf_r1i1p1f1_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/AER/LBLRTM-12-8/rad-irf/r1i1p1f2/Efx/rlu/gn/v20190517/rlu_Efx_LBLRTM-12-8_rad-irf_r1i1p1f2_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/AER/LBLRTM-12-8/rad-irf/r1i1p1f2/Efx/rld/gn/v20190517/rld_Efx_LBLRTM-12-8_rad-irf_r1i1p1f2_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/AER/LBLRTM-12-8/rad-irf/r1i1p1f3/Efx/rld/gn/v20190516/rld_Efx_LBLRTM-12-8_rad-irf_r1i1p1f3_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/AER/LBLRTM-12-8/rad-irf/r1i1p1f3/Efx/rlu/gn/v20190516/rlu_Efx_LBLRTM-12-8_rad-irf_r1i1p1f3_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/UHH/ARTS-2-3/rad-irf/r1i1p1f1/Efx/rld/gn/v20190620/rld_Efx_ARTS-2-3_rad-irf_r1i1p1f1_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/UHH/ARTS-2-3/rad-irf/r1i1p1f1/Efx/rlu/gn/v20190620/rlu_Efx_ARTS-2-3_rad-irf_r1i1p1f1_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/UHH/ARTS-2-3/rad-irf/r1i1p1f2/Efx/rld/gn/v20190620/rld_Efx_ARTS-2-3_rad-irf_r1i1p1f2_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/UHH/ARTS-2-3/rad-irf/r1i1p1f2/Efx/rlu/gn/v20190620/rlu_Efx_ARTS-2-3_rad-irf_r1i1p1f2_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/UHH/ARTS-2-3/rad-irf/r1i1p1f3/Efx/rld/gn/v20190620/rld_Efx_ARTS-2-3_rad-irf_r1i1p1f3_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/UHH/ARTS-2-3/rad-irf/r1i1p1f3/Efx/rlu/gn/v20190620/rlu_Efx_ARTS-2-3_rad-irf_r1i1p1f3_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/UHH/ARTS-2-3/rad-irf/r1i1p2f1/Efx/rld/gn/v20190620/rld_Efx_ARTS-2-3_rad-irf_r1i1p2f1_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/UHH/ARTS-2-3/rad-irf/r1i1p2f1/Efx/rlu/gn/v20190620/rlu_Efx_ARTS-2-3_rad-irf_r1i1p2f1_gn.nc",

"http://vesg.ipsl.upmc.fr/thredds/fileServer/cmip6/RFMIP/IPSL/4AOP-v1-5/rad-irf/r1i1p1f1/Efx/rld/gn/v20200611/rld_Efx_4AOP-v1-5_rad-irf_r1i1p1f1_gn.nc",
"http://vesg.ipsl.upmc.fr/thredds/fileServer/cmip6/RFMIP/IPSL/4AOP-v1-5/rad-irf/r1i1p1f1/Efx/rlu/gn/v20200611/rlu_Efx_4AOP-v1-5_rad-irf_r1i1p1f1_gn.nc",   

"http://vesg.ipsl.upmc.fr/thredds/fileServer/cmip6/RFMIP/IPSL/4AOP-v1-5/rad-irf/r1i1p1f2/Efx/rld/gn/v20200611/rld_Efx_4AOP-v1-5_rad-irf_r1i1p1f2_gn.nc",
"http://vesg.ipsl.upmc.fr/thredds/fileServer/cmip6/RFMIP/IPSL/4AOP-v1-5/rad-irf/r1i1p1f2/Efx/rlu/gn/v20200611/rlu_Efx_4AOP-v1-5_rad-irf_r1i1p1f2_gn.nc",

"http://vesg.ipsl.upmc.fr/thredds/fileServer/cmip6/RFMIP/IPSL/4AOP-v1-5/rad-irf/r1i1p1f3/Efx/rld/gn/v20200611/rld_Efx_4AOP-v1-5_rad-irf_r1i1p1f3_gn.nc",
"http://vesg.ipsl.upmc.fr/thredds/fileServer/cmip6/RFMIP/IPSL/4AOP-v1-5/rad-irf/r1i1p1f3/Efx/rlu/gn/v20200611/rlu_Efx_4AOP-v1-5_rad-irf_r1i1p1f3_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p2f2/Efx/rld/gn/v20190605/rld_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p2f2_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p2f2/Efx/rlu/gn/v20190605/rlu_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p2f2_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p2f2/Efx/rsu/gn/v20190605/rsu_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p2f2_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p2f2/Efx/rsd/gn/v20190605/rsd_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p2f2_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p2f3/Efx/rld/gn/v20190417/rld_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p2f3_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p2f3/Efx/rlu/gn/v20190417/rlu_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p2f3_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p2f3/Efx/rsu/gn/v20190417/rsu_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p2f3_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p2f3/Efx/rsd/gn/v20190417/rsd_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p2f3_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p3f2/Efx/rld/gn/v20191031/rld_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p3f2_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p3f2/Efx/rlu/gn/v20191031/rlu_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p3f2_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p3f2/Efx/rsd/gn/v20191031/rsd_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p3f2_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p3f2/Efx/rsu/gn/v20191031/rsu_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p3f2_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p3f3/Efx/rld/gn/v20191030/rld_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p3f3_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p3f3/Efx/rlu/gn/v20191030/rlu_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p3f3_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p3f3/Efx/rsd/gn/v20191030/rsd_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p3f3_gn.nc",
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p3f3/Efx/rsu/gn/v20191030/rsu_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p3f3_gn.nc",

"http://crd-esgf-drc.ec.gc.ca/thredds/fileServer/esgG_dataroot/AR6/CMIP6/RFMIP/CCCma/CanESM5/rad-irf/r1i1p2f2/Efx/rld/gn/v20190429/rld_Efx_CanESM5_rad-irf_r1i1p2f2_gn.nc", 
"http://crd-esgf-drc.ec.gc.ca/thredds/fileServer/esgG_dataroot/AR6/CMIP6/RFMIP/CCCma/CanESM5/rad-irf/r1i1p2f2/Efx/rlu/gn/v20190429/rlu_Efx_CanESM5_rad-irf_r1i1p2f2_gn.nc", 
"http://crd-esgf-drc.ec.gc.ca/thredds/fileServer/esgG_dataroot/AR6/CMIP6/RFMIP/CCCma/CanESM5/rad-irf/r1i1p2f2/Efx/rsd/gn/v20190429/rsd_Efx_CanESM5_rad-irf_r1i1p2f2_gn.nc", 
"http://crd-esgf-drc.ec.gc.ca/thredds/fileServer/esgG_dataroot/AR6/CMIP6/RFMIP/CCCma/CanESM5/rad-irf/r1i1p2f2/Efx/rsu/gn/v20190429/rsu_Efx_CanESM5_rad-irf_r1i1p2f2_gn.nc",

"https://dpesgf03.nccs.nasa.gov/thredds/fileServer/CMIP6/RFMIP/NASA-GISS/GISS-E2-1-G/rad-irf/r1i1p1f1/Efx/rld/gn/v20191230/rld_Efx_GISS-E2-1-G_rad-irf_r1i1p1f1_gn.nc", 
"https://dpesgf03.nccs.nasa.gov/thredds/fileServer/CMIP6/RFMIP/NASA-GISS/GISS-E2-1-G/rad-irf/r1i1p1f1/Efx/rlu/gn/v20191230/rlu_Efx_GISS-E2-1-G_rad-irf_r1i1p1f1_gn.nc", 
"https://dpesgf03.nccs.nasa.gov/thredds/fileServer/CMIP6/RFMIP/NASA-GISS/GISS-E2-1-G/rad-irf/r1i1p1f1/Efx/rsu/gn/v20191230/rsu_Efx_GISS-E2-1-G_rad-irf_r1i1p1f1_gn.nc", 
"https://dpesgf03.nccs.nasa.gov/thredds/fileServer/CMIP6/RFMIP/NASA-GISS/GISS-E2-1-G/rad-irf/r1i1p1f1/Efx/rsd/gn/v20191230/rsd_Efx_GISS-E2-1-G_rad-irf_r1i1p1f1_gn.nc",

"https://dpesgf03.nccs.nasa.gov/thredds/fileServer/CMIP6/RFMIP/NASA-GISS/GISS-E3-G/rad-irf/r1i1p1f1/Efx/rld/gn/v20191230/rld_Efx_GISS-E3-G_rad-irf_r1i1p1f1_gn.nc", 
"https://dpesgf03.nccs.nasa.gov/thredds/fileServer/CMIP6/RFMIP/NASA-GISS/GISS-E3-G/rad-irf/r1i1p1f1/Efx/rlu/gn/v20191230/rlu_Efx_GISS-E3-G_rad-irf_r1i1p1f1_gn.nc", 
"https://dpesgf03.nccs.nasa.gov/thredds/fileServer/CMIP6/RFMIP/NASA-GISS/GISS-E3-G/rad-irf/r1i1p1f1/Efx/rsu/gn/v20191230/rsu_Efx_GISS-E3-G_rad-irf_r1i1p1f1_gn.nc", 
"https://dpesgf03.nccs.nasa.gov/thredds/fileServer/CMIP6/RFMIP/NASA-GISS/GISS-E3-G/rad-irf/r1i1p1f1/Efx/rsd/gn/v20191230/rsd_Efx_GISS-E3-G_rad-irf_r1i1p1f1_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/AER/RRTMG-LW-4-91/rad-irf/r1i1p1f1/Efx/rld/gn/v20200110/rld_Efx_RRTMG-LW-4-91_rad-irf_r1i1p1f1_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/AER/RRTMG-LW-4-91/rad-irf/r1i1p1f1/Efx/rlu/gn/v20200110/rlu_Efx_RRTMG-LW-4-91_rad-irf_r1i1p1f1_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/AER/RRTMG-SW-4-02/rad-irf/r1i1p1f1/Efx/rsd/gn/v20200110/rsd_Efx_RRTMG-SW-4-02_rad-irf_r1i1p1f1_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/AER/RRTMG-SW-4-02/rad-irf/r1i1p1f1/Efx/rsu/gn/v20200110/rsu_Efx_RRTMG-SW-4-02_rad-irf_r1i1p1f1_gn.nc",

"https://esgdata.gfdl.noaa.gov/thredds/fileServer/gfdl_dataroot4/RFMIP/NOAA-GFDL/GFDL-CM4/rad-irf/r1i1p1f2/Efx/rld/gn/v20180701/rld_Efx_GFDL-CM4_rad-irf_r1i1p1f2_gn.nc",
"https://esgdata.gfdl.noaa.gov/thredds/fileServer/gfdl_dataroot4/RFMIP/NOAA-GFDL/GFDL-CM4/rad-irf/r1i1p1f2/Efx/rlu/gn/v20180701/rlu_Efx_GFDL-CM4_rad-irf_r1i1p1f2_gn.nc", 
"https://esgdata.gfdl.noaa.gov/thredds/fileServer/gfdl_dataroot4/RFMIP/NOAA-GFDL/GFDL-CM4/rad-irf/r1i1p1f2/Efx/rsu/gn/v20180701/rsu_Efx_GFDL-CM4_rad-irf_r1i1p1f2_gn.nc", 
"https://esgdata.gfdl.noaa.gov/thredds/fileServer/gfdl_dataroot4/RFMIP/NOAA-GFDL/GFDL-CM4/rad-irf/r1i1p1f2/Efx/rsd/gn/v20180701/rsd_Efx_GFDL-CM4_rad-irf_r1i1p1f2_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/RTE-RRTMGP-Consortium/RTE-RRTMGP-181204/rad-irf/r1i1p1f1/Efx/rld/gn/v20191007/rld_Efx_RTE-RRTMGP-181204_rad-irf_r1i1p1f1_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/RTE-RRTMGP-Consortium/RTE-RRTMGP-181204/rad-irf/r1i1p1f1/Efx/rlu/gn/v20191007/rlu_Efx_RTE-RRTMGP-181204_rad-irf_r1i1p1f1_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/RTE-RRTMGP-Consortium/RTE-RRTMGP-181204/rad-irf/r1i1p1f1/Efx/rsd/gn/v20191007/rsd_Efx_RTE-RRTMGP-181204_rad-irf_r1i1p1f1_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/RTE-RRTMGP-Consortium/RTE-RRTMGP-181204/rad-irf/r1i1p1f1/Efx/rsu/gn/v20191007/rsu_Efx_RTE-RRTMGP-181204_rad-irf_r1i1p1f1_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p1f2/Efx/rld/gn/v20190605/rld_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p1f2_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p1f2/Efx/rlu/gn/v20190605/rlu_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p1f2_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p1f2/Efx/rsd/gn/v20190605/rsd_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p1f2_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p1f2/Efx/rsu/gn/v20190605/rsu_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p1f2_gn.nc",

"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p1f3/Efx/rld/gn/v20190417/rld_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p1f3_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p1f3/Efx/rlu/gn/v20190417/rlu_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p1f3_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p1f3/Efx/rsd/gn/v20190417/rsd_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p1f3_gn.nc", 
"http://esgf3.dkrz.de/thredds/fileServer/cmip6/RFMIP/MOHC/HadGEM3-GC31-LL/rad-irf/r1i1p1f3/Efx/rsu/gn/v20190417/rsu_Efx_HadGEM3-GC31-LL_rad-irf_r1i1p1f3_gn.nc",

"http://aims3.llnl.gov/thredds/fileServer/user_pub_work/input4MIPs/CMIP6/RFMIP/UColorado/UColorado-RFMIP-1-2/atmos/fx/multiple/none/v20190401/multiple_input4MIPs_radiation_RFMIP_UColorado-RFMIP-1-2_none.nc",
]

import pooch 
from pathlib import Path 

data_dir = "esgf-data"
with open("registry.txt", "w") as registry:
  for u in urls: 
    fname=Path(u).parts[-1]
    # Download each data file to the specified directory
    path = pooch.retrieve(
        url=u, known_hash=None, fname=fname, path=data_dir
    )
    # Add the name, hash, and url of the file to the new registry file
    registry.write(
        f"{fname} {pooch.file_hash(path)} {u}\n"
    )
