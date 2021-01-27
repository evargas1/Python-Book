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

    def describe_rest(self):
        print(self.resturant_name.title() + " cool place to pick!!")
        print(self.cuisne_type.title() + " love it too!!")
        
  

    def open_resturant(self):
        """Will let you know we are open"""
        print("We are open today at 1" )



class User():
    """will be the infomation for a user portfilo."""
    def __init__(self, first_name, last_name, age, height, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.location = location


    def describe_user(self):
        """Prints all the general infomation"""
        print("Your first name: \t " + self.first_name.title())
        print("Your last name: \t" + self.last_name.title())
        print("You are " + str(self.age) + " years old cool!")
        print("Wow you are " + str(self.height) + " cm tall.")
        print("Loacted: \t" + self.location.title())


    def welcome_mess(self):
        """welcome message to all new users"""
        print("Hey welcome to the home page once again! " + self.first_name.title())





my_rest = Resturant('night stars', 'kimbap')
print("My family owned resturant is called " + my_rest.resturant_name.title() + ".")
print("Its main cusine is called the " + my_rest.cuisne_type.title() + "!")
my_rest.open_resturant()

my_rest_2 = Resturant('cloudy day', 'fried rice', 'chicago', 3.4)
print("This small hidden gem is called " + my_rest_2.resturant_name.title())
print("Main cuisne " + my_rest_2.cuisne_type.title() + " sounds yummy!!")
print("We are loctaed in " + my_rest_2.city.title())
print("Our current rating is " + str(my_rest_2.rating))
my_rest_2.open_resturant()
my_rest.describe_rest()

student_1 = User('estrella', 'vargas', '17', '172', 'chicago')
student_1.describe_user()

student_2 = User('tiara', 'harris', 25, 180, 'south korea')
student_2.describe_user()
student_2.welcome_mess()

print("\n Alternative way to write \n")
print("Hey so your first name is " + student_2.first_name.title() + " nice to meet you!")
print("on record your last name is " + student_2.last_name.title() + ".")
print("You are currently " + str(student_2.age))
print("You are so tall " + str(student_2.height))
print("Lastly staioned in " + student_2.location.title())

print("\n Exmaple #3 \n")

student_3 = User('meredith', 'grey', 40, 150, 'seattle')
student_3.describe_user()
student_3.welcome_mess()
print("Hey so your first name on record is " + student_3.first_name.title() + " nice to see you!!")
print("Last name: " + student_3.last_name.title())
print("It appears you are " + str(student_3.age) + " years old.")
print("Its okay you are only " + str(student_3.age) + "cm tall.")
print("I live in " + student_3.location.title() + " the best city!")


class Car():
    """This will return info on a new car"""

    def __init__(self, model, color, year):
        """ Initializing all the sttributes to describe a car"""
        self.model = model
        self.color = color
        self.year = year
        # setting a default value / optional value
        self.odometer = 0

    def desriptive_name(self):
        """Will print one statment with all the car info"""
        print("Your car: " + self.model.title() + " " +  self.color.title() +  " " + str(self.year))

    def odometer_milage(self):
        """Print showing cars milage default value 0"""
        print("This car has " + str(self.odometer) + " miles.")


print("\nThis will begin the car example \n")
my_car = Car('honda', 'green', 2003)
my_car.desriptive_name()
my_car.odometer_milage()