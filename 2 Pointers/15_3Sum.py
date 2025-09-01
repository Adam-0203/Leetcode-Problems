class Solution(object):
    def threeSum(self,nums):
        L = len(nums)
        nums.sort()
        res = []
        deja = 0

        for i in range(L):
            if i>0 and nums[i-1]==nums[i]:
                continue
                
            if nums[i]>0:
                break

            left = i+1
            right = L-1

            while left<right:
                val = nums[left]+nums[right]

                if val>-nums[i]:
                    right -= 1
                
                elif val<-nums[i]:
                    left += 1
                
                elif val == -nums[i]:
                    if not deja:
                        res.append([nums[i],nums[left],nums[right]])
                        deja = 1
                    elif [nums[i],nums[left],nums[right]] != res[-1]:
                        res.append([nums[i],nums[left],nums[right]])
                    left+=1
            
        
        return res
