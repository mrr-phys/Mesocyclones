with open('./nam_small.csv') as nam:
    with open('./nam_flip.csv', 'w') as new_nam:
        for line in nam:
            line = line.split(',')
            value = line[3].strip().replace('\\n', '')
            new_nam.write(value + ',')