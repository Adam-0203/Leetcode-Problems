class Solution(object):
    def maxProfit(self, prices):
        bp = prices[0]
        profit = 0
        for i in prices:
            if i<bp:
                bp = i
            elif i-bp>profit:
                profit = i-bp
        return profit
