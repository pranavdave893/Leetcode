from collections import deque
import numpy as np

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # If we change from 1 to 0 its 'Z'
        # If we change from 0 to 1 its 'X'
        
        R = len(board)
        C = len(board[0])
        points = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
        neighbours = deque([(0, 0)])
        visited = set()

        def get_live_count(neighbours):
            live_count = 0
            
            for xi, yi in neighbours:
                if board[xi][yi] in [1, 'Z'] :
                    live_count += 1
            
            return live_count

        def dead_condition(neighbours):
            live_count = get_live_count(neighbours)
            return 'X' if live_count == 3 else 0

        def live_condition(neighbours):
            live_count = get_live_count(neighbours)
            if live_count < 2:
                return 'Z'
            
            if live_count > 3:
                return 'Z'
            
            if live_count in [2,3]:
                return 1

        neighbours_2 = []
        while neighbours:
            (x, y) = neighbours.popleft()
            if (x,y) not in visited:
                for xi, yi in points:
                    if 0 <= xi+x < R and 0 <= yi+y < C:
                        neighbours_2.append((xi+x, yi+y))
                visited.add((x,y))

                if board[x][y] == 0:
                    board[x][y] = dead_condition(neighbours_2)
                
                if board[x][y] == 1:
                    board[x][y] = live_condition(neighbours_2)
            
            if neighbours_2:
                neighbours.extend(neighbours_2)
                neighbours_2 = []
        
        x, y = 0, 0
        while x < R:
            y = 0
            while y < C:
                if board[x][y] == 'Z':
                    board[x][y] = 0
                if board[x][y] == 'X':
                    board[x][y] = 1
                y += 1
            x += 1
        
        return board

abc = Solution()
print (np.matrix(abc.gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
])))

                

        
        

        

