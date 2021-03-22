from typing import List
from collections import deque
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # find the root node, assume root is node(0) by default
		# a node without any parent would be a root node
		# note: if there are multiple root nodes => 2+ trees
        root = 0
        children = set(leftChild + rightChild)
        for i in range(n):
            if i not in children:
                root = i
        
        visited = set()
        q = deque([root])

        while q:
            node = q.popleft()
            if node in visited:
                return False
            
            visited.add(node)
            
            if leftChild[node] != -1:
                q.append(leftChild[node])
            
            if rightChild != -1:
                q.append(rightChild[node])
        
        return len(visited) == n

        # leftEdge = 0
        
        # if n == 1:
        #     return True
        
        # for x in leftChild:
        #     if x != -1:
        #         leftEdge += 1
        
        # rightEdge = 0
        
        # for x in rightChild:
        #     if x != -1:
        #         rightEdge += 1
        
        # # Since there should be exactly n-1 edges we calculate first all the edges.
        # if leftEdge + rightEdge != n-1:
        #     return False
        
        
        # parent = [[] for i in range(n)]
        
        # for i in range(n):
            
        #     if leftChild[i] != -1:
        #         parent[leftChild[i]].append(i)
            
        #     if rightChild[i] != -1:
        #         parent[rightChild[i]].append(i)
        
        
        # for i in range(n):
        #     # Check if parent child relationship is not bi-directional.
        #     if parent[i] and parent[parent[i][0]]==[i]:
        #         return False    
        
        # # FIND ALL ROOT NODES (IE. THOSE WITHOUT PARENT) - O(N)
        # roots = [i for i in range(len(parent)) if not parent[i]]
        
        # # CHECK IF THERE'S EXACTLY 1 ROOT NODE  - O(1)
        # if len(roots) != 1:
        #     return False
        
        # root = roots[0]
        
        # if leftChild[root] == -1 and rightChild[root] == -1:
        #     return False
        
        # return True      
        

abc = Solution()
print (abc.validateBinaryTreeNodes(4, [1,0,3,-1],[-1, -1, -1, -1]))