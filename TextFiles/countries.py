filename = 'country_info.txt'
countries = {}
# code_lookup = {}
with open(filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {'name': country,
                        'capital': capital,
                        'country_code': code,
                        'cc3': code3,
                        'dialing_code': dialing,
                        'timezone': timezone,
                        'currency': currency
                        }
        print(country_dict)
        countries[country.casefold()] = country_dict
        # code_lookup[code.casefold()] = country
        countries[code.casefold()] = country_dict  # adds e secondary key to the dict (country code)

print(countries)

# print("type a country name")
# print(countries[input()])
chosen_country = input('Please enter the name of a country\n').casefold()
if chosen_country in countries:
    country_data = countries[chosen_country]
    print(country_data['capital'])
    print(f"the capital of the {chosen_country} is {country_data['capital']}")
