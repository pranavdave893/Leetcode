class Solution(object):
    def island(self, matrix):

        if not matrix or not matrix[0]:
            return 0
        
        R = len(matrix)
        C = len(matrix[0])

        points = ((1, 0), (0, 1), (0,-1), (-1,0))
        visited = set()
        
        sq_area = []

        dct = {}
        
        def is_valid(x, y):
            return 0 <= x < R and 0 <= y < C and matrix[x][y] == 1 and (x, y) not in visited
        
        def dfs(x, y, count):
            
            for r, c in points:
                Rx, Cy = r+x, c+y
                if is_valid(Rx, Cy):
                    visited.add((Rx, Cy))
                    count = dfs(Rx, Cy, count+1)

            return count

        areas = []
        for x in range(R):
            for y in range(C):
                if matrix[x][y] == 1 and (x, y) not in visited:
                    result = dfs(x, y, 0)
                    visited.add((x, y))
                    if result:
                        areas.append(result)
        
        print (areas)


abc = Solution()
abc.island([
  [1,1,1,1,0],
  [1,1,1,1,0],
  [1,1,1,0,0],
  [0,0,0,1,1]
])



# for x in range(1, R):
        #     for y in range(1, C):
        #         if matrix[x][y] == 1:
                    

                    # matrix[x][y] = min(matrix[x-1][y], matrix[x][y-1], matrix[x-1][y-1]) + 1
                    # if matrix[x][y] >= 2:
                    #     dct[matrix[x][y]] += 1

                    #     count = matrix[x][y]
                    #     tmp_count = 2
                    #     while count > 2:
                    #         dct[count-1] -= (2 * tmp_count) - 1
                    #         count -= 1
                    #         tmp_count += 1