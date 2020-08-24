import csv

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

    for row in rows:
        try:
            name, shares, cost = row
            print(f"name: {name}, shares: {shares}, cost: {cost}")
            total_cost += (float(cost) * float(shares))
        except ValueError:
            print("Missing field!") 


    f.close()
    return total_cost


# cost = portfolio_cost('Data/portfolio.csv')
# print(f"Total cost to purchase all of the shares: {cost}")

# cost = portfolio_cost('Data/missing.csv')
# print(f"Total cost to purchase all of the shares: {cost}")


cost = portfolio_cost_csv_library('Data/portfolio.csv')
print(f"Total cost to purchase all of the shares: {cost}")

cost = portfolio_cost_csv_library('Data/missing.csv')
print(f"Total cost to purchase all of the shares: {cost}")

