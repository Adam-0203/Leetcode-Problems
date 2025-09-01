class Solution(object):
    def calPoints(self, operations):

        def is_number(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        stack = []
        for op in operations:
            if is_number(op):
                stack.append(int(op))

            elif op == '+':
                stack.append(int(stack[-1]) + int(stack[-2]))

            elif op == 'D':
                stack.append(int(stack[-1])*2)

            else: 
                stack.pop()



        return sum(stack)
