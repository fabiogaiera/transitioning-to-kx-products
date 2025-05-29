import sys

import matplotlib.pyplot as plt
import pykx as kx

from benckmark_util import log_execution_time

"""
CSV format example
datetime,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""


@log_execution_time
def retrieve_taq_dataframe(csv_file_path_1, csv_file_path_2):
    # Using PyKX interface
    trades = kx.q.read.csv(csv_file_path_1, 'PSFJ')
    quotes = kx.q.read.csv(csv_file_path_2, 'PSFJFJ')
    # Key the table
    quotes = kx.q.xkey(['sym', 'datetime'], quotes)
    # As-Of Join
    taq_table = kx.q.aj(kx.SymbolVector(['sym', 'datetime']), trades, quotes)
    # Convert to pandas DataFrame
    return taq_table.pd()


def create_taq_chart(df):

    df.set_index('datetime', inplace=True)

    fig = plt.figure()
    fig.canvas.manager.set_window_title('Intraday Analysis')

    plt.plot(df.index, df['price'], label='Trade Price', color='blue')
    plt.plot(df.index, df['ask_price'], label='Ask Price', color='green')
    plt.plot(df.index, df['bid_price'], label='Bid Price', color='orange')

    plt.xlabel('Datetime')
    plt.ylabel('Price')
    plt.title('Trades and Quotes Chart')

    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python tag_chart_creator.py </path/to/file/trades.csv> </path/to/file/quotes.csv>")
        sys.exit(1)

    data_frame = retrieve_taq_dataframe(sys.argv[1], sys.argv[2])
    create_taq_chart(data_frame)
