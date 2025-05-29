import sys

import pykx as kx

from benckmark_util import log_execution_time


@log_execution_time
def as_of(csv_file_path_1, csv_file_path_2):
    # Using PyKX interface
    trades = kx.q.read.csv(csv_file_path_1, 'PSFJ')
    quotes = kx.q.read.csv(csv_file_path_2, 'PSFJFJ')
    quotes = kx.q.xkey(['sym', 'datetime'], quotes)
    kx.q.aj(kx.SymbolVector(['sym', 'datetime']), trades, quotes)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python asof.py </path/to/file/trades.csv> </path/to/file/quotes.csv>")
        sys.exit(1)

    as_of(sys.argv[1], sys.argv[2])
