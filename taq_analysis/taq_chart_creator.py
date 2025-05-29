import sys

import matplotlib.pyplot as plt

from taq_dataframe_creator import retrieve_taq_dataframe_pykx
from taq_dataframe_creator import retrieve_taq_dataframe_q


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

    data_frame = retrieve_taq_dataframe_pykx(sys.argv[1], sys.argv[2])
    # data_frame = retrieve_taq_dataframe_q(sys.argv[1], sys.argv[2])
    create_taq_chart(data_frame)
