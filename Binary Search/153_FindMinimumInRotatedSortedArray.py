class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = len(nums)
        left, right = 0, L-1

        def ismin(left,right,mid):
            if mid == 0 and L == 1:
                return True
            elif mid==0 and nums[mid]<nums[1] and nums[mid]<nums[L-1]:
                return True
            elif mid==L-1 and nums[mid]<nums[L-2] and nums[mid]<nums[0]:
                return True
            elif nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                return True
            return False

        while left<=right:
            mid = (left+right)//2
            val = nums[mid]

            if ismin(left,right,mid):
                return nums[mid]
            
            elif val>=nums[left] and val>=nums[right]:
                left = mid+1
            
            else:
                right = mid-1

        return nums[right]
