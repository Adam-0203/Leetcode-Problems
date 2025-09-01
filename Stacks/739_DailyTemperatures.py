class Solution(object):
    def dailyTemperatures(self, temperatures):
        L = len(temperatures)
        res = [0]*L
        stack = []

        for i in range(L):
            val = temperatures[i]
            while stack and stack[-1][0]<val:
                temp = stack.pop()
                res[temp[1]] = (i-temp[1])

            stack.append([val,i])

        return res
