import sys

from intraday_trading_volume.python.trades_dataframe_creator import create_dataframe
from intraday_trading_volume.python.volumes_histogram_creator import create_histogram

# from intraday_trading_volume.q.trades_dataframe_creator import create_dataframe
# from intraday_trading_volume.q.volumes_histogram_creator import create_histogram

"""
Usage in Linux / Mac:
python -m intraday_trading_volume.script /path/to/file/trades.csv

Usage in Windows: 
python -m intraday_trading_volume.script C:/path/to/file/trades.csv
"""

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Incorrect parameters")
        sys.exit(1)
    trades_data_frame = create_dataframe(sys.argv[1])
    create_histogram(trades_data_frame)
