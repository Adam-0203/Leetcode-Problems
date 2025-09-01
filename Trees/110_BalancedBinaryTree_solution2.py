class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depthTree(root):
            if not root:
                return 0
            
            left_depth = depthTree(root.left)
            right_depth = depthTree(root.right)

            return 1 + max(left_depth,right_depth)
        
        
        stack = [root]
        while stack:
            curr = stack.pop()
            if abs(depthTree(curr.left)-depthTree(curr.right))>1:
                return False
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return True
        
        
