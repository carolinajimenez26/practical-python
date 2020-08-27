import csv

def parse_csv(filename, select = None, types = None, has_headers = False, delimiter = ',', silence_errors = False):
    '''
    Parse a CSV file into a list of records
    '''
    if not has_headers and select:
        raise RuntimeError("select argument requires column headers")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers: 
            headers = next(rows)
            if not select:
                select = headers
        
        records = []

        for index_row, row in enumerate(rows, 1):
            if not row:    # Skip rows with no data
                continue

            try:
                if has_headers:
                    record = {header: val for header_index, (header, val) in enumerate(zip(headers, row)) if header in select }
                    if types:
                        record = { key: func(record[key]) for func, key in zip(types, record) }
                else:
                    record = tuple(val for val in row)
                    if types:
                        record = tuple(func(val) for func, val in zip(types, row))
            except ValueError as err:
                if not silence_errors:
                    print(f"Row {index_row}: Couldn't convert {row}")
                    print(f"Row {index_row}: Reason {err}")

            records.append(record)

    return records


# portfolio = parse_csv('Data/missing.csv', types=[str, int, float], has_headers=True, silence_errors=True)
# portfolio = parse_csv('Data/missing.csv', types=[str, int, float], has_headers=True)
# parse_csv('Data/prices.csv', select=['name','price'], has_headers=False) # Raises an Exception
# portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], has_headers=True, delimiter=' ')
# portfolio = parse_csv('Data/prices.csv', types=[str, float], has_headers=False)
# portfolio = parse_csv('Data/portfolio.csv', select=['name', 'price'], types=[str, float], has_headers=True)
# portfolio = parse_csv('Data/portfolio.csv', select=['name', 'prices'], types=[str, float])
# portfolio = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
# print(portfolio)
