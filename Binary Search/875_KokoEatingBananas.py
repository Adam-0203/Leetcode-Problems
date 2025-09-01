class Solution:
    from math import ceil
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #trouvons un left et right adapté
        somme = 0
        maxi = 0
        L = len(piles)
        rapport = h/L

        for x in piles:
            somme += x
            if x>maxi:
                maxi = x

        left = ceil(somme/h)

        if rapport>2:
            right = ceil(maxi/rapport)
        else:
            right = maxi
        
        #une fonction pour vérifier si une valeur fonctionne
        def isEnough(val):
            counter = 0
            for x in piles:
                counter += ceil(x/val)

            if counter > h or counter<0:
                return False
        
            return True


        #the binary search
        res = 0
        while left <= right:
            mid = (left+right)//2

            if isEnough(mid):
                res = mid
                right = mid-1
                
            else:
                left = mid+1
            
        return res
