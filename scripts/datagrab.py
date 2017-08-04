import os
import subprocess
import numpy as np
import pandas as pd
from sys import version_info

def main():
    """ main """

    nam_src = 'https://nomads.ncdc.noaa.gov/data/meso-eta-hi/'
    model = 'nam_218'   # model

    date = '20170701'
    time_init = '0000'

    time_forecast_1 = 000
    time_forecast_2 = 006
    
    #date = raw_input("Enter 8-digit date (e.g. 20170701): ")  
    #time_init = raw_input("Enter 4-digit initialization time (e.g. 1800): ") 

    #time_forecast_1 = raw_input("Enter 3-digit forecast hour (e.g. 001): ")
    #time_forecast_2 = raw_input("Enter 3-digit forecast hour (e.g. 083): ")

    for i in range(int(time_forecast_1), int(time_forecast_2)+1):
        time_forecast = str(i).zfill(3)
        date_month = date[:len(date)-2]
        
        filetag = "%s_%s_%s_%s" % (model, date, time_init, time_forecast)

        url="%s/%s/%s/%s.grb2" % (nam_src, date_month, date, filetag)
        wget_cmd = "wget %s" % (url)
        subprocess.call(wget_cmd, shell=True)

if __name__ == '__main__':
    main()
