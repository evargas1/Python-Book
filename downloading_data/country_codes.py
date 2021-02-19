from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n

# this will be a function to return the two digit code of any country 

def get_country_code(country_name):
    """will return the code of any country searched"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if the country was not found don't break code
    # just continuew looping through and don't print
    # any error message
    return None


# print(get_country_code('Mexico'))

# print(get_country_code('Andorra'))
# print(get_country_code('United States'))
    # its a dictionary 
