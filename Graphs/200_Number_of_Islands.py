class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])

        def dfs(root):
            lands.remove(root)
            for x in dic[root]:
                if x not in seen:
                    seen.add(x)
                    dfs(x)

        def neighbors(i,j):
            vois = []
            if 0<=i-1 and grid[i-1][j]=='1':
                vois.append((i-1,j))
            if (i+1)<=m-1 and grid[i+1][j]=='1':
                vois.append((i+1,j))
            if (j-1)>=0 and grid[i][j-1]=='1':
                vois.append((i,j-1))
            if (j+1)<=n-1 and grid[i][j+1]=='1':
                vois.append((i,j+1))
            return vois
        
        res = 0
        dic = {}
        lands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    lands.add((i,j))
                    dic[(i,j)] = neighbors(i,j)
        
        while lands:
            land = next(iter(lands))
            seen = {land}
            dfs(land)
            res += 1
        
        return res

