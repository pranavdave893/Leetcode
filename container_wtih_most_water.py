"""
https://leetcode.com/problems/container-with-most-water/
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        max_area = 0
        
        while start < end:
            
            width = end - start
            length = min(height[start], height[end])
            
            area = width * length
            
            if area > max_area:
                max_area = area
            
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max_area