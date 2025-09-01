class Solution(object):
    def spiralOrder(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        number_of_elements = n*m

        if m==1:
            return [matrix[i][0] for i in range(n)]

        elif n==1:
            return matrix[0]

        counter = 0
        res = []
        min_i = 0
        max_i = n-1
        min_j = 0
        max_j = m-1
        i=0
        j=0

        while counter != number_of_elements:
            if min_i==max_i and n!=m and j==min_j:
                for w in range(j,max_j+1):
                    res.append(matrix[i][w])
                    counter +=1
            elif min_i==max_i and n!=m and j==max_j:
                for w in range(j-1,min_j-1,-1):
                    res.append(matrix[i][w])
                    counter += 1
    
            elif min_j == max_j and n!=m and i==min_i:
                for w in range(i,max_i+1):
                    res.append(matrix[w][j])
                    counter += 1
            elif min_j == max_j and n!=m and i==max_i:
                for w in range(i-1,min_i-1,-1):
                    res.append(matrix[w][j])
                    counter += 1

            elif i==min_i and j==min_j:
                for w in range(j,max_j+1):
                    res.append(matrix[i][w])
                    counter +=1
                j = max_j


            elif i == min_i and j==max_j:
                for w in range(i+1,max_i+1):
                    res.append(matrix[w][j])
                    counter += 1
                i = max_i
                min_i+=1

            elif i== max_i and j == max_j:
                for w in range(j-1,min_j-1,-1):
                    res.append(matrix[i][w])
                    counter += 1
                j = min_j
                max_j-=1


            elif i == max_i and j==min_j:
                for w in range(i-1,min_i-1,-1):
                    res.append(matrix[w][j])
                    counter += 1
                max_i-=1
                min_j+=1
                i = min_i
                j = min_j

        return res
