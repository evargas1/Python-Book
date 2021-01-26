def greet_user(username):
    """ This will be a simple function to greet people """
    print("Hello, " + username.title() + " nice to meet you.")


greet_user('sarah')
# the infomation you passed in the parethis is sometimes refered to as 
# a parameter or arugument 
def learning_today():
    """ What I have learned """
    print("Today I have learned what a function is in python")


learning_today()
def favorite_book(title):
    """ The title of your favorite book"""
    print("One of my fvaorites books is " + title.title())


favorite_book('alice in wonderland')
print("\nThis will begin my pet function now ---")
def pets(pets_name, pets_kind= 'dog'):
    # the reason it would go at the end of the list is because python is still using positonal argum.
    # order matters the value with a defualt value has to be at the end of the list
    """ Simple pet function kind and name """
    print("Oh wow so you have a " + pets_kind.title())
    print("Yeah I do have a " + pets_kind.title() + " and his name is " + pets_name.title())


pets('monkey', 'ben')
# these functions help keep the code clean and simple
# these are all postional arguments and need to be read in one spot!!
# to avoid confusion you would spefy which prameyer is being called
pets(pets_kind= 'dog', pets_name= 'mike')
pets(pets_name= 'jan', pets_kind= 'dino')
pets(pets_name= 'jenny' )
pets('mickey')

print("\nWill return a neatly formatted name no default parameters")
def get_full_name(first_name, last_name):
    """This will return full name neatly formatted"""
    full_name = first_name + " " + last_name
    return full_name.title()


musican = get_full_name('kimmy', 'henderson')
print(musican)

print("\nAlthernate function for middle names")
def full_name_get(first_name, last_name, middle_name= ''):
    """Will retun the output of a neatly formatted name"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


ex_1 = full_name_get('dave', 'johnosn')
print(ex_1)
ex_2 = full_name_get('john', 'harris', 'tom')
print(ex_2)
# in order for the posistional argument to work the middle name needs to be at the end


# can also store infomation in a dictionary to make working with data easier
def make_a_person(first_name, last_name, age=''):
    """Will return info in the form of a dictionary"""
    person = {'first': first_name, 'last': last_name}
    if age:
        # will check if something has been added to age optional argum
        person['age_today'] = age
    return person


dancer = make_a_person('mickey', 'jake', age=20)
print(dancer)
# will store information in a dict
dancer_1 = make_a_person('jame', 'lewis')
print(dancer_1)


def full_formatted_name(first_name, last_name ):
    """Will be used in a while loop to take input info"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


# while True:
#     print("\nPlease tell us your name, ")
#     f_name = input("Please give us your first name: \t")
#     l_name = input("Please give us your last name: \t")

#     whole_name = full_formatted_name(f_name, l_name)
#     print("Hey! " + whole_name + " thanks for taking our survey we appreciate it!")



# while True:
#     print("\nWelcome to cadialc, please give us your name ")
#     print("\nEnter 'q' at any time to quit")

#     f_name = input("Hey give us your first name: \t")
#     if f_name == 'q':
#         break

#     l_name = input("What is your last name: \t")
#     if l_name == 'q':
#         break

#     whole_name = full_formatted_name(f_name, l_name)
#     print("Thanks for taking our survery, " + whole_name + "!")
# there is nothing wrong with this solution just long i think the is a better way



# this way does not work beacuse its usally at the end of the code isn't stopping the code
# this method is not stopping the code form running right at this time


def city_country(city_name, country_name):
    """This will produce a neatly formatted string"""
    format_name = city_name + ", " + country_name
    return format_name.title()


my_city = city_country('chicago', 'america')
print(my_city)
diff_city = city_country('miami', 'america')
print(diff_city)
    

def make_my_album(artist_name, album_name, number_of_songs= ''):
    """This will put the results of input in a dict"""
    album = {'artist': artist_name, 'album': album_name}
    if number_of_songs:
        album['songs'] = number_of_songs
    return album


mikey = make_my_album('jones', 'lights on fire', number_of_songs= 35)
janey = make_my_album('janey rose', 'drop the mic')
miguel = make_my_album('hampton', 'live once')

print(mikey)
print(janey)
print(miguel)


# commented out because it requires inputs from the users

# while True:
#     print("\nPlease tell us your favorite artist and the song you love most")
#     print("You can quit at any time by typing 'q' have fun")

#     name = input("Please input the artist name: \t")
#     if name == 'q':
#         break

#     song = input("Please input your favorite song from " + name.title() + ": \t")
#     if song == 'q':
#         break

#     whole_name = make_my_album(name, song)
#     print("\nThanks for taking our survery you love " + name.title() + " and your favorite song is " + song.title())
#     print(whole_name)

#     again = input("\t\nWould you like to survey again?(yes/no) \t ")
#     if again == 'no':
#         break

def greet_users(names):
    """Will print a personalized message to a list of people"""
    for person in names:
        msg = ("Hola! " + person.title() + " thanks for joining.")
        print(msg)


usernames = ['janet', 'martha', 'micheal', 'jakie']
greet_users(usernames)

unprinted_designs = ['iphone case', 'computer box', 'blue box', 'stopper']
completed_designs = []

print("\nThis will be moving items without a function")
while len(unprinted_designs) > 0:
    current_process = unprinted_designs.pop()

    print("We are currently producing your " + current_process.title())
    completed_designs.append(current_process)

print("\tThese are all the new items added")
for design in completed_designs:
    print(design)



def print_models_processing(unprinted_designs, completed_designs):
    """prints any 3D models while being processed"""
    while len(unprinted_designs) > 0:
        current_process = unprinted_designs.pop()

        print("Printing models: " + current_process.title())
        completed_designs.append(current_process)


def print_all_new_models(completed_designs):
    """print vertical list of all the objects, that are now complete"""
    print("\nThis will be a list of all the objects that have been added to the list.")
    for thing in completed_designs:
        print(thing)


unprinted_designs = ['iphone case', 'computer box', 'blue box', 'stopper', 'stero']
completed_designs = []
print_models_processing(unprinted_designs[:], completed_designs)
# [:] makes a copy of the orginal list unprinted list and stores it on file.
print_all_new_models(completed_designs)
print(unprinted_designs)

magicans_creeps = ['peter', 'mike', 'dave', 'christopher']

print
def list_all_names(names):
    """Will print a long list of many magicans"""
    for person in names:
        print(person)

list_all_names(magicans_creeps[:])

def nice_message(persons):
    """Prints a cutie message to all people"""
    for person in persons:
        print("We are so happy to have you " + person.title() + " Welcome!")

nice_message(magicans_creeps[:])
print(magicans_creeps)

    



