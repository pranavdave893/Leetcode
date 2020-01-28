from collections import defaultdict
import heapq

class Solution(object):
    def findTheCity(self, n, edges, maxd):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        adj = defaultdict(dict)
        for a,b,c in edges:
            adj[a][b] = adj[b][a] = c
        
        def bfs(s, distanceThreshold):
            visited = [False] * n
            dist = [float('inf')] * n
            frontier = [(0, s)]
            visited[s] = True
            dist[s] = 0
            
            while not all(visited) and frontier:
                d, s = heapq.heappop(frontier)
                if d > distanceThreshold: break
                dist[s] = d
                visited[s] = True
            
                for t in adj[s]:
                    if not visited[t]:
                        heapq.heappush(frontier, (d + adj[s][t], t))
            
            return len([d for d in dist if d <= maxd])
        res = 0
        count = n
        for i in range(n):
            c = bfs(i, maxd)
            if c <= count:
                res = max(res, i)
                count = c
        return res

abc = Solution()
print (abc.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))