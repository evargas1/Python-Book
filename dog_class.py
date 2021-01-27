class Dog(object):
    """A simple attempt to model an object dog"""
    
    def __init__(self, name, age):
        """Will create the two main functions"""
        self.name = name
        self.age = age

    def sit(self):
        """Will make the dog sit"""
        print(self.name.title() + " is now sitting")

    def roll(self):
        """Will ensure the dog can roll on command"""
        print(self.name.title() + " has now rolled over")


my_dog = Dog('willie', 6)
our_dog = Dog('lucy', 3)
print("My dogs name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
# i dont understand how classes make writting the code effectieve
my_dog.sit()
my_dog.roll()
# okay I guess that is kinda cool it made the dog do stuff
print("Our dogs name is " + our_dog.name.title() + "!")
print("Our dog is " + str(our_dog.age) + " years old isn't she so young!!")

class Resturant():
    """Will show infomation on a cool resturant"""

    def __init__(self, resturant_name, cuisne_type, city='', rating=''):
        self.resturant_name = resturant_name
        self.cuisne_type = cuisne_type
        self.city = city
        self.rating = rating

    def open_resturant(self):
        """Will let you know we are open"""
        print("We are open today at 1" )


my_rest = Resturant('night stars', 'kimbap')
print("My family owned resturant is called " + my_rest.resturant_name.title() + ".")
print("Its main cusine is called the " + my_rest.cuisne_type.title() + "!")
my_rest.open_resturant()

my_rest_2 = Resturant('cloudy day', 'fried rice', 'chicago', '3.4')
print("This small hidden gem is called " + my_rest_2.resturant_name.title())
print("Main cuisne " + my_rest_2.cuisne_type.title() + " sounds yummy!!")
print("We are loctaed in " + my_rest_2.city.title())
print("Our current rating is " + my_rest_2.rating)