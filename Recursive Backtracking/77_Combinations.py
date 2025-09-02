class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []
        number = 0

        def combiner(index=1):
            nonlocal number
            if number == k:
                res.append(curr[:])
                return
            if (k-number) > (n+1-index):
                return
            
            
            combiner(index+1)
            curr.append(index)
            number += 1
            combiner(index+1)
            curr.pop()
            number -= 1

        combiner()
        return res
