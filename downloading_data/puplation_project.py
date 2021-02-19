from country_codes import get_country_code

import json
from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n
import pygal




filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)


def get_country_code(country_name):
    """will return the code of any country searched"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if the country was not found don't break code
    # just continuew looping through and don't print
    # any error message
    return None



#  print only the countrys with info recorded in 2010
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        total_population = int(float((pop_dict['Value'])))
        
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = total_population
            # the key will be code and the value
            # will be total poulation.
       

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
    # will print the code and name of the country


# wm = pygal.maps.world.World()
# wm.title = 'North, Central, and South America'

# wm.add('North America', {'ca': 34128900, 'us': 678906, 'mx: 678900098'})
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('Soth America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

# wm.render_to_file('americas.svg')

wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('world populations.svg')