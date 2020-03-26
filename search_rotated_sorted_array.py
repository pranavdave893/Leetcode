class Solution:
    def search(self, nums, target):
        L, H = 0, len(nums)
        while L < H:

            M = (L+H) // 2
            if target < nums[0] < nums[M]: # -inf (2,3,4,1,2) target = 1
                L = M+1

            elif target >= nums[0] > nums[M]: # +inf (4,5,1,2,3) target = 4 or 5
                H = M

            elif nums[M] < target:
                L = M+1

            elif nums[M] > target:
                H = M
            else:
                return M
        return -1
abc = Solution()
print (abc.search([4,5,6,7,0,1,2],3))