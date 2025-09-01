class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        L = len(nums)
        res = 0

        for i in range(k):
            res += nums[i]

        val = res
        left = 1
        right = k

        while right<L:
            val -= nums[left-1]
            val += nums[right]
            if val>res:
                res = val

            left += 1
            right += 1
        
        return res/k
