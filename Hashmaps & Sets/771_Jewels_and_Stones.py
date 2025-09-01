class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        dic = {x:0 for x in jewels}
        for x in stones:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=0
        
        counter = 0
        for x in jewels:
            counter += dic[x]
        return counter
