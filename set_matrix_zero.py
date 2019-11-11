import numpy as np
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        def is_valid(ri, rc):
            return 0<= ri < m and 0<= rc < n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = -1
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0

                    for x in range(0, m):
                        matrix[x][j] = 0
                    
                    for y in range(0, n):
                        matrix[i][y] = 0
                        
                    # for ri, rc in [(0,1),(1,0),(-1,0),(0,-1)]:
                    #     R, C = i+ri, j+rc
                    #     if is_valid(R, C):
                    #         matrix[R][C] = 0

        print (np.matrix(matrix))

abc = Solution()
abc.setZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1]
])

abc.setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
])
