class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = deque([root.left,root.right])

        while stack:
            left = stack.popleft()
            right = stack.popleft()

            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        
        return True
            
