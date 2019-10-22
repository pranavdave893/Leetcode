
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        visited = {}
        
        def dfs(prev_node, node):
            
            if node in visited:
                prev_node.neighbors.append(visited[node])
                return
                
            new_node = Node(node.val, [])
            
            visited[node] = new_node
            
            if prev_node:
                prev_node.neighbors.append(new_node)
            
            for neighbor in node.neighbors:
                dfs(new_node, neighbor)
        
            return new_node
        
        return dfs(None, node)