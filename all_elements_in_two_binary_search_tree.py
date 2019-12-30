class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack_1 = []
        stack_2 = []

        def dfs(root, ans):
            if not root:
                return
            dfs(root.left, ans)
            ans.append(root.val)
            dfs(root.right, ans)
            return ans
        
        if not root1:
            dfs(root2, ans)
            return ans
        
        if not root2:
            dfs(root1, ans)
            return ans
        
        def append_left_value(temp_root, stack):
            while temp_root:
                stack.append(temp_root)
                temp_root = temp_root.left
            
            return stack
        
        stack_1 = append_left_value(root1 ,stack_1)
        
        stack_2 = append_left_value(root2, stack_2)
        
        while stack_1 and stack_2:
            if stack_1[-1].val == stack_2[-1].val:
                x = stack_1.pop()
                y = stack_2.pop()
                ans.append(x.val)
                ans.append(y.val)

                if x.right:
                    stack_1 = append_left_value(x.right, stack_1)
                
                if y.right:
                    stack_2 = append_left_value(y.right, stack_2)
            
            elif stack_1[-1].val < stack_2[-1].val:
                x = stack_1.pop()
                ans.append(x.val)
                if x.right:
                    stack_1 = append_left_value(x.right, stack_1)
            
            elif stack_1[-1].val > stack_2[-1].val:
                y = stack_2.pop()
                ans.append(y.val)
                if y.right:
                    stack_2 = append_left_value(y.right, stack_2)
        
        if stack_1:
            x = stack_1.pop()
            ans = dfs(x, ans)
        
        if stack_2:
            y = stack_2.pop()
            ans = dfs(y, ans)
        
        return ans

abc = Solution()
roo1 = TreeNode