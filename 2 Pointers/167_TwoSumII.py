class Solution(object):
    def twoSum(self, numbers, target):
        L = len(numbers)
        left = 0
        right = L-1

        while left<right:
            val = numbers[left]+numbers[right]

            if val == target:
                return [left+1,right+1]
            
            elif val>target:
                right -=1
            elif val<target:
                left +=1
