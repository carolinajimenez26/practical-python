import csv

def parse_csv(filename, select = None, types = None, has_headers = False):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        if (has_headers): 
            headers = next(rows)
        
        records = []

        for row in rows:
            if not row:    # Skip rows with no data
                continue

            if (has_headers):
                record = {header: val for header_index, (header, val) in enumerate(zip(headers, row)) if header in select }
                if types:
                    record = { key: func(record[key]) for func, key in zip(types, record) }
            else:
                record = tuple(val for val in row)
                if types:
                    record = tuple(func(val) for func, val in zip(types, row))
            
            records.append(record)

    return records


# portfolio = parse_csv('Data/prices.csv', types=[str, float], has_headers=False)
portfolio = parse_csv('Data/portfolio.csv', select=['name', 'price'], types=[str, float], has_headers=True)
# portfolio = parse_csv('Data/portfolio.csv', select=['name', 'prices'], types=[str, float])
# portfolio = parse_csv('Data/portfolio.csv', select=['name', 'shares'], types=[str, int])
print(portfolio)
