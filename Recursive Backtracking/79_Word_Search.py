class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        
        def voisins(position,visited):
            i,j = position[0],position[1]
            vois = set()
            if 0<=i-1 and (i-1,j) not in visited:
                vois.add((i-1,j))
            if (i+1)<=m-1 and (i+1,j) not in visited:
                vois.add((i+1,j))
            if (j-1)>=0 and (i,j-1) not in visited:
                vois.add((i,j-1))
            if (j+1)<=n-1 and (i,j+1) not in visited:
                vois.add((i,j+1))
            return vois

        res = False
        
        def exister(curr,index=0):
            if word[index] != board[curr[0]][curr[1]]:
                return

            if index+1==len(word):
                nonlocal res
                res = True
                return
            
            for position in voisins(curr,visited):
                visited.add(curr)
                exister(position,index+1)
                visited.remove(curr)

        for i in range(m):
            for j in range(n):
                visited = set()
                exister((i,j))
                if res:
                    return True
                
        
        return False
