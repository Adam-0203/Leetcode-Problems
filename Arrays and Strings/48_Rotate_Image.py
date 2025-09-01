class Solution(object):
    def rotate(self, matrix):
        
        n = len(matrix)-1

        def permuter(quatre):
            matrix[quatre[0][0]][quatre[0][1]],matrix[quatre[1][0]][quatre[1][1]],matrix[quatre[2][0]][quatre[2][1]],matrix[quatre[3][0]][quatre[3][1]] = matrix[quatre[3][0]][quatre[3][1]],matrix[quatre[0][0]][quatre[0][1]],matrix[quatre[1][0]][quatre[1][1]],matrix[quatre[2][0]][quatre[2][1]] 
        
        def quatrin(counter,i,val):
            longueur = val + counter*2
            min_i = counter
            min_j = counter
            max_i = longueur-counter
            max_j = longueur-counter
        
            brouk = i-counter
            return [[min_i,min_j+brouk],[min_i+brouk,max_j],[max_i,max_j-brouk],[max_i-brouk,min_j]]
        
        
        val = n
        counter = 0
        while val>=1:
            for i in range(counter,counter + val):
                permuter(quatrin(counter,i,val))
        
            counter +=1
            val-=2

        
