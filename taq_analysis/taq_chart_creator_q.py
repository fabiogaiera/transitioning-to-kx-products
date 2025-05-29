import sys

import pykx as kx

from benckmark_util import log_execution_time


@log_execution_time
def retrieve_taq_dataframe(csv_file_path_1, csv_file_path_2):
    # Using q expressions
    kx.q(f'trades: ("PSFJ";enlist ",") 0: `$":{csv_file_path_1}"')
    kx.q(f'quotes: ("PSFJFJ";enlist ",") 0: `$":{csv_file_path_2}"')
    kx.q('quotes: `datetime`sym xkey quotes')
    kx.q('aj[`sym`datetime;trades;quotes]')


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python taq_chart_creator_q.py </path/to/file/trades.csv> </path/to/file/quotes.csv>")
        sys.exit(1)

    retrieve_taq_dataframe(sys.argv[1], sys.argv[2])
