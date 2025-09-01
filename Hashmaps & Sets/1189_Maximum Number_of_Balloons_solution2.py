class Solution(object):
    def maxNumberOfBalloons(self, text):
        dic = {x:0 for x in 'balloon'}

        for x in text:
            if x in dic:
                dic[x]+=1
        
        res = 0
        def word_possible():
            for x in 'balloon':
                if dic[x]==0:
                    return False
                else:
                    dic[x]-=1
            return True
        
        while word_possible():
            res +=1
        
        return res
        
