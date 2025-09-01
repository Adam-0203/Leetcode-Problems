class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return 0
        
        def dfs(root):
            if not root:
                return 0
            nonlocal res
            lDepth = dfs(root.left)
            rDepth = dfs(root.right)

            res = max(res,1+lDepth+rDepth)
            return 1+max(lDepth,rDepth)
        dfs(root)

        return res-1
