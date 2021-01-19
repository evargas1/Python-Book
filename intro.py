import this


message = ("hello python world")
print(message)


message = ("Hello python world interperter")
print(message)

name = "ada lovance"
print(name.title())

first_name = "suga"
last_name = "yoongi"
fulle_name = first_name + " " + last_name

greeting = "Hello, " + fulle_name.title() + "!"
print(greeting)
print("python")
print("\tpython")
# to create a space
print("python is a \n great lang ")

fav_lang = "   python is the best  "
print(fav_lang)
fav_lang = fav_lang.rstrip()
print(fav_lang)
fav_lang = fav_lang.lstrip()
print(fav_lang)

age = 24
happy_mes = "Happy " + str(age) +"th Birthdau"
print(happy_mes)

print(5 + 3)
print(10 - 2)        
print(4 * 2)
print(16 / 2)
# python comment are a life saver no every lang that has comments are aweome.
# also works well for testing by just commenting code out
fav_number = 14
fav_message = "My favorite number has always been " + str(fav_number) + " I have also liked this number"
print(fav_message)

bible_chara = ['Ester', 'Samuel', 'David', 'Mary', 'Joseph']

print(bible_chara[1].title())
print(bible_chara[0].title())
print(bible_chara[4].title())

print(bible_chara[-1].title())
print(bible_chara[-2].title())

# my message to the bible charcters that i love the most

ester_mess = "Why do I love " + str(bible_chara[0].title()) + " so much good question she was courgeous" 
print(ester_mess)
samuel_mess = str(bible_chara[1].title()) + " was an excellent example of a faithful servent he also found David"
print(samuel_mess)
david_mess = "when you think of Samuel you cant help thing of repentent " + str(bible_chara[2].title())
print(david_mess)
parents = "the best parents ever the one and only " + str(bible_chara[3].title()) + " " + str(bible_chara[4].title())
print(parents)


bible_chara.append('Moses')
print(bible_chara)

bible_chara.insert(0, 'Job')
print(bible_chara)
del bible_chara[1]
print(bible_chara)

popped_var = bible_chara.pop()
print("Sadly one person had to be removed and that was " + popped_var.title())


print(bible_chara)

first_popped = bible_chara.pop(3)
print("I need to remove a character from this list " + first_popped)
print(bible_chara)

too_expensive = 'David'
bible_chara.remove(too_expensive)
print(bible_chara)
print("He lived a great life did some sketch stuff but its okay " + too_expensive.title() + ".")