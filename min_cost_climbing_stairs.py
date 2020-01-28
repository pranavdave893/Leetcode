class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        
        dp = [0] * (len(cost) + 1)
        
        if len(cost) < 2:
            return cost[1]
        
        dp[0], dp[1] = cost[0], cost[1]
        
        for x in range(2, len(cost)+1):
            dp[x] = min(dp[x-1], dp[x-2]) + (0 if x == len(cost) else cost[x])
        
        return dp[-1]