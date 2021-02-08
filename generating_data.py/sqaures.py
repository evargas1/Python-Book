import matplotlib.pyplot as plt 

x_values = list(range(1, 1001))
y_values =[x**2 for x in x_values]

plt.scatter(x_values, y_values, s=20)


# set chart title and label the x and y axis
plt.title("Scatter Plots", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Scatter plot values", fontsize=14)


# set size  of tick labels
plt.tick_params(axis='both', labelsize=12)


plt.show()