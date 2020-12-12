"""
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
"""
from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        res, sums = 0, 0
        dct = {0 : -1}

        for i in range(len(nums)):

            sums += nums[i]

            if -(k-sums) in dct:
                res = max(res, i-dct[-(k-sums)])
            if sums not in dct:
                dct[sums] = i
        print( res)

abc = Solution()
abc.maxSubArrayLen([1,-1,5,-2,3], 3)


            