class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        failed = set()
        won = set()
        def voisins(point):
            i,j = point[0],point[1]
            neighbors = []
            if i+1<m and (i+1,j) not in seen and heights[i][j]>=heights[i+1][j] and (i+1,j) not in failed:
                neighbors.append((i+1,j))
            if i-1>=0 and (i-1,j) not in seen and heights[i][j]>=heights[i-1][j] and (i-1,j) not in failed:
                neighbors.append((i-1,j))
            if j+1<n and (i,j+1) not in seen and heights[i][j]>=heights[i][j+1] and (i,j+1) not in failed:
                neighbors.append((i,j+1))
            if j-1>=0 and (i,j-1) not in seen and heights[i][j]>=heights[i][j-1] and (i,j-1) not in failed:
                neighbors.append((i,j-1))

            return neighbors
        
        def dfs(point):
            stack = [point]
            res = [0,0]
            while stack:
                i,j = stack.pop()
                if i==0 or j==0:
                    res[0]=1
                if i==m-1 or j==n-1:
                    res[1]=1
                if (res[0] and res[1]) or (i,j) in won:
                    won.add(point)
                    return True
                
                lista = voisins((i,j))
                for x in lista:
                    seen.add(x)
                    stack.append(x)

            if not res[0] and not res[1]:
                failed.add(point)
            return False

        res = []
        for i in range(m):
            for j in range(n):
                seen = {(i,j)}
                if dfs((i,j)):
                   res.append([i,j]) 
        
        return res
