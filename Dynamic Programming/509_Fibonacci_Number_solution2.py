class Solution:
    def fib(self, n: int) -> int:
        cache = {0:0, 1:1}
        def fibo(val):
            if val in cache:
                return cache[val]

            a = fibo(val-1)
            b = fibo(val-2)

            cache[val] = a+b
            return cache[val]
            
        return fibo(n)
        
