"""
https://leetcode.com/problems/rotting-oranges/
"""

import collections
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        queue = collections.deque()
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    queue.append([i,j])
        
        count = 0
         
        def update_grid(nr, nc, grid):
            grid[nr][nc] = 2
        
        def is_valid(nr, nc, grid):
            if 0 <= nr < R and 0 <= nc < C:
                if grid[nr][nc] == 1:
                    return True
            return False
        
        ans = 0
        while queue:
            new_queue = collections.deque()
            while queue:
                r, c = queue.popleft()
                nr, nc = r-1, c
                if is_valid(nr, nc, grid):
                    update_grid(nr, nc, grid)
                    new_queue.append([nr,nc])

                nr, nc = r, c-1
                if is_valid(nr, nc, grid):
                    update_grid(nr, nc, grid)
                    new_queue.append([nr,nc])

                nr, nc = r+1, c
                if is_valid(nr, nc, grid):
                    update_grid(nr, nc, grid)
                    new_queue.append([nr,nc])

                nr, nc = r, c+1
                if is_valid(nr, nc, grid):
                    update_grid(nr, nc, grid)
                    new_queue.append([nr,nc])
            
            queue = new_queue
            if queue:
                ans += 1
        
        if any(1 in row for row in grid):
            return -1
        
        return ans

grid = [[0,2]]
abcd = Solution()
print (abcd.orangesRotting(grid))