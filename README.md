# RFMIP_data_intake
This repo contains an Intake catalog for parameterized and line-by-line radiation models following the RFMIP protocol. The files in this repo form a catalog of the following structure:

```mermaid
graph TD;
    main-->benchmark;
    main-->parameterized;
    benchmark-->LBLRTM;
    benchmark-->ARTS;
    benchmark-->4AOP;
    benchmark-->HadGEM3;
    parameterized-->CanESM5;
    parameterized-->HadGEM3;
    parameterized-->GISS-E2-1;
    parameterized-->GISS-E3;
    parameterized-->RTE-RRTMGP;
    parameterized-->RRTMG;
    parameterized-->MIROC6;
```
