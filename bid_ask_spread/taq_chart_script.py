import sys

from bid_ask_spread.taq_chart.taq_chart_creator import create_taq_chart
from bid_ask_spread.taq_chart.taq_dataframe_creator import retrieve_taq_dataframe

"""
Usage in Linux / Mac:
python -m bid_ask_spread.taq_chart_script /path/to/file/trades.csv /path/to/file/quotes.csv"

Usage in Windows: 
python -m bid_ask_spread.taq_chart_script C:/path/to/file/trades.csv C:/path/to/file/quotes.csv"
"""

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Incorrect parameters")
        sys.exit(1)
    taq_data_frame = retrieve_taq_dataframe(sys.argv[1], sys.argv[2])
    create_taq_chart(taq_data_frame)
