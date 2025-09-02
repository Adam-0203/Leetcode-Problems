class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n , m = len(text1), len(text2)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][-1] = 0
        for j in range(m):
            dp[-1][j] = 0

        def best(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            if text1[i] == text2[j]:
                dp[i][j] = 1 + best(i+1,j+1)
                return dp[i][j]

            dp[i][j] = max(best(i+1,j),best(i,j+1))
            return dp[i][j]

        return best(0,0)
