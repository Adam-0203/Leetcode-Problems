class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = len(s)
        res = 0
        max_occur = 0

        l=0
        occurences = {}
        for r in range(L):
            occurences[s[r]] = 1 + occurences.get(s[r],0)

            max_occur = max(max_occur,occurences[s[r]])

            if (r-l+1 - max_occur)>k: 
                occurences[s[l]] -= 1
                l += 1

            res = max(res,r-l+1) 
        return res
