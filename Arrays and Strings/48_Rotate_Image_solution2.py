class Solution(object):
    def rotate(self, matrix):
        
        n = len(matrix)
        m = len(matrix[0])
        number_of_elements = n*m



        if m==1:
            print([matrix[i][0] for i in range(n)])

        elif n==1:
            print(matrix[0])

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
                    res.append([i,w])
                    counter +=1
            elif min_i==max_i and n!=m and j==max_j:
                for w in range(j-1,min_j-1,-1):
                    res.append([i,w])
                    counter += 1

            elif min_j == max_j and n!=m and i==min_i:
                for w in range(i,max_i+1):
                    res.append([w,j])
                    counter += 1
            elif min_j == max_j and n!=m and i==max_i:
                for w in range(i-1,min_i-1,-1):
                    res.append([w,j])
                    counter += 1


            elif i==min_i and j==min_j:
                for w in range(j,max_j+1):
                    res.append([i,w])
                    counter +=1
                j = max_j


            elif i == min_i and j==max_j:
                for w in range(i+1,max_i+1):
                    res.append([w,j])
                    counter += 1
                i = max_i
                min_i+=1

            elif i== max_i and j == max_j:
                for w in range(j-1,min_j-1,-1):
                    res.append([i,w])
                    counter += 1
                j = min_j
                max_j-=1


            elif i == max_i and j==min_j:
                for w in range(i-1,min_i-1,-1):
                    res.append([w,j])
                    counter += 1
                max_i-=1
                min_j+=1
                i = min_i
                j = min_j



        def quatrin(a,b,val):
            for i in range(len(res)):
                if res[i]==[a,b]:
                    return [res[i],res[i+val],res[i+2*val],res[i+3*val]]
    
        def permuter(quatre):
            matrix[quatre[0][0]][quatre[0][1]],matrix[quatre[1][0]][quatre[1][1]],matrix[quatre[2][0]][quatre[2][1]],matrix[quatre[3][0]][quatre[3][1]] = matrix[quatre[3][0]][quatre[3][1]],matrix[quatre[0][0]][quatre[0][1]],matrix[quatre[1][0]][quatre[1][1]],matrix[quatre[2][0]][quatre[2][1]] 
    
    
        val = n-1
        counter = 0
        while val>=1:
            for i in range(counter,counter + val):
                permuter(quatrin(counter,i,val))
    
            counter +=1
            val-=2

        
