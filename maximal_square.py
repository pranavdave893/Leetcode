class Solution(object):
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        max_len = 1
        
        for i in range(m):
            matrix[i][0] = int(matrix[i][0])
        
        for j in range(n):
            matrix[0][j] = int(matrix[0][j])
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != '0':
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                    max_len = max(matrix[i][j], max_len)
                else:
                    matrix[i][j] = int(matrix[i][j])
        print(max_len * max_len)

abc = Solution()
abc.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])