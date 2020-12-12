from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
                
        points = ((-1, 0), (0, -1), (1, 0), (0, 1))
        R = len(matrix)
        C = len(matrix[0])
        
        p_visited = [[False]*(C) for _ in range(R)]
        a_visited = [[False]*(C) for _ in range(R)]
        p_q = deque()
        a_q = deque()
        
        points = ((-1, 0), (0, -1), (1, 0), (0, 1))
        
        ans = []
        
        def is_valid(x, y, visited):
            return 0 <= x < R and 0 <= y < C and not visited[x][y]
        
        # def dfs(x, y, visited):
        #     visited[x][y] = True
        #     for i, j in points:
        #         xi, yj = x + i, y + j
        #         if is_valid(xi, yj, visited) and matrix[xi][yj] >= matrix[x][y]:
        #             dfs(xi, yj, visited)

        def bfs(q, visited):
            while q:
                x, y = q.popleft()
                visited[x][y] = True
                for i, j in points:
                    xi, yj = x + i, y + j
                    if is_valid(xi, yj, visited) and matrix[xi][yj] >= matrix[x][y]:
                        q.append((xi, yj))
        

        for r in range(R):
            p_q.append((r, 0))
            a_q.append((r, C-1))
            p_visited[r][0], a_visited[r][C-1] = True, True
        
        for c in range(C):
            p_q.append((0, c))
            a_q.append((R-1, c))
            p_visited[0][c], a_visited[R-1][c] = True, True
            # dfs(0, c, p_visited)
            # dfs(R-1, c, a_visited)
        
        bfs(p_q, p_visited)
        bfs(a_q, a_visited)
            
        for r in range(R):
            for c in range(C):
                if p_visited[r][c] and a_visited[r][c]:
                    ans.append([r, c])
        
        print( ans)

abc = Solution()
abc.pacificAtlantic([
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
])