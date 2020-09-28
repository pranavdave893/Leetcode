"""
Get all the path from source to destination in a graph
"""

from collections import defaultdict

class Solution():
    def get_paths(self, lst, start, end):

        graph = defaultdict(list)

        for x, y in lst:
            graph[x].append(y)

        path = []    
        visited = set()

        def dfs(child, new_path):
            if child in visited:
                return

            visited.add(child)

            if child == end:
                path.append(new_path)
                visited.remove(child)
            
            for new_child in graph[child]:
                dfs(new_child, new_path+[new_child])
            
        dfs(0, [0])
        print (path)


abc = Solution()
abc.get_paths([[1,3], [1, 2], [2, 5], [2, 3],[0, 1], [3, 5], [2, 4], [4, 3]], 0, 5)


"""
0 : 1
1 : 3, 2
2 : 3, 4, 5
3 : 5
4 : 3
"""