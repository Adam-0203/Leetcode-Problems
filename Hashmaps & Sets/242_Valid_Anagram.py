class Solution(object):
    def isAnagram(self, s, t):
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        for x in t:
            if x not in dic or dic[x]==0:
                return False
            else:
                dic[x]-=1
        
        for i in s:
            if dic[i]!=0: return False
        
        return True
