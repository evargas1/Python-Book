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
def pets(pets_kind, pets_name):
    """ Simple pet function kind and name """
    print("Oh wow so you have a " + pets_kind.title())
    print("Yeah I do have a " + pets_kind.title() + " and his name is " + pets_name.title())


pets('monkey', 'ben')
# these functions help keep the code clean and simple
# these are all postional arguments and need to be read in one spot!!
# to avoid confusion you would spefy which prameyer is being called