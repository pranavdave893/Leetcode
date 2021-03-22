from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse_number(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        k, n = k % len(nums), len(nums)
        
        if k:
            reverse_number(0, n-1)
            reverse_number(0, k-1)
            reverse_number(k, n-1)
        
        """
        O(N) space
        def rotate(self, nums, k):
            n = len(nums)
            k = k % n
            nums[:] = nums[n-k:] + nums[:n-k]
        """

abc = Solution()
abc.rotate([1, 2, 3, 4, 5, 6, 7], 3)