with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())


filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        # this prints every line individually and strips 
        # any blank lines!

with open(filename) as file_object:
    lines = file_object.readlines()

# this method is effective because it allows you to work
# with the file outside of the while loop.
for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()
# the rstrip also removed all the spaces!
print(pi_string)
print(len(pi_string))