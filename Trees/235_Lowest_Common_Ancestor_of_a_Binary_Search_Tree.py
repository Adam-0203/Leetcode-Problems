class Solution:
    def lowestCommonAncestor(self, root, p, q) -> 'TreeNode':
        
        if p.val<=root.val<= q.val or q.val<=root.val<= p.val:
            return root
        
        elif p.val<=root.val and q.val<= root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        else:
            return self.lowestCommonAncestor(root.right,p,q)
