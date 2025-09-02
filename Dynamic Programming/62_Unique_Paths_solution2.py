class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def path(bas,droite):
            if not bas or not droite:
                return 1
            
            if (bas,droite) in memo:
                return memo[(bas,droite)]
            if (droite,bas) in memo:
                return memo[(droite,bas)]

            memo[(bas,droite)] = path(bas-1,droite)+path(bas,droite-1)
            return memo[(bas,droite)]

        return path(m-1,n-1)
