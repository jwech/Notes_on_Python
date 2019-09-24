from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    '''Return 2-letters country code baed on given country name'''
    for code, name  in COUNTRIES.items():
        if name == country_name:
            return code
    # Return none if country not found
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))