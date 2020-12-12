from typing import List
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        leftEdge = 0
        
        if n == 1:
            return True
        
        for x in leftChild:
            if x != -1:
                leftEdge += 1
        
        rightEdge = 0
        
        for x in rightChild:
            if x != -1:
                rightEdge += 1
        
        # Since there should be exactly n-1 edges we calculate first all the edges.
        if leftEdge + rightEdge != n-1:
            return False
        
        
        parent = [[] for i in range(n)]
        
        for i in range(n):
            
            if leftChild[i] != -1:
                parent[leftChild[i]].append(i)
            
            if rightChild[i] != -1:
                parent[rightChild[i]].append(i)
        
        
        for i in range(n):
            if parent[i] and parent[parent[i][0]]==[i]:
                return False    
        
        roots = [i for i in range(len(parent)) if not parent[i]]
        
        if len(roots) != 1:
            return False
        
        root = roots[0]
        
        if leftChild[root] == -1 and rightChild[root] == -1:
            return False
        
        return True      
        

abc = Solution()
abc.validateBinaryTreeNodes(4, [1,0,3,-1],[-1, -1, -1, -1])