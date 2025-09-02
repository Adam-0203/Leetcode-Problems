class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        def voisins(point):
            i,j = point[0],point[1]
            neighbors = []
            if i+1<m and heights[i][j]>=heights[i+1][j]:
                neighbors.append((i+1,j))
            if i-1>=0 and heights[i][j]>=heights[i-1][j]:
                neighbors.append((i-1,j))
            if j+1<n and heights[i][j]>=heights[i][j+1]:
                neighbors.append((i,j+1))
            if j-1>=0 and heights[i][j]>=heights[i][j-1]:
                neighbors.append((i,j-1))

            return neighbors
        
        matrix = [[[False,False] for j in range(n)] for i in range(m)]
        for j in range(n):
            matrix[0][j][0] = True
            matrix[m-1][j][1] = True
        for i in range(m):
            matrix[i][0][0] = True
            matrix[i][n-1][1] = True
        
        def dfs(point):
            i,j = point[0],point[1]
            if matrix[i][j] == [True,True]:
                if (i,j) not in res:
                    res.add((i,j))
                return [True,True]
            
            val = matrix[i][j]

            for nei in voisins((i,j)):
                if nei not in seen:
                    seen.add(nei)
                    poss = dfs(nei)
                    val = [val[0] or poss[0],val[1] or poss[1]]
                    if val == [True,True]:
                        if (i,j) not in res:
                            res.add((i,j))
                        return [True,True]

            return val


        res = set()
        for i in range(m):
            for j in range(n):
                if (i,j) not in res:
                    seen = {(i,j)}
                    dfs((i,j))
                        
        return [[i,j] for (i,j) in res]
