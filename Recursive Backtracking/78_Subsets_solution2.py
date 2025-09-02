class Solution(object):
    def subsets(self, nums):
        res = []
        def comb(nums,index=0,curr=[]):
            if len(nums)==index:
                res.append(curr)
                return
            
            comb(nums,index+1,curr)
            comb(nums,index+1,curr+[nums[index]])
        
        comb(nums)
        return res
