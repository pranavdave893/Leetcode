from collections import defaultdict
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        
        player_1_row = defaultdict(lambda:0)
        player_1_col = defaultdict(lambda:0)
        player_1_diag_count = 0
        player_1_anti_diag_count = 0

        player_2_row = defaultdict(lambda:0)
        player_2_col = defaultdict(lambda:0)
        player_2_diag_count = 0
        player_2_anti_diag_count = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        diag_points = set()
        for i in range(n):
            diag_points.add((i,i))
        
        anti_diag_points = set()
        for i in range(len(n)-1, -1, -1):
            
        if player == 1:
            player_1_row[row] += 1
            if player_1_row[row] == n:
                return 1
        
            

            