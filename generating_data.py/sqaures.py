import matplotlib.pyplot as plt 

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# for x in x_values:
#     y_vales = x**2
plt.title("Squares", fontsize=15)
plt.xlabel("value", fontsize=10)
plt.ylabel("sqaure vale", fontsize=10)

plt.tick_params(axis='both', labelsize=10)

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds,  edgecolor='none', s=40)
#  the c=() property can be used to creat custom colors for your lines
# the edgecolor none function allows you to get rid of certain
# colors around the dots.

# setting the range seems to cause a probelm
plt.axis([0, 1100, 0, 1100000])
plt.show()
# to save the graph you made
plt.savefig('squares_plot.png')

# set chart title and label the x and y axis





# set the range for each axis 



