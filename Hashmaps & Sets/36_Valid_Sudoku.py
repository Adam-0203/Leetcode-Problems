class Solution(object):
    def isValidSudoku(self, board):

        for i in range(0,9): #le nombre de ligne
            s = set()
            for j in range(0,9):
                if board[i][j]==".": continue
                if board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])

        for j in range(0,9):
            s = set()
            for i in range(0,9):
                if board[i][j]==".": continue
                if board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
        
        def check(min_i,max_i,min_j,max_j):
            s = set()
            for i in range(min_i,max_i+1):
                for j in range(min_j,max_j+1):
                    if board[i][j]==".": continue
                    if board[i][j] in s:
                        return False
                    else:
                        s.add(board[i][j])
            return True


        lista = [[0,2,0,2],[0,2,3,5],[0,2,6,8],[3,5,0,2],[3,5,3,5],[3,5,6,8],[6,8,0,2],[6,8,3,5],[6,8,6,8]]
        for quatrin in lista:
            if not check(quatrin[0],quatrin[1],quatrin[2],quatrin[3]): return False


        return True
