"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
tags : Facebook, medium, tree, Blind curated
"""

class Solution:

    def kthSmallestDfs(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res
    

    def helper(self, root):
        if k < 0: return
        if not root: return

        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            return root.val
        
        self.helper(root.right)


    def kthSmallestBFS(self, root, k):
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            
            root = root.right
        
        return None