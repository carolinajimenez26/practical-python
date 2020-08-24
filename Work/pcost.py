import csv
import sys

def portfolio_cost(filename):
    total_cost = 0

    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            try:
                name, shares, cost = line.split(",")
                print(f"name: {name}, shares: {shares}, cost: {cost}")
                total_cost += (float(cost) * float(shares))
            except ValueError:
                print("Missing field!") 

    return total_cost

def portfolio_cost_csv_library(filename):
    total_cost = 0
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)

    for lineno, row in enumerate(rows):
        try:
            record = dict(zip(headers, row))
            print(record)
            total_cost += (float(record["price"]) * float(record["shares"]))
        except ValueError:
            print(f"Row {lineno}: Couldn\'t convert: {row}")


    f.close()
    return total_cost


# cost = portfolio_cost('Data/portfolio.csv')
# print(f"Total cost to purchase all of the shares: {cost}")

# cost = portfolio_cost('Data/missing.csv')
# print(f"Total cost to purchase all of the shares: {cost}")


# cost = portfolio_cost_csv_library('Data/portfolio.csv')
# print(f"Total cost to purchase all of the shares: {cost}")

# cost = portfolio_cost_csv_library('Data/missing.csv')
# print(f"Total cost to purchase all of the shares: {cost}")


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost_csv_library(filename)
print(f"Total cost to purchase all of the shares: {cost}")