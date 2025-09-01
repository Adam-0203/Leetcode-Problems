class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seto = set()

        for r in range(len(s)):
            while s[r] in seto:
                seto.remove(s[l])
                l += 1
            
            seto.add(s[r])
            res = max(res, r-l+1)
        return res
