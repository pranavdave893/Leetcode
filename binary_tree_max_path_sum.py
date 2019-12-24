# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        self.mx_value = root.val
        left_value = self.dfs(root.left)
        
        right_value = self.dfs(root.right)
        # import pdb; pdb.set_trace()
        return max(self.mx_value, root.val, left_value, right_value, root.val+left_value+right_value, root.val+left_value, root.val + right_value)
    
    def dfs(self, root):
        if not root:
            return float('-inf')

        left_val = self.dfs(root.left)
        right_val = self.dfs(root.right)

        self.mx_value = max(root.val, left_val + root.val, right_val + root.val, root.val + left_val + right_val, 
                            left_val, right_val, self.mx_value)
        
        # import pdb; pdb.set_trace()
        return_value = max(root.val, root.val + left_val, root.val + right_val)

        return return_value


tree = TreeNode(1)
tree.left = TreeNode(2)

abc = Solution()
print (abc.maxPathSum(tree))