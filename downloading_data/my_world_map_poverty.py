import csv
from pygal.style import RotateStyle
from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n
import pygal
from country_codes import get_country_code


filename = 'HNP_StatsCountry.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    main_dit = {}
    names, data = [], []
    
    for row in reader:
        
        table_nam = row[2]
        print(table_nam)
       
        data_info = row[8]
        main_dit[table_nam] = data_info
         
    new_dit = {}
    for key, value in main_dit.items():

        code = get_country_code(key)
        
        if code:
            new_dit[code] = value

            print(key + " ---- " + value)

    print(new_dit)

    upper_middle_income, lower_middle_income, high_income, low_income = {}, {}, {}, {}
    for key, value in new_dit.items():
        if value == 'Upper middle income':
            upper_middle_income[key] = value
        elif value == 'Lower middle income':
            lower_middle_income[key] = value
        elif value == 'High income':
            high_income[key] = value
        elif value == 'Low income':
            low_income[key] = value
        else:
            print("Some did not fit this category")


print("\n lower middle income")
key_lower_middle_income = []
for key in lower_middle_income.keys():
    key_lower_middle_income.append(key)
print(key_lower_middle_income)


print("\n high income")
key_high_income = []
for key in high_income.keys():
    key_high_income.append(key)
print(key_high_income)

print("\n low income")
key_low_income = []
for key in low_income.keys():
    key_low_income.append(key)
print(key_low_income)

print("\n Upper middle income ")
key_upper_middle_income = []
for key in upper_middle_income.keys():
    key_upper_middle_income.append(key)

print(key_upper_middle_income)
# was tested and ran properly
# success!
# run on trinket -- code below





# from pygal.maps.world import COUNTRIES
# from pygal_maps_world import i18n
# import csv
# from pygal.style import RotateStyle
# import pygal

# # this will be a function to return the two digit code of any country 

# def get_country_code(country_name):
#     """will return the code of any country searched"""
#     for code, name in COUNTRIES.items():
#         if name == country_name:
#             return code
#         if country_name == 'Yemen, Rep.':
#             return 'ye'
#         if country_name == 'Bolivia':
#             return 'bo'
#         if country_name == 'Congo, Dem. Rep.':
#             return 'cd'
#         if country_name == 'Congo, Rep.':
#             return 'cg'
#         if country_name == 'Dominica':
#             return 'do'
#         if country_name == 'Egypt, Arab Rep.':
#             return 'eg'
#         if country_name == 'Gambia, The':
#             return 'gm'
#         if country_name == 'Hong Kong SAR, China':
#             return 'hk'
#         if country_name == 'Iran, Islamic Rep.':
#             return 'ir'
#         if country_name == 'Korea, Dem. Rep.':
#             return 'kr'
#         if country_name == 'Lao PDR':
#             return 'la'
#         if country_name == 'Libya':
#             return 'ly'
#         if country_name == 'Macao SAR, China':
#             return 'mo'
#         if country_name == 'Macedonia, FYR':
#             return 'mk'
#         if country_name == 'Moldova':
#             return 'md'
#         if country_name == 'Egypt, Arab Rep.':
#             return 'eg'
#         if country_name == 'Tonzania':
#             return 'tz'
#     # if the country was not found don't break code
#     # just continuew looping through and don't print
#     # any error message
#     return None


# # print(get_country_code('Mexico'))

# # print(get_country_code('Andorra'))
# # print(get_country_code('United States'))
#     # its a dictionary 
    
    
    
# # wm.add('North America', {'ca': 34128900, 'us': 678906, 'mx: 678900098'})
# # wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# # wm.add('Soth America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

# # wm.render_to_file('americas.svg')

# wm_style = RotateStyle('#336699')
# wm = pygal.maps.world.World(style=wm_style)
# wm.title = 'Poverty Levels Around The World'
# wm.add('High income', ['ad', 'ae', 'au', 'at', 'be', 'bh', 'bn', 'ca', 'ch', 'cl', 
# 'cy', 'cz', 'de', 'dk', 'es', 'ee', 'fi', 'fr', 'gb', 'gr', 'gl', 'gu', 'hk', 'hr',
# 'hu', 'ie', 'is', 'il', 'it', 'jp', 'kw', 'li', 'lt', 'lu', 'lv', 'mo', 'mc', 'mt', 
# 'mu', 'nl', 'no', 'nz', 'om', 'pa', 'pl', 'pr', 'pt', 'ro', 'sa', 'sg', 'sm', 'si', 
# 'se', 'sc', 'uy', 'us'])
# wm.add('Upper middle income', ['al', 'ar', 'am', 'az', 'bg', 'ba', 'by', 'bz', 'br',
# 'bw', 'cn', 'co', 'cr', 'cu', 'do', 'ec', 'ga', 'ge', 'gq', 'gt', 'gy', 'id', 'ir', 
# 'iq', 'jm', 'jo', 'kz', 'lb', 'ly', 'mv', 'mx', 'me', 'my', 'na', 'pe', 'py', 'ru',
# 'rs', 'sr', 'th', 'tm', 'tr', 'za'])
# wm.add('Lower middle income', ['ao', 'bj', 'bd', 'bo', 'bt', 'cm', 'cg', 'dj', 'dz', 
# 'eg', 'gh', 'hn', 'in', 'ke', 'kh', 'la', 'lk', 'ls', 'ma', 'md', 'mm', 'mn', 'mr', 
# 'ng', 'ni', 'np', 'pk', 'ph', 'pg', 'sn', 'sv', 'tl', 'tn', 'ua', 'uz', 'zm', 'zw'])

# wm.add('Low income', ['af', 'bi', 'bf', 'cf', 'cd', 'er', 'et', 'gn', 'gm', 'gw',
# 'ht', 'lr', 'mg', 'ml', 'mz', 'mw', 'ne', 'rw', 'sd', 'sl', 'so', 'sy', 'td', 'tg',
# 'tj', 'ug', 'ye'])
# wm.render_to_file('world populations.svg')

    
    






# for index , column_header in enumerate(header_row):
#     print(index, column_header)


    