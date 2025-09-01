class Solution(object):
    def twoSum(self, nums, target):
        L = len(nums)
        dic = {}

        for i in range(L):
            if nums[i] in dic and 2*nums[i]==target:
                return [dic[nums[i]],i]
            
            else:
                dic[nums[i]] = i

        for x in dic:
            if (target-x) in dic and target != 2*x:
                return [dic[x],dic[target-x]]
        
