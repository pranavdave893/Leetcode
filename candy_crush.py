class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        if board == [] or board == [[]]: return board 
        R, C = len(board), len(board[0])
        while True:
            crushcandy = False
            for i in xrange(R):
                for j in xrange(C - 2):
                    if abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]):
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
            for j in xrange(C):
                for i in xrange(R - 2):
                    if abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]):
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j]) 
            for i in xrange(R):
                for j in xrange(C):
                    if board[i][j] < 0:
                        board[i][j] = 0
                        crushcandy = True 
            for j in xrange(C):
                point = R - 1
                for i in xrange(R - 1, -1, -1):
                    if board[i][j] != 0:
                        board[point][j] = board[i][j]
                        point -= 1
                for b in xrange(point + 1):
                    board[b][j] = 0 
            if not crushcandy: return board 

abc = Solution()
abc.candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]])