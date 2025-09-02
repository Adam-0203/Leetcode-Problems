class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (1,2):
            return n

        prev,curr = 1,2

        for _ in range(n-2):
            temp = curr
            curr = prev+curr
            prev= temp
        
        return curr
