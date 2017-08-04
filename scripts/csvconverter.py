""" script to extract parameter value data from grb2 files """
import os
import subprocess
import numpy as np
import pandas as pd

def main():
    """ main """
    wgrib2 = '~/MESO/grib2/wgrib2/wgrib2 ' # location of your wgrib2 tool

    parameter = 'TMP'       # parameter
    height = '50'          # millibar

    model = 'nam_218'   # model
    date = '20170701'   # date --- year: 2017, month: 07, day: 01
    time_init = '0000'   # initialization time

    time_forecast_1 = '000'
    time_forecast_2 = '003'

    #parameter = raw_input("Enter parameter code (e.g. TMP): ")  
    #height = raw_input("Enter height in mb (e.g. 50): ")
    
    #date = raw_input("Enter 8-digit date (e.g. 20170701): ")  
    #time_init = raw_input("Enter 4-digit initialization time (e.g. 1800): ") 

    #time_forecast_1 = raw_input("Enter 3-digit forecast hour (e.g. 001): ")
    #time_forecast_2 = raw_input("Enter 3-digit forecast hour (e.g. 083): ")

    for i in range(int(time_forecast_1), int(time_forecast_2)+1):
        time_forecast = str(i).zfill(3)
        filetag = "%s_%s_%s_%s" % (model, date, time_init, time_forecast)
        csvfile = "%s_%s_%s_mb.csv" % (filetag, parameter, height)
        
        # full command
        wgrib2_cmd = "%s %s.grb2 -match \":%s:%s mb:\" -csv %s" % (wgrib2, filetag, parameter, height, csvfile)
        # python3 wgrib2_cmd = "{} {}.grb2 -match \":{}:{} mb:\" -csv {}".format(wgrib2, filetag, parameter, height, csvfile)
        subprocess.call(wgrib2_cmd, shell=True)

    datfile = "%s_%s_mb_%s_%s_%s_%s.dat" % (parameter, height, date, time_init, time_forecast_1, time_forecast_2)
    writefile = open(datfile,"wb")

    for i in range(int(time_forecast_1), int(time_forecast_2)):
        time_forecast = str(i).zfill(3)
        filetag = "%s_%s_%s_%s" % (model, date, time_init, time_forecast)
        csvfile = "%s_%s_%s_mb.csv" % (filetag, parameter, height)
        
        arr = np.genfromtxt(open(csvfile, "rb"), dtype='str', delimiter=",")
        var = arr[:,arr.shape[1] - 1]
        print(var)

        if i==int(time_forecast_1):
            nam_dataframe = pd.read_csv(csvfile, names=['tinit', 'tfcst', 'param', 'mb', 'lat', 'long', 'val'])
        
            keygen = nam_dataframe.loc[:,['lat','long']]
            #print keygen
            keyfile = open('key.dat',"w")
            keygen.to_csv(keyfile, index=True, mode='a')
        
        np.savetxt(writefile, var, fmt='%s', newline=",")
        writefile.write(b'\n')
        os.remove(csvfile)

    writefile.close()

if __name__ == '__main__':
    main()


