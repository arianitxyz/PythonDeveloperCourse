import csv

from TextFiles import country_dialect

dialect = csv.excel
dialect.delimiter = '|'
country_file = 'country_info.txt'

countries = {}
# code_lookup = {}
with open(country_file, encoding='utf-8', newline='') as country_file:
    # get the column headers from the file
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index]=heading.casefold()

    dict_reader = csv.DictReader(country_file, dialect=dialect,fieldnames=headings)

    for row in dict_reader:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')

print(countries)

# print("type a country name")
# print(countries[input()])
while True:
    chosen_country = input('Please enter the name of a country\n').casefold()
    if chosen_country in countries:
        country_data = countries[chosen_country]
        print(country_data['capital'])
        print(f"the capital of the {chosen_country} is {country_data['capital']}")
