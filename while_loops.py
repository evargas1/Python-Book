# message = input("Tell me something about you and I will repeat ith back: ")
# print(message)

# name = input("Please tell me your name: ")
# print("Hello! " + name)

# prompt = "If you tell me who you are, we can perosonalize this message to you."
# prompt += "\nWhat is your name? "

# name = input(prompt)
# print("\nHello! " + name)
# age = input("How old are you? ")

# print(int(age) == 18)
# it is a string because if it wasnt it would print error 

# rollercoatster example
# height = input("How tall are you? ")
# height = int(height)

# if height >= 178:
#     print("You are tall engough to ride the rides have fun!")
# else:
#     print("Im sorry you are tall engough to ride the rides")


# # second prompt statement
# prompt = "Hey! If you enter a message I will keep repeating it! "
# prompt += "Type quit to end program "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# its a bit more lines of code but looks much cleaner and makes editing easier

# we are going to use a loop with the while True function
# pro = ("\nWe are doing a survery. Which cities have you been to? ")
# pro += ("If you would like to stop type, quit------")

# while True:
#     city = input(pro)

#     if city == 'quit':
#         break
#     else:
#         print("\nWow I would love to go to " + city.title() + "!")

latest_num = 0
while latest_num < 10:
    latest_num += 1
    if latest_num % 2 == 0:
        continue
    print(latest_num)
print("\nNext opperation of code")
x = 1
while x <= 5:
    print(x)
    x += 1
# careful with infinite loops not never make those mistakes just try and find them fast when you do make them!
print("\nThis will start the pizza function")
pizza_toppings = ("What toppings would you like on your pizza?")
pizza_toppings += (" If you are done type quit \n")

# active = Truemu
# while active:
#     message = input(pizza_toppings)
    
#     if message == 'quit':
#         active = False
#     else:
#         print("I will add " + message + " to your pizza anything else? ")
# this is how i chose to write my function alternate solution will also be made now

# message = ""
# while message != 'quit':
#     message = input(pizza_toppings)

#     if message != 'quit':
#         print("I will add " + message + " to your pizza anything else? ")
# that is crazy both functions work exactly the same!!!!! there are so many ways to solve things
# i pefer the top way but thats just me

message = ""
while message != 'quit':
    message = input(pizza_toppings)

    if message == 'quit':
        break

    print("I will add " + message + " to your pizza anything else?")
# there is a solid three ways to solve this problem all work but they work differently
# best way in my opinion is the active true and fasle 

print("\nMovie problem")
movie_mes = ("Hey how old are you? \n")
age = input(movie_mes)
age = int(age)

if age < 3:
    price = 0
elif age < 12:
    price = 10
else:
    price = 15

print("Hey, so you are " + 
str(age) + 
" years old so your ticket today will be $" + 
str(price) + 
" enjoy!")

number_run = 0
while number_run < 20:
    number_run += 1
    if number_run % 3 != 0:
        continue
    
    print(number_run)


    
