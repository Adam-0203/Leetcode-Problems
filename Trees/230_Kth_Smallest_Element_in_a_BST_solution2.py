class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res= 0
        current = 0

        def dfs(root):
            if not root:
                return
            

            dfs(root.left)

            nonlocal current
            current += 1
            if current == k:
                nonlocal res
                res = root.val

            dfs(root.right)

        dfs(root)
        return res
