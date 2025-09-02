class Solution:
    def canJump(self, nums: List[int]) -> bool:
        but = len(nums) - 1

        while but != 0:
            trouver = False
            for i in range(but-1,-1,-1):
                if i+nums[i]>=but:
                    but = i
                    trouver = True
                    break

            if not trouver:
                return False
        
        return True
