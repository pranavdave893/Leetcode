from typing import List
from collections import defaultdict, deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        g = defaultdict(list)
        
        ans = []
        
        visited = set()   
        temp = [0]
        def dfs(start, temp):
            if start == n-1:
                temp.append(start)
                ans.append(temp[:])
                return

            visited.add(start)
            temp.append(start)
            
            for child in graph[start]:
                dfs(child, temp[:])
        
        for child in graph[0]:
            dfs(child, temp[:])
        return ans

abc = Solution()
print (abc.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))