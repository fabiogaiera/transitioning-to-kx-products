# bid_ask_spread_df_creator.py

import pykx as kx

from bid_ask_spread.benchmark_util import log_execution_time

"""
CSV format example for trades
timestamp,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""

"""
CSV format example for quotes
timestamp,sym,bid_price,bid_size,ask_price,ask_size
2025.05.23D08:00:00.001037561,IBM,257.03,2,260.91,1
2025.05.23D08:00:00.001062570,IBM,257.03,2,259.77,1
2025.05.23D08:00:00.009487606,IBM,257.03,2,259.49,1
2025.05.23D08:00:00.017576775,IBM,257.03,2,259.41,1
"""


@log_execution_time
def retrieve_bid_ask_spread_df(csv_file_path_1, csv_file_path_2, market_open, market_close):
    # Upload CSV files into kdb+ tables
    kx.q(f'trades: ("PSFJ";enlist ",") 0: `$":{csv_file_path_1}"')
    kx.q(f'quotes: ("PSFJFJ";enlist ",") 0: `$":{csv_file_path_2}"')

    # Key the quotes table
    kx.q('quotes: `timestamp`sym xkey quotes')

    # As-Of Join between trades and quotes tables
    kx.q('taq_table: aj[`sym`timestamp;trades;quotes]')

    # Filter TAQ data considering only market hours
    kx.q(f'filtered_taq_table: select from taq_table where timestamp within({market_open};{market_close})')

    # Calculate mid_price
    kx.q('filtered_taq_table: update mid_price: (bid_price + ask_price) % 2 from filtered_taq_table')

    # Calculate Effective bid_ask_spread (Percentage Form)
    filtered_taq_table = kx.q(
        'update bid_ask_spread: 2 * (abs(price - mid_price) % mid_price) * 100 from filtered_taq_table')

    # Convert to pandas DataFrame
    return filtered_taq_table.pd()
