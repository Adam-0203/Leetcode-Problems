class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        res = 1

        for i in range(len(nums)-1,-1,-1):
            sequence = 1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    sequence = max(sequence,1+dp[j])
            dp[i] = sequence
            res = max(dp[i],res)

        return res  
