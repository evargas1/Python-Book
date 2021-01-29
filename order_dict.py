from collections import OrderedDict
from random import randint

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'ruby'
favorite_languages['sam'] = 'python'
favorite_languages['janet'] = 'java'
favorite_languages['robin'] = 'javascript'

for name, lang in favorite_languages.items():
    print(name.title() + "'s favorite coding languange is " + lang.title())


glossary = OrderedDict()
glossary['tuples'] = 'a umutable list that is repsented with ()'
glossary['list'] = 'stores infomation in order repsented with []'
glossary['attribute'] = 'value in a class that is the main'
glossary['method'] = 'function inside a class'
glossary['instance'] = 'calling a class and any methods in it'

for word, meaning in glossary.items():
    print(word.title() + " -------- " + meaning)

# x = randint(1, 10)
# print(x)

class Dice():
    """model a game with a dice"""
    def __init__(self, sides=6):
        """initalize attributes"""
        self.sides = sides

    def roll_dice(self):
        """will roll dice and print a random number"""
        self.sides = randint(1, 6)
        print(self.sides)

game = Dice(6)
game.roll_dice()

class DiceTen():
    """model a game with a dice that has 10 sides"""
    def __init__(self, sides=10):
        """Initailize attributes to start"""
        self.sides = sides

    def roll_dice(self):
        """random number between 1-10"""
        self.sides = randint(1, 10)
        print(self.sides)

game2 = DiceTen()
game2.roll_dice()

class Die():
    """model a dice game with 20 sides"""
    def __init__(self, sides=20):
        """Intialize the main attributes"""
        self.sides = sides

    def roll_dice(self):
        """will roll a random number"""
        self.sides = randint(1, 20)
        print(self.sides)
        

game3 = Die()
game3.roll_dice()