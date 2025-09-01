class Solution(object):
    def maxArea(self, height):
        maxi = 0
        L = len(height)
        largeur = L-1

        left = 0
        right = L-1

        while largeur>0:
            val = largeur*min(height[left],height[right])

            if val>maxi:
                maxi = val
            
            if height[left] > height[right]:
                right -= 1
                largeur -= 1
            elif height[left] < height[right]:
                left += 1
                largeur -= 1
            elif height[left+1]>= height[right-1]:
                left += 1
                largeur -= 1
            else:
                right -= 1
                largeur -= 1

                

        return maxi
