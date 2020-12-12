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
        return self.ans
    
    def combinationSum_2(self, nums, target):
        nums.sort()
        ans = []
        
        def dfs(idx, path, target):

            if target < 0:
                return
            
            if target == 0:
                ans.append(path)
            
            # while idx > 0 and nums[idx-1] == nums[idx]:
            #     idx += 1
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                if nums[i] > target:
                    return
                dfs(i+1, path+[nums[i]], target-nums[i])
        
        dfs(0, [], target)
        return ans

abc = Solution()
# print (abc.combinationSum([2,3,6,7], 7))
print (abc.combinationSum_2([10,1,2,7,6,1,5] ,8))
