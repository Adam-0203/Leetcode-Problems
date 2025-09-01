class Solution(object):
    def maxProfit(self, prices):
        def profit(lista):
            return max(lista)-lista[0]


        def max_profit(lista):
            if len(lista) == 2: return lista[1]-lista[0]
            elif len(lista)<=1: return 0
            return max(max_profit(lista[:lista.index(min(lista))]),profit(lista[lista.index(min(lista)):]))

        
        res = max_profit(prices)
        if res>0: return res
        return 0
