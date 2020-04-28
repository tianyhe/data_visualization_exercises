"""Plotting a simple line graph."""
import matplotlib.pyplot as plt

def main():
    """Plotting a line graph with given."""
    input_values = [1, 2, 3, 4, 5]
    output_values = [1, 8, 27, 64, 125]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(input_values, output_values, linewidth=3)

    # Set chart title and label axes.
    ax.set_title("Cubic Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Cubic of Value", fontsize=14)

    # Set size of tick labels.
    ax.tick_params(axis='both', labelsize=14)

    plt.show()

main()
