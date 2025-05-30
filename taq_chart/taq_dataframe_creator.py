import pykx as kx

from benckmark_util import log_execution_time

"""
CSV format example
datetime,sym,price,size
2025.05.05D08:00:00.009039359,IBM,244.56,10
2025.05.05D08:00:00.156501572,IBM,243,8
2025.05.05D08:00:00.156579644,IBM,244.03,6
"""


@log_execution_time
def retrieve_taq_dataframe_q(csv_file_path_1, csv_file_path_2):
    # Using q expressions
    kx.q(f'trades: ("PSFJ";enlist ",") 0: `$":{csv_file_path_1}"')
    kx.q(f'quotes: ("PSFJFJ";enlist ",") 0: `$":{csv_file_path_2}"')
    # Key the table
    kx.q('quotes: `datetime`sym xkey quotes')
    # As-Of Join
    taq_table = kx.q('aj[`sym`datetime;trades;quotes]')
    # Convert to pandas DataFrame
    return taq_table.pd()


@log_execution_time
def retrieve_taq_dataframe_pykx(csv_file_path_1, csv_file_path_2):
    # Using PyKX interface (Pythonic code)
    trades = kx.q.read.csv(csv_file_path_1, 'PSFJ')
    quotes = kx.q.read.csv(csv_file_path_2, 'PSFJFJ')
    # Key the table
    quotes = kx.q.xkey(['sym', 'datetime'], quotes)
    # As-Of Join
    taq_table = kx.q.aj(kx.SymbolVector(['sym', 'datetime']), trades, quotes)
    # Convert to pandas DataFrame
    return taq_table.pd()
