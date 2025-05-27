import sys

import pykx as kx


def as_of_q(csv_file_path_1, csv_file_path_2):
    kx.q(f'trades: ("PSFJ";enlist ",") 0: `$":{csv_file_path_1}"')
    kx.q(f'quotes: ("SFJFJP";enlist ",") 0: `$":{csv_file_path_2}"')
    kx.q('show aj[`sym`datetime;trades;quotes]')


def as_of_python(csv_file_path_1, csv_file_path_2):
    trades = kx.q.read.csv(csv_file_path_1, 'PSFJ')
    quotes = kx.q.read.csv(csv_file_path_2, 'SFJFJP')
    print(kx.q.asof(trades, quotes))


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python taq.py </path/to/file/trades.csv> </path/to/file/quotes.csv>")
        sys.exit(1)
    # It works
    as_of_q(sys.argv[1], sys.argv[2])
    # It doesn't work
    as_of_python(sys.argv[1], sys.argv[2])
