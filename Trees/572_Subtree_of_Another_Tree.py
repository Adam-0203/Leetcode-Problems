class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p,q):
            stackP = deque([p])
            stackQ = deque([q])

            while stackP and stackQ:
                nodeP = stackP.popleft()
                nodeQ = stackQ.popleft()

                if nodeP:
                    stackP.append(nodeP.left)
                    stackP.append(nodeP.right)

                if nodeQ:
                    stackQ.append(nodeQ.left)
                    stackQ.append(nodeQ.right)

                if nodeP is None and nodeQ is None:
                    continue
                elif nodeP is None:
                    return False
                elif nodeQ is None:
                    return False
                elif nodeP.val != nodeQ.val:
                    return False

            if len(stackP) == len(stackQ):
                return True
            return False
        
        stack = [root]
        while stack:
            curr = stack.pop()
            if same(curr,subRoot):
                return True
            
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)
        
        return False

