class Solution(object):
    def isSubsequence(self, s, t):

        if not s: return True

        found = 0
        counter = 0
        curr = s[counter]
        for i in t:
                if counter == len(s)-1 and curr ==i:
                    found = 1
                    break
                elif curr==i:
                    counter+=1
                    curr = s[counter]
        
        if found: return True
        return False
