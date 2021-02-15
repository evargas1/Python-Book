import lxml
from random import randint
import pygal

class Die():
    """A class for rolling a dice with 6 sides"""
    def __init__(self, sides=6):
   
        self.sides = sides

    def roll(self):
        """retirns a random number between 1 and the num of sides"""
        return randint(1, self.sides)





die = Die()

# dice_results = []
# for roll_num in range(1000):
#     # for some reason the range function when up to and including
#     results = die.roll()
#     dice_results.append(results)
dice_results = [(die.roll()) for x in range(500) ]


# freq = []
# for value in range(1, die.sides+1):
#     # for some reason this function is up to but not including
#     amount = dice_results.count(value)
#     # in order for the count function to work 
#     # it needs to be saved to a variable
#     freq.append(amount)
freq = [(dice_results.count(x)) for x in range(1, die.sides+1)]

print(dice_results)
print(len(dice_results))
print(freq)

# visulaize the chart

hist = pygal.Bar()


hist.title = "Results of rolling one dice 1,000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Different Sides of The Dice"
hist.y_title = "Frequency of Results"

hist.add('D6', freq)

hist.render_to_file('please_Work.svg')
