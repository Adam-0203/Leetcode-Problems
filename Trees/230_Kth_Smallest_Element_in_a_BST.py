class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        zid = 1
        counter = 0
        stack = [root]
        while stack:
            if zid:
                current = stack[-1]
                while current.left:
                    stack.append(current.left)
                    current = current.left
                zid = 0
                continue
            
            else:
                current = stack.pop()
                counter += 1
                if counter == k:
                    return current.val
                
                if current.right:
                    stack.append(current.right)
                    if current.right.left:
                        zid = 1


            
