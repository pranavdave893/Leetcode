"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/306427/Different-Python-solutions-with-thinking-process
"""
from typing import List
# O(n^2) # TLE 

def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n < 2: 
        return 0
    dp = [0 for _ in range(n)]
    for i in range(1, n):
        dp[i] = dp[i-1]
        for j in range(i):
            tmp = prices[i] - prices[j]
            tmp += dp[j-1] if j > 0 else 0
            dp[i] = max(dp[i], tmp)
    return dp[n-1]

"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/208241/Explanation-for-the-dummy-like-me.
"""

def maxProfit2(prices: List[int]) -> int:
    N = len(prices)-1
    buy, sell, profit = 0, 0, 0 
    i = 0

    while i < N:
        
        while i< N and prices[i+1] <= prices[i]:
            i += 1
        buy = prices[i]

        while i<N and prices[i+1] > prices[i]:
            i += 1
        
        sell = prices[i]

        profit += sell-buy
    return profit

print (maxProfit([7,1,5,3,6]))
print (maxProfit2([7,1,5,3,6]))


heap = []
for x, y in count.items():
    if len(heap) < topk:
        heapq.heappush(heap, (-y, x))
    
    if heap[0][0] <= -y:
        heapq.heappushpop(heap, (-y, x))

return [x[1] for x, y in heap]



