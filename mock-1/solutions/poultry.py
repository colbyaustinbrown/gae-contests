n = int(input())

prices = dict()

for i in range(0, n):
    line = input().split(" ")
    name = line[:-1]
    fullname = ""
    for n in name:
        fullname = fullname + " " + n
    price = float(line[-1:][0][1:])

    if not (fullname in prices):
        prices[fullname] = 0
    prices[fullname] = prices[fullname] + price

keys = list(prices.keys())
keys.sort()
for k in keys:
    print("{:s} ${:.2f}".format(k, prices[k]))

