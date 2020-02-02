class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root: return 0
        self.res = total_sum =  0

        def dfs(node, total_sum):
            if not node:
                return total_sum
            
            total_sum += node.val
            total_sum = dfs(node.left, total_sum)
            total_sum = dfs(node.right, total_sum)
            return total_sum
    
        total_sum = dfs(root, total_sum)

        def child_dfs(node):
            if not node: return 0
            
            left = child_dfs(node.left)
            right = child_dfs(node.right)

            self.res = max(self.res, left * (total_sum-left), right * (total_sum-right))

            return left + right + root.val
        
        child_dfs(root)
        return self.res % % (10**9 + 7)