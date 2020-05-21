class Solution(object):
    def combinationSum(self, nums, target):
        self.ans = 0
        nums.sort()
        
        def dfs(nums, ans, i, target, path=[]):
            if target < 0:
                return
            if target == 0:
                self.ans += 1
                return
            
            for x in range(i, len(nums)):
                dfs(nums, self.ans, x, target-nums[x], path+[nums[x]])
        
        dfs(nums, self.ans, 0, target)
        return ans

abc = Solution()
abc.combinationSum([2,3,6,7], 7)
