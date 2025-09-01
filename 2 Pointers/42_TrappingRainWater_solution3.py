class Solution(object):
    # this solution is not effiscient enough to be Accepted in leetocde
    # But it introduces an interesting concept which the way to indentify a "hole" then fill it with water
    # We start from an edge then we use the function "find_end" to go to its end and calculate the water we need to fill it
    def trap(self, height):
        L = len(height)
        res = 0
        
        def find_end(i):

            first_end = height[i]

            
            if height[i]==0:
                return 0
            if i>=L-2:
                return 0
            
            mini = height[i+1]
            if mini >= first_end:
                return 0
            
            possibility = i+1
            for j in range(i+2,L):

                if height[j]>mini:
                    if height[j]>=first_end:
                        return j
                    elif j==L-1 and height[j]>height[possibility]:
                        return j
                    
                    elif height[j]<first_end and height[j]>height[possibility]:
                        possibility = j

            if possibility == i+1:
                return 0
            else:
                return possibility

                

            
        


        index = 0
        while index<L:
            end = find_end(index)
            if not end:
                index += 1
            else:
                val = min(height[index],height[end])
                for w in range(index+1,end):
                    res += (val-height[w])
                index = end

        return res


        
