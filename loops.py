qualitiess_of_paul = ['brave', 'patient', 'faithful']
for qaulitie in qualitiess_of_paul:
    # for every qaulity in qaulites of paul print out each of them
    print(qaulitie.title() + " what a beautiful qaulity!")
    print("I will strive to develop " + qaulitie.title() + ".\n")

print("Thank you Paul for showing me such beatiful qulities.")

# pizza exmaple 
pizzas = ['pepproni', 'superme', 'vegan']
for pizza in pizzas:
    print("I really like: " + pizza + " pizza.")

print("I really like these 3 types of pizzas: " + pizzas[0].title())
print("I really like these 3 types of pizzas: " + pizzas[1].title())
print("I really like these 3 types of pizzas: " + pizzas[2].title())

print("Man I must really like pizza")

# I think the book asked me to fo the 3 print statements to show me how useful loops are

# ANIMALS 
animals = ['dog', 'cat', 'bunny']
for animal in animals:
    print("A " + animal.title() + " would make a great pet!")

print("All these animals are domisated and would make a great pet!")

for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(3, 16, 3))
print(even_numbers)

sqaures = []
for value in range(1, 11):
    sqaure = value ** 2
    # although this method works lets write clear and simple code as clear as we can. MORE ORGANIZED
    sqaures.append(sqaure)

print(sqaures)

sqaured = []
for number in range(1, 11):
    sqaured.append(number ** 2)

print(sqaured)
# write this code which ever way seems easier for you to understand you can always go back later and make it more effiecent!


# list comphensions is what you will see most programmers using so they introduced it early
digits = [1, 30, 56, 80, 92, 44]
min(digits)
print(min(digits))
print(max(digits))
print(sum(digits))

boxes = [value ** 2 for value in range(1,11)]
print(boxes)
# it does work wutt
for digit in range(1, 21):
    print(digit)


# for num in range(1, 100000):
#     print(num)

# one_thosand = [value for value in range(1, 100000)]
# print(one_thosand)
# print(min(one_thosand))
# print(max(one_thosand))
# print(sum(one_thosand))

# long_num = []
# for ex in range(1, 100000):
#     long_num.append(ex)

# print(long_num)
# print(min(long_num))
# print(max(long_num))
# print(sum(long_num))

odd_numbers = []
for odd in range(1, 21, 2):
    odd_numbers.append(odd)

print(odd_numbers)

odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

for three in range(3, 30, 3):
    print(three)

three_list = list(range(3, 30, 3))
for thr in three_list:
    print(thr)

print(three_list)

boxes = [value ** 2 for value in range(1,11)]
print(boxes)

cubed = [box ** 3 for box in range(1, 11)]
print(cubed)

cubed_list = list(range(1, 11))
for corner in cubed_list:
    print(corner ** 3)

corner_list = []
for s in range(1, 11):
    corner_list.append(s ** 3)

print(corner_list)
print(cubed)

list_example = ['tamyah', 'salma', 'tiara', 'jael', 'taylor', 'robin']
print(list_example[0:3])
print(list_example[2:4])
# starts at 0 if not specified
print(list_example[:3])
# no end will stop at the end of the list
print(list_example[2:])
print(list_example[-3:])

print("All the players: ")
for player in list_example:
    print(player.title())
print("\nThe three main players: ")
for player in list_example[:3]:
    print(player.title())

# copying a list 
my_foods = ['fruit', 'coffee', 'water', 'donuts', 'tacos']
fiedns_foods = my_foods[:]
print(my_foods)
print(fiedns_foods)


print(len(my_foods[:3]))
print(my_foods[-3:])
print(my_foods[1:4])
print(len(my_foods))


my_pizza = ['pepproni', 'superme', 'vegan']
print(my_pizza, len(my_pizza))
friends_pizza = my_pizza[:]
print(friends_pizza)
# add an item to each list
my_pizza.append('icee')
friends_pizza.append('sausage')
print("\nMy friends fav pizza: " + str(friends_pizza))
print("\nMy fav pizza: " + str(my_pizza))


# print them using for loops I am going to try and use list comphensions for this 
boxes = [value ** 2 for value in range(1,11)]
print(boxes)

print("\nMy fave pizzas: ")
list_of_my_pizza = [food for food in my_pizza]
print(list_of_my_pizza)
# in this case the list comphensions is not the most effiecent way because it is already a list 
for p in friends_pizza:
    print("\nMy friends favorite pizzas: " + p)

# immutable list are refered to as tuples
# the differance between how list and tuples look is the fact that tuple uses ()

dimensions = (30, 60)
print(dimensions[0])
print("\norignal dimensions")
for d in dimensions:
    print(d)
# although they are immutable tuples can be overwritten by a new variable not idel

print("\n modified overwritting a variable this is valid: ")
dimensions = (10, 5)
for n in dimensions:
    print(n)
# i can not believe that worked lol
buffet_tuple = ('rice', 'noodles', 'mashed_poataoes', 'soda', 'chicken')
for buffet in buffet_tuple:
    print(buffet)

# buffet_tuple.insert(1, 'spicy_chi')
# print(buffet_tuple)
# error should arise
buffet_tuple = ('water', 'kimichi', 'mashed_poatoes', 'soda', 'chicken')
for b in buffet_tuple:
    print("This is the new re-wriiteen menu: " + b)
# tuples were not intended to be edited                     
                                



