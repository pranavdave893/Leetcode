from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        graph = defaultdict(list)
        def dfs(parent, current, visited):
            visited.add(current)
            for child in graph[current]:
                if child not in visited:
                    if dfs(current, child, visited):
                        return True
                elif child in visited and child != parent:
                    return True
            return False
        
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        
        if dfs(-1, 0, visited):
            return False
        if len(visited) != n:
            return False
        return True
        
abc = Solution()
# print (abc.validTree(5,[[0,1],[0,2],[1,2],[2,3],[2,4]])) # False
print (abc.validTree(4, [[0,1],[1,2],[1,3],[1,4],[2,3]]))