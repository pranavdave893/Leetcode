class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxSumAdjacentLevelConnectedNodes(self, root):
        if not root:
            return 0
        
        incl_sum = root.val

        if root.left:
            incl_sum += self.maxSumAdjacentLevelConnectedNodes(root.left.left) + self.maxSumAdjacentLevelConnectedNodes(root.left.right)
        
        if root.right:
            incl_sum += self.maxSumAdjacentLevelConnectedNodes(root.right.left) + self.maxSumAdjacentLevelConnectedNodes(root.right.right)
        
        excl_sum = self.maxSumAdjacentLevelConnectedNodes(root.left) + self.maxSumAdjacentLevelConnectedNodes(root.right)

        return max(incl_sum, excl_sum)
    
    def getSumAlternate(self, root):
        if not root:
            return 0
        
        total_sum = root.val

        if root.left:
            total_sum += self.maxSumAdjacentLevel(root.left.left) + self.maxSumAdjacentLevel(root.left.right)
        
        if root.right:
            total_sum += self.maxSumAdjacentLevel(root.right.left) + self.maxSumAdjacentLevel(root.right.right)
        
        return total_sum
    
    def maxSumAdjacentLevel(self, root):
        if not root:
            return 0
        
        return max(self.getSumAlternate(root), self.getSumAlternate(root.left), self.getSumAlternate(root.right))
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.right = TreeNode(5)
root.right.left.right.left = TreeNode(6)

abc = Solution()
print (abc.maxSumAdjacentLevel(root))