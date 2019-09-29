class Solution:
    def lengthOfLIS(self, nums):
        
        if not nums:
            return 0
        
        dp = [1 for i in range(len(nums))]
        
        answer = 0
        
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] < dp[j]+1:
                    dp[i] = 1+ dp[j]
                    if (answer < dp[i]):
                        answer = dp[i]
        
        return answer

abc = Solution()
print (abc.lengthOfLIS([10,22,9,33,21,50,41,60,80]))