import os
ROOT = os.path.realpath('.')
NAM_CSV = ROOT + '/data/NAM/csv'
CSV_FILES = next(os.walk(NAM_CSV))[2]
SINGLE_CSV = NAM_CSV + '/' + CSV_FILES[0]

def main():
    """ splits the csv files (converted from grb2) seperate csv files per mb """
    with open(SINGLE_CSV, 'r') as csv:
        with open('50mb.csv', 'w') as filtered_csv:
            for line in csv: 
                if line.split(',')[3] == '"50 mb"':
                    filtered_csv.write(line + '\n')

if __name__ == '__main__':
    print() # just spacing for reading the ouput easier
    main()