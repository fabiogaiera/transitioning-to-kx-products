# Import necessary libraries
import pykx as kx

"""
CSV format example
timestamp,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""


def create_dataframe(csv_file_path, market_open_timespan, market_close_timespan):
    # Upload a CSV file into a kdb+ table
    # P stands for timestamp
    # S stands for symbol
    # F stands for float
    # J stands for long
    kx.q(f'trades: ("PSFJ";enlist ",") 0: `$":{csv_file_path}"')

    kx.q(f'trades: update date: `date$timestamp from trades')

    kx.q(f'trades: update mo: date + {market_open_timespan}, mc: date + {market_close_timespan} from trades')

    kx.q(f'trades: select from trades where timestamp within (mo; mc)')

    aggregation = kx.q(f'select open: first price, high: max price, low: min price, close: last price, volume: sum size by date from trades ')

    return aggregation.pd()
