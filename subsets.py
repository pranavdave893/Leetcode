# Better solution
class Solution_2:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, res, [], 0)
        return res
    
    
    def dfs(self, nums, res, path, i):
        res.append(path)
        for x in range(i, len(nums)):
            self.dfs(nums, res, path+[nums[x]], x+1)
    
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
            
        