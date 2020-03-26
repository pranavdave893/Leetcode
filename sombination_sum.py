class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        
        def dfs(nums, target, idx, path, res):
            if target < 0:
                return
            
            if target == 0:
                res.append(path)
                return
            
            for i in xrange(idx, len(nums)):
                dfs(nums, target-nums[i], i, path+[nums[i]], res)
        
        res = []
        dfs(candidates, target, 0, [], res)
        return res

abc = Solution()
abc.combinationSum([2,3,6,7], 7)