"""
https://www.geeksforgeeks.org/construct-binary-tree-string-bracket-representation/
tags : Medium/Hard, Tree
company: Houzz
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution():
    def convertBTree(self, s):

        def dfs(s, idx):
            if not s:
                return None
            
            while idx < len(s):
        
                if s[idx] == "(" and idx+1 < len(s):
                    root.left, idx = dfs(s, idx+1)
                    if idx < len(s) and s[idx] == "(":
                        root.right, idx = dfs(s, idx+1)
                        continue
                
                elif s[idx] == ")":
                    return root, idx+1
                
                else:
                    root = Node(s[idx])
                
                
                idx += 1
        
            return root, idx
        
        root, idx = dfs(s, 0)
        return root


abc = Solution()
abc.convertBTree("4(2(3)(1))(6(5))")
