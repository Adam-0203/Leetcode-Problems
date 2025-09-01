class Solution(object):
    def majorityElement(self, nums):
        ans = 0
        count =0

        for i in nums:
            if count == 0:
                ans = i
            if ans == i:
                count += 1
            elif ans!=i:
                count -= 1
        return ans
