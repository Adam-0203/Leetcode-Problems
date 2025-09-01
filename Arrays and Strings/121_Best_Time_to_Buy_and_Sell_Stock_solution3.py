class Solution(object):
    def maxProfit(self, prices):
        res = 0
        index = len(prices)
        while index>1:
            min_index = prices.index(min(prices[:index]))
    
            if index == len(prices) : 
                profit = max(prices[min_index:])-prices[min_index]
            else:
                profit = max(prices[min_index:index])-prices[min_index]
    
            if profit>res:
                res = profit
        
    
            index = min_index
    
        return res
