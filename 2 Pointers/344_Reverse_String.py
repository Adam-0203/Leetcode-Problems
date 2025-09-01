class Solution(object):
    def reverseString(self, s):
        
        L = len(s)
        left = 0
        right = L-1

        while left<right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -=1
