class Solution(object):
    def isValid(self, s):
        stack = []
        dic = {'(':')', '{':'}', '[':']'}

        for char in list(s):
            if not stack:
                stack.append(char)

            elif char not in dic:
                if stack[-1] not in dic:
                    return False
                    
                elif char != dic[stack[-1]]:
                    return False
                stack.pop()
        
            else:
                stack.append(char)
        
        if stack: 
            return False
        return True
