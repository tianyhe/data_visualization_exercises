"""Die"""
from random import randint

from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die:
    """A class representing a sigle die."""

    def __init__(self, num_sides=6):
        """Initialize attributes of the die."""
        self.num_sides = num_sides
        self.results = 0
        self.frequencies = 0

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

    def mult_roll(self, numbers_roll=1):
        """Return results of x times rolling in a list."""
        self.numbers_roll = numbers_roll
        self.results = [self.roll() for num_roll in range(numbers_roll)]
        return self.results

    def frequency(self):
        """
        Count the frequency of each side with given results.
        """
        self.frequencies = [
            self.results.count(value) for value in range(1, self.num_sides + 1)
            ]
        return self.frequencies

    def one_die_histogram(self):
        """After rolling the die, visualize the results of the die roll."""
        x_values = list(range(1, self.num_sides + 1))
        data = [Bar(x=x_values, y=self.frequencies)]

        x_axis_config = {'title': 'Result'}
        y_axis_config = {'title': 'Frequencies'}
        my_layout = Layout(
            title=f"Results of rolling one D{self.num_sides} {self.numbers_roll} times",
            xaxis=x_axis_config, yaxis=y_axis_config
            )
        offline.plot(
            {'data':data, 'layout':my_layout},
            filename=f"d{self.num_sides}.html"
            )

# D6 = Die(6)
# results = D6.mult_roll(100)
# print(results)
# freq = D6.frequency()
# print(freq)
# D6.one_die_histogram()
