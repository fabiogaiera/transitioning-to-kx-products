# Import necessary libraries

import matplotlib.pyplot as plt


def create_histogram(df):
    # Set window title using a temporary figure
    fig = plt.figure()
    fig.canvas.manager.set_window_title("Intraday Analysis")

    # Aggregate and plot
    volume_by_time = df.groupby('datetime')['i'].sum()
    volume_by_time.plot(kind='bar')

    # Set labels and title using plt (global interface)
    plt.title("Intraday Trading Volume Histogram")
    plt.xlabel("Hour")
    plt.ylabel("Total Size")

    # Style tweaks
    plt.grid(True)
    plt.tight_layout()
    plt.show()
