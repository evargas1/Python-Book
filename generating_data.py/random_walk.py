from random import choice


class RandomWalk():
    """A class to generate random walks """

    def __init__(self, num_points=5000):
        """initalize attributes of a walk"""
        self.num_points = num_points


# all walks start at the point (0,0)
        self.x_values = [0]
        self.y_values = [0]
    
       
    def get_step(self):
        """will include the code for this program to run"""

        direction = choice([1, -1])
        # telling the choice function to pick from these options
        step_size = choice([1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * step_size

        return(step)



    def fill_walk(self):
        """will calcualte the number of random steps"""
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # reject the cordinates if they are both 0
            if x_step and y_step == 0:
                continue

            # will begin the process of appending to the list
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


janet = RandomWalk()
janet.fill_walk()



