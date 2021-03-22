"""
tags : Facebook, Medium, array
URL : https://leetcode.com/problems/contiguous-array/
"""
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        
        dct = {0 : -1}
        
        max_ans = 0
        
        total_sum = 0
        
        for idx, x in enumerate(nums):
            
            if x == 1:
                total_sum += 1
            else:
                total_sum -= 1
            
            if total_sum in dct:
                max_ans = max(max_ans, (idx - dct[total_sum]))
            else:
                dct[total_sum] = idx
        
        return max_ans

abc = Solution()
abc.findMaxLength([0,0,1,0,1,1])