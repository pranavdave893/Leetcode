class Solution(object):
    def canJump(self, nums):
        if not nums: return False
        first = nums[0]
        if first == 0 and len(nums) == 1:return True
        for x in xrange(first, 0, -1):
            if x >= len(nums):
                return True
            ans = self.canJump(nums[x:])
            if ans:
                return ans
            else:
                continue

        return False

abc = Solution()
print (abc.canJump([2,5,0,0]))
print (abc.canJump([2,3,1,1,4]))
print (abc.canJump([3,2,1,0,4]))