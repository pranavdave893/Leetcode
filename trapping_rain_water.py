class Solution(object):
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





