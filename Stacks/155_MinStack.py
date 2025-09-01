class MinStack(object):

    def __init__(self):
        self.data = []

    def push(self, val):
        if not self.data:
            self.data.append([val,val])
        elif val< self.data[-1][1]:
            self.data.append([val,val])
        else:
            self.data.append([val,self.data[-1][1]])
        

    def pop(self):
        self.data.pop()

        

    def top(self):
        return self.data[-1][0]
        

    def getMin(self):
        return self.data[-1][1]
