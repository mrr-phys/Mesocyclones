# Predicting Mesocyclones using Machine Learning Techniques

### About
This is project to test if we can predict the location of tornadoes using modern machine learning techniques.

### Getting the Data
The data we use is provided by NOAA which stores its weather data in a format called **.grb2**. You will need a tool called **wgrib2** in order to extract text data (e.g. csv) from it. You can also look on the website for accessing the data using other (maybe more efficient) methods (like netcdf).
- [wgrib2](http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/)
- [NOAA data access](https://www.ncdc.noaa.gov/data-access)
- Model datasets we are currently using:
    - [GFS](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs)
    -  [NAM](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/north-american-mesoscale-forecast-system-nam)

#### About grb2 files (.grb2)
grb2 files are binary files made for storing data efficiently. Technically, we don't need convert this data into a text format to feed it into a machine learning model, but we need the date to be human readable for our project. A grb2 has two parts: 
1. the grb2 file itself
2. a inv (.inv) file that describes whats in the grb2 file; also known as a (simple) inventory

A inv file is neccessary because fully uncompressed grb2 files are 10 gb each (in csv text format). To create an inv files: 
```
wgrib2 -s filename.grb2 > filename.inv 
```
- `wgrib2` is the tool 
- `-s` tells the tool to create a simple inventory 
- `filename.grb2` is the grb2 file you want to create an inventory for
- `> filename.inv` the `>` is called redirect (its a command line tool), it will redirect the output of the command before into a file called `filename.inv`

A (simple) inventory or inv file of a grb2 files describes whats in the grb2. You will get something like this inside the file:
```
16:1926853:d=2017070100:TMP:50 mb:anl:
```
- `:TMP:` this is a parameter (in this case, it is the *temperature* parameter)
- `:50 mb:` stands for 50 milibar, indicating *temperature at 50 milibar*
- everything else I'm not sure what it is

#### Using wgrib2 
In this project, we extract csv text data from grb2 using the following command: 

`wgrib2 filename.grb2 -match "TMP" -csv filename.csv`

> Official Help Text:
wgrib2 IN.grb -match ":(UGRD|VGRD|TMP):(200|500) mb:"
This selects the UGRD, VGRD and TMP fields at the 200 and 500 mb levels.
full documentation on [wgrib2](http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/) and [wgrib2 -match](http://www.cpc.ncep.noaa.gov/products/wesley/wgrib2/match.html)

- `wgrib2` is the tool
- `filename.grb2` is the grb2 file you want to use
- `-match "TMP` will create an inventory of the grb2 file
- `-csv filename` because the `-match` option was used earlier in the command, `-csv` option will create a csv text file that exports only temperature data (without `-match` it will export all of the data in the grb2 file into a csv text format, this file will be 10 gb or more) 

> *extra notes:* 
refer to above, what this command does it create a simple inventory of all the data is has matching the "regular expression" "TMP" and then uses that information to export only temperature (aka "TMP) data. "Regular expression" is a computer nerd term for, basically, google searching (expect regular expressions are much more powerful than a google search, google it to find out more). 

#### Python file i/o 
Use the following as a template for performing python file i/o
```python
with open('foo') as f:
    for line in f:
        pass
```
Some tutorials and resources online may tell you to use the `readlines()` method, *DON'T!* It is extremely inefficient and will cause your computer to become unresponsive when reading large files (files larger than kilobytes which all of our data files are).
