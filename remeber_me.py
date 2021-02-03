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

