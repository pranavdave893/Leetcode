class Solution(object):
    def validTree(self, n, edges):
        if not edges:
            return False
        
        graph = {}
        
        for x,y in edges:
            if x not in graph:
                graph[x] = [y]
                graph[y] = [x]
            else:
                graph[x].append(y)
                graph[y] = [x]
        
        visited = set()

        print (graph)
        
        def dfs(prev_node, curr_node):
            visited.add(curr_node)
            for next_node in graph[curr_node]:
                if next_node in graph and next_node != prev_node:
                    if next_node in visited:
                        return False
                    else:
                        return dfs(curr_node, next_node)
            return True
        
        return dfs(None, edges[0][0])
        
abc = Solution()
print (abc.validTree(5,[[0,1],[0,2],[1,2],[2,3],[2,4]]))