import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
sqaures = [1, 4, 9, 16, 25]

plt.title("Sqaure Numbers", fontsize=25)
plt.plot(input_values, sqaures, linewidth=5)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Exponent of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=12)
# this top function afffects the size of the numbers on the graph

plt.show()