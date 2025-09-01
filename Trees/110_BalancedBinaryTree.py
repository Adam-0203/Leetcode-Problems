class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balancer(root):
            if not root:
                return [True,0]

            left = balancer(root.left)
            right = balancer(root.right)

            depth = max(left[1],right[1])

            if not (left[0] and right[0]):
                return [False,depth+1]

            elif abs(left[1]-right[1])>1:
                return [False,depth+1]

            else:
                return [True,depth+1]
        
        return balancer(root)[0]
        
        
