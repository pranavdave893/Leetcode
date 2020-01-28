class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
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