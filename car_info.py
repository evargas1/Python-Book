def car_info(model, year_manfactured, **more_info):
    """Save info about a car in a dictionary"""
    car_in = {}
    car_in['model'] = model.title()
    car_in['year made'] = year_manfactured
    # will it be stored as a string? I think yes,
    # it stores in whatever way you input it which means
    # whenever you go back to work on it you will have to convert it
    for key, value in more_info.items():
        car_in[key] = value
    return car_in