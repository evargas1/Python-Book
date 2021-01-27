def build_portfilo(first_name, last_name, **user_info):
    """Will save info on a person to a dictionary"""
    user_portfilo = {}
    user_portfilo['first'] = first_name.title()
    # the key will be the title first and the value will be whatever argum is passed
    user_portfilo['last'] = last_name.title()
    for key, value in user_info.items():
        user_portfilo[key] = value
    return user_portfilo