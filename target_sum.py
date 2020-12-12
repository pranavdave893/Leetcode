from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        ans = 0
        sm = 0
        
        def dfs(idx, sm):
            nonlocal ans
            
            if sm == S and idx >= len(nums):
                ans += 1
                return
                
            if idx >= len(nums):
                return
            
            # for x in range(idx, len(nums)):
            dfs(idx+1, sm + nums[idx])
            dfs(idx+1, sm - nums[idx])
        
        dfs(0, sm)
        return ans
    
    def findTarget(self, nums, S):
        sm = 0
        memo = {}
        
        def dfs(nums, idx, sm):
            
            if idx == len(nums):
                if sm == S:
                    memo[(idx, sm)] = 1
                else:
                    memo[(idx, sm)] = 0
            
            if (idx, sm) not in memo:
                memo[(idx, sm)] = dfs(nums, idx+1, sm + nums[idx]) + dfs(nums, idx+1, sm - nums[idx])
            return memo[(idx, sm)]
        
        dfs(nums, 0, 0)
        return memo[(0, 0)]
    
    def findTargetSumWays_2(self, nums: List[int], S: int) -> int:
       memo = {}
       def DFS(nums,i,summary):
           if i == len(nums):
               if summary == S:
                   memo[(i,summary)] = 1
               else:
                   memo[(i,summary)] = 0
           if (i,summary) not in memo:   
               memo[(i,summary)] = DFS(nums,i+1,summary+nums[i]) + DFS(nums,i+1,summary-nums[i])
           return memo[(i,summary)]
       DFS(nums,0,0)
       return memo[(0,0)]

abc = Solution()
print (abc.findTarget([1,1,1,1,1], 3))