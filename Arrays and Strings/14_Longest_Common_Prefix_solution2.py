strs = ["flower","flow","flight"]

if not strs :  print("")
elif not strs[0]: print("")
mini = min([len(i) for i in strs])


index = 0
def check(index):
    global mini
    if index>=mini:
        return False
    temoin = strs[0][index]

    for mot in strs:
        if mot[index]!=temoin:
            return False
    return True
        
while check(index):
    index += 1
    
print(strs[0][:index])
