# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        self.inorder_map = {i:v for v,i in enumerate(inorder)}
        return self._buildTree(0, len(inorder)-1, postorder)

    
    def _buildTree(self, low, high, postorder):
        if low > high:
            return None
        
        import pdb; pdb.set_trace()
        root = TreeNode(postorder.pop())
        index = self.inorder_map[root.val]

        root.right = self._buildTree(index+1, high, postorder)
        root.left = self._buildTree(low, index-1, postorder)

        return root

abc = Solution()
print (abc.buildTree([9,3,15,20,7], [9,15,7,20,3]))