class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        first_row, first_col = 0, 0
        square_range = n*n
        rows = cols = n
        matrix = [[0]*n for i in range(n)]
        count = 0
        
        
        while rows > 0 and cols > 0:
            last_row = first_row + rows -1
            last_col = last_row
            
            for i in range(cols):
                count += 1
                matrix[first_row][first_col + i] = count
            for i in range(1, rows):
                count += 1
                matrix[first_row + i][last_col] = count
            
            for i in range(1, cols):
                count += 1
                matrix[last_row][last_col - i] = count
            
            for i in range(1, rows-1):
                count += 1
                matrix[last_row - i][first_col] = count
            
            first_row += 1
            first_col += 1
            
            rows -= 2
            cols -= 2
        
        return matrix

abcd = Solution()
print (abcd.generateMatrix(3))