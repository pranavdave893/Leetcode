class Solution(object):
    def combinationSum2(self, nums, target):
        ans = []
        nums.sort()
        
        def dfs(nums, ans, i, target, path=[]):
            if target < 0:
                return
            if target == 0:
                ans.append(path)
                return
            
            for x in range(i, len(nums)):
                if x > i and nums[x-1] == nums[x]: continue
                dfs(nums, ans, x+1, target-nums[x], path+[nums[x]])
        
        dfs(nums, ans, 0, target)
        return ans

abc = Solution()
abc.combinationSum2([2,5,2,1,2], 5)