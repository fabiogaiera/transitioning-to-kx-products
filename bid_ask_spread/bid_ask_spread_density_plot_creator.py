# bid_ask_spread_density_plot_creator.py

import matplotlib.pyplot as plt
import seaborn as sns


def create_density_plot(df):
    # Create a new figure object
    fig = plt.figure()

    # Set the window title of the figure (only works in some GUI backends)
    fig.canvas.manager.set_window_title("Intraday Analysis")

    # Plot Kernel Density Estimate (KDE) of the 'bid_ask_spread' column
    sns.kdeplot(df['bid_ask_spread'], fill=True, color='purple', linewidth=2)

    # Set the plot title and axis labels with font size adjustments
    plt.title("Density Plot of Effective Bid-Ask Spread (%)", fontsize=14)
    plt.xlabel("Effective Bid-Ask Spread (%)", fontsize=12)
    plt.ylabel("Density", fontsize=12)

    # Add grid lines for easier readability
    plt.grid(True)

    # Adjust subplot params to give specified padding and prevent clipping of labels/titles
    plt.tight_layout()

    # Display the plot on the screen
    plt.show()
