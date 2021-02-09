import matplotlib.pyplot as plt

x_values = list(range(1, 501))
y_values = [x**3 for x in x_values]
# the ** stars raises numbers to the power of and
# than the number you put after it is teh power
# you need it raised too

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, edgecolor='none')
# the more plots it is the straighter the lines

plt.title("Cubed Graph", fontsize=15)
plt.xlabel("Values", fontsize=10)
plt.ylabel("Cubed Values", fontsize=10)



plt.show()