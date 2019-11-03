class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visited_path = {}
        visited_dp = [[0]*n]*m
        for col in range(n):
            visited_dp[0][col] = 1
        
        for row in range(m):
            visited_dp[row][0] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                visited_dp[i][j] = visited_dp[i-1][j] + visited_dp[i][j-1]
            
        print(visited_dp[m-1][n-1])

        def recur(i, j, visited_path):
            if i == m-1 or j == n-1:
                return 1

            if (i, j) in visited_path:
                return visited_path[(i, j)]
            
            visited_path[(i,j)] = recur(i, j+1, visited_path) + recur(i+1, j, visited_path)
            return visited_path[(i,j)]
        
        return recur(0,0, visited_path)

abc = Solution()
print (abc.uniquePaths(3,2))