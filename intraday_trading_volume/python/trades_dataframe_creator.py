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


def create_dataframe(csv_file_path, date, market_open, market_close):
    # Upload a CSV file into a kdb+ table
    trades = kx.q.read.csv(csv_file_path, 'PSFJ')

    # Filter trades data by day
    intraday_trades = trades.select(
        where=(
                (kx.Column('datetime').cast('date')) == kx.q(date)
        )
    )

    # Filter trades data considering only market hours
    filtered_intraday_trades = intraday_trades.select(
        where=(
                (kx.Column('datetime') >= kx.q(market_open)) &
                (kx.Column('datetime') <= kx.q(market_close))
        )
    )

    # Execute a qSQL query using xbar to bucket the minutes into hours
    trades_table = filtered_intraday_trades.select(kx.Column('trade_count', value=kx.Column('i').count()),
                                                   by=kx.Column('time', value=kx.Column('datetime').minute.xbar(60)))

    # Transform to a pandas.DataFrame instance
    return trades_table.pd()
