cars = ['audi', 'bmw', 'toyato', 'subaru']
for car in cars:
    if car == 'bmw':
     
        print(car.upper())
    else:
        print(car.title())

car = 'Audi'
print(car == 'audi')

print(car.lower() == 'audi')
print(car)

requested_topping = 'pepproni'
if requested_topping != 'mushrooms':
    print("Hold the mushrooms")

age = 17 
print(age == 17)
if age != 30:
    print("wrong number guess again")

print(age >= 15)
print(age <= 30)

age_0 = 20
age_1 = 17
print((age_0 >= 21) or (age_1 >= 21))

wanted_top = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in wanted_top)
print('sasuage' in wanted_top)

banned_users = ['tamyah', 'salama', 'tiara', 'trystan']
user = 'danny'
ex = 'Ely'
if user not in banned_users:
    print(user.title() + ", You are welcome to comment in this post.")
# boolean expressions are the same as true and false or condional statments

print("\nIs tamyah in the list of banned users: True")
print('tamyah' in banned_users)

print("\nIs krystal in the list of banned users: False")
print('kystal' in banned_users)

print("\nIs tiara in the list of banned users: True")
print('tiara' in banned_users)

print("\nis Salama in the list of banned users: False case sensetive")
print('Salama' in banned_users)

print("\n Is DANNY a valid user will change captilaztion to search for name: True")
print(user.upper() == 'DANNY')

print("\n Is Ely in the banned user list i will make lowercase before checking: True")
print(ex.lower() == 'ely')

print("\nIs susy not in banned users list: True")
print('suzy' not in banned_users)

print("\n Is SUZY not in banned users list: True")
print('SUZY' not in banned_users)

min_age = 18
max_age = 21

if min_age >= 18 and max_age <= 21:
    print("Congrtaultions you can make to the party")

print((min_age >= 18) and (max_age <= 20))
print((min_age >= 18) or (max_age <= 20))


cities_visted = ['chicago', 'san_diego', 'colima']
city = 'amsterdam'
if city not in cities_visted:
    print("\nYou have not not gone to " + city + " yet, plan this trip.")

if 'chicago' not in cities_visted:
    print("You have not gone to beligum yet plan this trip!")
else:
    print("You have already been here silly")
# you can assiagn it to a varaible for oraginzation and to keep track of it or 
# you can just test the string alone


# if condtional test:
# do something

new_age = 16
if new_age >= 18:
    print("\nYou are old enough to vote")
    print("Have you registered to vote yet? You are " + str(new_age) + " after all.")
else:
    print("\nSorry you are to young to vote you have to be 18")
# in a simple if and else chain something will always be done

age = 12

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $5")
else:
    print("You admission cost is $10")
# Although this code works its not easy to read and hard to modfiy

age_3 = 11
if age_3 < 4:
    price = 0
elif age_3 < 18:
    price = 5
else:
    price = 10

print("Your admission cost will be $" + str(price) + " have fun!")
# this is much easier to read and wull be easier to edit too


age_4 = 30
if age_4 < 4:
    price = 0
elif age_4 < 18:
    price = 5
elif age_4 < 65:
    price = 10
elif age_4 > 65:
    price = 5
print("Your admission cost will be $" + str(price) + " have fun!")
# There is an alternative way to write but not recommend
# ending with else is not idle
if age_4 < 4:
    price = 0
elif age_4 < 18:
    price = 5
elif age_4 < 65:
    price = 10
else:
    price = 5
# not an idle way to write because its left open at the end

# pizza example 
wanted_toppings = ['roni', 'cheese', 'spianch']
if 'mushrooms' in wanted_toppings:
    print("\nWe will be adding mushrooms")
if 'roni' in wanted_toppings:
    print("We will be adding roni to this")
if 'cheese' in wanted_toppings:
    print("We will be adding extra cheese")

print("\nFinished making your unique pizza")

print("\nThis will be the same exmple but with elif blocks")
if 'roni' in wanted_toppings:
    print("We will add roni to you pizza")
    # the code stops running here even though all the conditions are true
    # this is why using elif is only for one condition
    # if blocks will work for more than one block
elif 'cheese' in wanted_toppings:
    print("We will be adding cheese to this ")
elif 'spianch' in wanted_toppings:
    print("We will be adding cheese to this ")

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points")

if alien_color == 'yellow':
    print("You just earned -5 points")

alien = 'green'
if alien == 'green':
    print("You just earned 5 points good job")
else:
    print("You just earned 10 points good job")


# two different ways to solve this line code one more neat

if alien == 'green':
    print("Earned 5 points")
elif alien == 'yellow':
    print("You just earned 10 points")
else:
    print("you just earned 15 points")
# or a more efeective way i think to write this is 

if alien == 'green':
    print("You just earned 5 points")
elif alien == 'yellow':
    print("you just earned 10 points")
elif alien == 'red':
    print("You just earned 15 points")


life = 30
if life < 2:
    print("you are a baby")
elif life < 4:
    print("You are a toddler")
elif life < 13:
    print("You are a kid")
elif life < 20:
    print("You are a teenager")
elif life < 65:
    print("You are an adult sorry babe")
elif life > 65:
    print("You are an elder")

# fruits problem
fav_fruits = ['apple', 'strawberry', 'oranges', 'pineapple', 'mango']
if 'apple' in fav_fruits:
    print("Man you really like apples")
if 'banna' in fav_fruits:
    print("Man you really like bannas")
if 'oranges' in fav_fruits:
    print("Man bro oranges are yummy!")
if 'mango' in fav_fruits:
    print("Bro legit mangos are so good")
if 'pineapple' in fav_fruits:
    print("pineapples are good for you")

if life < 2:
    mes = 'baby'
elif life < 4:
    mes = 'toddler'
elif life < 13:
    mes = 'kid'
elif life < 20:
    mes = 'teenager'
elif life < 65:
    mes = 'sorry adult'
elif life > 65:
    mes = 'elder'
print("\nYou are " + str(life) + " years old that means in life you are a " + mes)

wanted_toppings = ['roni', 'cheese', 'spianch', 'olives']
for toping in wanted_toppings:
    print("Adding " + toping + ".")
print("Finsihed making your unique pizza")

for toping in wanted_toppings:
    if toping == 'cheese':
        print("Sorry we are going dairy free now!!")
    else:
        print("Adding " + toping + ".")

print("Finsihed making your unique pizza")

if wanted_toppings:
    # the function above checks to see if the list has items before running the for lope
    for toping in wanted_toppings:
        if toping == 'cheese':
            print("Sorry we are going diary free now")
        else:
            print("Adding " + toping + ".")
else:
    print("Plain pizza?")

# think of your own problem you can write to this code
pizzas_near_me = []
if pizzas_near_me:
    for place in pizzas_near_me:
        print("The " + place + " is near by you for a resturnat check it out")
else:
    print("No pizza places near you at the moment sorry")
# is a simple if and else that will alwasy produce a resul in your code 

avaialble_toppings = ['roni', 'sausage', 'mac_and_cheese', 'pineapple', 'spinach', 'vegatbles']
wired_topping = ['pineapple', 'spinach', 'banna']

print("\nStarting real life code for real world problem")

for top in wired_topping:
    if top in avaialble_toppings:
        print("Adding " + top + " to your pizza.")
    else:
        print("Sorry at the moment we dont have " + top)
print("\n Your pizza is done")

usernames = ['evargas11', 'dan45', 'jenna2', 'notmike30', 'admin']
if usernames:
    for user in usernames:
        if 'admin' == user:
            print("Welcome admin would you like to the status report")
        else:
            print("Welcome " + user + " this is your student portal")
else:
    print("We need to find some users NOW!!")

print("\nNext question")
current_users = ['janedoe', 'marie88', 'janetstop90', 'mericen', 'joesy5']
new_users = ['miranda', 'Joesy5', 'JANEDOE']
# assuming all the usernames are already saved in lower case forum i would change the new to .lower()

for new in new_users:
    if new.lower() in current_users:
        print("Sorry " + new + " this username is already taken, input a new one")
    else:
        print("This username is avaible!")

the_number_formal = list(range(1,10))
print(the_number_formal)
print("\nLooping through formal numbers")

for formal in the_number_formal:
    if formal == 1 :
        print(str(formal) + "st")
    elif formal == 2 :
        print(str(formal) + "nd")
    elif formal == 3: 
        print(str(formal) + "rd")
    else:
        print(str(formal) + "th")
# It works and its appearing all in seperste lines but it could be better

for formal in the_number_formal:
    if formal == 1:
        end = "st"
    elif formal == 2:
        end = "nd"
    elif formal == 3:
        end = "rd"
    else:
        end = "th"
    print("The formal way to all numbers is " + str(formal) + end)
# im sure there is an even faster way than this but 
# the second way looks much cleaner bravo 


        

