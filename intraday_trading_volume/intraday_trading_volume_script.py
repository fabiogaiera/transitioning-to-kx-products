import sys

from intraday_trading_volume.python.trades_dataframe_creator import create_dataframe
from intraday_trading_volume.volumes_histogram_creator import create_histogram

"""
Usage in Linux / Mac:
python -m intraday_trading_volume.intraday_trading_volume_script /path/to/file/trades.csv

Usage in Windows: 
python -m intraday_trading_volume.intraday_trading_volume_script C:/path/to/file/trades.csv
"""

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Incorrect parameters")
        sys.exit(1)
    trades_data_frame = create_dataframe(sys.argv[1])
    create_histogram(trades_data_frame)
