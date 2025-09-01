class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(root):
            if not root.left and not root.right:
                return [root.val,root.val,True]
            elif not root.left:
                right = dfs(root.right)
                bolien = right[0]>root.val and right[2]
                return [min(root.val,right[0]),max(root.val,right[1]),bolien]
            
            elif not root.right:
                left = dfs(root.left)    
                bolien = left[1]<root.val and left[2]
                return [min(root.val,left[0]),max(root.val,left[1]),bolien]
            
            else:
                left = dfs(root.left)
                right = dfs(root.right)
                bolien = left[1]<root.val<right[0] and right[2] and left[2]
                return [min(root.val,left[0],right[0]),max(root.val,left[1],right[1]),bolien]

        return dfs(root)[2]
