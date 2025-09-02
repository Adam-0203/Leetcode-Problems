class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        dispo = nums[:]
        n = len(nums)

        def backtrack(index=0):
            if index==n:
                res.append(curr[:])
                return
            
            for i in range(len(dispo)):
                curr.append(dispo[i])
                element = dispo[i]
                dispo.pop(i)

                backtrack(index+1)

                dispo.insert(i,element)
                curr.pop()
                

        backtrack()
        return res
