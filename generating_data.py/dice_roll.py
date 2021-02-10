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


die = Die()

dice_results = []
for roll_num in range(1000):
    # for some reason the range function when up to and including
    results = die.roll()
    dice_results.append(results)


freq = []
for value in range(1, die.sides+1):
    # for some reason this function is up to but not including
    amount = dice_results.count(value)
    # in order for the count function to work 
    # it needs to be saved to a variable
    freq.append(amount)

print(dice_results)
print(len(dice_results))
print(freq)

# visulaize the chart

hist = pygal.Bar(style=DarkSolarizedStyle)

hist._title = "Results of rolling one dice 1,000 times"
hist._x_labels = ['1', '2', '3', '4', '5', '6']
hist._x_title = "Different Sides of The Dice"
hist._y_title = "Frequency of Results"

hist.add('D6', freq)
hist.render_to_file('die_visual.svg')