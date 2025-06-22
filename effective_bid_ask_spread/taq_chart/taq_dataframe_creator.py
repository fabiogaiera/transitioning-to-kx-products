import pykx as kx

from effective_bid_ask_spread.benchmark_util import log_execution_time


@log_execution_time
def retrieve_taq_dataframe(csv_file_path_1, csv_file_path_2):
    # Using PyKX interface (Pythonic code)
    trades = kx.q.read.csv(csv_file_path_1, 'PSFJ')
    quotes = kx.q.read.csv(csv_file_path_2, 'PSFJFJ')

    # Key the table
    quotes = kx.q.xkey(['sym', 'datetime'], quotes)
    # As-Of Join
    taq_table = kx.q.aj(kx.SymbolVector(['sym', 'datetime']), trades, quotes)
    # Convert to pandas DataFrame
    return taq_table.pd()
