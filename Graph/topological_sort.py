"""
https://leetcode.com/problems/alien-dictionary/discuss/397216/Clean-concise-super-easy-python-topological-sort-Kahn's
https://leetcode.com/problems/alien-dictionary/discuss/370727/Python-topo-sort-greater-91
https://leetcode.com/problems/alien-dictionary/discuss/370466/python-topological-sort-for-beginners-greater-98
https://leetcode.com/problems/alien-dictionary/discuss/387823/Python-O(N)-DFS-and-Topological-Sort-beats-100-with-detailed-explanation
https://leetcode.com/problems/alien-dictionary/discuss/405220/Python-Graph%2BTopological-Sort-or-Beats-99.8
https://leetcode.com/problems/alien-dictionary/discuss/406447/36ms-93-Python-3-solution-(easy-to-understand)

"""

class Topological_sort():

    def isAcyclic(self, seen, graph, parent, rec_stac):
        seen.add(parent)
        rec_stac.add(parent)

        for next_node in graph.get(parent,[]):
            if next_node in rec_stac:
                return True
            if next_node not in seen and self.isAcyclic(seen, graph, next_node, rec_stac):
                return True
        rec_stac.remove(parent)
        return False


    def topo_util(self, graph):
        seen = set()
        rec_stac = set()
        for parent in graph:
            if self.isAcyclic(seen, graph, parent, rec_stac):
                return ""

        in_degree = set()
        zero_in_degree = set()

        for key,value in graph.items():
            zero_in_degree.add(key)
            for x in value:
                in_degree.add(x)

        zero_in_degree = zero_in_degree - in_degree
        answer_stack = []
        visited = set()
        
        for node in zero_in_degree:
            self.topo_actual(graph, node, visited, answer_stack)
        
        return ''.join(answer_stack)
    
    def topo_actual(self, graph, node, visited, answer_stack):
        if node not in visited:
            visited.add(node)
            if node in graph:
                for next_node in graph[node]:
                    self.topo_actual(graph, next_node, visited, answer_stack)
                answer_stack.insert(0, node)
            else:
                answer_stack.insert(0, node)
    
    def alian_dictonary(self, words):
        graph = {}

        for word in words:
            for c in word:
                graph[c] = set()

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            x = 0
            while x < len(word1) and x < len(word2):
                char1 = word1[x]
                char2 = word2[x]
                # import pdb; pdb.set_trace()
                if char1 != char2:
                    if char2 not in graph[char1]:
                        graph[char1].add(char2)
                    break
                x += 1
            
        return self.topo_util(graph)

words = ["wrt", "wrf", "erx", "ett", "rftt"]
words2 = ["z","z"]
# words = ["za","zb","ca","cb"]
abc = Topological_sort()
# print (abc.alian_dictonary(words))
print (abc.alian_dictonary(words2))
