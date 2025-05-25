def adjust_datetime(expression):
    expression = expression.replace('Z', '').replace('-', '.').replace('T', 'D')
    if len(expression) < 29:
        expression = expression.ljust(29, '0')
    return expression


def fetch_csv_rows_from_dict(parsed_data_as_dict):

    quotes = parsed_data_as_dict['quotes']
    lst = []

    for elem in quotes:
        pass

    return lst
