try:
    print(5/0)
    # that was confusing for me beacuse I am bad at math
except ZeroDivisionError:
    print("You can't divide by zero silly!")

print("\nGive me two numbers and Ill divide them fo you!")
print("Enter 'q' to exit a break")

# while True:
#     first_number = input("Your first number: \t")
#     if first_number == 'q':
#         break
    
#     second_number = input("Your second number: \t")
#     if second_number == 'q':
#         break

#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError :
#         print("You can't divide by zero silly!")
#     except ValueError:
#         print("You cant use a letter silly!")
#         # will provide a message if a letter is used instead of a #
#     else:
#         print(answer)

file_name = 'alice.txt'


def count_words(file_name):
    """will count the amount of words in a txt file and can handle exceptions"""
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # msg = ("Im sorry it seems " + file_name + " does not exist.")
        # print(msg)
        pass
    # tp just continue running as normally
    else:
        words = contents.split()
        see_words = len(words)
        print("The file " + file_name + " has about " + str(see_words) + " words.")


file_names = ['alice.txt', 'mirror.txt', 'moby_dick.txt', 'little_women.txt']
for file in file_names:
    count_words(file)
# these files have millions of words an the computer read them in seconds.
    

# the purpose of try blocks is to make sure the user never sees 
# a traceback erroe since they will likely not know how to interpet it
print("\nHey please type two numbers and we will add them for you")

# while True:
#     first_number = input("Please give us a number: \t")
#     second_number = input("Please give us a second number:\t ")
#     try:
#         answer = int(first_number) + int(second_number)
#     except ValueError:
#         print("Sorry it seems you typed a letter try again!")
#     else:
#         print(answer)


def show_words(filename):
    """will print every word in a small files"""

    try:
        with open(filename) as file_object:
            contents = file_object.read()
            list_form = contents.split()
    except FileNotFoundError:
        pass
    else:
        for item in list_form:
            print(item)


filename = 'mouse.txt'
show_words(filename)

