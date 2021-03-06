class Solution(object):
    def coinchange(self, coins, number):
        dp = [[0 for x in range(number+1)] for i in range(len(coins)+1)]
        dp[0][0] = 1
        
        for row in range(1, len(coins)+1):
            
            dp[row][0] = 1
            
            for col in range(1, number+1):
                curr_coin = coins[row-1]
                
                without_coin = dp[row-1][col]
                
                with_coin = dp[row][col - curr_coin] if col >= curr_coin else 0
                
                dp[row][col] = without_coin + with_coin
        
        return dp[len(coins)][number]

    def coinchnage_fast(self, coins, amount):
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        if dp[-1] == amount + 1:
            return -1
        return dp[-1]


abc = Solution()
coins = [1,2,5]
number = 11
print (abc.coinchange(coins, number))
print (abc.coinchnage_fast(coins, number))