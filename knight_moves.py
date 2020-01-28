from collections import defaultdict, deque

class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x, y = abs(x), abs(y)
        points = [(1,2), (-1,2), (1, -2), (-1, -2), (2,1), (-2,1), (2,-1), (-2,-1)]

        dq = deque()
        dq.append((0, 0, 0))

        visited = {(0,0)}

        while deque:
            np_x, np_y, d = dq.popleft()
            
            for p_x, p_y in points:
                i, j = np_x + p_x, np_y + p_y

                if (i,j) == (x,y):
                    return d + 1
                
                if (i,j) not in visited and i > -2 and j > -2:
                    dq.append((i, j, d+1))
                    visited.add((i, j))
    
    def bfs(self, curr_points, curr_seen):
        temp_points = []
        for i, j in curr_points:
            for x, y in self.points:
                
                nx, ny = x + i, y + j

                if (nx, ny) not in curr_seen and -2 <= nx <= self.x + 2 and -2 <= ny <= self.y +2:
                    curr_seen.add((nx, ny))
                    temp_points.append((nx, ny))
        
        return temp_points, curr_seen

    def minKnightMoves_bfs(self, x, y):
        if x == y == 0: return 0
        self.x, self.y = abs(x), abs(y)
        self.points = [(1,2), (-1,2), (1, -2), (-1, -2), (2,1), (-2,1), (2,-1), (-2,-1)]
        start_point, start_seen = [(0, 0)], {(0, 0)}
        end_point, end_seen = [(self.x, self.y)], {(self.x, self.y)}
        start_dist, end_dist = 0, 0

        while True:

            if start_seen & end_seen: return start_dist + end_dist
            
            start_point, start_seen = self.bfs(start_point, start_seen)
            start_dist += 1

            if start_seen & end_seen: return start_dist + end_dist

            end_point, end_seen = self.bfs(end_point, end_seen)
            end_dist += 1
        

abc = Solution()
# print (abc.minKnightMoves(11, 248))
print (abc.minKnightMoves_bfs(11, 248))

                




