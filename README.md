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

You can also look on the website for accessing the data using other (maybe more efficient) methods (like netcdf).

#### About grb2 files (.grb2)
grb2 files are binary files made for storing data efficiently. Technically, we don't need convert this data into a text format to feed it into a machine learning model, but we need to be able to read the data to do a lot of what we want to do. A grb2 has two parts: 

1. the grb2 file itself
2. a inv (.inv) file that describes whats in the grb2 file; also known as a (simple) inventory

A inv file is neccessary because fully uncompressed grb2 files are 10 gb each (in csv text format). To create an inv files: 

```
wgrib2 -s filename.grb2 > filename.inv 
```

- `wgrib2` is the tool 
- `-s` tells the tool to create a simple inventory 
- `filename.grb2` is the grb2 file you want to create an inventory for
- `> filename.inv` `>` is called redirect (its a command line tool), it will redirect the output of the command before into a file called `filename.inv`

A (simple) inventory or inv file of a grb2 files describes whats in the grb2. You will get something like this:
```
16:1926853:d=2017070100:TMP:50 mb:anl:
```
- `16:` idk
- `:1926853:` idk
- `:d=2017070100:` idk
- `:TMP:` this is a parameter (in this case, it is the *temperature* parameter)
- `:50 mb:` stands for 50 milibar, indicating *temperature at 50 milibar*
- `:anl:` idk

#### Using wgrib 
In this project, we extract csv text data from grb2 using the following commands: 

1. wgrib2 filename.grb2 -match "TMP" -csv filename.csv
    
    wgrib2 IN.grb -match ":(UGRD|VGRD|TMP):(200|500) mb:"
    This selects the UGRD, VGRD and TMP fields at the 200 and 500 mb levels.
    [full documentation on wgrib -match](http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/match.html)

2. 

#### python file i/o 
Use the following as a template for performing python file i/o
```python
with open('foo') as f:
    for line in f:
        pass
```
Some tutorials and resources online may tell you to use the `readlines()` method, *DON'T!* It is extremely inefficient and will cause your computer to become unresponsive when reading large files (files larger than kilobytes which all of our data files are).