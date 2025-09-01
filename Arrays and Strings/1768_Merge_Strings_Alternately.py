class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = []
        len1 = len(word1); ptr1 = 0
        len2 = len(word2); ptr2 = 0

        while (ptr1 < len1) and (ptr2<len2):
            res.append(word1[ptr1])
            res.append(word2[ptr2])
            ptr1 += 1
            ptr2 += 1


        while ptr1<len1:
            res.append(word1[ptr1])
            ptr1 += 1
        
        while ptr2<len2:
            res.append(word2[ptr2])
            ptr2 += 1

        return "".join(res)
