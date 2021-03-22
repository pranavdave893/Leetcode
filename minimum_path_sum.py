class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        R = len(grid)
        C = len(grid[0])
        
        dp = [[0]*C for _ in range(R)]
        
        
        def dfs(x, y):
            if x >= R or y >= C:
                return float('inf')
            
            if dp[x][y]:
                return dp[x][y]
            
            if x == R-1 and y == C-1:
                return grid[x][y]
            
            
            path1 = dfs(x+1, y)
            path2 = dfs(x, y+1)
            
            dp[x][y] = grid[x][y] + min(path1, path2)
            return dp[x][y]
        
        print (dfs(0, 0))


        R = len(grid)
        C = len(grid[0])

        if not grid or not grid[0]:
            return 0
        
        dp = [[0] * len(grid[0])] * len(grid)

        dp[0][0] = grid[0][0]

        for i in range(R):
            for j in range(C):
                if i == j == 0:
                    continue

                if 0 < i < R and 0< j < C:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                
                elif 0 < i < R and not 0 < j < C:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                
                elif 0 < j < C and not 0<i<R:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
        
        print (dp[-1][-1])

abc = Solution()
abc.minPathSum([
    [1,3,1],
    [1,5,1],
    [4,2,1]
])