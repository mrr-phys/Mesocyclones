# Predicting Mesocyclones using Machine Learning Techniques

## About
This is project to test if we can predict the location of tornadoes using modern machine learning techniques.

## Getting the Data
The data we use is provided by NOAA which stores its weather data in a format called **.grb2**. You will need a tool called **wgrib** in order to extract text data (e.g. csv) from it. 

- [NOAA data access](https://www.ncdc.noaa.gov/data-access)
- Model datasets we are currently using:
    - [GFS](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs)
    -  [NAM](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/north-american-mesoscale-forecast-system-nam)
- [wgrib2](http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/)

#### Using wgrib 
In this project, we extract csv text data from grb2 using the following commands: 

1. wgrib2 IN.grb -match ":(UGRD|VGRD|TMP):(200|500) mb:"
    
    This selects the UGRD, VGRD and TMP fields at the 200 and 500 mb levels.

    [more help info](http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/match.html)

2. 