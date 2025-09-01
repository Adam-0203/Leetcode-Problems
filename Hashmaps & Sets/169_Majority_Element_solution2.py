class Solution(object):
    def majorityElement(self, nums):
        L=0
        dic = {}

        for x in nums:
            if x in dic:
                dic[x]+=1
                L+=1
            else:
                dic[x]=1
                L+=1
        
        val = L//2
        for x in dic:
            if dic[x]>val:
                return x
