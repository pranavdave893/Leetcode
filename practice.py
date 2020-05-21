import heapq
from serialize
class Solution(object):
    def lengthOfLIS(self, nums, k):
        def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(root, step):
            if not root:
                return step, False
            if not root.left:
                step += 1
                if step == k:
                    return root.val, True
                step, found = dfs(root.right, step)
                if found:
                    return step, True
            else:
                step, found = dfs(root.left, step)
                if step == k:
                    return root.val, True
                
                step += 1
                if step == k:
                    return root.val, True
                step, found = dfs(root.right, step)
                if found: return step, True
            
            return step, False
        
        step = 0
        step, found = dfs(root.left, step)
        return step

                    
        

abc = Solution()
print (abc.lengthOfLIS([3,2,3,1,2,4,5,5,6], 4))