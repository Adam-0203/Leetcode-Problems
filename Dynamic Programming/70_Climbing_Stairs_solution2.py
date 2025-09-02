class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1:1, 2:2}

        def possible(val):
            if val in cache:
                return cache[val]
            
            a = possible(val-1)
            b = possible(val-2)

            cache[val] = a+b
            return a+b

        return possible(n)
