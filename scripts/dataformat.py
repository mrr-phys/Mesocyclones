""" script to extract parameter value data from grb2 files """
import os
import subprocess
import datetime
from datetime import datetime
from datetime import timedelta
import numpy as np
import pandas as pd

def filenamer(filefcsthour, indatetime):
    indatetime -= timedelta(hours=int(filefcsthour))

    model = 'nam_218'   # model
    fcsthour=str(filefcsthour).zfill(3)

    filetag = "%s_%s%s%s_%s_%s" % (model, indatetime.year, str(indatetime.month).zfill(2), str(indatetime.day).zfill(2), str(indatetime.hour*100).zfill(4),fcsthour)
    return filetag

def dateparse(indate):
    outyear = int(indate[:len(indate)-4])
    outmonth = int(indate[len(indate)-4:len(indate)-2])
    outday = int(indate[len(indate)-2:])
    return outyear, outmonth, outday

def filegrabber(infilename):
    urlbase='https://nomads.ncdc.noaa.gov/data/meso-eta-hi'
    
    strdate=infilename.split("_")[2]
    fileyear, filemonth, fileday = dateparse(strdate)

    urltag = "%s/%s%s/%s%s%s/%s.grb2" % (urlbase, str(fileyear), str(filemonth).zfill(2), str(fileyear), str(filemonth).zfill(2), str(fileday).zfill(2), infilename)
    wget_cmd = "wget %s" % (urltag)
    subprocess.call(wget_cmd, shell=True)

def main():
    """ main """
    ##Define features
    feats = ['TMP:2 m above ground']#,'RH:2 m above ground','CAPE:surface','CIN:surface','CAPE:180-0 mb above ground','CIN:180-0 mb above ground']
    featskey = ['TMP_surf']#,'RH_surf','CAPE_surf','CIN_surf','CAPE_180mb','CIN_180mb']

    start_date = raw_input("Enter 8-digit start date (e.g. 20170701): ")
    start_hour = int(raw_input("Enter start hour (0, 6, 12, or 18): "))
    end_date = raw_input("Enter 8-digit end date (e.g. 20170701): ")
    end_hour = int(raw_input("Enter end hour (0, 6, 12, or 18): "))
    fcst_hour = int(raw_input("Enter forecast hour (0, 6, 12, or 18): "))

    #start_date='20170701'
    #start_hour='0'
    #end_date='20170701'
    #end_hour='6'
    #fcst_hour='6'

    wgrib2 = '~/MESO/grib2/wgrib2/wgrib2 ' # location of your wgrib2 tool

    df_TMP_surf = pd.DataFrame()
    df_RH_surf = pd.DataFrame()
    df_CAPE_surf = pd.DataFrame()
    df_CIN_surf = pd.DataFrame()
    df_CAPE_180mb = pd.DataFrame()
    df_CIN_180mb = pd.DataFrame()
    
    start_year, start_month, start_day = dateparse(start_date)
    end_year, end_month, end_day = dateparse(end_date)

    start_datetime = datetime(start_year,start_month,start_day,int(start_hour))
    end_datetime = datetime(end_year,end_month,end_day,int(end_hour))
    
    now_datetime = start_datetime
    while now_datetime <= end_datetime:
        
        filename=filenamer(fcst_hour, now_datetime)
        timestamp="%s_%s_pre%s" % (datetime.date(now_datetime), str(now_datetime.hour*100).zfill(4), fcst_hour)

        print timestamp
        ##Download files if not present in folder
        if not os.path.exists(filename+'.grb2'):
            filegrabber(filename)
        else:
            print filename+' already downloaded'

        ##Append pandas dataframes
        print 'doing something on ', filename, ' and at ', now_datetime

        for i in range(len(featskey)):
            
            tempcsv = "%s_%s.csv" % (featskey[i], filename)
            wgrib2_cmd = "%s %s.grb2 -match \":%s:\" -csv %s" % (wgrib2, filename, feats[i], tempcsv)
            subprocess.call(wgrib2_cmd, shell=True)

            df_single = pd.read_csv(tempcsv, names=['tinit', 'tfcst', 'param', 'mb', 'lat', 'long', 'val'])
            os.remove(tempcsv)

            df_single['lat'] = df_single['lat'].astype(str)
            df_single['long'] = df_single['long'].astype(str)
            coord=df_single['lat'].str.cat(df_single['long'], sep="_")

            valcol = df_single['val']
            valcol=valcol.rename(timestamp)
            valcol=valcol.rename(index=coord)
            
            if featskey[i]=='TMP_surf':
                df_TMP_surf=df_TMP_surf.append(valcol)

            elif featskey[i]=='RH_surf':
                df_RH_surf=df_RH_surf.append(valcol)

            elif featskey[i]=='CAPE_surf':
                df_CAPE_surf=df_CAPE_surf.append(valcol)

            elif featskey[i]=='CIN_surf':
                df_CIN_surf=df_CIN_surf.append(valcol)

            elif featskey[i]=='CAPE_180mb':
                df_CAPE_180mb=df_CAPE_180mb.append(valcol)

            elif featskey[i]=='CIN_180mb':
                df_CIN_180mb=df_CIN_180mb.append(valcol)

        ##Continue the loop
        
        now_datetime += timedelta(hours=6)

    timerange="%s_%s_%s_%s_pre%s" % (datetime.date(start_datetime), str(start_datetime.hour*100).zfill(4), datetime.date(end_datetime), str(end_datetime.hour*100).zfill(4), fcst_hour)
    
    df_TMP_surf.T.to_csv('TMP_surf'+timerange+'.csv')
    df_RH_surf.T.to_csv('RH_surf'+timerange+'.csv')
    df_CAPE_surf.T.to_csv('CAPE_surf'+timerange+'.csv')
    df_CIN_surf.T.to_csv('CIN_surf'+timerange+'.csv')
    df_CAPE_180mb.T.to_csv('CAPE_180mb'+timerange+'.csv')
    df_CIN_180mb.T.to_csv('CIN_180mb'+timerange+'.csv')
    
if __name__ == '__main__':
    main()
