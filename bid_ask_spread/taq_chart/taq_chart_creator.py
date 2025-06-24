import matplotlib.pyplot as plt


def create_taq_chart(df):
    # Set the DataFrame index
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
