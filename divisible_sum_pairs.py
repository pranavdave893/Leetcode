"""
Handy coding interview
https://www.hackerrank.com/challenges/divisible-sum-pairs/forum
"""

from collections import defaultdict

def divisible_sum(nums, K):

    dct = defaultdict(int)
    ans = 0

    for x in nums:
        mod = x % K

        ans += dct[(K-mod) % K]

        dct[mod] += 1
    
    print(ans)

divisible_sum([60, 60, 60, 60, 60, 10, 50, 10, 50], 60)

