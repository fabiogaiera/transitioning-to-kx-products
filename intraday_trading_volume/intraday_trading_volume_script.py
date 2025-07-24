import sys

from intraday_trading_volume.python.trades_dataframe_creator import create_dataframe
from intraday_trading_volume.volumes_histogram_creator import create_histogram

"""
Usage in Linux / Mac:
python -m intraday_trading_volume.intraday_trading_volume_script /path/to/file/trades.csv 2025-06-06

Usage in Windows: 
python -m intraday_trading_volume.intraday_trading_volume_script C:/path/to/file/trades.csv 2025-06-06
"""

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Incorrect parameters")
        sys.exit(1)

    # Path to the CSV file
    trades_data = sys.argv[1]

    # Date data type in q
    date = sys.argv[2].replace('-', '.')

    # Daylight Saving Time (DST) for Eastern Time (ET) in the U.S. as we're analyzing the IBM ticker.
    # Timestamp data type in q
    market_open = '2025.06.06D13:30:00.000000000'
    market_close = '2025.06.06D20:00:00.000000000'

    trades_data_frame = create_dataframe(trades_data, date, market_open, market_close)
    print(trades_data_frame)
    create_histogram(trades_data_frame)
