# volumes_histogram_creator.py

# Import necessary libraries
import matplotlib.pyplot as plt


def create_histogram(df):
    # Create a new figure object
    fig = plt.figure()

    # Set the window title of the figure (only works in some GUI backends)
    fig.canvas.manager.set_window_title("Intraday Analysis")

    # Aggregate and plot
    volume_by_time = df.groupby('time')['trade_count'].sum()
    volume_by_time.plot(kind='bar')

    # Set the plot title and axis labels with font size adjustments
    plt.title("Intraday Trading Volume Histogram", fontsize=14)
    plt.xlabel("Hour", fontsize=12)
    plt.ylabel("Total Size", fontsize=12)

    # Add grid lines for easier readability
    plt.grid(True)

    # Adjust subplot params to give specified padding and prevent clipping of labels/titles
    plt.tight_layout()

    # Display the plot on the screen
    plt.show()
