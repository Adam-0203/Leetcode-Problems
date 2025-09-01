class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, (n*m - 1)

        while left <= right:
            mid = (left+right)//2
            val = matrix[mid//n][mid%n]

            if val<target:
                left = mid+1

            elif val>target:
                right = mid-1

            else:
                return True
                
        return False        


