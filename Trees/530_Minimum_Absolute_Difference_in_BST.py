class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        def dfs(root):
            nonlocal res
            if not root.right and not root.left:
                return [root.val,root.val]

            elif not root.right:
                left = dfs(root.left)
                res = min(res,root.val-left[1])
                return [left[0],root.val]

            elif not root.left:
                right = dfs(root.right)
                res = min(res,right[0]-root.val)
                return [root.val,right[1]]

            else:
                left = dfs(root.left)
                right = dfs(root.right)
                res = min(res,root.val-left[1],right[0]-root.val)
                return [left[0],right[1]]
        
        dfs(root)
        return res
