class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        self.preorder, self.inorder = preorder, inorder
        self.indict = {v:i for i,v in enumerate(inorder)}
        return self.helper(0, len(inorder), 0)
    
    
    def helper(self, Lin, Rin, pre_order_idx):
        root = TreeNode(self.preorder[pre_order_idx])
        root_index = self.indict[root.val]
        
        if Lin < root_index:
            pre_order_idx+= 1
            root.left = self.helper(Lin, root_index, pre_order_idx)
        if root_index+1 < Rin:
            pre_order_idx+=1
            root.right = self.helper(root_index+1, Rin, pre_order_idx)
        return root

abc = Solution()
abc.buildTree([3,9,20,15,7], [9,3,15,20,7])