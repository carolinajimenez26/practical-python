import csv
import sys

def read_portfolio(filename):
    portfolio = []
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        try:
            holding = {
                "name": row[0],
                "shares": int(row[1]),
                "price": float(row[2])
            }
            portfolio.append(holding)
            print(f"holding: {holding}")
        except ValueError:
            pass

    f.close()
    return portfolio

def read_prices(filename):
    prices = {}
    f = open(filename)
    rows = csv.reader(f)

    for row in rows:
        try:
            prices[row[0]] = float(row[1])
            print(f"prices[{row[0]}] = {prices[row[0]]}")
        except IndexError:
            pass

    f.close()
    return prices


portfolio = read_portfolio('./Data/portfolio.csv')
prices    = read_prices('./Data/prices.csv')

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']

print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print('Current value', total_value)
print('Gain', total_value - total_cost)
