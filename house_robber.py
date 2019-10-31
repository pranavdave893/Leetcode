class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        if len(nums) <=2:
            return max(nums)
        
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max((nums[i]+dp[i-2]),dp[i-1])
        
        return dp[len(dp)-1]

abc = Solution()
print (abc.rob([2,7,9,3,1]))