from collections import deque
class Solution:
    def hasPath(self, maze, start, destination):

        ## DFS
        R, C, visited = len(maze), len(maze[0]), set()
        direction = [(0,1),(1,0),(-1,0),(0,-1)]


        def dfs(x,y):
            if [x,y] == destination:
                return True

            visited.add((x,y))
            
            # import pdb; pdb.set_trace()
            for i, j in direction:
                newX, newY = x, y
                while 0 <= newX + i < R and 0<= newY+j < C and maze[newX+i][newY+j] == 0:
                    newX += i
                    newY += j
                
                if (newX, newY) not in visited:
                    if dfs(newX, newY): return True
            
            return False

        return dfs(*start)

        # XXX: this is BFS approch.
        # m, n, stopped = len(maze), len(maze[0]), set()
        # adj = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        # q = deque([start])
        # while q:
        #     x, y = q.popleft()
        #     if [x, y] == destination:
        #         return True
        #     if (x, y) in stopped:
        #         continue
        #     stopped.add((x, y))
            
        #     for i, j in adj:
        #         newX, newY = x, y
        #         while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
        #             newX += i
        #             newY += j
        #         q.append([newX, newY])
        # return False

maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
end = [4,4]
abc = Solution()
print abc.hasPath(maze, start, end)