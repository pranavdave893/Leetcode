"""
https://medium.com/youstart-labs/implement-graphs-in-python-like-a-pro-63bc220b45a0
"""
from collections import defaultdict
class Graph:
    graph_dict = {}

    def addEdge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)
    
    def dfs(self, graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for next_node in graph[start]:
            if next_node not in visited:
                self.dfs(graph, next_node, visited)
        
        return visited
    
    def bfs(self, graph, start):
        visited, queue = set(), [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                for next_node in graph[node]:
                    if next_node not in visited:
                        queue.extend(next_node)
        
        return visited