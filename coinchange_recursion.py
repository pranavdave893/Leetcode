class Solution(object):
    def coinchange(self,coins, number):
        
        def get_change(coins, start, n):
            if n == 0:return 1

            if n < 0:return 0

            if start < 0 or start >= len(coins): return 0

            result = 0

            result += get_change(coins, start+1, n) + get_change(coins, start, n-coins[start])

            return result

        
        return get_change(coins, 0, number)

abc = Solution()
coins = [1,2,3]
number = 4
print abc.coinchange(coins, number)