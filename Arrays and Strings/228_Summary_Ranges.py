class Solution(object):
    def summaryRanges(self, nums):

        res=[]
        if len(nums)==0: return res
        if len(nums)==1: return [str(nums[0])]

        def ajouter(num1,num2):
            if num1 == num2: res.append(str(num1))
            else: res.append(str(num1)+"->"+str(num2))

        debut = nums[0]
        L = len(nums)

        for i in range(L-1):
            if nums[i+1] != nums[i]+1:
                ajouter(debut,nums[i])
                debut = nums[i+1]

        if nums[-1] == nums[-2]+1:
            ajouter(debut,nums[-1])
        else:
            ajouter(nums[-1],nums[-1])
        return res
