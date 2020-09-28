from typing import List
class Solution:

    def largestRectangleArea(self, height: List[int]) -> int:
        stack = [-1]
        height.append(0)
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h*w)
            stack.append(i)
        
        return ans
    

    def largestRectangleArea_divide(self, heights: List[int]) -> int:
        
        def divide(start:int, end:int) -> int:
            if start > end:
                return 0
            
            min_idx = start
            
            for idx in range(start, end+1):
                if heights[min_idx] > heights[idx]:
                    min_idx = idx
            
            return max(heights[min_idx] * (end - start + 1), max(divide(start, min_idx-1), divide(min_idx+1, end)))
        
        return divide(0, len(heights)-1)
            


        

abc = Solution()
print (abc.largestRectangleArea([6,7,5,2,4,5,9,3]))