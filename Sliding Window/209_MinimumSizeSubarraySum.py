class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        somme = 0
        res = float('inf')

        for r in range(len(nums)):
            somme += nums[r]
            if somme >= target:
                while somme >= target:
                    somme -= nums[l]
                    l += 1

                res = min(res,r-l+2)

                
        if res == float("inf"): 
            return 0
        return res
