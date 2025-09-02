# my algorithm has a complexity of O(n*max(nums))
# it is based on the idea that from a given position
# we move to the position that can take us the farthest

def canJump(self, nums: list[int]) -> bool:
        n = len(nums) - 1

        def jump(index):
            bestSpot = 0
            arrive = index
            for i in range(index+1,min(index+nums[index]+1,n+1)):
                val = min(i+nums[i],n)
                if val >= arrive: # the "or equal" is very important here because it allows us 
                                  # to move forward if a position has the same potential instead of staying in place
                    bestSpot = i
                    arrive = val
            return bestSpot,arrive

        i= 0
        while i<n:
            i,arrive = jump(i)
            if i == 0:
                return False
            if arrive>=n:
                return True
        return True
