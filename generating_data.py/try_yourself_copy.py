import matplotlib.pyplot as plt

from random_walk import RandomWalk

# make a random walk and plot the points


while True:

    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))

    #  set the size of the plotting window 
    plt.figure(figsize=(10, 6))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
         cmap=plt.cm.Blues, edgecolors='none', s=1)
    # plt.plot(rw.x_values, rw.y_values, linewidth=1)

    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # -1 stands for the last point on the list

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    print(len(point_numbers))


    plt.show()