# Import necessary libraries

import sys

import matplotlib.pyplot as plt
import pykx as kx

"""
CSV format example
datetime,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""


def create_histogram(csv_file_path):
    # Upload a CSV file into a kdb+ table
    kx.q(f'trades: ("PSFJ";enlist ",") 0: `$":{csv_file_path}"')

    # Execute a qSQL query using xbar to bucket the minutes into hours
    trades_table = kx.q('select trade_count:count i by time:60 xbar datetime.minute from trades')

    # Seamless integration with existent Python code (pandas and Matplotlib libraries)

    # Transform to a pandas.DataFrame instance
    df = trades_table.pd()
    print(df)

    # Set window title using a temporary figure
    fig = plt.figure()
    fig.canvas.manager.set_window_title("Intraday Analysis")

    # Aggregate and plot
    volume_by_time = df.groupby('time')['trade_count'].sum()
    volume_by_time.plot(kind='bar')

    # Set labels and title using plt (global interface)
    plt.title("Intraday Trading Volume Histogram")
    plt.xlabel("Hour")
    plt.ylabel("Total Size")

    # Style tweaks
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python histogram_creator_q.py </path/to/file/trades.csv>")
        sys.exit(1)
    create_histogram(sys.argv[1])
