# show the length and remove the word the from this sentence
# using list comphensions 

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)

show_words = [x for x in words if x!="the"]
print(show_words)
print(len(show_words))
again_see_words = [x for x in sentence.split() if x !="the"]
print(again_see_words)
print(len(again_see_words))
# yes it worked good!
# but this was an easy list comphensions 
# i need to do something harder 



# the list should only print postieve integers

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# for num in numbers:
#     if num >= 0:
#         newlist.append(num)
newlist = [x for x in numbers if x>=0]
print(newlist)
print(len(newlist))


# I made some up for you!
# Find all of the numbers from 1-1000 that are divisible by 7

# for num in range(1, 1001):
#     if num % 7 == 0:
#         divisible_by.append(num)
divisible_by = [x for x in range(1000) if x%7==0 ]
print(len(divisible_by))


# Find all of the numbers from 1-1000 that have a 3 in them

# contains_three = []
# for num in range(1001):
#     if '3' in str(num):
#         contains_three.append(num)

# print(contains_three)
# print(len(contains_three))

cotanins = [x for x in range(1001) if '3' in str(x)]
print(cotanins)
print(len(cotanins))

# Count the number of spaces in a string

my_example = "Gods name is Jehovah, it means he causes to become"

x = my_example.count(' ')
print(x)

number_of_spaces = [my_example.count(' ')]
print(number_of_spaces)
# it just printed the number to a list 


# Remove all of the vowels in a string

my_sec_example = "Gods name helps us understand the theme of the Bible"
print(my_sec_example)



vowel = ('a', 'i', 'e', 'o', 'u')
for letter in my_sec_example:
    if letter in vowel:
        my_sec_example = my_sec_example.replace(letter, ' ')

print(my_sec_example)

my_list = [x for x in my_sec_example if x not in ('a', 'o', 'u', 'i')]

print(my_list)

        

# Find all of the words in a string that are less than 4 letters
less_than = ("Hello my name is Daniel it is very nice to meet you")
short_words = []
four_letter = list(less_than.split(" "))
print(four_letter)
for word in four_letter:
    if len(word) < 4:
        print(word)
        short_words.append(word)
print(short_words)

# i feel like there is a much shorted 
# way to do this but i chose the complicated way 

semi_words = [x for x in less_than.split(' ') if len(x)<4]
print(semi_words)
# there was a way easier way to do this with one statment 


# Challenge:
# Use a dictionary comprehension to count the length of each word in a sentence.

# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
# For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by