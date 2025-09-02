from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        new = Node(1)
        correspond = {1:new}

        def dfs(root):
            for nei in root.neighbors:
                if nei.val not in correspond:
                    correspond[nei.val] = Node(nei.val)
                correspond[root.val].neighbors.append(correspond[nei.val])

            seen.add(root.val)
            for nei in root.neighbors:
                if nei.val not in seen:
                    dfs(nei)
        
        seen = set()
        dfs(node)
        return new
            
