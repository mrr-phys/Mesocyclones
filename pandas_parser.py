import pandas

# nam = pandas.read_csv('../nam.csv')
nam = pandas.read_csv('./nam.csv', names=['time0', 'time1', 'paramter', 'mb', 'lat', 'long', 'value'])
del mb[' time1']
del mb[' parameter']
del mb[' long']
del mb[' lat']
unique_mb = nam[' mb'].unique()
for mb in unique_mb:
    nam[nam[' mb'] == mb].to_csv(mb + '.csv', index=False)