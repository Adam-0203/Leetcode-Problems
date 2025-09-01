class Solution(object):
    def longestConsecutive(self, nums):
        if not nums: return 0

        nums = set(nums)
        max_sequence = 1

        for x in nums: 
            if x-1 not in nums:
                sequence = 1
                val = x
                while val+1 in nums:
                    sequence += 1
                    val +=1
                if sequence>max_sequence :
                    max_sequence = sequence
        
        return max_sequence
