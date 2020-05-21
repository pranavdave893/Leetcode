class Solution(object):
    def rotate_1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Transpose the matrix
        n = len(matrix)
        for i in range(n-1):
          for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
          
        # change columns:
        for i in range(n):
          for j in range(n/2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
        
        return matrix
    
    def rotate_2(self, matrix):
      # reverse and then transpose.
      matrix = matrix[::-1]
      for i in range(len(matrix)):
          for j in range(i):
              matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

      return matrix 
       

abc = Solution()
# print (abc.rotate_1([
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]))

print (abc.rotate_2([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))