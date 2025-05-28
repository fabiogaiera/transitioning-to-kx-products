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
    # kx.q(f'trades: ("PSFJ";enlist ",") 0: `$":{csv_file_path}"')
    trades = kx.q.read.csv(csv_file_path, 'PSFJ')

    # Execute a qSQL query using xbar to bucket the minutes into hours
    # trades_table = kx.q('select count i by 60 xbar datetime.minute from trades')
    trades_table = trades.select(kx.Column('i').count(), by=kx.Column('datetime').minute.xbar(60))

    # Seamless integration with existent Python code (pandas and Matplotlib libraries)

    # Transform to a pandas.DataFrame instance
    df = trades_table.pd()
    # print(type(df))

    fig, ax = plt.subplots()

    df.groupby('datetime')['i'].sum().plot(kind='bar', ax=ax)

    ax.set_title("Intraday Trading Volume Histogram")
    ax.set_xlabel('Hour')
    ax.set_ylabel('Total Size')

    fig.canvas.manager.set_window_title("Intraday Analysis")

    plt.show()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python histogram_creator.py </path/to/file/trades.csv>")
        sys.exit(1)
    create_histogram(sys.argv[1])
