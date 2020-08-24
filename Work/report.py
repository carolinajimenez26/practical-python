import csv
import sys

def read_portfolio(filename):
    portfolio = []
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        try:
            holding = dict(zip(headers, row))
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


def make_report(portfolio, prices):
    report = []

    for stock in portfolio:
        current_price = float(prices[stock['name']])
        change = current_price - float(stock['price'])
        summary = (stock['name'], int(stock['shares']), current_price, change)
        report.append(summary)
    return report



portfolio = read_portfolio('./Data/portfolio.csv')
prices    = read_prices('./Data/prices.csv')

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += int(s['shares']) * float(s['price'])

print('Total cost', total_cost)

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += int(s['shares']) * float(prices[s['name']])

print('Current value', total_value)
print('Gain', total_value - total_cost)

report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(f'{"":->10s} {"":->10s} {"":->10s} {"":->10s}')

for name, shares, price, change in report:
    s_price = '$' + f'{price:0.2f}'
    print(f'{name:>10s} {shares:>10d} {s_price:>10s} {change:>10.2f}')