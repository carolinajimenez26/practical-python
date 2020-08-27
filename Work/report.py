import csv
import sys
import fileparse

def make_report(portfolio, prices):
    report = []

    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
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
    portfolio = fileparse.parse_csv(portfolio_file_name, types=[str, int, float], has_headers=True)
    prices    = dict(fileparse.parse_csv(prices_file_name, types=[str, float]))

    # Calculate the total cost of the portfolio
    total_cost = sum([s['shares'] * s['price'] for s in portfolio])
    print('Total cost', total_cost)

    # Compute the current value of the portfolio
    total_value = sum([s['shares'] * prices[s['name']] for s in portfolio])
    print('Current value', total_value)
    print('Gain', total_value - total_cost)

    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
