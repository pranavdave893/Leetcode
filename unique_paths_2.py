class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        M = obstacleGrid
        ct = 0
        visited = set()
        points = [(0, 1), (1, 0)]
        cache = {}
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])
        
        def is_valid(x, y):
            return x < R and y < C and M[x][y] == 0

        def dfs(x, y, ct, cache):
            if (x,y) in cache:
                return cache[(x, y)]
    
            for i, j in points:
                Rx, Ry = i + x, j + y
                if x == R-1 and y == C-1:                    
                    return 1
                if is_valid(Rx, Ry):
                    x = dfs(Rx, Ry, ct, cache)
                    if x:
                        ct += x 
                        cache[(Rx, Ry)] = ct
        
            return ct

        if is_valid(0, 0):
            ct = dfs(0, 0, ct, cache)
        return ct

abc = Solution()
print (abc.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))




