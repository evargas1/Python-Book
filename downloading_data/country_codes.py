from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n

# this will be a function to return the two digit code of any country 

def get_country_code(country_name):
    """will return the code of any country searched"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        if country_name == 'Yemen, Rep.':
            return 'ye'
        if country_name == 'Bolivia':
            return 'bo'
        if country_name == 'Congo, Dem. Rep.':
            return 'cd'
        if country_name == 'Congo, Rep.':
            return 'cg'
        if country_name == 'Dominica':
            return 'do'
        if country_name == 'Egypt, Arab Rep.':
            return 'eg'
        if country_name == 'Gambia, The':
            return 'gm'
        if country_name == 'Hong Kong SAR, China':
            return 'hk'
        if country_name == 'Iran, Islamic Rep.':
            return 'ir'
        if country_name == 'Korea, Dem. Rep.':
            return 'kr'
        if country_name == 'Lao PDR':
            return 'la'
        if country_name == 'Libya':
            return 'ly'
        if country_name == 'Macao SAR, China':
            return 'mo'
        if country_name == 'Macedonia, FYR':
            return 'mk'
        if country_name == 'Moldova':
            return 'md'
        if country_name == 'Egypt, Arab Rep.':
            return 'eg'
        if country_name == 'Tonzania':
            return 'tz'
    # if the country was not found don't break code
    # just continuew looping through and don't print
    # any error message
    return None


# print(get_country_code('Mexico'))

# print(get_country_code('Andorra'))
# print(get_country_code('United States'))
    # its a dictionary 
