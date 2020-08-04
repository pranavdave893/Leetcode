from functools import lru_cache
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        def dfs(d, tg):
            if (d, tg) in memo:
                return memo[(d, tg)]
            
            if d <= 0 or tg <= 0:
                return 0
            
            if d == 1 and tg  > f:
                return 0
            if d == 1 and tg <= f:
                return 1
            
            if tg > f*d or tg < d:
                return 0
            
            ans = 0
            for x in range(1, f+1):
                ans += dfs(d-1, tg-x)
            memo[(d, tg)] = ans
            return ans
        
        return dfs(d, target) % (10**9 + 7)

abc = Solution()
print (abc.numRollsToTarget(30, 30, 500))

