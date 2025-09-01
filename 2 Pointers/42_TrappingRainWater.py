class Solution(object):
    def trap(self, height):
        L = len(height)
        res = 0

        left = 0
        right = L-1
        maxL = height[0]
        maxR = height[L-1]

        while left<right:
            if maxL < maxR:
                val = min(maxL,maxR)-height[left+1]
                if val>0:
                    res += val
                if height[left+1]>maxL:
                    maxL = height[left+1]
                left += 1
            else:
                val = min(maxL,maxR)-height[right-1]
                if val>0:
                    res += val
                if height[right-1]>maxR:
                    maxR = height[right-1]
                right -= 1

        return res                


        
