class Solution(object):
    def findMaxPath(self, matrix):
        near_points = [(0,1),(1,0),(-1,0),(0,-1)]

        def is_valid(i, j):
            return i >=0 and j>=0 and i<r and j<c

        def dfs(x, y, dp_matrix):
            if dp_matrix[x][y] != -1:
                return dp_matrix[x][y]

            max_sum = 1

            for i, j in near_points:
                R = x+i
                C = y+j
                if is_valid(R, C) and matrix[R][C] > matrix[x][y]:
                    len_path = dfs(R, C, dp_matrix) + 1 
                    max_sum = max(len_path, max_sum)
                    
            dp_matrix[x][y] = max_sum
            return dp_matrix[x][y]
        
        r, c = len(matrix), len(matrix[0])
        dp_matrix = [[-1]*c for _ in range(r)]
        res = 0
        for x in range(r):
            for y in range(c):
                dp_matrix[x][y] = dfs(x,y,dp_matrix)
                if dp_matrix[x][y] > res:
                    res = dp_matrix[x][y]
        
        return res

abc = Solution()
matrix = [
    [7,2,3,4,5],
    [36,37,38,34,6],
    [33,44,46,40,7],
    [24,43,42,41,8],
    [35,32,47,30,9]

]
print (abc.findMaxPath(matrix))






        
