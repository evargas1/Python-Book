from random import randint
import pygal
from pygal.style import DarkSolarizedStyle

class Die():
    """A class for rolling a dice with 6 sides"""
    def __init__(self, sides=6):
   
        self.sides = sides

    def roll(self):
        """retirns a random number between 1 and the num of sides"""
        return randint(1, self.sides)


