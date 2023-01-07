import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    county_dialect = csv.Sniffer().sniff(sample)
    county_dialect.skipinitialspace = True
    countries_data.seek(0)
    country_reader = csv.reader(countries_data, dialect=county_dialect)
    for row in country_reader:
        print(row)

print('*' * 80)

attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

for attribute in attributes:
    print(f'{attribute}: {repr(getattr(county_dialect, attribute))}')
