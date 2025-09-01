
class Solution:
    def invertTree(self,root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
          
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
              curr.right , curr.left = curr.left , curr.right
              stack.append(curr.right)
              stack.append(curr.left) 

        return root
        
        
            
        

        
