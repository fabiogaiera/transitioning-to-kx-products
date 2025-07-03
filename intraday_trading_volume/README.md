# Intraday Trading Volume

In this brief example, I’d like to share a real-world use case that I’ve encountered in my work experience: how to build
an intraday trading volume histogram using kdb+ along with Python technologies.

Assuming you've successfully installed kdb+ and PyKX, you can proceed with building the histogram as follows:

```python
# trades_dataframe_creator.py

# Import necessary libraries
import pykx as kx

"""
CSV format example for trades
datetime,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""


def create_dataframe(csv_file_path):
    # Upload a CSV file into a kdb+ table
    trades = kx.q.read.csv(csv_file_path, 'PSFJ')

    # Execute a qSQL query using xbar to bucket the minutes into hours
    trades_table = trades.select(kx.Column('trade_count', value=kx.Column('i').count()),
                                 by=kx.Column('time', value=kx.Column('datetime').minute.xbar(60)))

    # Transform to a pandas.DataFrame instance
    return trades_table.pd()
 ```

```python 
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
```

**Potential enhancements for this use case:**

- In real-world scenarios, kdb+ tables are partitioned. This allows to achieve an optimal performance when storing /
  retrieving kdb+ data.

- Consider building a kdb+tick architecture when creating a real-time database and historical
  database with tick data.

**Alpaca Trading API Documentation (Required in case you want to download market data)**

Historical trades (single symbol): [Stock Trades](https://docs.alpaca.markets/reference/stocktradesingle-1)

**KX Documentation**

Database and Programming Language: [kdb+ and q](https://code.kx.com/q)

Python interface library: [PyKX](https://code.kx.com/pykx)