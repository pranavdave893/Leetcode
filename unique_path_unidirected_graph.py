from collections import defaultdict
class Solution:

    def find_path(self, lst, start, end):

        graph = defaultdict(list)

        for x, y in lst:
            graph[x].append(y)
            graph[y].append(x)
        
        if start not in graph:
            return []
        
        visited = set()
        ans = []
        temp = [start]
        visited.add(start)
        
        def dfs(start, temp):
            for child in graph[start]:

                if child in visited:
                    continue
                
                if child == end:
                    ans.append(temp + [child])
                    continue
                
                visited.add(child)
                dfs(child, temp[:] + [child])
        
        dfs(start, temp)
        return ans
        
lst = [[0,1], [1,7], [1,2], [2,3], [2,6], [3,4], [4,5], [5,6], [6,7]]
abc = Solution()
print (abc.find_path(lst, 0, 6))