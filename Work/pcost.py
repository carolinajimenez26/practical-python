total_cost = 0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        name, shares, cost = line.split(",")
        print(f"name: {name}, shares: {shares}, cost: {cost}")
        total_cost += (float(cost) * float(shares))

print(f"Total cost to purchase all of the shares: {total_cost}")