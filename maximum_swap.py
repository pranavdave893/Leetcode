"""
Q: https://leetcode.com/problems/maximum-swap/submissions/
tags : Facebook, medium, array
"""

class Solution(object):
    def max_swap(self, nums):
        nums = [int(i) for i in str(nums)]
        
        xi, yi = 0, 0
        
        max_id = len(nums)-1
        
        for x in range(len(nums)-1, -1, -1):
            if nums[x] > nums[max_id]:
                max_id = x
            
            elif nums[x] < nums[max_id]:
                xi = x
                yi = max_id
        
        nums[xi], nums[yi] = nums[yi], nums[xi]
        
        return int("".join([str(x) for x in nums]))
    

    def maximumSwap(self, num):
        A = map(int, str(num))
        last = {x: i for i, x in enumerate(A)}
        
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, None) > i:
                    
                    A[i], A[last[d]] = A[last[d]], A[i]
                    
                    return int("".join(map(str, A)))
        return num

abc = Solution()
abc.max_swap(2763)