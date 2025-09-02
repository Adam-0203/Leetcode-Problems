class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        memo = {(L-1,1):nums[L-1],(L-1,0):0}

        def voler(index=-1,prendi=0):
            if (index,prendi) in memo:
                return memo[(index,prendi)]

            if prendi == 0:
                a = voler(index+1,0)
                b = voler(index+1,1)
                memo[(index,prendi)] = max(a,b)
                return memo[(index,prendi)]

            else:
                memo[(index,prendi)] = nums[index] + voler(index+1,0)
                return memo[(index,prendi)]
        
        return voler()


            
