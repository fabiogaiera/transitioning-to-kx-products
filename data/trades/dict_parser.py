def adjust_datetime(expression):

    expression = expression.replace('Z', '').replace('-', '.').replace('T', 'D')
    if len(expression) < 29:
        expression = expression.ljust(29, '0')
    return expression


def fetch_csv_rows_from_dict(parsed_data_as_dict):

    symbol = parsed_data_as_dict['symbol']
    trades = parsed_data_as_dict['trades']
    lst = []
    for elem in trades:
        # Adjusting datetime for kdb+ type conversion on a later stage
        datetime = adjust_datetime(elem['t'])
        nested_list = [datetime, symbol, elem['p'], elem['s']]
        lst.append(nested_list)
    return lst
