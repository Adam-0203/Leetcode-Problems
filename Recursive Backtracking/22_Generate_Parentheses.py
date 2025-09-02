class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        def generate(ouvert=0,ferme=0):
            if (ouvert+ferme)==2*n:
                res.append(''.join(curr))
                return

            if ouvert<n:
                curr.append('(')
                generate(ouvert+1,ferme)
                curr.pop()

            if ouvert>ferme:
                curr.append(')')
                generate(ouvert,ferme+1)
                curr.pop()


        generate()
        return res
