class Solution:
    def findRedundantDirectedConnection(self, edges):
        def find(u):  # union find
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]
        
        def detect_cycle(edge):  # check whether you can go from u to v (forms a cycle) along the parents 
            u, v = edge
            while u != v and u in parents:
                u = parents[u]
            return u == v
        
        candidates = []  # stores the two edges from the vertex where it has two parents
        parents = {}
        for u, v in edges:
            if v not in parents:
                parents[v] = u
            else:
                candidates.append((parents[v], v)) 
                candidates.append((u, v))
           
        if candidates:  # case 2 & case 3 where one vertex has two parents
            return candidates[0] if detect_cycle(candidates[0]) else candidates[1]
        else:  # case 1, we just perform a standard union find, same as redundant-connection
            p = list(range(len(edges)+1))
            for edge in edges:
                u, v = map(find, edge)
                if u == v:
                    return edge
                p[u] = p[v]

abc = Solution()
abc.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]])
