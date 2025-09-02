class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = len(cost)
        cache = {L-2:cost[-2], L-1:cost[-1]}

        def f(val):
            if val in cache:
                return cache[val]
            
            a = f(val+1)
            b = f(val+2)

            cache[val] = cost[val] + min(a, b)

            return cache[val]

        return min(f(0),f(1))
