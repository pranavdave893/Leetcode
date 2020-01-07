class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
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
            


        

abc = Solution()
print (abc.largestRectangleArea([2,1,5,6,2,3,2,2,1,1,1,1,1]))