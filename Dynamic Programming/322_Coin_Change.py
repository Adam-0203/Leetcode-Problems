class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {amount:0}

        for money in range(amount-1,-1,-1):
            cost = float("inf")
            for coin in coins:
                if coin + money in dp:
                    cost = min(cost,1+dp[coin+money])
                
            if cost != float("inf"):
                dp[money] = cost
        
        if 0 in dp:
            return dp[0]
        return -1
