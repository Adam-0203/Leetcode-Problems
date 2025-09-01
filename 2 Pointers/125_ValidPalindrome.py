class Solution(object):
    def isPalindrome(self, s):
        L = len(s)
        left = 0
        right = L-1

        while left<right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue


            if s[left].lower()==s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
        
