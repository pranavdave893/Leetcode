class Solution(object):
    def sortColors(self, nums):
       ans = []

       def dfs(idx, temp):
           ans.append(temp[:])

           for x in range(idx, len(nums)):
               temp.append(nums[x])
               dfs(temp, idx+1)
               temp.pop()

               


abc = Solution()
abc.sortColors([1,2,3])
