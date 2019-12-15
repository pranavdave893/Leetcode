import numpy as np
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        x = matrix
        matrix.reverse() 
        print (np.matrix(x))

abc = Solution()
abc.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])