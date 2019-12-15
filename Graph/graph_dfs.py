from create_graph import Graph


class dfs_graph(object):
    abc = Graph()
    g = abc.create_graph()

    def dfs_graph_util(self, v, visited):
        visited[v] = True
        import pdb; pdb.set_trace()
        print (v)
        for i in self.g[v]:
            if visited[i] == False:
                self.dfs_graph_util(i, visited)
    
    def dfs(self, v):
        V = len(self.g)
        visited = [False] * V
        for i in range(V):
            if visited[i] == False:
                self.dfs_graph_util(i, visited)
    

abc = dfs_graph()
print (abc.dfs(1))