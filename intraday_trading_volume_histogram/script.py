import sys

from histogram_creator import create_histogram
from volume_dataframe_creator import create_dataframe

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python script.py </path/to/file/trades.csv>")
        sys.exit(1)
    data_frame = create_dataframe(sys.argv[1])
    create_histogram(data_frame)
