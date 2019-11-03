class Solution:
    def climbStairs(self, n):
        
        if n == 0:return 1
        
        if n < 0 : return 0
        count = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return count
    
    def climbStairs_dp(self, n):
        if n == 0: return 1

        if n < 0 : return 0

        base = {1:1, 2:2}
        if base == 1: return 1
        if base == 2: return 2

        for i in range(3, n+1):
            base[i] = base[i-1] + base[i-2]
        
        return base[n]
        
abc = Solution()
print abc.climbStairs(15)
print abc.climbStairs_dp(15)