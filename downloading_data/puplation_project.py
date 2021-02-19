import json
from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n
from country_codes import get_country_code
import pygal


filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

#  print only the countrys with info recorded in 2010
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        total_population = int(float((pop_dict['Value'])))
        
        code = get_country_code(country_name)
        if code:
            print(code + " : " + str(total_population))
        else:
            print("Error" + " : " + country_name )
    # now we can succesfully graph all the int num

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
    # will print the code and name of the country


wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add('North America', {'ca': 34128900, 'us': 678906, 'mx: 678900098'})
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('Soth America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')