import json

numbers = [34, 17, 7, 18, 9]

filename = 'numbers.json'

with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

with open(filename) as file_object:
    # if not speceified default action when file is called is to read
    numbers = json.load(file_object)

print(numbers)

# remeber user input data when stored inside of json
# username = input("Hey tell us your name? \t")

file_name = 'usernames_saved.json'
# with open(file_name, 'w') as file_object:
#     json.dump(username, file_object)
#     print("Thanks for logging on we will remeber you next time, " + username.title())

with open(file_name) as file_object:
    username = json.load(file_object)
    print("Hey welcome back " + username)