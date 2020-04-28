"""Random Walk"""
from random import choice

import matplotlib.pyplot as plt

class RandomWalk:
    """A class to generate random walk."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks starts at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def main(self, visual_way):
        """Generating multiple random walk and visualize it."""
        while True:
            rw = RandomWalk()
            rw.fill_walk()
            if visual_way == 'scatter':
                rw.scatter_visual()
            elif visual_way == 'plot':
                rw.plot_visual()

            keep_running = input("Make another walk? (y/n): ")
            if keep_running == 'n':
                break

    def fill_walk(self):
        """Calculate all the points in the walk."""
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()
            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            x_values = self.x_values[-1] + x_step
            y_values = self.y_values[-1] + y_step

            self.x_values.append(x_values)
            self.y_values.append(y_values)

    def get_step(self):
        """Determine the direction and distance for each step."""
        direction = choice([1, -1])
        distance = choice(range(9))
        step = direction * distance
        return step

    def scatter_visual(self):
        """Scatter the points in the walk."""
        plt.style.use('classic')
        fig, ax = plt.subplots(figsize=(15, 9))
        point_numbers = range(self.num_points)
        ax.scatter(self.x_values, self.y_values, c=point_numbers,
                   cmap=plt.cm.Blues, edgecolors='none', s=10)

        # Empasize the first and last points.
        ax.scatter(0, 0, c='green', edgecolors='none', s=100) # starting point
        ax.scatter(self.x_values[-1], self.y_values[-1],
                   c='red', edgecolors='none', s=100) # ending point

        self.show(ax)

    def plot_visual(self):
        """Plot the points in the walk."""
        plt.style.use('seaborn')
        fig, ax = plt.subplots(figsize=(15, 9))
        ax.plot(self.x_values, self.y_values, linewidth=1)

        # Empasize the first and last points.
        ax.scatter(0, 0, c='green', edgecolors='none', s=100) # starting point
        ax.scatter(self.x_values[-1], self.y_values[-1],
                   c='red', edgecolors='none', s=100) # ending point

        self.show(ax)

    def show(self, plot):
        """Show the graph."""
        # Remove the axes.
        plot.get_xaxis().set_visible(False)
        plot.get_yaxis().set_visible(False)

        #plt.show()
        plt.savefig('cube_plot.png', bbox_inches='tight')

RandomWalk(10_000_000).main('scatter')
#RandomWalk(5000).main('plot')
