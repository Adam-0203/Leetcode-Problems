class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, maxi = 0, 0, 0
        L = len(nums)
        counter, fautes = 0,0

        while right < L:
            if nums[right] == 1:
                counter += 1
                right += 1
            elif nums[right]==0 and fautes == k:
                
                maxi = max(maxi,counter)
                while nums[left]!=0:
                    counter -= 1
                    left += 1
                
                counter -= 1
                fautes -= 1
                left += 1
            else:
                counter += 1
                fautes += 1
                right += 1

        return max(counter,maxi)
        
