import sys

from python.trades_dataframe_creator import create_dataframe
from python.volumes_histogram_creator import create_histogram
# from q.trades_dataframe_creator import create_dataframe
# from q.volumes_histogram_creator import create_histogram

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage in Linux: python script.py /path/to/file/trades.csv")
        print("Usage in Windows: python script.py C:/path/to/file/trades.csv")
        sys.exit(1)
    trades_data_frame = create_dataframe(sys.argv[1])
    create_histogram(trades_data_frame)
