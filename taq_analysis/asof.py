import sys

import pykx as kx

from benckmark_util import log_execution_time


@log_execution_time
def retrieve_taq_dataframe(csv_file_path_1, csv_file_path_2):
    # Using PyKX interface
    trades = kx.q.read.csv(csv_file_path_1, 'PSFJ')
    quotes = kx.q.read.csv(csv_file_path_2, 'PSFJFJ')
    # Key the table
    quotes = kx.q.xkey(['sym', 'datetime'], quotes)
    # As-Of Join
    taq_table = kx.q.aj(kx.SymbolVector(['sym', 'datetime']), trades, quotes)
    return taq_table.pd()


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python asof.py </path/to/file/trades.csv> </path/to/file/quotes.csv>")
        sys.exit(1)

    taq_df = retrieve_taq_dataframe(sys.argv[1], sys.argv[2])
    print(taq_df)
