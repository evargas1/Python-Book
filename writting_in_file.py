# filename = 'programming.txt'
# with open(filename, 'a') as file_object:
#     file_object.write("Welcome to this new small folder\n")
#     file_object.write("We hope you can stay with us for awhile.\n")

# if the file does not exist this above function will immediatly
# create and save the info you need in it

# filename = 'guest.txt'
# name = input("What is your name?\t")
# with open(filename, 'a') as file_object:
#     file_object.write(name.title())

# filename = 'guestbook'

# active = True
# while active:
#     name = input("\nWhat is your name?\t")
    
#     with open(filename, 'a') as file_object:
#         file_object.write(name.title())

#     print("Thank you " + name.title() + " for logging on with us!")
    
#     again = input("\nWould you like to add another name? (yes/no)")
#     if again == 'no':
#         active = False
#     else:
#         active = True


filename = 'why_you_like_programming'

active = True
while active:
    response = input("What is one reason why you love programming? \t")

    with open(filename, 'a') as file_object:
        file_object.write(response.title())

    print("\nThank you for your response!")

    again = input("Would you like to enter another reason? (yes/no)")
    if again == 'no':
        active = False
    else:
        active = True

