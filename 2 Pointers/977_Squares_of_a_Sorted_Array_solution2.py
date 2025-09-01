class Solution(object):
    def sortedSquares(self, nums):
        res1 = [] ; len1 = 0
        res2 = [] ; len2 = 0
        res = []


        for i in nums:
            if i < 0:
                res1.append(i**2)
                len1 += 1
            else:
                res2.append(i**2)
                len2 += 1
        
        ptr_1 = len1-1
        ptr_2  = 0

        while ptr_1>=0 and ptr_2<=(len2-1):
            a = res1[ptr_1]
            b = res2[ptr_2]
            if a<=b:
                res.append(a)
                ptr_1 -= 1
            else:
                res.append(b)
                ptr_2 += 1

        while ptr_1>=0:
            res.append(res1[ptr_1])
            ptr_1 -=1

        while ptr_2<=(len2-1):
            res.append(res2[ptr_2])
            ptr_2 += 1

        return res


        
