class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        answer = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] > nums[i] and dp[i] < dp[j]+1:
                    dp[i] = 1 + dp[j]
                
                answer = max(answer, dp[i])
        
        print (answer)

                    
        

abc = Solution()
abc.lengthOfLIS([10,9,2,5,3,7,101,18])