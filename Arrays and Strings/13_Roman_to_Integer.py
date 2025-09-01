class Solution(object):
    def romanToInt(self, s):
        res = 0
        length = len(s)
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100,"D":500,"M":1000 }
        for i in range(length-1):
            if dic[s[i]] >= dic[s[i+1]]:
                res += dic[s[i]]
            
            else:
                res -= dic[s[i]]
        return res + dic[s[length-1]] 
