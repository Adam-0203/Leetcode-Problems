class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        somme = 0

        def combiner(index=0):
            nonlocal somme
            if somme>target:
                return
            if somme==target:
                res.append(curr[:])
                return
            if index==len(candidates):
                return
            
            number = (target-somme)//candidates[index]

            for i in range(number+1):
                for _ in range(i):
                    curr.append(candidates[index])
                    somme += candidates[index]
                combiner(index+1)
                for _ in range(i):
                    curr.pop()
                    somme -= candidates[index]
        
        combiner()
        return res
