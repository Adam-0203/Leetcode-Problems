prices = [7,1,5,3,6,4]
com = [[0]]
#the idea here is to test every possible outcome
# the "b" means "buy" and the "w" means "wait"

L = len(prices)
com = [[1,'b'],[0,'w']]
res = 0
for i in range(L-1):
    for x in range(len(com)):
        if com[0][-1]=='b':
            com.append([0]+com[0][1:]+['s'])
            com.append(com[0]+['w'])
            com.pop(0)
        elif com[0][-1]=='s':
            com.append([1]+com[0][1:]+['b'])
            com.append(com[0]+['w'])
            com.pop(0)
        elif com[0][-1]=='w' and com[0][0]==1:
            com.append(com[0]+['w'])
            com.append([0]+com[0][1:]+['s'])
            com.pop(0)
        else:
            com.append(com[0]+['w'])
            com.append([1]+com[0][1:]+['b'])
            com.pop(0)

for sce in com:
    if sce[0]==0:
        profit = 0
        for i in range(L):
            if sce[i+1]=='b':
                profit -= prices[i]
            elif sce[i+1]=='s':
                profit += prices[i]
        if profit>res:
            res = profit

print(res)
