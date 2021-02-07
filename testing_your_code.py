def get_formatted_name(first, last, middle=''):
    """will print a neat line of code"""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last

    return full_name.title()


# print("Please give us your name. Type q to quit whenever")
# while True:
#     first_name = input("what is your first name? \t")
#     if first_name == 'q':
#         break
#     last_name = input("What is your last name? \t")
#     if last_name == 'q':
#         break

#     full_name = get_formatted_name(first_name, last_name)
#     print(full_name)

def formatted_city_country(city, country, population=''):
    """ Will print the name of city and country"""

    if population:
        formatte_name = city.title() + ", " + country.title() + " - " + str(population) + " people."
    else:
        formatte_name = city.title() + ", " + country.title()    
    return formatte_name

spain = formatted_city_country('madrid', 'spain')
print(spain)
