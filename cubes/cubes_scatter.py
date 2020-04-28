"""Plotting with scatter()."""
import matplotlib.pyplot as plt

def main():
    """
    Plot the cubic values of the first 5000 cubic numbers
    with scatter() and apply colormap.
    """
    x_values = range(1, 5001)
    y_values = [x**3 for x in x_values]

    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.RdPu, s=10)

    # Set chart title and label axes.
    ax.set_title("Cubic Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Cubic of Value", fontsize=14)

    # Set size of tick labels.
    ax.tick_params(axis='both', which='major', labelsize=14)

    # Set the range for each axis.
    ax.axis([0, 5000, 0, 5000**3])

    plt.show()
    #plt.savefig('cube_plot.png', bbox_inches='tight')

main()
