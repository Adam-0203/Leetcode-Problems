class Solution(object):
    def containsDuplicate(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                return True
            else:
                dic[i]=0
        return False
