# Intraday Trading Volume

While migrating tick data from OneTick to kdb+, one of the more straightforward aspects is handling raw trade and quote
data. This is because such data can often be re-sourced from market data providers. Therefore, the main focus during
migration lies in rethinking the architecture of the data analytics platform itself.

By shifting from OneTick Query Language to the q programming language, teams can take full advantage of kdb+’s
performance and expressiveness, among other powerful features. This transition also enables seamless integration with
existing Python-based analytics platforms through PyKX, resulting in a more flexible and scalable architecture.

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
    trades_table = trades.select(kx.Column('i').count(), by=kx.Column('datetime').minute.xbar(60))

    # Transform to a pandas.DataFrame instance
    return trades_table.pd()
```

```python 
# volumes_histogram_creator.py

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
```

