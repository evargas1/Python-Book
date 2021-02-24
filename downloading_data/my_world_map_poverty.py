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
    
    






# for index , column_header in enumerate(header_row):
#     print(index, column_header)


    