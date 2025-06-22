# trades_dataframe_creator.py

# Import necessary libraries
import pykx as kx

"""
CSV format example
datetime,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""


def create_dataframe(csv_file_path):
    # Upload a CSV file into a kdb+ table
    kx.q(f'trades: ("PSFJ";enlist ",") 0: `$":{csv_file_path}"')

    # Execute a qSQL query using xbar to bucket the minutes into hours
    trades_table = kx.q('select trade_count:count i by time:60 xbar datetime.minute from trades')

    # Transform to a pandas.DataFrame instance
    return trades_table.pd()
