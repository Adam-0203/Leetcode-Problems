class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [root]
        counter = 1
        while stack:
            add = 0
            numberNodes = 0
            for _ in range(counter):
                curr = stack.pop(0)
                if curr:
                    if not add:
                        add = 1
                        res += 1
                    stack.append(curr.left)
                    stack.append(curr.right)
                    numberNodes += 2
            counter = numberNodes
        return res
