res = 0
index = len(prices)
L = len(prices)


while index>1:
    min_index=0
    for i in range(index):
        if prices[i]<prices[min_index]:
            min_index = i
    
    if index == len(prices) : 
        max_prices = 0
        for i in range(min_index,L):
            if prices[i]>max_prices:
                max_prices = prices[i]

        profit = max_prices-prices[min_index]
    else:
        max_prices = 0
        for i in range(min_index,index):
            if prices[i]>max_prices:
                max_prices = prices[i]

        profit = max_prices-prices[min_index]

    if profit>res:
        res = profit

    index = min_index

print(res)
