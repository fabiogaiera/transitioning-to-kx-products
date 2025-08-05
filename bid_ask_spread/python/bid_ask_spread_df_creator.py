# bid_ask_spread_df_creator.py

import logging

import pykx as kx

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

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def retrieve_bid_ask_spread_df(csv_file_path_1, csv_file_path_2, market_open, market_close):
    # Upload CSV files into kdb+ tables
    logging.info("Started trades retrieval")
    trades = kx.q.read.csv(csv_file_path_1,
                           [kx.TimestampAtom, kx.SymbolAtom, kx.FloatAtom, kx.LongAtom])
    logging.info("Ended trades retrieval")

    logging.info("Started quotes retrieval")
    quotes = kx.q.read.csv(csv_file_path_2,
                           [kx.TimestampAtom, kx.SymbolAtom, kx.FloatAtom, kx.LongAtom, kx.FloatAtom, kx.LongAtom])
    logging.info("Ended quotes retrieval")

    # Key the quotes table
    logging.info("Started quotes keying")
    quotes = kx.q.xkey(['sym', 'timestamp'], quotes)
    logging.info("Ended quotes keying")

    # As-Of Join between trades and quotes tables
    logging.info("Started As-Of Join")
    taq_table = kx.q.aj(kx.SymbolVector(['sym', 'timestamp']), trades, quotes)
    logging.info("Ended As-Of Join")

    # Filter TAQ data considering only market hours
    logging.info("Started filtering by market hours")
    filtered_taq_table = taq_table.select(
        where=(
                (kx.Column('timestamp') >= kx.q(market_open)) &
                (kx.Column('timestamp') <= kx.q(market_close))
        )
    )
    logging.info("Ended filtering by market hours")

    # Calculate mid_price
    logging.info("Started adding mid_price")
    filtered_taq_table = filtered_taq_table.update(
        kx.Column('mid_price',
                  value=((kx.Column('bid_price') + kx.Column('ask_price')) / 2)))
    logging.info("Ended adding mid_price")

    # Calculate Effective bid_ask_spread (Percentage Form)
    logging.info("Started adding bid_ask_spread")
    filtered_taq_table = filtered_taq_table.update(
        kx.Column('bid_ask_spread',
                  value=((2 * abs(kx.Column('price') - kx.Column('mid_price'))) / kx.Column('mid_price')) * 100)
    )
    logging.info("Ended adding bid_ask_spread")

    # Convert to pandas DataFrame
    return filtered_taq_table.pd()
