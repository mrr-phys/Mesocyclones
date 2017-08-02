""" pandas script to parse large csv files and filter out the data we want """
import os
import pandas

NAM_RAW = r'C:\Users\dontran\Downloads\csv\raw'
NAM_EXTRACTED = r'C:\Users\dontran\Downloads\csv\extracted'

def main():
    """ main """
    raw_file = next(os.walk(NAM_RAW))[2][3]
    # for raw_file in next(os.walk(NAM_RAW))[2]: # next(os.walk(NAM_RAW))[2] returns the files in the NAM_RAW directory
    nam_dataframe = pandas.read_csv(r'{}\{}'.format(NAM_RAW, raw_file), names=['time0', 'time1', 'paramter', 'mb', 'lat', 'long', 'value'])

    # init_time = nam_dataframe['time0'][0]
    unique_mb = nam_dataframe['mb'].unique()

    for mb in unique_mb:
        filename = r'{}\{}.csv'.format(NAM_EXTRACTED, mb)
        nam_dataframe[nam_dataframe['mb'] == mb][['time0', 'value']].to_csv(filename, index=False, mode='a')

if __name__ == '__main__':
    main()
