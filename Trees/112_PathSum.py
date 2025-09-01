class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        res = False
        def dfs(root,valeur=0):
            if not root.left and not root.right:
                if root.val + valeur == targetSum:
                    nonlocal res
                    res = True
            
                else:
                    return 
            
            if root.left:
                dfs(root.left,valeur + root.val)
            if root.right:
                dfs(root.right, valeur + root.val)
        dfs(root)
        return res
