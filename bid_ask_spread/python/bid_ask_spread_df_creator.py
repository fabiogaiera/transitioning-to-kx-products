import pykx as kx

from bid_ask_spread.benchmark_util import log_execution_time

"""
CSV format example for trades
datetime,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""

"""
CSV format example for quotes
datetime,sym,bid_price,bid_size,ask_price,ask_size
2025.05.23D08:00:00.001037561,IBM,257.03,2,260.91,1
2025.05.23D08:00:00.001062570,IBM,257.03,2,259.77,1
2025.05.23D08:00:00.009487606,IBM,257.03,2,259.49,1
2025.05.23D08:00:00.017576775,IBM,257.03,2,259.41,1
"""


@log_execution_time
def retrieve_bid_ask_spread_df(csv_file_path_1, csv_file_path_2, market_open, market_close):
    # Upload CSV files into kdb+ tables
    trades = kx.q.read.csv(csv_file_path_1, 'PSFJ')
    quotes = kx.q.read.csv(csv_file_path_2, 'PSFJFJ')

    # Key the quotes table
    quotes = kx.q.xkey(['sym', 'datetime'], quotes)

    # As-Of Join between trades and quotes tables
    taq_table = kx.q.aj(kx.SymbolVector(['sym', 'datetime']), trades, quotes)

    # Filter TAQ data considering only market hours in UTC
    filtered_taq_table = taq_table.select(
        where=(
                (kx.Column('datetime') >= kx.q(market_open)) &
                (kx.Column('datetime') <= kx.q(market_close))
        )
    )

    # TODO: Calculate effective bid-ask spread here
    effective_bid_ask_spread_table = filtered_taq_table.select(...)

    # Convert to pandas DataFrame
    return effective_bid_ask_spread_table.pd()
