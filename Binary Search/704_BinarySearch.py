class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L = len(nums)
        start = 0
        end = L-1

        while start<end:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                start = mid+1
            else:
                end = mid-1


        if nums[start]==target:
            return start
        else:
            return -1

        
