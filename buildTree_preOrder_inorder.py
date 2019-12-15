# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        import pdb; pdb.set_trace()
        if len(preorder) == 0:
            return None
            
        head = TreeNode(preorder[0])
        stack = [head]
        i = 1
        j = 0
        
        while i < len(preorder):
            temp = None
            t = TreeNode(preorder[i])
            while stack and stack[-1].val == inorder[j]:
                temp = stack.pop()
                j += 1
            if temp:
                temp.right = t
            else:
                stack[-1].left = t
            stack.append(t)
            i += 1
        
        return head


inorder = [3,7,2,9,1,6,0,10,-1,5,-2,8,-3,4,-4]
preorder = [10,9,7,3,2,6,1,0,8,5,-1,-2,4,-3,-4]
abc = Solution()
abc.buildTree(preorder, inorder)