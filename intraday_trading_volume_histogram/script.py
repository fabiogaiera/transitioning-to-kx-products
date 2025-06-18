import sys

from intraday_trading_volume_histogram.python.trades_dataframe_creator import create_dataframe
from intraday_trading_volume_histogram.python.volumes_histogram_creator import create_histogram

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script.py </path/to/file/trades.csv>")
        sys.exit(1)
    trades_data_frame = create_dataframe(sys.argv[1])
    create_histogram(trades_data_frame)
