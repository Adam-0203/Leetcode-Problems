class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        res = 0
        graph = {}
        start = set()
        fresh = set()

        def voisins(position):
            vois = []
            i,j = position[0],position[1]
            if i+1 in range(m) and grid[i+1][j]:
                vois.append((i+1,j))
            if i-1 in range(m) and grid[i-1][j]:
                vois.append((i-1,j))
            if j+1 in range(n) and grid[i][j+1]:
                vois.append((i,j+1))
            if j-1 in range(n) and grid[i][j-1]:
                vois.append((i,j-1))
            return vois

        def dfs(node):
            i,j = node[0],node[1]
            start.remove((i,j))
            if grid[i][j] == 2:
                nonlocal rotten
                rotten = True
            
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    graph[(i,j)] = voisins((i,j))
                    start.add((i,j))
                if grid[i][j] == 1:
                    fresh.add((i,j))

        if not fresh:
            return res

        while start:
            element = next(iter(start))
            rotten = False

            seen = {element}
            dfs(element)

            if not rotten:
                return -1
        
        
        while fresh:
            willRott = []
            for orange in graph:
                x,y = orange[0],orange[1]
                if grid[x][y] == 1 and any([grid[i][j]==2 for i,j in graph[orange]]):
                    willRott.append(orange)
                    fresh.remove(orange)
                    
            
            for i,j in willRott:
                grid[i][j] = 2
            res += 1

        return res


