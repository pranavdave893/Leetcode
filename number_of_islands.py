class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def is_safe(r, c):
            return 0<= r < R and 0 <= c < C and grid[r][c] == "1" and not visited.get((r,c))
        
        def processNeighbours(i, j, count):
            """
            Method to process Neighbours and to count the maximum size of island.
            """
            visited[(i, j)] = 1
            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                r, c = i + di, j + dj
                if is_safe(r,c):
                    count += 1
                    count = processNeighbours(r, c, count)
            
            return count
        
        visited = {}
        
        R, C = len(grid), len(grid[0])
        count_of_island = 0
        max_size = 0
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and not visited.get((i,j)):
                    island_size = 1
                    island_size = processNeighbours(i,j,1)
                    count_of_island += 1
                    
                    if island_size > max_size:
                        max_size = island_size
        
        return count_of_island

abc = Solution()
abc.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])