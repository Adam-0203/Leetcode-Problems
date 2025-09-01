class Solution(object):
    def maxNumberOfBalloons(self, text):
        dic = {x:0 for x in 'balloon'}

        for x in text:
            if x in dic:
                dic[x]+=1
        
        dic['l'] = dic['l']//2 
        dic['o'] = dic['o']//2 
        
        return min([x for x in dic.values()])
