class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)

        if dp[-1] == amount + 1:
            return -1
        return dp[-1]


abc = Solution()
print (abc.coinChange([1,2,5], 11))
print (abc.coinChange([2], 3))
print (abc.coinChange([1], 3))
print (abc.coinChange([1,2], 3))
print (abc.coinChange([4,10,10,23], 24))