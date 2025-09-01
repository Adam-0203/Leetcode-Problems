class Solution(object):
    # this is a simpler way to understand better the first method
    # though it has a greater space complexity
    def trap(self, height):
        L = len(height)
        res = 0

        max_l = 0
        max_r = 0
        maxs_l = [0]*L
        maxs_r = [0]*L

        for i in range(1,L):
            if height[i-1]>max_l:
                max_l = height[i-1]
            maxs_l[i] = max_l 

            if height[-i]>max_r:
                max_r = height[-i]
            maxs_r[-i-1] = max_r

        for i in range(1,L-1):
            val = min(maxs_l[i],maxs_r[i]) - height[i]
            if val>0:
                res += val

        return res


        
