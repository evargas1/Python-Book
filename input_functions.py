# modulo method 

# number = input("Give me a number and I will tell you if its even or odd!")
# number = int(number)

# if number % 2 == 0:
#     print("The number " + str(number) + " is even.")
# else:
#     print("The number " + str(number) + " that you entered is odd.")

# type_car = input("What kind of car are you looking for? ")
# print("I will seach for any cars that are " + type_car)

# welcome to Rudinas resturnat !!
# welcome_greeting = ("Welcome to Rudinas retsurnat how mnay are in your party? ")
# enter_amount = input(welcome_greeting)
# enter_amount = int(enter_amount)

# if enter_amount <= 8:
#     print("Great! Come this way your table is ready.")
# else:
#     print("I am sorry your party of " + str(enter_amount) + " will have to wait for about 30min.")

# give me a number and I will tell you if its a mutiple of 10
# number_intro = ("Give me a number and I will tell you if its a mutiple of 10  ")
# num = input(number_intro)
# num = int(num)
# spacing is so important otherwise the output looks crazy 
# if num % 10 == 0:
#     print("The number " + str(num) + " that you entered is divisble by 10")
# else:
#     print("Im sorry it seems the number " + str(num) + " you entered is not divisable by 10")



# moving items from one list to another using the while loop
unconfirmed_users = ['alice45', 'dan7', 'janetgg1']
confirmed_users = []

while unconfirmed_users:
    if len(unconfirmed_users) > 0:
        current_user = unconfirmed_users.pop()
        
        print("Verfying to check if " + current_user.title() + " is avaiable")
        
        confirmed_users.append(current_user)
    else:
        break

print(confirmed_users, len(confirmed_users))
print("\nThe following users have been confirmed: ")
for user in confirmed_users:
    print(user)

pets = ['cat', 'dog', 'rabbit', 'cat', 'monkey', 'cat']
while 'cat' in pets:
    pets.remove('cat')

# will print the new list without cat in it gone 4ever
print(pets)

# mountain function exmaple saving responese an a emoty dictionary 
# print("\nThe empty dictionary exmpale will begin: ")

# responses = {}
# active_poll = True

# while active_poll:
#     name = input("\nTo start please give us your name: \t")
#     mountain = input("\nWhich mountain would you like to climb: \t")

#     responses[name] = mountain

#     again = input("Would someone else like to enter their poll? (Yes/No) \t")
#     if again == 'no':
#         active_poll = False

# for name, mountain in responses.items():
#     print("Great so " + name.title() + " wants to climb " + mountain.title() + " one day!")

sandwhich_orders = ['subway', 'new york', 'jason delis', 'kathys deli', 'marinos', 'new york', 'indian burritos', 'new york']
finished_sandwhitchs = []

# first removed new york deli and than continued with the function as normal
print("Im sad to say but " + sandwhich_orders[-1].title() + " have gone out of bizzz")

while 'new york' in sandwhich_orders:
    sandwhich_orders.remove('new york')

while sandwhich_orders:
    if len(sandwhich_orders) > 0:
        under_inspection = sandwhich_orders.pop()
        print("\n Hey we are currently inspecting " + under_inspection + ".")

        finished_sandwhitchs.append(under_inspection)
    else:
        break
print("\nThese places have all passe inspection")
for place in finished_sandwhitchs:
    print(place )
print("There are a total of " + str(len(finished_sandwhitchs)) + " places still open")

results = {}
active = True
while active:
    name = input("Hi to start survey we need your name \t")
    print("Great hey " + name.title())
    response = input("Were would you like to go on vacation? \t")
    results[name] = response

    repeat = input("\nWould someone else like to try? (yes/no) \t")
    if repeat == 'no':
        active = False

for name, response in results.items():
    print("Great so " + name.title() + " wants to visit " + response.title())







