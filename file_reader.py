# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())


# filename = 'pi_million_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()
# # this method is effective because it allows you to work
# # with the file outside of the while loop.


# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# # the rstrip also removed all the spaces!
# print(pi_string[:52] + "...")
# print(len(pi_string))

# print("\nCutie birthday function \n")

# birthday = input("Please enter your birthday? (mmddyy) \t")
# if birthday in pi_string:
#     print("Congrats your birthday appears in the one million digits of pi!")
# else:
#     print("Sorry your birthday does not appear in pi.")


# readlines makes it a list to work with throughtout the code
sec_file_name = 'learned_in_python.txt'
with open(sec_file_name) as file_object:
    lines = file_object.readlines()

print(lines)


pi_string = ''
for line in lines:
    pi_string += line


for sent in pi_string:
    print("The main " + sent)

print(pi_string)
print(len(pi_string))
# this one whipped my but thank god for google
# i would have never though to write this method this way
# iteriated over every line to find the word!
for value in lines:
    x = value.replace('python', 'ruby')
    print(x)
        












