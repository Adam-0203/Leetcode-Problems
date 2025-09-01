prices = [7,1,5,3,6,4]
profit = 0
L = len(prices)
mini = float("inf")
maxi = 0
index = 0
trouve=0

while index<L:
    while index<L and prices[index]<mini:
        mini = prices[index]
        index += 1

    while index<L and prices[index]>maxi:
        maxi = prices[index]
        index += 1
        trouve = 1


    if trouve: profit += (maxi-mini)
    trouve = 0
    mini = float("inf")
    maxi = 0

print(profit)
