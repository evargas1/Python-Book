from country_codes import get_country_code
from pygal.style import RotateStyle
import json
from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n
import pygal




filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    



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
        

        

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 1000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# print the numbers of how many countires are in each dict
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
    # will print the code and name of the country


# wm = pygal.maps.world.World()
# wm.title = 'North, Central, and South America'

# wm.add('North America', {'ca': 34128900, 'us': 678906, 'mx: 678900098'})
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('Soth America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

# wm.render_to_file('americas.svg')

wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('> 1bn', cc_pops_3)
wm.render_to_file('world populations.svg')