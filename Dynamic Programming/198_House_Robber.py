class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 1:
            return nums[0]

        old = (1,nums[-1])
        if nums[-2]>nums[-1]:
            prev = (1,nums[-2])
        else: 
            prev = (0,nums[-1])

        for i in range(2,L):
            val = nums[L-i-1]

            if prev[0] == 1:
                steal = val+old[1]
            else:
                steal = max(prev[1]+val,old[1]+val)

            leave = max(prev[1],old[1])

            if steal>leave:
                temp = prev
                prev = (1,steal)
                old = temp
            else:
                temp = prev
                prev = (0,leave)
                old = temp
            
            
        return prev[1]
