class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        len1, len2 = len(s1), len(s2)
        matches = 0
        if len2<len1:
            return False
        
        toBeChecked = set()
        dic = {}
        dic1 = {}

        for x in s1:
            dic1[x] = 1 + dic1.get(x,0)

        for i in range(len1):
            dic[s2[i]] = 1 + dic.get(s2[i],0)
            if s2[i] in dic1: 
                if dic[s2[i]]<=dic1[s2[i]]:
                    matches += 1
                else:
                    toBeChecked.add(i)

        l = 0
        for r in range(len1,len2):
            if matches == len1:
                return True
            
            left = s2[l]
            change = 0
            if left in dic1:
                if l not in toBeChecked:
                    matches -= 1
                    change = 1
                else:
                    toBeChecked.remove(l)
                dic[left] -= 1


            if change:
                for index in toBeChecked:
                    if s2[index]==left:
                        matches += 1
                        toBeChecked.remove(index)  
                        break      
            
            l += 1
            dic[s2[r]] = 1 + dic.get(s2[r],0)
            if s2[r] in dic1: 
                if dic[s2[r]]<=dic1[s2[r]]:
                    matches += 1
                else:
                    toBeChecked.add(r)

        if matches == len1:
            return True
        return False



        




        
        
            
