class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        dic = {}
        for x,y in edges:
            if x in dic:
                dic[x].append(y)
            else:
                dic[x] = [y]
            if y in dic:
                dic[y].append(x)
            else:
                dic[y]=[x]
                
        seen = {source}
        stack = [source]
        def dfs(root):
            while stack:
                val = stack.pop()
                if val == destination:
                    return True
                if val in dic:
                    for nei in dic[val]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
            return False
        
        return dfs(source)
            
