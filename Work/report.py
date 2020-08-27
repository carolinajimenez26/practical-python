import csv
import sys

def read_portfolio(filename):
    portfolio = []
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    types = [str, int, float]

    for row in rows:
        try:
            holding = { name: func(val) for name, func, val in zip(headers, types, row) }
            portfolio.append(holding)
            # print(f"holding: {holding}")
        except ValueError:
            pass

    f.close()
    return portfolio

def read_prices(filename):
    prices = {}
    f = open(filename)
    rows = csv.reader(f)
    types = [str,float]

    for row in rows:
        converted = [ func(val) for func, val in zip(types, row) ]
        # print(converted)
        try:
            prices[converted[0]] = converted[1]
            # print(f"prices[{row[0]}] = {prices[row[0]]}")
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


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{"":->10s} {"":->10s} {"":->10s} {"":->10s}')

    for name, shares, price, change in report:
        s_price = '$' + f'{price:0.2f}'
        print(f'{name:>10s} {shares:>10d} {s_price:>10s} {change:>10.2f}')


def portfolio_report(portfolio_file_name, prices_file_name):
    portfolio = read_portfolio(portfolio_file_name)
    prices    = read_prices( prices_file_name)

    # Calculate the total cost of the portfolio
    total_cost = sum([int(s['shares']) * float(s['price']) for s in portfolio])
    print('Total cost', total_cost)

    # Compute the current value of the portfolio
    total_value = sum([int(s['shares']) * float(prices[s['name']]) for s in portfolio])
    print('Current value', total_value)
    print('Gain', total_value - total_cost)

    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
