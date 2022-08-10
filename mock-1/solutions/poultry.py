n = int(input())

prices = dict()

for i in range(0, n):
    line = input().split(" ")
    name = line[:-1][0]
    price = float(line[-1:][0][1:])

    if not (name in prices):
        prices[name] = 0
    else:
        prices[name] = prices[name] + price

keys = list(prices.keys())
keys.sort()
for k in keys:
    print("{:s} ${:.2f}".format(k, prices[k]))

