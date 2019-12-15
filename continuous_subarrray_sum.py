class Solution(object):
    def checkSubarraySum(self, nums, k):
        
        if not nums:
            return False

        dp = [0]*len(nums)
        dp[0] = nums[0]
        
        for x in range(1, len(nums)):
            dp[x] = dp[x-1] + nums[x]

            if k != 0 and dp[x] % k == 0:
                return True
            
            elif dp[x] == 0 and k == 0:
                return True
            
            elif x > 1:
                for y in range(0, x-1):
                    if k != 0 and (dp[x] - dp[y]) % k == 0:
                        return True
                    elif k == 0 and (dp[x] - dp[y]) == 0:
                        return True
        
        return False

abc = Solution()
print (abc.checkSubarraySum([5,0,0], 0))
print (abc.checkSubarraySum([23,2,6,4,7], 0))
print (abc.checkSubarraySum([0,0],0))






            
