#!/usr/bin python3
"""
converts grb2 files to CSV then converts the CSV into our special format
"""
import os
ROOT = os.path.realpath('.')
NAM_CSV = ROOT + '/data/NAM/csv'
CSV_FILES = next(os.walk(NAM_CSV))[2]
SINGLE_CSV = NAM_CSV + '/' + CSV_FILES[0]

def main():
    """ format csv files into our special format """
    with open(SINGLE_CSV, 'r') as csv:
        with open('test.csv', 'w') as formatted_csv:
            line = csv.readline().split(',')
            line_dic = {
                'init_time': line[0], # and line[1] since they are the same but idk why
                'parameter': line[2],
                'mb': line[3],
                'long': line[4],
                'lat': line[5],
                'value': line[6].strip() # value of the parameter
            }
            # print(type(line['init_time']))
            # print(line['init_time'] + ', ')
            formatted_csv.write(line_dic['init_time'] + ', ')
            for line in csv.readlines():
                formatted_csv.write(line_dic['value'] + ', ')

if __name__ == '__main__':
    print() # just spacing for reading the ouput easier
    main()
