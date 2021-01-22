# [] list 
# () tuples
# {} dictionaries 

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print(alien_0)

alien_0['x_posistion'] = 0
alien_0['y_posistion'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'yellow'
alien_1['points'] = 10
print(alien_1)

alien_1['color'] = 'blue'
print(alien_1)
print("The alien is now " + alien_1['color'] + ".")

alien_3 = {'x_pos': 0, 'y_pos': 25, 'speed': 'fast'}
print("The aliens current posistion is " + str(alien_3['x_pos']))

if alien_3['speed'] == 'slow':
    move = 1
elif alien_3['speed'] == 'medium':
    move = 2
else:
    # btw this means the alien is about to win lol
    move = 3


# the new posistion is the old posistion plus move both int
alien_3['x_pos'] = alien_3['x_pos'] + move
print("\n  The aliens new posistion is " + str(alien_3['x_pos']))
print(alien_1)
del alien_1['color']
# removes value permently 
print(alien_1)



favorite_languages = {
    'ken': 'java',
    'Jackie': 'ruby',
    'star': 'python',
    'edward': 'c#',
}

print("\nKens favorite programming lang is " + 
    favorite_languages['ken'].title() +
     ".")
print("\nThe small question section")
info_Tiara = {
    'name': 'tiara',
    'age': 25,
    'gender': 'female',
    'city': 'chicago',
    'learning': 'korean',
}
print("\nThe name of our character is: " + info_Tiara['name'].title())
print("\nThe age of our character is: " + str(info_Tiara['age']))
print("\nThe avatar that we will be using today is " + info_Tiara['gender'].title())
print("\nThe city in which our avtar lives is " + 
    info_Tiara['city'] + 
    " this will greatly affect the results.")
print("\nOur avtar is quite unusaul in the fact that she has many skills like: " + 
    info_Tiara['learning'].title() + 
    " very impressive considering this is a diffult lang.")

favorite_numbers = {
    'salma': 17,
    'jade': 15,
    'tiara': 19,
    'tamyah': 15,
    'jael': 15,
}
# serpartor
print("\nThis will begin a new fun section")
print("Salma favorite number is actually her age " + str(favorite_numbers['salma']))
print("Jades favorite number is " + str(favorite_numbers['jade']))
print("Tiaras favorite number is quite odd " + str(favorite_numbers['tiara']))
print("Tamyahs favorite number is you guessed it " + str(favorite_numbers['tamyah']))
print("Jael the baby: " + str(favorite_numbers['jael']))

# is better to refer to dictionaries as a glossery 
new_words = {
    'pop': 'temperoly removes an item from a list',
    'insert': 'adds value to any part of the list',
    'append': 'adds value to the end of the list',
    'tuple': 'immutable list',
    'str': 'switches any int to a str to use in print',
}
print("\n This will begin my vocab section")

print("\nLearned what pop does: " + 
    new_words['pop'] +
     ".") 
print("\nI had so much fun learning what insert means: " + 
    new_words['insert'] + 
    ".")
print("\nI think this vocab will prove to be awesome append: " 
    + new_words['append'] + 
    ".")
print("\nTuples were so confusing to me but now i understand they are " + 
    new_words['tuple'] + 
    ".")
print("\nStr method amazing life saver in print statements: " 
    + new_words['str']  +
     ".")

# New dictionary exmaple
tiara = {
    'first_name': 'tiara',
    'last_name': 'harris',
    'username': 'tiarah25',
}
for k, v in tiara.items():
    print("\nKey: " + k.title())
    print("Value: " + v.title())

# start a new activity section
print("\nThis will begin a new activity section")
favorite_languages = {
    'ken': 'java',
    'jackie': 'ruby',
    'star': 'python',
    'edward': 'c#',
    'jane': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite programming language is " + language.title() + ".")

for name in favorite_languages.keys():
    print(name.title())

friends = ['jackie', 'star']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print("hey " + 
            name.title() +
            ", I see that your favorite programming langauge is " + 
            favorite_languages[name].title() + 
            "!")


if 'jane' not in favorite_languages.keys():
    print("Hey jane take the poll!")

for n in sorted(favorite_languages.keys()):
    print("Hey, " + n.title() + " thanks for taking our survey!")
# the sorted function will sort the dictionary permently 

print("\nThese are the languages we have right now.")
for l in favorite_languages.values():
    print(l.title())

for l in sorted(favorite_languages.values()):
    print(l.title())


# the sorted function permently sorts the results in alheobatcal order

# the set function helps to avoid repuation
print("\nThis will be the set function")
for l in set(favorite_languages.values()):
    print(l.title())


print("\nRiver and country dictionary\n")
rivers = {
    'nile': 'egypt',
    'michigan': 'america',
    'yellow': 'china',
}
for r, c in rivers.items():
    print("The " + r.title() + " river runs in " + c.title())
for r in rivers.keys():
    print(r.title() + " these rivers exist in " + rivers[r].title())
for c in rivers.values():
    print(c.title())

print("\nThis will be the last bullet point\n")
favorite_languages = {
    'ken': 'java',
    'jackie': 'ruby',
    'star': 'python',
    'edward': 'c#',
    'jane': 'python',
}
should_take_poll = ['ruby', 'jane', 'ken']

for people in should_take_poll:
    if people in favorite_languages:
        print("Thank you for taking the poll " + people.title() + ".")
    else:
        print("We invite you take the poll " + people.title())
    # I feel like this methods of coding is going to be popular

alien_4 = {'color': 'red', 'points': 6}
alien_8 = {'color': 'blue', 'points': 9}
alien_12 = {'color': 'yellow', 'points': 12}

alien_list = [alien_4, alien_8, alien_12]

# {} dictionary or glossary
# [] list
# () tuples unmutable

for head in alien_list:
    print(head)

all_the_aliens = []
# the 30 in rnage tells the loop how many times to run, 
# since there are no items in the list at the moment
for a_num in range(30):
    new_alien = {'color': 'red', 'points': 6, 'speed': 'medium',}
    all_the_aliens.append(new_alien)



for al in all_the_aliens[0:3]:
    if al['color'] == 'red':
        al['color'] = 'blue'
        al['points'] = 12
        al['speed'] = 'fast'
    elif al['color'] == 'blue':
        al['color'] = 'green'
        al['points'] = 15
        al['speed'] = 'slow'


# the method below is the one the book uses but the differance 
# is when it prints its vertical
for a in all_the_aliens[0:5]:
    print(a)

print("Total number of aliens that have been created " + str(len(all_the_aliens)))


# a dictionary that contains a list as well
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra_cheese'],
}
print("\nGreat so you orderd a " + 
    pizza['crust'] + 
    " crust pizza. Yummmmyyyy!!!!")

for toppings in pizza['toppings']:
    print("\n These are the avaible toppings: " + toppings + ".\n")

# this for loop will run through all the items with a key of toppings. 
# .items() .keys() .values() are super important becuase that is the only way the for loop
# will go around the dictionaries
for items in pizza.keys():
    print(items)

print("\n Fav languages problem\n")
fav_lang = {
    'jen': ['ruby', 'python', 'c#'],
    'ken': ['java'],
    'star': ['python', 'html', 'ruby'],
    'tiara': ['php', 'c'],
}
# what a awesome simple yet powerful program 
for name, lang in fav_lang.items():
    if len(lang) == 1:
        print("\n" + name.title() + " loves to program in " + lang[0].title() )
    else:
        print("\n-------" + name.title() + " loves to program in: \n")
        for language in lang:
            print("\t" + language.title())

# a dictionary inside a larger dictoionary with identcal sub keys
print("\nThe user with a sub dictionary in it")
user = {
    'alber2': {
        'first': 'samuel',
        'last': 'jay',
        'location': 'princeton',
    },
    'samurl9': {
        'first': 'samuel',
        'last': 'jay',
        'location': 'harvard',
    },
}
# wow that was so much fun to code almost cried
for name, info in user.items():
    print("\n The users name is: " + name.title())
    full_name = info['first'].title() + " " + info['last'].title()
    locle = info['location'].title()
    
    print("\tHis full name is: " + full_name)
    print("\tLoaction of student: " + locle)

# dang is spacing important the last two were only running for the last piece 
# of code because it was not in the for loop and looping around every item in the dictionary

haily = {
    'hair_color': 'brown',
    'eyes': 'black',
    'fav_color': 'green',
}
nancy = {
    'hair_color': 'blone',
    'eyes': 'black',
    'fav_color': 'yellow',
}
janet = {
    'hair_color': 'red',
    'eyes': 'green',
    'fav_color': 'blue',
}
applicants = [haily, nancy, janet]
for people in applicants:
    print(people)

princess = {
    'breed': 'golden retriver',
    'owner': 'james',
}
freckle = {
    'breed': 'husky',
    'owner': 'karen',
}
spots = {
    'breed': 'pitbull',
    'owner': 'derek',
}
babe = {
    'breed': 'skitozia',
    'owner': 'michelle',
}
pets = [princess, freckle, spots, babe]
for animal in pets:
    print(animal)
# come back and unpack everything !!!!!!
# You though i forgot sikyeeee


favorite_places = {
    'kate': ['korea', 'mexico', 'china'],
    'janet': ['norway', 'mississippi', 'arentina'],
    'star': ['korea', 'england', 'spain'],
}
for name, places in favorite_places.items():
    print("These are " + name.title() + " favorite places to visit: ")
    for c in places:
       print("\t" + c.title())

# favorite numbers functions
favorite_numbers = {
    'salma': [17, 9, 5],
    'jade': [20, 15, 16, 9],
    'tiara': [2, 5],
    'tamyah': [22, 7, 0],
    'jael': [15],
}
for name, numbers in favorite_numbers.items():
    print("\nThese are " + name.title() + "'s favorite numbers: ")
    for fav in numbers:
        print("\t" + str(fav))

cities = {
    'chicago': {
        'pouplation': 5,
        'country': 'america',
        'fact': 'windy city',
    },
    'seoul': {
        'pouplation': 10000,
        'country': 'korea',
        'fact': 'BTS',
    },
    'amsterdam': {
        'pouplation': 23,
        'country': 'netherlands',
        'fact': 'bicyle',
    },
}
for city, and_info in cities.items():
    print("\n" + city.title() + " beautiful city here are some facts: ")
    country = and_info['country'].title()
    fact = and_info['fact'].title()
    popu = str(and_info['pouplation']).title()
    # added string here to help with future programs 
    # that way people would not have to worry about errors
    print("The country: " +
         country + 
        " \nAverage pouplation: " + 
        popu + 
        " \nFun fact: " +  fact)
    # spacing super important if I want it to print for every country I need it in the loop.
# still neeed to unpack dogs I ant forget 


princess = {
    'breed': 'golden retriver',
    'owner': 'james',
}
freckle = {
    'breed': 'husky',
    'owner': 'karen',
}
spots = {
    'breed': 'pitbull',
    'owner': 'derek',
}
babe = {
    'breed': 'skitozia',
    'owner': 'michelle',
}
pets = [princess, freckle, spots, babe]
for animal in pets:
    for info, info_details in animal.items():
        print("The " + info + " of this animale is " + info_details + ".\n")
        
# come back and unpack everything !!!!!!
# You though i forgot sikyeee
# I dont like how it works but it does 
# message = input("Tell me something about you and I will repeat ith back: ")
# print(message)

# name = input("Please tell me your name: ")
# print("Hello! " + name)

# prompt = "If you tell me who you are, we can perosonalize this message to you."
# prompt += "\nWhat is your name? "

# name = input(prompt)
# print("\nHello! " + name)
age = input("How old are you? ")
print(age)
print("Wow you are so young only " + age)
# it is a string because if it wasnt it would print error 