"""
Q : https://leetcode.com/problems/product-of-array-except-self/
"""

class Solution:
    # Two Pass
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        
        output = []
        for i in range(n):
            output.append(p)
            p *= nums[i]
        
        p = 1
        for i in range(n-1, -1, -1):
            output[i] *= p
            p *= nums[i]
        
        return output
    
    
    # One pass
    def productExceptSelf_2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        lp = 1
        rp = 1
        
        lo = 0
        hi = n-1
        
        while lo < n:
            res[lo] *= lp
            res[hi] *= rp
            
            lp *= nums[lo]
            rp *= nums[hi]
            
            lo += 1
            hi -= 1
        
        return res


