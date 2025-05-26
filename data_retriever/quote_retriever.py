import csv
import sys
from pathlib import Path

from alpaca_rest_client.api_client import get_response
from alpaca_rest_client.dict_parser import fetch_csv_rows_from_quotes_dict


def retrieve_quotes_data(symbol, date, destination_folder):

    file_name = "{}_{}_daily_quotes.csv".format(symbol, date)
    full_path = Path(destination_folder) / file_name
    str_full_path = str(full_path)
    base_url = f"https://data.alpaca.markets/v2/stocks/{symbol}/quotes"

    with open(str_full_path, 'w', newline='') as file:

        writer = csv.writer(file)
        first_row = ["datetime", "sym", "bid_price", "bid_size", "ask_price", "ask_size"]
        writer.writerow(first_row)

        next_page_token = None
        first_iteration = True

        while next_page_token or first_iteration:

            if first_iteration:

                parsed_data, next_page_token = get_response(base_url, date)
                rows = fetch_csv_rows_from_quotes_dict(parsed_data)
                writer.writerows(rows)
                next_page_token = parsed_data['next_page_token']
                first_iteration = False

            else:

                parsed_data, next_page_token = get_response(base_url, date, next_page_token)
                rows = fetch_csv_rows_from_quotes_dict(parsed_data)
                writer.writerows(rows)
                next_page_token = parsed_data['next_page_token']


"""

To use this script, you must setup both environment variables in your OS:
API-KEY
API-SECRET
See https://alpaca.markets to get an API key and its corresponding secret

"""

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python quote_retriever.py <symbol> <yyyy-MM-dd> </path/to/folder>")
        sys.exit(1)
    retrieve_quotes_data(sys.argv[1], sys.argv[2], sys.argv[3])
