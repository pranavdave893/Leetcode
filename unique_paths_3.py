class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        R = len(grid)
        C = len(grid[0])
        ans = 0
        zero_count = 0
        extra_count = 0
        points = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        def is_valid(x, y):
            return 0 <= x < R and 0 <= y < C and grid[x][y] != -1
        
        def dfs(x, y, ans, temp_zero):
            for i, j in points:
                r, c = x+i, y+j
                if is_valid(r,c) and grid[r][c] == 0:

                    temp_zero += 1
                    grid[r][c] = -2
                    ans = dfs(r, c, ans, temp_zero)
                    grid[r][c] = 0 if grid[r][c] == -2 else grid[r][c]
                    temp_zero -= 1
                
                elif is_valid(r,c) and grid[r][c] == 2:
                    if temp_zero == zero_count:
                        ans += 1
            
            return ans
        
        for x in xrange(R):
            for y in xrange(C):
                if grid[x][y] == 1:
                    start_point = (x, y)
                elif grid[x][y] == 0: zero_count += 1
                else: extra_count += 1

        ans = dfs(start_point[0], start_point[1], ans, 0)
        return (ans)

abc = Solution()
abc.uniquePathsIII([[0,1],[2,0]])