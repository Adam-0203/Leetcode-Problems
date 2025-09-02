class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = len(cost)
        two = cost[L-1]
        one = cost[L-2]

        for i in range(2,len(cost)):
            temp = one
            one = min(one,two) + cost[L-1-i]
            two = temp

        return min(one,two)
