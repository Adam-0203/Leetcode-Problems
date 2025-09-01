prices = [2,1000000,1,5,3,6,4]

def profit(lista):
    return max(lista)-lista[0]


def max_profit(lista):
    if len(lista) == 2: 
        if lista[1]-lista[0]<0:
            return 0
        return lista[1]-lista[0]
    elif len(lista)<=1: return 0


    return max(max_profit(lista[:lista.index(min(lista))]),
               profit(lista[lista.index(min(lista)):]))

print(max_profit(prices))
