class Solution(object):
    def productExceptSelf(self, nums):
        res=[]

        L = len(nums)
        left = [0]*L ; product_left=1
        right = [0]*L ; product_right=1
        left[0]=1
        right[L-1]=1

        for i in range(L-1):
            product_left *= nums[i]
            product_right *= nums[-i-1]
        
            left[i+1] = product_left
            right[-i-2] = product_right


        
        return [left[i]*right[i] for i in range(L)]
        
        
