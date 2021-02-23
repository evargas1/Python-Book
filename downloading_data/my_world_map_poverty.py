from country_codes import get_country_code
from pygal.style import RotateStyle
import json
from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n
import pygal


filename = 'HNP_StatsCountry.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)