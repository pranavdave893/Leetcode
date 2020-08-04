# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        inorder_map = {}
        for idx, x in enumerate(inorder):
            inorder_map[x] = idx
        
        def dfs(low, high):
            if low > high: return None
            if not inorder or not postorder:
                return
            
            root = TreeNode(val=postorder.pop())
            idx = inorder_map[root.val]
            root.right = dfs(idx+1, high)
            root.left = dfs(low, idx-1)
            return root
        
        root = dfs(0, len(inorder))
        return root
        

abc = Solution()
abc.buildTree([1,2,3,4], [2,1,4,3])