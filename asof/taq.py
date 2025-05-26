import sys
import time

import pykx as kx


def as_of(csv_file_path_1, csv_file_path_2):
    trades = kx.q.read.csv(csv_file_path_1, 'PSFJ')
    quotes = kx.q.read.csv(csv_file_path_2, 'PSFJFJ')
    print(trades)
    print(quotes)


if __name__ == "__main__":

    start_time = time.time()

    if len(sys.argv) != 3:
        print("Usage: python taq.py </path/to/file/trades.csv> </path/to/file/quotes.csv>")
        sys.exit(1)
    as_of(sys.argv[1], sys.argv[2])

    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time:.2f} seconds")
