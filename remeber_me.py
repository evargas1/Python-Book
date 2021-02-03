import json

# this will check to see if a user has already entered their name
# if they have their name with a msg will appear if not they will be asked
def greet_user():
    """this function will check to see if the name has already been stored"""

    file_name = 'usernames_saved.json'
    try:
        with open(file_name) as file_object:
            username = json.load(file_object)
        # this will need an else statemnt with a print #TODO
    except FileNotFoundError:
    # if username does not exist yet you will be asked 
        username = input("Hey please give us your name")
        with open(file_name, 'w') as file_object:
        # order -- info or block of code first than location of storage
            json.dump(username, file_object)
            print("Welcome " + username.title() + " we will remeber you next time!")
    else:
        print("Hey Welcome back, " + username.title())
# it worked returned Janet did i memorize everything maybe 

greet_user()


def get_stored_username():
    """will retirve a username if one exist otherwise pass"""
    file_name = 'usernames_y.json'
    try:
        with open(file_name) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """will ask the user for their name"""
    username = input("Hey Welcome what is your name? \t")
    file_name = 'usernames_y.json'
    with open(file_name, 'w') as file_object:
        json.dump(username, file_object)
    return username
        

def welcome_user():
    """offer a greeting to everyone old and new"""
    username = get_stored_username()

    
    
    if username:
        is_this_you = input("The name we have on file is " + username + " is this you? (yes/no) \t ")
        if is_this_you == 'yes':
            print("Welcome back " + username.title() + "!")
        if is_this_you == 'no':
            username = get_new_username()
            print("Next time you login we will remeber you " + 
            username.title() + 
            " ")


welcome_user()
# yup it worked that is crazy how much more orgainzed cna it get 

# filename = 'favorite_number.txt'
# your_number = input("What is your favorite number? \t")

# with open(filename, 'w') as file_object:
#     json.dump(your_number, file_object)
#     print("Great next we will rember your favorite number as: " + your_number)

# with open(filename) as file_object:
#     your_number = json.load(file_object)
#     print("Hey welcome back your favorite number was: " + your_number)


def return_my_number():
    """check to see if a number is store if so return it"""
    filename = 'fate.txt'
    try:
        with open(filename) as file_object:
            your_number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return(your_number)

def new_user_number():
    """will ask the user for their favorite number"""
    your_number = input("HEY please give us your favorite number: \t")
    filename = 'fate.txt'
    with open(filename, 'w') as file_object:
        json.dump(your_number, file_object)
    return your_number
    # this line of code was important because it makes sure 
    # something is given back to the greet_new_old_suer function


def greet_new_old_user():
    """welcome back message for old or new users """
    your_number = return_my_number()
    if your_number:
        print("Welcome back your favorite number was " + str(your_number))
        # this might need a sring come back if so #TODO
    else:
        your_number = new_user_number()
        print("Hey we will remeber your number as: " + str(your_number))

greet_new_old_user()


filename = 'tae.number.txt'

try:
    with open(filename) as file_object:
        num = json.load(file_object)
except FileNotFoundError:
    num = input("Hey please tell us your favorite number and we will remeber next time! \t")
    with open(filename, 'w') as file_object:
        json.dump(num, file_object)
        print("Great so your favorite number, " + str(num) + " has been saved")
else:
    print("Your favorite number is " + str(num))

# these few lines of the try statement are perfoming a lot of tasks hsould be in a function
# or as done above stored in several function all connected.
