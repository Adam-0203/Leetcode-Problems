class Solution(object):
    def sortedSquares(self, nums):
        L = len(nums)
        l_ptr = 0
        r_ptr = L-1

        nums = [i**2 for i in nums]
        res = []

        while l_ptr <= r_ptr:
            if nums[l_ptr]>= nums[r_ptr]:
                res.append(nums[l_ptr])
                l_ptr += 1
            else:
                res.append(nums[r_ptr])
                r_ptr -= 1
        
        return res[::-1]
