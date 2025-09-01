class Solution(object):
    import operator
    def evalRPN(self, tokens):
        stack = []
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        for token in tokens:
            if token in operations:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(operations[token](b,a)))
            else:
                stack.append(int(token))
        
        return stack[0]

        
