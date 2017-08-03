""" script to extract parameter value data from grb2 files """
import os
import subprocess
import numpy as np

def main():
    """ main """
    wgrib2 = '~/MESO/grib2/wgrib2/wgrib2 ' # location of your wgrib2 tool

    param = 'TMP'       # parameter
    hgt = '50'          # millibar

    model = 'nam_218'   # model
    date = '20170701'   # date --- year: 2017, month: 07, day: 01
    time_init = '0000'   # initialization time

    time_forecast_1 = '000'
    time_forecast_2 = '003'

    for i in range(int(time_forecast_1), int(time_forecast_2)):
        time_forcast = str(i).zfill(3)
        filetag = "%s_%s_%s_%s" % (model, date, time_init, time_forcast)
        csvfile = "%s_%s_%s_mb.csv" % (filetag, param, hgt)
        # full command we are running
        wgrib2_cmd = "%s %s.grb2 -match :%s:%s mb: -csv %s" % (wgrib2, filetag, param, hgt, csvfile)
        # # python3 version
        # wgrib2_cmd = "{} {}.grb2 -match :{}:{} mb: -csv {}".format(wgrib2, filetag, param, hgt, csvfile)
        # # old command
        # matchcom=filetag+'.grb2'+' -match ":'+param+':'+hgt+' mb:" -csv '+csvfile
        subprocess.call(wgrib2_cmd, shell=True)

    writefile = open('format.dat',"wb")

    for i in range(int(time_forecast_1), int(time_forecast_2)):
        time_forcast = str(i).zfill(3)
        filetag = "%s_%s_%s_%s" % (model, date, time_init, time_forcast)
        csvfile = "%s_%s_%s_mb.csv" % (filetag, param, hgt)
        arr = np.genfromtxt(open(csvfile, "rb"), dtype='str', delimiter=",")
        var = np.transpose(arr)[arr.shape[1] - 1]
        print(var)
        np.savetxt(writefile, var, fmt='%s', newline=",")
        writefile.write(b'\n')
        os.remove(csvfile)

    writefile.close()

if __name__ == '__main__':
    main()
