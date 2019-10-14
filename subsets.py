class Solution(object):
    def subsets(self, nums):
        result = []

        def dfs(temp, idx):
            result.append(temp[:])

            for i in range(idx, len(nums)):
                temp.append(nums[i])
                dfs(temp, i+1)
                temp.pop()
        
        dfs([], 0)
        return result

abc = Solution()
print (abc.subsets([1,2,3]))
            
        