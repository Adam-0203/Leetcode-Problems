# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left ,right = 1,n

        while left <= right:
            mid = (right+left)//2

            if not isBadVersion(mid):
                left = mid+1

            elif isBadVersion(mid-1):
                right = mid-1
            
            else:
                return mid
