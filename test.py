import numpy as np
import math
import re
import os
import subprocess

gribcom='~/MESO/grib2/wgrib2/wgrib2 '

param='TMP'
hgt='50'

model='nam_218'
date='20170701'
timeinit='0000'

timefcst1='000'
timefcst2='003'

for i in range(int(timefcst1),int(timefcst2)):
    timefcst=str(i).zfill(3)
    filetag=model+'_'+date+'_'+timeinit+'_'+timefcst
    csvfile=filetag+'_'+param+'_'+hgt+'_mb.csv'
    
    matchcom=filetag+'.grb2'+' -match ":'+param+':'+hgt+' mb:" -csv '+csvfile
    gencom=gribcom+matchcom
    subprocess.call([str(gencom)],shell=True)

writefile=open('format.dat',"wb")

for i in range(int(timefcst1),int(timefcst2)):
    
    timefcst=str(i).zfill(3)
    filetag=model+'_'+date+'_'+timeinit+'_'+timefcst
    csvfile=filetag+'_'+param+'_'+hgt+'_mb.csv'
    
    arr = np.genfromtxt(open(csvfile,"rb"),dtype='str',delimiter=",")
    var=np.transpose(arr)[arr.shape[1]-1]
    print var

    np.savetxt(writefile,var,fmt='%s',newline=",")
    writefile.write(b'\n')

    os.remove(csvfile)

writefile.close()
