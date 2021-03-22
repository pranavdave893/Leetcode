from typing import List
class Solution:
    def calculateMinimumHP(self, M: List[List[int]]) -> int:
        
        
        ans = 0
        for i in range(R):
            for j in range(C):
                dp[i][j] = max(dp[i][j], abs(dfs(i, j, M[i][j]))+1)
                ans = max(ans, dp[i][j])
        
        return ans

abc = Solution()
abc.calculateMinimumHP([
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
])