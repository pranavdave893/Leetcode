class Solution(object):
    def trap_stack(self, x):
        """
        Stack based approch Space O(N) and Time O(N)
        """
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                            
                top = stack.pop()
                
                if not stack:
                    break
                    
                distance = i- stack[-1] - 1
                min_height = min(height[i], height[stack[-1]]) - height[top]
                
                ans += distance*min_height
            
            stack.append(i)
        return ans

        """
        stack = []
        water = 0
        for idx, e in enumerate(height):
            
            while stack and e >= stack[-1][0]:
                
                top, _ = stack.pop()
                
                if not stack:
                    break
                    
                left_boundry, left_distance  = stack[-1]
                
                height = min(left_boundry, e) - top
                
                distance = idx - left_distance - 1
                
                water += distance*height
            
            stack.append((e, idx))
        return water
        """
    
    def trap(self, x):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(x) - 1

        left_max = 0
        right_max = 0
        answer = 0

        while left < right:
            if x[left] < x[right]:
                if x[left] >= left_max:
                    left_max = x[left]
                else:
                    answer += left_max - x[left]
                
                left += 1
            else:
                if x[right] >= right_max:
                    right_max = x[right]
                else:
                    answer += right_max - x[right]

                right -= 1
        print(answer)

abc = Solution()
abc.trap([0,1,0,2,1,0,1,3,2,1,2,1])





