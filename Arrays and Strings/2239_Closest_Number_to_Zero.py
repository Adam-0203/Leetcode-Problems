class Solution(object):
    def findClosestNumber(self, nums):
        res = nums[0]
        for i in range(1,len(nums)):
            if abs(nums[i])<abs(res):
                res = nums[i]

        if res<0 and abs(res) in nums:
                return abs(res)
        return res
