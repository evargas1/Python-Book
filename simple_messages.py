message_one = "This is going to be hard"
print(message_one)

# guest list 

guess_list = ['Joseph', 'Paul', 'Eve', 'Gabe', 'Abel', 'Peter', 'Esther']

evite = "You Have been invited to our dinner, "
print(evite + guess_list[0].title())
print(evite + guess_list[5].title())
print(evite + guess_list[-1].title())

print(len(guess_list))

guess_list[0] = 'Naomi'
print(guess_list)
print("sad to say Joseph can't make it something came up so our next guest will be " + guess_list[0].title())

print(guess_list[0].title() + " You have been invited hopefully you can make it!")
print("WE recived your resvp just sedning you a conifmration can't wait to see you, " + guess_list[-2].title())
print("Hopefully you can get back to us soon " + guess_list[-1].title())
print("Great news we just found a larger table guys some people are not avaiable. ")

guess_list.insert(0, 'Adam')
print(guess_list)

guess_list.insert(4, 'Timothy')
print(guess_list)

guess_list.append('Mary')
print(guess_list)


print("Im sorry to say the table for dinner will not be coming we apolgize for this!")

sorry_mess = "We are sorry, we will have you over soon, "
last_popped = guess_list.pop(-1)
print(sorry_mess + last_popped.title())
print(guess_list)


last_popped2 = guess_list.pop(-2)
print(sorry_mess + last_popped2.title())
print(guess_list)

last_popped3 = guess_list.pop(-1)
print(sorry_mess + last_popped3.title())
print(guess_list)

last_popped4 = guess_list.pop(-1)
print(sorry_mess + last_popped4.title())
print(guess_list)
last_popped5 = guess_list.pop(-1)
print(sorry_mess + last_popped5.title())
print(guess_list)
last_popped6 = guess_list.pop(-1)
print(sorry_mess + last_popped6.title())
print(guess_list)
last_popped7 = guess_list.pop(-1)
print(sorry_mess + last_popped7.title())
print(guess_list)
last_popped8 = guess_list.pop(-1)
print(sorry_mess + last_popped8.title())
print(guess_list)

# last message
last_mess = "You have been invited hopefully you can make it "
print(last_mess + guess_list[0].title())
print(last_mess + guess_list[1].title())

del guess_list[1]
del guess_list[0]
print(guess_list)

# the sort method will change the order of a list permentaly

char = ['Ester', 'Moses', 'David', 'Jonah']
print("Here is the orignal lise: ")
print(char)

print("\nHere is the sorted list: ")
print(sorted(char))
# this function will not actully change the order of the list it will just print it in a differnet order for you the user

print("\nHere is the orignal lise: ")
print(char)
char.reverse()
print(char)
print(len(char))

places = ['amsterdam', 'belium', 'poland', 'korea', 'peru']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
# there is no "." in this temp sorted method
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
# this function will permentaly sort the list
print(places)
places.sort(reverse=True)
print(places)

print(len(places))
print("I am happy to say these are the places i would love to go to its only " + str(len(places)) + " I can go to all easy.")

# if you were to use the sort revrse = True method it would change the list permently



