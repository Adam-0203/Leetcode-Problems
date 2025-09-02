class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        curr = []
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def combiner(index =0):
            if len(digits) == index:
                if len(digits):
                    res.append(''.join(curr))
                return
            
            letters = dic[digits[index]]
            for letter in letters:
                curr.append(letter)
                combiner(index+1)
                curr.pop()
        
        combiner()
        return res
            
