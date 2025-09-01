class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dic = {}
        for i in magazine:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        for x in ransomNote:
            if x not in dic or dic[x]==0:
                return False
            else:
                dic[x]-=1
        return True
        
