class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fac(n):
            res = 1
            for i in range(2,n+1):
                res *= i
            return res

        def C(k,n):
            return (fac(n))/(fac(n-k)*fac(k))

        return int(C(n-1,n+m-2))
