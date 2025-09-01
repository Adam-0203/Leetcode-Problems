class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        stack = [[root,1]]

        while stack:
            node,depth = stack.pop()
            if depth>res:
                res = depth

            if node.right:
                stack.append([node.right,depth+1])
            if node.left:
                stack.append([node.left,depth+1])

        return res
