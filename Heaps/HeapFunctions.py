# lista = [673, 720, 163, 319, 216, 947, 848, 439, 913, 566, 823, 561, 898, 254, 545]

def afficher(lista):
    fin = 1
    debut = 0
    L = len(lista)

    while debut<L:
        for i in range(debut,min(L,fin)):
            print(lista[i],end = ' ')
        print()
        debut = fin
        fin = fin*2+1
    print()

# lista = [10,7,8,6,3,4,7,1,2]
lista = [2,1,7,6,4,3,5,10,8]

def switch(lista,a,b):
    lista[a],lista[b] = lista[b],lista[a]

# Here we fix the node if it becomes smaller than its children
# Otherwise, we have to go backwards, i.e., switch with the parent,
# then the parent's parent, and so on until reaching the root.
# Note that by using THIS repair algorithm, traversing
# the tree from start to end for heapify will be correct.

def reparer(lista,p):
    index = p
    L = len(lista)

    while 2*index+1<L:
        if 2*index+2<L:
            if lista[2*index+1]>lista[2*index+2] and lista[2*index+1]>lista[index]:
                switch(lista,index,2*index+1)
                index = 2*index+1
            elif lista[2*index+2]>lista[2*index+1] and lista[2*index+2]>lista[index]:
                switch(lista,index,2*index+2)
                index = 2*index+2
            else:
                break
        elif lista[2*index+1]>lista[index]:
            switch(lista,2*index+1,index)
            index = 2*index+1
        else:
            break

def heapify(lista):
    for i in range(len(lista)//2,-1,-1):
        reparer(lista,i)

def maximum(lista):
    lista[0],lista[-1] = lista[-1],lista[0]
    max = lista.pop()
    reparer(lista,0)
    return max

def insert(lista,value):
    lista.append(value)
    index = len(lista)-1
    while ((index-1)//2) >= 0:
        if lista[((index-1)//2)]<lista[index]:
            switch(lista,((index-1)//2),index)
            index = ((index-1)//2)
        else:
            break

heapify(lista)
afficher(lista)
