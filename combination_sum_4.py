class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        dp = {}

        def dp_recur(nums, target, dp):
            if target in dp:
                return dp[target]
            else:
                count = 0
                for x in nums:
                    if x <= target:
                        new_target = target - x
                        if new_target == 0:
                            count += 1
                            continue 
                        count += dp_recur(nums, new_target, dp)
            
                dp[target] = count
            return count
    
        count = dp_recur(nums, target, dp)
        # print (dp)
        
        return count
    
    def combinationSum4_bottomup(self, nums, target):
        dp = [0] * (target+1)
        dp[0] = 1

        # This is the same thing we do in for loop and recursion.
        for i in range(1, target+1):
            for num in nums:
                if i>=num:
                    dp[i] += dp[i-num]
        
        return dp[target]
                    
        

abc = Solution()
print (abc.combinationSum4([1,2,3,4], 4))
print (abc.combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 10))
print (abc.combinationSum4_bottomup([1,2,3,4], 4))
print (abc.combinationSum4_bottomup([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 10))