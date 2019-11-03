from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if not edges:
            return False
        
        graph = defaultdict(set)
        
        for x,y in edges:
            graph[x].add(y)
            graph[y].add(x)
        
        visited = set()
        
        def dfs(prev_node, curr_node):
            visited.add(curr_node)
            for next_node in graph[curr_node]:
                # import pdb; pdb.set_trace()
                if next_node in graph and next_node != prev_node:
                    if next_node in visited:
                        return False
                    else:
                        dfs(curr_node, next_node)
            
            if len(visited) == n:
                return True

        abc =  dfs(None, edges[0][0])
        import pdb; pdb.set_trace()
        return False if len(visited) != n else abc

abc = Solution()
print (abc.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))